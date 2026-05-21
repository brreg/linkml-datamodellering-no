# linkml-datamodellering-no

Norske W3C-applikasjonsprofiler og offentlige domenemodeller i [LinkML-format](https://linkml.io/).

> LinkML er et åpen-kildekode modelleringsspråk der du skriver skjema i YAML som beskriver datastrukturen din, og som du kan bruke til å generere skjema, data, diagram og dokumentasjon i andre formater ([LinkML generators](https://linkml.io/linkml/generators/index.html)).

Dette [koderepositoryet](https://github.com/brreg/linkml-datamodellering-no) inneholder:
* LinkML modeller for Norske W3C-applikasjonsprofiler og offentlige domenemodeller for gjenbruk.
* mcp-linkml-generator og mcp-linkml-validator for å generere og validere LinkML-skjemaer (med mulighet for KI-integrasjon).
* LinkML-generatorer for å produsere artefakter i andre formater fra LinkML-skjemaer.
* Dokumentasjonsportal med oversikt over alle LinkML-skjemaer og genererte artefakter.



## Kom i gang

**Forutsetninger:** [Podman](https://podman.io/) (rootless), WSL2 og GNU make.

```bash
# 0. Sjekk at alt er på plass
make check-prereqs
```
```bash
# 1. Bygg container-images (én gang)
make linkml-build-docker && make python-build-docker && make mcp-val-build && make mcp-gen-build
```

> Bytt ut `domene` og `modellnavn` i kommandoene nedenfor med dine egne verdier.

```bash
# 2. Lag et nytt tomt LinkML-skjema (med tilhørende filstruktur og eksempelfil)
make new-model NAME=modellnavn DOMAIN=domene

# 2b. (hvis ønskelig): generer LinkML-skjema fra eksisterende JSON Schema
# Legg JSON Schema-filen i tmp/, f.eks. tmp/modellnavn.json
make mcp-generate SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Flytt den til src/linkml/domene/modellnavn/
```
```bash
# 3. Valider LinkML-skjema mot minimumskrav
make mcp-validate SCHEMA=src/linkml/domene/modellnavn/modellnavn-schema.yaml POLICY=bronze
```
```bash
# 4. Generer artefakter fra LinkML-skjema og se resultatet
make domene && make publish && make docs-serve   # → http://localhost:8000
```

Nye skjemaer under `src/linkml/<domene>/<modellnavn>/` blir oppdaget automatisk.

For full veiledning om modellering, validering og importer: se [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/) i dokumentasjonsportalen.

Se [CLAUDE.md](CLAUDE.md) for modelleringsprinsipper og [COMMANDS.md](COMMANDS.md) for alle tilgjengelige kommandoer.

## Skjemaer og struktur

### Domener

| Domene | Beskrivelse | Dokumentasjon |
|---|---|---|
| ap-no | Norske W3C-applikasjonsprofiler — DCAT, SKOS, CPSV, DQV m.fl. Importeres av domenemodeller. | [RDF-baserte maskinlesbare ressurser](https://data.norge.no/showroom/overview)
| fair | FAIR-metadataoverbygning — **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. Kan importeres av alle domenemodeller. | [FAIR principles](https://www.go-fair.org/fair-principles/)
| ngr | Nasjonale grunndata — adresse, eiendom, person og virksomhet. | [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#OmNasjonaleGrunndata)
| oreg | Offentlige registre. |
| fint | FINT felleskomponent — integrasjonsmodeller for fylkeskommunal sektor. | [FINT informasjonsmodell](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20)
| samt | SAMT — integrasjonsmodeller for kommunesektoren. | [SAMT prosjektet](https://docs.samt-bu.no/om/)

### Skjemaer

| Domene | Skjema | Beskrivelse | Dokumentasjon
|---|---|---|---|
| ap-no | common-ap-no | Felles slot-definisjoner for alle AP-NO-profiler |
| ap-no | cpsv-ap-no | Offentlige tjenester og hendelser | [data.norge.no/specification/cpsv-ap-no](https://data.norge.no/specification/cpsv-ap-no)
| ap-no | dcat-ap-no | Datakataloger og datasett | [data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no)
| ap-no | dqv-ap-no | Datakvalitet | [data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no)
| ap-no | modelldcat-ap-no | Informasjonsmodeller | [data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no)
| ap-no | skos-ap-no | Begrepssamlinger | [data.norge.no/specification/skos-ap-no-begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| ap-no | xkos-ap-no | Utvidet klassifikasjon | [data.norge.no/specification/xkos-ap-no](https://data.norge.no/specification/xkos-ap-no)
| fair | fair-metadata | FAIR-metadataoverbygning (F/A/I/R-prinsippene) | [www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)
| fint | fint-common | Felles klasser for FINT |
| fint | fint-administrasjon | Lønn, arbeidsforhold, organisasjon | [informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)
| fint | fint-arkiv | Sak, journal, dokument | [informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)
| fint | fint-okonomi | Økonomi og regnskap | [informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)
| fint | fint-personvern | Personvernmeldinger | [informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)
| fint | fint-ressurs | Ressurser | [informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)
| fint | fint-utdanning | Utdanning og skole | [informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)
| ngr | ngr-adresse | Adresse | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)
| ngr | ngr-eiendom | Fast eiendom, matrikkelenhet og bygning | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)
| ngr | ngr-person | Person, identifikasjon og familierelasjoner | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Person](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)
| ngr | ngr-virksomhet | Virksomheter, roller og organisasjonsstruktur | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)
| oreg | register-over-aksjeeiere | Aksjeeiere og eiendeler |
| samt | samt-bu | Skoler og barnehager | [docs.samt-bu.no/om/](https://docs.samt-bu.no/om/)

**AP-NO-profilene** og **FAIR-metadata** er skjemaer uten `tree_root` — de er ikke selvstendige, men er ment å importeres av domenemodeller.

Skjemaer ligger under `src/linkml/<domene>/<skjema>/`.  

## Katalogstruktur

```
linkml-datamodellering-no/
├──src/
│   ├── assets/                 # Containere, skript og maler
│   ├── linkml/                 # LinkML-skjemaer
│   ├── mcp-linkml-validator/   # MCP-server: policy-basert validering
│   ├── mcp-linkml-generator/   # MCP-server: JSON Schema → LinkML
│   └── templates/              # Jinja2-maler for make gen-docs
│
├──examples/    # Eksempeldata per domene
├──tests/       # Tester og fixtures
├──generated/   # Genererte artefakter (ikke sjekket inn i git)
├──mkdocs/      # Dokumentasjonsportal (MkDocs Material)
├──tmp/         # Midlertidige filer, f.eks. JSON Schema-filer til mcp-linkml-generator
```
