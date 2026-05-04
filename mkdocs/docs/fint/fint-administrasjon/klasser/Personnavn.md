

# Class: Personnavn 


_Namn på ein person._





URI: [fint:Personnavn](https://schema.fintlabs.no/Personnavn)





```mermaid
 classDiagram
    class Personnavn
    click Personnavn href "../Personnavn/"
      Personnavn : etternavn
        
      Personnavn : fornavn
        
      Personnavn : mellomnavn
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [fint:Personnavn](https://schema.fintlabs.no/Personnavn) |


## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [fornavn](fornavn.md) | 1 <br/> [String](String.md) | Fornamn til personen |
| [mellomnavn](mellomnavn.md) | 0..1 <br/> [String](String.md) | Mellomnamn |
| [etternavn](etternavn.md) | 1 <br/> [String](String.md) | Etternamn til personen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [navn](navn.md) | range | [Personnavn](Personnavn.md) |
| [Kontaktperson](Kontaktperson.md) | [navn](navn.md) | range | [Personnavn](Personnavn.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:Personnavn |
| native | https://schema.fintlabs.no/administrasjon/:Personnavn |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Personnavn
description: Namn på ein person.
from_schema: https://data.norge.no/linkml/fint-administrasjon
attributes:
  fornavn:
    name: fornavn
    description: Fornamn til personen.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:fornavn
    domain_of:
    - Personnavn
    range: string
    required: true
  mellomnavn:
    name: mellomnavn
    description: Mellomnamn.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:mellomnavn
    domain_of:
    - Personnavn
    range: string
  etternavn:
    name: etternavn
    description: Etternamn til personen.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:etternavn
    domain_of:
    - Personnavn
    range: string
    required: true
class_uri: fint:Personnavn

```
</details>

### Induced

<details>
```yaml
name: Personnavn
description: Namn på ein person.
from_schema: https://data.norge.no/linkml/fint-administrasjon
attributes:
  fornavn:
    name: fornavn
    description: Fornamn til personen.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:fornavn
    alias: fornavn
    owner: Personnavn
    domain_of:
    - Personnavn
    range: string
    required: true
  mellomnavn:
    name: mellomnavn
    description: Mellomnamn.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:mellomnavn
    alias: mellomnavn
    owner: Personnavn
    domain_of:
    - Personnavn
    range: string
  etternavn:
    name: etternavn
    description: Etternamn til personen.
    from_schema: https://data.norge.no/linkml/fint-common
    rank: 1000
    slot_uri: fint:etternavn
    alias: etternavn
    owner: Personnavn
    domain_of:
    - Personnavn
    range: string
    required: true
class_uri: fint:Personnavn

```
</details>