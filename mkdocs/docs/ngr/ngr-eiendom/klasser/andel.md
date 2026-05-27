

# Class: Andel 


_Ein eigarandel i eit heimelsdokument (også kalt eierandel). Kvar andel har ein eller fleire rettigheitshavarar._





URI: [ngre:Andel](https://data.norge.no/vocabulary/ngr-eiendom#Andel)





```mermaid
 classDiagram
    class Andel
    click Andel href "../Andel/"
      Andel : har_rettighetshaver
        
          
    
        
        
        Andel --> "1..*" Rettighetshaver : har_rettighetshaver
        click Rettighetshaver href "../Rettighetshaver/"
    

        
      Andel : id
        
          
    
        
        
        Andel --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ngre:Andel](https://data.norge.no/vocabulary/ngr-eiendom#Andel) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_rettighetshaver](har_rettighetshaver.md) | 1..* <br/> [Rettighetshaver](rettighetshaver.md) | Rettigheitshavar(ar) for andelen |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | [andeler](andeler.md) | range | [Andel](andel.md) |
| [Hjemmel](hjemmel.md) | [har_andel](har_andel.md) | range | [Andel](andel.md) |
| [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) | [har_andel](har_andel.md) | range | [Andel](andel.md) |
| [HjemmelTilFesterett](hjemmeltilfesterett.md) | [har_andel](har_andel.md) | range | [Andel](andel.md) |
| [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) | [har_andel](har_andel.md) | range | [Andel](andel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:Andel |
| native | https://data.norge.no/ngr/ngr-eiendom/Andel |




## Examples
### Example: Andel-andel-1

```yaml
id: ngre:eksempel/andel-1
har_rettighetshaver:
- ngre:eksempel/rettighetshaver-1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Andel
description: Ein eigarandel i eit heimelsdokument (også kalt eierandel). Kvar andel
  har ein eller fleire rettigheitshavarar.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slots:
- id
- har_rettighetshaver
slot_usage:
  har_rettighetshaver:
    name: har_rettighetshaver
    in_subset:
    - Obligatorisk
    required: true
    minimum_cardinality: 1
class_uri: ngre:Andel

```
</details>

### Induced

<details>
```yaml
name: Andel
description: Ein eigarandel i eit heimelsdokument (også kalt eierandel). Kvar andel
  har ein eller fleire rettigheitshavarar.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_usage:
  har_rettighetshaver:
    name: har_rettighetshaver
    in_subset:
    - Obligatorisk
    required: true
    minimum_cardinality: 1
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    identifier: true
    owner: Andel
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
  har_rettighetshaver:
    name: har_rettighetshaver
    description: Rettigheitshavar(ar) for andelen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ngr/ngr-eiendom
    rank: 1000
    slot_uri: ngre:harRettighetshaver
    owner: Andel
    domain_of:
    - Andel
    range: Rettighetshaver
    required: true
    multivalued: true
    minimum_cardinality: 1
class_uri: ngre:Andel

```
</details>