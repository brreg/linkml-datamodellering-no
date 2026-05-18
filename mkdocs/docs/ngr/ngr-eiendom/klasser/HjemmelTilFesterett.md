

# Class: HjemmelTilFesterett 


_Heimelsdokument for festerett (langvarig bruksrett til festegrunn)._





URI: [ngre:HjemmelTilFesterett](https://data.norge.no/vocabulary/ngr-eiendom#HjemmelTilFesterett)





```mermaid
 classDiagram
    class HjemmelTilFesterett
    click HjemmelTilFesterett href "../HjemmelTilFesterett/"
      Hjemmel <|-- HjemmelTilFesterett
        click Hjemmel href "../Hjemmel/"
      
      HjemmelTilFesterett : har_andel
        
          
    
        
        
        HjemmelTilFesterett --> "1..*" Andel : har_andel
        click Andel href "../Andel/"
    

        
      HjemmelTilFesterett : id
        
          
    
        
        
        HjemmelTilFesterett --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [Hjemmel](hjemmel.md)
    * **HjemmelTilFesterett**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:HjemmelTilFesterett](https://data.norge.no/vocabulary/ngr-eiendom#HjemmelTilFesterett) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Hjemmel](hjemmel.md) |
| [har_andel](har_andel.md) | 1..* <br/> [Andel](andel.md) | Andel(ar) i heimelsdokumentet | [Hjemmel](hjemmel.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [hjemmelFesterett](hjemmelfesterett.md) | range | [HjemmelTilFesterett](hjemmeltilfesterett.md) |
| [Eierforhold](eierforhold.md) | [gjelder_hjemmel_festerett](gjelder_hjemmel_festerett.md) | range | [HjemmelTilFesterett](hjemmeltilfesterett.md) |
| [TinglystEierforhold](tinglysteierforhold.md) | [gjelder_hjemmel_festerett](gjelder_hjemmel_festerett.md) | range | [HjemmelTilFesterett](hjemmeltilfesterett.md) |
| [IkkeTinglystEierforhold](ikketinglysteierforhold.md) | [gjelder_hjemmel_festerett](gjelder_hjemmel_festerett.md) | range | [HjemmelTilFesterett](hjemmeltilfesterett.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:HjemmelTilFesterett |
| native | https://data.norge.no/linkml/ngr-eiendom/HjemmelTilFesterett |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HjemmelTilFesterett
description: Heimelsdokument for festerett (langvarig bruksrett til festegrunn).
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
is_a: Hjemmel
class_uri: ngre:HjemmelTilFesterett

```
</details>

### Induced

<details>
```yaml
name: HjemmelTilFesterett
description: Heimelsdokument for festerett (langvarig bruksrett til festegrunn).
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
is_a: Hjemmel
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    identifier: true
    alias: id
    owner: HjemmelTilFesterett
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
    from_schema: https://data.norge.no/linkml/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harAndel
    alias: har_andel
    owner: HjemmelTilFesterett
    domain_of:
    - Hjemmel
    range: Andel
    required: true
    multivalued: true
    minimum_cardinality: 1
class_uri: ngre:HjemmelTilFesterett

```
</details>