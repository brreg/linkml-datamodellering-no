

# Class: OdrlPolicy 


_Ein ODRL-policy._





URI: [odrl:Policy](http://www.w3.org/ns/odrl/2/Policy)





```mermaid
 classDiagram
    class OdrlPolicy
    click OdrlPolicy href "../OdrlPolicy/"
      OdrlPolicy : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [odrl:Policy](http://www.w3.org/ns/odrl/2/Policy) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Distribusjon](Distribusjon.md) | [policy](policy.md) | range | [OdrlPolicy](OdrlPolicy.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odrl:Policy |
| native | https://data.norge.no/linkml/dcat-ap-no/OdrlPolicy |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OdrlPolicy
description: Ein ODRL-policy.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: odrl:Policy

```
</details>

### Induced

<details>
```yaml
name: OdrlPolicy
description: Ein ODRL-policy.
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: OdrlPolicy
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
class_uri: odrl:Policy

```
</details>