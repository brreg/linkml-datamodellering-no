# Auto-oppdatering av datoannotasjonar ved release

## Bakgrunn

`annotations.endringsdato` og `annotations.utgivelsesdato` i skjema-YAML-filene er i dag
sette manuelt. Det er lett å gløyme å oppdatere `endringsdato` ved kvar release, og
`utgivelsesdato` vert aldri systematisk sett for nye modellar.

release-please handterer allereie automatisk versjonsbump via `extra-files` i
`release-please-config.json`. Men det finst inga tilsvarande mekanisme for dynamiske
datoar — release-please kan berre sette faste verdiar, ikkje dagens dato.

Løysinga er eit post-release-steg i `release-please.yml` som oppdaterer datoane etter
at release-please har laga ein release.

---

## Regler

| Felt | Når | Logikk |
|---|---|---|
| `annotations.endringsdato` | Kvar release | Set til dagens dato (ISO 8601) |
| `annotations.utgivelsesdato` | Berre første gong | Set til dagens dato viss feltet ikkje finst frå før |

Skjema utan `annotations:`-seksjon vert hoppa over.
Skjema som har `annotations:` men manglar `endringsdato` → legg til feltet.
Skjema som har `annotations.utgivelsesdato` allereie → bevar verdien (ikkje overskriv).

---

## Tiltak

| # | Tiltak | Avhengigheit | Prioritet |
|---|---|---|---|
| 1 ✓ | Python-script `src/assets/scripts/update-schema-dates.py` | — | Høg |
| 2 ✓ | Utvid `release-please.yml` med `update-dates`-jobb | Tiltak 1 | Høg |

---

## Steg 1 — Python-script `update-schema-dates.py` ✓

Oppretta `src/assets/scripts/update-schema-dates.py`.

**Inndata:**
- `--released-paths <JSON>` — JSON-array med pakke-stiar (valfri; les manifest-diff mot `HEAD~1` viss utelaten)
- `--config <fil>` — sti til `release-please-config.json` (default: `release-please-config.json`)
- `--dry-run` — vis kva som ville vorte endra utan å skrive

**Implementert logikk per pakke-sti:**

1. Slå opp sti i `release-please-config.json` → finn `extra-files[0].path` (schema YAML)
2. Sjekk at `^annotations:` finst på toppnivå (regex, ikkje substring — skjema med berre klassenivå-annotations vert hoppa over)
3. Viss `endringsdato:` finst → erstat dato-verdien; elles legg til etter `^annotations:\n`
4. Viss `utgivelsesdato:` manglar → legg til etter `endringsdato:`-linja
5. Skriv tilbake til filen

**Avvik frå plan:** scriptet har også ein `find_released_packages()`-funksjon som les
manifest-diff mot `HEAD~1` viss `--released-paths` ikkje er oppgjeve. Workflow-en
brukar denne fallback-mekanismen i staden for `paths_released`-outputtet (sjå steg 2).

---

## Steg 2 — Utvid `release-please.yml` med `update-dates`-jobb ✓

Lagt til `id: release-please` på det eksisterande steget og `outputs:`-blokk på jobben.
Ny `update-dates`-jobb som køyrer berre når `releases_created == 'true'`.

**Avvik frå plan:** scriptet les manifest-diff (`HEAD~1` vs `HEAD`) internt i staden
for å motta `paths_released` frå release-please-outputtet. Dette gjer implementeringa
meir robust mot framtidige endringar i release-please-action sitt output-API.
`fetch-depth: 2` er sett på checkout slik at `HEAD~1` er tilgjengeleg.

---

## Avhengigheiter

- `release-please-action@v5` (allereie i bruk) — eksponerer `releases_created`
- Python 3 (pre-installert på `ubuntu-22.04`)
- Ingen nye containerar eller pakkeavhengigheiter

---

## Verifisering

Etter implementering:
1. Lag ein `feat(<modell>): ...`-commit og push til `main`
2. Merge den resulterende release-PR
3. Sjekk at `update-dates`-jobben køyrer i Actions
4. Sjekk at `endringsdato` er oppdatert til releasedatoen i schema-YAML-filen
5. For ein modell utan `utgivelsesdato`: sjekk at feltet er lagt til
6. For ein modell som allereie har `utgivelsesdato`: sjekk at verdien er uendra

---

## Utført

Utført 2026-06-19.

**Tiltak 1 — `update-schema-dates.py`:** Ny Python-script i `src/assets/scripts/`.
Brukar stdlib-regex utan eksterne avhengigheiter. Sjekkar for toppnivå `^annotations:`
med regex (ikkje substring) for å unngå falske treff på klassenivå-annotations.
Legg til `endringsdato` og `utgivelsesdato` om dei manglar; bevarar eksisterande
`utgivelsesdato`. Har `--dry-run`-støtte og `find_released_packages()`-fallback.

**Tiltak 2 — `release-please.yml`:** Lagt til `id: release-please`, `outputs:
releases_created`-blokk på `release-please`-jobben og ny `update-dates`-jobb.
`update-dates` køyrer med `fetch-depth: 2` og `contents: write`, og committer
`chore(*): oppdater datoannotasjonar etter release [skip ci]` viss det er endringar.
