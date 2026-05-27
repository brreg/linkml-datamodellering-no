

# Class: Valuta 


_Valutakodar for offisielle valutaer._





URI: [fint:Valuta](https://schema.fintlabs.no/Valuta)





```mermaid
 classDiagram
    class Valuta
    click Valuta href "../Valuta/"
      Valuta : bokstavkode
        
          
    
        
        
        Valuta --> "1" Identifikator : bokstavkode
        click Identifikator href "../Identifikator/"
    

        
      Valuta : id
        
          
    
        
        
        Valuta --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Valuta : nummerkode
        
          
    
        
        
        Valuta --> "1" Identifikator : nummerkode
        click Identifikator href "../Identifikator/"
    

        
      Valuta : valuta_navn
        
          
    
        
        
        Valuta --> "1" String : valuta_navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Valuta](https://schema.fintlabs.no/Valuta) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [bokstavkode](bokstavkode.md) | 1 <br/> [Identifikator](identifikator.md) | Bokstavkode for aktuell valuta |
| [valuta_navn](valuta_navn.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på valuta |
| [nummerkode](nummerkode.md) | 1 <br/> [Identifikator](identifikator.md) | Nummerkode for aktuell valuta |





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Valuta |
| native | https://schema.fintlabs.no/:Valuta |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Valuta
description: Valutakodar for offisielle valutaer.
from_schema: https://data.norge.no/fint/fint-common
slots:
- id
- bokstavkode
- valuta_navn
- nummerkode
slot_usage:
  bokstavkode:
    name: bokstavkode
    in_subset:
    - Obligatorisk
    required: true
  valuta_navn:
    name: valuta_navn
    in_subset:
    - Obligatorisk
    required: true
  nummerkode:
    name: nummerkode
    in_subset:
    - Obligatorisk
    required: true
class_uri: fint:Valuta

```
</details>

### Induced

<details>
```yaml
name: Valuta
description: Valutakodar for offisielle valutaer.
from_schema: https://data.norge.no/fint/fint-common
slot_usage:
  bokstavkode:
    name: bokstavkode
    in_subset:
    - Obligatorisk
    required: true
  valuta_navn:
    name: valuta_navn
    in_subset:
    - Obligatorisk
    required: true
  nummerkode:
    name: nummerkode
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: Valuta
    domain_of:
    - Begrep
    - Elev
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    - Applikasjon
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    - DigitalEnhet
    - Enhetsgruppe
    - Enhetsgruppemedlemskap
    - Identitet
    - Rettighet
    - Applikasjonskategori
    - Brukertype
    - Enhetstype
    - Handhevingstype
    - Lisensmodell
    - Plattform
    - Produsent
    - Status
    range: uriorcurie
    required: true
  bokstavkode:
    name: bokstavkode
    description: Bokstavkode for aktuell valuta.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:bokstavkode
    owner: Valuta
    domain_of:
    - Valuta
    range: Identifikator
    required: true
    inlined: true
  valuta_navn:
    name: valuta_navn
    description: Namn på valuta.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:valutaNavn
    owner: Valuta
    domain_of:
    - Valuta
    range: string
    required: true
  nummerkode:
    name: nummerkode
    description: Nummerkode for aktuell valuta.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:nummerkode
    owner: Valuta
    domain_of:
    - Valuta
    range: Identifikator
    required: true
    inlined: true
class_uri: fint:Valuta

```
</details>