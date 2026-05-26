#!/usr/bin/env python3
"""MCP-server for generering og validering av SKOS-AP-NO Begrep-instansar."""

import json
import sys
import tempfile
import yaml
from pathlib import Path


_PROFILES_DIR = Path(__file__).parent / "profiles"


def send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _list_profiles() -> list:
    profiles = []
    for path in sorted(_PROFILES_DIR.glob("*.yaml")):
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            profiles.append({"name": path.stem, "description": data.get("description", "")})
        except Exception:
            profiles.append({"name": path.stem, "description": ""})
    return profiles


# ---------------------------------------------------------------------------
# Verktøy-definisjonar
# ---------------------------------------------------------------------------

TOOL_OPPRETT_BEGREP = {
    "name": "opprett_begrep",
    "description": (
        "Genererer ein komplett BegrepContainer-YAML-blokk frå strukturerte parametrar. "
        "Følgjer SKOS-AP-NO-Begrep og mønsteret i specs/begrep-modellering.md. "
        "Bruk list_profiles for å sjå tilgjengelege profiler, "
        "og list_los_tema for gyldige fagomrade_uri-verdiar."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["slug", "anbefalt_term_nb", "definisjon_nb", "fagomrade_uri"],
        "properties": {
            "profil": {
                "type": "string",
                "description": "Profilnamn (standard: 'default'). Profilen set standardverdiar for URI-mønster og org-spesifikke felt.",
                "default": "default",
            },
            "base_uri": {
                "type": "string",
                "description": "Base-URI for organisasjonen, t.d. 'https://begrep.brreg.no'. Kan setjast av profilen.",
                "default": "",
            },
            "slug": {
                "type": "string",
                "description": "Kort identifikator for begrepet, t.d. 'foretaksnavn'.",
            },
            "anbefalt_term_nb": {
                "type": "string",
                "description": "Anbefalt term på bokmål.",
            },
            "anbefalt_term_nn": {
                "type": "string",
                "description": "Anbefalt term på nynorsk (valfri).",
                "default": "",
            },
            "anbefalt_term_en": {
                "type": "string",
                "description": "Anbefalt term på engelsk (valfri).",
                "default": "",
            },
            "definisjon_nb": {
                "type": "string",
                "description": "Definisjonstekst på bokmål.",
            },
            "definisjon_nn": {
                "type": "string",
                "description": "Definisjonstekst på nynorsk (valfri).",
                "default": "",
            },
            "definisjon_en": {
                "type": "string",
                "description": "Definisjonstekst på engelsk (valfri).",
                "default": "",
            },
            "kjelde_relasjon": {
                "type": "string",
                "description": "Kjeldetype. Kan setjast av profilen.",
                "enum": ["direct-from-source", "self-composed", "derived-from-source"],
                "default": "",
            },
            "utgjevar_uri": {
                "type": "string",
                "description": "URI til utgjevande organisasjon. Kan setjast av profilen.",
                "default": "",
            },
            "fagomrade_uri": {
                "type": "string",
                "description": "URI til LOS-tema. Bruk list_los_tema for gyldige verdiar.",
            },
            "kontaktpunkt_uri": {
                "type": "string",
                "description": "URI til kontaktpunkt-objekt. Sett av profil-standard om utelate.",
                "default": "",
            },
            "merknad": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Merknadstekstar (valfri).",
                "default": [],
            },
            "eksempel": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Eksempelstrengjer (valfri).",
                "default": [],
            },
            "sja_ogsa_omgrep": {
                "type": "array",
                "items": {"type": "string"},
                "description": "URI-ar til relaterte begreper (valfri).",
                "default": [],
            },
        },
    },
}

TOOL_VALIDER_BEGREP = {
    "name": "valider_begrep",
    "description": (
        "Validerer ei YAML-instansfil mot eit skos-ap-no-basert skjema. "
        "Skjemastien er relativ til /repo (repo-rota montert inn i containeren)."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["yaml_innhald", "skjema_sti"],
        "properties": {
            "yaml_innhald": {
                "type": "string",
                "description": "Heile innhaldet i instansfila som YAML-streng.",
            },
            "skjema_sti": {
                "type": "string",
                "description": (
                    "Sti til skjemafil relativt til /repo, "
                    "t.d. 'src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml'."
                ),
            },
        },
    },
}

TOOL_LIST_PROFILES = {
    "name": "list_profiles",
    "description": "Listar tilgjengelege profiler med namn og skildring.",
    "inputSchema": {
        "type": "object",
        "properties": {},
    },
}

TOOL_LIST_LOS_TEMA = {
    "name": "list_los_tema",
    "description": "Listar gyldige LOS-tema URI-ar med norske namn (statisk liste, ingen nettverkskall).",
    "inputSchema": {
        "type": "object",
        "properties": {},
    },
}


# ---------------------------------------------------------------------------
# Meldingshandtering
# ---------------------------------------------------------------------------

def handle(msg: dict) -> dict | None:
    method = msg.get("method", "")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "mcp-linkml-begrep-utkast", "version": "1.0.0"},
            },
        }

    if method == "initialized":
        return None

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": [
                    TOOL_OPPRETT_BEGREP,
                    TOOL_VALIDER_BEGREP,
                    TOOL_LIST_PROFILES,
                    TOOL_LIST_LOS_TEMA,
                ]
            },
        }

    if method == "tools/call":
        tool_name = (msg.get("params") or {}).get("name")
        arguments = (msg.get("params") or {}).get("arguments") or {}

        if tool_name == "list_profiles":
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(_list_profiles(), ensure_ascii=False)}
                    ]
                },
            }

        if tool_name == "list_los_tema":
            return _handle_list_los_tema(msg_id)

        if tool_name == "opprett_begrep":
            return _handle_opprett_begrep(msg_id, arguments)

        if tool_name == "valider_begrep":
            return _handle_valider_begrep(msg_id, arguments)

        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjent verktøy: {tool_name}"},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Metode ikkje funnen: {method}"},
    }


