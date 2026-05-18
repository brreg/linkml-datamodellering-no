

# Class: Anmerkninger 


_Åtferds- og ordensanmerkningar for ein elev i eit skoleår._





URI: [utd:Anmerkninger](https://schema.fintlabs.no/utdanning/Anmerkninger)





```mermaid
 classDiagram
    class Anmerkninger
    click Anmerkninger href "../Anmerkninger/"
      Anmerkninger : atferd
        
          
    
        
        
        Anmerkninger --> "1" Integer : atferd
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
      Anmerkninger : id
        
          
    
        
        
        Anmerkninger --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Anmerkninger : orden
        
          
    
        
        
        Anmerkninger --> "1" Integer : orden
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
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







  
  

  
  
    
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [atferd](atferd.md) | 1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | Åtferdskarakter |
| [orden](orden.md) | 1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | Ordenskarakter |





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [skoleaar](skoleaar.md) | 0..1 <br/> [Skoleaar](skoleaar.md) | Skoleåret |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








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
rank: 1000
slots:
- id
- atferd
- orden
- skoleaar
slot_usage:
  atferd:
    name: atferd
    in_subset:
    - Obligatorisk
    range: integer
    required: true
  orden:
    name: orden
    in_subset:
    - Obligatorisk
    range: integer
    required: true
  skoleaar:
    name: skoleaar
    in_subset:
    - Valgfri
class_uri: utd:Anmerkninger

```
</details>

### Induced

<details>
```yaml
name: Anmerkninger
description: Åtferds- og ordensanmerkningar for ein elev i eit skoleår.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_usage:
  atferd:
    name: atferd
    in_subset:
    - Obligatorisk
    range: integer
    required: true
  orden:
    name: orden
    in_subset:
    - Obligatorisk
    range: integer
    required: true
  skoleaar:
    name: skoleaar
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-common
    identifier: true
    alias: id
    owner: Anmerkninger
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
  atferd:
    name: atferd
    description: Åtferdskarakter.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
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
    description: Ordenskarakter.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
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
    description: Skoleåret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
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
class_uri: utd:Anmerkninger

```
</details>