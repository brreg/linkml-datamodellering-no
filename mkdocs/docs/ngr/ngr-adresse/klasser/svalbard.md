

# Class: Svalbard 


_Svalbard som særskild geografisk område._





URI: [ngr:Svalbard](https://data.norge.no/vocabulary/ngr-adresse#Svalbard)





```mermaid
 classDiagram
    class Svalbard
    click Svalbard href "../Svalbard/"
      GeografiskOmrade <|-- Svalbard
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      Svalbard : id
        
          
    
        
        
        Svalbard --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Svalbard : namn
        
          
    
        
        
        Svalbard --> "0..1" String : namn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* [GeografiskOmrade](geografiskomrade.md)
    * **Svalbard**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Svalbard](https://data.norge.no/vocabulary/ngr-adresse#Svalbard) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [GeografiskOmrade](geografiskomrade.md) |
| [namn](namn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](geografiskomrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | [svalbardOmrader](svalbardomrader.md) | range | [Svalbard](svalbard.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Svalbard |
| native | https://data.norge.no/ngr/ngr-adresse/Svalbard |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Svalbard
description: Svalbard som særskild geografisk område.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
is_a: GeografiskOmrade
class_uri: ngr:Svalbard

```
</details>

### Induced

<details>
```yaml
name: Svalbard
description: Svalbard som særskild geografisk område.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
is_a: GeografiskOmrade
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-adresse
    rank: 1000
    identifier: true
    owner: Svalbard
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
    owner: Svalbard
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Svalbard

```
</details>