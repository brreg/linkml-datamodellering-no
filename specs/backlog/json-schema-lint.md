# Plan: lint/valider generert JSON Schema (meta-schema-sjekk)

## Bakgrunn

Brukaren spurde om repoet har verktøy for å linte JSON Schema, og fekk
stadfesta at det **ikkje** finst i dag: `make roundtrip-json-schema`
sjekkar berre rundtur-datakonsistens (JSON Schema → instans → attende),
ikkje om `<name>-schema.json` sjølv er eit strukturelt gyldig JSON Schema-
dokument (t.d. ugyldig `"type"`-verdi, feil forma `$ref`, motstridande
`minimum`/`maximum`).

`jq` vart vurdert og forkasta som einaste løysing — han kan stadfeste at
fila er gyldig JSON (`jq empty fil.json`), men har ingen kunnskap om JSON
Schema-spesifikasjonen (meta-schema), og kan difor ikkje fange dei faktisk
interessante feila. Brukaren bad om ei spec for eit verktøy som **også**
gjer reell meta-schema-validering, etter mønster av korleis
`gen-openapi`/`gen-asyncapi` alt "genererer og validerer".

## Kartlegging — det etablerte mønsteret

Repoet har alt **to** presedensar for "generer og valider same steg":

**`gen-openapi`** (`make/11-generator-targets.mk` linje 63, kommentar
"Generer og valider OpenAPI-spec"): custom makro
`run_gen_openapi_parallel` (`make/10-generator-macros.mk` linje 183-185)
kallar `batch-generate-instances.py --generator openapi`, som i
`run_openapi()` (linje 248-273) byggjer OpenAPI-dokumentet OG køyrer
`openapi_spec_validator` i **same prosess, same container-image**
(`python-pytest`/`PYTHON_RUN` — `openapi-spec-validator` ligg alt i
`src/assets/containers/requirements-python-test.txt`). Feilar valideringa,
feilar heile `gen-openapi` for det skjemaet (per-skjema-isolert, ikkje
heile batchen).

**`gen-asyncapi`**: same idé, men validator-steget (`asyncapi validate`,
Node.js-CLI) er **medvite ikkje** batcha i Python-prosessen (jf.
`batch-generate-instances.py` sin moduldocstring linje 18-22) — det er
framleis eit eige podman-kall til `ASYNCAPI_IMAGE`, kjeda etter
generering i `run_gen_asyncapi_parallel`-makroen
(`make/10-generator-macros.mk` linje 158-173), fordi validatoren krev ein
heilt annan runtime (Node) enn generatoren (Python).

**Kvifor JSON Schema er nærare OpenAPI-mønsteret enn AsyncAPI-mønsteret:**
ein Python-basert JSON Schema-validator (sjå Verktøyval under) treng
ingen ny container-runtime — han kan leggjast rett inn i den alt
eksisterande `python-pytest`-imaget, same stad som
`openapi-spec-validator` bur. Ingen eiga container-kall naudsynt.

**Arkitektur-skilnad å vere merksam på:** `gen-jsonschema` sjølv er i dag
kopla til den **generiske** `run_gen_parallel`-makroen
(`make/11-generator-targets.mk` linje 33: `$(call
make_gen_target,gen-jsonschema,run_gen_parallel,json-schema)`), delt med
fem andre reint-generative format (jsonld-context, python, owl, proto,
graphql) som ikkje har eller treng etterhandsaming. `gen-openapi`/
`gen-asyncapi` har **derimot** alltid hatt sine eigne custom-makroar,
nettopp fordi dei treng eit etterhandsamingssteg. Å leggje validering til
`gen-jsonschema` krev difor at han **flyttar ut** av den delte
`run_gen_parallel`-makroen og får si eiga (som openapi/asyncapi), i staden
for å prøve å parametrisere den delte makroen med eit valfritt
valideringssteg for berre éitt av dei seks formata han dekkjer.

**Fase-rekkjefølgje** (`run-domain-pipeline.sh`): `gen-jsonschema` køyrer
i Fase 1 (uavhengig), og `gen-openapi`/`gen-asyncapi`/`gen-xsd` i Fase 2
ventar spesifikt på at han er ferdig. Eit valideringssteg **inni**
`gen-jsonschema` sjølv (køyrer før han reknast som ferdig) endrar ikkje
denne fase-logikken — Fase 2 ventar framleis berre på at målet er ferdig,
uavhengig av kor mange steg det no inneheld internt.

## Verktøyval

**`check-jsonschema`** (PyPI, rein Python) — anbefalt:
- `check-jsonschema --check-metaschema <fil>` validerer at eit JSON
  Schema-dokument sjølv er gyldig mot si eiga deklarerte meta-schema
  (autodetekert frå `$schema`-feltet, eller overstyrbar)
- Rein Python, ingen ny container-runtime — kan leggjast i
  `requirements-python-test.txt` saman med `openapi-spec-validator`,
  brukt via `PYTHON_RUN` (same mønster som openapi)
