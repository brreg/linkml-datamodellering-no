# Oppsummering til slutt i run-domain-pipeline.sh

## Bakgrunn

Under vurderinga av om `make test`-optimaliseringane frå denne økta
kunne vidareførast til `make domain-*`
(`specs/done/vidarefor-test-optimaliseringar-til-domain-x.md`) vart det
identifisert at `run-domain-pipeline.sh` (orkestrerer `domain-<domain>`
sin Fase 1/2/3-parallellisme) IKKJE har nokon tilsvarande oppsummering
av kva som skjedde og kor lang tid kvart steg tok — berre feillogging
via `log_error` når eit steg feilar. Brukaren ønskjer ein spec for å
leggje til ei oppsummering, analogt `print_phase_a_summary()` i
`tests/test_make.sh` (`specs/done/fase-a-oppsummering-test-make.md`).

**Merk:** ein tidlegare versjon av denne specen inkluderte å liste opp
KONKRETE SKJEMANAMN for steg som feila (analogt `phase_a_error_names()`
i `test_make.sh`). Brukaren bad om at dette droppast dersom det skapte
unødig kompleksitet — det gjorde det (krov å FANGE kvart steg sitt
output via `tee`, eksplisitt handtere `${PIPESTATUS[0]}` for å halde
`wait_job()` sin eksisterande feildeteksjon korrekt, nye
loggfil-array + oppryddingslogikk), så det er teke ut att. Steget sitt
EIGE `log_error`-kall (uendra, upåverka av dette tiltaket) dekkjer
framleis feilattribuering.

## Skilnad frå test_make.sh sin situasjon

`run-domain-pipeline.sh` sin arkitektur er ENKLARE enn `test_make.sh`
sin Fase A på eitt vesentleg punkt: kvart steg her (`run_bg key ...`)
vert starta DIREKTE i HOVUDSKALET (ikkje inni ein djupt-backgrounda
funksjon slik Fase A-stega i `test_make.sh` var), så assosiative array
(`PIDS` er alt slik i dag) FUNGERER TRYGT for å halde på tidsbruk/status
per steg — INGEN fast-fil-arbeidsrunde (`phase_a_logfile()`/
`phase_a_metafile()`) er nødvendig her, ulikt `test_make.sh` sin
løysing. Output-strauminga er UENDRA (framleis direkte til terminal,
ikkje omdirigert/fanga) — tiltaka under legg BERRE til tidsmåling og
status-tracking oppå det eksisterande `run_bg`/`wait_job`-mønsteret.

## Tre grupper, ikkje to — pipelinen sitt REELLE avhengigheitsmønster

Fase 1 og Fase 2 er BEGGE "batcha, parallelle kall" i teknisk forstand
(begge går via `run_bg`/`wait_job`), men dei er IKKJE likeverdige:
Fase 1 sine 12 steg har INGEN innbyrdes avhengigheit (alle kan starte
med det same), medan Fase 2 sine 3 steg (`xsd`/`openapi`/`asyncapi`)
FØRST ventar på at `json-schema` (frå Fase 1) er ferdig — jf. den
eksisterande `wait_job json-schema`-linja mellom dei to gruppene i
scriptet i dag — FØR dei sjølve startar (parallelt seg imellom). Dette
er nøyaktig det brukaren kallar ei "rekkje av batcha kall" (kall som
ventar på at andre er utført først), og skal difor vere EI EIGA,
TREDJE gruppe med eiga overskrift, IKKJE slåast saman med Fase 1:

1. **«Parallelle batcha kall (uavhengige)»** — Fase 1, 12 steg, ingen
   ventar på noko.
2. **«Rekkjefølgde batcha kall (ventar på gen-jsonschema)»** — Fase 2,
   3 steg, ventar på steg 1 sin `json-schema`, køyrer så parallelt seg
   imellom.
