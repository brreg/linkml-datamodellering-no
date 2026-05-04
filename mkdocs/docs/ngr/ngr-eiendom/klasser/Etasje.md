

# Class: Etasje 


_Ei etasje i ein bygning._





URI: [ngre:Etasje](https://data.norge.no/vocabulary/ngr-eiendom#Etasje)





```mermaid
 classDiagram
    class Etasje
    click Etasje href "../Etasje/"
      Etasje : etasjenummer
        
      Etasje : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Etasje](https://data.norge.no/vocabulary/ngr-eiendom#Etasje) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [etasjenummer](etasjenummer.md) | 1 <br/> [Integer](Integer.md) | Etasjenummer (t |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | [etasjer](etasjer.md) | range | [Etasje](Etasje.md) |
| [Bygning](Bygning.md) | [har_etasje](har_etasje.md) | range | [Etasje](Etasje.md) |
| [Bruksenhet](Bruksenhet.md) | [ligger_i_etasje](ligger_i_etasje.md) | range | [Etasje](Etasje.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Etasje |
| native | https://data.norge.no/linkml/ngr-eiendom/Etasje |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Etasje
description: Ei etasje i ein bygning.
from_schema: https://data.norge.no/linkml/ngr-eiendom
slots:
- id
- etasjenummer
slot_usage:
  etasjenummer:
    name: etasjenummer
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Etasje

```
</details>

### Induced

<details>
```yaml
name: Etasje
description: Ei etasje i ein bygning.
from_schema: https://data.norge.no/linkml/ngr-eiendom
slot_usage:
  etasjenummer:
    name: etasjenummer
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: Etasje
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
  etasjenummer:
    name: etasjenummer
    description: Etasjenummer (t.d. 2 for 2. etasje).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:etasjenummer
    alias: etasjenummer
    owner: Etasje
    domain_of:
    - Bruksenhetsnummer
    - Etasje
    range: integer
    required: true
class_uri: ngre:Etasje

```
</details>