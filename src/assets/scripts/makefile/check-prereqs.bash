#!/usr/bin/env bash
# Sjekkar at alle føresetnader for lokal utvikling er oppfylte.
set -euo pipefail

OK=0
WARN=0
FAIL=0

ok()   { echo "  ✓ $1"; ((OK++))   || true; }
warn() { echo "  ⚠ $1"; ((WARN++)) || true; }
fail() { echo "  ✗ $1"; ((FAIL++)) || true; }

echo ""
echo "=== make check-prereqs ==="
echo ""

# GNU make
if make --version 2>/dev/null | grep -q "GNU Make"; then
  ok "GNU make tilgjengeleg ($(make --version | head -1))"
else
  fail "GNU make ikkje funne. Installer: sudo apt install make"
fi

# Podman
if command -v podman &>/dev/null; then
  ok "Podman tilgjengeleg ($(podman --version))"
else
  fail "Podman ikkje funne. Sjå: https://podman.io/getting-started/installation"
fi

# Podman rootless
if podman run --rm --quiet alpine echo ok &>/dev/null; then
  ok "Podman rootless fungerer"
else
  fail "Podman rootless fungerer ikkje. Prøv: podman system migrate"
fi

# /etc/subuid og /etc/subgid
USER_NAME=$(id -un)
if grep -q "^${USER_NAME}:" /etc/subuid 2>/dev/null && grep -q "^${USER_NAME}:" /etc/subgid 2>/dev/null; then
  ok "User namespace-mapping konfigurert (/etc/subuid + /etc/subgid)"
else
  warn "User namespace-mapping manglar for '${USER_NAME}'. Prøv: sudo usermod --add-subuids 100000-165535 --add-subgids 100000-165535 ${USER_NAME}"
fi

# WSL2
if grep -qi microsoft /proc/version 2>/dev/null; then
  ok "WSL2-miljø oppdaga"
else
  warn "Ikkje WSL2 — skript er primært testa i WSL2, men kan fungere på vanleg Linux"
fi

# Diskplass (>= 5 GB)
AVAIL_GB=$(df -BG . 2>/dev/null | awk 'NR==2 {gsub("G",""); print int($4)}')
if [ "${AVAIL_GB:-0}" -ge 5 ]; then
  ok "Tilstrekkeleg diskplass (${AVAIL_GB} GB ledig)"
else
  fail "For lite diskplass (${AVAIL_GB:-?} GB ledig, treng minst 5 GB)"
fi

echo ""
printf "  OK: %d  Åtvaringar: %d  Feil: %d\n" "$OK" "$WARN" "$FAIL"
echo ""

if [ "$FAIL" -gt 0 ]; then
  echo "  → Rett feilane ovanfor før du går vidare."
  exit 1
fi