3. **«Synkrone kall»** — Fase 3, 1 steg, ventar på ALT frå gruppe 1+2,
   køyrer heilt åleine.

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Legg til `declare -A START_TIMES ELAPSED_MS OK_FLAG` saman med eksisterande `PIDS`/`FAILED`. To SEPARATE ordna array i staden for éin flat liste: `declare -a STEP_ORDER_PHASE1=()` og `declare -a STEP_ORDER_PHASE2=()` — held styr på KVA GRUPPE kvart steg høyrer til (sjå avsnittet over) | `src/assets/scripts/makefile/run-domain-pipeline.sh` |
| 2 | Legg til `PIPELINE_T0=$(date +%s%3N)` HEILT ØVST i scriptet (rett etter `domain="$1"`, FØR noko steg vert starta) — same mønster/namnekonvensjon som `SCRIPT_T0` i `test_make.sh` (`specs/done/logging-test-make-debug-og-tidsbruk.md`) | same fil |
| 3 | `run_bg()` får eit NYTT fyrste argument `<phase>` (`1` eller `2`): `run_bg <phase> <key> <kommando...>`. Legg `$key` til `STEP_ORDER_PHASE1` eller `STEP_ORDER_PHASE2` avhengig av `$phase`, og set `START_TIMES[$key]=$(date +%s%3N)` FØR `( "$@" ) &` (UENDRA elles — ingen fanga output). Alle 15 eksisterande `run_bg`-kallstader (12 i Fase 1, 3 i Fase 2) må oppdaterast med det nye fyrste argumentet | same fil |
| 4 | `wait_job()`: mål `ELAPSED_MS[$key]` etter `wait`, set `OK_FLAG[$key]=1`/`0` basert på exit-koden (attval av eksisterande `if ! wait ...`-logikk, ingen endring i FEIL-handteringa/`log_error`-kallet) | same fil |
| 5 | Ny `print_pipeline_summary()` skriv oppsummeringa i TRE EKSPLISITT ÅTSKILDE GRUPPER (sjå avsnittet over for definisjon/grunngjeving) — KVAR gruppe innleia med EI FORKLÅRANDE LINJE. Kvar linje INNI ei gruppe er kolonnejustert namn/tidsbruk/status, same visuelle mønster som `print_phase_a_summary()` i `test_make.sh` (`printf` med faste breidder, `${CLR_OK}OK${CLR_RST}`/`${CLR_ERR}FEIL${CLR_RST}`). Ei gruppe med INGEN steg registrerte enno (Fase 3 ved fyrste kallpunkt, sjå tiltak 7) skal IKKJE skrive ut si eiga (tomme) overskrift. HEILT TIL SLUTT i funksjonen: skriv `"Resultat: domain-${domain}: <N> OK, <M> feil"` etterfølgt av `"Total tidsbruk: $(fmt_elapsed_ms $(( $(date +%s%3N) - PIPELINE_T0 )))"` — same to-linjers rekkjefølgje og `fmt_elapsed_ms`-format som `wait_for_tests()` i `test_make.sh` alt brukar for `SCRIPT_T0` | `src/assets/scripts/makefile/run-domain-pipeline.sh` |
| 6 | Fase 3 (`gen-informasjonsmodell-instance`) er i dag EIN DIREKTE, ikkje-backgrounda kall utanfor `run_bg`/`wait_job`-mønsteret — pakk han inn i EIGA tidsmåling/`OK_FLAG`-tracking (eigen nøkkel, IKKJE lagt i nokon av `STEP_ORDER_PHASE1/2`-array, sidan han høyrer til den TREDJE gruppa) utan å endre at han framleis køyrer synkront, sist | same fil |
| 7 | Kall `print_pipeline_summary()` på TO stader: (a) rett før den eksisterande `if [ "$FAILED" -gt 0 ]; then ... exit 1; fi`-sjekken — då vert gruppe 1+2 viste (Fase 3 har ikkje køyrt enno) OG total tidsbruk MÅLT SÅ LANGT (ikkje heile pipelinen), og (b) heilt til slutt etter Fase 3 — då vert ALLE TRE gruppene viste med FULL total tidsbruk | same fil |
| 8 | `bash -n src/assets/scripts/makefile/run-domain-pipeline.sh` | — |
| 9 | Verifiser: `make domain-<eit lite domene, t.d. samt eller fair>` — stadfest oppsummeringa vert vist med rett gruppeinndeling, alle steg-namn/tider/status er korrekte, `Total tidsbruk`-linja er med og verkar rimeleg (om lag same storleiksorden som `time make domain-X` sin eigen `real`-verdi), INGEN endring i eksisterande åtferd (exit-kode, feilmeldingar, `gen-informasjonsmodell-instance` sin plassering sist, live terminal-output uendra) | — |
| 10 | Verifiser: `make domain-ap-no` (største domenet, 9 skjema) — stadfest oppsummeringa handterer alle 16 steg korrekt fordelt på dei TRE gruppene | — |

