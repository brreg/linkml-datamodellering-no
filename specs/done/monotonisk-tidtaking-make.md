# Bytt vegg-klokke-tidtaking til monotonisk klokke i byggesystemet

## Bakgrunn

Brukaren observerte at `make gen-plantuml SCHEMA=...` viste
`gen-plantuml-svg batch (2 fil(er)) (1983547.09s)` — ca. 23 dagar elapsed
for ein batch-rendering som i praksis tok under eitt sekund.

## Rotårsak

Alle tidtakingar i byggesystemet brukar `date +%s%3N` (millisekund sidan
epoch, **vegg-klokke-basert**). WSL2 er kjent for å la systemklokka inni
gjestemiljøet drifte eller hoppe ved dvale/oppvakning av vertsmaskinen —
skjer eit slikt hopp mellom start- og slutt-målinga (t.d. fordi maskinen
sov mellom to steg i ein interaktiv gjennomgang, jf. "Trykk Enter for å
halde fram"-prompten i brukaren sin terminal), vert differansen absurd
stor. Dette er eit tidtakingsartefakt, ikkje ein reell ytelsesregresjon i
PlantUML-rendringa.

Same mønster (`t0=$(date +%s%3N); ...; t1=$(date +%s%3N); ms=$((t1-t0))`)
er brukt konsekvent 10 stader:

- `make/00-settings.mk` — `timed_run()` (delt hjelpefunksjon)
- `make/40-validation.mk` — `validate-data`, `validate-examples` (2×2 stader)
- `src/assets/scripts/makefile/batch-render-plantuml.sh`
- `src/assets/scripts/makefile/run-domain-pipeline.sh` (3 stader: pipeline-total,
  per-steg i `run_bg()`, informasjonsmodell-instance-steget)

Alle er difor råka av same sårbarheit.

## Fiks

Legg til ein delt `now_ms()`-funksjon i `LOG_FUNCTIONS`-definisjonen i
`make/00-settings.mk` (same stad som `fmt_elapsed_ms`, som alt er den
eksisterande delte kjelda for elapsed-formatering) som les
`/proc/uptime` — ei monotonisk klokke, upåverka av NTP-justeringar eller
klokkehopp ved dvale/oppvakning. Byt ut alle 10 `date +%s%3N`-kallstadene
med `now_ms`.

`/proc/uptime` har forma `<sekund>.<hundredel> <idle-sekund>.<hundredel>`
(stadfesta empirisk på dette systemet). Konverter til heiltals-millisekund
utan `awk`/`bc` (unngå ekstra prosessar per kall):

```bash
now_ms() {
  local up sec frac
  read -r up _ < /proc/uptime
  sec=${up%.*}
  frac=${up#*.}
  printf '%d' $(( sec * 1000 + 10#$frac * 10 ))
}
```

`10#$frac` tvingar base-10-tolking (unngår oktal-feiltolking dersom
hundredelen har leiande null, t.d. "05").

## Handlingsliste

1. Legg `now_ms()` til `LOG_FUNCTIONS` i `make/00-settings.mk`.
2. Byt `date +%s%3N` → `now_ms` i `timed_run()` (same fil).
3. Byt `date +%s%3N` → `now_ms` i `make/40-validation.mk` (4 kallstader).
4. Byt `date +%s%3N` → `now_ms` i `batch-render-plantuml.sh` (2 kallstader).
5. Byt `date +%s%3N` → `now_ms` i `run-domain-pipeline.sh` (6 kallstader) —
   merk at `eval "$LOG_FUNCTIONS"` må flyttast FØR `PIPELINE_T0`-linja
   (for tida etter, sidan `now_ms` må vere definert før første bruk).
6. Dokumenter som ny bug (BUG-21) i `bugs/` + `BUGS.md`, sidan dette er eit
   reproduserbart, forklart avvik i eit eksisterande verktøy (jf.
   konvensjonen i CLAUDE.md § «Kjente feil»).
7. Verifiser: køyr eit par av dei råka make-targeta og stadfest at
   elapsed-tida er rimeleg (ikkje avhengig av faktisk klokkehopp å
   reprodusere — koden sjølv er korrekt uavhengig av om eit hopp skjer i
   testøkta).

## Ikkje gjort

Rettar ikkje eventuelle andre stader i repoet som måtte bruke
`date +%s%3N` utanfor `make/`- og `src/assets/scripts/makefile/`-katalogane
(ingen slike funne ved søk i heile repoet).

## Utført

Implementert 2026-08-28.

- `make/00-settings.mk`: ny `now_ms()`-funksjon lagt til `LOG_FUNCTIONS`
  (les `/proc/uptime`, monotonisk). `timed_run()` bruker no `now_ms` i
  staden for `date +%s%3N` (2 stader).
- `make/40-validation.mk`: `validate-data` og `validate-examples` bruker no
  `now_ms` (4 stader).
- `src/assets/scripts/makefile/batch-render-plantuml.sh`: `now_ms` i staden
  for `date +%s%3N` (2 stader).
- `src/assets/scripts/makefile/run-domain-pipeline.sh`: `now_ms` på alle 6
  kallstadene; `eval "$LOG_FUNCTIONS"` flytta til FØR første bruk av
  `now_ms` (var før: rett etter `PIPELINE_T0`-linja, som brukte rå `date`
  og difor ikkje trong funksjonen definert enno).
- Ny bug-dokumentasjon: `bugs/monotonisk-tidtaking-make.md` (BUG-21),
  lagt til `BUGS.md`-tabellen, status `løyst`.

**Verifisert:**
- `make gen-plantuml SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml`
  — `(1.39s)`, ikkje lenger absurd stort.
- `make validate-examples DOMAIN=oreg` — `(9.22s)`.
- `make domain-oreg` (full pipeline, alle steg i Fase 1–3) — realistiske
  tider gjennomgåande, total `42.91s`.
- Isolert test av `now_ms()`: 200 ms `sleep` målt korrekt som `0.20s`.

**Merk:** `make domain-oreg`-verifiseringskøyringa oppdaterte òg fleire
allereie-spora `metadata/`- og `validation/`-artefaktar under
`src/linkml/oreg/**` (og oppretta slike for skjema som endå ikkje hadde
dei committa) — dette er venta, sannkjelde-korrekt åtferd frå
byggesystemet (same mønster som CI produserer), ikkje ein del av denne
fiksen sitt formål. Nemnt her for sporbarheit; brukaren avgjer sjølv om
desse skal committast saman med fiksen eller separat.
