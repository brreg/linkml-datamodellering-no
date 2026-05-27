

# Class: Applikasjonsressurstilgjengelighet 


_Kva organisasjonselements brukarar som har tilgang til ein ressurs._





URI: [res:Applikasjonsressurstilgjengelighet](https://schema.fintlabs.no/ressurs/Applikasjonsressurstilgjengelighet)





```mermaid
 classDiagram
    class Applikasjonsressurstilgjengelighet
    click Applikasjonsressurstilgjengelighet href "../Applikasjonsressurstilgjengelighet/"
      Applikasjonsressurstilgjengelighet : gyldighetsperiode
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "1" Periode : gyldighetsperiode
        click Periode href "../Periode/"
    

        
      Applikasjonsressurstilgjengelighet : id
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Applikasjonsressurstilgjengelighet : konsument
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "1" Uriorcurie : konsument
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Applikasjonsressurstilgjengelighet : lisensantall
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "0..1" Integer : lisensantall
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
      Applikasjonsressurstilgjengelighet : ressursRef
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "1" Applikasjonsressurs : ressursRef
        click Applikasjonsressurs href "../Applikasjonsressurs/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [res:Applikasjonsressurstilgjengelighet](https://schema.fintlabs.no/ressurs/Applikasjonsressurstilgjengelighet) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gyldighetsperiode](gyldighetsperiode.md) | 1 <br/> [Periode](periode.md) | Periode ressursen er gyldig for |
| [konsument](konsument.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Referanse til Organisasjonselement som har tilgang til ressursen |
| [ressursRef](ressursref.md) | 1 <br/> [Applikasjonsressurs](applikasjonsressurs.md) | Ressursen organisasjonselementet har tilgang til |





  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  
    
  

  
  

  
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [lisensantall](lisensantall.md) | 0..1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | Totalt tal på lisensar |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | [applikasjonsressurstilgjengelegheit](applikasjonsressurstilgjengelegheit.md) | range | [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) |
| [Applikasjonsressurs](applikasjonsressurs.md) | [ressurstilgjengelighet](ressurstilgjengelighet.md) | range | [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:Applikasjonsressurstilgjengelighet |
| native | https://schema.fintlabs.no/ressurs/:Applikasjonsressurstilgjengelighet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Applikasjonsressurstilgjengelighet
description: Kva organisasjonselements brukarar som har tilgang til ein ressurs.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slots:
- id
- gyldighetsperiode
- lisensantall
- konsument
- ressursRef
slot_usage:
  gyldighetsperiode:
    name: gyldighetsperiode
    in_subset:
    - Obligatorisk
    required: true
  lisensantall:
    name: lisensantall
    in_subset:
    - Valgfri
  konsument:
    name: konsument
    in_subset:
    - Obligatorisk
    required: true
  ressursRef:
    name: ressursRef
    in_subset:
    - Obligatorisk
    required: true
class_uri: res:Applikasjonsressurstilgjengelighet

```
</details>

### Induced

<details>
```yaml
name: Applikasjonsressurstilgjengelighet
description: Kva organisasjonselements brukarar som har tilgang til ein ressurs.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_usage:
  gyldighetsperiode:
    name: gyldighetsperiode
    in_subset:
    - Obligatorisk
    required: true
  lisensantall:
    name: lisensantall
    in_subset:
    - Valgfri
  konsument:
    name: konsument
    in_subset:
    - Obligatorisk
    required: true
  ressursRef:
    name: ressursRef
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: Applikasjonsressurstilgjengelighet
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
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Periode ressursen er gyldig for.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:gyldighetsperiode
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Begrep
    - Identifikator
    - Applikasjon
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    - Rettighet
    - Applikasjonskategori
    - Brukertype
    - Enhetstype
    - Handhevingstype
    - Lisensmodell
    - Plattform
    - Produsent
    - Status
    range: Periode
    required: true
    inlined: true
  lisensantall:
    name: lisensantall
    description: Totalt tal på lisensar.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-ressurs
    rank: 1000
    slot_uri: res:lisensantall
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    range: integer
  konsument:
    name: konsument
    description: Referanse til Organisasjonselement som har tilgang til ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-ressurs
    rank: 1000
    slot_uri: res:konsument
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjonsressurstilgjengelighet
    range: uriorcurie
    required: true
  ressursRef:
    name: ressursRef
    description: Ressursen organisasjonselementet har tilgang til.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-ressurs
    rank: 1000
    slot_uri: res:ressursRef
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjonsressurstilgjengelighet
    range: Applikasjonsressurs
    required: true
class_uri: res:Applikasjonsressurstilgjengelighet

```
</details>