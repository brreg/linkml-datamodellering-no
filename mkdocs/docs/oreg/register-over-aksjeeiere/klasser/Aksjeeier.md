

# Class: Aksjeeier 


_Person eller organisasjon som eig aksjar._





URI: [aksje:Aksjeeier](https://example.no/ontology/aksje#Aksjeeier)





```mermaid
 classDiagram
    class Aksjeeier
    click Aksjeeier href "../Aksjeeier/"
      Aksjeeier : har_eierposisjon
        
          
    
        
        
        Aksjeeier --> "0..1" Eierposisjon : har_eierposisjon
        click Eierposisjon href "../Eierposisjon/"
    

        
      Aksjeeier : identifikator
        
          
    
        
        
        Aksjeeier --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Aksjeeier : navn
        
          
    
        
        
        Aksjeeier --> "0..1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [navn](navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på instansen |
| [har_eierposisjon](har_eierposisjon.md) | 0..1 <br/> [Eierposisjon](eierposisjon.md) | Eierposisjon aksjeeigaren har |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [aksjeeiere](aksjeeiere.md) | range | [Aksjeeier](aksjeeier.md) |
| [Aksjeeier](aksjeeier.md) | [har_eierposisjon](har_eierposisjon.md) | domain | [Aksjeeier](aksjeeier.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:Aksjeeier |
| native | aksje:Aksjeeier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjeeier
description: Person eller organisasjon som eig aksjar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- navn
- har_eierposisjon

```
</details>

### Induced

<details>
```yaml
name: Aksjeeier
description: Person eller organisasjon som eig aksjar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Aksjeeier
    domain_of:
    - Containerklasse
    - Aksjeselskap
    - Aksjekapital
    - Aksje
    - Aksjeklasse
    - Aksjeeierrettighet
    - Aksjeeier
    - Eierposisjon
    - Aksjepost
    - Utbytte
    - Utdeling
    - Eierskapstransaksjon
    - Aksjeoverdragelse
    - Vederlag
    - Selskapshendelse
    - Aksjeinnskudd
    range: uriorcurie
    required: true
  navn:
    name: navn
    description: Namn på instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    alias: navn
    owner: Aksjeeier
    domain_of:
    - Aksjeselskap
    - Aksjeklasse
    - Aksjeeier
    range: string
    inlined: true
  har_eierposisjon:
    name: har_eierposisjon
    description: Eierposisjon aksjeeigaren har.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksjeeier
    alias: har_eierposisjon
    owner: Aksjeeier
    domain_of:
    - Aksjeeier
    range: Eierposisjon

```
</details>