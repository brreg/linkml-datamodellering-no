

# Class: Aksjeselskap 


_Selskap som utsteder aksjar og har aksjekapital._





URI: [aksje:Aksjeselskap](https://example.no/ontology/aksje#Aksjeselskap)





```mermaid
 classDiagram
    class Aksjeselskap
    click Aksjeselskap href "../Aksjeselskap/"
      Aksjeselskap : har_aksjekapital
        
          
    
        
        
        Aksjeselskap --> "0..1" Aksjekapital : har_aksjekapital
        click Aksjekapital href "../Aksjekapital/"
    

        
      Aksjeselskap : identifikator
        
      Aksjeselskap : navn
        
      Aksjeselskap : utsteder_aksje
        
          
    
        
        
        Aksjeselskap --> "0..1" Aksje : utsteder_aksje
        click Aksje href "../Aksje/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | Global identifikator for instansen |
| [navn](navn.md) | 0..1 <br/> [String](string.md) | Namn på instansen |
| [har_aksjekapital](har_aksjekapital.md) | 0..1 <br/> [Aksjekapital](aksjekapital.md) | Aksjekapital som høyrer til selskapet |
| [utsteder_aksje](utsteder_aksje.md) | 0..1 <br/> [Aksje](aksje.md) | Aksje utstedt av selskapet |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [aksjeselskaper](aksjeselskaper.md) | range | [Aksjeselskap](aksjeselskap.md) |
| [Aksjeselskap](aksjeselskap.md) | [har_aksjekapital](har_aksjekapital.md) | domain | [Aksjeselskap](aksjeselskap.md) |
| [Aksjeselskap](aksjeselskap.md) | [utsteder_aksje](utsteder_aksje.md) | domain | [Aksjeselskap](aksjeselskap.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:Aksjeselskap |
| native | aksje:Aksjeselskap |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjeselskap
description: Selskap som utsteder aksjar og har aksjekapital.
from_schema: https://example.no/ontology/aksje-eierskap
slots:
- identifikator
- navn
- har_aksjekapital
- utsteder_aksje

```
</details>

### Induced

<details>
```yaml
name: Aksjeselskap
description: Selskap som utsteder aksjar og har aksjekapital.
from_schema: https://example.no/ontology/aksje-eierskap
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Aksjeselskap
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
    owner: Aksjeselskap
    domain_of:
    - Aksjeselskap
    - Aksjeklasse
    - Aksjeeier
    range: string
    inlined: true
  har_aksjekapital:
    name: har_aksjekapital
    description: Aksjekapital som høyrer til selskapet.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksjeselskap
    alias: har_aksjekapital
    owner: Aksjeselskap
    domain_of:
    - Aksjeselskap
    range: Aksjekapital
  utsteder_aksje:
    name: utsteder_aksje
    description: Aksje utstedt av selskapet
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksjeselskap
    alias: utsteder_aksje
    owner: Aksjeselskap
    domain_of:
    - Aksjeselskap
    range: Aksje

```
</details>