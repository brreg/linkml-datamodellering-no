

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
    * [Datasett](datasett.md)
    * [Datasettserie](datasettserie.md)
    * [Datatjeneste](datatjeneste.md)
    * [Katalog](katalog.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Resource](http://www.w3.org/ns/dcat#Resource) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Katalogpost](katalogpost.md) | [primaertema](primaertema.md) | range | [KatalogisertRessurs](katalogisertressurs.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Resource |
| native | samtbuskole:KatalogisertRessurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KatalogisertRessurs
description: Basisklasse for ressursar som kan katalogiserast.
from_schema: https://example.no/ontology/samt-bu-skole
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
from_schema: https://example.no/ontology/samt-bu-skole
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: KatalogisertRessurs
    domain_of:
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
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
    range: uriorcurie
    required: true
class_uri: dcat:Resource

```
</details>