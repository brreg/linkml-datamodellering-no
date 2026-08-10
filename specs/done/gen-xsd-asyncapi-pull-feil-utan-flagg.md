# gen-xsd/gen-asyncapi feilar med "pull localhost" for domene utan xsd/asyncapi-flagg

## Bakgrunn

Brukaren limte inn feilloggen frå ein feila `generate`-workflow-køyring.
`make domain-ap-no` feila i to grupper:

```
Error: initializing source docker://localhost/avrotize-local:latest: ...
make[1]: *** [make/11-generator-targets.mk:37: gen-xsd] Error 125
...
Error: initializing source docker://localhost/asyncapi-cli-minimal:latest: ...
make[1]: *** [make/11-generator-targets.mk:38: gen-asyncapi] Error 125
```

Retry-logikken i `generate.yml` prøvde 3 gonger, alle feila likt.

## Rotårsak

`generate.yml` sitt steg «Detekter påkrevde images» (linje 174–212) scannar
`build.yaml` for kvart domene og legg berre `avrotize-local`/
`asyncapi-cli-minimal` til i lista over images som skal lastast ned frå
GHCR **dersom** minst eitt skjema i domenet har `xsd: true`/`asyncapi: true`.//
I dag er det berre `src/linkml/samt/samt-bu/build.yaml` som har desse
flagga — ingen `ap-no`-skjema treng dei. Difor lastar CI aldri
`avrotize-local`/`asyncapi-cli-minimal` inn i podman for `domain-ap-no`.

`run_gen_xsd_parallel` og `run_gen_asyncapi_parallel`
(`make/10-generator-macros.mk`) kalla likevel **alltid** `podman run` mot
`$(AVROTIZE_IMAGE)`/`$(ASYNCAPI_IMAGE)`, uavhengig av om nokon av skjemaa i
`$(1)` faktisk treng generatoren — filtreringa mot `xsd: true`/
`asyncapi: true` skjedde først **inni** kontainer-scriptet
(`batch-gen-xsd.sh`/`batch-asyncapi-validate.sh`), ikkje før `podman run`
vart kalla. Alle andre generatorar (owl, rdf, shacl, openapi, m.fl.) brukar
`$(LINKML_RUN)`/`$(PYTHON_RUN)` — image som er `always_required: true` og
difor alltid lasta lokalt, så det problemet oppstår ikkje der.

Når podman får eit ukvalifisert imagenamn (`localhost/avrotize-local:latest`)
som ikkje finst lokalt, prøver det å pulle frå ein registry kalla
`localhost` — som ikkje finst i CI-miljøet — og feilar med
`connection refused`.

## Tiltak

1. **`make/10-generator-macros.mk`** — gate `podman run`-kallet i
   `run_gen_xsd_parallel` og validerings-fasen i `run_gen_asyncapi_parallel`
   bak ei sjekk av om minst eitt skjema i `$(1)` har `xsd: true`/
   `asyncapi: true` i sin `build.yaml` (same grep-mønster som skripta sjølv
   brukar). Ingen treff → hopp over `podman run` heilt, berre logg
   `log_debug "... — køyrer: (ingen)"` (same stil som
   `batch-generate-instances.py` sin `log_debug`), i tråd med korleis dei
   andre generatorane oppfører seg for tomme lister.
2. Verifiser med `make -n gen-xsd DOMAIN=ap-no` / `DOMAIN=samt` og
   `make -n gen-asyncapi DOMAIN=ap-no` / `DOMAIN=samt` at:
   - `ap-no` (ingen skjema med flagget) ikkje lenger inneheld `podman run`
     mot avrotize/asyncapi-imaget.
   - `samt` (har `samt-bu` med begge flagga) framleis inneheld kallet.
3. Køyr `LOGLVL=DEBUG make gen-xsd DOMAIN=ap-no` reelt (utan podman-kall
   forventa) og stadfest at det fullfører utan feil.

## Utført

Tiltak 1–3 gjennomførte og verifiserte:
- `run_gen_xsd_parallel`: podman-kallet er no gata bak ei `grep -q "^  xsd: true"`-sjekk over alle build.yaml for skjemaa i `$(1)`.
- `run_gen_asyncapi_parallel`: valideringsfasen (andre `podman run`) er tilsvarande gata bak `grep -q "^  asyncapi: true"`.
- `make -n gen-xsd DOMAIN=ap-no` og `make -n gen-asyncapi DOMAIN=ap-no` viser ingen `podman run` mot avrotize/asyncapi-imaget lenger.
- `make -n gen-xsd DOMAIN=samt` og `make -n gen-asyncapi DOMAIN=samt` viser at kallet framleis skjer (samt-bu har begge flagga).
- `LOGLVL=DEBUG make gen-xsd DOMAIN=ap-no` køyrde reelt og fullførte utan feil, med `[DEBUG] xsd (xsd: true) — køyrer: (ingen)`.
