# Kjente feil og avgrensingar

Oversikt over alle kjente feil og avgrensingar i repoet. Kvar feil har éi eiga fil med fullstendig analyse.

Når du legg til ein skip-betingelse i `tests/test_make.sh`, skal det alltid finnast ei tilhøyrande fil her.

## For eksterne brukarar

Denne oversikta er skrive for tekniske brukarar og bidragsytarar. Dersom du berre brukar repoet for datamodellering, les:

- [Kjende avgrensingar](../../mkdocs/docs/index.md#kjende-avgrensingar) (brukarvendt oversikt)
- "Kjende avgrensingar"-seksjonane i kvar rettleiing (t.d. [ny-domenemodell.md](../../mkdocs/docs/ny-domenemodell.md#kjende-avgrensingar))

## PoC-status

Dette repoet er ein **Proof of Concept** og har fleire kjente avgrensingar:

### Validering og testing
- **BUG-1, BUG-2, BUG-3**: Roundtrip-testing (YAML → TTL → YAML) fungerer ikkje for alle skjema pga. bugs i `linkml-runtime`
- Ingen automatisk validering mot eksterne API-ar (t.d. at Los-tema faktisk eksisterer)
- Ingen automatisk sjekk for duplikate begrep eller modellar på tvers av katalogar

### Generatorar
- PlantUML-diagram vert ikkje genererte for skjema med meir enn 50 klasser (ytelsesproblem)
- JSON Schema-generatoren støttar ikkje `union_of` med meir enn to typar
- AsyncAPI-generering er eksperimentell og ikkje aktivert by default
- **BUG-6, BUG-7**: Class/slot-override av importerte element krasjar eller korrumperer genererte artefaktar

### Publisering
- Publisering til Felles Begrepskatalog/Datakatalog krev manuell koordinering med Digitaliseringsdirektoratet
- Ingen automatisk validering av at høstingsendepunkt faktisk er tilgjengelege frå data.norge.no
- Tilbaketrekking av feil-publiserte data må handterast manuelt
- **BUG-8**: Polymorf `inlined_as_list` støttes ikkje fullt ut — påverkar framtidige ModelDCAT-AP-NO-utvidingar

### Samhandling og CI/CD
- GitHub-team-konfigurasjon føresett at alle medlemmar har write-tilgang til heile repoet (ikkje berre eigne modellar)
- CI køyrer under repo-eigar sin GitHub-konto — alle organisasjonar må godta dette
- `.github/CODEOWNERS`-fila må oppdaterast manuelt basert på `CODEOWNERS.md` (ingen automatisk synkronisering)

Sjå [GOVERNANCE.md](../../GOVERNANCE.md) for kva stabilitet og support du kan forvente i PoC-fasen.

## Indeks

| ID | Tittel | Status | Komponent | Berørte skjema |
|---|---|---|---|---|
| [BUG-1](langstring-rdflib-roundtrip.md) | `rdflib_loader` rekonstruerer ikkje `LangString` frå TTL | `upstream` | `linkml-runtime` | `brreg-begrepskatalog`, `brreg-modellkatalog`, `digdir-modellkatalog`, `novari-modellkatalog`, `ksdigital-modellkatalog`, `skatteetaten-modellkatalog`, `kartverket-modellkatalog` |
| [BUG-2](inlined-as-list-rdflib-roundtrip.md) | `rdflib_loader` feiler på `inlined_as_list` med `identifier: true` | `upstream` | `linkml-runtime` | `ngr-adresse`, `ngr-eiendom`, `ngr-virksomhet` |
| [BUG-3](mappingerror-rdflib-roundtrip.md) | `rdflib_loader` kastar `MappingError` for domene-URI-ar utan eksplisitt `slot_uri` | `open` | `linkml-runtime` | `fint-administrasjon`, `fint-okonomi`, `fint-personvern`, `fint-utdanning`, `samt-bu` |
| [BUG-4](lint-validate-flag-deprecated.md) | `linkml lint --validate` er avvikla og vert fjerna i 1.13.0 | `løyst` | `Makefile` | alle skjema |
| [BUG-5](instance-check-walk-skips-lists.md) | `walk()` i `instance_slot_uri_pattern`-sjekkar hoppar over lister av objekt | `løyst` | `mcp-linkml-validator` | alle (via `felles-begrepskatalog`-policyen) |
| [BUG-6](dqv-standard-class-override.md) | Class override av importert klasse krasjar (python/rdf/jsonld-context) eller korrumperer (json-schema/shacl/owl) avhengig av generator | `workaround` | `linkml` | `dqv-ap-no`, `samt-bu` |
| [BUG-7](duplicate-slot-merge-konflikt.md) | Duplikat globalt slot-namn i importgrafen krasjar `merge_dicts` (slot-variant av BUG-6) | `workaround` | `linkml` | `modelldcat-ap-no`, `brreg-modellkatalog` |
| [BUG-8](polymorphic-inlined-list-yaml-loader.md) | YAML/SchemaLoader-basert lasting støttar ikkje polymorf `inlined_as_list` (subklasseinstansar i delt liste) | `open` | `linkml-runtime` | `modelldcat-ap-no` (modelldel), `*-modellkatalog` (planlagt, MD5) |

## Statusforklaring

| Status | Tydning |
|---|---|
| `open` | Feilen er dokumentert, ingen workaround eller løysing er på plass |
| `upstream` | Workaround er på plass; permanent fix krev endring i eit eksternt bibliotek |
| `workaround` | Intern workaround er på plass; ingen upstream-bug |
| `løyst` | Feilen er fiksa og workarounds er fjerna |
