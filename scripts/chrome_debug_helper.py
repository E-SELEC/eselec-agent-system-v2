"""Helper local para Chrome DevTools Protocol.

Uso principal:
  python scripts/chrome_debug_helper.py status
  python scripts/chrome_debug_helper.py open
  python scripts/chrome_debug_helper.py tabs
  python scripts/chrome_debug_helper.py scrape-chatgpt

No guarda cookies, tokens ni contenido scrapeado. Imprime el resultado en stdout.
Chrome 136+ bloquea CDP sobre el perfil real/default; por eso `open`
usa un perfil CDP separado por defecto.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import random
import socket
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 9222
DEFAULT_TIMEOUT = 5
DEFAULT_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHATGPT_HOSTS = ("chatgpt.com", "chat.openai.com")


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def fetch_json(url: str, timeout: float = DEFAULT_TIMEOUT) -> object:
    request = urllib.request.Request(url, headers={"User-Agent": "eselec-chrome-debug-helper"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def chrome_processes_running() -> bool:
    if os.name == "nt":
        result = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq chrome.exe", "/NH"],
            capture_output=True,
            text=True,
            check=False,
        )
        return "chrome.exe" in result.stdout.lower()

    result = subprocess.run(["pgrep", "-x", "chrome"], capture_output=True, check=False)
    return result.returncode == 0


def tabs(host: str, port: int) -> list[dict[str, object]]:
    data = fetch_json(f"http://{host}:{port}/json/list")
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict) and item.get("type") == "page"]


def wait_for_port(host: str, port: int, timeout: float) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if is_port_open(host, port, timeout=0.5):
            return True
        time.sleep(0.25)
    return False


def command_status(args: argparse.Namespace) -> int:
    port_ready = is_port_open(args.host, args.port)
    chrome_running = chrome_processes_running()

    print(f"Chrome corriendo: {'si' if chrome_running else 'no'}")
    print(f"CDP {args.host}:{args.port}: {'abierto' if port_ready else 'cerrado'}")

    if port_ready:
        try:
            page_count = len(tabs(args.host, args.port))
            print(f"Pestanas disponibles por CDP: {page_count}")
            return 0
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
            print(f"CDP responde, pero no pude listar pestanas: {exc}")
            return 1

    if chrome_running:
        print("Diagnostico: Chrome esta abierto, pero no hay endpoint CDP disponible.")
        print("Nota: Chrome 136+ ignora el debug remoto sobre perfiles reales/default.")
        print("Solucion: ejecuta `open` para abrir un perfil CDP separado.")
    else:
        print("Diagnostico: Chrome no esta abierto. Ejecuta `open`.")
    return 1


def command_open(args: argparse.Namespace) -> int:
    if is_port_open(args.host, args.port):
        print(f"Chrome ya esta disponible en {args.host}:{args.port}.")
        return 0

    chrome_path = Path(args.chrome_path)
    if not chrome_path.exists():
        print(f"No encontre Chrome en: {chrome_path}")
        print("Pasa la ruta con `--chrome-path`.")
        return 2

    chrome_args = [
        str(chrome_path),
        f"--remote-debugging-port={args.port}",
    ]

    if args.use_default_user_data_dir:
        if chrome_processes_running():
            print("Chrome ya esta abierto. No puedo activar CDP sobre una instancia existente.")
            print("Ademas, Chrome 136+ suele bloquear CDP sobre el perfil real/default.")
            return 2
        print("Aviso: `--use-default-user-data-dir` no es recomendado y puede no abrir CDP.")
    else:
        profile_dir = Path(args.user_data_dir) if args.user_data_dir else (
            Path(os.getenv("LOCALAPPDATA", Path.home())) / "ESELEC" / "chrome-debug-profile"
        )
        profile_dir.mkdir(parents=True, exist_ok=True)
        chrome_args.append(f"--user-data-dir={profile_dir}")

    if args.url:
        chrome_args.append(args.url)

    subprocess.Popen(chrome_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if wait_for_port(args.host, args.port, args.timeout):
        print(f"Chrome listo en {args.host}:{args.port}.")
        return 0

    print("Chrome se lanzo, pero el puerto CDP no respondio a tiempo.")
    return 1


def command_tabs(args: argparse.Namespace) -> int:
    if not is_port_open(args.host, args.port):
        print("CDP no esta disponible. Ejecuta `status` para ver el diagnostico.")
        return 1

    for index, page in enumerate(tabs(args.host, args.port), start=1):
        title = str(page.get("title", "")).strip()
        url = str(page.get("url", "")).strip()
        print(f"[{index}] {title}\n    {url}")
    return 0


class DevToolsWebSocket:
    def __init__(self, url: str, timeout: float = DEFAULT_TIMEOUT) -> None:
        parsed = urlparse(url)
        if parsed.scheme != "ws":
            raise ValueError("Solo se soportan URLs ws:// locales.")
        self.host = parsed.hostname or DEFAULT_HOST
        self.port = parsed.port or 80
        self.path = parsed.path
        if parsed.query:
            self.path += f"?{parsed.query}"
        self.timeout = timeout
        self.sock: socket.socket | None = None

    def __enter__(self) -> "DevToolsWebSocket":
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
        sock.settimeout(self.timeout)
        request = (
            f"GET {self.path} HTTP/1.1\r\n"
            f"Host: {self.host}:{self.port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        sock.sendall(request.encode("ascii"))
        response = sock.recv(4096)
        if b" 101 " not in response.split(b"\r\n", 1)[0]:
            raise ConnectionError("Chrome no acepto el WebSocket CDP.")
        self.sock = sock
        return self

    def __exit__(self, *_exc: object) -> None:
        if self.sock:
            self.sock.close()
            self.sock = None

    def _read_exact(self, length: int) -> bytes:
        if not self.sock:
            raise ConnectionError("WebSocket no conectado.")
        chunks = bytearray()
        while len(chunks) < length:
            chunk = self.sock.recv(length - len(chunks))
            if not chunk:
                raise ConnectionError("WebSocket cerrado por Chrome.")
            chunks.extend(chunk)
        return bytes(chunks)

    def send_json(self, payload: dict[str, object]) -> None:
        if not self.sock:
            raise ConnectionError("WebSocket no conectado.")
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        mask = struct.pack("!I", random.getrandbits(32))
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(body))
        header = bytearray([0x81])
        length = len(body)
        if length < 126:
            header.append(0x80 | length)
        elif length < 65536:
            header.extend([0x80 | 126])
            header.extend(struct.pack("!H", length))
        else:
            header.extend([0x80 | 127])
            header.extend(struct.pack("!Q", length))
        self.sock.sendall(bytes(header) + mask + masked)

    def receive_json(self) -> dict[str, object]:
        first, second = self._read_exact(2)
        opcode = first & 0x0F
        masked = bool(second & 0x80)
        length = second & 0x7F
        if length == 126:
            length = struct.unpack("!H", self._read_exact(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self._read_exact(8))[0]
        mask = self._read_exact(4) if masked else b""
        payload = self._read_exact(length)
        if masked:
            payload = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        if opcode == 0x8:
            raise ConnectionError("Chrome cerro el WebSocket CDP.")
        if opcode != 0x1:
            return self.receive_json()
        return json.loads(payload.decode("utf-8"))


def evaluate(page: dict[str, object], expression: str, timeout: float) -> object:
    ws_url = page.get("webSocketDebuggerUrl")
    if not isinstance(ws_url, str):
        raise ValueError("La pestana no expone webSocketDebuggerUrl.")

    message_id = 1
    with DevToolsWebSocket(ws_url, timeout=timeout) as ws:
        ws.send_json(
            {
                "id": message_id,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": expression,
                    "returnByValue": True,
                    "awaitPromise": True,
                },
            }
        )
        deadline = time.time() + timeout
        while time.time() < deadline:
            message = ws.receive_json()
            if message.get("id") != message_id:
                continue
            if "exceptionDetails" in message:
                raise RuntimeError(json.dumps(message["exceptionDetails"], ensure_ascii=False))
            result = message.get("result")
            if not isinstance(result, dict):
                return None
            value = result.get("result")
            if isinstance(value, dict):
                return value.get("value")
            return None
    raise TimeoutError("Timeout esperando respuesta CDP.")


def find_chatgpt_tab(pages: list[dict[str, object]], tab_index: int | None) -> dict[str, object] | None:
    if tab_index is not None:
        if 1 <= tab_index <= len(pages):
            return pages[tab_index - 1]
        return None

    for page in pages:
        url = str(page.get("url", "")).lower()
        if any(host in url for host in CHATGPT_HOSTS):
            return page
    return None


def command_scrape_chatgpt(args: argparse.Namespace) -> int:
    if not is_port_open(args.host, args.port):
        print("CDP no esta disponible. Ejecuta `status` para ver el diagnostico.")
        return 1

    pages = tabs(args.host, args.port)
    page = find_chatgpt_tab(pages, args.tab_index)
    if page is None:
        print("No encontre una pestana de ChatGPT por CDP.")
        print("Abre el chat en Chrome y ejecuta `tabs` para confirmar.")
        return 1

    expression = """
