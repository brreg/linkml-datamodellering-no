

# Class: Organisasjon 


_Ein organisasjon eller aktør (foaf:Agent)._





URI: [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)





```mermaid
 classDiagram
    class Organisasjon
    click Organisasjon href "../Organisasjon/"
      Organisasjon : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [foaf:Agent](http://xmlns.com/foaf/0.1/Agent) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Klassifikasjon](Klassifikasjon.md) | [utgjevar](utgjevar.md) | range | [Organisasjon](Organisasjon.md) |
| [Klassifikasjonssamanlikning](Klassifikasjonssamanlikning.md) | [utgjevar](utgjevar.md) | range | [Organisasjon](Organisasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Agent |
| native | https://data.norge.no/linkml/xkos-ap-no/Organisasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organisasjon
description: Ein organisasjon eller aktør (foaf:Agent).
from_schema: https://data.norge.no/linkml/xkos-ap-no
slots:
- id
class_uri: foaf:Agent

```
</details>

### Induced

<details>
```yaml
name: Organisasjon
description: Ein organisasjon eller aktør (foaf:Agent).
from_schema: https://data.norge.no/linkml/xkos-ap-no
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Organisasjon
    domain_of:
    - Klassifikasjon
    - Klassifikasjonsnivaa
    - Kategori
    - Klassifikasjonssamanlikning
    - Kategorisamanlikning
    - Organisasjon
    - Tidsrom
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
class_uri: foaf:Agent

```
</details>