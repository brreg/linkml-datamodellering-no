

# Class: Vegadresse 


_Ei vegadresse (adressenavn + adressenummer)._





URI: [brreg_felles_geografisk_adresse:Vegadresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse/Vegadresse)





```mermaid
 classDiagram
    class Vegadresse
    click Vegadresse href "../vegadresse/"
      GeografiskAdresse <|-- Vegadresse
        click GeografiskAdresse href "../geografiskadresse/"
      
      Vegadresse : adressenavn
        
          
    
        
        
        Vegadresse --> "0..1" String : adressenavn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Vegadresse : adressenummer
        
          
    
        
        
        Vegadresse --> "0..1" Adressenummer : adressenummer
        click Adressenummer href "../adressenummer/"
    

        
      Vegadresse : adressetilleggsnavn
        
          
    
        
        
        Vegadresse --> "0..1" String : adressetilleggsnavn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Vegadresse : br_adresse_id
        
          
    
        
        
        Vegadresse --> "0..1" String : br_adresse_id
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Vegadresse : bruksenhetsnummer
        
          
    
        
        
        Vegadresse --> "0..1" Bruksenhetsnummer : bruksenhetsnummer
        click Bruksenhetsnummer href "../bruksenhetsnummer/"
    

        
      Vegadresse : co_navn
        
          
    
        
        
        Vegadresse --> "0..1" String : co_navn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Vegadresse : fylke
        
          
    
        
        
        Vegadresse --> "0..1" Fylke : fylke
        click Fylke href "../fylke/"
    

        
      Vegadresse : id
        
          
    
        
        
        Vegadresse --> "1" Uriorcurie : id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      Vegadresse : kommune
        
          
    
        
        
        Vegadresse --> "0..1" Kommune : kommune
        click Kommune href "../kommune/"
    

        
      Vegadresse : kort_adressenavn
        
          
    
        
        
        Vegadresse --> "0..1" String : kort_adressenavn
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Vegadresse : poststed
        
          
    
        
        
        Vegadresse --> "0..1" Poststed : poststed
        click Poststed href "../poststed/"
    

        
      Vegadresse : type
        
          
    
        
        
        Vegadresse --> "0..1" String : type
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Vegadresse : vegadresse_id
        
          
    
        
        
        Vegadresse --> "0..1" String : vegadresse_id
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
    * **Vegadresse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [brreg_felles_geografisk_adresse:Vegadresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse/Vegadresse) |

## Eigenskapar

### Andre

| Navn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [vegadresse_id](vegadresse_id.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | BR sin interne identifikator for vegadressa. |
| [bruksenhetsnummer](bruksenhetsnummer.md) | 0..1 <br/> [Bruksenhetsnummer](bruksenhetsnummer.md) | Bruksenhetsnummer (bustadnummer) i adressa, t.d. "H0101". |
| [adressenavn](adressenavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namnet på vegen/gata/staden. |
| [kort_adressenavn](kort_adressenavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Forkorta versjon av adressenamnet. |
| [adressenummer](adressenummer.md) | 0..1 <br/> [Adressenummer](adressenummer.md) | Husnummer og eventuell husbokstav i vegadressa. |
| [poststed](poststed.md) | 0..1 <br/> [Poststed](poststed.md) | Poststedet adressa høyrer til. |
| [adressetilleggsnavn](adressetilleggsnavn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tilleggsnamn til adressa (t.d. stadnamn i tillegg til vegadresse). |
| [kommune](kommune.md) | 0..1 <br/> [Kommune](kommune.md) | Kommunen adressa ligg i. |
| [fylke](fylke.md) | 0..1 <br/> [Fylke](fylke.md) | Fylket adressa ligg i. |


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
| self | brreg_felles_geografisk_adresse:Vegadresse |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/Vegadresse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vegadresse
description: Ei vegadresse (adressenavn + adressenummer).
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
rank: 1000
is_a: GeografiskAdresse
slots:
- vegadresse_id
- bruksenhetsnummer
- adressenavn
- kort_adressenavn
- adressenummer
- poststed
- adressetilleggsnavn
- kommune
- fylke
slot_usage:
  vegadresse_id:
    name: vegadresse_id
    description: BR sin interne identifikator for vegadressa.
class_uri: brreg_felles_geografisk_adresse:Vegadresse

```
</details>

### Induced

<details>
```yaml
name: Vegadresse
description: Ei vegadresse (adressenavn + adressenummer).
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
rank: 1000
is_a: GeografiskAdresse
slot_usage:
  vegadresse_id:
    name: vegadresse_id
    description: BR sin interne identifikator for vegadressa.
attributes:
  vegadresse_id:
    name: vegadresse_id
    description: BR sin interne identifikator for vegadressa.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:vegadresseId
    owner: Vegadresse
    domain_of:
    - Vegadresse
    range: string
  bruksenhetsnummer:
    name: bruksenhetsnummer
    description: Bruksenhetsnummer (bustadnummer) i adressa, t.d. "H0101".
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:bruksenhetsnummer
    owner: Vegadresse
    domain_of:
    - Vegadresse
    - Matrikkeladresse
    range: Bruksenhetsnummer
  adressenavn:
    name: adressenavn
    description: Namnet på vegen/gata/staden.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:adressenavn
    owner: Vegadresse
    domain_of:
    - Vegadresse
    - InternasjonalAdresse
    range: string
  kort_adressenavn:
    name: kort_adressenavn
    description: Forkorta versjon av adressenamnet.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:kortAdressenavn
    owner: Vegadresse
    domain_of:
    - Vegadresse
    range: string
  adressenummer:
    name: adressenummer
    description: Husnummer og eventuell husbokstav i vegadressa.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:adressenummer
    owner: Vegadresse
    domain_of:
    - Vegadresse
    range: Adressenummer
  poststed:
    name: poststed
    description: Poststedet adressa høyrer til.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:poststed
    owner: Vegadresse
    domain_of:
    - Postboksadresse
    - Stedsadresse
    - Vegadresse
    range: Poststed
  adressetilleggsnavn:
    name: adressetilleggsnavn
    description: Tilleggsnamn til adressa (t.d. stadnamn i tillegg til vegadresse).
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:adressetilleggsnavn
    owner: Vegadresse
    domain_of:
    - Vegadresse
    - Matrikkeladresse
    range: string
  kommune:
    name: kommune
    description: Kommunen adressa ligg i.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:kommune
    owner: Vegadresse
    domain_of:
    - Postboksadresse
    - Stedsadresse
    - Vegadresse
    range: Kommune
  fylke:
    name: fylke
    description: Fylket adressa ligg i.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:fylke
    owner: Vegadresse
    domain_of:
    - Vegadresse
    range: Fylke
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    identifier: true
    owner: Vegadresse
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
    owner: Vegadresse
    domain_of:
    - GeografiskAdresse
    range: string
  co_navn:
    name: co_navn
    description: C/O-namn (omsorgsperson/-verksemd) knytt til adressa.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:coNavn
    owner: Vegadresse
    domain_of:
    - GeografiskAdresse
    range: string
  type:
    name: type
    description: Diskriminator for kva slag geografisk adresse dette er.
    from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
    slot_uri: brreg_felles_geografisk_adresse:type
    owner: Vegadresse
    domain_of:
    - GeografiskAdresse
    range: string
class_uri: brreg_felles_geografisk_adresse:Vegadresse

```
</details>