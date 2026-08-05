# Parallelliser gen-informasjonsmodell-instance i domain_target

## Bakgrunn

`domain_target` (`make/20-domain-targets.mk`) parallelliserer alle
generator-steg via `run-parallel-gen.sh` (gen-linkml, gen-jsonld-context,
gen-shacl, gen-python, gen-json-schema, gen-owl, gen-rdf, gen-doc,
gen-erdiagram, gen-proto, gen-plantuml, gen-openapi, gen-asyncapi) —
unntatt siste steg, `gen-informasjonsmodell-instance`, som framleis køyrer
seriell via `run_gen_informasjonsmodell_instance`
(`make/30-instances.mk`). For domene med mange skjema (t.d. ap-no med 10
skjema) gir dette unødvendig lang byggetid sidan steget må vente på at
kvart skjema er ferdig før neste startar.

`generate-informasjonsmodell.py` er trygt å parallellisere:
- Skriv berre til sin eigen `metadata/<modell>-manifest.yaml` per skjema —
  ingen delt tilstand eller aggregering på tvers av skjema.
- Ingen `build.yaml`-generatorflagg gatar steget i dag (køyrer
  uvilkårleg for alle skjema i domenet).
- Må framleis køyre *etter* dei andre generator-stega, sidan
  `discover_artifacts()` glob-ar `generated/<domain>/<modell>/` for
  artefaktar (`.ttl`, `.json`, `.puml`, `-openapi.yaml` osv.) — denne
  rekkjefølgja er alt sikra ved at kallet ligg sist i `domain_target`.

## Steg

1. Legg til `run_gen_informasjonsmodell_instance_parallel`-makro i
   `make/30-instances.mk`, etter same mønster som
   `run_gen_asyncapi_parallel`/`run_gen_openapi_parallel` (bruk
   `run_logged` inni `GEN_CMD`, ingen `--flag` sidan ingen manifest-gate
   finst).
2. Oppdater `make/20-domain-targets.mk` til å kalle den nye
   `_parallel`-makroen i staden for den serielle.
3. Behald den serielle `run_gen_informasjonsmodell_instance` uendra —
   framleis brukt av den frittståande `make gen-informasjonsmodell-instance`
   SCHEMA=/DOMAIN=-targeten.
4. Verifiser med `make domain-ap-no` (eller eit mindre domene) at alle
   manifestfiler vert generert korrekt og at rekkjefølgja mot andre
   generator-steg held.

## Handlingsliste

- [x] `make/30-instances.mk`: ny `run_gen_informasjonsmodell_instance_parallel`
- [x] `make/20-domain-targets.mk`: bruk ny makro i `domain_target`
- [x] Verifiser med testkøyring

## Utført

Verifisert med mellombels test-target mot `domain-oreg` (2 skjema):
begge manifestfilene (`enhetsregisteret-bvrinn-manifest.yaml`,
`register-over-aksjeeiere-manifest.yaml`) vart generert korrekt og
parallelt via `run-parallel-gen.sh`, med same innhald som den serielle
varianten produserer. Testfilene og det mellombelse target vart fjerna
etter verifisering.