## Eksempel på ønska output

```
=== domain-ap-no — oppsummering ===

Parallelle batcha kall (Fase 1 — uavhengige steg, køyrer samstundes, ingen ventar på noko):
→ merge                        (2.14s)     OK
→ jsonld-context                (1.87s)     OK
→ shacl                         (3.02s)     OK
→ python                        (2.45s)     OK
→ json-schema                   (2.19s)     OK
→ owl                           (2.88s)     OK
→ rdf                           (4.12s)     OK
→ proto                         (1.55s)     OK
→ graphql                       (1.61s)     OK
→ linkml-convert                (5.03s)     OK
→ docs                          (8.77s)     OK
→ plantuml                      (6.34s)     OK

Rekkjefølgde batcha kall (Fase 2 — ventar på gen-jsonschema frå Fase 1, køyrer så samstundes seg imellom):
→ xsd                           (1.98s)     OK
→ openapi                       (2.21s)     OK
→ asyncapi                      (2.09s)     OK

Synkrone kall (Fase 3 — ventar på ALT frå Fase 1+2, køyrer heilt åleine sist):
→ informasjonsmodell-instance   (0.94s)     OK

Resultat: domain-ap-no: 16 OK, 0 feil
Total tidsbruk: 12.34s
```

### Eksempel med feil

```
=== domain-ap-no — oppsummering ===

Parallelle batcha kall (Fase 1 — uavhengige steg, køyrer samstundes, ingen ventar på noko):
→ merge                        (2.09s)     OK
→ jsonld-context                (1.91s)     OK
→ shacl                         (3.11s)     OK
→ python                        (2.38s)     OK
→ json-schema                   (2.22s)     OK
→ owl                           (2.95s)     OK
→ rdf                           (4.30s)     FEIL
→ proto                         (1.58s)     OK
→ graphql                       (1.64s)     OK
→ linkml-convert                (5.11s)     OK
→ docs                          (8.62s)     OK
→ plantuml                      (6.28s)     OK

Rekkjefølgde batcha kall (Fase 2 — ventar på gen-jsonschema frå Fase 1, køyrer så samstundes seg imellom):
→ xsd                           (2.01s)     OK
→ openapi                       (2.19s)     OK
→ asyncapi                      (2.14s)     OK

Resultat: domain-ap-no: 14 OK, 1 feil
Total tidsbruk: 8.71s
```

(Fase 3 køyrer IKKJE her — pipelinen stoppar før `gen-informasjonsmodell-
instance`, sidan `FAILED > 0` etter Fase 1+2, uendra eksisterande
åtferd. Difor manglar «Synkrone kall»-gruppa i dette eksempelet. Kva
SKJEMA som feila for `rdf` finn ein via `rdf` steget sitt EIGE
`log_error`-kall, uendra frå i dag — ikkje del av denne oppsummeringa.)

## Referanse

- `specs/done/fase-a-oppsummering-test-make.md` — mønsteret dette
  tiltaket speglar
- `specs/done/vidarefor-test-optimaliseringar-til-domain-x.md` — kor
  denne ideen kom frå
- `src/assets/scripts/makefile/run-domain-pipeline.sh` — fila som skal
  endrast

## Utført

Alle tiltak gjennomførte og verifiserte.

