

# Class: Spraak 


_Ein språkreferanse (dct:LinguisticSystem)._





URI: [dct:LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)





```mermaid
 classDiagram
    class Spraak
    click Spraak href "../Spraak/"
      Spraak : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RegulativRessurs](RegulativRessurs.md) | [sprak](sprak.md) | range | [Spraak](Spraak.md) |
| [Distribusjon](Distribusjon.md) | [sprak](sprak.md) | range | [Spraak](Spraak.md) |
| [Datasett](Datasett.md) | [sprak](sprak.md) | range | [Spraak](Spraak.md) |
| [Katalogpost](Katalogpost.md) | [sprak](sprak.md) | range | [Spraak](Spraak.md) |
| [Katalog](Katalog.md) | [sprak](sprak.md) | range | [Spraak](Spraak.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:LinguisticSystem |
| native | https://data.norge.no/linkml/dcat-ap-no/Spraak |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Spraak
description: Ein språkreferanse (dct:LinguisticSystem).
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: dct:LinguisticSystem

```
</details>

### Induced

<details>
```yaml
name: Spraak
description: Ein språkreferanse (dct:LinguisticSystem).
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Spraak
    domain_of:
    - Frekvens
    - ProvenanceStatement
    - OdrlPolicy
    - ProvAktivitet
    - ProvAttributering
    - Tidsinstant
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - Standard
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Katalogpost
    - Spraak
    - Mediatype
    - Begrep
    - Begrepssamling
    range: uriorcurie
    required: true
class_uri: dct:LinguisticSystem

```
</details>