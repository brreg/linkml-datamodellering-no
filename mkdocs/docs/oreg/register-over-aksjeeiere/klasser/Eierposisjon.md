

# Class: Eierposisjon 


_Eierens samla posisjon i eit selskap._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:Eierposisjon](https://data.norge.no/linkml/register-over-aksjeeiere/:Eierposisjon)





```mermaid
 classDiagram
    class Eierposisjon
    click Eierposisjon href "../Eierposisjon/"
      Eierposisjon : gjelder_aksjepost
        
          
    
        
        
        Eierposisjon --> "0..1" Aksjepost : gjelder_aksjepost
        click Aksjepost href "../Aksjepost/"
    

        
      Eierposisjon : identifikator
        
          
    
        
        
        Eierposisjon --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [gjelder_aksjepost](gjelder_aksjepost.md) | 0..1 <br/> [Aksjepost](aksjepost.md) | Aksjepost som inngår i eigarposisjonen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [eierposisjoner](eierposisjoner.md) | range | [Eierposisjon](eierposisjon.md) |
| [Aksjeeier](aksjeeier.md) | [har_eierposisjon](har_eierposisjon.md) | range | [Eierposisjon](eierposisjon.md) |
| [Eierposisjon](eierposisjon.md) | [gjelder_aksjepost](gjelder_aksjepost.md) | domain | [Eierposisjon](eierposisjon.md) |
| [Utbytte](utbytte.md) | [er_basert_paa_eierposisjon](er_basert_paa_eierposisjon.md) | range | [Eierposisjon](eierposisjon.md) |
| [Eierskapstransaksjon](eierskapstransaksjon.md) | [paavirker_eierposisjon](paavirker_eierposisjon.md) | range | [Eierposisjon](eierposisjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:Eierposisjon |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:Eierposisjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Eierposisjon
description: Eierens samla posisjon i eit selskap.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- gjelder_aksjepost

```
</details>

### Induced

<details>
```yaml
name: Eierposisjon
description: Eierens samla posisjon i eit selskap.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    owner: Eierposisjon
    domain_of:
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
  gjelder_aksjepost:
    name: gjelder_aksjepost
    description: Aksjepost som inngår i eigarposisjonen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Eierposisjon
    owner: Eierposisjon
    domain_of:
    - Eierposisjon
    range: Aksjepost

```
</details>