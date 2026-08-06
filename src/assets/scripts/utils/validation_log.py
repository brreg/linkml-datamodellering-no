#!/usr/bin/env python3
"""Delt hjelpefunksjon for å byggje og skrive valideringslogg-JSON.

Konsoliderer feltnamna som `run-validation.sh` og `save-validation-log.py`
skriv til `validation/<versjon>/<policy>.json` (BUG-12: dei to skrivarane
brukte tidlegare ulike feltnamn — `validation_policy` vs `validation_type`,
med/utan `validated_at`). Begge skal no gå via denne modulen slik at
strukturen er identisk uansett kva kallstad som skreiv fila.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def build_validation_log_entry(
    schema_name: str,
    domain: str,
    version: str,
    policy: str,
    result: Dict[str, Any],
) -> Dict[str, Any]:
    """Bygg eit valideringslogg-objekt med konsistente feltnamn.

    `policy` er policy-namnet valideringa vart køyrd mot (bronze/silver/gold/
    felles-datakatalog/felles-begrepskatalog), eller — for
    `save-validation-log.py` sine ikkje-policy-kategoriar — ei tilsvarande
    kategorietikett (t.d. `examples`, `data-<catalog>`).
    """
    return {
        "schema": schema_name,
        "domain": domain,
        "version": version,
        "validation_policy": policy,
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "result": result,
    }


def write_validation_log(log_path: Path, entry: Dict[str, Any]) -> None:
    """Skriv valideringslogg-objektet til fil (opprettar overordna katalogar)."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        json.dumps(entry, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
