

# Class: Aksjeeierrettighet 


_Rettigheiter knytt til aksjar, til dømes stemmerett._





URI: [aksje:Aksjeeierrettighet](https://example.no/ontology/aksje#Aksjeeierrettighet)





```mermaid
 classDiagram
    class Aksjeeierrettighet
    click Aksjeeierrettighet href "../Aksjeeierrettighet/"
      Aksjeeierrettighet : beskrivelse
        
      Aksjeeierrettighet : gjelder_aksjer_i_aksjeklasse
        
          
    
        
        
        Aksjeeierrettighet --> "0..1" Aksjeklasse : gjelder_aksjer_i_aksjeklasse
        click Aksjeklasse href "../Aksjeklasse/"
    

        
      Aksjeeierrettighet : identifikator
        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Global identifikator for instansen |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [String](String.md) | Tekstleg forklaring av instansen |
| [gjelder_aksjer_i_aksjeklasse](gjelder_aksjer_i_aksjeklasse.md) | 0..1 <br/> [Aksjeklasse](Aksjeklasse.md) | Rettigheiter knytt til aksjeklassen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](Containerklasse.md) | [aksjeeierrettigheter](aksjeeierrettigheter.md) | range | [Aksjeeierrettighet](Aksjeeierrettighet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:Aksjeeierrettighet |
| native | aksje:Aksjeeierrettighet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aksjeeierrettighet
description: Rettigheiter knytt til aksjar, til dømes stemmerett.
from_schema: https://example.no/ontology/aksje-eierskap
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
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Aksjeeierrettighet
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
  beskrivelse:
    name: beskrivelse
    description: Tekstleg forklaring av instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    alias: beskrivelse
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
    alias: gjelder_aksjer_i_aksjeklasse
    owner: Aksjeeierrettighet
    domain_of:
    - Aksjeeierrettighet
    - Aksjepost
    range: Aksjeklasse

```
</details>