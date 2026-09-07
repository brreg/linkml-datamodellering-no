#!/usr/bin/env python3
"""Delt JSON-RPC 2.0-over-stdio-mekanikk for MCP-serverane under src/mcp-*/.

Før dette modulet fanst implementerte alle tre server.py-filene
(mcp-linkml-validator, mcp-linkml-modell-utkast, mcp-linkml-begrep-utkast)
nesten identisk kode for: å skrive eit JSON-RPC-svar til stdout (`send`),
handtere `initialize`/`initialized`/`tools/list`/ukjend-verktøy/
metode-ikkje-funnen (`dispatch`), og lese meldingar linje for linje frå
stdin med feilhandtering (`run_stdio_loop`). Dette var over CLAUDE.md sin
eigen DRY-terskel (3+ identiske tilfelle) — sjå
`.claude/rules/mcp-server-python.md` og `specs/done/mcp-server-python-tiltak.md`
for grunngjeving.

Kvar server sin eigen `handle()`-funksjon byggjer no berre ein
`tool_handlers`-dict (verktøynamn → funksjon som tek `(msg_id, arguments)`
og returnerer eit fullstendig JSON-RPC-svar) og delegerer den generiske
protokolldelen til `dispatch()`. All tool-spesifikk forretningslogikk
(TOOL_*-definisjonar, `_handle_*`-funksjonar) er urørt og ligg framleis i
kvar server sin eigen `server.py`.

Modulet vert mounta/kopiert til `/app/utils` i alle tre serverkontainarane
og til `/repo/src/assets/scripts/utils` i batch-invokeringane som monterer
heile repoet (sjå `linkml_relative_import_patch.py` for same mønster) —
kvar server sin eigen `sys.path`-oppsett prøver begge kandidatane pluss ein
repo-relativ sti for køyring direkte frå eit git-checkout (t.d. testar som
importerer `server.py` utan container).
"""

import json
import sys
from typing import Callable, Optional


def send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def error_response(msg_id, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}}


def dispatch(
    msg: dict,
    *,
    tools: list,
    tool_handlers: dict,
    server_name: str,
    server_version: str = "1.0.0",
) -> Optional[dict]:
    """Handterer JSON-RPC-metodane som er identiske på tvers av alle MCP-serverane.

    tool_handlers: dict[str, Callable[[Any, dict], dict]] — verktøynamn →
    funksjon som tek (msg_id, arguments) og returnerer eit fullstendig
    JSON-RPC-svar (result- eller error-dict). Kvar server byggjer denne
    sjølv ut frå sine eigne _handle_*-funksjonar.
    """
    method = msg.get("method", "")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": server_name, "version": server_version},
            },
        }

    if method == "initialized":
        return None  # notifikasjon — ingen respons

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": tools}}

    if method == "tools/call":
        tool_name = (msg.get("params") or {}).get("name")
        arguments = (msg.get("params") or {}).get("arguments") or {}
        handler = tool_handlers.get(tool_name)
        if handler is None:
            return error_response(msg_id, -32602, f"Ukjent verktøy: {tool_name}")
        return handler(msg_id, arguments)

    return error_response(msg_id, -32601, f"Metode ikkje funnen: {method}")


def run_stdio_loop(handle_fn: Callable[[dict], Optional[dict]]) -> None:
    """Les JSON-RPC-meldingar linje for linje frå stdin og sender svar via send().

    Pakkar kvart handle_fn(msg)-kall i eit try/except slik at éin uventa
    exception i handteringa av éi melding ikkje tek ned resten av
    stdin-straumen — kritisk når fleire kall vert batcha inn i éin
    serverprosess (jf. batch-flatten-and-validate.py), sidan éin ubehandla
    exception elles ville drepe heile prosessen og miste resultatet for
    alle attverande jobbar.
    """
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError as exc:
            send(error_response(None, -32700, f"Parse-feil: {exc}"))
            continue

        try:
            response = handle_fn(msg)
        except Exception as exc:
            response = error_response(msg.get("id"), -32000, f"Uventa feil: {exc}")
        if response is not None:
            send(response)
