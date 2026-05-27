

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
        
          
    
        
        
        Fylke --> "0..1" String : fylkesnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Fylke : id
        
          
    
        
        
        Fylke --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Fylke : navn
        
          
    
        
        
        Fylke --> "0..1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* [Skoleeier](skoleeier.md)
    * **Fylke**


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [fylkesnummer](fylkesnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Fylkesnummer er definerte identifikasjonskoder for Norges fylker og to territ... |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Skoleeier](skoleeier.md) |
| [navn](navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på ressursen | [Skoleeier](skoleeier.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | [fylker](fylker.md) | range | [Fylke](fylke.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:Fylke |
| native | samtbuskole:Fylke |
| exact | org:Organization |




## Examples
### Example: Fylke-fylke-30

```yaml
id: samtbuskole:fylke-30
fylkesnummer: '30'
navn: Viken fylkeskommune

```



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
rank: 1000
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
rank: 1000
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
    owner: Fylke
    domain_of:
    - Fylke
    range: string
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Fylke
    domain_of:
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - SamtBuContainer
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
    owner: Fylke
    domain_of:
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: string

```
</details>