

# Class: OrdensvurderingAbstrakt 


_Abstrakt basisklasse for ordensvurderingar._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [utd:OrdensvurderingAbstrakt](https://schema.fintlabs.no/utdanning/OrdensvurderingAbstrakt)





```mermaid
 classDiagram
    class OrdensvurderingAbstrakt
    click OrdensvurderingAbstrakt href "../OrdensvurderingAbstrakt/"
      OrdensvurderingAbstrakt <|-- Halvaarsordensvurdering
        click Halvaarsordensvurdering href "../Halvaarsordensvurdering/"
      OrdensvurderingAbstrakt <|-- Sluttordensvurdering
        click Sluttordensvurdering href "../Sluttordensvurdering/"
      OrdensvurderingAbstrakt <|-- Underveisordensvurdering
        click Underveisordensvurdering href "../Underveisordensvurdering/"
      
      OrdensvurderingAbstrakt : atferd
        
          
    
        
        
        OrdensvurderingAbstrakt --> "0..1" Karakterverdi : atferd
        click Karakterverdi href "../Karakterverdi/"
    

        
      OrdensvurderingAbstrakt : id
        
      OrdensvurderingAbstrakt : kommentar
        
      OrdensvurderingAbstrakt : orden
        
          
    
        
        
        OrdensvurderingAbstrakt --> "0..1" Karakterverdi : orden
        click Karakterverdi href "../Karakterverdi/"
    

        
      OrdensvurderingAbstrakt : skoleaar
        
          
    
        
        
        OrdensvurderingAbstrakt --> "0..1" Skoleaar : skoleaar
        click Skoleaar href "../Skoleaar/"
    

        
      OrdensvurderingAbstrakt : vurderingsdato
        
      
```





## Inheritance
* **OrdensvurderingAbstrakt**
    * [Halvaarsordensvurdering](halvaarsordensvurdering.md)
    * [Sluttordensvurdering](sluttordensvurdering.md)
    * [Underveisordensvurdering](underveisordensvurdering.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:OrdensvurderingAbstrakt](https://schema.fintlabs.no/utdanning/OrdensvurderingAbstrakt) |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |
| [kommentar](kommentar.md) | 1 <br/> [String](string.md) | Kommentar til vurderinga |
| [vurderingsdato](vurderingsdato.md) | 1 <br/> [Datetime](datetime.md) | Dato og tidspunkt for vurderinga |
| [atferd](atferd.md) | 0..1 <br/> [Karakterverdi](karakterverdi.md) | Karakterverdi for åtferd |
| [orden](orden.md) | 0..1 <br/> [Karakterverdi](karakterverdi.md) | Karakterverdi for orden |
| [skoleaar](skoleaar.md) | 0..1 <br/> [Skoleaar](skoleaar.md) | Skoleåret vurderinga tilhøyrer |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:OrdensvurderingAbstrakt |
| native | https://schema.fintlabs.no/utdanning/:OrdensvurderingAbstrakt |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrdensvurderingAbstrakt
description: Abstrakt basisklasse for ordensvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
slots:
- id
attributes:
  kommentar:
    name: kommentar
    description: Kommentar til vurderinga.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:kommentar
    domain_of:
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    - Fraversregistrering
    range: string
    required: true
  vurderingsdato:
    name: vurderingsdato
    description: Dato og tidspunkt for vurderinga.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:vurderingsdato
    domain_of:
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    range: datetime
    required: true
  atferd:
    name: atferd
    description: Karakterverdi for åtferd.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:atferd
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: Karakterverdi
  orden:
    name: orden
    description: Karakterverdi for orden.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:orden
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: Karakterverdi
  skoleaar:
    name: skoleaar
    description: Skoleåret vurderinga tilhøyrer.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:skoleaar
    domain_of:
    - UtdanningContainer
    - Elevforhold
    - Klasse
    - Kontaktlaerergruppe
    - Persongruppe
    - Faggruppe
    - Undervisningsgruppe
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    - Anmerkninger
    - Eksamensgruppe
    range: Skoleaar
class_uri: utd:OrdensvurderingAbstrakt

```
</details>

### Induced

<details>
```yaml
name: OrdensvurderingAbstrakt
description: Abstrakt basisklasse for ordensvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
attributes:
  kommentar:
    name: kommentar
    description: Kommentar til vurderinga.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:kommentar
    alias: kommentar
    owner: OrdensvurderingAbstrakt
    domain_of:
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    - Fraversregistrering
    range: string
    required: true
  vurderingsdato:
    name: vurderingsdato
    description: Dato og tidspunkt for vurderinga.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:vurderingsdato
    alias: vurderingsdato
    owner: OrdensvurderingAbstrakt
    domain_of:
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    range: datetime
    required: true
  atferd:
    name: atferd
    description: Karakterverdi for åtferd.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:atferd
    alias: atferd
    owner: OrdensvurderingAbstrakt
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: Karakterverdi
  orden:
    name: orden
    description: Karakterverdi for orden.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: utd:orden
    alias: orden
    owner: OrdensvurderingAbstrakt
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: Karakterverdi
  skoleaar:
    name: skoleaar
    description: Skoleåret vurderinga tilhøyrer.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:skoleaar
    alias: skoleaar
    owner: OrdensvurderingAbstrakt
    domain_of:
    - UtdanningContainer
    - Elevforhold
    - Klasse
    - Kontaktlaerergruppe
    - Persongruppe
    - Faggruppe
    - Undervisningsgruppe
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    - Anmerkninger
    - Eksamensgruppe
    range: Skoleaar
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    identifier: true
    alias: id
    owner: OrdensvurderingAbstrakt
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
class_uri: utd:OrdensvurderingAbstrakt

```
</details>