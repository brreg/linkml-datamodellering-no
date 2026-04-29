# LINKML-W3C-NO-PROFILES

Dette repoet modellerer alle norske W3C applikasjonsprofiler på LinkML format for gjenbruk.

## Utvikling
>Prosjektet er utstyrt med agents fil CLAUDE.md for å gi instruksjoner til LLM. 


## Krav

- [Podman](https://podman.io/) — alle LinkML-kommandoar køyrer via `docker.io/linkml/linkml:latest`

## Kommandoar

| Kommando | Beskriving |
|---|---|
| `make` | Køyr testar og generer dokumentasjon |
| `make test` | Lint alle skjema og valider alle eksempelfiler |
| `make validate` | Valider skjema mot LinkML-metaskjemaet |
| `make gen-jsonld` | Generer JSON-LD kontekst (`*-context.jsonld`) |
| `make gen-shacl` | Generer SHACL shapes (`*-shapes.ttl`) |
| `make gen-python` | Generer Python-dataklassar (`*-model.py`) |
| `make gen-jsonschema` | Generer JSON Schema (`*-schema.json`) |
| `make gen-owl` | Generer OWL/Turtle-ontologi (`*-ontology.ttl`) |
| `make docs` | Generer HTML-dokumentasjon til `docs/` |
| `make clean` | Slett `generated/` og `docs/` |

Genererte artefakter hamnar i `generated/ap-no/<profil>/` og `generated/ngr/<modell>/`.

### Enkeltskjema direkte

```bash
podman run --rm -v "$(pwd):/work" -w /work docker.io/linkml/linkml:latest \
  linkml validate --schema src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml \
  tests/fixtures/dcat-ap-no-fixture.yaml
```

## Katalogstruktur

```
src/linkml/
├── ap-no/                          # W3C applikasjonsprofiler (AP-NO)
│   ├── common/
│   │   └── common-ap-no-schema.yaml    # Felles slot-definisjonar (delt av alle AP-NO)
│   ├── dcat-ap-no/
│   │   └── dcat-ap-no-schema.yaml      # Datakatalogar og datasett
│   ├── dqv-ap-no/
│   │   └── dqv-ap-no-schema.yaml       # Datakvalitet
│   ├── cpsv-ap-no/
│   │   └── cpsv-ap-no-schema.yaml      # Offentlege tenester
│   ├── skos-ap-no/
│   │   └── skos-ap-no-schema.yaml      # Begrepssamlingar
│   └── xkos-ap-no/
│       └── xkos-ap-no-schema.yaml      # Utvidet klassifikasjon
└── ngr/                            # Nasjonale grunndata (NGR) domenemodeller
    └── ngr-adresse/
        └── ngr-adresse-schema.yaml     # Adressemodell (Matrikkelen)

examples/
├── ap-no/                          # Eksempeldata for AP-NO-profilene
│   ├── dcat-ap-no-eksempel.yaml
│   ├── dqv-ap-no-eksempel.yaml
│   ├── cpsv-ap-no-eksempel.yaml
│   ├── skos-ap-no-eksempel.yaml
│   └── xkos-ap-no-eksempel.yaml
└── ngr/                            # Eksempeldata for NGR-domenemodellane
    └── ngr-adresse-eksempel.yaml

tests/
├── fixtures/                       # Testfixturer – legg til Container/tree_root for AP-NO
│   ├── dcat-ap-no-fixture.yaml
│   ├── dqv-ap-no-fixture.yaml
│   ├── cpsv-ap-no-fixture.yaml
│   ├── skos-ap-no-fixture.yaml
│   └── xkos-ap-no-fixture.yaml
└── test_schemas.sh                 # Lint og valider alle skjema og eksempel

generated/                          # Genererte artefakter (ikkje innsjekka)
├── ap-no/<profil>/                 # JSON-LD, SHACL, JSON Schema, OWL, RDF, docs
└── ngr/<modell>/                   # Same format som AP-NO
```

### Arkitekturprinsipp

**AP-NO-profiler** (`src/linkml/ap-no/`) definerer klasser og slot-ar utan `Container`/`tree_root`. Dei er meint å importerast av domenemodeller og er ikkje sjølvstendige datasett-skjema. Felles slot-ar som går att i fleire profiler ligg i `common/`.

**NGR-domenemodeller** (`src/linkml/ngr/`) er sjølvstendige og har eigen `Container`-klasse med `tree_root: true`. Dei kan importere relevante AP-NO-profiler og utvide desse med domenemodellen sin eigen kontekst.

**Testfixturer** (`tests/fixtures/`) legg til ein `Container`-klasse for kvar AP-NO-profil, slik at eksempeldata kan validerast isolert utan at AP-NO-skjemaet sjølv treng `tree_root`.