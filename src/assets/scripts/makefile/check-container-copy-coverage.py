#!/usr/bin/env python3
"""
Sjekk at delte moduler under src/assets/scripts/utils/ faktisk er tilgjengelege
i alle stader som treng dei — det konkrete hòlet som braut ekstern validering
via reusable-validate.yml (sjå specs/done/rule-full-kartlegging-manglar-
dockerfile-og-mcp-json.md og .claude/rules/container-images.md § «Ein ny
påkravd delt modul krev full kartlegging av alle monteringsstader»).

To uavhengige dekningssjekkar:

**A — Dockerfile.mcp-linkml sine COPY-lister.** Kvar `server.py` under
src/mcp-*/ som har eit `sys.path.insert(0, "/app/utils")`-mønster (den
etablerte konvensjonen for "denne serveren har ein hard avhengigheit til
src/assets/scripts/utils/") må høyre til eit Dockerfile-stadium der
`src/assets/scripts/utils/` faktisk er kopiert inn — anten direkte i
stadiet sjølv, eller arva frå eit `FROM <parent> AS <stadium>`-steg lenger
opp i kjeda (t.d. base-runtime).

**B — .github/workflows/reusable-*.yml sine sparse-checkout-lister.** Kvar
`src/assets/scripts/makefile/*.py`-script som vert sparse-checked-out OG
direkte køyrt (`python3 .../scriptnamn.py`) i ein reusable-workflow, og
som sjølv har eit `parent.parent / "utils"`-mønster (hard, ubetinga
avhengigheit til src/assets/scripts/utils/ — ikkje eit valfritt,
try/except-verna fallback-mønster), må ha `src/assets/scripts/utils` med i
same workflow sin sparse-checkout-liste.

**Kva dette IKKJE dekker** (jf. same avgrensing som check-cache-key-
coverage.py sin eigen docstring): scriptavhengigheiter utover
src/assets/scripts/utils/ (t.d. profiles/, policies/), og skript med eit
BEVISST valfritt/betinga monteringsmønster (t.d. flatten-and-validate.bash
sin UTILS_MOUNT-vakt) — desse er by design robuste mot ein manglande
katalog, og skal ikkje flaggast her. Dette skriptet fangar berre den
konkrete, faktisk observerte regresjonsklassen: ein HARD avhengigheit som
manglar sin eigen kopierings-/monteringsstad.

Ingen eksterne avhengigheiter (rein regex/tekstsøk — same tilnærming som
check-cache-key-coverage.py).

Bruk:
    python3 check-container-copy-coverage.py
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(".")
DOCKERFILE = REPO_ROOT / "src/assets/containers/Dockerfile.mcp-linkml"
WORKFLOW_DIR = REPO_ROOT / ".github/workflows"
UTILS_DIR = "src/assets/scripts/utils"

FROM_RE = re.compile(r"^FROM\s+(\S+)\s+AS\s+(\S+)\s*$", re.IGNORECASE)
COPY_RE = re.compile(r"^COPY\s+(?!--from=)(.+?)\s+\S+\s*$")
SERVER_HARD_UTILS_RE = re.compile(r'sys\.path\.insert\(0,\s*"/app/utils"\)')
SCRIPT_HARD_UTILS_RE = re.compile(r'parent\.parent\s*/\s*"utils"')
SPARSE_CHECKOUT_ITEM_RE = re.compile(r"^\s{4,}(\S.*)$")


# --- Del A: Dockerfile-stadium-dekning ------------------------------------


def parse_dockerfile_stages(text: str) -> dict[str, dict]:
    """Returnerer {stadium: {"parent": str|None, "own_copies": set[str]}}."""
    stages: dict[str, dict] = {}
    current = None
    for line in text.splitlines():
        m = FROM_RE.match(line.strip())
        if m:
            parent, name = m.group(1), m.group(2)
            stages[name] = {"parent": parent if parent in stages else None, "own_copies": set()}
            current = name
            continue
        m = COPY_RE.match(line.strip())
        if m and current:
            for src in m.group(1).split():
                if src.startswith("src/"):
                    stages[current]["own_copies"].add(src)
    return stages


def accumulated_copies(stages: dict[str, dict], stage: str) -> set[str]:
    seen: set[str] = set()
    name: str | None = stage
    while name is not None and name in stages:
        seen |= stages[name]["own_copies"]
        name = stages[name]["parent"]
    return seen


def stage_covers_utils(copies: set[str]) -> bool:
    return any(src.rstrip("/") == UTILS_DIR or src.startswith(UTILS_DIR + "/") for src in copies)


def check_dockerfile_coverage() -> list[str]:
    problems = []
    if not DOCKERFILE.is_file():
        return [f"Fann ikkje {DOCKERFILE} — hoppar over Dockerfile-sjekk (A)."]

    stages = parse_dockerfile_stages(DOCKERFILE.read_text(encoding="utf-8"))

    for server_py in sorted(REPO_ROOT.glob("src/mcp-*/server.py")):
        server_name = server_py.parent.name
        if not SERVER_HARD_UTILS_RE.search(server_py.read_text(encoding="utf-8")):
            continue  # denne serveren har ikkje ein hard utils-avhengigheit

        # Finn stadiet(a) som kopierer inn nettopp denne server.py-fila.
        matching_stages = [
            name
            for name, data in stages.items()
            if any(src == f"src/{server_name}/server.py" for src in data["own_copies"])
        ]
        if not matching_stages:
            problems.append(
                f"A: {server_py} har sys.path.insert(0, \"/app/utils\") (hard avhengigheit), "
                f"men vart ikkje funne kopiert inn i noko stadium i {DOCKERFILE}."
            )
            continue

        for stage in matching_stages:
            copies = accumulated_copies(stages, stage)
            if not stage_covers_utils(copies):
                problems.append(
                    f"A: {server_py} har sys.path.insert(0, \"/app/utils\") (hard avhengigheit), "
                    f"men Dockerfile-stadiet '{stage}' (og forfedrane sine COPY-linjer) dekker "
                    f"ikkje {UTILS_DIR}/. Legg til 'COPY {UTILS_DIR}/ utils/' i stadiet eller ein "
                    f"forfar det arvar frå."
                )
    return problems


# --- Del B: reusable-workflow sparse-checkout-dekning ----------------------


def extract_sparse_checkout_items(text: str) -> list[str]:
    items = []
    in_block = False
    for line in text.splitlines():
        if re.match(r"^\s*sparse-checkout:\s*\|?\s*$", line):
            in_block = True
            continue
        if in_block:
            m = SPARSE_CHECKOUT_ITEM_RE.match(line)
            if m:
                items.append(m.group(1).strip())
            else:
                in_block = False
    return items


def check_reusable_workflow_coverage() -> list[str]:
    problems = []
    if not WORKFLOW_DIR.is_dir():
        return []

    for workflow in sorted(WORKFLOW_DIR.glob("reusable-*.yml")):
        text = workflow.read_text(encoding="utf-8")
        sparse_items = extract_sparse_checkout_items(text)
        if not sparse_items:
            continue  # denne reusable workflowen hentar ikkje filer via sparse-checkout

        referenced_scripts = set(re.findall(r"src/assets/scripts/makefile/(\S+\.py)", text))
        for script_name in sorted(referenced_scripts):
            script_path = REPO_ROOT / "src/assets/scripts/makefile" / script_name
            if not script_path.is_file():
                continue
            if not SCRIPT_HARD_UTILS_RE.search(script_path.read_text(encoding="utf-8")):
                continue  # ingen hard utils-avhengigheit i dette scriptet

            covered = any(
                item.rstrip("/") == UTILS_DIR or item.startswith(UTILS_DIR + "/")
                for item in sparse_items
            )
            if not covered:
                problems.append(
                    f"B: {workflow} køyrer src/assets/scripts/makefile/{script_name} direkte "
                    f"(harde avhengigheit til {UTILS_DIR}/ via parent.parent/\"utils\"), men "
                    f"sparse-checkout-lista manglar {UTILS_DIR}."
                )
    return problems


def build_report(problems: list[str]) -> str:
    lines = ["# Container-/workflow-dekning for delte utils-moduler", ""]
    if not problems:
        lines.append(
            "Ingen avvik funne — alle harde utils-avhengigheiter (server.py sitt "
            '`sys.path.insert(0, "/app/utils")`, og reusable-workflow-script sitt '
            '`parent.parent / "utils"`) er dekte av tilhøyrande Dockerfile-COPY eller '
            "sparse-checkout-liste."
        )
        return "\n".join(lines)

    lines.append(f"**{len(problems)} avvik funne.**")
    lines.append("")
    for problem in problems:
        lines.append(f"- {problem}")
    return "\n".join(lines)


def main() -> None:
    problems = check_dockerfile_coverage() + check_reusable_workflow_coverage()
    print(build_report(problems))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
