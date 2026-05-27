

# Class: KatalogisertRessurs 


_Basisklasse for ressursar som kan katalogiserast._




* __NOTE__: this is an abstract class and should not be instantiated directly


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
        
          
    
        
        
        KatalogisertRessurs --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
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
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Katalogpost](katalogpost.md) | [primaertema](primaertema.md) | range | [KatalogisertRessurs](katalogisertressurs.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Resource |
| native | https://data.norge.no/ap-no/dcat-ap-no/KatalogisertRessurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KatalogisertRessurs
description: Basisklasse for ressursar som kan katalogiserast.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
abstract: true
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
from_schema: https://data.norge.no/ap-no/dcat-ap-no
abstract: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: KatalogisertRessurs
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    range: uriorcurie
    required: true
class_uri: dcat:Resource

```
</details>