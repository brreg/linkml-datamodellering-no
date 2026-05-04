

# Class: PersonvernContainer 


_Rotcontainer for FINT Personvern-instansar._





URI: [https://schema.fintlabs.no/personvern/:PersonvernContainer](https://schema.fintlabs.no/personvern/:PersonvernContainer)





```mermaid
 classDiagram
    class PersonvernContainer
    click PersonvernContainer href "../PersonvernContainer/"
      PersonvernContainer : behandlingar
        
          
    
        
        
        PersonvernContainer --> "*" Behandling : behandlingar
        click Behandling href "../Behandling/"
    

        
      PersonvernContainer : behandlingsgrunnlag
        
          
    
        
        
        PersonvernContainer --> "*" Behandlingsgrunnlag : behandlingsgrunnlag
        click Behandlingsgrunnlag href "../Behandlingsgrunnlag/"
    

        
      PersonvernContainer : personopplysningar
        
          
    
        
        
        PersonvernContainer --> "*" Personopplysning : personopplysningar
        click Personopplysning href "../Personopplysning/"
    

        
      PersonvernContainer : samtykker
        
          
    
        
        
        PersonvernContainer --> "*" Samtykke : samtykker
        click Samtykke href "../Samtykke/"
    

        
      PersonvernContainer : tenester
        
          
    
        
        
        PersonvernContainer --> "*" Tjeneste : tenester
        click Tjeneste href "../Tjeneste/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Eigenskapar







  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [behandlingar](behandlingar.md) | * <br/> [Behandling](Behandling.md) |  |
| [samtykker](samtykker.md) | * <br/> [Samtykke](Samtykke.md) |  |
| [tenester](tenester.md) | * <br/> [Tjeneste](Tjeneste.md) |  |
| [behandlingsgrunnlag](behandlingsgrunnlag.md) | * <br/> [Behandlingsgrunnlag](Behandlingsgrunnlag.md) |  |
| [personopplysningar](personopplysningar.md) | * <br/> [Personopplysning](Personopplysning.md) |  |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:PersonvernContainer |
| native | https://schema.fintlabs.no/personvern/:PersonvernContainer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonvernContainer
description: Rotcontainer for FINT Personvern-instansar.
from_schema: https://data.norge.no/linkml/fint-personvern
attributes:
  behandlingar:
    name: behandlingar
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    domain_of:
    - PersonvernContainer
    range: Behandling
    multivalued: true
    inlined: true
    inlined_as_list: true
  samtykker:
    name: samtykker
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    domain_of:
    - PersonvernContainer
    range: Samtykke
    multivalued: true
    inlined: true
    inlined_as_list: true
  tenester:
    name: tenester
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    domain_of:
    - PersonvernContainer
    range: Tjeneste
    multivalued: true
    inlined: true
    inlined_as_list: true
  behandlingsgrunnlag:
    name: behandlingsgrunnlag
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    domain_of:
    - PersonvernContainer
    - Behandling
    range: Behandlingsgrunnlag
    multivalued: true
    inlined: true
    inlined_as_list: true
  personopplysningar:
    name: personopplysningar
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    domain_of:
    - PersonvernContainer
    range: Personopplysning
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: PersonvernContainer
description: Rotcontainer for FINT Personvern-instansar.
from_schema: https://data.norge.no/linkml/fint-personvern
attributes:
  behandlingar:
    name: behandlingar
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    alias: behandlingar
    owner: PersonvernContainer
    domain_of:
    - PersonvernContainer
    range: Behandling
    multivalued: true
    inlined_as_list: true
  samtykker:
    name: samtykker
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    alias: samtykker
    owner: PersonvernContainer
    domain_of:
    - PersonvernContainer
    range: Samtykke
    multivalued: true
    inlined_as_list: true
  tenester:
    name: tenester
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    alias: tenester
    owner: PersonvernContainer
    domain_of:
    - PersonvernContainer
    range: Tjeneste
    multivalued: true
    inlined_as_list: true
  behandlingsgrunnlag:
    name: behandlingsgrunnlag
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    alias: behandlingsgrunnlag
    owner: PersonvernContainer
    domain_of:
    - PersonvernContainer
    - Behandling
    range: Behandlingsgrunnlag
    multivalued: true
    inlined_as_list: true
  personopplysningar:
    name: personopplysningar
    from_schema: https://data.norge.no/linkml/fint-personvern
    rank: 1000
    alias: personopplysningar
    owner: PersonvernContainer
    domain_of:
    - PersonvernContainer
    range: Personopplysning
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>