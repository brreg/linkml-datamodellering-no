

# Class: Fylke 


_Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt geografisk område, tilsvarende amt og len._





URI: [samtbuskole:Fylke](https://example.no/ontology/skole#Fylke)





```mermaid
 classDiagram
    class Fylke
    click Fylke href "../Fylke/"
      Skoleeier <|-- Fylke
        click Skoleeier href "../Skoleeier/"
      
      Fylke : fylkesnummer
        
      Fylke : identifikator
        
      Fylke : navn
        
      
```





## Inheritance
* [Skoleeier](skoleeier.md)
    * **Fylke**


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [fylkesnummer](fylkesnummer.md) | 0..1 <br/> [String](string.md) | Fylkesnummer er definerte identifikasjonskoder for Norges fylker og to territ... |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | Global identifikator (CURIE/URI) | [Skoleeier](skoleeier.md) |
| [navn](navn.md) | 0..1 <br/> [String](string.md) | Namn på ressursen | [Skoleeier](skoleeier.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [fylker](fylker.md) | range | [Fylke](fylke.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:Fylke |
| native | samtbuskole:Fylke |
| exact | org:Organization |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Fylke
description: Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt
  geografisk område, tilsvarende amt og len.
from_schema: https://example.no/ontology/samt-bu-skole
exact_mappings:
- org:Organization
is_a: Skoleeier
slots:
- fylkesnummer

```
</details>

### Induced

<details>
```yaml
name: Fylke
description: Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt
  geografisk område, tilsvarende amt og len.
from_schema: https://example.no/ontology/samt-bu-skole
exact_mappings:
- org:Organization
is_a: Skoleeier
attributes:
  fylkesnummer:
    name: fylkesnummer
    description: Fylkesnummer er definerte identifikasjonskoder for Norges fylker
      og to territorier (Svalbard og Jan Mayen).
    from_schema: https://example.no/ontology/samt-bu-skole
    close_mappings:
    - skos:notation
    rank: 1000
    slot_uri: dcat:identifier
    alias: fylkesnummer
    owner: Fylke
    domain_of:
    - Fylke
    range: string
  identifikator:
    name: identifikator
    description: Global identifikator (CURIE/URI).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Fylke
    domain_of:
    - Containerklasse
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: uriorcurie
    required: true
  navn:
    name: navn
    description: Namn på ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    alias: navn
    owner: Fylke
    domain_of:
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: string

```
</details>