1-8: `PIPELINE_T0`, `STEP_ORDER_PHASE1`/`STEP_ORDER_PHASE2`,
`run_bg(<phase> <key> ...)` (nytt fyrste argument, alle 15 kallstader
oppdaterte), `wait_job()`, `print_step_line()`/`print_pipeline_summary()`
(tre grupper med forklårande overskrifter, kolonnejustert, `Total
tidsbruk`), Fase 3 pakka inn i tilsvarande tracking, `print_pipeline_summary()`
kalla på begge stadene (før tidleg-exit og til slutt) — alt implementert
som spesifisert.

**Feil oppdaga og retta undervegs (ikkje i opphavleg spec):**
Fyrste implementasjon rekna `ELAPSED_MS[$key]` i `wait_job()` som
`$(date +%s%3N) - START_TIMES[$key]`, målt PÅ DET TIDSPUNKTET
`wait_job()` vart kalla for akkurat den nøkkelen. Sidan
`for key in "${!PIDS[@]}"` itererer eit USORTERT bash-associative-array,
og `wait_job()` for MANGE nøklar først vert kalla ETTER at løkka har
blokkert på eit anna, seinare-ferdig steg tidlegare i iterasjons-
rekkjefølgja, synte fyrste verifiseringskøyringa (`make domain-samt`)
tydeleg feil: 10 av 12 Fase 1-steg synte IDENTISK ~25.2-25.3s uansett
faktisk arbeidsmengd — openbert feil, sidan generatorane sine EIGNE
interne tidslinjer (t.d. `→ merge samt/samt-bu (0.67s)`) synte reelle
tider under 1 sekund. Retta ved å måle elapsed-tid INNI subskalet sjølv
(`t0`/slutt-tid FØR/ETTER `"$@"`, skrive til ei eiga, mktemp-generert
fil PER NØKKEL, lesen tilbake av `wait_job()` ETTER `wait`) — heilt
uavhengig av NÅR `wait_job()` tilfeldigvis vert kalla. Brukte
`if "$@"; then rc=0; else rc=$?; fi` (ikkje `"$@" || rc=$?`) slik at
linja som skriv elapsed-fila ALLTID køyrer, sjølv om `"$@"` feilar —
kritisk sidan `set -euo pipefail` er aktivt (arva av subskalet), og eit
feila steg elles ville avslutta subskalet FØR elapsed vart skriven.
Verifisert ved omkøyring: alle tider no synleg varierte og plausible
(t.d. `docs` 40.48s, `linkml-convert` 3.53s for `ap-no`), og total
tidsbruk stemmer godt med kritisk sti (lengste Fase 1-steg + Fase 3).

**Verifisering:**
- `bash -n` — OK, både før og etter retting.
- `make domain-samt` (1 skjema) — 16 OK, 0 feil, alle tre grupper viste
  korrekt, tider plausible etter retting, total tidsbruk 35.36s.
- `make domain-ap-no` (9 skjema, største domenet) — 16 OK, 0 feil, alle
  tre grupper korrekte, total tidsbruk 46.09s.
- **Feilscenario** (ikkje i sluttversjonen av tiltak-tabellen, men
  verifisert likevel): mellombels øydelagt `fair-metadata-schema.yaml`
  (lagt til ugyldig YAML), køyrde `make domain-fair` — 6 av 12 Fase
  1-steg synte korrekt raud `FEIL` (merge/shacl/owl/rdf/docs/plantuml —
  alle avhengige av det øydelagde skjemaet), «Synkrone kall»-gruppa
  vart KORREKT UTELATEN (Fase 3 køyrde ikkje, som spesifisert),
  `Resultat: domain-fair: 9 OK, 6 feil` og `Total tidsbruk` framleis
  viste. Retta skjemafila tilbake (`git checkout --`), stadfesta
  `make domain-fair` igjen gav 16 OK, 0 feil.
- Reverterte biverknad-endringar i `*/metadata/*-manifest.yaml`
  (kjent, uendra sidan tidlegare i økta) etter kvar verifiseringskøyring.
