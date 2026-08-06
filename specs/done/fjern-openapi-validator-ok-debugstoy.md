# Fjern openapi-spec-validator sin "<fil>: OK"-debuglinje

## Bakgrunn

`run_gen_openapi_parallel` (`make/10-generator-macros.mk`) køyrer `openapi-spec-validator`
etter `gen-openapi.py`, via `run_logged`. Ved vellykka validering skriv
`openapi-spec-validator` sjølv `<sti>: OK` til stdout — fanga av `run_logged` og logga
via `log_debug`, t.d.:

```
[DEBUG] /work/generated/fint/fint-okonomi/fint-okonomi-openapi.yaml: OK
→ gen-openapi  fint/fint-okonomi (6.9s)
```

Linja er redundant: den påfølgjande `→ gen-openapi ... (Xs)`-linja frå
`run-parallel-gen.sh` stadfestar alt at heile steget (skriving + validering) lukkast.

**Tidlegare vurdert:** `specs/done/gen-openapi-asyncapi-debug-stoy.md` såg på nøyaktig
denne linja og valde å **behalde** ho — grunngjeving den gong var at (a) eit
spesialtilfelle i den delte `run_logged()` bryt med at funksjonen skal vere generisk,
og (b) `> /dev/null` rundt validator-kallet ville også undertrykt feilinformasjon ved
faktisk valideringsfeil (forbode av CLAUDE.md sin "Ingen stille feil"-regel). Brukaren
har no eksplisitt bede om at linja vert fjerna likevel — denne specen reverserer difor
det tidlegare valet, med brukaren sitt samtykke til tilnærminga under.

**Vald tilnærming (avklart med brukar):** utvid det eksisterande "None"-filteret i
`run_logged` (`make/00-settings.mk`) til også å hoppe over linjer som matchar
mønsteret `<sti>: OK`. Dette er trygt fordi `openapi-spec-validator` sine
feilmeldingar (via `print(exc)` i verktøyet sin kjeldekode) har eit heilt anna format
enn `<sti>: OK` — feilsporing via `run_logged` sin `log_error`-grein (ikkje-null exit
code) er difor uendra og framleis fullt synleg.

## Steg

1. **Utvid filteret** i `run_logged()` (`make/00-settings.mk`, rundt linje 105) slik at
   linjer som matchar `<noko>: OK` (t.d. via ein bash-regex eller `grep -qE ': OK$'`)
   vert hoppa over på same måte som bokstaveleg `"None"`, i tillegg til (ikkje i staden
   for) den eksisterande sjekken.
2. **Test:** køyr `LOGLVL=DEBUG make gen-openapi DOMAIN=fint` (eller tilsvarande) og
   stadfest at:
   - `<sti>: OK`-debuglinja frå `openapi-spec-validator` ikkje lenger vert vist
   - `→ gen-openapi domain/name (Xs)`-fullført-linja framleis vert vist uendra
   - Filene (`*-openapi.yaml`) vert framleis skrivne korrekt (uendra innhald)
3. **Test feilsporing:** framkall ein kunstig valideringsfeil (t.d. midlertidig
   korrupt ein generert `*-openapi.yaml`) og stadfest at `run_logged` sin
   `log_error`-grein framleis viser full feilmelding frå `openapi-spec-validator`.
4. **Oppdater** `specs/done/gen-openapi-asyncapi-debug-stoy.md` sin "Vurdert, men
   utelate"-seksjon med ei kort tilvising til denne specen, sidan det tidlegare valet
   no er reversert.

## Handlingsliste

- [x] Utvid `run_logged()`-filteret i `make/00-settings.mk`
- [x] Køyr `LOGLVL=DEBUG make gen-openapi DOMAIN=fint` og stadfest redusert støy
- [x] Stadfest feilsporing uendra ved kunstig valideringsfeil
- [x] Oppdater tilvising i `specs/done/gen-openapi-asyncapi-debug-stoy.md`

## Utført

Utvida filteret i `run_logged()` (`make/00-settings.mk`) til å hoppe over debug-logging
av output som anten er bokstaveleg `"None"` eller sluttar på `": OK"` (glob-match
`*": OK"`), i tillegg til den eksisterande `None`-sjekka.

Verifisert:
- `LOGLVL=DEBUG make gen-openapi DOMAIN=fint` viser no berre éi debug-deloverskrift
  (`gen-openapi (openapi: true) for schemas: ...`) + éi `→ gen-openapi ... (Xs)`
  fullført-linje per skjema — `<sti>: OK`-linja frå `openapi-spec-validator` er borte
- Isolert bash-test av filterlogikken stadfestar: `"None"` og `"<sti>: OK"`-suksessoutput
  vert filtrert, ekte informativ suksessoutput vert framleis logga, og feilmeldingar
  (sjølv med `OK`-liknande delstrengar) går uendra gjennom `log_error`-greina med full
  tekst — feilsporing er ikkje svekt
- `specs/done/gen-openapi-asyncapi-debug-stoy.md` oppdatert med tilvising til denne
  reverseringa
