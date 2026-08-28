# Bug: vegg-klokke-basert tidtaking i byggesystemet kan gi absurd store elapsed-tal

**ID:** BUG-21
**Status:** `løyst`
**Komponent:** `make/00-settings.mk`, `make/40-validation.mk`, `src/assets/scripts/makefile/batch-render-plantuml.sh`, `src/assets/scripts/makefile/run-domain-pipeline.sh`
**Oppdaga:** 2026-08-28

## Symptom

`make gen-plantuml SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml`
viste:

```
→ gen-plantuml-svg  batch (2 fil(er)) (1983547.09s)
```

— ca. 22,9 dagar elapsed for ein batch-rendering av 2 filer som i praksis
tok under eitt sekund.

## Rot-årsak

All elapsed-tidtaking i byggesystemet brukte `date +%s%3N` (millisekund
sidan epoch) til å måle start- og slutt-tidspunkt, og rekna differansen:

```bash
t0=$(date +%s%3N)
<kommando>
t1=$(date +%s%3N)
ms=$(( t1 - t0 ))
```

`date +%s%3N` er **vegg-klokke-basert**. WSL2 er kjent for å la systemklokka
inni gjestemiljøet drifte eller hoppe når vertsmaskinen søv/vaknar opp igjen
(klokka i WSL2-gjesten synkroniserer seg mot Windows-verten på nytt ved
oppvakning, og kan i mellomtida vise feil tid). Hoppar klokka mellom `t0`
og `t1` — t.d. fordi maskinen sov mellom to steg i ein interaktiv
gjennomgang av byggesystemet — vert `ms` ein vilkårleg stor (eller,
teoretisk, negativ) verdi. Dette er eit reint tidtakingsartefakt, ikkje ein
reell ytelsesregresjon i sjølve kommandoen som vert tidtatt.

Same mønster gjekk igjen 10 stader i byggesystemet:

| Fil | Stader |
|---|---|
| `make/00-settings.mk` | `timed_run()` — delt hjelpefunksjon (2 kall) |
| `make/40-validation.mk` | `validate-data`, `validate-examples` (2×2 kall) |
| `src/assets/scripts/makefile/batch-render-plantuml.sh` | 2 kall |
| `src/assets/scripts/makefile/run-domain-pipeline.sh` | pipeline-total, per-steg i `run_bg()`, informasjonsmodell-instance-steget (6 kall) |

Alle var difor sårbare for same feilkjelde.

## Fiks

La til ein delt `now_ms()`-hjelpefunksjon i `LOG_FUNCTIONS`-definisjonen i
`make/00-settings.mk` (same stad som den eksisterande delte
`fmt_elapsed_ms()`), som les `/proc/uptime` i staden — ei **monotonisk**
klokke, upåverka av NTP-justeringar eller klokkehopp ved dvale/oppvakning:

```bash
now_ms() {
  local up sec frac
  read -r up _ < /proc/uptime
  sec=${up%.*}
  frac=${up#*.}
  printf '%d' $(( sec * 1000 + 10#$frac * 10 ))
}
```

(`10#$frac` tvingar base-10-tolking av hundredels-delen, elles vil bash
tolke ein leiande-null-verdi som t.d. `05` som eit ugyldig oktaltal.)

Alle 10 kallstadene bytta frå `date +%s%3N` til `now_ms`. I
`run-domain-pipeline.sh` måtte `eval "$LOG_FUNCTIONS"` flyttast til FØR
`PIPELINE_T0=$(now_ms)`-linja (var før: `date`-kallet før
`LOG_FUNCTIONS`-evalueringa, sidan `date` ikkje treng nokon funksjon
definert på førehand — `now_ms` gjer det).

## Verifisert

- `make gen-plantuml SCHEMA=src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml`
  — viser no `(1.39s)`, ikkje `(1983547.09s)`.
- `make validate-examples DOMAIN=oreg` — viser realistisk `(9.22s)`.
- `make domain-oreg` (full pipeline, alle 17 batcha steg + Fase 3) —
  realistiske tider på alle steg, total `42.91s`.
- Manuell test av `now_ms()` åleine: 200 ms `sleep` målt som nøyaktig
  `0.20s`.

## Generell regel

Bruk **aldri** `date +%s%3N` (eller anna vegg-klokke-kjelde) for
elapsed-tidtaking i byggesystemet — bruk `now_ms()` frå `LOG_FUNCTIONS`.
Vegg-klokka er rett verktøy for tidsstempel (t.d. `endringsdato` i
skjemametadata), men **feil** verktøy for å måle *varigheit*, sidan ho ikkje
er garantert monotonisk.
