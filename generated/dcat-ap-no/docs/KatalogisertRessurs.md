

# Class: KatalogisertRessurs 


_Basisklasse for ressursar som kan katalogiserast._





URI: [dcat:Resource](http://www.w3.org/ns/dcat#Resource)





```mermaid
 classDiagram
    class KatalogisertRessurs
    click KatalogisertRessurs href "../KatalogisertRessurs/"
      KatalogisertRessurs <|-- Datasett
        click Datasett href "../Datasett/"
      KatalogisertRessurs <|-- Datasettserie
        click Datasettserie href "../Datasettserie/"
      KatalogisertRessurs <|-- Datatjeneste
        click Datatjeneste href "../Datatjeneste/"
      KatalogisertRessurs <|-- Katalog
        click Katalog href "../Katalog/"
      
      KatalogisertRessurs : id
        
      
```





## Inheritance
* **KatalogisertRessurs**
    * [Datasett](Datasett.md)
    * [Datasettserie](Datasettserie.md)
    * [Datatjeneste](Datatjeneste.md)
    * [Katalog](Katalog.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Resource](http://www.w3.org/ns/dcat#Resource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Katalogpost](Katalogpost.md) | [primaertema](primaertema.md) | range | [KatalogisertRessurs](KatalogisertRessurs.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Resource |
| native | https://data.norge.no/linkml/dcat-ap-no/KatalogisertRessurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KatalogisertRessurs
description: Basisklasse for ressursar som kan katalogiserast.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
class_uri: dcat:Resource

```
</details>

### Induced

<details>
```yaml
name: KatalogisertRessurs
description: Basisklasse for ressursar som kan katalogiserast.
from_schema: https://data.norge.no/linkml/dcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: KatalogisertRessurs
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
class_uri: dcat:Resource

```
</details>