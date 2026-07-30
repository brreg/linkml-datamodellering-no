# referanse

## Om denne modellen

Referanseskjema for nye utviklarar — viser alle hovudmønster brukte i dette repoet.

Skjemaet demonstrerer alle hovudmønster i repoet: containerklasse, globale slots, import-hierarki, URI-mapping, fleirspråklege strengar, obligatorisk/anbefalt/valgfri-klassifisering og lenking framfor inlining.

**Typisk brukar:** Nye utviklarar som lærer LinkML-modellering i dette repoet — skjemaet vert ikkje brukt i produksjon.

**Nøkkelklasser:** `ReferanseContainer` (containerklasse), `Eksempelressurs`, `Eksempelkatalog`.



---

## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/referanse-v1.3.0/src/linkml/referanse/referanse/referanse-schema.yaml
```

### Valider skjemaet mot bronze-policy

```bash
make mcp-validate SCHEMA=src/linkml/referanse/referanse/referanse-schema.yaml
```

### Valider datafil mot LinkML-skjemaet

```bash
make validate-instance SCHEMA=src/linkml/referanse/referanse/referanse-schema.yaml INSTANCE=mine-data.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from referanse_model import Ressurs

ressurs = yaml_loader.load('mine-data.yaml', target_class=Ressurs)
```


---

## Avhengigheiter (4) {#avhengigheiter}

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types  # direkte import
└── common-ap-no-schema  # transitiv import
    └── dqv-core-schema  # transitiv import
        └── dcat-ap-no-schema  # direkte import
```

*Sjå [Importhierarki](../../importhierarki.md) for oversikt over heile repoet sitt importhierarki.*

*Importerte modeller: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [common-ap-no](../../ap-no/common-ap-no/#metadata), [dcat-ap-no](../../ap-no/dcat-ap-no/#metadata), [dqv-core](../../ap-no/dqv-core/#metadata)*



## Datamodell

Kjelde-datamodell i LinkML-format: [`referanse-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse/referanse-schema.yaml)


---

## Generated artifacts (1) {#generated-artifacts}

| Artefakt | Fil |
|----------|-----|
| JSON-LD kontekst | [referanse-context.jsonld](referanse-context.jsonld) |

*Full byggekonfigurasjon: [build.yaml](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse/build.yaml)*

---

## Valideringsresultat

*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*

---

## Versjonslog


### [1.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/referanse-v1.2.0...referanse-v1.3.0) (2026-07-30)


#### Features

* **metadata:** dynamisk README-generering frå skjema-metadata ([53def55](https://github.com/brreg/linkml-datamodellering-no/commit/53def559d46e92c604ff429b46be90381f907eaf))

### [1.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/referanse-v1.1.0...referanse-v1.2.0) (2026-07-10)


#### Features

* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([20d8bf8](https://github.com/brreg/linkml-datamodellering-no/commit/20d8bf8c0e3d5ed31c608ece6bf5d64d7802b9af))


#### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([dbda72a](https://github.com/brreg/linkml-datamodellering-no/commit/dbda72ac21c417c8e31e97fa7832fbc993242f76))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

### [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/referanse-v1.0.3...referanse-v1.1.0) (2026-07-09)


#### Features

* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))

### [1.0.3](https://github.com/brreg/linkml-datamodellering-no/compare/referanse-v1.0.2...referanse-v1.0.3) (2026-07-04)


#### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

### [1.0.2](https://github.com/brreg/linkml-datamodellering-no/compare/referanse-v1.0.1...referanse-v1.0.2) (2026-07-01)


#### Bug Fixes

* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([6e4d623](https://github.com/brreg/linkml-datamodellering-no/commit/6e4d623d1a5f91b472748d45942e8a4fb05ad53b))

### [1.0.1](https://github.com/brreg/linkml-datamodellering-no/compare/referanse-v1.0.0...referanse-v1.0.1) (2026-06-19)


#### Bug Fixes

* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))


---

## Kontakt

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

