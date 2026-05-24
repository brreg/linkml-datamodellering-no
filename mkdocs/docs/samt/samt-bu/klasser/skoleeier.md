

# Class: Skoleeier 


_Superklasse for alle typer skoleeiere._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [samtbuskole:Skoleeier](https://example.no/ontology/skole#Skoleeier)





```mermaid
 classDiagram
    class Skoleeier
    click Skoleeier href "../Skoleeier/"
      Skoleeier <|-- Kommune
        click Kommune href "../Kommune/"
      Skoleeier <|-- Fylke
        click Fylke href "../Fylke/"
      Skoleeier <|-- PrivatVirksomhet
        click PrivatVirksomhet href "../PrivatVirksomhet/"
      
      Skoleeier : id
        
          
    
        
        
        Skoleeier --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Skoleeier : navn
        
          
    
        
        
        Skoleeier --> "0..1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* **Skoleeier**
    * [Kommune](kommune.md)
    * [Fylke](fylke.md)
    * [PrivatVirksomhet](privatvirksomhet.md)


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |
| [navn](navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Skole](skole.md) | [har_skoleeier](har_skoleeier.md) | range | [Skoleeier](skoleeier.md) |










## See Also

* [https://data.norge.no/concepts/91b83e9a-8beb-3747-b65c-238a2bef605a](https://data.norge.no/concepts/91b83e9a-8beb-3747-b65c-238a2bef605a)



## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:Skoleeier |
| native | samtbuskole:Skoleeier |
| exact | foaf:Agent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Skoleeier
description: Superklasse for alle typer skoleeiere.
from_schema: https://example.no/ontology/samt-bu-skole
see_also:
- https://data.norge.no/concepts/91b83e9a-8beb-3747-b65c-238a2bef605a
exact_mappings:
- foaf:Agent
rank: 1000
abstract: true
slots:
- id
- navn

```
</details>

### Induced

<details>
```yaml
name: Skoleeier
description: Superklasse for alle typer skoleeiere.
from_schema: https://example.no/ontology/samt-bu-skole
see_also:
- https://data.norge.no/concepts/91b83e9a-8beb-3747-b65c-238a2bef605a
exact_mappings:
- foaf:Agent
rank: 1000
abstract: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: Skoleeier
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
    owner: Skoleeier
    domain_of:
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: string

```
</details>