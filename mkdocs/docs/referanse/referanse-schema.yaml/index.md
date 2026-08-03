# referanse-schema.yaml

[![Versjon](https://img.shields.io/badge/versjon-1.0.0-blue)]()
[![Status](https://img.shields.io/badge/status-UnderDevelopment |-blue)]()
[![Validering](https://img.shields.io/badge/bronze-ukjent-lightgrey)]()
[![Lisens](https://img.shields.io/badge/NLOD-2.0-blue)]()


## Kom i gang

> Her finn du døme på korleis du importerer, validerer og brukar modellen i eigne prosjekt.

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/referanse/referanse-schema.yaml/referanse-schema.yaml-schema.yaml
```

### Valider skjemaet mot bronze-policy

```bash
make mcp-validate SCHEMA=src/linkml/referanse/referanse-schema.yaml/referanse-schema.yaml-schema.yaml
```

### Valider datafil mot LinkML-skjemaet

```bash
make validate-instance SCHEMA=src/linkml/referanse/referanse-schema.yaml/referanse-schema.yaml-schema.yaml INSTANCE=mine-data.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from referanse_schema.yaml_model import Container

container = yaml_loader.load('mine-data.yaml', target_class=Container)
```


---


## Datamodell

> Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette skjemaet.

Kjelde-datamodell i LinkML-format: [`referanse-schema.yaml-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse-schema.yaml/referanse-schema.yaml-schema.yaml)

---


---


---

## Genererte artefakter (1) {#generated-artifacts}

> Denne seksjonen listar maskinlesbare artefakt som er genererte frå skjemaet. Artefakta blir brukte til validering, integrasjon, dokumentasjon og kodegenerering.

| Artefakt | Fil |
|----------|-----|
| ER-diagram (Mermaid) | [referanse-schema.yaml-erdiagram.md](referanse-schema.yaml-erdiagram.md) |

*Full byggekonfigurasjon: [build.yaml](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse-schema.yaml/build.yaml)*

---

## Valideringsresultat

> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.

*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*

---

## Kontakt

> Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar.

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