- **Uavklart, sjekk ved implementering:** nøyaktig programmatisk
  API/invokeringsmåte (t.d. `check_jsonschema.cli.main([...])` kalla i
  same prosess, likt `openapi_spec_validator.__main__.main([...])` i
  `run_openapi()`, eller om biblioteket krev subprocess-kall i staden).
  Pin versjon med `>=`, same stil som resten av
  `requirements-python-test.txt`.

**Forkasta alternativ:**
- `ajv-cli` (Node.js) — ville kravd ein heilt ny container-runtime/image,
  same ulempe som AsyncAPI-mønsteret, utan tilsvarande grunngjeving (det
  finst ingen eksisterande Node-avhengigheit å dele med, i motsetnad til
  openapi_spec_validator som alt deler image med generering)
- Spectral — tyngre verktøy retta mot stil-/beste praksis-linting
  (OpenAPI/AsyncAPI-fokusert primært), meir enn det som trengst for rein
  meta-schema-gyldigheit
- `jq` åleine — stadfesta i samtalen: ingen JSON Schema-kunnskap, berre
  generell JSON-syntakssjekk. **Overflødig** dersom check-jsonschema vert
  lagt til: check-jsonschema må uansett parse JSON-fila for å validere
  henne, og vil feile med ei tydeleg feilmelding på ugyldig JSON åleine —
  ein separat jq-forsjekk gir ingen ekstra dekning, berre eit ekstra steg.

## Plan

1. Legg `check-jsonschema` til
   `src/assets/containers/requirements-python-test.txt` (same fil som
   `openapi-spec-validator`) — krev `make build-docker-python` på nytt
2. Ny funksjon `run_jsonschema_lint(schemas)` i
   `src/assets/scripts/makefile/batch-generate-instances.py`, strukturelt
   lik `run_openapi()` (linje 248-273) men **utan** eige genererings-steg
   (les berre den alt genererte `<name>-schema.json` — jsonschemagen sjølv
   køyrer framleis via `run_gen_parallel`/`LINKML_RUN`, uendra):
   - Hopp over skjema der `<name>-schema.json` manglar (åtvaring, ikkje feil
     — same `log_error(f"ÅTVARING: ... finst ikkje — hoppar over ...")`
     -mønster som `run_openapi`/`run_asyncapi`)
   - Køyr check-jsonschema si meta-schema-validering, fangar feil
     per-skjema (same isolasjonsmønster: éin broten schema stoppar ikkje
     resten av batchen)
   - Registrer i `RUNNERS`-dispatch-tabellen (linje 308-314) som
     `"jsonschema-lint": run_jsonschema_lint`
3. Ny makro `run_gen_jsonschema_parallel` i `make/10-generator-macros.mk`
   (etter mønster av `run_gen_openapi_parallel`, linje 183-185), to steg:
   ```make
   define run_gen_jsonschema_parallel
   @$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator json-schema -- $(1)
   @$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator jsonschema-lint -- $(1)
   endef
   ```
4. `make/11-generator-targets.mk` linje 33: byt
   `$(call make_gen_target,gen-jsonschema,run_gen_parallel,json-schema)`
   → `$(call make_gen_target,gen-jsonschema,run_gen_jsonschema_parallel)`
   (ingen tredje makro-parameter — `run_gen_jsonschema_parallel` treng
   ikkje `json-schema`-kind-argumentet, han er alt hardkoda inni makroen,
   likt openapi/asyncapi sine eigne makroar)
5. Oppdater `##`-kommentaren (same fil, linje 58): "Generer JSON Schema"
   → "Generer og valider JSON Schema" (matchar openapi/asyncapi-ordlyden
   presist)
6. Verifiser:
   - `make gen-jsonschema SCHEMA=<eit gyldig skjema>` — framleis grønt,
     ingen regresjon i genereringssteget
   - Injiser medvite eit ugyldig JSON Schema (t.d. `"type": "ikkje-ein-
     gyldig-type"` rett i den genererte `.json`-fila, midlertidig) og
     stadfest at `make gen-jsonschema` no faktisk feilar synleg
   - `make gen-docs`/full domenepipeline framleis fungerer (Fase
     2-avhengige `gen-openapi`/`gen-asyncapi`/`gen-xsd` ventar framleis
     korrekt)
7. Vurder om `COMMANDS.md`/mkdocs-kommandotabellane skildrar
   `gen-jsonschema` presist nok til at "Generer og valider"-ordlyden bør
   speglast der òg (same enkle sjekk som gjort for openapi/asyncapi når
   dei fekk sin valideringsomtale)

## Opne spørsmål (avklar ved implementering, ikkje i denne specen)

- Nøyaktig programmatisk API for `check-jsonschema` (sjå Verktøyval)
- Skal meta-schema-versjonen tvingast (t.d. alltid draft 2020-12) eller
  autodetekterast frå kvart skjema sin eigen `$schema`-verdi? LinkML sin
  `jsonschemagen` sitt output-`$schema`-felt bør styre standardvalet.
