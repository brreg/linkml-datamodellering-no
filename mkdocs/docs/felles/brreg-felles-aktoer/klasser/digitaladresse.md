

# Class: DigitalAdresse 


_Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under._





URI: [brreg_felles_digital_adresse:DigitalAdresse](https://data.norge.no/felles/brreg-felles-digital-adresse/DigitalAdresse)





```mermaid
 classDiagram
    class DigitalAdresse
    click DigitalAdresse href "../digitaladresse/"
      DigitalAdresse <|-- IPAdresse
        click IPAdresse href "../ipadresse/"
      DigitalAdresse <|-- EPostadresse
        click EPostadresse href "../epostadresse/"
      DigitalAdresse <|-- Nettadresse
        click Nettadresse href "../nettadresse/"
      DigitalAdresse <|-- Meldingsboks
        click Meldingsboks href "../meldingsboks/"
      DigitalAdresse <|-- Mobiltelefonnummer
        click Mobiltelefonnummer href "../mobiltelefonnummer/"
      DigitalAdresse <|-- Telefonnummer
        click Telefonnummer href "../telefonnummer/"
      
      DigitalAdresse : digital_adresse_id
        
          
    
        
        
        DigitalAdresse --> "1" Uriorcurie : digital_adresse_id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      DigitalAdresse : digital_adresse_type
        
          
    
        
        
        DigitalAdresse --> "0..1" String : digital_adresse_type
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      DigitalAdresse : identifikator
        
          
    
        
        
        DigitalAdresse --> "0..1" String : identifikator
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      
```

!!! note "Om diagrammet"
    Klikk på attributt-radene i klasseboksen ovanfor opnar same side som
    klassenavnet — Mermaid sin `classDiagram`-syntaks støttar berre éin
    klikkbar lenkje per klasseboks, ikkje éin per attributt (BUG-14).
    `## Eigenskapar`-tabellen lenger nede på sida er fasiten for
    slot-spesifikke lenkjer.





## Inheritance
* **DigitalAdresse**
    * [IPAdresse](ipadresse.md)
    * [EPostadresse](epostadresse.md)
    * [Nettadresse](nettadresse.md)
    * [Meldingsboks](meldingsboks.md)
    * [Mobiltelefonnummer](mobiltelefonnummer.md)
    * [Telefonnummer](telefonnummer.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [brreg_felles_digital_adresse:DigitalAdresse](https://data.norge.no/felles/brreg-felles-digital-adresse/DigitalAdresse) |

## Eigenskapar

### Andre

| Navn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [digital_adresse_id](digital_adresse_id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. |
| [identifikator](identifikator.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Identifikator for den digitale adressa (form varierer per undertype). |
| [digital_adresse_type](digital_adresse_type.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Diskriminator for kva slag digital adresse dette er. |






## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Aktoer](aktoer.md) | [digital_adresse](digital_adresse.md) | range | [DigitalAdresse](digitaladresse.md) |
| [Virksomhet](virksomhet.md) | [digital_adresse](digital_adresse.md) | range | [DigitalAdresse](digitaladresse.md) |
| [Person](person.md) | [digital_adresse](digital_adresse.md) | range | [DigitalAdresse](digitaladresse.md) |
| [Kontaktinformasjon](kontaktinformasjon.md) | [digital_adresse](digital_adresse.md) | range | [DigitalAdresse](digitaladresse.md) |
| [Rolle](rolle.md) | [digital_adresse](digital_adresse.md) | range | [DigitalAdresse](digitaladresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-digital-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_digital_adresse:DigitalAdresse |
| native | https://data.norge.no/felles/brreg-felles-digital-adresse/DigitalAdresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DigitalAdresse
description: Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane
  under.
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
slots:
- digital_adresse_id
- identifikator
- digital_adresse_type
slot_usage:
  identifikator:
    name: identifikator
    description: Identifikator for den digitale adressa (form varierer per undertype).
  digital_adresse_type:
    name: digital_adresse_type
    description: Diskriminator for kva slag digital adresse dette er.
class_uri: brreg_felles_digital_adresse:DigitalAdresse

```
</details>

### Induced

<details>
```yaml
name: DigitalAdresse
description: Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane
  under.
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
slot_usage:
  identifikator:
    name: identifikator
    description: Identifikator for den digitale adressa (form varierer per undertype).
  digital_adresse_type:
    name: digital_adresse_type
    description: Diskriminator for kva slag digital adresse dette er.
attributes:
  digital_adresse_id:
    name: digital_adresse_id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:id
    identifier: true
    alias: id
    owner: DigitalAdresse
    domain_of:
    - DigitalAdresse
    range: uriorcurie
    required: true
  identifikator:
    name: identifikator
    description: Identifikator for den digitale adressa (form varierer per undertype).
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:identifikator
    owner: DigitalAdresse
    domain_of:
    - DigitalAdresse
    - Aktoer
    range: string
  digital_adresse_type:
    name: digital_adresse_type
    description: Diskriminator for kva slag digital adresse dette er.
    from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
    slot_uri: brreg_felles_digital_adresse:type
    alias: type
    owner: DigitalAdresse
    domain_of:
    - DigitalAdresse
    range: string
class_uri: brreg_felles_digital_adresse:DigitalAdresse

```
</details>