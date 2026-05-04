

# Class: Eierposisjon 


_Eierens samla posisjon i eit selskap._





URI: [aksje:Eierposisjon](https://example.no/ontology/aksje#Eierposisjon)





```mermaid
 classDiagram
    class Eierposisjon
    click Eierposisjon href "../Eierposisjon/"
      Eierposisjon : gjelder_aksjepost
        
          
    
        
        
        Eierposisjon --> "0..1" Aksjepost : gjelder_aksjepost
        click Aksjepost href "../Aksjepost/"
    

        
      Eierposisjon : identifikator
        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Global identifikator for instansen |
| [gjelder_aksjepost](gjelder_aksjepost.md) | 0..1 <br/> [Aksjepost](Aksjepost.md) | Aksjepost som inngår i eigarposisjonen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](Containerklasse.md) | [eierposisjoner](eierposisjoner.md) | range | [Eierposisjon](Eierposisjon.md) |
| [Aksjeeier](Aksjeeier.md) | [har_eierposisjon](har_eierposisjon.md) | range | [Eierposisjon](Eierposisjon.md) |
| [Eierposisjon](Eierposisjon.md) | [gjelder_aksjepost](gjelder_aksjepost.md) | domain | [Eierposisjon](Eierposisjon.md) |
| [Utbytte](Utbytte.md) | [er_basert_paa_eierposisjon](er_basert_paa_eierposisjon.md) | range | [Eierposisjon](Eierposisjon.md) |
| [Eierskapstransaksjon](Eierskapstransaksjon.md) | [paavirker_eierposisjon](paavirker_eierposisjon.md) | range | [Eierposisjon](Eierposisjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:Eierposisjon |
| native | aksje:Eierposisjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Eierposisjon
description: Eierens samla posisjon i eit selskap.
from_schema: https://example.no/ontology/aksje-eierskap
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
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Eierposisjon
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
  gjelder_aksjepost:
    name: gjelder_aksjepost
    description: Aksjepost som inngår i eigarposisjonen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Eierposisjon
    alias: gjelder_aksjepost
    owner: Eierposisjon
    domain_of:
    - Eierposisjon
    range: Aksjepost

```
</details>