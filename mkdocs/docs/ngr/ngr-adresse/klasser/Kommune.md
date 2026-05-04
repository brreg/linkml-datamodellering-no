

# Class: Kommune 


_Ein norsk kommune._





URI: [ngr:Kommune](https://data.norge.no/vocabulary/ngr-adresse#Kommune)





```mermaid
 classDiagram
    class Kommune
    click Kommune href "../Kommune/"
      GeografiskOmrade <|-- Kommune
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      Kommune : id
        
      Kommune : kommunenummer_kode
        
      Kommune : namn
        
      
```





## Inheritance
* [GeografiskOmrade](GeografiskOmrade.md)
    * **Kommune**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Kommune](https://data.norge.no/vocabulary/ngr-adresse#Kommune) |


## Eigenskapar







  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kommunenummer_kode](kommunenummer_kode.md) | 1 <br/> [String](String.md) | Firesifra kommunenummer (t |





  
  





  
  






  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | [GeografiskOmrade](GeografiskOmrade.md) |
| [namn](namn.md) | 0..1 <br/> [String](String.md) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](GeografiskOmrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | [kommunar](kommunar.md) | range | [Kommune](Kommune.md) |
| [OffisiellAdresse](OffisiellAdresse.md) | [kommunenummer_ref](kommunenummer_ref.md) | range | [Kommune](Kommune.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Kommune |
| native | https://data.norge.no/linkml/ngr-adresse/Kommune |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kommune
description: Ein norsk kommune.
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
slots:
- kommunenummer_kode
slot_usage:
  kommunenummer_kode:
    name: kommunenummer_kode
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngr:Kommune

```
</details>

### Induced

<details>
```yaml
name: Kommune
description: Ein norsk kommune.
from_schema: https://data.norge.no/linkml/ngr-adresse
is_a: GeografiskOmrade
slot_usage:
  kommunenummer_kode:
    name: kommunenummer_kode
    in_subset:
    - Obligatorisk
    required: true
attributes:
  kommunenummer_kode:
    name: kommunenummer_kode
    description: Firesifra kommunenummer (t.d. 0301 for Oslo).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: ngr:kommunenummer
    alias: kommunenummer_kode
    owner: Kommune
    domain_of:
    - Kommune
    range: string
    required: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: Kommune
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
    owner: Kommune
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Kommune

```
</details>