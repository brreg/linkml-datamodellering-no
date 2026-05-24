

# Class: Aksjeinnskudd 


_Innskot knytt til aksjar i samband med selskapshending._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeinnskudd](https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeinnskudd)





```mermaid
 classDiagram
    class Aksjeinnskudd
    click Aksjeinnskudd href "../Aksjeinnskudd/"
      Aksjeinnskudd : gjelder_innbetalt_aksjekapital
        
          
    
        
        
        Aksjeinnskudd --> "0..1" Decimal : gjelder_innbetalt_aksjekapital
        click Decimal href "../http://www.w3.org/2001/XMLSchema#decimal/"
    

        
      Aksjeinnskudd : gjelder_innbetalt_overkurs
        
          
    
        
        
        Aksjeinnskudd --> "0..1" Decimal : gjelder_innbetalt_overkurs
        click Decimal href "../http://www.w3.org/2001/XMLSchema#decimal/"
    

        
      Aksjeinnskudd : identifikator
        
          
    
        
        
        Aksjeinnskudd --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [gjelder_innbetalt_aksjekapital](gjelder_innbetalt_aksjekapital.md) | 0..1 <br/> [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) | Innbetalt aksjekapital |
| [gjelder_innbetalt_overkurs](gjelder_innbetalt_overkurs.md) | 0..1 <br/> [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) | Innbetalt overkurs |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [aksjeinnskudder](aksjeinnskudder.md) | range | [Aksjeinnskudd](aksjeinnskudd.md) |
| [Selskapshendelse](selskapshendelse.md) | [kan_ha_aksjeinnskudd](kan_ha_aksjeinnskudd.md) | range | [Aksjeinnskudd](aksjeinnskudd.md) |
| [Aksjeinnskudd](aksjeinnskudd.md) | [gjelder_innbetalt_aksjekapital](gjelder_innbetalt_aksjekapital.md) | domain | [Aksjeinnskudd](aksjeinnskudd.md) |
| [Aksjeinnskudd](aksjeinnskudd.md) | [gjelder_innbetalt_overkurs](gjelder_innbetalt_overkurs.md) | domain | [Aksjeinnskudd](aksjeinnskudd.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeinnskudd |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeinnskudd |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjeinnskudd
description: Innskot knytt til aksjar i samband med selskapshending.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- gjelder_innbetalt_aksjekapital
- gjelder_innbetalt_overkurs

```
</details>

### Induced

<details>
```yaml
name: Aksjeinnskudd
description: Innskot knytt til aksjar i samband med selskapshending.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    owner: Aksjeinnskudd
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
  gjelder_innbetalt_aksjekapital:
    name: gjelder_innbetalt_aksjekapital
    description: Innbetalt aksjekapital.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksjeinnskudd
    owner: Aksjeinnskudd
    domain_of:
    - Aksjeinnskudd
    range: decimal
  gjelder_innbetalt_overkurs:
    name: gjelder_innbetalt_overkurs
    description: Innbetalt overkurs.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksjeinnskudd
    owner: Aksjeinnskudd
    domain_of:
    - Aksjeinnskudd
    range: decimal

```
</details>