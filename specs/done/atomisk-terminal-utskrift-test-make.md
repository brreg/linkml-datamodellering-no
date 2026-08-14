# Atomisk terminalutskrift i _run_one() — fiks garbla interleaving i make test

## Bakgrunn

Brukaren opplever at `make test` sin live terminalutskrift er vanskeleg å
lese — linjer frå ulike skjema smeltar saman midt i teksten, t.d.:

```
  validate (cpsv-ap-no)                                ...→ Startar testar for dcat-ap-no ...
  validate (dcat-ap-no)                                ... OK
  gen-jsonld (cpsv-ap-no)                              ...→ Startar testar for dqv-ap-no ...
```

## Stadfesta: pre-eksisterande, ikkje forårsaka av dagens økt sine endringar

Same garbling finst identisk i ei loggfil frå **før** Del 1/Del 2/DEBUG-
logging-arbeidet i denne økta (`make-test-run2.log`, teke opp tidlegare i
same samtale) — t.d. nøyaktig same mønster:
`validate (cpsv-ap-no)  ...→ Startar testar for dcat-ap-no ...`. Dette er
altså ein eksisterande eigenskap ved `SCHEMA_PIDS`/`run_schema_tests()` sin
per-skjema-parallellisme (som var på plass lenge før denne økta), ikkje ein
regresjon frå Fase A-parallelliseringa. Fase A-parallelliseringa (Del 1)
gjer derimot problemet **meir synleg i praksis**: Fase A tek no ~1 minutt i
staden for ~13 — Fase B (alltid parallell, éin bakgrunnsprosess per skjema)
startar difor raskare og alle skjemaa sine testblokker kjem tettare på
kvarandre i tid enn før.

## Rotårsak

`_run_one()` (`tests/test_make.sh`) skriv statuslinja si til terminalen
(`>&3`) i **to separate** `printf`-kall:

```bash
printf "  %-52s ..." "$tname" >&3   # (1) utan linjeskift
...                                    # <- testen køyrer her
printf " ${CLR_OK}OK${CLR_RST}\n" >&3  # (2) med linjeskift, seinare
```

Sidan mange skjema køyrer samstundes (kvart sitt bakgrunnsprosess via
`SCHEMA_PIDS`), kan eit **anna** skjema sitt (1)-kall lande i tidsvindauget
mellom denne testen sitt (1)- og (2)-kall — begge skriv til same
fildeskriptor utan nokon synkronisering. Resultatet er at linje (1) frå
skjema A og linje (1) frå skjema B hamnar på same rad, før nokon av dei får
skrive sitt (2)-kall.

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Bygg heile statuslinja (namn + `...` + `OK`/`FEIL`, inkl. linjeskift) som **éin** streng og skriv henne med **eitt** `printf`-kall **etter** at testen er ferdig — ikkje eitt kall før og eitt kall etter. Ein enkelt `printf`/`echo` av ei linje på denne lengda (~70-80 teikn) er éin `write()`-syscall, og dermed atomisk med omsyn til andre samstundes prosessar sine skriv til same fildeskriptor på Linux — eliminerer midt-i-linja-garbling heilt. Rekkjefølgja linjer frå ULIKE skjema kjem i kan framleis variere (forventa og akseptabelt for ein parallell testkøyrar), men kvar enkelt linje vil alltid vere heil og lesbar | `tests/test_make.sh`, `_run_one()` |
| 2 | Verifiser at `>&3`-skrivet framleis skjer FØR eventuell `log_debug`/`log_info`-logging (tiltak uendra frå `specs/done/logging-test-make-debug-og-tidsbruk.md`) — berre sjølve `>&3`-linja skal bli atomisk, ikkje resten av funksjonen sin struktur | `tests/test_make.sh` |
| 3 | Verifiser: `make test` (alle skjema) — stadfest visuelt (eller via eit script som grep-ar etter linjer med meir enn éin `"..."` eller meir enn éitt skjemanamn) at ingen linjer lenger inneheld garbla, samanblanda tekst frå to ulike testkall | — |
| 4 | Verifiser ingen regresjon: `##RESULT:OK`/`##RESULT:FAIL`-markørane (skrivne til `$tmplog`, ikkje `>&3`) er uendra, og full `make test` gjev framleis identisk resultatsett (591 OK, 5 feil) | — |
| 5 | `bash -n tests/test_make.sh` (syntakssjekk) | — |

## Utført

Alle 5 tiltak gjennomførte og verifiserte:

1. `_run_one()` bygg no heile statuslinja (namn + `...` + `OK`/`FEIL` +
   linjeskift) som éin streng, skriven med **eitt** `printf`-kall til `>&3`
   **etter** at testen er ferdig — det tidlegare `printf "  %-52s ..." ... >&3`-
   kallet FØR testen (utan linjeskift) er fjerna heilt.
2. `log_debug`/`log_info`-kalla frå `specs/done/logging-test-make-debug-og-tidsbruk.md`
   er uendra i struktur og innhald — berre sjølve `>&3`-skrivet vart gjort
   atomisk.
3. Verifisert med full `make test` (35 skjema, tee-a til fil): 0 linjer
   med to `"..."`-førekomstar eller ei skjema-startlinje midt inni ei
   testlinje (mønstera frå det opphavlege garbling-eksempelet er borte).
   Stikkprøve av rå linjer (`cat -A`) stadfestar kvar linje er heil og
   korrekt linjeskift-terminert.
4. Full `make test` gav framleis **591 OK, 5 feil** — identisk
   resultatsett som referansen, ingen regresjon.
5. `bash -n tests/test_make.sh` — syntaks OK.

## Referanse

- `tests/test_make.sh`, `_run_one()` og `run_schema_tests()`/`SCHEMA_PIDS` — kjelda til den pre-eksisterande per-skjema-parallellismen
- `specs/done/paralleliser-fase-a-test-make.md` — Del 1, kvifor problemet vart meir synleg (raskare Fase A → tettare Fase B-oppstart)
- `specs/done/logging-test-make-debug-og-tidsbruk.md` — den nyleg lagt til DEBUG/INFO-logginga i same funksjon (uendra av dette tiltaket, går via `$tmplog`, ikkje `>&3`)
