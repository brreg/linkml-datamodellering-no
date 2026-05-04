

# Class: Fakturalinje 


_Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype)._





URI: [okn:Fakturalinje](https://schema.fintlabs.no/okonomi/Fakturalinje)





```mermaid
 classDiagram
    class Fakturalinje
    click Fakturalinje href "../Fakturalinje/"
      Fakturalinje : antall
        
      Fakturalinje : fritekst
        
      Fakturalinje : pris
        
      Fakturalinje : vare
        
          
    
        
        
        Fakturalinje --> "1" Vare : vare
        click Vare href "../Vare/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [okn:Fakturalinje](https://schema.fintlabs.no/okonomi/Fakturalinje) |


## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [antall](antall.md) | 1 <br/> [Float](Float.md) | Mengd av varen levert |
| [pris](pris.md) | 1 <br/> [Integer](Integer.md) | Pris per eining levert, i øre |
| [fritekst](fritekst.md) | * <br/> [String](String.md) | Fritekst som skildrar varen slik han er levert |
| [vare](vare.md) | 1 <br/> [Vare](Vare.md) | Vare i vareregisteret |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Fakturagrunnlag](Fakturagrunnlag.md) | [fakturalinjer](fakturalinjer.md) | range | [Fakturalinje](Fakturalinje.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:Fakturalinje |
| native | https://schema.fintlabs.no/okonomi/:Fakturalinje |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Fakturalinje
description: Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype).
from_schema: https://data.norge.no/linkml/fint-okonomi
attributes:
  antall:
    name: antall
    description: Mengd av varen levert.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:antall
    domain_of:
    - Fakturalinje
    range: float
    required: true
  pris:
    name: pris
    description: Pris per eining levert, i øre.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:pris
    domain_of:
    - Fakturalinje
    - Vare
    range: integer
    required: true
  fritekst:
    name: fritekst
    description: Fritekst som skildrar varen slik han er levert.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:fritekst
    domain_of:
    - Fakturalinje
    range: string
    multivalued: true
  vare:
    name: vare
    description: Vare i vareregisteret.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-okonomi
    slot_uri: okn:vare
    domain_of:
    - Fakturautsteder
    - Fakturalinje
    range: Vare
    required: true
class_uri: okn:Fakturalinje

```
</details>

### Induced

<details>
```yaml
name: Fakturalinje
description: Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype).
from_schema: https://data.norge.no/linkml/fint-okonomi
attributes:
  antall:
    name: antall
    description: Mengd av varen levert.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:antall
    alias: antall
    owner: Fakturalinje
    domain_of:
    - Fakturalinje
    range: float
    required: true
  pris:
    name: pris
    description: Pris per eining levert, i øre.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:pris
    alias: pris
    owner: Fakturalinje
    domain_of:
    - Fakturalinje
    - Vare
    range: integer
    required: true
  fritekst:
    name: fritekst
    description: Fritekst som skildrar varen slik han er levert.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-okonomi
    rank: 1000
    slot_uri: okn:fritekst
    alias: fritekst
    owner: Fakturalinje
    domain_of:
    - Fakturalinje
    range: string
    multivalued: true
  vare:
    name: vare
    description: Vare i vareregisteret.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-okonomi
    slot_uri: okn:vare
    alias: vare
    owner: Fakturalinje
    domain_of:
    - Fakturautsteder
    - Fakturalinje
    range: Vare
    required: true
class_uri: okn:Fakturalinje

```
</details>