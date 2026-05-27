

# Class: Kvalitetsdeldimensjon 


_Ein deldimensjon av ein kvalitetsdimensjon._





URI: [dqvno:SubDimension](https://data.norge.no/vocabulary/dqvno#SubDimension)





```mermaid
 classDiagram
    class Kvalitetsdeldimensjon
    click Kvalitetsdeldimensjon href "../Kvalitetsdeldimensjon/"
      Kvalitetsdimensjon <|-- Kvalitetsdeldimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
      
      Kvalitetsdeldimensjon : er_deldimensjon_av
        
          
    
        
        
        Kvalitetsdeldimensjon --> "1" Kvalitetsdimensjon : er_deldimensjon_av
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Kvalitetsdeldimensjon : har_anbefalt_term
        
          
    
        
        
        Kvalitetsdeldimensjon --> "*" LangString : har_anbefalt_term
        click LangString href "../LangString/"
    

        
      Kvalitetsdeldimensjon : har_definisjon
        
          
    
        
        
        Kvalitetsdeldimensjon --> "*" LangString : har_definisjon
        click LangString href "../LangString/"
    

        
      Kvalitetsdeldimensjon : id
        
          
    
        
        
        Kvalitetsdeldimensjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [Kvalitetsdimensjon](kvalitetsdimensjon.md)
    * **Kvalitetsdeldimensjon**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqvno:SubDimension](https://data.norge.no/vocabulary/dqvno#SubDimension) |


## Eigenskapar







  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_deldimensjon_av](er_deldimensjon_av.md) | 1 <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Overordna kvalitetsdimensjon denne deldimensjonen høyrer til |





  
  





  
  






  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| [har_anbefalt_term](har_anbefalt_term.md) | * <br/> [LangString](langstring.md) | Føretrekt term/namn for dimensjonen eller målet | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| [har_definisjon](har_definisjon.md) | * <br/> [LangString](langstring.md) | Definisjon av dimensjonen eller målet | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Kvalitetsmaal](kvalitetsmaal.md) | [er_i_kvalitetsdeldimensjon](er_i_kvalitetsdeldimensjon.md) | range | [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqvno:SubDimension |
| native | https://data.norge.no/ap-no/dqv-ap-no/Kvalitetsdeldimensjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsdeldimensjon
description: Ein deldimensjon av ein kvalitetsdimensjon.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
is_a: Kvalitetsdimensjon
slots:
- er_deldimensjon_av
slot_usage:
  er_deldimensjon_av:
    name: er_deldimensjon_av
    in_subset:
    - Obligatorisk
    required: true
  har_anbefalt_term:
    name: har_anbefalt_term
    in_subset:
    - Anbefalt
  har_definisjon:
    name: har_definisjon
    in_subset:
    - Anbefalt
class_uri: dqvno:SubDimension

```
</details>

### Induced

<details>
```yaml
name: Kvalitetsdeldimensjon
description: Ein deldimensjon av ein kvalitetsdimensjon.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
is_a: Kvalitetsdimensjon
slot_usage:
  er_deldimensjon_av:
    name: er_deldimensjon_av
    in_subset:
    - Obligatorisk
    required: true
  har_anbefalt_term:
    name: har_anbefalt_term
    in_subset:
    - Anbefalt
  har_definisjon:
    name: har_definisjon
    in_subset:
    - Anbefalt
attributes:
  er_deldimensjon_av:
    name: er_deldimensjon_av
    description: Overordna kvalitetsdimensjon denne deldimensjonen høyrer til.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    slot_uri: skos:broader
    owner: Kvalitetsdeldimensjon
    domain_of:
    - Kvalitetsdeldimensjon
    range: Kvalitetsdimensjon
    required: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Kvalitetsdeldimensjon
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    range: uriorcurie
    required: true
  har_anbefalt_term:
    name: har_anbefalt_term
    description: Føretrekt term/namn for dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    slot_uri: skos:prefLabel
    owner: Kvalitetsdeldimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
  har_definisjon:
    name: har_definisjon
    description: Definisjon av dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    slot_uri: skos:definition
    owner: Kvalitetsdeldimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
class_uri: dqvno:SubDimension

```
</details>