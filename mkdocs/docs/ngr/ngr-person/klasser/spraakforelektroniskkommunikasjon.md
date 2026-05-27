

# Class: SpraakForElektroniskKommunikasjon 


_Føretrekt språk for elektronisk kommunikasjon med offentlege styresmakter, valt av personen sjølv._





URI: [ngrp:SpraakForElektroniskKommunikasjon](https://data.norge.no/vocabulary/ngr-person#SpraakForElektroniskKommunikasjon)





```mermaid
 classDiagram
    class SpraakForElektroniskKommunikasjon
    click SpraakForElektroniskKommunikasjon href "../SpraakForElektroniskKommunikasjon/"
      SpraakForElektroniskKommunikasjon : id
        
          
    
        
        
        SpraakForElektroniskKommunikasjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      SpraakForElektroniskKommunikasjon : spraakkode
        
          
    
        
        
        SpraakForElektroniskKommunikasjon --> "1" String : spraakkode
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngrp:SpraakForElektroniskKommunikasjon](https://data.norge.no/vocabulary/ngr-person#SpraakForElektroniskKommunikasjon) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [spraakkode](spraakkode.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | BCP 47 språkkode for føretrekt kommunikasjonsspråk (t |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonContainer](personcontainer.md) | [spraak](spraak.md) | range | [SpraakForElektroniskKommunikasjon](spraakforelektroniskkommunikasjon.md) |
| [Person](person.md) | [har_valgt_spraak](har_valgt_spraak.md) | range | [SpraakForElektroniskKommunikasjon](spraakforelektroniskkommunikasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:SpraakForElektroniskKommunikasjon |
| native | https://data.norge.no/ngr/ngr-person/SpraakForElektroniskKommunikasjon |




## Examples
### Example: SpraakForElektroniskKommunikasjon-spraak-1

```yaml
id: ngrp:eksempel/spraak-1
spraakkode: nb

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SpraakForElektroniskKommunikasjon
description: Føretrekt språk for elektronisk kommunikasjon med offentlege styresmakter,
  valt av personen sjølv.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slots:
- id
- spraakkode
slot_usage:
  spraakkode:
    name: spraakkode
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngrp:SpraakForElektroniskKommunikasjon

```
</details>

### Induced

<details>
```yaml
name: SpraakForElektroniskKommunikasjon
description: Føretrekt språk for elektronisk kommunikasjon med offentlege styresmakter,
  valt av personen sjølv.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_usage:
  spraakkode:
    name: spraakkode
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-person
    rank: 1000
    identifier: true
    owner: SpraakForElektroniskKommunikasjon
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
  spraakkode:
    name: spraakkode
    description: BCP 47 språkkode for føretrekt kommunikasjonsspråk (t.d. nb, nn,
      en).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-person
    rank: 1000
    slot_uri: ngrp:spraakkode
    owner: SpraakForElektroniskKommunikasjon
    domain_of:
    - SpraakForElektroniskKommunikasjon
    range: string
    required: true
class_uri: ngrp:SpraakForElektroniskKommunikasjon

```
</details>