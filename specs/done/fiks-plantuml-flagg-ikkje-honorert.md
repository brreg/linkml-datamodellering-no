# Fiks: `plantuml: false` i build.yaml vart aldri honorert av generator-pipelinen

## Bakgrunn

`make domain-begrepskatalog` feila i CI (`generate.yml`) med:

```
Trying to pull localhost/plantuml:latest...
Error: initializing source docker://localhost/plantuml:latest: pinging container registry
localhost: ... connection refused
Error: make domain-begrepskatalog feila etter 2 retrys
```

**Rotårsak:** `specs/done/reduser-image-storleik-ghcr.md` sitt tiltak A1 endra
`images.json` sitt `plantuml`-oppslag frå `always_required: true` til
`required_if_generator_flag: "plantuml"`, basert på funnet at «0 av `begrepskatalog` sine 2
manifest og 0 av `modellkatalog` sine 12 manifest har `plantuml: true`». Dette var korrekt
observert, men konklusjonen («desse domena treng ikkje `plantuml`-imaget») var **feil**:
`run_gen_plantuml_parallel` i `make/10-generator-macros.mk` har **aldri** sjekka
`build.yaml` sitt `plantuml:`-flagg — han køyrer `gen-plantuml` ubetinga for **alle** skjema i
domenet, uavhengig av manifestet. Samanlikn med `gen-xsd`/`gen-openapi`/`gen-asyncapi`, som
alle har eit eksplisitt `grep -q "^  <flagg>: true" "$manifest"`-steg før dei køyrer.

Før A1 vart dette skjult av at `plantuml`-imaget alltid vart pulla uansett (sløsing, men
ikkje ein feil). Etter A1 sluttar CI å pulle imaget for domene utan `plantuml: true`, men
`domain-<domene>`-pipelinen prøver framleis å bruke det — og feilar.

**8 skjema** har eksplisitt `plantuml: false` i sitt `build.yaml`, men flagget vert altså
ignorert i dag:

```
brreg-begrepskatalog, brreg-modellkatalog, digdir-modellkatalog, kartverket-modellkatalog,
ksdigital-modellkatalog, novari-modellkatalog, skatteetaten-modellkatalog,
begrepssamling-foretaksregisteret
```

## Tiltak

Legg til same manifest-flagg-sjekk i `run_gen_plantuml_parallel` som `gen-xsd`/
`gen-openapi`/`gen-asyncapi` alt brukar: hopp over `gen-plantuml` (heile raw/filter/render-
kjeda) for skjema der `build.yaml` ikkje har `plantuml: true`, med ei synleg
`log_debug`-melding om kvifor (jf. «Ingen stille feil»-prinsippet i CLAUDE.md).

Dette gjer `images.json` sitt A1-tiltak (frå `reduser-image-storleik-ghcr.md`) faktisk
korrekt: no vil verken `ensure-images`-pullinga **eller** sjølve genereringa bruke
`plantuml`-imaget for domene utan `plantuml: true`.

## Steg

1. Endra `run_gen_plantuml_parallel` i `make/10-generator-macros.mk` til å sjekke
   `build.yaml` sitt `plantuml: true`-flagg før han køyrer gen-plantuml-kjeda, med
   `log_debug`-melding ved skip (same mønster som `run_gen_with_check_parallel`).
2. Test: `make domain-begrepskatalog` (og `make domain-modellkatalog`) skal no fullføre
   utan å prøve å bruke `plantuml`-imaget i det heile.
3. Test: `make domain-samt` (eller eit anna domene med `plantuml: true`) skal framleis
   generere diagram som før — ingen regresjon for domene som faktisk brukar plantuml.
4. `actionlint` er ikkje relevant (ingen CI-workflow-fil endra).

## Utført (2026-08-04)

Lagt til manifest-flagg-sjekk i `run_gen_plantuml_parallel` (`make/10-generator-macros.mk`):
hoppar no over heile gen-plantuml-kjeda (raw → filter → render) med ei `log_debug`-melding
dersom `build.yaml` ikkje har `plantuml: true`, same mønster som `run_gen_with_check_parallel`
brukar for `openapi`/`asyncapi`.

**Verifisert:**
- `make domain-begrepskatalog` — fullførte utan feil, **ingen** forsøk på å pulle/bruke
  `plantuml`-imaget (tidlegare feilkjelde er borte).
- `make domain-modellkatalog` (12 skjema, alle `plantuml: false`) — fullførte utan feil,
  ingen `plantuml`-referanse i loggen.
- `make domain-samt` (har `plantuml: true`) — gen-plantuml køyrde som før (25.2s), begge
  SVG-diagramma (`samt-bu.svg`, `samt-bu-filtered.svg`) vart generert korrekt. Ingen
  regresjon for domene som faktisk brukar plantuml.
