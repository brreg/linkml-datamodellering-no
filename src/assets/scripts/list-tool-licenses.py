#!/usr/bin/env python3
"""Kartlegg direkte verktøyavhengigheiter i repoet (Dockerfile*, requirements*.txt,
.github/workflows/*.yml) for lisensoversikten i specs/done/verktoy-lisensoversikt.md.

Lisensfelt må verifiseres manuelt mot offisiell kjelde — dette skriptet
finner berre *kva* verktøy som er i bruk og *kor* dei er referert.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def join_continuations(text):
    """Collapse backslash line-continuations so multi-line RUN statements
    become single logical lines for regex matching."""
    return re.sub(r"\\\s*\n\s*", " ", text)


def find_dockerfile_tools():
    tools = []
    for dockerfile in sorted(REPO_ROOT.glob("**/Dockerfile*")):
        if "node_modules" in dockerfile.parts:
            continue
        raw = dockerfile.read_text()
        text = join_continuations(raw)
        rel = dockerfile.relative_to(REPO_ROOT)
        for m in re.finditer(r"^FROM\s+(\S+)", raw, re.MULTILINE):
            tools.append((str(rel), "base-image", m.group(1)))
        for m in re.finditer(r"pip install\s+([^\n]*)", text):
            line = m.group(1)
            for tok in line.split():
                tok = tok.strip("\"'")
                if tok.startswith("-") or tok.startswith("/") or tok.startswith("requirements"):
                    continue
                pkg = re.split(r"[><=!~\[]", tok)[0].strip()
                if pkg:
                    tools.append((str(rel), "pip", pkg))
        for m in re.finditer(r"apt-get install\s+([^\n]*)", text):
            line = m.group(1).split("&&")[0]
            for tok in line.split():
                if tok.startswith("-"):
                    continue
                tools.append((str(rel), "apt", tok))
    return tools


def find_requirements_tools():
    tools = []
    for req in sorted(REPO_ROOT.glob("**/requirements*.txt")):
        rel = req.relative_to(REPO_ROOT)
        for line in req.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            pkg = re.split(r"[><=!~\[]", line)[0].strip()
            if pkg:
                tools.append((str(rel), "pip", pkg))
    return tools


def find_workflow_tools():
    tools = []
    for wf in sorted(REPO_ROOT.glob(".github/workflows/*.yml")):
        rel = wf.relative_to(REPO_ROOT)
        for m in re.finditer(r"uses:\s*(\S+)", wf.read_text()):
            tools.append((str(rel), "github-action", m.group(1)))
    return tools


def find_makefile_images():
    tools = []
    makefile = REPO_ROOT / "Makefile"
    if makefile.exists():
        for m in re.finditer(r"_IMAGE\s*:?=\s*(\S+)", makefile.read_text()):
            image = m.group(1)
            if image.startswith("localhost/"):
                continue  # lokal build-tag, ikkje eit separat oppstrøms-verktøy
            if image.count("/") or ":" in image:
                tools.append(("Makefile", "base-image", image))
    return tools


def dedupe(rows):
    seen = {}
    for source, kind, name in rows:
        key = name
        seen.setdefault(key, {"kind": kind, "sources": set()})
        seen[key]["sources"].add(source)
    return seen


def main():
    rows = (
        find_dockerfile_tools()
        + find_requirements_tools()
        + find_workflow_tools()
        + find_makefile_images()
    )
    merged = dedupe(rows)
    for name in sorted(merged):
        info = merged[name]
        sources = ", ".join(sorted(info["sources"]))
        print(f"{name}\t{info['kind']}\t{sources}")


if __name__ == "__main__":
    sys.exit(main())
