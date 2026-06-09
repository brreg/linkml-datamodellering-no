# tests/

Oversikt over kva testane dekker, korleis dei køyrer, og roundtrip-status per skjema.

## Testsuite (`test_make.sh`)

`make test [SCHEMA=<sti>]` køyrer alle testar via `tests/test_make.sh`.
Kvar skjema-køyring utfører 17 testar parallelt (generatorar, lint, roundtrip).

| Test | Kva det sjekkar |
|---|---|
| `validate` | `gen-linkml` kan lese og validere skjemaet |
| `gen-jsonld` | JSON-LD-kontekst vert generert |
| `gen-python` | Python-klasser vert generert |
| `gen-jsonschema` | JSON Schema vert generert |
| `gen-rdf` | RDF/TTL-skjema vert generert |
| `gen-erdiagram` | ER-diagram vert generert |
| `gen-docs` | HTML-dokumentasjon vert generert |
| `gen-shacl` | SHACL-shapes vert generert |
| `gen-owl` | OWL-ontologi vert generert |
| `convert-rdf` | Eksempelfil kan konverterast til TTL |
| `linkml-lint` | Skjema følgjer LinkML best practices |
| `linkml-validate` | Eksempelfil er gyldig mot skjema |
| `gen-proto` | Protobuf-skjema vert generert |
| `gen-plantuml` | PlantUML-diagram vert generert |
| `mcp-validate-instance` | MCP-validator godkjenner eksempelfil |
| `roundtrip-json` | `yaml→json→yaml→json` er informasjonstap-fri |
| `roundtrip-ttl` | `yaml→ttl→yaml→json` er informasjonstap-fri |

Raskare alternativ for utvikling:

```bash
make lint SCHEMA=<sti>              # berre lint (~5 sek)
make validate-instance SCHEMA=<sti> INSTANCE=<sti>  # berre instansvalidering (~5 sek)
make roundtrip SCHEMA=<sti>         # berre roundtrip-testar (~30 sek)
make test SCHEMA=<sti>              # full suite (~3 min)
```

## Roundtrip-dekning

`make roundtrip [SCHEMA=<sti>]` køyrer berre roundtrip-testane.

**Teiknforklaring:** `✓` = passerer · `skip` = hoppet over (årsak i parentes) · `FEIL` = feiler

| Skjema | JSON | TTL | Merknad |
|---|---|---|---|
| **Nasjonale grunndata** | | | |
| `ngr-adresse` | ✓ | skip ([BUG-2]) | inlined_as_list+identifier |
| `ngr-eiendom` | ✓ | skip ([BUG-2]) | same |
| `ngr-person` | ✓ | ✓ | |
| `ngr-virksomhet` | ✓ | skip ([BUG-2]) | same |
| **FINT** | | | |
| `fint-administrasjon` | ✓ | FEIL | MappingError: No pred for fint-uri ([BUG-3]) |
| `fint-arkiv` | ✓ | ✓ | |
| `fint-okonomi` | ✓ | FEIL | same ([BUG-3]) |
| `fint-personvern` | ✓ | FEIL | same ([BUG-3]) |
| `fint-ressurs` | ✓ | ✓ | |
| `fint-utdanning` | ✓ | FEIL | same ([BUG-3]) |
| **SAMT** | | | |
| `samt-bu` | ✓ | FEIL | MappingError: No pred for samt-uri ([BUG-3]) |
| **Offentlege register** | | | |
| `enhetsregisteret-bvrinn` | ✓ | ✓ | |
| `register-over-aksjeeiere` | ✓ | ✓ | |
| **Begrepskatalog** | | | |
| `brreg-begrepskatalog` | ✓ | skip ([BUG-1]) | LangString forsvinn i TTL |
| `brreg-modellkatalog` | ✓ | skip ([BUG-1]) | same |
| **AP-NO (alle)** | skip | skip | manglar `tree_root` |
| **FAIR** | skip | skip | manglar `tree_root` |

[BUG-1]: ../specs/bugs/langstring-rdflib-roundtrip.md
[BUG-2]: ../specs/bugs/inlined-as-list-rdflib-roundtrip.md
[BUG-3]: ../specs/bugs/mappingerror-rdflib-roundtrip.md

**Tabellen skal haldast oppdatert** når skip-lista eller testresultata i `test_make.sh` endrar seg.
