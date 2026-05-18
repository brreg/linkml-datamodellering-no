

# Class: Adresseomrade 


_Geografisk område eit adressenavn høyrer til, t.d. ei gate, eit veg eller eit stadnamn._





URI: [ngr:Adresseomrade](https://data.norge.no/vocabulary/ngr-adresse#Adresseomrade)





```mermaid
 classDiagram
    class Adresseomrade
    click Adresseomrade href "../Adresseomrade/"
      Adresseomrade : id
        
          
    
        
        
        Adresseomrade --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Adresseomrade : namn
        
          
    
        
        
        Adresseomrade --> "0..1" String : namn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Adresseomrade](https://data.norge.no/vocabulary/ngr-adresse#Adresseomrade) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [namn](namn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på det geografiske området eller adressekomponenten |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | [adresseomrader](adresseomrader.md) | range | [Adresseomrade](adresseomrade.md) |
| [Adressenavn](adressenavn.md) | [adresseomrade_ref](adresseomrade_ref.md) | range | [Adresseomrade](adresseomrade.md) |
| [Adressekode](adressekode.md) | [adresseomrade_ref](adresseomrade_ref.md) | range | [Adresseomrade](adresseomrade.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Adresseomrade |
| native | https://data.norge.no/linkml/ngr-adresse/Adresseomrade |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Adresseomrade
description: Geografisk område eit adressenavn høyrer til, t.d. ei gate, eit veg eller
  eit stadnamn.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slots:
- id
- namn
class_uri: ngr:Adresseomrade

```
</details>

### Induced

<details>
```yaml
name: Adresseomrade
description: Geografisk område eit adressenavn høyrer til, t.d. ei gate, eit veg eller
  eit stadnamn.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: Adresseomrade
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
  namn:
    name: namn
    description: Namn på det geografiske området eller adressekomponenten.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:namn
    alias: namn
    owner: Adresseomrade
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Adresseomrade

```
</details>