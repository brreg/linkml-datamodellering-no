

# Class: Bostedsadresse 


_Adressa personen er registrert busett på i Folkeregisteret._





URI: [ngrp:Bostedsadresse](https://data.norge.no/vocabulary/ngr-person#Bostedsadresse)





```mermaid
 classDiagram
    class Bostedsadresse
    click Bostedsadresse href "../Bostedsadresse/"
      GeografiskAdresse <|-- Bostedsadresse
        click GeografiskAdresse href "../GeografiskAdresse/"
      
      Bostedsadresse : gyldig_fra_og_med
        
      Bostedsadresse : gyldig_til_og_med
        
      Bostedsadresse : id
        
      
```





## Inheritance
* [GeografiskAdresse](GeografiskAdresse.md)
    * **Bostedsadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrp:Bostedsadresse](https://data.norge.no/vocabulary/ngr-person#Bostedsadresse) |


## Eigenskapar







  
  

  
  





  
  
    
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gyldig_fra_og_med](gyldig_fra_og_med.md) | 0..1 <br/> [Date](Date.md) | Dato opplysinga er gyldig frå og med |





  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gyldig_til_og_med](gyldig_til_og_med.md) | 0..1 <br/> [Date](Date.md) | Dato opplysinga er gyldig til og med |






  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [GeografiskAdresse](GeografiskAdresse.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonContainer](PersonContainer.md) | [bostedsadresser](bostedsadresser.md) | range | [Bostedsadresse](Bostedsadresse.md) |
| [Person](Person.md) | [har_bosted_paa](har_bosted_paa.md) | range | [Bostedsadresse](Bostedsadresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:Bostedsadresse |
| native | https://data.norge.no/linkml/ngr-person/Bostedsadresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bostedsadresse
description: Adressa personen er registrert busett på i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
is_a: GeografiskAdresse
slots:
- gyldig_fra_og_med
- gyldig_til_og_med
slot_usage:
  gyldig_fra_og_med:
    name: gyldig_fra_og_med
    in_subset:
    - Anbefalt
  gyldig_til_og_med:
    name: gyldig_til_og_med
    in_subset:
    - Valgfri
class_uri: ngrp:Bostedsadresse

```
</details>

### Induced

<details>
```yaml
name: Bostedsadresse
description: Adressa personen er registrert busett på i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
is_a: GeografiskAdresse
slot_usage:
  gyldig_fra_og_med:
    name: gyldig_fra_og_med
    in_subset:
    - Anbefalt
  gyldig_til_og_med:
    name: gyldig_til_og_med
    in_subset:
    - Valgfri
attributes:
  gyldig_fra_og_med:
    name: gyldig_fra_og_med
    description: Dato opplysinga er gyldig frå og med.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:gyldigFraOgMed
    alias: gyldig_fra_og_med
    owner: Bostedsadresse
    domain_of:
    - Kjoenn
    - Sivilstand
    - Personstatus
    - Statsborgerskap
    - Opphold
    - Bostedsadresse
    - Postadresse
    - Oppholdsadresse
    - ReservasjonMotKommunikasjonPaaNett
    range: date
  gyldig_til_og_med:
    name: gyldig_til_og_med
    description: Dato opplysinga er gyldig til og med.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:gyldigTilOgMed
    alias: gyldig_til_og_med
    owner: Bostedsadresse
    domain_of:
    - Statsborgerskap
    - Opphold
    - Bostedsadresse
    - Postadresse
    - Oppholdsadresse
    range: date
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    identifier: true
    alias: id
    owner: Bostedsadresse
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
class_uri: ngrp:Bostedsadresse

```
</details>