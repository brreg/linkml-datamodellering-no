

# Class: ProvAttributering 


_Ein kvalifisert PROV-attributering._





URI: [prov:Attribution](http://www.w3.org/ns/prov#Attribution)





```mermaid
 classDiagram
    class ProvAttributering
    click ProvAttributering href "../ProvAttributering/"
      ProvAttributering : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [prov:Attribution](http://www.w3.org/ns/prov#Attribution) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](Datasett.md) | [annen_ansvarlig_aktor](annen_ansvarlig_aktor.md) | range | [ProvAttributering](ProvAttributering.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Attribution |
| native | https://data.norge.no/linkml/dcat-ap-no/ProvAttributering |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvAttributering
description: Ein kvalifisert PROV-attributering.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: prov:Attribution

```
</details>

### Induced

<details>
```yaml
name: ProvAttributering
description: Ein kvalifisert PROV-attributering.
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: ProvAttributering
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
class_uri: prov:Attribution

```
</details>