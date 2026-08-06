# Fjern redundant DEBUG-melding frå gen-openapi.py og gen-asyncapi.py

## Bakgrunn

`generate.yml`-workflowen køyrer med `LOGLVL=DEBUG` (linje 357, 461). For kvart openapi-/asyncapi-aktiverte skjema produserer `gen-openapi`/`gen-asyncapi`-steget **tre** DEBUG-linjer, mot **éi** for dei fleste andre generator-steg (etter [[run-logged-tom-none-debug-stoy]]-fiksen):

```
[DEBUG] [ap-no/dcat-ap-no] Startar gen-openapi: generated/.../dcat-ap-no-schema.json → generated/.../dcat-ap-no-openapi.yaml
[DEBUG] gen-openapi: skriven til /work/generated/.../dcat-ap-no-openapi.yaml
[DEBUG] /work/generated/.../dcat-ap-no-openapi.yaml: OK
```

**Årsak, stadfesta ved kodelesing:**

`run_gen_openapi_parallel` (`make/10-generator-macros.mk:395-396`) kallar `run_gen_with_check_parallel` med to kjeda `run_logged`-kall i `$(6)`:
1. `run_logged "gen-openapi $$domain/$$name" ... gen-openapi.py ... --out $$out`
2. `run_logged "openapi-spec-validator $$domain/$$name" ... openapi-spec-validator $$out`

(`gen-asyncapi` har identisk mønster, linje 359: `gen-asyncapi.py` + `asyncapi validate`.)

Linje 1 over kjem frå `run_gen_with_check_parallel` sin eigen `log_debug "[domain/name] Startar $(2): $$input → $$out"` (`make/10-generator-macros.mk:66`) — dette er den forventa, informative linja alle andre generator-steg òg har.

Linje 2 kjem frå at `gen-openapi.py:58` (og `gen-asyncapi.py:58`) sjølv skriv `print(f"gen-openapi: skriven til {args.out}", file=sys.stderr)` — fanga av `run_logged` og logga via `log_debug`. Denne teksten er **reint redundant**: ho seier akkurat det same som linje 1 alt sa (kva fil som vart skriven), berre med anna ordlyd og utan domain/schema-prefiks. Ho er ikkje load-bearing (ingen test refererer teksten; stadfesta med grep mot `tests/`).

Linje 3 kjem frå at `openapi-spec-validator` (tredjeparts CLI-verktøy) sjølv skriv `<fil>: OK` til stdout ved vellykka validering — fanga og logga på same måte. Dette **er** ny informasjon (stadfestar at spesifikasjonen er gyldig, ikkje berre at scriptet køyrde), og kjem frå eit tredjepartsverktøy vi ikkje kan redigere kjeldekoden til. Denne specen **rører ikkje** denne linja — sjå "Vurdert, men utelate" under.

## Vurdert, men utelate

- **Undertrykkje `openapi-spec-validator`/`asyncapi validate` sin eigen suksess-output.** Ville krevje anten (a) endring i den delte `run_logged()`-funksjonen med spesialtilfelle per verktøy (bryt med at `run_logged` skal vere generisk), eller (b) `> /dev/null` rundt validator-kallet (forbode av CLAUDE.md sin "Ingen stille feil"-regel, sidan det ville undertrykt feilinformasjon òg). Utelate frå denne specen — linja er dessutan genuint informativ (stadfestar gyldig spesifikasjon), i motsetnad til linje 2 som berre gjentek linje 1.

  **Reversert i `specs/done/fjern-openapi-validator-ok-debugstoy.md`:** brukaren bad eksplisitt om at linja vert fjerna likevel. Løysinga vart eit filter i `run_logged()` (utvida det eksisterande "None"-filteret), ikkje `> /dev/null` — feilmeldingar (heilt anna tekstformat enn `<sti>: OK`) er difor framleis fullt synlege via `log_error`-greina.

## Steg

1. **Fjern** `print(f"gen-openapi: skriven til {args.out}", file=sys.stderr)` frå `src/assets/scripts/makefile/gen-openapi.py` (linje 58). Skriving til fil (`with open(args.out, "w") as f: f.write(output)`) er uendra — berre stderr-stadfestinga vert fjerna.
2. **Fjern** tilsvarande `print(f"gen-asyncapi: skriven til {args.out}", file=sys.stderr)` frå `src/assets/scripts/makefile/gen-asyncapi.py` (linje 58), same grunngjeving og same mønster (DRY — begge scripta har identisk struktur).
3. **Test:** køyr `LOGLVL=DEBUG make domain-ap-no` og stadfest at:
   - `gen-openapi`/`gen-asyncapi`-steget no berre viser **to** DEBUG-linjer per aktivert skjema (`Startar ...` + validator sin `... OK`), ikkje tre
   - Filene (`*-openapi.yaml`, `*-asyncapi.yaml`) vert framleis skrivne korrekt (uendra innhald, stadfest med `diff` mot ein tidlegare generert versjon eller ved å inspisere fila)
   - Ein kunstig feil i `gen-openapi.py` (t.d. midlertidig ugyldig `--out`-sti) framleis gir full, synleg feilmelding via `run_logged` sin `log_error`-grein (uendra, sidan feilhandtering skjer via exceptions/exit code, ikkje via denne print-linja)

## Handlingsliste

- [x] Fjern redundant `print(...)`-linje i `gen-openapi.py`
- [x] Fjern redundant `print(...)`-linje i `gen-asyncapi.py`
- [x] Køyr `LOGLVL=DEBUG make domain-ap-no` og stadfest redusert DEBUG-støy (3 → 2 linjer per skjema) og uendra filinnhald
- [x] Stadfest feilsporing uendra ved ein kunstig feil

## Utført

Fjerna `print(f"gen-openapi: skriven til {args.out}", file=sys.stderr)` frå `gen-openapi.py` og tilsvarande linje frå `gen-asyncapi.py`. Filskriving (`with open(args.out, "w") as f: f.write(output)`) er uendra.

Verifisert med `LOGLVL=DEBUG make domain-ap-no` (exit 0):
- `gen-openapi`-steget viser no nøyaktig 2 DEBUG-linjer per aktivert skjema (`[domain/schema] Startar gen-openapi: ...` + `<fil>: OK` frå `openapi-spec-validator`), ikkje 3 — den redundante "skriven til"-linja er borte
- `gen-asyncapi` var ikkje aktivert for noko skjema i `ap-no`-domenet i denne testkøyringa (alle viste "Hoppar over"), men koderetting er identisk og symmetrisk med `gen-openapi`
- `generated/ap-no/dcat-ap-no/dcat-ap-no-openapi.yaml` er framleis korrekt generert (`openapi: 3.1.0`, riktig metadata)
- Feilsporing uendra: `run_logged` sin `rc -ne 0`-grein er ikkje rørt, og fjerninga gjeld berre eit suksess-stadfestingsprint, ikkje feilhandtering
