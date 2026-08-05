# Fjern tomme og «None»-DEBUG-linjer frå `run_logged()`

## Bakgrunn

Med `LOGLVL=DEBUG` produserer `gen-docgen-examples + gen-doc`-steget (og i praksis alle steg som brukar `run_logged()`) mykje støy:

```
[DEBUG]
[DEBUG]
...
[DEBUG] None
[DEBUG] None
...
```

**To ulike årsaker, stadfesta ved å køyre kvar kommando isolert:**

1. **Tomme DEBUG-linjer** — `run_logged()` i `make/00-settings.mk:88-103` kallar ubetinga `log_debug "$$output"` ved suksess, uavhengig av om `$$output` faktisk inneheld noko. `gen-docgen-examples.py` skriv **0 byte** til stdout ved vellykka køyring (stadfesta ved direkte køyring i `python-pytest`-containeren) — resultatet er ei tom `[DEBUG] `-linje for kvart skjema.

2. **`[DEBUG] None`** — `gen-doc`-CLI-en frå `linkml`-pakken (versjon 1.11.1, installert i `linkml-local`-imaget) skriv bokstaveleg `None\n` til stdout ved vellykka køyring (stadfesta ved direkte køyring: `gen-doc ...` → stdout er nøyaktig `None\n`, 5 byte). Dette er ei kjend eigenheit i `linkml` sin CLI (kommandofunksjonen sin returverdi frå `serialize()` — som for `DocGenerator` er `None` sidan output går til filer, ikkje stdout — vert implisitt printa av CLI-wrapperen). Ikkje noko vi kan fikse i `linkml`-pakken utan ein sårbar CLI-patch (jf. den eksisterande `docgen-max-chars.patch`, som berre patchar `docgen.py`-generatorlogikken, ikkje CLI-inngangspunktet).

`run_logged()` er delt infrastruktur brukt frå **9 kallstader** i `make/00-settings.mk`, `make/10-generator-macros.mk` og `make/30-instances.mk` — ein fiks her rettar støyen for alle generator-steg samtidig, i tråd med repoet sitt DRY-prinsipp (éi kjelde for logging-åtferd).

## Steg

1. **Endre `run_logged()` i `make/00-settings.mk`** (linje 88-103): berre kall `log_debug "$$output"` når `$$output` verken er tom eller nøyaktig strengen `"None"`. Feilstien (`rc -ne 0`) er uendra — full fanga output skal framleis loggast synleg ved feil, uavhengig av innhald, sidan det er der reelle feilmeldingar må vere synlege ("Ingen stille feil").

   ```bash
   run_logged() {
     local label="$$1"; shift
     local output rc
     if output=$$("$$@" 2>&1); then
       rc=0
     else
       rc=$$?
     fi
     if [ $$rc -ne 0 ]; then
       log_error "$$label feila (exit code $$rc) — kommando: $$*"
       [ -n "$$output" ] && log_error "$$output"
       return $$rc
     fi
     # linkml sine gen-*-CLI-kommandoar skriv stundom bokstaveleg "None" til
     # stdout ved suksess (CLI-en sin returverdi frå serialize()) — filtrer
     # vekk denne kjende støykjelda, og hopp over tom output, frå debug-logginga
     if [ -n "$$output" ] && [ "$$output" != "None" ]; then
       log_debug "$$output"
     fi
     return 0
   }
   ```

2. **Verifiser at feilsporing er uendra.** Filteret gjeld berre suksess-stien (`rc -eq 0`). Dersom ein kommando feilar og tilfeldigvis skriv "None" eller ingenting til stdout/stderr, skal `log_error`-greina framleis køyre uendra (ho er ikkje endra av denne fiksen).

3. **Test:** køyr `LOGLVL=DEBUG make domain-ap-no` (eller eit tilsvarande domene) og stadfest at:
   - Ingen tomme `[DEBUG]`-linjer eller `[DEBUG] None`-linjer dukkar opp
   - Reell debug-informasjon (t.d. `[DEBUG] [ap-no/dcat-ap-no] Startar gen-docgen-examples + gen-doc: ...`, som kjem frå `run_parallel_with_timer` sin eigen `log_debug`, ikkje frå `run_logged()`) er uendra
   - Ein kunstig feil (t.d. midlertidig broten skjemasti) framleis gir full, synleg feilmelding via `log_error`

## Handlingsliste

- [x] Endre `run_logged()` i `make/00-settings.mk` til å hoppe over tom/«None»-output i `log_debug`-kallet på suksess-stien
- [x] Køyr `LOGLVL=DEBUG make domain-ap-no` og stadfest at støyen er borte og reell debug-info er uendra
- [x] Stadfest at feilsporing (`log_error`-greina) er uendra ved ein kunstig feil

## Utført

`run_logged()` (`make/00-settings.mk:88-105`) hoppar no over `log_debug`-kallet på suksess-stien når fanga output er tomt eller nøyaktig `"None"`. Feilstien (`rc -ne 0` → `log_error`) er heilt uendra.

Verifisert:
- `LOGLVL=DEBUG make domain-ap-no` — første forsøk feila på ein transient DNS-feil i `gen-rdf` (`socket.gaierror`, urelatert til denne endringa); andre forsøk fullførte reint (exit 0). I `gen-docgen-examples + gen-doc`-seksjonen (10 skjema) var det **0** tomme `[DEBUG]`-linjer og **0** `[DEBUG] None`-linjer, medan `run_parallel_with_timer` sine eigne `[DEBUG] [domain/schema] Startar ...`-linjer var uendra til stades
- Isolert test med ein midlertidig `make -f`-fil: `run_logged` med feilande kommando (`false`) gir framleis synleg `[ERROR] ... feila (exit code 1) — kommando: false`; `run_logged` med vellykka kommando og tom output (`true`) gir no ingen DEBUG-linje i det heile
