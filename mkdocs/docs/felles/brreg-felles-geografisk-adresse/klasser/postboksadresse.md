

# Class: Postboksadresse 


_Ei postboksadresse._





URI: [brreg_felles_geografisk_adresse:Postboksadresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse/Postboksadresse)





```mermaid
 classDiagram
    class Postboksadresse
    click Postboksadresse href "../postboksadresse/"
      GeografiskAdresse <|-- Postboksadresse
        click GeografiskAdresse href "../geografiskadresse/"
      
      Postboksadresse : anleggsnavn
        
          
    
        
        
        Postboksadresse --> "0..1" String : anleggsnavn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Postboksadresse : br_adresse_id
        
          
    
        
        
        Postboksadresse --> "0..1" String : br_adresse_id
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Postboksadresse : co_navn
        
          
    
        
        
        Postboksadresse --> "0..1" String : co_navn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Postboksadresse : id
        
          
    
        
        
        Postboksadresse --> "1" Uriorcurie : id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      Postboksadresse : kommune
        
          
    
        
        
        Postboksadresse --> "0..1" Kommune : kommune
        click Kommune href "../kommune/"
    

        
      Postboksadresse : postboksnummer
        
          
    
        
        
        Postboksadresse --> "0..1" Postboksnummer : postboksnummer
        click Postboksnummer href "../postboksnummer/"
    

        
      Postboksadresse : poststed
        
          
    
        
        
        Postboksadresse --> "0..1" Poststed : poststed
        click Poststed href "../poststed/"
    

        
      Postboksadresse : type
        
          
    
        
        
        Postboksadresse --> "0..1" String : type
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      
```

!!! note "Om diagrammet"
    Klikk på attributt-radene i klasseboksen ovanfor opnar same side som
    klassenavnet — Mermaid sin `classDiagram`-syntaks støttar berre éin
    klikkbar lenkje per klasseboks, ikkje éin per attributt (BUG-14).
    `## Eigenskapar`-tabellen lenger nede på sida er fasiten for
    slot-spesifikke lenkjer.





## Inheritance
* [GeografiskAdresse](geografiskadresse.md)
    * **Postboksadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [brreg_felles_geografisk_adresse:Postboksadresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse/Postboksadresse) |

## Eigenskapar

### Andre

| Navn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [postboksnummer](postboksnummer.md) | 0..1 <br/> [Postboksnummer](postboksnummer.md) | Nummeret på postboksen. |
| [anleggsnavn](anleggsnavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namnet på anlegget/institusjonen postboksen høyrer til. |
| [poststed](poststed.md) | 0..1 <br/> [Poststed](poststed.md) | Poststedet adressa høyrer til. |
| [kommune](kommune.md) | 0..1 <br/> [Kommune](kommune.md) | Kommunen adressa ligg i. |


### Arva

| Navn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. | [GeografiskAdresse](geografiskadresse.md) |
| [br_adresse_id](br_adresse_id.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | BR sin interne identifikator for adressa. | [GeografiskAdresse](geografiskadresse.md) |
| [co_navn](co_navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | C/O-namn (omsorgsperson/-verksemd) knytt til adressa. | [GeografiskAdresse](geografiskadresse.md) |
| [type](type.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Diskriminator for kva slag geografisk adresse dette er. | [GeografiskAdresse](geografiskadresse.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:Postboksadresse |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/Postboksadresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Postboksadresse
description: Ei postboksadresse.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
rank: 1000
is_a: GeografiskAdresse
slots:
- postboksnummer
- anleggsnavn
- poststed
- kommune
class_uri: brreg_felles_geografisk_adresse:Postboksadresse

```
</details>

### Induced

<details>
```yaml
name: Postboksadresse
description: Ei postboksadresse.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
rank: 1000
is_a: GeografiskAdresse
attributes:
  postboksnummer:
    name: postboksnummer
    description: Nummeret på postboksen.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:postboksnummer
    owner: Postboksadresse
    domain_of:
    - Postboksadresse
    range: Postboksnummer
  anleggsnavn:
    name: anleggsnavn
    description: Namnet på anlegget/institusjonen postboksen høyrer til.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:anleggsnavn
    owner: Postboksadresse
    domain_of:
    - Postboksadresse
    range: string
  poststed:
    name: poststed
    description: Poststedet adressa høyrer til.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:poststed
    owner: Postboksadresse
    domain_of:
    - Postboksadresse
    - Stedsadresse
    - Vegadresse
    range: Poststed
  kommune:
    name: kommune
    description: Kommunen adressa ligg i.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:kommune
    owner: Postboksadresse
    domain_of:
    - Postboksadresse
    - Stedsadresse
    - Vegadresse
    range: Kommune
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    identifier: true
    owner: Postboksadresse
    domain_of:
    - GeografiskAdresse
    - Poststed
    - Kommune
    - Fylke
    - Matrikkelnummer
    - Adressenummer
    range: uriorcurie
    required: true
  br_adresse_id:
    name: br_adresse_id
    description: BR sin interne identifikator for adressa.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:brAdresseId
    owner: Postboksadresse
    domain_of:
    - GeografiskAdresse
    range: string
  co_navn:
    name: co_navn
    description: C/O-namn (omsorgsperson/-verksemd) knytt til adressa.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:coNavn
    owner: Postboksadresse
    domain_of:
    - GeografiskAdresse
    range: string
  type:
    name: type
    description: Diskriminator for kva slag geografisk adresse dette er.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:type
    owner: Postboksadresse
    domain_of:
    - GeografiskAdresse
    range: string
class_uri: brreg_felles_geografisk_adresse:Postboksadresse

```
</details>