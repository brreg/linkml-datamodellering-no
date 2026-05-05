

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
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [String](string.md) | Beskriven namn på perioden |
| [start](start.md) | 1 <br/> [Datetime](datetime.md) | Frå tidspunkt |
| [slutt](slutt.md) | 0..1 <br/> [Datetime](datetime.md) | Til tidspunkt |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Samtykke](samtykke.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Personopplysning](personopplysning.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Begrep](begrep.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Identifikator](identifikator.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Landkode](landkode.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Kjonn](kjonn.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Fylke](fylke.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Kommune](kommune.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |
| [Spraak](spraak.md) | [gyldighetsperiode](gyldighetsperiode.md) | range | [Periode](periode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Periode |
| native | https://schema.fintlabs.no/personvern/:Periode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Periode
description: Tidsperiode med obligatorisk start og valfri slutt.
from_schema: https://data.norge.no/linkml/fint-personvern
attributes:
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn på perioden.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:beskrivelse
    domain_of:
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
from_schema: https://data.norge.no/linkml/fint-personvern
attributes:
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn på perioden.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:beskrivelse
    alias: beskrivelse
    owner: Periode
    domain_of:
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