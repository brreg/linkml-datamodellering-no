# linkml-w3c-no-profiles

Norske W3C-applikasjonsprofiler og offentlige domenemodeller i [LinkML-format](https://linkml.io/).

* mcp-linkml-generator og mcp-linkml-validator for å jobbe med og validere LinkML skjema (med mulighet for KI integrasjon). 
* generatorer for å generere artifakter på andre formater fra LinkML skjema
* dokumentasjonsportal med oversikt over alle LinkML skjemaer og genererte artifakter

[koderepository](https://github.com/brreg/linkml-w3c-no-profiles)

## Kom i gang

**Føresetnadar:** [Podman](https://podman.io/) (rootless), WSL2 og GNU make.

```bash
# 1. Bygg container-images (éin gong)
make linkml-build-docker && make python-build-docker && make mcp-val-build
```
```bash
# 2. Lag eit nytt schema
make new-model NAME=mitt-register DOMAIN=oreg
```
```bash
# 3. Valider mot minimumskrav
make mcp-validate SCHEMA=src/linkml/oreg/mitt-register/mitt-register-schema.yaml POLICY=bronze
```
```bash
# 4. Generer artefaktar og sjå resultatet
make oreg && make publish && make docs-serve   # → http://localhost:8000
```

Nye skjema under `src/linkml/<domene>/<namn>/` vert oppdaga automatisk.

For full rettleiing om modellering, validering og importar: [Ny domenemodell](ny-domenemodell.md).


## Skjema og struktur

| Domene | Skjema | Beskriving | Dokumentasjon
|---|---|---|---|
| ap-no | common-ap-no | Felles slot-definisjonar for alle AP-NO-profiler |
| ap-no | cpsv-ap-no | Offentlege tenester og hendingar | [data.norge.no/specification/cpsv-ap-no](https://data.norge.no/specification/cpsv-ap-no)
| ap-no | dcat-ap-no | Datakatalogar og datasett | [data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no)
| ap-no | dqv-ap-no | Datakvalitet | [data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no)
| ap-no | modelldcat-ap-no | Informasjonsmodellar | [data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no)
| ap-no | skos-ap-no | Begrepssamlingar | [data.norge.no/specification/skos-ap-no-begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| ap-no | xkos-ap-no | Utvidet klassifikasjon | [data.norge.no/specification/xkos-ap-no](https://data.norge.no/specification/xkos-ap-no)
| fair | fair-metadata | FAIR-metadataoverbygning (F/A/I/R-prinsippa) | [www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)
| fint | fint-common | Felles klassar for FINT | 
| fint | fint-administrasjon | Lønn, arbeidsforhold, organisasjon | [informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)
| fint | fint-arkiv | Sak, journal, dokument | [informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)
| fint | fint-okonomi | Økonomi og rekneskap | [informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)
| fint | fint-personvern | Personvernmeldingar | [informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)
| fint | fint-ressurs | Ressursar | [informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)
| fint | fint-utdanning | Utdanning og skole | [informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)
| ngr | ngr-adresse | Adresse | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)
| ngr | ngr-eiendom | Fast eiendom, matrikkelenhet og bygning | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)
| ngr | ngr-person | Person, identifikasjon og familierelasjonar | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Person](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)
| ngr | ngr-virksomhet | Verksemder, roller og organisasjonsstruktur | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)
| oreg | register-over-aksjeeiere | Aksjeeigarar og eigendelar |
| samt | samt-bu | Skolar og barnehagar | [docs.samt-bu.no/om/](https://docs.samt-bu.no/om/)

**AP-NO-profilane** og **FAIR-metadata** er schema utan `tree_root` — dei er meint å importerast av domenemodeller (som har `tree_root`).

Skjema ligg under `src/linkml/<domene>/<skjema>/`.  
Øvrig struktur:

```
src/
├── assets/                 # Containerar, skript og malar
├── linkml/                 # LinkML skjemaer
├── mcp-linkml-validator/   # MCP-server: policy-basert validering
├── mcp-linkml-generator/   # MCP-server: JSON Schema → LinkML
└── templates/              # Jinja2 templates for make gen-docs

examples/    # Eksempeldata per domene
tests/       # Testar og fixtures
generated/   # Genererte artefaktar (ikkje innsjekka i git)
mkdocs/      # Dokumentasjonsportal (MkDocs Material)
tmp/         # Midlertidige filer. F.eks json-schema som skal brukes i mcp-linkml-generator kan legges her.
```
