

# Class: Periode 


_Tidsperiode med obligatorisk start og valfri slutt._





URI: [fint:Periode](https://schema.fintlabs.no/Periode)





```mermaid
 classDiagram
    class Periode
    click Periode href "../Periode/"
      Periode : beskrivelse
        
      Periode : slutt
        
      Periode : start
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Periode](https://schema.fintlabs.no/Periode) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [String](String.md) | Beskriven namn på perioden |
| [start](start.md) | 1 <br/> [Datetime](Datetime.md) | Frå tidspunkt |
| [slutt](slutt.md) | 0..1 <br/> [Datetime](Datetime.md) | Til tidspunkt |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdministrativEnhet](AdministrativEnhet.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [DokumentStatus](DokumentStatus.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [DokumentType](DokumentType.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Format](Format.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [JournalpostType](JournalpostType.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [JournalStatus](JournalStatus.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Klassifikasjonstype](Klassifikasjonstype.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [KorrespondansepartType](KorrespondansepartType.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Merknadstype](Merknadstype.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [PartRolle](PartRolle.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Rolle](Rolle.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Saksmappetype](Saksmappetype.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Saksstatus](Saksstatus.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Skjermingshjemmel](Skjermingshjemmel.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Tilgangsgruppe](Tilgangsgruppe.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Tilgangsrestriksjon](Tilgangsrestriksjon.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [TilknyttetRegistreringSom](TilknyttetRegistreringSom.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Variantformat](Variantformat.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Begrep](Begrep.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Identifikator](Identifikator.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Landkode](Landkode.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Kjonn](Kjonn.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Fylke](Fylke.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Kommune](Kommune.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |
| [Spraak](Spraak.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](Periode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Periode |
| native | https://schema.fintlabs.no/arkiv/:Periode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Periode
description: Tidsperiode med obligatorisk start og valfri slutt.
from_schema: https://data.norge.no/linkml/fint-arkiv
attributes:
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn på perioden.
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:beskrivelse
    domain_of:
    - Mappe
    - Registrering
    - Klassifikasjonssystem
    - Dokumentbeskrivelse
    - Periode
    range: string
  start:
    name: start
    description: Frå tidspunkt.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:start
    domain_of:
    - Periode
    range: datetime
    required: true
  slutt:
    name: slutt
    description: Til tidspunkt.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:slutt
    domain_of:
    - Periode
    range: datetime
class_uri: fint:Periode

```
</details>

### Induced

<details>
```yaml
name: Periode
description: Tidsperiode med obligatorisk start og valfri slutt.
from_schema: https://data.norge.no/linkml/fint-arkiv
attributes:
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn på perioden.
    from_schema: https://data.norge.no/linkml/fint-common
    slot_uri: fint:beskrivelse
    alias: beskrivelse
    owner: Periode
    domain_of:
    - Mappe
    - Registrering
    - Klassifikasjonssystem
    - Dokumentbeskrivelse
    - Periode
    range: string
  start:
    name: start
    description: Frå tidspunkt.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:start
    alias: start
    owner: Periode
    domain_of:
    - Periode
    range: datetime
    required: true
  slutt:
    name: slutt
    description: Til tidspunkt.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:slutt
    alias: slutt
    owner: Periode
    domain_of:
    - Periode
    range: datetime
class_uri: fint:Periode

```
</details>