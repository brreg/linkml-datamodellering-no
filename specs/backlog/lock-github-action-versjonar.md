# Lås GitHub Action-versjonar konsekvent på tvers av repoet

## Bakgrunn

CI-loggen for `mermaid-click-href-sjekk` viste:

> Node.js 20 is deprecated. The following actions target Node.js 20 but are
> being forced to run on Node.js 24: actions/upload-artifact@v4.

Kartlegging av alle `uses:`-referansar i `.github/workflows/*.yml` og
`.github/actions/*/action.yml` (grep, sjå metodikk under) stadfestar
rotårsaka: eitt einskild avvik — `actions/upload-artifact@v4` i
`.github/workflows/lenkje-og-mermaid-sjekk.yml` line 307 («Last opp
click-href-rapport») — mot 15 andre stader som konsekvent brukar `@v7`.

**Fullstendig oversikt over tredjeparts-actions og versjonar i bruk i dag**
(15 filer skanna, ingen andre avvik funne):

| Action | Versjon(ar) i bruk | Tal treff |
|---|---|---|
| `actions/checkout` | v7 | 28 |
| `actions/upload-artifact` | v7 (15×), **v4 (1×, avvik)** | 16 |
| `actions/download-artifact` | v8 | 8 |
| `actions/cache` | v6 | 5 |
| `actions/deploy-pages` | v5 | 3 |
| `aquasecurity/trivy-action` | v0.36.0 | 2 |
| `googleapis/release-please-action` | v5 | 1 |
| `peter-evans/create-pull-request` | v8 | 1 |
| `github/codeql-action/upload-sarif` | v4 | 1 |
| `github/codeql-action/init` | v4 | 1 |
| `github/codeql-action/analyze` | v4 | 1 |
| `actions/upload-pages-artifact` | v5 | 1 |
| `actions/configure-pages` | v6 | 1 |

**Avklart val (chat):** Handhev konsistens via ei referansefil +
valideringsscript (ikkje eigne wrapper-composite-actions for kvar
tredjepartsaction). Grunngjeving: GitHub Actions støttar ikkje
variabel-substitusjon i `uses:`-linjer for tredjeparts actions (må vere ein
bokstaveleg streng ved parse-tid, jf. offisiell dokumentasjon og stadfesta
åtferd i dette repoet sine eksisterande workflow-filer), så ei "live" delt
kjelde er teknisk umogleg. Ei referansefil + valideringsscript er difor det
mest realistiske nivået av handheving — fangar avvik automatisk i CI,
sjølv om det ikkje strukturelt hindrar nokon i å skrive feil versjon i
utgangspunktet.

## Steg

1. Opprett `.github/action-versions.yml` — flat `<action>: <versjon>`-liste
   (éi linje per action, inkl. dei tre `github/codeql-action/*`-under-stiane
   separat, sidan dei er ulike `uses:`-mål sjølv om dei kjem frå same
   repo), basert på tabellen over (bruk `v7` for `upload-artifact`, ikkje
   det avvikande `v4`).
2. Opprett `.github/scripts/check-action-versions.py`:
   - Reint stdlib (ingen PyYAML/tredjepartsavhengigheit) — same filosofi
     som `mkdocs/lib/scripts/check-mermaid-click-hrefs.py`: regex-basert
     linjeskanning (`uses:`-verdiar har eit enkelt, konsistent format,
     treng ikkje full YAML-parsing), køyrbar direkte med `python3` utan
     container.
   - Les `.github/action-versions.yml` (enkel `key: value`-linje-parsing).
   - Skannar `.github/workflows/*.yml` og `.github/actions/*/action.yml`
     for `uses:`-verdiar, hoppar over `./`-prefikserte (våre eigne
     composite actions).
   - For kvar treff: rapporter som feil (a) dersom versjonen avvik frå
     referansefila, (b) dersom actionen vert brukt men manglar i
     referansefila (bør leggjast til der).
   - Skriv `::error file=<fil>::`-annotasjonar for kvart avvik (synleg i
     CI-loggen, jf. mønsteret frå `check-mermaid-click-hrefs.py`).
   - `exit 1` ved eitt eller fleire avvik — "ingen stille feil", jf.
     CLAUDE.md.
3. Rett det stadfesta avviket: `actions/upload-artifact@v4` →
   `actions/upload-artifact@v7` i
   `.github/workflows/lenkje-og-mermaid-sjekk.yml` line 307.
4. Opprett `.github/workflows/action-versjon-sjekk.yml` — enkel,
   lettvekts-workflow som triggerar på `pull_request`/`push` når
   `.github/workflows/**`, `.github/actions/**`,
   `.github/action-versions.yml` eller `.github/scripts/**` endrar seg;
   køyrer `python3 .github/scripts/check-action-versions.py` direkte
   (ingen podman/container naudsynt, reint stdlib-script).
5. `actionlint` på den nye workflow-fila (og på den endra
   `lenkje-og-mermaid-sjekk.yml`), obligatorisk etter CI-endring jf.
   CLAUDE.md.
6. Køyr scriptet lokalt (`python3 .github/scripts/check-action-versions.py`)
   mot heile repoet for å stadfeste 0 avvik etter retting av steg 3.

## Handlingsliste

- [ ] `.github/action-versions.yml` med alle 13 kjende action-versjonar
- [ ] `.github/scripts/check-action-versions.py` (stdlib, regex-basert)
- [ ] Rett `upload-artifact@v4` → `@v7` i `lenkje-og-mermaid-sjekk.yml`
- [ ] `.github/workflows/action-versjon-sjekk.yml`
- [ ] `actionlint` på nye/endra workflow-filer
- [ ] Lokal køyring av scriptet, stadfest 0 avvik
