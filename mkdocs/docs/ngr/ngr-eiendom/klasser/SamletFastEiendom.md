

# Class: SamletFastEiendom 


_Samling av to eller fleire faste eigedommar som er organiserte saman. Lite brukt i praksis i dag._





URI: [ngre:SamletFastEiendom](https://data.norge.no/vocabulary/ngr-eiendom#SamletFastEiendom)





```mermaid
 classDiagram
    class SamletFastEiendom
    click SamletFastEiendom href "../SamletFastEiendom/"
      SamletFastEiendom : bestar_av_fast_eiendom
        
          
    
        
        
        SamletFastEiendom --> "1..*" FastEiendom : bestar_av_fast_eiendom
        click FastEiendom href "../FastEiendom/"
    

        
      SamletFastEiendom : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:SamletFastEiendom](https://data.norge.no/vocabulary/ngr-eiendom#SamletFastEiendom) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [bestar_av_fast_eiendom](bestar_av_fast_eiendom.md) | 1..* <br/> [FastEiendom](FastEiendom.md) | Faste eigedommar som inngår i samlinga (minimum 2) |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | [samlinger](samlinger.md) | range | [SamletFastEiendom](SamletFastEiendom.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:SamletFastEiendom |
| native | https://data.norge.no/linkml/ngr-eiendom/SamletFastEiendom |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SamletFastEiendom
description: Samling av to eller fleire faste eigedommar som er organiserte saman.
  Lite brukt i praksis i dag.
from_schema: https://data.norge.no/linkml/ngr-eiendom
slots:
- id
- bestar_av_fast_eiendom
slot_usage:
  bestar_av_fast_eiendom:
    name: bestar_av_fast_eiendom
    in_subset:
    - Obligatorisk
    required: true
    minimum_cardinality: 2
class_uri: ngre:SamletFastEiendom

```
</details>

### Induced

<details>
```yaml
name: SamletFastEiendom
description: Samling av to eller fleire faste eigedommar som er organiserte saman.
  Lite brukt i praksis i dag.
from_schema: https://data.norge.no/linkml/ngr-eiendom
slot_usage:
  bestar_av_fast_eiendom:
    name: bestar_av_fast_eiendom
    in_subset:
    - Obligatorisk
    required: true
    minimum_cardinality: 2
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: SamletFastEiendom
    domain_of:
    - FastEiendom
    - SamletFastEiendom
    - Borettslagsandel
    - Matrikkelenhet
    - Matrikkelnummer
    - Kommunenummer
    - Gaardsnummer
    - Bruksnummer
    - Festenummer
    - Seksjonsnummer
    - Bygning
    - Bygningsnummer
    - Representasjonspunkt
    - YtreInngang
    - Bruksenhet
    - Bruksenhetsnummer
    - Etasje
    - Teig
    - Anleggsprojeksjonsflate
    - Eierforhold
    - Hjemmel
    - Andel
    - Rettighetshaver
    - TinglystHeftelse
    - RettighetForAaBenytteEiendom
    - Borettslag
    - OffisiellAdresse
    - Person
    - Hovedenhet
    - Kommune
    range: uriorcurie
    required: true
  bestar_av_fast_eiendom:
    name: bestar_av_fast_eiendom
    description: Faste eigedommar som inngår i samlinga (minimum 2).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:bestarAvFastEiendom
    alias: bestar_av_fast_eiendom
    owner: SamletFastEiendom
    domain_of:
    - SamletFastEiendom
    range: FastEiendom
    required: true
    multivalued: true
    minimum_cardinality: 2
class_uri: ngre:SamletFastEiendom

```
</details>