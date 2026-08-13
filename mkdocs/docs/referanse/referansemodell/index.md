# referansemodell

[![Lisens](https://img.shields.io/badge/NLOD-2.0-blue)]()
[![Status](https://img.shields.io/badge/status-Under_utvikling-orange)]()
[![Versjon](https://img.shields.io/badge/versjon-1.3.0-blue)]()
[![Validering](https://img.shields.io/badge/bronze-ukjent-lightgrey)]()
[![Endringsdato](https://img.shields.io/badge/endringsdato-2026--07--30-blue)]()


## Om denne modellen

> Denne sida dokumenterer LinkML-modellen referansemodell, inkludert klassar, eigenskapar, datatypar, valideringsresultat og genererte artefakter. Informasjonen er generert automatisk frå skjemaet og tilhøyrande byggeproses.

Referanseskjema for nye utviklarar — viser alle hovudmønster brukte i dette repoet.

Skjemaet demonstrerer alle hovudmønster i repoet: containerklasse, globale slots, import-hierarki, URI-mapping, fleirspråklege strengar, obligatorisk/anbefalt/valgfri-klassifisering og lenking framfor inlining.

**Typisk brukar:** Nye utviklarar som lærer LinkML-modellering i dette repoet — skjemaet vert ikkje brukt i produksjon.




---

## Kom i gang

> Her finn du døme på korleis du importerer, validerer og brukar modellen i eigne prosjekt.

### Importer i egne LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/referansemodell-v1.3.0/src/linkml/referanse/referansemodell/referansemodell-schema.yaml
```

### Valider skjemaet mot bronze-policy

```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/referanse/referansemodell/referansemodell-schema.yaml
```

### Valider datafil mot LinkML-skjemaet

```bash
make validate-instance SCHEMA=src/linkml/referanse/referansemodell/referansemodell-schema.yaml INSTANCE=mine-data.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from referansemodell_model import Ressurs

ressurs = yaml_loader.load('mine-data.yaml', target_class=Ressurs)
```


---

## Modellmetadata {#metadata}

> Denne oversikta viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | referansemodell-schema |
| Title | Referansemodell |
| Description | Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur |
| Schema URI | [https://data.norge.no/linkml/referansemodell](https://data.norge.no/linkml/referansemodell) |
| Versjon | 1.3.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgjevar | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-07-30 |
| Utgivelsesdato | 2026-07-09 |
| Imports | linkml:types<br>../../ap-no/dcat-ap-no/dcat-ap-no-schema |


---

## Avhengigheiter (4) {#avhengigheiter}

> Denne modellen importerer og gjenbruker komponentar frå andre skjema. 
> Importerte klassar og eigenskapar kan vere synlege i diagram, valideringsrapportar og andre analysar sjølv om dei ikkje blir lista som lokale element i denne modellen.

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types  # direkte import
└── common-ap-no-schema  # transitiv import
    └── dqv-core-schema  # transitiv import
        └── dcat-ap-no-schema  # direkte import
```

*Sjå [Importhierarki](../../arkitektur/importhierarki.md) for oversikt over heile repoet sitt importhierarki.*

*Importerte modeller: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [common-ap-no](../../ap-no/common-ap-no/#datamodell), [dcat-ap-no](../../ap-no/dcat-ap-no/#datamodell), [dqv-core](../../ap-no/dqv-core/#datamodell)*



## Datamodell

> Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette skjemaet.

Kjelde-datamodell i LinkML-format: [`referansemodell-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referansemodell/referansemodell-schema.yaml)

---


*Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), [dcat-ap-no](../../ap-no/dcat-ap-no/#classes), [dqv-core](../../ap-no/dqv-core/#classes)*

---


---

## Genererte artefakter (2) {#generated-artifacts}

> Denne seksjonen listar maskinlesbare artefakt som er genererte frå skjemaet. Artefakta blir brukte til validering, integrasjon, dokumentasjon og kodegenerering.

| Artefakt | Fil |
|----------|-----|
| Modellmanifest ihht Modelldcat-ap-no | [referansemodell-manifest.yaml](referansemodell-manifest.yaml) |
| ER-diagram (Mermaid) | [referansemodell-erdiagram.md](referansemodell-erdiagram.md) |

*Full byggekonfigurasjon: [build.yaml](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referansemodell/build.yaml)*

---

## Valideringsresultat

> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.

*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*

---

## Versjonslog

> Versjonsloggen viser endringar mellom publiserte versjonar av modellen. Innhaldet blir generert frå prosjektets release-historikk.


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

> Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar.

**Forvaltningsansvarleg:** [Brønnøysundregistra](https://data.norge.no/organizations/974760673)

**Kontakt:** [Brønnøysundregistra - Kontakt](https://brreg.no/kontakt/modellforvaltning)

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

