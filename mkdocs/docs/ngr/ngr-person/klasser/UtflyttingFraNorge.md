

# Class: UtflyttingFraNorge 


_Registrering av utflytting frå Noreg i Folkeregisteret._





URI: [ngrp:UtflyttingFraNorge](https://data.norge.no/vocabulary/ngr-person#UtflyttingFraNorge)





```mermaid
 classDiagram
    class UtflyttingFraNorge
    click UtflyttingFraNorge href "../UtflyttingFraNorge/"
      UtflyttingFraNorge : id
        
          
    
        
        
        UtflyttingFraNorge --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      UtflyttingFraNorge : tilflyttingsland
        
          
    
        
        
        UtflyttingFraNorge --> "0..1" String : tilflyttingsland
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      UtflyttingFraNorge : tilflyttingssted_i_utlandet
        
          
    
        
        
        UtflyttingFraNorge --> "0..1" String : tilflyttingssted_i_utlandet
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      UtflyttingFraNorge : utflyttingsdato
        
          
    
        
        
        UtflyttingFraNorge --> "1" Date : utflyttingsdato
        click Date href "../http://www.w3.org/2001/XMLSchema#date/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrp:UtflyttingFraNorge](https://data.norge.no/vocabulary/ngr-person#UtflyttingFraNorge) |


## Eigenskapar







  
  

  
  

  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [utflyttingsdato](utflyttingsdato.md) | 1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato personen vart registrert utflytta frå Noreg |





  
  

  
  
    
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tilflyttingsland](tilflyttingsland.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | ISO 3166-1 landkode for landet personen flytta til |





  
  

  
  

  
  
    
  

  
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tilflyttingssted_i_utlandet](tilflyttingssted_i_utlandet.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Stad i utlandet personen flytta til |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonContainer](personcontainer.md) | [utflytting](utflytting.md) | range | [UtflyttingFraNorge](utflyttingfranorge.md) |
| [Person](person.md) | [har_utflytting_fra_norge](har_utflytting_fra_norge.md) | range | [UtflyttingFraNorge](utflyttingfranorge.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:UtflyttingFraNorge |
| native | https://data.norge.no/linkml/ngr-person/UtflyttingFraNorge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UtflyttingFraNorge
description: Registrering av utflytting frå Noreg i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slots:
- id
- tilflyttingsland
- tilflyttingssted_i_utlandet
- utflyttingsdato
slot_usage:
  utflyttingsdato:
    name: utflyttingsdato
    in_subset:
    - Obligatorisk
    required: true
  tilflyttingsland:
    name: tilflyttingsland
    in_subset:
    - Anbefalt
  tilflyttingssted_i_utlandet:
    name: tilflyttingssted_i_utlandet
    in_subset:
    - Valgfri
class_uri: ngrp:UtflyttingFraNorge

```
</details>

### Induced

<details>
```yaml
name: UtflyttingFraNorge
description: Registrering av utflytting frå Noreg i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_usage:
  utflyttingsdato:
    name: utflyttingsdato
    in_subset:
    - Obligatorisk
    required: true
  tilflyttingsland:
    name: tilflyttingsland
    in_subset:
    - Anbefalt
  tilflyttingssted_i_utlandet:
    name: tilflyttingssted_i_utlandet
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    identifier: true
    alias: id
    owner: UtflyttingFraNorge
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
  tilflyttingsland:
    name: tilflyttingsland
    description: ISO 3166-1 landkode for landet personen flytta til.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:tilflyttingsland
    alias: tilflyttingsland
    owner: UtflyttingFraNorge
    domain_of:
    - UtflyttingFraNorge
    range: string
  tilflyttingssted_i_utlandet:
    name: tilflyttingssted_i_utlandet
    description: Stad i utlandet personen flytta til.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:tilflyttingsstedIUtlandet
    alias: tilflyttingssted_i_utlandet
    owner: UtflyttingFraNorge
    domain_of:
    - UtflyttingFraNorge
    range: string
  utflyttingsdato:
    name: utflyttingsdato
    description: Dato personen vart registrert utflytta frå Noreg.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:utflyttingsdato
    alias: utflyttingsdato
    owner: UtflyttingFraNorge
    domain_of:
    - UtflyttingFraNorge
    range: date
    required: true
class_uri: ngrp:UtflyttingFraNorge

```
</details>