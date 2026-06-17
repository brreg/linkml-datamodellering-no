# Kjente feil

Oversikt over alle kjente feil i repoet. Kvar feil har éi eiga fil med fullstendig analyse.

Når du legg til ein skip-betingelse i `tests/test_make.sh`, skal det alltid finnast ei tilhøyrande fil her.

## Indeks

| ID | Tittel | Status | Komponent | Berørte skjema |
|---|---|---|---|---|
| [BUG-1](langstring-rdflib-roundtrip.md) | `rdflib_loader` rekonstruerer ikkje `LangString` frå TTL | `upstream` | `linkml-runtime` | `brreg-begrepskatalog`, `brreg-modellkatalog` |
| [BUG-2](inlined-as-list-rdflib-roundtrip.md) | `rdflib_loader` feiler på `inlined_as_list` med `identifier: true` | `upstream` | `linkml-runtime` | `ngr-adresse`, `ngr-eiendom`, `ngr-virksomhet` |
| [BUG-3](mappingerror-rdflib-roundtrip.md) | `rdflib_loader` kastar `MappingError` for domene-URI-ar utan eksplisitt `slot_uri` | `open` | `linkml-runtime` | `fint-administrasjon`, `fint-okonomi`, `fint-personvern`, `fint-utdanning`, `samt-bu` |
| [BUG-4](lint-validate-flag-deprecated.md) | `linkml lint --validate` er avvikla og vert fjerna i 1.13.0 | `løyst` | `Makefile` | alle skjema |

## Statusforklaring

| Status | Tydning |
|---|---|
| `open` | Feilen er dokumentert, ingen workaround eller løysing er på plass |
| `upstream` | Workaround er på plass; permanent fix krev endring i eit eksternt bibliotek |
| `workaround` | Intern workaround er på plass; ingen upstream-bug |
| `løyst` | Feilen er fiksa og workarounds er fjerna |
