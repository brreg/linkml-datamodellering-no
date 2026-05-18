

# Class: Vederlag 


_Vederlag knytt til ei aksjeoverdraging._





URI: [aksje:Vederlag](https://example.no/ontology/aksje#Vederlag)





```mermaid
 classDiagram
    class Vederlag
    click Vederlag href "../Vederlag/"
      Vederlag : belop
        
          
    
        
        
        Vederlag --> "0..1" Decimal : belop
        click Decimal href "../http://www.w3.org/2001/XMLSchema#decimal/"
    

        
      Vederlag : identifikator
        
          
    
        
        
        Vederlag --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [belop](belop.md) | 0..1 <br/> [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) | Monetært beløp |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [vederlager](vederlager.md) | range | [Vederlag](vederlag.md) |
| [Aksjeoverdragelse](aksjeoverdragelse.md) | [kan_ha_vederlag](kan_ha_vederlag.md) | range | [Vederlag](vederlag.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:Vederlag |
| native | aksje:Vederlag |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vederlag
description: Vederlag knytt til ei aksjeoverdraging.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- belop

```
</details>

### Induced

<details>
```yaml
name: Vederlag
description: Vederlag knytt til ei aksjeoverdraging.
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
    owner: Vederlag
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
  belop:
    name: belop
    description: Monetært beløp.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    alias: belop
    owner: Vederlag
    domain_of:
    - Utdeling
    - Vederlag
    - InnbetaltAksjekapital
    - InnbetaltOverkurs
    range: decimal
    inlined: true

```
</details>