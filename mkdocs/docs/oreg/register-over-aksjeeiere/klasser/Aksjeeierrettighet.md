

# Class: Aksjeeierrettighet 


_Rettigheiter knytt til aksjar, til dømes stemmerett._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeeierrettighet](https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeeierrettighet)





```mermaid
 classDiagram
    class Aksjeeierrettighet
    click Aksjeeierrettighet href "../Aksjeeierrettighet/"
      Aksjeeierrettighet : beskrivelse
        
          
    
        
        
        Aksjeeierrettighet --> "0..1" String : beskrivelse
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Aksjeeierrettighet : gjelder_aksjer_i_aksjeklasse
        
          
    
        
        
        Aksjeeierrettighet --> "0..1" Aksjeklasse : gjelder_aksjer_i_aksjeklasse
        click Aksjeklasse href "../Aksjeklasse/"
    

        
      Aksjeeierrettighet : identifikator
        
          
    
        
        
        Aksjeeierrettighet --> "1" Uriorcurie : identifikator
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Global identifikator for instansen |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg forklaring av instansen |
| [gjelder_aksjer_i_aksjeklasse](gjelder_aksjer_i_aksjeklasse.md) | 0..1 <br/> [Aksjeklasse](aksjeklasse.md) | Rettigheiter knytt til aksjeklassen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [aksjeeierrettigheter](aksjeeierrettigheter.md) | range | [Aksjeeierrettighet](aksjeeierrettighet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeeierrettighet |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:Aksjeeierrettighet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjeeierrettighet
description: Rettigheiter knytt til aksjar, til dømes stemmerett.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- identifikator
- beskrivelse
- gjelder_aksjer_i_aksjeklasse

```
</details>

### Induced

<details>
```yaml
name: Aksjeeierrettighet
description: Rettigheiter knytt til aksjar, til dømes stemmerett.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    owner: Aksjeeierrettighet
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
  beskrivelse:
    name: beskrivelse
    description: Tekstleg forklaring av instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    owner: Aksjeeierrettighet
    domain_of:
    - Aksjeeierrettighet
    range: string
    inlined: true
  gjelder_aksjer_i_aksjeklasse:
    name: gjelder_aksjer_i_aksjeklasse
    description: Rettigheiter knytt til aksjeklassen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    owner: Aksjeeierrettighet
    domain_of:
    - Aksjeeierrettighet
    - Aksjepost
    range: Aksjeklasse

```
</details>