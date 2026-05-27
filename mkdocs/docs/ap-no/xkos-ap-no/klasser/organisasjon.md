

# Class: Organisasjon 


_Ein organisasjon eller aktør (foaf:Agent)._





URI: [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)





```mermaid
 classDiagram
    class Organisasjon
    click Organisasjon href "../Organisasjon/"
      Organisasjon : id
        
          
    
        
        
        Organisasjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
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
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Klassifikasjon](klassifikasjon.md) | [utgjevar](utgjevar.md) | range | [Organisasjon](organisasjon.md) |
| [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md) | [utgjevar](utgjevar.md) | range | [Organisasjon](organisasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Agent |
| native | https://data.norge.no/ap-no/xkos-ap-no/Organisasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organisasjon
description: Ein organisasjon eller aktør (foaf:Agent).
from_schema: https://data.norge.no/ap-no/xkos-ap-no
rank: 1000
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
from_schema: https://data.norge.no/ap-no/xkos-ap-no
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Organisasjon
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Klassifikasjon
    - Klassifikasjonsnivaa
    - Kategori
    - Klassifikasjonssamanlikning
    - Kategorisamanlikning
    - Organisasjon
    - Tidsrom
    range: uriorcurie
    required: true
class_uri: foaf:Agent

```
</details>