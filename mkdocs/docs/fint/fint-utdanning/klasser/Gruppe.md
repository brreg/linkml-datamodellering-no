

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
        
      Gruppe : id
        
      Gruppe : navn
        
      
```





## Inheritance
* **Gruppe**
    * [Klasse](Klasse.md)
    * [Kontaktlaerergruppe](Kontaktlaerergruppe.md)
    * [Persongruppe](Persongruppe.md)
    * [Arstrinn](Arstrinn.md)
    * [Programomrade](Programomrade.md)
    * [Utdanningsprogram](Utdanningsprogram.md)
    * [Fag](Fag.md)
    * [Faggruppe](Faggruppe.md)
    * [Undervisningsgruppe](Undervisningsgruppe.md)
    * [Eksamensgruppe](Eksamensgruppe.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Gruppe](https://schema.fintlabs.no/utdanning/Gruppe) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |
| [navn](navn.md) | 1 <br/> [String](String.md) | Namn på gruppa |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [String](String.md) | Skildring av gruppa |


















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
abstract: true
slots:
- id
attributes:
  navn:
    name: navn
    description: Namn på gruppa.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:navn
    domain_of:
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
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    range: string
    required: true
  beskrivelse:
    name: beskrivelse
    description: Skildring av gruppa.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:beskrivelse
    domain_of:
    - Gruppe
    - Utdanningsforhold
    - Elevforhold
    - Eksamen
    - Time
    - OtStatus
    - Periode
    range: string
class_uri: utd:Gruppe

```
</details>

### Induced

<details>
```yaml
name: Gruppe
description: Abstrakt basisklasse for alle gruppetypar i utdanning.
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
attributes:
  navn:
    name: navn
    description: Namn på gruppa.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:navn
    alias: navn
    owner: Gruppe
    domain_of:
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
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    range: string
    required: true
  beskrivelse:
    name: beskrivelse
    description: Skildring av gruppa.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:beskrivelse
    alias: beskrivelse
    owner: Gruppe
    domain_of:
    - Gruppe
    - Utdanningsforhold
    - Elevforhold
    - Eksamen
    - Time
    - OtStatus
    - Periode
    range: string
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    identifier: true
    alias: id
    owner: Gruppe
    domain_of:
    - Gruppe
    - Gruppemedlemskap
    - Utdanningsforhold
    - Elev
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
    - Begrep
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    range: uriorcurie
    required: true
class_uri: utd:Gruppe

```
</details>