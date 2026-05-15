#!/usr/bin/env python
"""Guard de cierre para el sistema E-SELEC v2.

Revisa artefactos recientes, posibles valores sensibles y accesos pendientes
antes de cerrar una tarea. No imprime valores completos.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT_MARKERS = ("AGENTS.md", "CLAUDE.md", "protocols", "registries")
DEFAULT_SINCE_HOURS = 24
REPORT_PATH = Path("outputs/system/protocol-guard-latest.md")

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}

SCAN_EXTENSIONS = {
    ".py",
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".txt",
}

SENSITIVE_PATTERNS = [
    (
        "named_sensitive_assignment",
        re.compile(
            r"(?i)\b(api[_-]?key|token|secret|password|passwd|consumer[_-]?secret|"
            r"client[_-]?secret|refresh[_-]?token|access[_-]?token|webhook[_-]?secret)"
            r"\b\s*[:=]\s*[\"']([^\"'\r\n]{8,})[\"']"
        ),
        2,
    ),
    ("openai_or_generic_sk", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"), 3),
    ("anthropic_key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b"), 3),
    ("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"), 3),
    ("google_api_key", re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"), 3),
    ("google_oauth_value", re.compile(r"\bya29\.[0-9A-Za-z_-]{20,}\b"), 3),
    ("slack_value", re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{20,}\b"), 3),
    ("huggingface_value", re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"), 3),
    ("woocommerce_key", re.compile(r"\b(?:ck|cs)_[a-f0-9]{32,}\b", re.I), 3),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"), 3),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"), 3),
]


@dataclass
class Finding:
    severity: str
    category: str
    path: str
    message: str
    action: str


def find_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if all((candidate / marker).exists() for marker in ROOT_MARKERS):
            return candidate
    return current


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def iter_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        base = Path(dirpath)
        for name in filenames:
            yield base / name


def is_scan_candidate(path: Path) -> bool:
    if path.name.startswith("protocol-guard-latest"):
        return False
    if path.name.lower() in {".env", ".mcp.json"}:
        return False
    suffix = path.suffix.lower()
    return suffix in SCAN_EXTENSIONS or path.name.lower().endswith((".env.example", ".env.local"))


def looks_like_example(value: str) -> bool:
    lower = value.lower()
    examples = (
        "your_",
        "example",
        "placeholder",
        "xxxx",
        "replace",
        "dummy",
        "redacted",
        "changeme",
        "none",
        "null",
        "local_value",
        "env_value",
    )
    return any(item in lower for item in examples)


def redact(value: str) -> str:
    cleaned = value.strip()
    if len(cleaned) <= 10:
        return "[redacted]"
    return f"{cleaned[:4]}...{cleaned[-4:]}"


def recently_modified_files(root: Path, since_hours: float, scan_all: bool) -> list[Path]:
    if scan_all:
        return sorted(iter_files(root))
    cutoff = dt.datetime.now().timestamp() - since_hours * 3600
    files: list[Path] = []
    for path in iter_files(root):
        try:
            if path.stat().st_mtime >= cutoff:
                files.append(path)
        except OSError:
            continue
    return sorted(files)


def git_changed_files(root: Path) -> list[Path] | None:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None

    files: list[Path] = []
    for raw in result.stdout.splitlines():
        if len(raw) < 4:
            continue
        path_text = raw[3:].strip()
        if " -> " in path_text:
            path_text = path_text.split(" -> ", 1)[1].strip()
        path = root / path_text
        if path.exists():
            files.append(path)
    return sorted(set(files))


def registry_text(root: Path) -> str:
    return read_text(root / "registries/registro-artefactos.md").lower().replace("\\", "/")


def registered_in_registry(relative: str, registry: str) -> bool:
    lower = relative.lower().replace("\\", "/")
    if lower in registry or Path(relative).name.lower() in registry:
        return True
    parts = lower.split("/")
    for index in range(1, len(parts)):
        parent = "/".join(parts[:index]) + "/"
        if parent in registry:
            return True
    return False


def manifest_for_output(path: Path, root: Path) -> Path | None:
    parts = rel(path, root).split("/")
    if len(parts) >= 4 and parts[0] == "clients" and parts[2] == "outputs":
        return root / parts[0] / parts[1] / parts[2] / "manifest.md"
    if len(parts) >= 3 and parts[0] == "agency" and parts[1] == "outputs":
        return root / parts[0] / parts[1] / "manifest.md"
    return None


def check_artifacts(root: Path, files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    registry = registry_text(root)
    global_prefixes = (
        ".claude/",
        "agency/",
        "clients/",
        "core/",
        "planning/",
        "protocols/",
        "quality/",
        "scripts/",
        "teams/",
    )
    global_files = {"agents.md", "claude.md", "readme.md", ".mcp.example.json"}

    for path in files:
        if path.is_dir():
            continue
        relative = rel(path, root)
        lower = relative.lower()
        if lower == REPORT_PATH.as_posix():
            continue
        if lower.startswith("registries/"):
            continue

        manifest = manifest_for_output(path, root)
        if manifest and path.name.lower() != "manifest.md":
            if not manifest.exists():
                findings.append(
                    Finding(
                        "bloqueo",
                        "artefactos",
                        relative,
                        "Output sin manifest.",
                        f"Crear {rel(manifest, root)} y registrar el archivo.",
                    )
                )
                continue
            manifest_text = read_text(manifest).lower().replace("\\", "/")
            if path.name.lower() not in manifest_text and lower not in manifest_text:
                findings.append(
                    Finding(
                        "alerta",
                        "artefactos",
                        relative,
                        "Output reciente no aparece en su manifest.",
                        f"Registrar en {rel(manifest, root)} o marcarlo como temporal.",
                    )
                )

        if lower in global_files or lower.startswith(global_prefixes):
            if lower.startswith("outputs/"):
                continue
            if not registered_in_registry(relative, registry):
                findings.append(
                    Finding(
                        "alerta",
                        "artefactos",
                        relative,
                        "Artefacto global reciente sin entrada clara en registro-artefactos.",
                        "Registrar ruta, motivo, estado y riesgo en registries/registro-artefactos.md.",
                    )
                )

    return findings


def check_sensitive_values(root: Path, files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        if not is_scan_candidate(path):
            continue
        try:
            if path.stat().st_size > 1_000_000:
                continue
        except OSError:
            continue

        text = read_text(path)
        if not text:
            continue
        relative = rel(path, root)

        for pattern_name, pattern, level in SENSITIVE_PATTERNS:
            for match in pattern.finditer(text):
                value = match.group(2) if pattern_name == "named_sensitive_assignment" else match.group(0)
                if looks_like_example(value):
                    continue
                findings.append(
                    Finding(
                        "bloqueo" if level >= 3 else "alerta",
                        "valores sensibles",
                        relative,
                        f"Posible valor sensible detectado ({pattern_name}): {redact(value)}",
                        "Mover a .env local o gestor externo, redactar el archivo y rotar si el valor fue real.",
                    )
                )
    return findings


def check_access_registry(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    path = root / "registries/registro-accesos.md"
    text = read_text(path)
    if not text:
        findings.append(
            Finding(
                "alerta",
                "accesos",
                rel(path, root),
                "No se pudo leer registro-accesos.md.",
                "Crear o reparar el registro antes de cerrar tareas con accesos.",
            )
        )
        return findings

    current_heading = "entrada sin titulo"
    current_level = ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("### "):
            current_heading = line[4:].strip()
            current_level = ""
        elif line.lower().startswith("- nivel:"):
            current_level = line.split(":", 1)[1].strip().upper()
        elif line.lower().startswith("- estado:"):
            state = line.split(":", 1)[1].strip().lower()
            if "pendiente de rotar" in state:
                severity = "bloqueo" if current_level == "S4" else "alerta"
                findings.append(
                    Finding(
                        severity,
                        "accesos",
                        rel(path, root),
                        f"Acceso pendiente de rotar: {current_heading} ({current_level or 'nivel no declarado'}).",
                        "Rotar/revocar el acceso o justificar por que sigue activo.",
                    )
                )
    return findings


def build_report(root: Path, findings: list[Finding], scanned_count: int, scope: str) -> str:
    status = "limpio"
    if any(f.severity == "bloqueo" for f in findings):
        status = "bloqueo"
    elif findings:
        status = "alerta"

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Protocol Guard v2",
        f"**Fecha:** {now}",
        f"**Estado:** {status}",
        f"**Alcance:** {scope}",
        f"**Archivos revisados:** {scanned_count}",
        "",
    ]

    if status == "limpio":
        lines += [
            "Revision limpia.",
            "",
            "No se detectaron artefactos sin registro, valores sensibles expuestos ni accesos pendientes.",
            "",
        ]
    elif status == "alerta":
        lines += ["Hay alertas que conviene corregir o registrar antes de cerrar.", ""]
    else:
        lines += ["Cierre bloqueado por riesgo sensible u operativo.", ""]

    grouped = {
        "artefactos": [f for f in findings if f.category == "artefactos"],
        "valores sensibles": [f for f in findings if f.category == "valores sensibles"],
        "accesos": [f for f in findings if f.category == "accesos"],
    }
    for title, items in grouped.items():
        lines.append(f"## {title.capitalize()}")
        if not items:
            lines.append("- limpio")
        for finding in items:
            lines.append(f"- [{finding.severity}] `{finding.path}`: {finding.message}")
            lines.append(f"  Accion: {finding.action}")
        lines.append("")

    lines.append("## Accion")
    if status == "limpio":
        lines.append("- cerrar")
    elif status == "alerta":
        lines.append("- corregir o registrar antes de cerrar")
    else:
        lines.append("- bloquear cierre hasta corregir o pedir aprobacion")
    lines.append("")
    return "\n".join(lines)


def write_report(root: Path, content: str) -> Path:
    report = root / REPORT_PATH
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(content, encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Guard de cierre operativo E-SELEC v2.")
    parser.add_argument("--root", default=".", help="Raiz del workspace. Por defecto, autodetecta desde cwd.")
    parser.add_argument("--since-hours", type=float, default=DEFAULT_SINCE_HOURS, help="Ventana de archivos recientes.")
    parser.add_argument("--recent", action="store_true", help="Revisar archivos modificados por tiempo en vez de cambios Git.")
    parser.add_argument("--all", action="store_true", help="Revisar todo el workspace.")
    parser.add_argument("--no-report", action="store_true", help="No escribir reporte markdown.")
    parser.add_argument("--strict", action="store_true", help="Tratar alertas como bloqueo en el codigo de salida.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = find_root(Path(args.root))
    if args.all:
        files = recently_modified_files(root, args.since_hours, True)
        scope = "todo el workspace"
    elif args.recent:
        files = recently_modified_files(root, args.since_hours, False)
        scope = f"ultimas {args.since_hours:g} horas"
    else:
        changed_files = git_changed_files(root)
        if changed_files is None:
            files = recently_modified_files(root, args.since_hours, False)
            scope = f"ultimas {args.since_hours:g} horas"
        else:
            files = changed_files
            scope = "cambios Git actuales"

    findings: list[Finding] = []
    findings.extend(check_artifacts(root, files))
    findings.extend(check_sensitive_values(root, files))
    findings.extend(check_access_registry(root))

    report = build_report(root, findings, len(files), scope)
    if not args.no_report:
        report_path = write_report(root, report)
        report += f"\nReporte: `{rel(report_path, root)}`\n"

    print(report)

    has_block = any(f.severity == "bloqueo" for f in findings)
    has_alert = bool(findings)
    if has_block or (args.strict and has_alert):
        return 2
    if has_alert:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
