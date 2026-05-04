

# Class: Begrepssamling 


_Ei SKOS-omgrepssamling (temavokabular)._





URI: [skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme)





```mermaid
 classDiagram
    class Begrepssamling
    click Begrepssamling href "../Begrepssamling/"
      Begrepssamling : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | [temaer](temaer.md) | range | [Begrepssamling](Begrepssamling.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:ConceptScheme |
| native | https://data.norge.no/linkml/modelldcat-ap-no/Begrepssamling |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Begrepssamling
description: Ei SKOS-omgrepssamling (temavokabular).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
slots:
- id
class_uri: skos:ConceptScheme

```
</details>

### Induced

<details>
```yaml
name: Begrepssamling
description: Ei SKOS-omgrepssamling (temavokabular).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/modelldcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Begrepssamling
    domain_of:
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Standard
    - Lisensdokument
    - Lokasjon
    - Tidsperiode
    - Dokument
    - Modelkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
class_uri: skos:ConceptScheme

```
</details>