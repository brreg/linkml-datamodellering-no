

# Class: Identifikator 


_Unik identifikasjon til eit objekt._





URI: [fint:Identifikator](https://schema.fintlabs.no/Identifikator)





```mermaid
 classDiagram
    class Identifikator
    click Identifikator href "../Identifikator/"
      Identifikator : gyldighetsperiode
        
          
    
        
        
        Identifikator --> "0..1" Periode : gyldighetsperiode
        click Periode href "../Periode/"
    

        
      Identifikator : identifikatorverdi
        
          
    
        
        
        Identifikator --> "1" String : identifikatorverdi
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Identifikator](https://schema.fintlabs.no/Identifikator) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
    
      
    
      
    
      
    
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikatorverdi](identifikatorverdi.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [gyldighetsperiode](gyldighetsperiode.md) | 0..1 <br/> [Periode](periode.md) | Periode ressursen er gyldig for |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Elev](elev.md) | [elevnummer](elevnummer.md) | range | [Identifikator](identifikator.md) |
| [Enhet](enhet.md) | [organisasjonsnummer](organisasjonsnummer.md) | range | [Identifikator](identifikator.md) |
| [Valuta](valuta.md) | [bokstavkode](bokstavkode.md) | range | [Identifikator](identifikator.md) |
| [Valuta](valuta.md) | [nummerkode](nummerkode.md) | range | [Identifikator](identifikator.md) |
| [Person](person.md) | [fodselsnummer](fodselsnummer.md) | range | [Identifikator](identifikator.md) |
| [Virksomhet](virksomhet.md) | [virksomhetsId](virksomhetsid.md) | range | [Identifikator](identifikator.md) |
| [Virksomhet](virksomhet.md) | [organisasjonsnummer](organisasjonsnummer.md) | range | [Identifikator](identifikator.md) |
| [Mappe](mappe.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [Saksmappe](saksmappe.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [Arkivressurs](arkivressurs.md) | [kildesystemId](kildesystemid.md) | range | [Identifikator](identifikator.md) |
| [Sak](sak.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [Personalmappe](personalmappe.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | [soeknadsnummer](soeknadsnummer.md) | range | [Identifikator](identifikator.md) |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [TilskuddFartoy](tilskuddfartoy.md) | [soeknadsnummer](soeknadsnummer.md) | range | [Identifikator](identifikator.md) |
| [TilskuddFartoy](tilskuddfartoy.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | [soeknadsnummer](soeknadsnummer.md) | range | [Identifikator](identifikator.md) |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | [mappeId](mappeid.md) | range | [Identifikator](identifikator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Identifikator |
| native | https://schema.fintlabs.no/:Identifikator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Identifikator
description: Unik identifikasjon til eit objekt.
from_schema: https://data.norge.no/fint/fint-common
slots:
- identifikatorverdi
- gyldighetsperiode
slot_usage:
  identifikatorverdi:
    name: identifikatorverdi
    required: true
class_uri: fint:Identifikator

```
</details>

### Induced

<details>
```yaml
name: Identifikator
description: Unik identifikasjon til eit objekt.
from_schema: https://data.norge.no/fint/fint-common
slot_usage:
  identifikatorverdi:
    name: identifikatorverdi
    required: true
attributes:
  identifikatorverdi:
    name: identifikatorverdi
    description: Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein
      bestemt identifikator.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:identifikatorverdi
    owner: Identifikator
    domain_of:
    - Identifikator
    range: string
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Periode ressursen er gyldig for.
    from_schema: https://data.norge.no/fint/fint-common
    slot_uri: fint:gyldighetsperiode
    owner: Identifikator
    domain_of:
    - Begrep
    - Identifikator
    - AdministrativEnhet
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
    range: Periode
    inlined: true
class_uri: fint:Identifikator

```
</details>