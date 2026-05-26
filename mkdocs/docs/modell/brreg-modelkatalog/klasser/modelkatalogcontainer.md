

# Class: ModelkatalogContainer 



URI: [https://data.norge.no/linkml/brreg-modelkatalog/ModelkatalogContainer](https://data.norge.no/linkml/brreg-modelkatalog/ModelkatalogContainer)





```mermaid
 classDiagram
    class ModelkatalogContainer
    click ModelkatalogContainer href "../ModelkatalogContainer/"
      ModelkatalogContainer : aktorer
        
          
    
        
        
        ModelkatalogContainer --> "*" Aktor : aktorer
        click Aktor href "../Aktor/"
    

        
      ModelkatalogContainer : eigenskapar
        
          
    
        
        
        ModelkatalogContainer --> "*" Eigenskap : eigenskapar
        click Eigenskap href "../Eigenskap/"
    

        
      ModelkatalogContainer : informasjonsmodellar
        
          
    
        
        
        ModelkatalogContainer --> "*" Informasjonsmodell : informasjonsmodellar
        click Informasjonsmodell href "../Informasjonsmodell/"
    

        
      ModelkatalogContainer : kodelister
        
          
    
        
        
        ModelkatalogContainer --> "*" Kodeliste : kodelister
        click Kodeliste href "../Kodeliste/"
    

        
      ModelkatalogContainer : kontaktpunkt
        
          
    
        
        
        ModelkatalogContainer --> "*" Kontaktopplysning : kontaktpunkt
        click Kontaktopplysning href "../Kontaktopplysning/"
    

        
      ModelkatalogContainer : modelkatalogar
        
          
    
        
        
        ModelkatalogContainer --> "*" Modelkatalog : modelkatalogar
        click Modelkatalog href "../Modelkatalog/"
    

        
      ModelkatalogContainer : objekttypar
        
          
    
        
        
        ModelkatalogContainer --> "*" Objekttype : objekttypar
        click Objekttype href "../Objekttype/"
    

        
      
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
| [modelkatalogar](modelkatalogar.md) | * <br/> [Modelkatalog](modelkatalog.md) |  |
| [informasjonsmodellar](informasjonsmodellar.md) | * <br/> [Informasjonsmodell](informasjonsmodell.md) |  |
| [objekttypar](objekttypar.md) | * <br/> [Objekttype](objekttype.md) |  |
| [kodelister](kodelister.md) | * <br/> [Kodeliste](kodeliste.md) |  |
| [eigenskapar](eigenskapar.md) | * <br/> [Eigenskap](eigenskap.md) |  |
| [aktorer](aktorer.md) | * <br/> [Aktor](aktor.md) |  |
| [kontaktpunkt](kontaktpunkt.md) | * <br/> [Kontaktopplysning](kontaktopplysning.md) |  |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/brreg-modelkatalog




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/brreg-modelkatalog/ModelkatalogContainer |
| native | https://data.norge.no/linkml/brreg-modelkatalog/ModelkatalogContainer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelkatalogContainer
from_schema: https://data.norge.no/linkml/brreg-modelkatalog
rank: 1000
attributes:
  modelkatalogar:
    name: modelkatalogar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - ModelkatalogContainer
    range: Modelkatalog
    multivalued: true
    inlined: true
    inlined_as_list: true
  informasjonsmodellar:
    name: informasjonsmodellar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - ModelkatalogContainer
    range: Informasjonsmodell
    multivalued: true
    inlined: true
    inlined_as_list: true
  objekttypar:
    name: objekttypar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - ModelkatalogContainer
    range: Objekttype
    multivalued: true
    inlined: true
    inlined_as_list: true
  kodelister:
    name: kodelister
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - ModelkatalogContainer
    range: Kodeliste
    multivalued: true
    inlined: true
    inlined_as_list: true
  eigenskapar:
    name: eigenskapar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - ModelkatalogContainer
    range: Eigenskap
    multivalued: true
    inlined: true
    inlined_as_list: true
  aktorer:
    name: aktorer
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - ModelkatalogContainer
    range: Aktor
    multivalued: true
    inlined: true
    inlined_as_list: true
  kontaktpunkt:
    name: kontaktpunkt
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    domain_of:
    - Modelkatalog
    - Informasjonsmodell
    - ModelkatalogContainer
    range: Kontaktopplysning
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: ModelkatalogContainer
from_schema: https://data.norge.no/linkml/brreg-modelkatalog
rank: 1000
attributes:
  modelkatalogar:
    name: modelkatalogar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - ModelkatalogContainer
    range: Modelkatalog
    multivalued: true
    inlined: true
    inlined_as_list: true
  informasjonsmodellar:
    name: informasjonsmodellar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - ModelkatalogContainer
    range: Informasjonsmodell
    multivalued: true
    inlined: true
    inlined_as_list: true
  objekttypar:
    name: objekttypar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - ModelkatalogContainer
    range: Objekttype
    multivalued: true
    inlined: true
    inlined_as_list: true
  kodelister:
    name: kodelister
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - ModelkatalogContainer
    range: Kodeliste
    multivalued: true
    inlined: true
    inlined_as_list: true
  eigenskapar:
    name: eigenskapar
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - ModelkatalogContainer
    range: Eigenskap
    multivalued: true
    inlined: true
    inlined_as_list: true
  aktorer:
    name: aktorer
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - ModelkatalogContainer
    range: Aktor
    multivalued: true
    inlined: true
    inlined_as_list: true
  kontaktpunkt:
    name: kontaktpunkt
    from_schema: https://data.norge.no/linkml/brreg-modelkatalog
    rank: 1000
    owner: ModelkatalogContainer
    domain_of:
    - Modelkatalog
    - Informasjonsmodell
    - ModelkatalogContainer
    range: Kontaktopplysning
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>