

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
        
      Utdanningsforhold : id
        
      
```





## Inheritance
* **Utdanningsforhold**
    * [Undervisningsforhold](Undervisningsforhold.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Utdanningsforhold](https://schema.fintlabs.no/utdanning/Utdanningsforhold) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [String](String.md) | Skildring av utdanningsforholdet |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




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
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
slots:
- id
attributes:
  beskrivelse:
    name: beskrivelse
    description: Skildring av utdanningsforholdet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
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
class_uri: utd:Utdanningsforhold

```
</details>

### Induced

<details>
```yaml
name: Utdanningsforhold
description: Abstrakt basisklasse for undervisningsforhold i utdanning.
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
attributes:
  beskrivelse:
    name: beskrivelse
    description: Skildring av utdanningsforholdet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:beskrivelse
    alias: beskrivelse
    owner: Utdanningsforhold
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
    owner: Utdanningsforhold
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
class_uri: utd:Utdanningsforhold

```
</details>