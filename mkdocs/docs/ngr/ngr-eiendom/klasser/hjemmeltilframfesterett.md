

# Class: HjemmelTilFramfesterett 


_Heimelsdokument for framfesterett (vidarefestekontrakt)._





URI: [ngre:HjemmelTilFramfesterett](https://data.norge.no/vocabulary/ngr-eiendom#HjemmelTilFramfesterett)





```mermaid
 classDiagram
    class HjemmelTilFramfesterett
    click HjemmelTilFramfesterett href "../HjemmelTilFramfesterett/"
      Hjemmel <|-- HjemmelTilFramfesterett
        click Hjemmel href "../Hjemmel/"
      
      HjemmelTilFramfesterett : har_andel
        
          
    
        
        
        HjemmelTilFramfesterett --> "1..*" Andel : har_andel
        click Andel href "../Andel/"
    

        
      HjemmelTilFramfesterett : id
        
          
    
        
        
        HjemmelTilFramfesterett --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [Hjemmel](hjemmel.md)
    * **HjemmelTilFramfesterett**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:HjemmelTilFramfesterett](https://data.norge.no/vocabulary/ngr-eiendom#HjemmelTilFramfesterett) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Hjemmel](hjemmel.md) |
| [har_andel](har_andel.md) | 1..* <br/> [Andel](andel.md) | Andel(ar) i heimelsdokumentet | [Hjemmel](hjemmel.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [hjemmelFramfesterett](hjemmelframfesterett.md) | range | [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) |
| [Eierforhold](eierforhold.md) | [gjelder_hjemmel_framfesterett](gjelder_hjemmel_framfesterett.md) | range | [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) |
| [TinglystEierforhold](tinglysteierforhold.md) | [gjelder_hjemmel_framfesterett](gjelder_hjemmel_framfesterett.md) | range | [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) |
| [IkkeTinglystEierforhold](ikketinglysteierforhold.md) | [gjelder_hjemmel_framfesterett](gjelder_hjemmel_framfesterett.md) | range | [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:HjemmelTilFramfesterett |
| native | https://data.norge.no/ngr/ngr-eiendom/HjemmelTilFramfesterett |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HjemmelTilFramfesterett
description: Heimelsdokument for framfesterett (vidarefestekontrakt).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
is_a: Hjemmel
class_uri: ngre:HjemmelTilFramfesterett

```
</details>

### Induced

<details>
```yaml
name: HjemmelTilFramfesterett
description: Heimelsdokument for framfesterett (vidarefestekontrakt).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
is_a: Hjemmel
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: HjemmelTilFramfesterett
    domain_of:
    - FastEiendom
    - SamletFastEiendom
    - Borettslagsandel
    - Matrikkelenhet
    - Matrikkelnummer
    - Kommunenummer
    - Gaardsnummer
    - Bruksnummer
    - Festenummer
    - Seksjonsnummer
    - Bygning
    - Bygningsnummer
    - Representasjonspunkt
    - YtreInngang
    - Bruksenhet
    - Bruksenhetsnummer
    - Etasje
    - Teig
    - Anleggsprojeksjonsflate
    - Eierforhold
    - Hjemmel
    - Andel
    - Rettighetshaver
    - TinglystHeftelse
    - RettighetForAaBenytteEiendom
    - Borettslag
    - OffisiellAdresse
    - Person
    - Hovedenhet
    - Kommune
    range: uriorcurie
    required: true
  har_andel:
    name: har_andel
    description: Andel(ar) i heimelsdokumentet.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harAndel
    owner: HjemmelTilFramfesterett
    domain_of:
    - Hjemmel
    range: Andel
    required: true
    multivalued: true
    minimum_cardinality: 1
class_uri: ngre:HjemmelTilFramfesterett

```
</details>