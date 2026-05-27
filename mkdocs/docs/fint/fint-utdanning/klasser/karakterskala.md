

# Class: Karakterskala 


_Skala for karaktersetjing (t.d. 1-6, Bestått/Ikkje bestått)._





URI: [utd:Karakterskala](https://schema.fintlabs.no/utdanning/Karakterskala)





```mermaid
 classDiagram
    class Karakterskala
    click Karakterskala href "../Karakterskala/"
      Karakterskala : gyldighetsperiode
        
          
    
        
        
        Karakterskala --> "0..1" Periode : gyldighetsperiode
        click Periode href "../Periode/"
    

        
      Karakterskala : id
        
          
    
        
        
        Karakterskala --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Karakterskala : kode
        
          
    
        
        
        Karakterskala --> "1" String : kode
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Karakterskala : navn
        
          
    
        
        
        Karakterskala --> "1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Karakterskala : passiv
        
          
    
        
        
        Karakterskala --> "0..1" Boolean : passiv
        click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"
    

        
      Karakterskala : verdi
        
          
    
        
        
        Karakterskala --> "*" Karakterverdi : verdi
        click Karakterverdi href "../Karakterverdi/"
    

        
      Karakterskala : vigoreferanse
        
          
    
        
        
        Karakterskala --> "0..1" Uriorcurie : vigoreferanse
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Karakterskala](https://schema.fintlabs.no/utdanning/Karakterskala) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kode](kode.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Verdi som identifiserer omgrepet |
| [navn](navn.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Hovudnamn for ressursen |





  
  

  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gyldighetsperiode](gyldighetsperiode.md) | 0..1 <br/> [Periode](periode.md) | Periode ressursen er gyldig for |
| [passiv](passiv.md) | 0..1 <br/> [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) | Angir at koden er passiv og ikkje kan veljast |
| [verdi](verdi.md) | * <br/> [Karakterverdi](karakterverdi.md) | Karakterverdiar i skalaen |
| [vigoreferanse](vigoreferanse.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Referanse til Vigo-systemet |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | [karakterskalaer](karakterskalaer.md) | range | [Karakterskala](karakterskala.md) |
| [Karakterverdi](karakterverdi.md) | [skala](skala.md) | range | [Karakterskala](karakterskala.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:Karakterskala |
| native | https://schema.fintlabs.no/utdanning/:Karakterskala |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Karakterskala
description: Skala for karaktersetjing (t.d. 1-6, Bestått/Ikkje bestått).
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slots:
- id
- kode
- navn
- gyldighetsperiode
- passiv
- verdi
- vigoreferanse
slot_usage:
  kode:
    name: kode
    in_subset:
    - Obligatorisk
    required: true
  navn:
    name: navn
    in_subset:
    - Obligatorisk
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    in_subset:
    - Valgfri
  passiv:
    name: passiv
    in_subset:
    - Valgfri
  verdi:
    name: verdi
    in_subset:
    - Valgfri
  vigoreferanse:
    name: vigoreferanse
    in_subset:
    - Valgfri
class_uri: utd:Karakterskala

```
</details>

### Induced

<details>
```yaml
name: Karakterskala
description: Skala for karaktersetjing (t.d. 1-6, Bestått/Ikkje bestått).
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_usage:
  kode:
    name: kode
    in_subset:
    - Obligatorisk
    required: true
  navn:
    name: navn
    in_subset:
    - Obligatorisk
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    in_subset:
    - Valgfri
  passiv:
    name: passiv
    in_subset:
    - Valgfri
  verdi:
    name: verdi
    in_subset:
    - Valgfri
  vigoreferanse:
    name: vigoreferanse
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: Karakterskala
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
  kode:
    name: kode
    description: Verdi som identifiserer omgrepet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:kode
    owner: Karakterskala
    domain_of:
    - Begrep
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
  navn:
    name: navn
    description: Hovudnamn for ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:navn
    owner: Karakterskala
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
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Periode ressursen er gyldig for.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:gyldighetsperiode
    owner: Karakterskala
    domain_of:
    - Begrep
    - Identifikator
    - Gruppemedlemskap
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
    range: Periode
    inlined: true
  passiv:
    name: passiv
    description: Angir at koden er passiv og ikkje kan veljast.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:passiv
    owner: Karakterskala
    domain_of:
    - Begrep
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
    range: boolean
  verdi:
    name: verdi
    description: Karakterverdiar i skalaen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-utdanning
    rank: 1000
    slot_uri: utd:verdi
    owner: Karakterskala
    domain_of:
    - Karakterskala
    range: Karakterverdi
    multivalued: true
  vigoreferanse:
    name: vigoreferanse
    description: Referanse til Vigo-systemet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-utdanning
    rank: 1000
    slot_uri: utd:vigoreferanse
    owner: Karakterskala
    domain_of:
    - Skole
    - Arstrinn
    - Programomrade
    - Utdanningsprogram
    - Fag
    - Karakterskala
    range: uriorcurie
class_uri: utd:Karakterskala

```
</details>