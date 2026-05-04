

# Class: GeografiskAdresse 


_Abstrakt basisklasse for norske adressar. Konkrete subklassar er OffisiellAdresse og Postboksadresse._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [locn:Address](http://www.w3.org/ns/locn#Address)





```mermaid
 classDiagram
    class GeografiskAdresse
    click GeografiskAdresse href "../GeografiskAdresse/"
      GeografiskAdresse <|-- OffisiellAdresse
        click OffisiellAdresse href "../OffisiellAdresse/"
      GeografiskAdresse <|-- Postboksadresse
        click Postboksadresse href "../Postboksadresse/"
      
      GeografiskAdresse : id
        
      
```





## Inheritance
* **GeografiskAdresse**
    * [OffisiellAdresse](OffisiellAdresse.md)
    * [Postboksadresse](Postboksadresse.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [locn:Address](http://www.w3.org/ns/locn#Address) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:Address |
| native | https://data.norge.no/linkml/ngr-adresse/GeografiskAdresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeografiskAdresse
description: Abstrakt basisklasse for norske adressar. Konkrete subklassar er OffisiellAdresse
  og Postboksadresse.
from_schema: https://data.norge.no/linkml/ngr-adresse
abstract: true
slots:
- id
class_uri: locn:Address

```
</details>

### Induced

<details>
```yaml
name: GeografiskAdresse
description: Abstrakt basisklasse for norske adressar. Konkrete subklassar er OffisiellAdresse
  og Postboksadresse.
from_schema: https://data.norge.no/linkml/ngr-adresse
abstract: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: GeografiskAdresse
    domain_of:
    - GeografiskAdresse
    - Adressenavn
    - Adresseomrade
    - Adressekode
    - Husnummer
    - Bruksenhetsnummer
    - Representasjonspunkt
    - GeografiskOmrade
    - Postboks
    - Bygning
    - Bruksenhet
    range: uriorcurie
    required: true
class_uri: locn:Address

```
</details>