#!/usr/bin/env bash
# Slår opp catalog_slug for ein organisasjons-alias i CODEOWNERS.md sin
# YAML-frontmatter. Brukt av validate-modellkatalog-instance for å
# akseptere same alias-form som new-modellkatalog/gen-modelldcat-elements
# (sjå specs/done/valider-modellkatalog-org-alias.md).
# Bruk: bash src/assets/scripts/scaffolding/resolve-catalog-slug.sh <alias>
set -euo pipefail

ALIAS="${1:-}"

if [[ -z "$ALIAS" ]]; then
    echo "Feil: alias er påkravd." >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
CODEOWNERS="$REPO_ROOT/CODEOWNERS.md"

if [[ ! -f "$CODEOWNERS" ]]; then
    echo "Feil: Fann ikkje CODEOWNERS.md i repo-rota." >&2
    exit 1
fi

python3 - "$ALIAS" "$REPO_ROOT" << 'PYEOF'
import sys
from pathlib import Path

alias = sys.argv[1]
repo_root = Path(sys.argv[2])

sys.path.insert(0, str(repo_root / "src" / "assets" / "scripts"))
from utils.codeowners import load_codeowners  # noqa: E402

orgs = {o["alias"]: o for o in load_codeowners(repo_root)}

if alias not in orgs:
    print(f"Feil: Alias '{alias}' ikkje funne i CODEOWNERS.md. Gyldige aliasar: {', '.join(sorted(orgs))}", file=sys.stderr)
    sys.exit(1)

print(orgs[alias]["catalog_slug"])
PYEOF
