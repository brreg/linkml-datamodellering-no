

# Class: Gruppe 


_Abstrakt basisklasse for alle gruppetypar i utdanning._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [utd:Gruppe](https://schema.fintlabs.no/utdanning/Gruppe)





```mermaid
 classDiagram
    class Gruppe
    click Gruppe href "../Gruppe/"
      Gruppe <|-- Klasse
        click Klasse href "../Klasse/"
      Gruppe <|-- Kontaktlaerergruppe
        click Kontaktlaerergruppe href "../Kontaktlaerergruppe/"
      Gruppe <|-- Persongruppe
        click Persongruppe href "../Persongruppe/"
      Gruppe <|-- Arstrinn
        click Arstrinn href "../Arstrinn/"
      Gruppe <|-- Programomrade
        click Programomrade href "../Programomrade/"
      Gruppe <|-- Utdanningsprogram
        click Utdanningsprogram href "../Utdanningsprogram/"
      Gruppe <|-- Fag
        click Fag href "../Fag/"
      Gruppe <|-- Faggruppe
        click Faggruppe href "../Faggruppe/"
      Gruppe <|-- Undervisningsgruppe
        click Undervisningsgruppe href "../Undervisningsgruppe/"
      Gruppe <|-- Eksamensgruppe
        click Eksamensgruppe href "../Eksamensgruppe/"
      
      Gruppe : beskrivelse
        
          
    
        
        
        Gruppe --> "0..1" String : beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Gruppe : id
        
          
    
        
        
        Gruppe --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Gruppe : navn
        
          
    
        
        
        Gruppe --> "1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* **Gruppe**
    * [Klasse](klasse.md)
    * [Kontaktlaerergruppe](kontaktlaerergruppe.md)
    * [Persongruppe](persongruppe.md)
    * [Arstrinn](arstrinn.md)
    * [Programomrade](programomrade.md)
    * [Utdanningsprogram](utdanningsprogram.md)
    * [Fag](fag.md)
    * [Faggruppe](faggruppe.md)
    * [Undervisningsgruppe](undervisningsgruppe.md)
    * [Eksamensgruppe](eksamensgruppe.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Gruppe](https://schema.fintlabs.no/utdanning/Gruppe) |


## Eigenskapar







  
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [navn](navn.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Hovudnamn for ressursen |





  
  

  
  

  
  





  
  

  
  

  
  
    
  


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


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:Gruppe |
| native | https://schema.fintlabs.no/utdanning/:Gruppe |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gruppe
description: Abstrakt basisklasse for alle gruppetypar i utdanning.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
abstract: true
slots:
- id
- navn
- beskrivelse
slot_usage:
  navn:
    name: navn
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
class_uri: utd:Gruppe

```
</details>

### Induced

<details>
```yaml
name: Gruppe
description: Abstrakt basisklasse for alle gruppetypar i utdanning.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
abstract: true
slot_usage:
  navn:
    name: navn
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-common
    identifier: true
    alias: id
    owner: Gruppe
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
  navn:
    name: navn
    description: Hovudnamn for ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:navn
    alias: navn
    owner: Gruppe
    domain_of:
    - Begrep
    - Gruppe
    - Skole
    - Eksamen
    - Rom
    - Time
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
    range: string
    required: true
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn eller omtale.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:beskrivelse
    alias: beskrivelse
    owner: Gruppe
    domain_of:
    - Periode
    - Gruppe
    - Utdanningsforhold
    - Elevforhold
    - Eksamen
    - Time
    - OtStatus
    range: string
class_uri: utd:Gruppe

```
</details>