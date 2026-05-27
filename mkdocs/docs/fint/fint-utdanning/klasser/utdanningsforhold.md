

# Class: Utdanningsforhold 


_Abstrakt basisklasse for undervisningsforhold i utdanning._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [utd:Utdanningsforhold](https://schema.fintlabs.no/utdanning/Utdanningsforhold)





```mermaid
 classDiagram
    class Utdanningsforhold
    click Utdanningsforhold href "../Utdanningsforhold/"
      Utdanningsforhold <|-- Undervisningsforhold
        click Undervisningsforhold href "../Undervisningsforhold/"
      
      Utdanningsforhold : beskrivelse
        
          
    
        
        
        Utdanningsforhold --> "0..1" String : beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Utdanningsforhold : id
        
          
    
        
        
        Utdanningsforhold --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* **Utdanningsforhold**
    * [Undervisningsforhold](undervisningsforhold.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Utdanningsforhold](https://schema.fintlabs.no/utdanning/Utdanningsforhold) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Beskriven namn eller omtale |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:Utdanningsforhold |
| native | https://schema.fintlabs.no/utdanning/:Utdanningsforhold |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Utdanningsforhold
description: Abstrakt basisklasse for undervisningsforhold i utdanning.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
abstract: true
slots:
- id
- beskrivelse
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
class_uri: utd:Utdanningsforhold

```
</details>

### Induced

<details>
```yaml
name: Utdanningsforhold
description: Abstrakt basisklasse for undervisningsforhold i utdanning.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
abstract: true
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: Utdanningsforhold
    domain_of:
    - Begrep
    - Elev
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    - Gruppe
    - Gruppemedlemskap
    - Utdanningsforhold
    - Elevforhold
    - Elevtilrettelegging
    - Skole
    - Skoleressurs
    - Varsel
    - Eksamen
    - Rom
    - Time
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    - Anmerkninger
    - Elevfravar
    - Elevvurdering
    - Fravarsoversikt
    - Fraversregistrering
    - Karakterhistorie
    - Sensor
    - AvlagtProve
    - Laerling
    - OtUngdom
    - Avbruddsaarsak
    - Betalingsstatus
    - Bevistype
    - Brevtype
    - Eksamensform
    - Elevkategori
    - Fagmerknad
    - Fagstatus
    - Fravartype
    - Fullfortkode
    - Karakterskala
    - Karakterstatus
    - Karakterverdi
    - OtEnhet
    - OtStatus
    - Provestatus
    - Skoleaar
    - Skoleeiertype
    - Termin
    - Tilrettelegging
    - Varseltype
    - Vitnemalsmerknad
    range: uriorcurie
    required: true
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn eller omtale.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:beskrivelse
    owner: Utdanningsforhold
    domain_of:
    - Periode
    - Gruppe
    - Utdanningsforhold
    - Elevforhold
    - Eksamen
    - Time
    - OtStatus
    range: string
class_uri: utd:Utdanningsforhold

```
</details>