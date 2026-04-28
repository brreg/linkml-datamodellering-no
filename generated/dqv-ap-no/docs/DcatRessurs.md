

# Class: DcatRessurs 


_Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget)._





URI: [dcat:Resource](http://www.w3.org/ns/dcat#Resource)





```mermaid
 classDiagram
    class DcatRessurs
    click DcatRessurs href "../DcatRessurs/"
      DcatRessurs : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Resource](http://www.w3.org/ns/dcat#Resource) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Kvalitetsmerknad](Kvalitetsmerknad.md) | [har_maal](har_maal.md) | range | [DcatRessurs](DcatRessurs.md) |
| [Brukartilbakemelding](Brukartilbakemelding.md) | [har_maal](har_maal.md) | range | [DcatRessurs](DcatRessurs.md) |
| [Kvalitetssertifikat](Kvalitetssertifikat.md) | [har_maal](har_maal.md) | range | [DcatRessurs](DcatRessurs.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Resource |
| native | https://data.norge.no/linkml/dqv-ap-no/DcatRessurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DcatRessurs
description: Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget).
from_schema: https://data.norge.no/linkml/dqv-ap-no
slots:
- id
class_uri: dcat:Resource

```
</details>

### Induced

<details>
```yaml
name: DcatRessurs
description: Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget).
from_schema: https://data.norge.no/linkml/dqv-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: DcatRessurs
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
class_uri: dcat:Resource

```
</details>