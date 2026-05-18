

# Class: Poststed 


_Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret._





URI: [ngr:Poststed](https://data.norge.no/vocabulary/ngr-adresse#Poststed)





```mermaid
 classDiagram
    class Poststed
    click Poststed href "../Poststed/"
      GeografiskOmrade <|-- Poststed
        click GeografiskOmrade href "../GeografiskOmrade/"
      
      Poststed : id
        
          
    
        
        
        Poststed --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Poststed : namn
        
          
    
        
        
        Poststed --> "0..1" String : namn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Poststed : postnummer
        
          
    
        
        
        Poststed --> "1" String : postnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* [GeografiskOmrade](geografiskomrade.md)
    * **Poststed**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngr:Poststed](https://data.norge.no/vocabulary/ngr-adresse#Poststed) |


## Eigenskapar







  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [postnummer](postnummer.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Firesifra postnummer (locn:postCode) |





  
  





  
  






  
  
  
    
      
    
      
    
      
    
  
  




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [GeografiskOmrade](geografiskomrade.md) |
| [namn](namn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på det geografiske området eller adressekomponenten | [GeografiskOmrade](geografiskomrade.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | [poststeder](poststeder.md) | range | [Poststed](poststed.md) |
| [Postboksadresse](postboksadresse.md) | [poststed_ref](poststed_ref.md) | range | [Poststed](poststed.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:Poststed |
| native | https://data.norge.no/linkml/ngr-adresse/Poststed |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Poststed
description: Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
is_a: GeografiskOmrade
slots:
- postnummer
slot_usage:
  postnummer:
    name: postnummer
    in_subset:
    - Obligatorisk
    required: true
class_uri: ngr:Poststed

```
</details>

### Induced

<details>
```yaml
name: Poststed
description: Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
is_a: GeografiskOmrade
slot_usage:
  postnummer:
    name: postnummer
    in_subset:
    - Obligatorisk
    required: true
attributes:
  postnummer:
    name: postnummer
    description: Firesifra postnummer (locn:postCode).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    slot_uri: locn:postCode
    alias: postnummer
    owner: Poststed
    domain_of:
    - Poststed
    range: string
    required: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-adresse
    rank: 1000
    identifier: true
    alias: id
    owner: Poststed
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
    owner: Poststed
    domain_of:
    - Adresseomrade
    - GeografiskOmrade
    range: string
class_uri: ngr:Poststed

```
</details>