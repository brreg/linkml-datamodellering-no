

# Class: Nettadresse 


_Ei nettadresse (protokoll, domenenavn og filsti)._





URI: [brreg_felles_digital_adresse:Nettadresse](https://data.norge.no/felles/brreg-felles-digital-adresse/Nettadresse)





```mermaid
 classDiagram
    class Nettadresse
    click Nettadresse href "../nettadresse/"
      DigitalAdresse <|-- Nettadresse
        click DigitalAdresse href "../digitaladresse/"
      
      Nettadresse : digital_adresse_id
        
          
    
        
        
        Nettadresse --> "1" Uriorcurie : digital_adresse_id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      Nettadresse : digital_adresse_type
        
          
    
        
        
        Nettadresse --> "0..1" String : digital_adresse_type
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Nettadresse : domenenavn
        
          
    
        
        
        Nettadresse --> "0..1" String : domenenavn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Nettadresse : filsti
        
          
    
        
        
        Nettadresse --> "0..1" String : filsti
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Nettadresse : identifikator
        
          
    
        
        
        Nettadresse --> "0..1" String : identifikator
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Nettadresse : protokoll
        
          
    
        
        
        Nettadresse --> "0..1" String : protokoll
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      
```

!!! note "Om diagrammet"
    Klikk på attributt-radene i klasseboksen ovanfor opnar same side som
    klassenavnet — Mermaid sin `classDiagram`-syntaks støttar berre éin
    klikkbar lenkje per klasseboks, ikkje éin per attributt (BUG-14).
    `## Eigenskapar`-tabellen lenger nede på sida er fasiten for
    slot-spesifikke lenkjer.





## Inheritance
* [DigitalAdresse](digitaladresse.md)
    * **Nettadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [brreg_felles_digital_adresse:Nettadresse](https://data.norge.no/felles/brreg-felles-digital-adresse/Nettadresse) |

## Eigenskapar

### Andre

| Navn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [protokoll](protokoll.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Protokollen for nettadressa, t.d. https. |
| [domenenavn](domenenavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Domenenamnet i adressa. |
| [filsti](filsti.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Filstien i nettadressa. |


### Arva

| Navn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
| [digital_adresse_id](digital_adresse_id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. | [DigitalAdresse](digitaladresse.md) |
| [identifikator](identifikator.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Identifikator for den digitale adressa (form varierer per undertype). | [DigitalAdresse](digitaladresse.md) |
| [digital_adresse_type](digital_adresse_type.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Diskriminator for kva slag digital adresse dette er. | [DigitalAdresse](digitaladresse.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-digital-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_digital_adresse:Nettadresse |
| native | https://data.norge.no/felles/brreg-felles-digital-adresse/Nettadresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Nettadresse
description: Ei nettadresse (protokoll, domenenavn og filsti).
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
rank: 1000
is_a: DigitalAdresse
slots:
- protokoll
- domenenavn
- filsti
class_uri: brreg_felles_digital_adresse:Nettadresse

```
</details>

### Induced

<details>
```yaml
name: Nettadresse
description: Ei nettadresse (protokoll, domenenavn og filsti).
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
rank: 1000
is_a: DigitalAdresse
attributes:
  protokoll:
    name: protokoll
    description: Protokollen for nettadressa, t.d. https.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:protokoll
    owner: Nettadresse
    domain_of:
    - Nettadresse
    range: string
  domenenavn:
    name: domenenavn
    description: Domenenamnet i adressa.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:domenenavn
    owner: Nettadresse
    domain_of:
    - EPostadresse
    - Nettadresse
    range: string
  filsti:
    name: filsti
    description: Filstien i nettadressa.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:filsti
    owner: Nettadresse
    domain_of:
    - Nettadresse
    range: string
  digital_adresse_id:
    name: digital_adresse_id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:id
    identifier: true
    alias: id
    owner: Nettadresse
    domain_of:
    - DigitalAdresse
    range: uriorcurie
    required: true
  identifikator:
    name: identifikator
    description: Identifikator for den digitale adressa (form varierer per undertype).
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:identifikator
    owner: Nettadresse
    domain_of:
    - DigitalAdresse
    range: string
  digital_adresse_type:
    name: digital_adresse_type
    description: Diskriminator for kva slag digital adresse dette er.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:type
    alias: type
    owner: Nettadresse
    domain_of:
    - DigitalAdresse
    range: string
class_uri: brreg_felles_digital_adresse:Nettadresse

```
</details>