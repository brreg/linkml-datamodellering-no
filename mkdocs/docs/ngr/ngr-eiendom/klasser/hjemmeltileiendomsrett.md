

# Class: HjemmelTilEiendomsrett 


_Heimelsdokument for eigedomsrett (full eigarrett)._





URI: [ngre:HjemmelTilEiendomsrett](https://data.norge.no/vocabulary/ngr-eiendom#HjemmelTilEiendomsrett)





```mermaid
 classDiagram
    class HjemmelTilEiendomsrett
    click HjemmelTilEiendomsrett href "../HjemmelTilEiendomsrett/"
      Hjemmel <|-- HjemmelTilEiendomsrett
        click Hjemmel href "../Hjemmel/"
      
      HjemmelTilEiendomsrett : har_andel
        
          
    
        
        
        HjemmelTilEiendomsrett --> "1..*" Andel : har_andel
        click Andel href "../Andel/"
    

        
      HjemmelTilEiendomsrett : id
        
          
    
        
        
        HjemmelTilEiendomsrett --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```





## Inheritance
* [Hjemmel](hjemmel.md)
    * **HjemmelTilEiendomsrett**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:HjemmelTilEiendomsrett](https://data.norge.no/vocabulary/ngr-eiendom#HjemmelTilEiendomsrett) |


## Eigenskapar























### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Hjemmel](hjemmel.md) |
| [har_andel](har_andel.md) | 1..* <br/> [Andel](andel.md) | Andel(ar) i heimelsdokumentet | [Hjemmel](hjemmel.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [hjemmelEiendomsrett](hjemmeleiendomsrett.md) | range | [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) |
| [Eierforhold](eierforhold.md) | [gjelder_hjemmel_eiendomsrett](gjelder_hjemmel_eiendomsrett.md) | range | [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) |
| [TinglystEierforhold](tinglysteierforhold.md) | [gjelder_hjemmel_eiendomsrett](gjelder_hjemmel_eiendomsrett.md) | range | [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) |
| [IkkeTinglystEierforhold](ikketinglysteierforhold.md) | [gjelder_hjemmel_eiendomsrett](gjelder_hjemmel_eiendomsrett.md) | range | [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:HjemmelTilEiendomsrett |
| native | https://data.norge.no/ngr/ngr-eiendom/HjemmelTilEiendomsrett |




## Examples
### Example: HjemmelTilEiendomsrett-hjemmel-1

```yaml
id: ngre:eksempel/hjemmel-1
har_andel:
- ngre:eksempel/andel-1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HjemmelTilEiendomsrett
description: Heimelsdokument for eigedomsrett (full eigarrett).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
is_a: Hjemmel
class_uri: ngre:HjemmelTilEiendomsrett

```
</details>

### Induced

<details>
```yaml
name: HjemmelTilEiendomsrett
description: Heimelsdokument for eigedomsrett (full eigarrett).
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
    owner: HjemmelTilEiendomsrett
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
    owner: HjemmelTilEiendomsrett
    domain_of:
    - Hjemmel
    range: Andel
    required: true
    multivalued: true
    minimum_cardinality: 1
class_uri: ngre:HjemmelTilEiendomsrett

```
</details>