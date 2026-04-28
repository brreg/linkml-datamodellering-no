

# Class: Relasjon 


_Ein kvalifisert relasjon mellom to ressursar._





URI: [dcat:Relationship](http://www.w3.org/ns/dcat#Relationship)





```mermaid
 classDiagram
    class Relasjon
    click Relasjon href "../Relasjon/"
      Relasjon : har_rolle
        
          
    
        
        
        Relasjon --> "1" Begrep : har_rolle
        click Begrep href "../Begrep/"
    

        
      Relasjon : id
        
      Relasjon : relasjon_til
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Relationship](http://www.w3.org/ns/dcat#Relationship) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |
| [har_rolle](har_rolle.md) | 1 <br/> [Begrep](Begrep.md) | Rolle ein aktør eller ressurs har i ein relasjon | direct |
| [relasjon_til](relasjon_til.md) | 1 <br/> [Uri](Uri.md) | Den relaterte ressursen i ein kvalifisert relasjon | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [relasjonar](relasjonar.md) | range | [Relasjon](Relasjon.md) |
| [Datasett](Datasett.md) | [annen_spesifikk_relasjon](annen_spesifikk_relasjon.md) | range | [Relasjon](Relasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Relationship |
| native | https://data.norge.no/linkml/dcat-ap-no/Relasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Relasjon
description: Ein kvalifisert relasjon mellom to ressursar.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
- har_rolle
- relasjon_til
slot_usage:
  har_rolle:
    name: har_rolle
    in_subset:
    - Obligatorisk
    required: true
  relasjon_til:
    name: relasjon_til
    in_subset:
    - Obligatorisk
    required: true
class_uri: dcat:Relationship

```
</details>

### Induced

<details>
```yaml
name: Relasjon
description: Ein kvalifisert relasjon mellom to ressursar.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slot_usage:
  har_rolle:
    name: har_rolle
    in_subset:
    - Obligatorisk
    required: true
  relasjon_til:
    name: relasjon_til
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Relasjon
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
  har_rolle:
    name: har_rolle
    description: Rolle ein aktør eller ressurs har i ein relasjon.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dcat:hadRole
    alias: har_rolle
    owner: Relasjon
    domain_of:
    - Relasjon
    range: Begrep
    required: true
  relasjon_til:
    name: relasjon_til
    description: Den relaterte ressursen i ein kvalifisert relasjon.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:relation
    alias: relasjon_til
    owner: Relasjon
    domain_of:
    - Relasjon
    range: uri
    required: true
class_uri: dcat:Relationship

```
</details>