def _handle_list_los_tema(msg_id) -> dict:
    from los_tema import LOS_TEMA
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "content": [
                {"type": "text", "text": json.dumps(LOS_TEMA, ensure_ascii=False)}
            ]
        },
    }


def _handle_opprett_begrep(msg_id, arguments: dict) -> dict:
    from generator import load_profile, opprett_begrep

    profil_name = arguments.get("profil") or "default"

    try:
        profile = load_profile(profil_name)
    except FileNotFoundError:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjend profil: '{profil_name}'"},
        }

    slug          = arguments.get("slug", "")
    term_nb       = arguments.get("anbefalt_term_nb", "")
    def_nb        = arguments.get("definisjon_nb", "")
    fagomrade_uri = arguments.get("fagomrade_uri", "")

    if not slug:
        return _param_error(msg_id, "slug")
    if not term_nb:
        return _param_error(msg_id, "anbefalt_term_nb")
    if not def_nb:
        return _param_error(msg_id, "definisjon_nb")
    if not fagomrade_uri:
        return _param_error(msg_id, "fagomrade_uri")

    try:
        yaml_str = opprett_begrep(
            profile,
            slug=slug,
            anbefalt_term_nb=term_nb,
            definisjon_nb=def_nb,
            fagomrade_uri=fagomrade_uri,
            base_uri=arguments.get("base_uri", ""),
            kjelde_relasjon=arguments.get("kjelde_relasjon", ""),
            utgjevar_uri=arguments.get("utgjevar_uri", ""),
            anbefalt_term_nn=arguments.get("anbefalt_term_nn", ""),
            anbefalt_term_en=arguments.get("anbefalt_term_en", ""),
            definisjon_nn=arguments.get("definisjon_nn", ""),
            definisjon_en=arguments.get("definisjon_en", ""),
            kontaktpunkt_uri=arguments.get("kontaktpunkt_uri", ""),
            merknad=arguments.get("merknad") or [],
            eksempel=arguments.get("eksempel") or [],
            sja_ogsa_omgrep=arguments.get("sja_ogsa_omgrep") or [],
        )
    except ValueError as exc:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": str(exc)},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "content": [{"type": "text", "text": yaml_str}]
        },
    }


def _handle_valider_begrep(msg_id, arguments: dict) -> dict:
    yaml_innhald = arguments.get("yaml_innhald", "")
    skjema_sti   = arguments.get("skjema_sti", "")

    if not yaml_innhald:
        return _param_error(msg_id, "yaml_innhald")
    if not skjema_sti:
        return _param_error(msg_id, "skjema_sti")

    schema_path = Path("/repo") / skjema_sti
    if not schema_path.exists():
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Skjemafil finst ikkje: {schema_path}"},
        }

    try:
        instance = yaml.safe_load(yaml_innhald)
    except Exception as exc:
        result = {
            "gyldig": False,
            "feiltal": 1,
            "åtvaringtal": 0,
            "hendingar": [{"alvorlegheit": "error", "kode": "parse_error", "mål": "instance", "melding": str(exc)}],
        }
        return _ok(msg_id, result)

    try:
        from linkml_runtime.utils.schemaview import SchemaView
        from linkml.validator import validate as lm_validate
        from linkml.validator.report import Severity

        sv = SchemaView(str(schema_path))
        sv.merge_imports()

        target_class = None
        for cname, cls_def in (sv.schema.classes or {}).items():
            if cls_def.tree_root:
                target_class = cname
                break

        report = lm_validate(instance, sv.schema, target_class=target_class)

        _sev_map = {
            Severity.FATAL: "error",
            Severity.ERROR: "error",
            Severity.WARN:  "warning",
            Severity.INFO:  "info",
        }

        hendingar = []
        for r in report.results:
            sev = _sev_map.get(r.severity, "error")
            mal = r.instantiates or "instance"
            if r.instance_index is not None:
                mal = f"{mal}[{r.instance_index}]"
            hendingar.append({
                "alvorlegheit": sev,
                "kode": r.type or "validation_error",
                "mål": mal,
                "melding": r.message,
            })

    except Exception as exc:
        result = {
            "gyldig": False,
            "feiltal": 1,
            "åtvaringtal": 0,
            "hendingar": [{"alvorlegheit": "error", "kode": "validation_error", "mål": "schema", "melding": str(exc)}],
        }
        return _ok(msg_id, result)

    errors   = [h for h in hendingar if h["alvorlegheit"] == "error"]
    warnings = [h for h in hendingar if h["alvorlegheit"] == "warning"]
    result = {
        "gyldig":      len(errors) == 0,
        "feiltal":     len(errors),
        "åtvaringtal": len(warnings),
        "hendingar":   hendingar,
    }
    return _ok(msg_id, result)


def _ok(msg_id, data) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False, indent=2)}]
        },
    }


def _param_error(msg_id, param: str) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32602, "message": f"Påkravd parameter manglar: '{param}'"},
    }


# ---------------------------------------------------------------------------
# Hovudløkke
# ---------------------------------------------------------------------------

def main():
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError as exc:
            send({"jsonrpc": "2.0", "id": None,
                  "error": {"code": -32700, "message": f"Parse-feil: {exc}"}})
            continue

        response = handle(msg)
        if response is not None:
            send(response)


if __name__ == "__main__":
    main()
