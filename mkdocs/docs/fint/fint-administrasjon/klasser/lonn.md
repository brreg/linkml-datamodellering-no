

# Class: Lonn 


_Informasjon om lønn for eit arbeidsforhold (abstrakt base)._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [adm:Lonn](https://schema.fintlabs.no/administrasjon/Lonn)





```mermaid
 classDiagram
    class Lonn
    click Lonn href "../Lonn/"
      Lonn <|-- Fastlonn
        click Fastlonn href "../Fastlonn/"
      Lonn <|-- Fasttillegg
        click Fasttillegg href "../Fasttillegg/"
      Lonn <|-- Variabellonn
        click Variabellonn href "../Variabellonn/"
      
      Lonn : anviser
        
          
    
        
        
        Lonn --> "0..1" Personalressurs : anviser
        click Personalressurs href "../Personalressurs/"
    

        
      Lonn : anvist
        
          
    
        
        
        Lonn --> "0..1" Datetime : anvist
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      Lonn : attestant
        
          
    
        
        
        Lonn --> "0..1" Personalressurs : attestant
        click Personalressurs href "../Personalressurs/"
    

        
      Lonn : attestert
        
          
    
        
        
        Lonn --> "0..1" Datetime : attestert
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      Lonn : beskrivelse
        
          
    
        
        
        Lonn --> "1" String : beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Lonn : id
        
          
    
        
        
        Lonn --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Lonn : kildesystemId
        
          
    
        
        
        Lonn --> "0..1" Identifikator : kildesystemId
        click Identifikator href "../Identifikator/"
    

        
      Lonn : konterer
        
          
    
        
        
        Lonn --> "0..1" Personalressurs : konterer
        click Personalressurs href "../Personalressurs/"
    

        
      Lonn : kontert
        
          
    
        
        
        Lonn --> "0..1" Datetime : kontert
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      Lonn : kontostreng
        
          
    
        
        
        Lonn --> "1" Kontostreng : kontostreng
        click Kontostreng href "../Kontostreng/"
    

        
      Lonn : opptjent
        
          
    
        
        
        Lonn --> "0..1" Periode : opptjent
        click Periode href "../Periode/"
    

        
      Lonn : periode
        
          
    
        
        
        Lonn --> "1" Periode : periode
        click Periode href "../Periode/"
    

        
      
```





## Inheritance
* **Lonn**
    * [Fastlonn](fastlonn.md)
    * [Fasttillegg](fasttillegg.md)
    * [Variabellonn](variabellonn.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [adm:Lonn](https://schema.fintlabs.no/administrasjon/Lonn) |


## Eigenskapar







  
  

  
  

  
  

  
  
    
  

  
  

  
  

  
  
    
  

  
  

  
  
    
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Beskriven namn eller omtale |
| [kontostreng](kontostreng.md) | 1 <br/> [Kontostreng](kontostreng.md) | Kontering av lønn |
| [periode](periode.md) | 1 <br/> [Periode](periode.md) | Periode for ressursen |





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  
    
  

  
  
    
  

  
  

  
  
    
  

  
  
    
  

  
  

  
  
    
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [anvist](anvist.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Tidspunkt då lønn vart anvist |
| [attestert](attestert.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Tidspunkt då lønn vart attestert |
| [kildesystemId](kildesystemid.md) | 0..1 <br/> [Identifikator](identifikator.md) | Kjeldesystemets unike identifikator |
| [kontert](kontert.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Tidspunkt då lønn vart kontert |
| [opptjent](opptjent.md) | 0..1 <br/> [Periode](periode.md) | Periode der lønn vart opptent |
| [anviser](anviser.md) | 0..1 <br/> [Personalressurs](personalressurs.md) | Personalressurs som har anvist lønsmeldinga etter fullmakt |
| [konterer](konterer.md) | 0..1 <br/> [Personalressurs](personalressurs.md) | Personalressurs som har kontert lønsmeldinga etter fullmakt |
| [attestant](attestant.md) | 0..1 <br/> [Personalressurs](personalressurs.md) | Personalressurs som har attestert lønsmeldinga etter fullmakt |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:Lonn |
| native | https://schema.fintlabs.no/administrasjon/:Lonn |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Lonn
description: Informasjon om lønn for eit arbeidsforhold (abstrakt base).
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
abstract: true
slots:
- id
- anvist
- attestert
- beskrivelse
- kildesystemId
- kontert
- kontostreng
- opptjent
- periode
- anviser
- konterer
- attestant
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  kontostreng:
    name: kontostreng
    in_subset:
    - Obligatorisk
    required: true
  periode:
    name: periode
    in_subset:
    - Obligatorisk
    required: true
  anvist:
    name: anvist
    in_subset:
    - Valgfri
  attestert:
    name: attestert
    in_subset:
    - Valgfri
  kildesystemId:
    name: kildesystemId
    in_subset:
    - Valgfri
  kontert:
    name: kontert
    in_subset:
    - Valgfri
  opptjent:
    name: opptjent
    in_subset:
    - Valgfri
  anviser:
    name: anviser
    in_subset:
    - Valgfri
  konterer:
    name: konterer
    in_subset:
    - Valgfri
  attestant:
    name: attestant
    in_subset:
    - Valgfri
class_uri: adm:Lonn

```
</details>

### Induced

<details>
```yaml
name: Lonn
description: Informasjon om lønn for eit arbeidsforhold (abstrakt base).
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
abstract: true
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  kontostreng:
    name: kontostreng
    in_subset:
    - Obligatorisk
    required: true
  periode:
    name: periode
    in_subset:
    - Obligatorisk
    required: true
  anvist:
    name: anvist
    in_subset:
    - Valgfri
  attestert:
    name: attestert
    in_subset:
    - Valgfri
  kildesystemId:
    name: kildesystemId
    in_subset:
    - Valgfri
  kontert:
    name: kontert
    in_subset:
    - Valgfri
  opptjent:
    name: opptjent
    in_subset:
    - Valgfri
  anviser:
    name: anviser
    in_subset:
    - Valgfri
  konterer:
    name: konterer
    in_subset:
    - Valgfri
  attestant:
    name: attestant
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: Lonn
    domain_of:
    - Begrep
    - Elev
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    - Lonn
    - Fravaer
    - Fullmakt
    - Rolle
    - Arbeidslokasjon
    - Organisasjonselement
    - Personalressurs
    - Arbeidsforhold
    range: uriorcurie
    required: true
  anvist:
    name: anvist
    description: Tidspunkt då lønn vart anvist.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:anvist
    owner: Lonn
    domain_of:
    - Lonn
    range: datetime
  attestert:
    name: attestert
    description: Tidspunkt då lønn vart attestert.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:attestert
    owner: Lonn
    domain_of:
    - Lonn
    range: datetime
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn eller omtale.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:beskrivelse
    owner: Lonn
    domain_of:
    - Periode
    - Lonn
    - Rolle
    range: string
    required: true
  kildesystemId:
    name: kildesystemId
    description: Kjeldesystemets unike identifikator.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:kildesystemId
    owner: Lonn
    domain_of:
    - Lonn
    - Fravaer
    range: Identifikator
    inlined: true
  kontert:
    name: kontert
    description: Tidspunkt då lønn vart kontert.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:kontert
    owner: Lonn
    domain_of:
    - Lonn
    range: datetime
  kontostreng:
    name: kontostreng
    description: Kontering av lønn.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:kontostreng
    owner: Lonn
    domain_of:
    - Lonn
    range: Kontostreng
    required: true
    inlined: true
  opptjent:
    name: opptjent
    description: Periode der lønn vart opptent.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:opptjent
    owner: Lonn
    domain_of:
    - Lonn
    range: Periode
    inlined: true
  periode:
    name: periode
    description: Periode for ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:periode
    owner: Lonn
    domain_of:
    - Lonn
    - Fravaer
    range: Periode
    required: true
    inlined: true
  anviser:
    name: anviser
    description: Personalressurs som har anvist lønsmeldinga etter fullmakt.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:anviser
    owner: Lonn
    domain_of:
    - Lonn
    range: Personalressurs
  konterer:
    name: konterer
    description: Personalressurs som har kontert lønsmeldinga etter fullmakt.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:konterer
    owner: Lonn
    domain_of:
    - Lonn
    range: Personalressurs
  attestant:
    name: attestant
    description: Personalressurs som har attestert lønsmeldinga etter fullmakt.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-administrasjon
    rank: 1000
    slot_uri: adm:attestant
    owner: Lonn
    domain_of:
    - Lonn
    range: Personalressurs
class_uri: adm:Lonn

```
</details>