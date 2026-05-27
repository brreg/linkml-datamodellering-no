

# Class: GeografiskAdresse 


_Abstrakt klasse for geografiske adresser. Tilhøyrer Domene adresse og forvaltast av Matrikkelen. Konkrete typar er Bostedsadresse, Postadresse og Oppholdsadresse._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [ngrp:GeografiskAdresse](https://data.norge.no/vocabulary/ngr-person#GeografiskAdresse)





```mermaid
 classDiagram
    class GeografiskAdresse
    click GeografiskAdresse href "../GeografiskAdresse/"
      GeografiskAdresse <|-- Bostedsadresse
        click Bostedsadresse href "../Bostedsadresse/"
      GeografiskAdresse <|-- Postadresse
        click Postadresse href "../Postadresse/"
      GeografiskAdresse <|-- Oppholdsadresse
        click Oppholdsadresse href "../Oppholdsadresse/"
      
      GeografiskAdresse : id
        
          
    
        
        
        GeografiskAdresse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* **GeografiskAdresse**
    * [Bostedsadresse](bostedsadresse.md)
    * [Postadresse](postadresse.md)
    * [Oppholdsadresse](oppholdsadresse.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrp:GeografiskAdresse](https://data.norge.no/vocabulary/ngr-person#GeografiskAdresse) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:GeografiskAdresse |
| native | https://data.norge.no/ngr/ngr-person/GeografiskAdresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeografiskAdresse
description: Abstrakt klasse for geografiske adresser. Tilhøyrer Domene adresse og
  forvaltast av Matrikkelen. Konkrete typar er Bostedsadresse, Postadresse og Oppholdsadresse.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
abstract: true
slots:
- id
class_uri: ngrp:GeografiskAdresse

```
</details>

### Induced

<details>
```yaml
name: GeografiskAdresse
description: Abstrakt klasse for geografiske adresser. Tilhøyrer Domene adresse og
  forvaltast av Matrikkelen. Konkrete typar er Bostedsadresse, Postadresse og Oppholdsadresse.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
abstract: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-person
    rank: 1000
    identifier: true
    owner: GeografiskAdresse
    domain_of:
    - Person
    - Personnavn
    - Folkeregisteridentifikator
    - Personidentifikasjon
    - FalskIdentitet
    - Identifikasjonsdokument
    - Identitetsgrunnlag
    - Kjoenn
    - Sivilstand
    - Personstatus
    - Statsborgerskap
    - Opphold
    - Foedsel
    - Dodsfall
    - KontaktinformasjonDoedsbo
    - ForeldreansvarForelder
    - ForeldreansvarBarn
    - FamilierelasjonForelder
    - FamilierelasjonBarn
    - FamilierelasjonEktefelle
    - InnflyttingTilNorge
    - UtflyttingFraNorge
    - GeografiskAdresse
    - Adressebeskyttelse
    - Verge
    - RettsligHandleevne
    - ReservasjonMotKommunikasjonPaaNett
    - Kontaktopplysninger
    - SpraakForElektroniskKommunikasjon
    range: uriorcurie
    required: true
class_uri: ngrp:GeografiskAdresse

```
</details>