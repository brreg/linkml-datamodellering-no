

# Class: ProvenanceStatement 


_Ein provenienserklæring._





URI: [dct:ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)





```mermaid
 classDiagram
    class ProvenanceStatement
    click ProvenanceStatement href "../ProvenanceStatement/"
      ProvenanceStatement : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](Datasett.md) | [eierskapshistorikk](eierskapshistorikk.md) | range | [ProvenanceStatement](ProvenanceStatement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:ProvenanceStatement |
| native | https://data.norge.no/linkml/dcat-ap-no/ProvenanceStatement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvenanceStatement
description: Ein provenienserklæring.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: dct:ProvenanceStatement

```
</details>

### Induced

<details>
```yaml
name: ProvenanceStatement
description: Ein provenienserklæring.
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: ProvenanceStatement
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
class_uri: dct:ProvenanceStatement

```
</details>