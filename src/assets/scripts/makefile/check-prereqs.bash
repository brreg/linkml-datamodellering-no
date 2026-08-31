#!/usr/bin/env bash
# Sjekkar at alle føresetnader for lokal utvikling er oppfylte.
# Designa for å køyrast standalone (bash check-prereqs.bash), utan at
# make/podman er installerte frå før — ikkje legg til ei reell
# make-avhengigheit (t.d. $(MAKE)-kall) i dette scriptet.
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

# Git
if command -v git &>/dev/null; then
  ok "Git tilgjengeleg ($(git --version))"
else
  fail "Git ikkje funne. Installer: sudo apt install git"
fi

# jq
if command -v jq &>/dev/null; then
  ok "jq tilgjengeleg ($(jq --version))"
else
  fail "jq ikkje funne. Installer: sudo apt-get update && sudo apt-get -y install jq"
fi

# Podman
if command -v podman &>/dev/null; then
  ok "Podman tilgjengeleg ($(podman --version))"
else
  fail "Podman ikkje funne. Installer: sudo apt-get update && sudo apt-get -y install podman"
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

# WSL2 mirrored nettverksmodus (podman sin pasta-bakend + WSL2 sin NAT-baserte
# localhost-videresending har eit kjent samspelsproblem — sjå COMMANDS.md §
# docs-serve). Berre relevant i WSL2.
if grep -qi microsoft /proc/version 2>/dev/null; then
  if command -v wslinfo &>/dev/null; then
    NET_MODE=$(wslinfo --networking-mode 2>/dev/null || echo "ukjend")
    if [ "$NET_MODE" = "mirrored" ]; then
      ok "WSL2 nettverksmodus er 'mirrored'"
    else
      warn "WSL2 nettverksmodus er '${NET_MODE}', ikkje 'mirrored'. http://localhost:<port> (t.d. 'make docs-serve') kan feile i nettlesaren på Windows-verten. Fiks: legg til 'networkingMode=mirrored' under [wsl2] i C:\\Users\\<brukar>\\.wslconfig, køyr 'wsl --shutdown' frå Windows PowerShell, og start WSL2 på nytt. Sjå COMMANDS.md § docs-serve."
    fi
  else
    warn "Kan ikkje avgjere WSL2 nettverksmodus ('wslinfo' ikkje funne — krev nyare WSL2-versjon). Om http://localhost:<port> (t.d. 'make docs-serve') ikkje fungerer i nettlesaren på Windows-verten, sjå COMMANDS.md § docs-serve for mirrored-modus-fiks."
  fi
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
