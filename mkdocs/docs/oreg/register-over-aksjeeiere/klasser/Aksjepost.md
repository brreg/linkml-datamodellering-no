

# Class: Aksjepost 


_Samling aksjar eigd av ein aksjeeigar._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjepost](https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjepost)





```mermaid
 classDiagram
    class Aksjepost
    click Aksjepost href "../Aksjepost/"
      Aksjepost : gjelder_aksjer_i_aksjeklasse
        
          
    
        
        
        Aksjepost --> "0..1" Aksjeklasse : gjelder_aksjer_i_aksjeklasse
        click Aksjeklasse href "../Aksjeklasse/"
    

        
      Aksjepost : har_antall_aksjer
        
          
    
        
        
        Aksjepost --> "0..1" Integer : har_antall_aksjer
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
      Aksjepost : identifikator
        
          
    
        
        
        Aksjepost --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [har_antall_aksjer](har_antall_aksjer.md) | 0..1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | Tal aksjar |
| [gjelder_aksjer_i_aksjeklasse](gjelder_aksjer_i_aksjeklasse.md) | 0..1 <br/> [Aksjeklasse](aksjeklasse.md) | Rettigheiter knytt til aksjeklassen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [aksjeposter](aksjeposter.md) | range | [Aksjepost](aksjepost.md) |
| [Eierposisjon](eierposisjon.md) | [gjelder_aksjepost](gjelder_aksjepost.md) | range | [Aksjepost](aksjepost.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjepost |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjepost |




## Examples
### Example: Aksjepost-Aksjepost1

```yaml
identifikator: aksje:Aksjepost1
har_antall_aksjer: 300
gjelder_aksjer_i_aksjeklasse: aksje:Aksjeklasse1

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjepost
description: Samling aksjar eigd av ein aksjeeigar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- har_antall_aksjer
- gjelder_aksjer_i_aksjeklasse

```
</details>

### Induced

<details>
```yaml
name: Aksjepost
description: Samling aksjar eigd av ein aksjeeigar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    owner: Aksjepost
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
  har_antall_aksjer:
    name: har_antall_aksjer
    description: Tal aksjar.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    owner: Aksjepost
    domain_of:
    - Aksjekapital
    - Aksjepost
    range: integer
    inlined: true
  gjelder_aksjer_i_aksjeklasse:
    name: gjelder_aksjer_i_aksjeklasse
    description: Rettigheiter knytt til aksjeklassen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    owner: Aksjepost
    domain_of:
    - Aksjeeierrettighet
    - Aksjepost
    range: Aksjeklasse

```
</details>