

# Class: Adresseomrade 


_Geografisk område eit adressenavn høyrer til, t.d. ei gate, eit veg eller eit stadnamn._





URI: [ngr:Adresseomrade](https://data.norge.no/vocabulary/ngr-adresse#Adresseomrade)





```mermaid
 classDiagram
    class Adresseomrade
    click Adresseomrade href "../Adresseomrade/"
      Adresseomrade : id
        
      Adresseomrade : namn
        
      
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
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |
| [namn](namn.md) | 0..1 <br/> [String](String.md) | Namn på det geografiske området eller adressekomponenten |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | [adresseomrader](adresseomrader.md) | range | [Adresseomrade](Adresseomrade.md) |
| [Adressenavn](Adressenavn.md) | [adresseomrade_ref](adresseomrade_ref.md) | range | [Adresseomrade](Adresseomrade.md) |
| [Adressekode](Adressekode.md) | [adresseomrade_ref](adresseomrade_ref.md) | range | [Adresseomrade](Adresseomrade.md) |












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