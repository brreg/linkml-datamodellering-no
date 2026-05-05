

# Class: KommunalKrets 


_Ein kommunal krets (administrativ inndeling definert av kommunen)._





URI: [ngr:KommunalKrets](https://data.norge.no/vocabulary/ngr-adresse#KommunalKrets)





```mermaid
 classDiagram
    class KommunalKrets
    click KommunalKrets href "../KommunalKrets/"
      GeografiskOmrade <|-- KommunalKrets
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      KommunalKrets : id
        
      KommunalKrets : kretsnummer
        
      KommunalKrets : namn
        
      
```





## Inheritance
* [GeografiskOmrade](geografiskomrade.md)
    * **KommunalKrets**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:KommunalKrets](https://data.norge.no/vocabulary/ngr-adresse#KommunalKrets) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kretsnummer](kretsnummer.md) | 0..1 <br/> [String](string.md) | Kommunalt kretsnummer |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen | [GeografiskOmrade](geografiskomrade.md) |
| [namn](namn.md) | 0..1 <br/> [String](string.md) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](geografiskomrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | [kommunaleKretsar](kommunalekretsar.md) | range | [KommunalKrets](kommunalkrets.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:KommunalKrets |
| native | https://data.norge.no/linkml/ngr-adresse/KommunalKrets |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KommunalKrets
description: Ein kommunal krets (administrativ inndeling definert av kommunen).
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
slots:
- kretsnummer
class_uri: ngr:KommunalKrets

```
</details>

### Induced

<details>
```yaml
name: KommunalKrets
description: Ein kommunal krets (administrativ inndeling definert av kommunen).
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
attributes:
  kretsnummer:
    name: kretsnummer
    description: Kommunalt kretsnummer.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:kretsnummer
    alias: kretsnummer
    owner: KommunalKrets
    domain_of:
    - KommunalKrets
    range: string
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: KommunalKrets
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
    owner: KommunalKrets
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:KommunalKrets

```
</details>