(() => {
  const root = document.querySelector('main') || document.querySelector('[role="main"]') || document.body;
  const text = root ? root.innerText : '';
  return { title: document.title, url: location.href, text };
})()
"""
    scraped = evaluate(page, expression, timeout=args.timeout)
    if not isinstance(scraped, dict):
        print("No pude extraer texto visible de la pestana.")
        return 1

    text = str(scraped.get("text", ""))
    if args.max_chars and len(text) > args.max_chars:
        text = text[: args.max_chars] + "\n\n[TRUNCADO]"

    if args.json:
        print(
            json.dumps(
                {
                    "title": scraped.get("title", ""),
                    "url": scraped.get("url", ""),
                    "text": text,
                    "sha256_16": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    print(f"TITLE: {scraped.get('title', '')}")
    print(f"URL: {scraped.get('url', '')}")
    print(f"SHA256_16: {hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]}")
    print("\nTEXT:\n")
    print(text)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Helper local para Chrome CDP / Playwright MCP.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="Diagnostica Chrome y el puerto CDP.")
    status.set_defaults(func=command_status)

    open_cmd = subparsers.add_parser("open", help="Abre Chrome con remote debugging.")
    open_cmd.add_argument("--chrome-path", default=os.getenv("CHROME_PATH", DEFAULT_CHROME))
    open_cmd.add_argument("--separate-profile", action="store_true", help="Compatibilidad: `open` ya usa perfil separado por defecto.")
    open_cmd.add_argument("--user-data-dir", help="Directorio de perfil CDP separado.")
    open_cmd.add_argument(
        "--use-default-user-data-dir",
        action="store_true",
        help="No recomendado; Chrome 136+ suele bloquear CDP sobre perfiles reales/default.",
    )
    open_cmd.add_argument("--url", help="URL inicial opcional.")
    open_cmd.set_defaults(func=command_open)

    tabs_cmd = subparsers.add_parser("tabs", help="Lista pestanas visibles por CDP.")
    tabs_cmd.set_defaults(func=command_tabs)

    scrape_cmd = subparsers.add_parser("scrape-chatgpt", help="Extrae texto visible de una pestana ChatGPT.")
    scrape_cmd.add_argument("--tab-index", type=int, help="Indice 1-based de `tabs`; por defecto busca ChatGPT.")
    scrape_cmd.add_argument("--max-chars", type=int, default=60000)
    scrape_cmd.add_argument("--json", action="store_true", help="Devuelve JSON en stdout.")
    scrape_cmd.set_defaults(func=command_scrape_chatgpt)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except KeyboardInterrupt:
        eprint("Cancelado.")
        return 130
    except Exception as exc:  # noqa: BLE001 - CLI debe explicar fallos de entorno local.
        eprint(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
