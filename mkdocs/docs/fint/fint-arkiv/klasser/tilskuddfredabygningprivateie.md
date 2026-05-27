

# Class: TilskuddFredaBygningPrivatEie 


_Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP)._





URI: [ark:TilskuddFredaBygningPrivatEie](https://schema.fintlabs.no/arkiv/TilskuddFredaBygningPrivatEie)





```mermaid
 classDiagram
    class TilskuddFredaBygningPrivatEie
    click TilskuddFredaBygningPrivatEie href "../TilskuddFredaBygningPrivatEie/"
      Saksmappe <|-- TilskuddFredaBygningPrivatEie
        click Saksmappe href "../Saksmappe/"
      
      TilskuddFredaBygningPrivatEie : administrativEnhet
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "1" AdministrativEnhet : administrativEnhet
        click AdministrativEnhet href "../AdministrativEnhet/"
    

        
      TilskuddFredaBygningPrivatEie : arkivdel
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Arkivdel : arkivdel
        click Arkivdel href "../Arkivdel/"
    

        
      TilskuddFredaBygningPrivatEie : avsluttetAv
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Arkivressurs : avsluttetAv
        click Arkivressurs href "../Arkivressurs/"
    

        
      TilskuddFredaBygningPrivatEie : avsluttetDato
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Datetime : avsluttetDato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      TilskuddFredaBygningPrivatEie : beskrivelse
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" String : beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : bygningsnavn
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" String : bygningsnavn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : id
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      TilskuddFredaBygningPrivatEie : journalenhet
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" AdministrativEnhet : journalenhet
        click AdministrativEnhet href "../AdministrativEnhet/"
    

        
      TilskuddFredaBygningPrivatEie : journalpost
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "*" Journalpost : journalpost
        click Journalpost href "../Journalpost/"
    

        
      TilskuddFredaBygningPrivatEie : klasse
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "*" Klasse : klasse
        click Klasse href "../Klasse/"
    

        
      TilskuddFredaBygningPrivatEie : kulturminneId
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "1" String : kulturminneId
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : mappeId
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Identifikator : mappeId
        click Identifikator href "../Identifikator/"
    

        
      TilskuddFredaBygningPrivatEie : matrikkelnummer
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Matrikkelnummer : matrikkelnummer
        click Matrikkelnummer href "../Matrikkelnummer/"
    

        
      TilskuddFredaBygningPrivatEie : merknad
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "*" Merknad : merknad
        click Merknad href "../Merknad/"
    

        
      TilskuddFredaBygningPrivatEie : noekkelord
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "*" String : noekkelord
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : offentligTittel
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" String : offentligTittel
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : opprettetAv
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "1" Arkivressurs : opprettetAv
        click Arkivressurs href "../Arkivressurs/"
    

        
      TilskuddFredaBygningPrivatEie : opprettetDato
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Datetime : opprettetDato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      TilskuddFredaBygningPrivatEie : part
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "*" Part : part
        click Part href "../Part/"
    

        
      TilskuddFredaBygningPrivatEie : saksaar
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" String : saksaar
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : saksansvarlig
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "1" Arkivressurs : saksansvarlig
        click Arkivressurs href "../Arkivressurs/"
    

        
      TilskuddFredaBygningPrivatEie : saksdato
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Datetime : saksdato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      TilskuddFredaBygningPrivatEie : saksmappetype
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Saksmappetype : saksmappetype
        click Saksmappetype href "../Saksmappetype/"
    

        
      TilskuddFredaBygningPrivatEie : sakssekvensnummer
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" String : sakssekvensnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : saksstatus
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "1" Saksstatus : saksstatus
        click Saksstatus href "../Saksstatus/"
    

        
      TilskuddFredaBygningPrivatEie : skjerming
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Skjerming : skjerming
        click Skjerming href "../Skjerming/"
    

        
      TilskuddFredaBygningPrivatEie : soeknadsnummer
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Identifikator : soeknadsnummer
        click Identifikator href "../Identifikator/"
    

        
      TilskuddFredaBygningPrivatEie : tilgangsgruppe
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Tilgangsgruppe : tilgangsgruppe
        click Tilgangsgruppe href "../Tilgangsgruppe/"
    

        
      TilskuddFredaBygningPrivatEie : tittel
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" String : tittel
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      TilskuddFredaBygningPrivatEie : utlaantDato
        
          
    
        
        
        TilskuddFredaBygningPrivatEie --> "0..1" Datetime : utlaantDato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      
```





## Inheritance
* [Mappe](mappe.md)
    * [Saksmappe](saksmappe.md)
        * **TilskuddFredaBygningPrivatEie**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ark:TilskuddFredaBygningPrivatEie](https://schema.fintlabs.no/arkiv/TilskuddFredaBygningPrivatEie) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kulturminneId](kulturminneid.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Kulturminnets ID i Askeladden |





  
  

  
  

  
  

  
  





  
  
    
  

  
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [bygningsnavn](bygningsnavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Bygningens namn |
| [matrikkelnummer](matrikkelnummer.md) | 0..1 <br/> [Matrikkelnummer](matrikkelnummer.md) | Kulturminnets/bygningens identifikator i Matrikkelen |
| [soeknadsnummer](soeknadsnummer.md) | 0..1 <br/> [Identifikator](identifikator.md) | Søknadsnummer frå Digisak |






  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [journalpost](journalpost.md) | * <br/> [Journalpost](journalpost.md) | Journalpostar knytt til saksmappa | [Saksmappe](saksmappe.md) |
| [saksaar](saksaar.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Inngår i M003 mappeID — viser året saksmappa vart oppretta | [Saksmappe](saksmappe.md) |
| [saksdato](saksdato.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Datoen saka er oppretta | [Saksmappe](saksmappe.md) |
| [sakssekvensnummer](sakssekvensnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Inngår i M003 mappeID — viser rekkjefølgja saksmappene vart oppretta | [Saksmappe](saksmappe.md) |
| [utlaantDato](utlaantdato.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Dato ein fysisk saksmappe eller journalpost vart utlånt | [Saksmappe](saksmappe.md) |
| [saksmappetype](saksmappetype.md) | 0..1 <br/> [Saksmappetype](saksmappetype.md) | Type saksmappe | [Saksmappe](saksmappe.md) |
| [saksstatus](saksstatus.md) | 1 <br/> [Saksstatus](saksstatus.md) | Status til saksmappa | [Saksmappe](saksmappe.md) |
| [tilgangsgruppe](tilgangsgruppe.md) | 0..1 <br/> [Tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe som har tilgang til arkivenheten | [Saksmappe](saksmappe.md) |
| [journalenhet](journalenhet.md) | 0..1 <br/> [AdministrativEnhet](administrativenhet.md) | Eining med arkivmessig ansvar | [Saksmappe](saksmappe.md) |
| [administrativEnhet](administrativenhet.md) | 1 <br/> [AdministrativEnhet](administrativenhet.md) | Administrativ eining som har ansvar for saksbehandlinga | [Saksmappe](saksmappe.md) |
| [saksansvarlig](saksansvarlig.md) | 1 <br/> [Arkivressurs](arkivressurs.md) | Person som er saksansvarleg | [Saksmappe](saksmappe.md) |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Mappe](mappe.md) |
| [avsluttetDato](avsluttetdato.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Dato og klokkeslett når arkivenheten vart avslutta/lukka | [Mappe](mappe.md) |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Beskriven namn eller omtale | [Mappe](mappe.md) |
| [klasse](klasse.md) | * <br/> [Klasse](klasse.md) | Klassifisering av arkivenhet | [Mappe](mappe.md) |
| [mappeId](mappeid.md) | 0..1 <br/> [Identifikator](identifikator.md) | Eintydig identifikasjon av mappa innanfor arkivet | [Mappe](mappe.md) |
| [merknad](merknad.md) | * <br/> [Merknad](merknad.md) | Merknader knytt til arkivenhet | [Mappe](mappe.md) |
| [noekkelord](noekkelord.md) | * <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Nøkkelord som skildrar innhaldet (Mappe) | [Mappe](mappe.md) |
| [offentligTittel](offentligtittel.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Offentleg tittel der skjerma ord er fjerna | [Mappe](mappe.md) |
| [opprettetDato](opprettetdato.md) | 0..1 <br/> [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Dato og klokkeslett arkivenheten vart oppretta/registrert | [Mappe](mappe.md) |
| [part](part.md) | * <br/> [Part](part.md) | Partar til arkivenhet | [Mappe](mappe.md) |
| [skjerming](skjerming.md) | 0..1 <br/> [Skjerming](skjerming.md) | Skjerming av arkivenhet | [Mappe](mappe.md) |
| [tittel](tittel.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tittel eller namn på arkivenheten | [Mappe](mappe.md) |
| [arkivdel](arkivdel.md) | 0..1 <br/> [Arkivdel](arkivdel.md) | Arkivdel arkivenheten tilhøyrer | [Mappe](mappe.md) |
| [avsluttetAv](avsluttetav.md) | 0..1 <br/> [Arkivressurs](arkivressurs.md) | Person som avslutta/lukka arkivenheten | [Mappe](mappe.md) |
| [opprettetAv](opprettetav.md) | 1 <br/> [Arkivressurs](arkivressurs.md) | Person som oppretta/registrerte arkivenheten | [Mappe](mappe.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | [tilskuddFredaBygningPrivatEie_liste](tilskuddfredabygningprivateie_liste.md) | range | [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:TilskuddFredaBygningPrivatEie |
| native | https://schema.fintlabs.no/arkiv/:TilskuddFredaBygningPrivatEie |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TilskuddFredaBygningPrivatEie
description: Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP).
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
is_a: Saksmappe
slots:
- bygningsnavn
- kulturminneId
- matrikkelnummer
- soeknadsnummer
slot_usage:
  bygningsnavn:
    name: bygningsnavn
    in_subset:
    - Valgfri
  kulturminneId:
    name: kulturminneId
    in_subset:
    - Obligatorisk
    required: true
  matrikkelnummer:
    name: matrikkelnummer
    in_subset:
    - Valgfri
  soeknadsnummer:
    name: soeknadsnummer
    in_subset:
    - Valgfri
class_uri: ark:TilskuddFredaBygningPrivatEie

```
</details>

### Induced

<details>
```yaml
name: TilskuddFredaBygningPrivatEie
description: Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP).
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
is_a: Saksmappe
slot_usage:
  bygningsnavn:
    name: bygningsnavn
    in_subset:
    - Valgfri
  kulturminneId:
    name: kulturminneId
    in_subset:
    - Obligatorisk
    required: true
  matrikkelnummer:
    name: matrikkelnummer
    in_subset:
    - Valgfri
  soeknadsnummer:
    name: soeknadsnummer
    in_subset:
    - Valgfri
attributes:
  bygningsnavn:
    name: bygningsnavn
    description: Bygningens namn.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:bygningsnavn
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - TilskuddFredaBygningPrivatEie
    range: string
  kulturminneId:
    name: kulturminneId
    description: Kulturminnets ID i Askeladden.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:kulturminneId
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - DispensasjonAutomatiskFredaKulturminne
    - TilskuddFartoy
    - TilskuddFredaBygningPrivatEie
    range: string
    required: true
  matrikkelnummer:
    name: matrikkelnummer
    description: Kulturminnets/bygningens identifikator i Matrikkelen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:matrikkelnummer
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - DispensasjonAutomatiskFredaKulturminne
    - TilskuddFredaBygningPrivatEie
    range: Matrikkelnummer
    inlined: true
  soeknadsnummer:
    name: soeknadsnummer
    description: Søknadsnummer frå Digisak.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:soeknadsnummer
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - DispensasjonAutomatiskFredaKulturminne
    - TilskuddFartoy
    - TilskuddFredaBygningPrivatEie
    range: Identifikator
    inlined: true
  journalpost:
    name: journalpost
    description: Journalpostar knytt til saksmappa.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:journalpost
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: Journalpost
    multivalued: true
  saksaar:
    name: saksaar
    description: Inngår i M003 mappeID — viser året saksmappa vart oppretta.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:saksaar
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: string
  saksdato:
    name: saksdato
    description: Datoen saka er oppretta.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:saksdato
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: datetime
  sakssekvensnummer:
    name: sakssekvensnummer
    description: Inngår i M003 mappeID — viser rekkjefølgja saksmappene vart oppretta.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:sakssekvensnummer
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: string
  utlaantDato:
    name: utlaantDato
    description: Dato ein fysisk saksmappe eller journalpost vart utlånt.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:utlaantDato
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: datetime
  saksmappetype:
    name: saksmappetype
    description: Type saksmappe.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:saksmappetype
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: Saksmappetype
  saksstatus:
    name: saksstatus
    description: Status til saksmappa.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:saksstatus
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: Saksstatus
    required: true
  tilgangsgruppe:
    name: tilgangsgruppe
    description: Tilgangsgruppe som har tilgang til arkivenheten.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:tilgangsgruppe
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    - Registrering
    range: Tilgangsgruppe
  journalenhet:
    name: journalenhet
    description: Eining med arkivmessig ansvar.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:journalenhet
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    - Journalpost
    range: AdministrativEnhet
  administrativEnhet:
    name: administrativEnhet
    description: Administrativ eining som har ansvar for saksbehandlinga.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:administrativEnhet
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    - Registrering
    - Tilgang
    range: AdministrativEnhet
    required: true
  saksansvarlig:
    name: saksansvarlig
    description: Person som er saksansvarleg.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:saksansvarlig
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Saksmappe
    range: Arkivressurs
    required: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Begrep
    - Elev
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    - Mappe
    - Registrering
    - AdministrativEnhet
    - Arkivdel
    - Arkivressurs
    - Autorisasjon
    - Dokumentfil
    - Klassifikasjonssystem
    - Tilgang
    - Dokumentbeskrivelse
    - DokumentStatus
    - DokumentType
    - Format
    - JournalpostType
    - JournalStatus
    - Klassifikasjonstype
    - KorrespondansepartType
    - Merknadstype
    - PartRolle
    - Rolle
    - Saksmappetype
    - Saksstatus
    - Skjermingshjemmel
    - Tilgangsgruppe
    - Tilgangsrestriksjon
    - TilknyttetRegistreringSom
    - Variantformat
    range: uriorcurie
    required: true
  avsluttetDato:
    name: avsluttetDato
    description: Dato og klokkeslett når arkivenheten vart avslutta/lukka.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:avsluttetDato
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Klassifikasjonssystem
    range: datetime
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn eller omtale.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:beskrivelse
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Periode
    - Mappe
    - Registrering
    - Klassifikasjonssystem
    - Dokumentbeskrivelse
    range: string
  klasse:
    name: klasse
    description: Klassifisering av arkivenhet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:klasse
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Klassifikasjonssystem
    range: Klasse
    multivalued: true
    inlined: true
    inlined_as_list: true
  mappeId:
    name: mappeId
    description: Eintydig identifikasjon av mappa innanfor arkivet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:mappeId
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    range: Identifikator
    inlined: true
  merknad:
    name: merknad
    description: Merknader knytt til arkivenhet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:merknad
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    range: Merknad
    multivalued: true
    inlined: true
    inlined_as_list: true
  noekkelord:
    name: noekkelord
    description: Nøkkelord som skildrar innhaldet (Mappe).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:noekkelord
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    range: string
    multivalued: true
  offentligTittel:
    name: offentligTittel
    description: Offentleg tittel der skjerma ord er fjerna.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:offentligTittel
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    range: string
  opprettetDato:
    name: opprettetDato
    description: Dato og klokkeslett arkivenheten vart oppretta/registrert.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:opprettetDato
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Klassifikasjonssystem
    - Dokumentbeskrivelse
    range: datetime
  part:
    name: part
    description: Partar til arkivenhet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:part
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Dokumentbeskrivelse
    range: Part
    multivalued: true
    inlined: true
    inlined_as_list: true
  skjerming:
    name: skjerming
    description: Skjerming av arkivenhet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:skjerming
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Dokumentbeskrivelse
    - Klasse
    - Korrespondansepart
    range: Skjerming
    inlined: true
  tittel:
    name: tittel
    description: Tittel eller namn på arkivenheten.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:tittel
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Arkivdel
    - Klassifikasjonssystem
    - Tilgang
    - Dokumentbeskrivelse
    - Klasse
    range: string
  arkivdel:
    name: arkivdel
    description: Arkivdel arkivenheten tilhøyrer.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:arkivdel
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Klassifikasjonssystem
    - Tilgang
    range: Arkivdel
  avsluttetAv:
    name: avsluttetAv
    description: Person som avslutta/lukka arkivenheten.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:avsluttetAv
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    range: Arkivressurs
  opprettetAv:
    name: opprettetAv
    description: Person som oppretta/registrerte arkivenheten.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:opprettetAv
    owner: TilskuddFredaBygningPrivatEie
    domain_of:
    - Mappe
    - Registrering
    - Dokumentbeskrivelse
    - Dokumentobjekt
    range: Arkivressurs
    required: true
class_uri: ark:TilskuddFredaBygningPrivatEie

```
</details>