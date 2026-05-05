

# Class: Anmerkninger 


_Åtferds- og ordensanmerkningar for ein elev i eit skoleår._





URI: [utd:Anmerkninger](https://schema.fintlabs.no/utdanning/Anmerkninger)





```mermaid
 classDiagram
    class Anmerkninger
    click Anmerkninger href "../Anmerkninger/"
      Anmerkninger : atferd
        
      Anmerkninger : id
        
      Anmerkninger : orden
        
      Anmerkninger : skoleaar
        
          
    
        
        
        Anmerkninger --> "0..1" Skoleaar : skoleaar
        click Skoleaar href "../Skoleaar/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Anmerkninger](https://schema.fintlabs.no/utdanning/Anmerkninger) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |
| [atferd](atferd.md) | 1 <br/> [Integer](integer.md) | Antal åtferdsanmerkningar |
| [orden](orden.md) | 1 <br/> [Integer](integer.md) | Antal ordensanmerkningar |
| [skoleaar](skoleaar.md) | 0..1 <br/> [Skoleaar](skoleaar.md) | Skoleåret anmerkningane gjeld |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | [anmerkningar](anmerkningar.md) | range | [Anmerkninger](anmerkninger.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:Anmerkninger |
| native | https://schema.fintlabs.no/utdanning/:Anmerkninger |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Anmerkninger
description: Åtferds- og ordensanmerkningar for ein elev i eit skoleår.
from_schema: https://data.norge.no/linkml/fint-utdanning
slots:
- id
attributes:
  atferd:
    name: atferd
    description: Antal åtferdsanmerkningar.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:atferd
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: integer
    required: true
  orden:
    name: orden
    description: Antal ordensanmerkningar.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:orden
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: integer
    required: true
  skoleaar:
    name: skoleaar
    description: Skoleåret anmerkningane gjeld.
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
class_uri: utd:Anmerkninger

```
</details>

### Induced

<details>
```yaml
name: Anmerkninger
description: Åtferds- og ordensanmerkningar for ein elev i eit skoleår.
from_schema: https://data.norge.no/linkml/fint-utdanning
attributes:
  atferd:
    name: atferd
    description: Antal åtferdsanmerkningar.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:atferd
    alias: atferd
    owner: Anmerkninger
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: integer
    required: true
  orden:
    name: orden
    description: Antal ordensanmerkningar.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:orden
    alias: orden
    owner: Anmerkninger
    domain_of:
    - OrdensvurderingAbstrakt
    - Anmerkninger
    range: integer
    required: true
  skoleaar:
    name: skoleaar
    description: Skoleåret anmerkningane gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    slot_uri: utd:skoleaar
    alias: skoleaar
    owner: Anmerkninger
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
    owner: Anmerkninger
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
class_uri: utd:Anmerkninger

```
</details>