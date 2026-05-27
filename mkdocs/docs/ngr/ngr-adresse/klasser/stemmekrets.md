

# Class: Stemmekrets 


_Ei stemmekrets brukt ved val._





URI: [ngr:Stemmekrets](https://data.norge.no/vocabulary/ngr-adresse#Stemmekrets)





```mermaid
 classDiagram
    class Stemmekrets
    click Stemmekrets href "../Stemmekrets/"
      GeografiskOmrade <|-- Stemmekrets
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      Stemmekrets : id
        
          
    
        
        
        Stemmekrets --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Stemmekrets : namn
        
          
    
        
        
        Stemmekrets --> "0..1" String : namn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Stemmekrets : stemmekretsnummer
        
          
    
        
        
        Stemmekrets --> "0..1" String : stemmekretsnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* [GeografiskOmrade](geografiskomrade.md)
    * **Stemmekrets**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Stemmekrets](https://data.norge.no/vocabulary/ngr-adresse#Stemmekrets) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [stemmekretsnummer](stemmekretsnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Stemmekretsnummer |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [GeografiskOmrade](geografiskomrade.md) |
| [namn](namn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](geografiskomrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | [stemmekretsar](stemmekretsar.md) | range | [Stemmekrets](stemmekrets.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Stemmekrets |
| native | https://data.norge.no/ngr/ngr-adresse/Stemmekrets |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Stemmekrets
description: Ei stemmekrets brukt ved val.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
is_a: GeografiskOmrade
slots:
- stemmekretsnummer
class_uri: ngr:Stemmekrets

```
</details>

### Induced

<details>
```yaml
name: Stemmekrets
description: Ei stemmekrets brukt ved val.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
is_a: GeografiskOmrade
attributes:
  stemmekretsnummer:
    name: stemmekretsnummer
    description: Stemmekretsnummer.
    from_schema: https://data.norge.no/ngr/ngr-adresse
    rank: 1000
    slot_uri: ngr:stemmekretsnummer
    owner: Stemmekrets
    domain_of:
    - Stemmekrets
    range: string
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-adresse
    rank: 1000
    identifier: true
    owner: Stemmekrets
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
    from_schema: https://data.norge.no/ngr/ngr-adresse
    rank: 1000
    slot_uri: ngr:namn
    owner: Stemmekrets
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Stemmekrets

```
</details>