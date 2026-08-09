#!/usr/bin/env bash
# Delt hjelpefunksjon for å køyre python3-kall i mkdocs-pipelinen via
# python-pytest-kontaineren (har PyYAML installert) i staden for python3
# direkte på hosten. Sjå specs/backlog/nye-host-python-kall-batching.md
# (Funn 3) for grunngjeving.
set -euo pipefail

MKDOCS_PYTHON_IMAGE="${MKDOCS_PYTHON_IMAGE:-localhost/python-pytest:latest}"

# to_container_path <host-absolutt-sti under REPO_ROOT>
# Konverterer ein REPO_ROOT-relativ absolutt sti til tilsvarande /work-sti
# inne i kontaineren (jf. -v "$REPO_ROOT:/work:ro"-mounten i
# run_python_container).
to_container_path() {
    local path="$1"
    printf '/work%s' "${path#"$REPO_ROOT"}"
}

# run_python_container [python3-argument ...]
# Køyr python3 inne i python-pytest-kontaineren med REPO_ROOT mounta
# read-only som /work. Kode/skript sendast som vanleg via -c-argument eller
# stdin-heredoc ("- <<'PYEOF' ... PYEOF") — kallar konverterer sjølv
# filsti-argument til /work-stiar via to_container_path først.
run_python_container() {
    podman run -i --rm \
        -v "$REPO_ROOT:/work:ro" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$MKDOCS_PYTHON_IMAGE" \
        python3 "$@"
}
