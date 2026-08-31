

# Class: Telefonnummer 


_Eit fasttelefonnummer._





URI: [brreg_felles_adresse:Telefonnummer](https://data.norge.no/felles/brreg-felles-adresse/Telefonnummer)





```mermaid
 classDiagram
    class Telefonnummer
    click Telefonnummer href "../telefonnummer/"
      DigitalAdresse <|-- Telefonnummer
        click DigitalAdresse href "../digitaladresse/"
      
      Telefonnummer : id
        
          
    
        
        
        Telefonnummer --> "1" Uriorcurie : id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      Telefonnummer : identifikator
        
          
    
        
        
        Telefonnummer --> "0..1" String : identifikator
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Telefonnummer : nasjonalt_nummer
        
          
    
        
        
        Telefonnummer --> "0..1" NasjonaltNummer : nasjonalt_nummer
        click NasjonaltNummer href "../nasjonaltnummer/"
    

        
      Telefonnummer : prefiks_med_nasjonal_kode
        
          
    
        
        
        Telefonnummer --> "0..1" PrefiksMedNasjonalKode : prefiks_med_nasjonal_kode
        click PrefiksMedNasjonalKode href "../prefiksmednasjonalkode/"
    

        
      Telefonnummer : type
        
          
    
        
        
        Telefonnummer --> "0..1" String : type
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
    * **Telefonnummer**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [brreg_felles_adresse:Telefonnummer](https://data.norge.no/felles/brreg-felles-adresse/Telefonnummer) |

## Eigenskapar

### Andre

| Navn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [prefiks_med_nasjonal_kode](prefiks_med_nasjonal_kode.md) | 0..1 <br/> [PrefiksMedNasjonalKode](prefiksmednasjonalkode.md) | Internasjonalt telefonprefiks (landkode), t.d. "+47". |
| [nasjonalt_nummer](nasjonalt_nummer.md) | 0..1 <br/> [NasjonaltNummer](nasjonaltnummer.md) | Telefonnummeret utan landkode/prefiks. |


### Arva

| Navn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. | [DigitalAdresse](digitaladresse.md) |
| [identifikator](identifikator.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Identifikator for den digitale adressa (form varierer per undertype). | [DigitalAdresse](digitaladresse.md) |
| [type](type.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Diskriminator for kva slag digital adresse dette er. | [DigitalAdresse](digitaladresse.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_adresse:Telefonnummer |
| native | https://data.norge.no/felles/brreg-felles-adresse/Telefonnummer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Telefonnummer
description: Eit fasttelefonnummer.
from_schema: https://data.norge.no/felles/brreg-felles-adresse
rank: 1000
is_a: DigitalAdresse
slots:
- prefiks_med_nasjonal_kode
- nasjonalt_nummer
class_uri: brreg_felles_adresse:Telefonnummer

```
</details>

### Induced

<details>
```yaml
name: Telefonnummer
description: Eit fasttelefonnummer.
from_schema: https://data.norge.no/felles/brreg-felles-adresse
rank: 1000
is_a: DigitalAdresse
attributes:
  prefiks_med_nasjonal_kode:
    name: prefiks_med_nasjonal_kode
    description: Internasjonalt telefonprefiks (landkode), t.d. "+47".
    from_schema: https://data.norge.no/felles/brreg-felles-adresse
    slot_uri: brreg_felles_adresse:prefiksMedNasjonalKode
    owner: Telefonnummer
    domain_of:
    - Mobiltelefonnummer
    - Telefonnummer
    range: PrefiksMedNasjonalKode
  nasjonalt_nummer:
    name: nasjonalt_nummer
    description: Telefonnummeret utan landkode/prefiks.
    from_schema: https://data.norge.no/felles/brreg-felles-adresse
    slot_uri: brreg_felles_adresse:nasjonaltNummer
    owner: Telefonnummer
    domain_of:
    - Mobiltelefonnummer
    - Telefonnummer
    range: NasjonaltNummer
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/felles/brreg-felles-adresse
    identifier: true
    owner: Telefonnummer
    domain_of:
    - GeografiskAdresse
    - DigitalAdresse
    - Poststed
    - Kommune
    - Fylke
    - Matrikkelnummer
    - Adressenummer
    range: uriorcurie
    required: true
  identifikator:
    name: identifikator
    description: Identifikator for den digitale adressa (form varierer per undertype).
    from_schema: https://data.norge.no/felles/brreg-felles-adresse
    slot_uri: brreg_felles_adresse:identifikator
    owner: Telefonnummer
    domain_of:
    - DigitalAdresse
    range: string
  type:
    name: type
    description: Diskriminator for kva slag digital adresse dette er.
    from_schema: https://data.norge.no/felles/brreg-felles-adresse
    slot_uri: brreg_felles_adresse:type
    owner: Telefonnummer
    domain_of:
    - GeografiskAdresse
    - DigitalAdresse
    range: string
class_uri: brreg_felles_adresse:Telefonnummer

```
</details>