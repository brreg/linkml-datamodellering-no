# Bug: To ulike skriveveger til valideringslogg-JSON med ulike feltnamn

**ID:** BUG-12
**Status:** `løyst`
**Komponent:** `make/40-validation.mk`
**Oppdaga:** 2026-08-06
**Løyst:** 2026-08-06

## Symptom

`src/linkml/<domain>/<modell>/validation/<versjon>/<policy>.json` kan ha to
inkompatible skjema avhengig av kva kodeveg som sist skreiv fila:

- **CI-vegen** (`src/assets/scripts/makefile/run-validation.sh`, brukt av
  `generate.yml`/`validate.yml` og `make log-mcp-validate`) skriv
  `{schema, domain, version, validation_policy, result}` — **ingen**
  `validated_at`-felt (`run-validation.sh:136,154-188`).
- **`save-validation-log.py`** (brukt av `make validate-bronze`/
  `make validate-data`) skriv `validation_type` i staden for
  `validation_policy`, og legg i tillegg til eit `validated_at`-tidsstempel
  (UTC ISO) (`save-validation-log.py:59-67`).

Ein konsument som stolar blindt på eitt av feltnamna (t.d. alltid forventar
`validation_policy` eller alltid forventar `validated_at`) vil få
manglande/`None`-verdiar avhengig av kva veg som sist skreiv fila for det
gjeldande skjemaet/versjonen.

## Rot-årsak

To uavhengige script vart skrivne for to ulike kallstader — manifest-baserte
CI-valideringar (`run-validation.sh`) og eksempel/data-valideringar
(`save-validation-log.py`) — utan ei delt skrivefunksjon eller eit felles
JSON-skjema mellom dei.

## Workaround (i drift)

Den einaste konsumenten som faktisk les desse filene i produksjon,
`mkdocs/lib/scripts/generate-validation-md.py`, handterer begge formata
defensivt:

- Policy vert **alltid** re-utleia frå skjemaet sin `build.yaml`
  (`validation_policy`-nøkkelen), aldri stolt på frå JSON-feltet — sjå
  kommentar `generate-validation-md.py:62-64`.
- `validated_at` lesast med `data.get("validated_at", "")` (tom streng
  dersom feltet manglar).
- Feil-/åtvaringstal lesast med
  `result.get("errorCount") or result.get("error_count")` (begge
  nøkkelnamn-variantar).

Ingen fiks er gjort ved kjelda (dei to skrivarane sjølve).

## Løysing

Konsoliderte dei tre skrivarane (`run-validation.sh`,
`save-validation-log.py`, og ein tredje — tidlegare udokumentert —
skrivar `src/mcp-linkml-validator/validate-and-log.py`, funne under
oppfølging av denne bugen) til éin delt struktur, jf. "DRY — ikkje gjenta
deg sjølv" i `CLAUDE.md`.

**Filer:** `src/assets/scripts/utils/validation_log.py`,
`src/assets/scripts/makefile/run-validation.sh`,
`src/assets/scripts/makefile/save-validation-log.py`,
`src/mcp-linkml-validator/validate-and-log.py`

Oppdaga under arbeid med `specs/backlog/artefakt-generering.md` § 3.5.

### Utført (2026-08-06)

1. ✓ Ny delt modul `src/assets/scripts/utils/validation_log.py`:
   `build_validation_log_entry()` byggjer eit logg-objekt med konsistente
   felt (`schema`, `domain`, `version`, `validation_policy`, `validated_at`,
   `result`); `write_validation_log()` skriv det til fil.
2. ✓ `save-validation-log.py`: brukar no den delte modulen i staden for å
   byggje `log_entry`/skrive fila sjølv. `validation_type` er framleis
   parameter-/CLI-namnet (feltet dekkjer meir enn reine policy-namn, t.d.
   `examples`/`data-<catalog>`), men JSON-nøkkelen er no `validation_policy`
   som i dei to andre skrivarane. Fjerna no ubrukt `datetime`/`timezone`-import.
3. ✓ `run-validation.sh`: Python-heredoc-en importerer no den delte modulen
   (`sys.path` utvida med `$REPO_ROOT/src/assets/scripts`, `REPO_ROOT` sendt
   inn som nytt argv-ledd) og får dermed `validated_at` med, som tidlegare
   mangla heilt frå denne kodevegen.
4. ✓ `validate-and-log.py` (`src/mcp-linkml-validator/`): omdøypte
   `validation_type` → `validation_policy` i JSON-output. Denne fila deler
   ikkje `sys.path` med resten av repoet (kun `server.py` og seg sjølv vert
   kopiert inn i `Dockerfile.mcp-linkml`), så feltnamnet vart retta direkte
   i staden for å trekkje inn den delte modulen.
5. ✓ `mkdocs/lib/scripts/generate-validation-md.py` verifisert å ikkje
   trenge endring — han les allereie berre `version`, `validated_at` (med
   default), og `result.*`, og utleier policy frå `build.yaml` (aldri frå
   JSON-feltet), så han var alt uavhengig av kva feltnamn skrivaren brukte.
6. ✓ Verifisert manuelt: køyrde `save-validation-log.py` og den nye
   Python-blokka frå `run-validation.sh` mot same skjema (`ngr-adresse`) —
   begge produserer no identisk feltstruktur
   (`{schema, domain, version, validation_policy, validated_at, result}`).
   `bash -n` og `python3 -m py_compile` køyrt på alle endra filer.
7. ✓ Ikkje migrert eksisterande, allereie committa `validation/**/*.json`
   (46 filer med gamalt `validation_type`-felt) — `generate-validation-md.py`
   var alt uavhengig av feltnamnet, så dette er ikkje nødvendig; nye
   valideringskøyringar skriv konsekvent format framover.
8. ✓ Status oppdatert til `løyst`.
