

# Class: Bruksnummer 


_Bruksnummer innanfor gardsnamnet._





URI: [ngre:Bruksnummer](https://data.norge.no/vocabulary/ngr-eiendom#Bruksnummer)





```mermaid
 classDiagram
    class Bruksnummer
    click Bruksnummer href "../Bruksnummer/"
      Bruksnummer : bruksnummer_verdi
        
      Bruksnummer : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Bruksnummer](https://data.norge.no/vocabulary/ngr-eiendom#Bruksnummer) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [bruksnummer_verdi](bruksnummer_verdi.md) | 1 <br/> [Integer](Integer.md) | Bruksnummer innanfor gardsnamnet |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Matrikkelnummer](Matrikkelnummer.md) | [bestar_av_bruksnummer](bestar_av_bruksnummer.md) | range | [Bruksnummer](Bruksnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Bruksnummer |
| native | https://data.norge.no/linkml/ngr-eiendom/Bruksnummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bruksnummer
description: Bruksnummer innanfor gardsnamnet.
from_schema: https://data.norge.no/linkml/ngr-eiendom
slots:
- id
- bruksnummer_verdi
slot_usage:
  bruksnummer_verdi:
    name: bruksnummer_verdi
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngre:Bruksnummer

```
</details>

### Induced

<details>
```yaml
name: Bruksnummer
description: Bruksnummer innanfor gardsnamnet.
from_schema: https://data.norge.no/linkml/ngr-eiendom
slot_usage:
  bruksnummer_verdi:
    name: bruksnummer_verdi
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
    owner: Bruksnummer
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
  bruksnummer_verdi:
    name: bruksnummer_verdi
    description: Bruksnummer innanfor gardsnamnet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:bruksnummer
    alias: bruksnummer_verdi
    owner: Bruksnummer
    domain_of:
    - Bruksnummer
    range: integer
    required: true
class_uri: ngre:Bruksnummer

```
</details>