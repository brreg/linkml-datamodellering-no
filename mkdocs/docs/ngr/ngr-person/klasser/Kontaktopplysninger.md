

# Class: Kontaktopplysninger 


_Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon med det offentlege. Forvaltast av Kontakt- og reservasjonsregisteret (KRR)._





URI: [ngrp:Kontaktopplysninger](https://data.norge.no/vocabulary/ngr-person#Kontaktopplysninger)





```mermaid
 classDiagram
    class Kontaktopplysninger
    click Kontaktopplysninger href "../Kontaktopplysninger/"
      Kontaktopplysninger : epostadresse_verdi
        
      Kontaktopplysninger : id
        
      Kontaktopplysninger : mobiltelefonnummer
        
      Kontaktopplysninger : sist_oppdatert
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrp:Kontaktopplysninger](https://data.norge.no/vocabulary/ngr-person#Kontaktopplysninger) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  
    
  

  
  
    
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [epostadresse_verdi](epostadresse_verdi.md) | 0..1 <br/> [String](string.md) | E-postadresse |
| [mobiltelefonnummer](mobiltelefonnummer.md) | 0..1 <br/> [String](string.md) | Mobiltelefonnummer registrert i KRR |





  
  

  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [sist_oppdatert](sist_oppdatert.md) | 0..1 <br/> [Date](date.md) | Dato kontaktopplysningane sist vart oppdatert |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonContainer](personcontainer.md) | [kontaktopplysningar](kontaktopplysningar.md) | range | [Kontaktopplysninger](kontaktopplysninger.md) |
| [Person](person.md) | [har_kontaktopplysninger](har_kontaktopplysninger.md) | range | [Kontaktopplysninger](kontaktopplysninger.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:Kontaktopplysninger |
| native | https://data.norge.no/linkml/ngr-person/Kontaktopplysninger |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kontaktopplysninger
description: Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon
  med det offentlege. Forvaltast av Kontakt- og reservasjonsregisteret (KRR).
from_schema: https://data.norge.no/linkml/ngr-person
slots:
- id
- epostadresse_verdi
- mobiltelefonnummer
- sist_oppdatert
slot_usage:
  epostadresse_verdi:
    name: epostadresse_verdi
    in_subset:
    - Anbefalt
  mobiltelefonnummer:
    name: mobiltelefonnummer
    in_subset:
    - Anbefalt
  sist_oppdatert:
    name: sist_oppdatert
    in_subset:
    - Valgfri
class_uri: ngrp:Kontaktopplysninger

```
</details>

### Induced

<details>
```yaml
name: Kontaktopplysninger
description: Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon
  med det offentlege. Forvaltast av Kontakt- og reservasjonsregisteret (KRR).
from_schema: https://data.norge.no/linkml/ngr-person
slot_usage:
  epostadresse_verdi:
    name: epostadresse_verdi
    in_subset:
    - Anbefalt
  mobiltelefonnummer:
    name: mobiltelefonnummer
    in_subset:
    - Anbefalt
  sist_oppdatert:
    name: sist_oppdatert
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
    owner: Kontaktopplysninger
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
  epostadresse_verdi:
    name: epostadresse_verdi
    description: E-postadresse.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:epostadresse
    alias: epostadresse_verdi
    owner: Kontaktopplysninger
    domain_of:
    - KontaktinformasjonDoedsbo
    - Kontaktopplysninger
    range: string
  mobiltelefonnummer:
    name: mobiltelefonnummer
    description: Mobiltelefonnummer registrert i KRR.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:mobiltelefonnummer
    alias: mobiltelefonnummer
    owner: Kontaktopplysninger
    domain_of:
    - Kontaktopplysninger
    range: string
  sist_oppdatert:
    name: sist_oppdatert
    description: Dato kontaktopplysningane sist vart oppdatert.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/ngr-person
    rank: 1000
    slot_uri: ngrp:sistOppdatert
    alias: sist_oppdatert
    owner: Kontaktopplysninger
    domain_of:
    - Kontaktopplysninger
    range: date
class_uri: ngrp:Kontaktopplysninger

```
</details>