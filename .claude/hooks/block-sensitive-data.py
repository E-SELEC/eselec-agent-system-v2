#!/usr/bin/env python3
"""Claude Code PreToolUse hook: block accidental sensitive data writes."""

from __future__ import annotations

import json
import re
import sys
from pathlib import PurePosixPath, PureWindowsPath
from typing import Any


HOOK_EVENT = "PreToolUse"

SENSITIVE_PATH_RE = re.compile(
    r"(?i)(^|[\\/])("
    r"\.env(\..*)?|"
    r"credentials(\..*)?|"
    r"client[_-]?secret.*|"
    r".*(token|secret|private[_-]?key|access[_-]?key).*|"
    r".*\.(pem|key|p12|pfx)"
    r")$"
)

ALLOWLIST_PATH_RE = re.compile(r"(?i)(^|[\\/])\.env\.example$")

HIGH_CONFIDENCE_VALUE_RE = re.compile(
    "(?i)("
    + "|".join(
        [
            "-----" + r"BEGIN [A-Z ]*PRIVATE KEY" + "-----",
            "github" + r"_pat_[A-Za-z0-9_]{20,}",
            "gh" + r"[pousr]_[A-Za-z0-9_]{20,}",
            "xox" + r"[baprs]-[A-Za-z0-9-]{20,}",
            "AK" + r"IA[0-9A-Z]{16}",
            "AI" + r"za[0-9A-Za-z_\-]{20,}",
            "Bearer" + r"\s+[A-Za-z0-9._\-]{24,}",
        ]
    )
    + ")"
)

SENSITIVE_ASSIGNMENT_RE = re.compile(
    r"(?im)\b([A-Za-z0-9_]*(?:"
    r"api[_-]?key|"
    r"access[_-]?key|"
    r"secret|"
    r"token|"
    r"password|"
    r"passwd|"
    r"pwd|"
    r"private[_-]?key|"
    r"client[_-]?secret|"
    r"authorization|"
    r"webhook"
    r")[A-Za-z0-9_]*)\s*[:=]\s*[\"']?([^\"'\s#]+)"
)

BASH_SENSITIVE_WRITE_RE = re.compile(
    r"(?is)\b("
    r"git\s+add|"
    r"set-content|"
    r"add-content|"
    r"out-file|"
    r"new-item|"
    r"copy-item|"
    r"move-item|"
    r"cp|"
    r"mv|"
    r"echo|"
    r"printf"
    r")\b.*("
    r"\.env(\.[A-Za-z0-9_.-]+)?|"
    r"credentials|"
    r"client[_-]?secret|"
    r"token|"
    r"secret|"
    r"private[_-]?key|"
    r"\.pem|"
    r"\.key|"
    r"\.p12|"
    r"\.pfx"
    r")"
)

PLACEHOLDER_RE = re.compile(
    r"(?i)^("
    r"your_.*|"
    r"example.*|"
    r"placeholder.*|"
    r"changeme|"
    r"change_me|"
    r"replace_me|"
    r"redacted|"
    r"xxx+|"
    r"\*+|"
    r"<[^>]+>|"
    r"\$\{[^}]+\}"
    r")$"
)


def deny(reason: str) -> None:
    payload = {
        "hookSpecificOutput": {
            "hookEventName": HOOK_EVENT,
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    print(json.dumps(payload, ensure_ascii=False))


def normalize_path(value: str) -> str:
    if "\\" in value:
        return PureWindowsPath(value).as_posix()
    return PurePosixPath(value).as_posix()


def is_sensitive_path(value: str) -> bool:
    normalized = normalize_path(value)
    return bool(SENSITIVE_PATH_RE.search(normalized)) and not bool(
        ALLOWLIST_PATH_RE.search(normalized)
    )


def looks_like_placeholder(value: str) -> bool:
    cleaned = value.strip().strip("\"'")
    if not cleaned:
        return True
    return bool(PLACEHOLDER_RE.match(cleaned))


def collect_strings(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, str):
        found.append(value)
    elif isinstance(value, dict):
        for child in value.values():
            found.extend(collect_strings(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(collect_strings(child))
    return found


def collect_paths(tool_input: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for key in ("file_path", "path", "notebook_path"):
        value = tool_input.get(key)
        if isinstance(value, str):
            paths.append(value)
    return paths


def check_text(text: str) -> str | None:
    if HIGH_CONFIDENCE_VALUE_RE.search(text):
        return "Bloqueado: posible valor sensible de alta confianza en la llamada de herramienta."

    for match in SENSITIVE_ASSIGNMENT_RE.finditer(text):
        value = match.group(2)
        if not looks_like_placeholder(value):
            name = match.group(1)
            return f"Bloqueado: posible valor sensible asignado a `{name}`."

    return None


def check_payload(payload: dict[str, Any]) -> str | None:
    tool_name = str(payload.get("tool_name", ""))
    tool_input = payload.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        return None

    for path in collect_paths(tool_input):
        if is_sensitive_path(path):
            return f"Bloqueado: intento de tocar ruta sensible `{path}`."

    if tool_name.lower() == "bash":
        command = str(tool_input.get("command", ""))
        if BASH_SENSITIVE_WRITE_RE.search(command):
            return "Bloqueado: comando shell parece escribir, mover o versionar datos sensibles."

    for text in collect_strings(tool_input):
        reason = check_text(text)
        if reason:
            return reason

    return None


def run_self_test() -> int:
    cases = [
        (
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": "docs/example.md",
                    "content": "API_KEY=your_api_key",
                },
            },
            False,
        ),
        (
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": ".env",
                    "content": "PLACEHOLDER=example",
                },
            },
            True,
        ),
        (
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": "docs/example.md",
                    "content": "ESELEC_" + "TOKEN" + "=" + "abc123abc123",
                },
            },
            True,
        ),
        (
            {
                "tool_name": "Bash",
                "tool_input": {"command": "git add .env"},
            },
            True,
        ),
    ]

    failed = 0
    for index, (payload, should_block) in enumerate(cases, start=1):
        blocked = check_payload(payload) is not None
        if blocked != should_block:
            print(f"self-test {index} failed: blocked={blocked}", file=sys.stderr)
            failed += 1

    if failed:
        return 1

    print("self-test passed")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return run_self_test()

    raw = sys.stdin.read()
    if not raw.strip():
        return 0

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return 0

    reason = check_payload(payload)
    if reason:
        deny(reason)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
