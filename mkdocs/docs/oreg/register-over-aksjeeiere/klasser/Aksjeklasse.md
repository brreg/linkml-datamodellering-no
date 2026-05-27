

# Class: Aksjeklasse 


_Klasse aksjar høyrer til, med eigne rettigheiter._





URI: [https://data.norge.no/oreg/register-over-aksjeeiere/:Aksjeklasse](https://data.norge.no/oreg/register-over-aksjeeiere/:Aksjeklasse)





```mermaid
 classDiagram
    class Aksjeklasse
    click Aksjeklasse href "../Aksjeklasse/"
      Aksjeklasse : identifikator
        
          
    
        
        
        Aksjeklasse --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Aksjeklasse : navn
        
          
    
        
        
        Aksjeklasse --> "0..1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [navn](navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på instansen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [aksjeklasser](aksjeklasser.md) | range | [Aksjeklasse](aksjeklasse.md) |
| [Aksje](aksje.md) | [tilhorer_aksjeklasse](tilhorer_aksjeklasse.md) | range | [Aksjeklasse](aksjeklasse.md) |
| [Aksjeeierrettighet](aksjeeierrettighet.md) | [gjelder_aksjer_i_aksjeklasse](gjelder_aksjer_i_aksjeklasse.md) | range | [Aksjeklasse](aksjeklasse.md) |
| [Aksjepost](aksjepost.md) | [gjelder_aksjer_i_aksjeklasse](gjelder_aksjer_i_aksjeklasse.md) | range | [Aksjeklasse](aksjeklasse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/oreg/register-over-aksjeeiere/:Aksjeklasse |
| native | https://data.norge.no/oreg/register-over-aksjeeiere/:Aksjeklasse |




## Examples
### Example: Aksjeklasse-Aksjeklasse1

```yaml
identifikator: aksje:Aksjeklasse1
navn: Ordinær aksje

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjeklasse
description: Klasse aksjar høyrer til, med eigne rettigheiter.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- navn

```
</details>

### Induced

<details>
```yaml
name: Aksjeklasse
description: Klasse aksjar høyrer til, med eigne rettigheiter.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    owner: Aksjeklasse
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
  navn:
    name: navn
    description: Namn på instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    owner: Aksjeklasse
    domain_of:
    - Aksjeselskap
    - Aksjeklasse
    - Aksjeeier
    range: string
    inlined: true

```
</details>