

# Class: InnflyttingTilNorge 


_Registrering av innflytting til Noreg i Folkeregisteret._





URI: [ngrp:InnflyttingTilNorge](https://data.norge.no/vocabulary/ngr-person#InnflyttingTilNorge)





```mermaid
 classDiagram
    class InnflyttingTilNorge
    click InnflyttingTilNorge href "../InnflyttingTilNorge/"
      InnflyttingTilNorge : fraflyttingsland
        
          
    
        
        
        InnflyttingTilNorge --> "0..1" String : fraflyttingsland
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      InnflyttingTilNorge : fraflyttingssted_i_utlandet
        
          
    
        
        
        InnflyttingTilNorge --> "0..1" String : fraflyttingssted_i_utlandet
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      InnflyttingTilNorge : id
        
          
    
        
        
        InnflyttingTilNorge --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      InnflyttingTilNorge : innflyttingsdato
        
          
    
        
        
        InnflyttingTilNorge --> "1" Date : innflyttingsdato
        click Date href "../http://www.w3.org/2001/XMLSchema#date/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrp:InnflyttingTilNorge](https://data.norge.no/vocabulary/ngr-person#InnflyttingTilNorge) |


## Eigenskapar







  
  

  
  

  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [innflyttingsdato](innflyttingsdato.md) | 1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato personen vart registrert innflytta til Noreg |





  
  

  
  
    
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [fraflyttingsland](fraflyttingsland.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | ISO 3166-1 landkode for landet personen flytta frå |





  
  

  
  

  
  
    
  

  
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [fraflyttingssted_i_utlandet](fraflyttingssted_i_utlandet.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Stad i utlandet personen flytta frå |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonContainer](personcontainer.md) | [innflytting](innflytting.md) | range | [InnflyttingTilNorge](innflyttingtilnorge.md) |
| [Person](person.md) | [har_innflytting_til_norge](har_innflytting_til_norge.md) | range | [InnflyttingTilNorge](innflyttingtilnorge.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:InnflyttingTilNorge |
| native | https://data.norge.no/linkml/ngr-person/InnflyttingTilNorge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InnflyttingTilNorge
description: Registrering av innflytting til Noreg i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slots:
- id
- fraflyttingsland
- fraflyttingssted_i_utlandet
- innflyttingsdato
slot_usage:
  innflyttingsdato:
    name: innflyttingsdato
    in_subset:
    - Obligatorisk
    required: true
  fraflyttingsland:
    name: fraflyttingsland
    in_subset:
    - Anbefalt
  fraflyttingssted_i_utlandet:
    name: fraflyttingssted_i_utlandet
    in_subset:
    - Valgfri
class_uri: ngrp:InnflyttingTilNorge

```
</details>

### Induced

<details>
```yaml
name: InnflyttingTilNorge
description: Registrering av innflytting til Noreg i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_usage:
  innflyttingsdato:
    name: innflyttingsdato
    in_subset:
    - Obligatorisk
    required: true
  fraflyttingsland:
    name: fraflyttingsland
    in_subset:
    - Anbefalt
  fraflyttingssted_i_utlandet:
    name: fraflyttingssted_i_utlandet
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
    owner: InnflyttingTilNorge
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
  fraflyttingsland:
    name: fraflyttingsland
    description: ISO 3166-1 landkode for landet personen flytta frå.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:fraflyttingsland
    alias: fraflyttingsland
    owner: InnflyttingTilNorge
    domain_of:
    - InnflyttingTilNorge
    range: string
  fraflyttingssted_i_utlandet:
    name: fraflyttingssted_i_utlandet
    description: Stad i utlandet personen flytta frå.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:fraflyttingsstedIUtlandet
    alias: fraflyttingssted_i_utlandet
    owner: InnflyttingTilNorge
    domain_of:
    - InnflyttingTilNorge
    range: string
  innflyttingsdato:
    name: innflyttingsdato
    description: Dato personen vart registrert innflytta til Noreg.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:innflyttingsdato
    alias: innflyttingsdato
    owner: InnflyttingTilNorge
    domain_of:
    - InnflyttingTilNorge
    range: date
    required: true
class_uri: ngrp:InnflyttingTilNorge

```
</details>