

# Class: Virksomhet 


_Ein juridisk organisasjon som produserer varer eller tenester._





URI: [fint:Virksomhet](https://schema.fintlabs.no/Virksomhet)





```mermaid
 classDiagram
    class Virksomhet
    click Virksomhet href "../Virksomhet/"
      Enhet <|-- Virksomhet
        click Enhet href "../Enhet/"
      
      Virksomhet : forretningsadresse
        
          
    
        
        
        Virksomhet --> "0..1" Adresse : forretningsadresse
        click Adresse href "../Adresse/"
    

        
      Virksomhet : id
        
          
    
        
        
        Virksomhet --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Virksomhet : kontaktinformasjon
        
          
    
        
        
        Virksomhet --> "0..1" Kontaktinformasjon : kontaktinformasjon
        click Kontaktinformasjon href "../Kontaktinformasjon/"
    

        
      Virksomhet : laerling
        
          
    
        
        
        Virksomhet --> "*" Uriorcurie : laerling
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Virksomhet : organisasjonsnavn
        
          
    
        
        
        Virksomhet --> "0..1" String : organisasjonsnavn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Virksomhet : organisasjonsnummer
        
          
    
        
        
        Virksomhet --> "0..1" Identifikator : organisasjonsnummer
        click Identifikator href "../Identifikator/"
    

        
      Virksomhet : postadresse
        
          
    
        
        
        Virksomhet --> "0..1" Adresse : postadresse
        click Adresse href "../Adresse/"
    

        
      Virksomhet : virksomhetsId
        
          
    
        
        
        Virksomhet --> "1" Identifikator : virksomhetsId
        click Identifikator href "../Identifikator/"
    

        
      
```





## Inheritance
* [Aktoer](aktoer.md)
    * [Enhet](enhet.md)
        * **Virksomhet**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Virksomhet](https://schema.fintlabs.no/Virksomhet) |


## Eigenskapar







  
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [virksomhetsId](virksomhetsid.md) | 1 <br/> [Identifikator](identifikator.md) | Intern unik identifikator i økonomisystemet |





  
  

  
  

  
  





  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [laerling](laerling.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Referanse til Laerling (Utdanning) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [forretningsadresse](forretningsadresse.md) | 0..1 <br/> [Adresse](adresse.md) | Besøksadresse til ein organisasjonseining | [Enhet](enhet.md) |
| [organisasjonsnavn](organisasjonsnavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på eining registrert i Einingsregisteret | [Enhet](enhet.md) |
| [organisasjonsnummer](organisasjonsnummer.md) | 0..1 <br/> [Identifikator](identifikator.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret | [Enhet](enhet.md) |
| [kontaktinformasjon](kontaktinformasjon.md) | 0..1 <br/> [Kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør | [Aktoer](aktoer.md) |
| [postadresse](postadresse.md) | 0..1 <br/> [Adresse](adresse.md) | Informasjon om postadresse til ein aktør | [Aktoer](aktoer.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Virksomhet |
| native | https://schema.fintlabs.no/:Virksomhet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Virksomhet
description: Ein juridisk organisasjon som produserer varer eller tenester.
from_schema: https://data.norge.no/fint/fint-common
is_a: Enhet
slots:
- id
- virksomhetsId
- laerling
slot_usage:
  virksomhetsId:
    name: virksomhetsId
    in_subset:
    - Obligatorisk
    required: true
  laerling:
    name: laerling
    in_subset:
    - Valgfri
class_uri: fint:Virksomhet

```
</details>

### Induced

<details>
```yaml
name: Virksomhet
description: Ein juridisk organisasjon som produserer varer eller tenester.
from_schema: https://data.norge.no/fint/fint-common
is_a: Enhet
slot_usage:
  virksomhetsId:
    name: virksomhetsId
    in_subset:
    - Obligatorisk
    required: true
  laerling:
    name: laerling
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/fint/fint-common
    identifier: true
    owner: Virksomhet
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
  virksomhetsId:
    name: virksomhetsId
    description: Intern unik identifikator i økonomisystemet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:virksomhetsId
    owner: Virksomhet
    domain_of:
    - Virksomhet
    range: Identifikator
    required: true
    inlined: true
  laerling:
    name: laerling
    description: Referanse til Laerling (Utdanning).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:laerling
    owner: Virksomhet
    domain_of:
    - Person
    - Virksomhet
    range: uriorcurie
    multivalued: true
  forretningsadresse:
    name: forretningsadresse
    description: Besøksadresse til ein organisasjonseining.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:forretningsadresse
    owner: Virksomhet
    domain_of:
    - Enhet
    range: Adresse
    inlined: true
  organisasjonsnavn:
    name: organisasjonsnavn
    description: Namn på eining registrert i Einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:organisasjonsnavn
    owner: Virksomhet
    domain_of:
    - Enhet
    - SoeknadDrosjeloeyve
    range: string
  organisasjonsnummer:
    name: organisasjonsnummer
    description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:organisasjonsnummer
    owner: Virksomhet
    domain_of:
    - Enhet
    range: Identifikator
    inlined: true
  kontaktinformasjon:
    name: kontaktinformasjon
    description: Den føretrekte måten å kome i kontakt med ein aktør.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:kontaktinformasjon
    owner: Virksomhet
    domain_of:
    - Aktoer
    - Kontaktperson
    - Korrespondansepart
    - Part
    range: Kontaktinformasjon
    inlined: true
  postadresse:
    name: postadresse
    description: Informasjon om postadresse til ein aktør.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:postadresse
    owner: Virksomhet
    domain_of:
    - Aktoer
    range: Adresse
    inlined: true
class_uri: fint:Virksomhet

```
</details>