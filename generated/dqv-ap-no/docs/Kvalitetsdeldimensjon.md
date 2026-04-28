

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
        
      Kvalitetsdeldimensjon : har_definisjon
        
      Kvalitetsdeldimensjon : id
        
      
```





## Inheritance
* [Kvalitetsdimensjon](Kvalitetsdimensjon.md)
    * **Kvalitetsdeldimensjon**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqvno:SubDimension](https://data.norge.no/vocabulary/dqvno#SubDimension) |


## Eigenskapar







  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_deldimensjon_av](er_deldimensjon_av.md) | 1 <br/> [Kvalitetsdimensjon](Kvalitetsdimensjon.md) | Overordna kvalitetsdimensjon denne deldimensjonen høyrer til |





  
  





  
  






  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [har_anbefalt_term](har_anbefalt_term.md) | * <br/> [LangString](LangString.md) | Føretrekt term/namn for dimensjonen eller målet | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |
| [har_definisjon](har_definisjon.md) | * <br/> [LangString](LangString.md) | Definisjon av dimensjonen eller målet | [Kvalitetsdimensjon](Kvalitetsdimensjon.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [kvalitetsdeldimensjonar](kvalitetsdeldimensjonar.md) | range | [Kvalitetsdeldimensjon](Kvalitetsdeldimensjon.md) |
| [Kvalitetsmaal](Kvalitetsmaal.md) | [er_i_kvalitetsdeldimensjon](er_i_kvalitetsdeldimensjon.md) | range | [Kvalitetsdeldimensjon](Kvalitetsdeldimensjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqvno:SubDimension |
| native | https://data.norge.no/linkml/dqv-ap-no/Kvalitetsdeldimensjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsdeldimensjon
description: Ein deldimensjon av ein kvalitetsdimensjon.
from_schema: https://data.norge.no/linkml/dqv-ap-no
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
from_schema: https://data.norge.no/linkml/dqv-ap-no
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
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: skos:broader
    alias: er_deldimensjon_av
    owner: Kvalitetsdeldimensjon
    domain_of:
    - Kvalitetsdeldimensjon
    range: Kvalitetsdimensjon
    required: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Kvalitetsdeldimensjon
    domain_of:
    - DcatRessurs
    - Datasett
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - Motivasjon
    - Spraak
    - Mediatype
    - Begrep
    - Begrepssamling
    range: uriorcurie
    required: true
  har_anbefalt_term:
    name: har_anbefalt_term
    description: Føretrekt term/namn for dimensjonen eller målet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: skos:prefLabel
    alias: har_anbefalt_term
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
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    slot_uri: skos:definition
    alias: har_definisjon
    owner: Kvalitetsdeldimensjon
    domain_of:
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    range: LangString
    multivalued: true
class_uri: dqvno:SubDimension

```
</details>