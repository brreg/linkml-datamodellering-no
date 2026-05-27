

# Class: Aksje 


_Ei enkelt aksje utstedt av eit aksjeselskap._





URI: [https://data.norge.no/oreg/register-over-aksjeeiere/:Aksje](https://data.norge.no/oreg/register-over-aksjeeiere/:Aksje)





```mermaid
 classDiagram
    class Aksje
    click Aksje href "../Aksje/"
      Aksje : har_palydende_belop
        
          
    
        
        
        Aksje --> "0..1" Decimal : har_palydende_belop
        click Decimal href "../http://www.w3.org/2001/XMLSchema#decimal/"
    

        
      Aksje : identifikator
        
          
    
        
        
        Aksje --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Aksje : tilhorer_aksjeklasse
        
          
    
        
        
        Aksje --> "0..1" Aksjeklasse : tilhorer_aksjeklasse
        click Aksjeklasse href "../Aksjeklasse/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [har_palydende_belop](har_palydende_belop.md) | 0..1 <br/> [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) | Pålydande verdi for aksja |
| [tilhorer_aksjeklasse](tilhorer_aksjeklasse.md) | 0..1 <br/> [Aksjeklasse](aksjeklasse.md) | Klassen aksja høyrer til |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [aksjer](aksjer.md) | range | [Aksje](aksje.md) |
| [Aksjeselskap](aksjeselskap.md) | [utsteder_aksje](utsteder_aksje.md) | range | [Aksje](aksje.md) |
| [Aksje](aksje.md) | [har_palydende_belop](har_palydende_belop.md) | domain | [Aksje](aksje.md) |
| [Aksje](aksje.md) | [tilhorer_aksjeklasse](tilhorer_aksjeklasse.md) | domain | [Aksje](aksje.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/oreg/register-over-aksjeeiere/:Aksje |
| native | https://data.norge.no/oreg/register-over-aksjeeiere/:Aksje |




## Examples
### Example: Aksje-Aksje1

```yaml
identifikator: aksje:Aksje1
har_palydende_belop: 100
tilhorer_aksjeklasse: aksje:Aksjeklasse1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksje
description: Ei enkelt aksje utstedt av eit aksjeselskap.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- har_palydende_belop
- tilhorer_aksjeklasse

```
</details>

### Induced

<details>
```yaml
name: Aksje
description: Ei enkelt aksje utstedt av eit aksjeselskap.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    owner: Aksje
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
  har_palydende_belop:
    name: har_palydende_belop
    description: Pålydande verdi for aksja.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksje
    owner: Aksje
    domain_of:
    - Aksje
    range: decimal
    inlined: true
  tilhorer_aksjeklasse:
    name: tilhorer_aksjeklasse
    description: Klassen aksja høyrer til.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Aksje
    owner: Aksje
    domain_of:
    - Aksje
    range: Aksjeklasse

```
</details>