

# Class: Motivasjon 


_Motivasjonen bak ein kvalitetsmerknad (Web Annotation)._





URI: [oa:Motivation](http://www.w3.org/ns/oa#Motivation)





```mermaid
 classDiagram
    class Motivasjon
    click Motivasjon href "../Motivasjon/"
      Motivasjon : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [oa:Motivation](http://www.w3.org/ns/oa#Motivation) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:Motivation |
| native | https://data.norge.no/linkml/dqv-ap-no/Motivasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Motivasjon
description: Motivasjonen bak ein kvalitetsmerknad (Web Annotation).
from_schema: https://data.norge.no/linkml/dqv-ap-no
slots:
- id
class_uri: oa:Motivation

```
</details>

### Induced

<details>
```yaml
name: Motivasjon
description: Motivasjonen bak ein kvalitetsmerknad (Web Annotation).
from_schema: https://data.norge.no/linkml/dqv-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Motivasjon
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
class_uri: oa:Motivation

```
</details>