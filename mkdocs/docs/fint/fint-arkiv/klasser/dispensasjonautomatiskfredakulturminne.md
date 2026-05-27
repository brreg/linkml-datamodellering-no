

# Class: DispensasjonAutomatiskFredaKulturminne 


_Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne._





URI: [ark:DispensasjonAutomatiskFredaKulturminne](https://schema.fintlabs.no/arkiv/DispensasjonAutomatiskFredaKulturminne)





```mermaid
 classDiagram
    class DispensasjonAutomatiskFredaKulturminne
    click DispensasjonAutomatiskFredaKulturminne href "../DispensasjonAutomatiskFredaKulturminne/"
      Saksmappe <|-- DispensasjonAutomatiskFredaKulturminne
        click Saksmappe href "../Saksmappe/"
      
      DispensasjonAutomatiskFredaKulturminne : administrativEnhet
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" AdministrativEnhet : administrativEnhet
        click AdministrativEnhet href "../AdministrativEnhet/"
    

        
      DispensasjonAutomatiskFredaKulturminne : arkivdel
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Arkivdel : arkivdel
        click Arkivdel href "../Arkivdel/"
    

        
      DispensasjonAutomatiskFredaKulturminne : avsluttetAv
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Arkivressurs : avsluttetAv
        click Arkivressurs href "../Arkivressurs/"
    

        
      DispensasjonAutomatiskFredaKulturminne : avsluttetDato
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Datetime : avsluttetDato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      DispensasjonAutomatiskFredaKulturminne : beskrivelse
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" String : beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : id
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      DispensasjonAutomatiskFredaKulturminne : journalenhet
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" AdministrativEnhet : journalenhet
        click AdministrativEnhet href "../AdministrativEnhet/"
    

        
      DispensasjonAutomatiskFredaKulturminne : journalpost
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "*" Journalpost : journalpost
        click Journalpost href "../Journalpost/"
    

        
      DispensasjonAutomatiskFredaKulturminne : klasse
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "*" Klasse : klasse
        click Klasse href "../Klasse/"
    

        
      DispensasjonAutomatiskFredaKulturminne : kulturminneId
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" String : kulturminneId
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : mappeId
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Identifikator : mappeId
        click Identifikator href "../Identifikator/"
    

        
      DispensasjonAutomatiskFredaKulturminne : matrikkelnummer
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" Matrikkelnummer : matrikkelnummer
        click Matrikkelnummer href "../Matrikkelnummer/"
    

        
      DispensasjonAutomatiskFredaKulturminne : merknad
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "*" Merknad : merknad
        click Merknad href "../Merknad/"
    

        
      DispensasjonAutomatiskFredaKulturminne : noekkelord
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "*" String : noekkelord
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : offentligTittel
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" String : offentligTittel
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : opprettetAv
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" Arkivressurs : opprettetAv
        click Arkivressurs href "../Arkivressurs/"
    

        
      DispensasjonAutomatiskFredaKulturminne : opprettetDato
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Datetime : opprettetDato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      DispensasjonAutomatiskFredaKulturminne : part
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "*" Part : part
        click Part href "../Part/"
    

        
      DispensasjonAutomatiskFredaKulturminne : saksaar
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" String : saksaar
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : saksansvarlig
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" Arkivressurs : saksansvarlig
        click Arkivressurs href "../Arkivressurs/"
    

        
      DispensasjonAutomatiskFredaKulturminne : saksdato
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Datetime : saksdato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      DispensasjonAutomatiskFredaKulturminne : saksmappetype
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Saksmappetype : saksmappetype
        click Saksmappetype href "../Saksmappetype/"
    

        
      DispensasjonAutomatiskFredaKulturminne : sakssekvensnummer
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" String : sakssekvensnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : saksstatus
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" Saksstatus : saksstatus
        click Saksstatus href "../Saksstatus/"
    

        
      DispensasjonAutomatiskFredaKulturminne : skjerming
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Skjerming : skjerming
        click Skjerming href "../Skjerming/"
    

        
      DispensasjonAutomatiskFredaKulturminne : soeknadsnummer
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "1" Identifikator : soeknadsnummer
        click Identifikator href "../Identifikator/"
    

        
      DispensasjonAutomatiskFredaKulturminne : tilgangsgruppe
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Tilgangsgruppe : tilgangsgruppe
        click Tilgangsgruppe href "../Tilgangsgruppe/"
    

        
      DispensasjonAutomatiskFredaKulturminne : tiltak
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" String : tiltak
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : tittel
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" String : tittel
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      DispensasjonAutomatiskFredaKulturminne : utlaantDato
        
          
    
        
        
        DispensasjonAutomatiskFredaKulturminne --> "0..1" Datetime : utlaantDato
        click Datetime href "../http://www.w3.org/2001/XMLSchema#dateTime/"
    

        
      
```





## Inheritance
* [Mappe](mappe.md)
    * [Saksmappe](saksmappe.md)
        * **DispensasjonAutomatiskFredaKulturminne**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ark:DispensasjonAutomatiskFredaKulturminne](https://schema.fintlabs.no/arkiv/DispensasjonAutomatiskFredaKulturminne) |


## Eigenskapar







  
  
    
  

  
  
    
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kulturminneId](kulturminneid.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Kulturminnets ID i Askeladden |
| [matrikkelnummer](matrikkelnummer.md) | 1 <br/> [Matrikkelnummer](matrikkelnummer.md) | Kulturminnets/bygningens identifikator i Matrikkelen |
| [soeknadsnummer](soeknadsnummer.md) | 1 <br/> [Identifikator](identifikator.md) | Søknadsnummer frå Digisak |





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tiltak](tiltak.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Skildrar kva tiltak som skal utførast på eigedommen |






  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  




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
| [ArkivContainer](arkivcontainer.md) | [dispensasjonAutomatiskFredaKulturminne_liste](dispensasjonautomatiskfredakulturminne_liste.md) | range | [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:DispensasjonAutomatiskFredaKulturminne |
| native | https://schema.fintlabs.no/arkiv/:DispensasjonAutomatiskFredaKulturminne |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DispensasjonAutomatiskFredaKulturminne
description: Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
is_a: Saksmappe
slots:
- kulturminneId
- matrikkelnummer
- soeknadsnummer
- tiltak
slot_usage:
  kulturminneId:
    name: kulturminneId
    in_subset:
    - Obligatorisk
    required: true
  matrikkelnummer:
    name: matrikkelnummer
    in_subset:
    - Obligatorisk
    required: true
  soeknadsnummer:
    name: soeknadsnummer
    in_subset:
    - Obligatorisk
    required: true
  tiltak:
    name: tiltak
    in_subset:
    - Valgfri
class_uri: ark:DispensasjonAutomatiskFredaKulturminne

```
</details>

### Induced

<details>
```yaml
name: DispensasjonAutomatiskFredaKulturminne
description: Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
is_a: Saksmappe
slot_usage:
  kulturminneId:
    name: kulturminneId
    in_subset:
    - Obligatorisk
    required: true
  matrikkelnummer:
    name: matrikkelnummer
    in_subset:
    - Obligatorisk
    required: true
  soeknadsnummer:
    name: soeknadsnummer
    in_subset:
    - Obligatorisk
    required: true
  tiltak:
    name: tiltak
    in_subset:
    - Valgfri
attributes:
  kulturminneId:
    name: kulturminneId
    description: Kulturminnets ID i Askeladden.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:kulturminneId
    owner: DispensasjonAutomatiskFredaKulturminne
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
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:matrikkelnummer
    owner: DispensasjonAutomatiskFredaKulturminne
    domain_of:
    - DispensasjonAutomatiskFredaKulturminne
    - TilskuddFredaBygningPrivatEie
    range: Matrikkelnummer
    required: true
    inlined: true
  soeknadsnummer:
    name: soeknadsnummer
    description: Søknadsnummer frå Digisak.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:soeknadsnummer
    owner: DispensasjonAutomatiskFredaKulturminne
    domain_of:
    - DispensasjonAutomatiskFredaKulturminne
    - TilskuddFartoy
    - TilskuddFredaBygningPrivatEie
    range: Identifikator
    required: true
    inlined: true
  tiltak:
    name: tiltak
    description: Skildrar kva tiltak som skal utførast på eigedommen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:tiltak
    owner: DispensasjonAutomatiskFredaKulturminne
    domain_of:
    - DispensasjonAutomatiskFredaKulturminne
    range: string
  journalpost:
    name: journalpost
    description: Journalpostar knytt til saksmappa.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-arkiv
    rank: 1000
    slot_uri: ark:journalpost
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
    domain_of:
    - Saksmappe
    range: Arkivressurs
    required: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
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
    owner: DispensasjonAutomatiskFredaKulturminne
    domain_of:
    - Mappe
    - Registrering
    - Dokumentbeskrivelse
    - Dokumentobjekt
    range: Arkivressurs
    required: true
class_uri: ark:DispensasjonAutomatiskFredaKulturminne

```
</details>