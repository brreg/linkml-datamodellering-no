

# Class: Bygning 


_Referanse til ein bygning i Matrikkelen. Offisiell adresse kan adressere ytre inngang(ar) til bygningen._





URI: [ngr:Bygning](https://data.norge.no/vocabulary/ngr-adresse#Bygning)





```mermaid
 classDiagram
    class Bygning
    click Bygning href "../Bygning/"
      Bygning : id
        
          
    
        
        
        Bygning --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Bygning](https://data.norge.no/vocabulary/ngr-adresse#Bygning) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | [bygningar](bygningar.md) | range | [Bygning](bygning.md) |
| [OffisiellAdresse](offisielladresse.md) | [adresserer_bygning](adresserer_bygning.md) | range | [Bygning](bygning.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Bygning |
| native | https://data.norge.no/ngr/ngr-adresse/Bygning |




## Examples
### Example: Bygning-12345

```yaml
id: https://example.org/bygning/12345

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bygning
description: Referanse til ein bygning i Matrikkelen. Offisiell adresse kan adressere
  ytre inngang(ar) til bygningen.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slots:
- id
class_uri: ngr:Bygning

```
</details>

### Induced

<details>
```yaml
name: Bygning
description: Referanse til ein bygning i Matrikkelen. Offisiell adresse kan adressere
  ytre inngang(ar) til bygningen.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-adresse
    rank: 1000
    identifier: true
    owner: Bygning
    domain_of:
    - GeografiskAdresse
    - Adressenavn
    - Adresseomrade
    - Adressekode
    - Husnummer
    - Bruksenhetsnummer
    - Representasjonspunkt
    - GeografiskOmrade
    - Postboks
    - Bygning
    - Bruksenhet
    range: uriorcurie
    required: true
class_uri: ngr:Bygning

```
</details>