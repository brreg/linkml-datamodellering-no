

# Class: Kontostreng 


_Kontodimensjonar for ei postering (kompleks datatype)._





URI: [okn:Kontostreng](https://schema.fintlabs.no/okonomi/Kontostreng)





```mermaid
 classDiagram
    class Kontostreng
    click Kontostreng href "../Kontostreng/"
      Kontostreng : ansvar
        
      Kontostreng : art
        
      Kontostreng : funksjon
        
      Kontostreng : prosjekt
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [okn:Kontostreng](https://schema.fintlabs.no/okonomi/Kontostreng) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [art](art.md) | 0..1 <br/> [String](String.md) | Artskonto (type utgift/inntekt) |
| [funksjon](funksjon.md) | 0..1 <br/> [String](String.md) | Funksjonskode (KOSTRA) |
| [ansvar](ansvar.md) | 0..1 <br/> [String](String.md) | Ansvarsomrade |
| [prosjekt](prosjekt.md) | 0..1 <br/> [String](String.md) | Prosjektkode |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Postering](Postering.md) | [kontering](kontering.md) | range | [Kontostreng](Kontostreng.md) |
| [Vare](Vare.md) | [kontering](kontering.md) | range | [Kontostreng](Kontostreng.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:Kontostreng |
| native | https://schema.fintlabs.no/okonomi/:Kontostreng |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kontostreng
description: Kontodimensjonar for ei postering (kompleks datatype).
from_schema: https://data.norge.no/linkml/fint-okonomi
attributes:
  art:
    name: art
    description: Artskonto (type utgift/inntekt).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:art
    domain_of:
    - Kontostreng
    range: string
  funksjon:
    name: funksjon
    description: Funksjonskode (KOSTRA).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:funksjon
    domain_of:
    - Kontostreng
    range: string
  ansvar:
    name: ansvar
    description: Ansvarsomrade.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:ansvar
    domain_of:
    - Kontostreng
    range: string
  prosjekt:
    name: prosjekt
    description: Prosjektkode.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:prosjekt
    domain_of:
    - Kontostreng
    range: string
class_uri: okn:Kontostreng

```
</details>

### Induced

<details>
```yaml
name: Kontostreng
description: Kontodimensjonar for ei postering (kompleks datatype).
from_schema: https://data.norge.no/linkml/fint-okonomi
attributes:
  art:
    name: art
    description: Artskonto (type utgift/inntekt).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:art
    alias: art
    owner: Kontostreng
    domain_of:
    - Kontostreng
    range: string
  funksjon:
    name: funksjon
    description: Funksjonskode (KOSTRA).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:funksjon
    alias: funksjon
    owner: Kontostreng
    domain_of:
    - Kontostreng
    range: string
  ansvar:
    name: ansvar
    description: Ansvarsomrade.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:ansvar
    alias: ansvar
    owner: Kontostreng
    domain_of:
    - Kontostreng
    range: string
  prosjekt:
    name: prosjekt
    description: Prosjektkode.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:prosjekt
    alias: prosjekt
    owner: Kontostreng
    domain_of:
    - Kontostreng
    range: string
class_uri: okn:Kontostreng

```
</details>