

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
| [identifikatorverdi](identifikatorverdi.md) | 1 <br/> [String](string.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [gyldighetsperiode](gyldighetsperiode.md) | 0..1 <br/> [Periode](periode.md) | Perioden ein gjeven identifikator er gyldig |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
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
| [Enhet](enhet.md) | [organisasjonsnummer](organisasjonsnummer.md) | range | [Identifikator](identifikator.md) |
| [Valuta](valuta.md) | [bokstavkode](bokstavkode.md) | range | [Identifikator](identifikator.md) |
| [Valuta](valuta.md) | [nummerkode](nummerkode.md) | range | [Identifikator](identifikator.md) |
| [Person](person.md) | [fodselsnummer](fodselsnummer.md) | range | [Identifikator](identifikator.md) |
| [Virksomhet](virksomhet.md) | [virksomhetsId](virksomhetsid.md) | range | [Identifikator](identifikator.md) |
| [Virksomhet](virksomhet.md) | [organisasjonsnummer](organisasjonsnummer.md) | range | [Identifikator](identifikator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Identifikator |
| native | https://schema.fintlabs.no/arkiv/:Identifikator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Identifikator
description: Unik identifikasjon til eit objekt.
from_schema: https://data.norge.no/linkml/fint-arkiv
attributes:
  identifikatorverdi:
    name: identifikatorverdi
    description: Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein
      bestemt identifikator.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:identifikatorverdi
    domain_of:
    - Identifikator
    range: string
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Perioden ein gjeven identifikator er gyldig.
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:gyldighetsperiode
    domain_of:
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
    - Begrep
    - Identifikator
    range: Periode
    inlined: true
class_uri: fint:Identifikator

```
</details>

### Induced

<details>
```yaml
name: Identifikator
description: Unik identifikasjon til eit objekt.
from_schema: https://data.norge.no/linkml/fint-arkiv
attributes:
  identifikatorverdi:
    name: identifikatorverdi
    description: Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein
      bestemt identifikator.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:identifikatorverdi
    alias: identifikatorverdi
    owner: Identifikator
    domain_of:
    - Identifikator
    range: string
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Perioden ein gjeven identifikator er gyldig.
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:gyldighetsperiode
    alias: gyldighetsperiode
    owner: Identifikator
    domain_of:
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
    - Begrep
    - Identifikator
    range: Periode
    inlined: true
class_uri: fint:Identifikator

```
</details>