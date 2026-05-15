#!/usr/bin/env python
"""Scrape official Claude Code docs listed in fuentes-claude-code.md.

The scraper stores Markdown pages locally so the alignment agent can verify
rules against official sources before making strong recommendations.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
DEFAULT_SOURCES = REFERENCES / "fuentes-claude-code.md"
DEFAULT_OUT = REFERENCES / "claude-docs"

URL_RE = re.compile(r"https://code\.claude\.com/docs/[^\s)]+")
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
SECRET_PATTERNS = [
    re.compile(
        r"(?i)(\b(?:api[_-]?key|token|secret|password|passwd|consumer[_-]?secret|"
        r"client[_-]?secret|refresh[_-]?token|access[_-]?token|webhook[_-]?secret)"
        r"\b\s*[:=]\s*[\"'])([^\"'\r\n]{8,})([\"'])"
    ),
    re.compile(r"sk-ant-[A-Za-z0-9_-]{12,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"ya29\.[0-9A-Za-z_-]{20,}"),
    re.compile(r"xox[baprs]-[0-9A-Za-z-]{20,}"),
]


def parse_sources(path: Path) -> list[tuple[str, str]]:
    category = "Sin categoria"
    found: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            category = line[3:].strip()
            continue
        for url in URL_RE.findall(line):
            found.append((category, url.rstrip(".,;")))
    return found


def markdown_url(url: str) -> str:
    fetch = url
    if not fetch.endswith((".txt", ".md")):
        fetch = f"{fetch}.md"
    return fetch


def fetch_url(url: str) -> tuple[str, str, int]:
    fetch = markdown_url(url)
    response = requests.get(
        fetch,
        timeout=45,
        headers={"User-Agent": "E-SELEC-alignment-check/1.0"},
    )
    response.encoding = "utf-8"
    if response.status_code == 404 and "/docs/es/" in fetch:
        fallback = fetch.replace("/docs/es/", "/docs/en/", 1)
        fallback_response = requests.get(
            fallback,
            timeout=45,
            headers={"User-Agent": "E-SELEC-alignment-check/1.0"},
        )
        fallback_response.encoding = "utf-8"
        if fallback_response.status_code < 400:
            return fallback, fallback_response.text, fallback_response.status_code
    return fetch, response.text, response.status_code


def sanitize(text: str) -> str:
    cleaned = text
    for pattern in SECRET_PATTERNS:
        if pattern.groups >= 3:
            cleaned = pattern.sub(r"\1[REDACTED_EXAMPLE_SECRET]\3", cleaned)
        else:
            cleaned = pattern.sub("[REDACTED_EXAMPLE_SECRET]", cleaned)
    return cleaned


def title_for(markdown: str, fallback: str) -> str:
    match = TITLE_RE.search(markdown)
    if match:
        return match.group(1).strip()
    return fallback


def local_path_for(out_dir: Path, url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path
    if path.startswith("/docs/"):
        path = path[len("/docs/") :]
    if path.endswith(".txt"):
        relative = Path(path)
    else:
        relative = Path(f"{path}.md" if not path.endswith(".md") else path)
    return out_dir / relative


def write_page(path: Path, original_url: str, fetched_url: str, category: str, status: int, content: str) -> dict[str, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    safe = sanitize(content).replace("\r\n", "\n")
    digest = hashlib.sha256(safe.encode("utf-8")).hexdigest()[:16]
    title = title_for(safe, path.stem)
    body = "\n".join(
        [
            "---",
            f"source_url: {original_url}",
            f"fetched_url: {fetched_url}",
            f"category: {category}",
            f"status: {status}",
            f"scraped_at: {now}",
            f"sha256_16: {digest}",
            "sanitized: true",
            "---",
            "",
            safe.strip(),
            "",
        ]
    )
    path.write_text(body, encoding="utf-8", newline="\n")
    return {
        "title": title,
        "local": path.as_posix(),
        "source": original_url,
        "fetched": fetched_url,
        "category": category,
        "status": str(status),
        "sha": digest,
    }


def write_manifest(out_dir: Path, rows: list[dict[str, str]]) -> None:
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    manifest = out_dir / "manifest.md"
    lines = [
        "# Manifest Claude Code docs scrapeadas",
        "",
        f"- Generado: {now}",
        f"- Total URLs: {len(rows)}",
        "- Uso: fuente local oficial para el agente `alineacion`.",
        "- Nota: los ejemplos con formato de secreto se redactan como `[REDACTED_EXAMPLE_SECRET]`.",
        "",
        "| Estado | Categoria | Titulo | Local | URL | Fetch |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        local_rel = Path(row["local"]).relative_to(out_dir).as_posix()
        title = row["title"].replace("|", "\\|")
        category = row["category"].replace("|", "\\|")
        lines.append(f"| {row['status']} | {category} | {title} | `{local_rel}` | {row['source']} | {row['fetched']} |")
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape official Claude Code docs to local Markdown.")
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--delay", type=float, default=0.05)
    args = parser.parse_args()

    sources = parse_sources(args.sources)
    args.out.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    failures: list[str] = []
    seen: set[str] = set()

    for category, url in sources:
        if url in seen:
            continue
        seen.add(url)
        local_path = local_path_for(args.out, url)
        try:
            fetched, content, status = fetch_url(url)
            rows.append(write_page(local_path, url, fetched, category, status, content))
            if status >= 400:
                failures.append(f"{status} {url}")
        except Exception as exc:  # noqa: BLE001 - report and continue all URLs.
            failures.append(f"ERR {url}: {exc}")
            rows.append(
                write_page(
                    local_path,
                    url,
                    url,
                    category,
                    0,
                    f"# Error al descargar\n\n{exc}\n",
                )
            )
        time.sleep(args.delay)

    write_manifest(args.out, rows)

    print(f"Scraped {len(rows)} URLs into {args.out}")
    if failures:
        print("Failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
