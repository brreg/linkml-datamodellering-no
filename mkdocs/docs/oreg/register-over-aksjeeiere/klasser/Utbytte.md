

# Class: Utbytte 


_Utbytte knytt til ein eigarposisjon._





URI: [aksje:Utbytte](https://example.no/ontology/aksje#Utbytte)





```mermaid
 classDiagram
    class Utbytte
    click Utbytte href "../Utbytte/"
      Utbytte : er_basert_paa_eierposisjon
        
          
    
        
        
        Utbytte --> "0..1" Eierposisjon : er_basert_paa_eierposisjon
        click Eierposisjon href "../Eierposisjon/"
    

        
      Utbytte : har_utdeling
        
          
    
        
        
        Utbytte --> "0..1" Utdeling : har_utdeling
        click Utdeling href "../Utdeling/"
    

        
      Utbytte : identifikator
        
      Utbytte : tidspunkt
        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Global identifikator for instansen |
| [tidspunkt](tidspunkt.md) | 0..1 <br/> [Date](Date.md) | Tidspunkt for utbytte/eierskapstransaksjon |
| [har_utdeling](har_utdeling.md) | 0..1 <br/> [Utdeling](Utdeling.md) | Utdeling knytt til utbyttet |
| [er_basert_paa_eierposisjon](er_basert_paa_eierposisjon.md) | 0..1 <br/> [Eierposisjon](Eierposisjon.md) | Utbytte knytt til eigarposisjonen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](Containerklasse.md) | [utbytter](utbytter.md) | range | [Utbytte](Utbytte.md) |
| [Utbytte](Utbytte.md) | [har_utdeling](har_utdeling.md) | domain | [Utbytte](Utbytte.md) |
| [Utbytte](Utbytte.md) | [er_basert_paa_eierposisjon](er_basert_paa_eierposisjon.md) | domain | [Utbytte](Utbytte.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:Utbytte |
| native | aksje:Utbytte |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Utbytte
description: Utbytte knytt til ein eigarposisjon.
from_schema: https://example.no/ontology/aksje-eierskap
slots:
- identifikator
- tidspunkt
- har_utdeling
- er_basert_paa_eierposisjon

```
</details>

### Induced

<details>
```yaml
name: Utbytte
description: Utbytte knytt til ein eigarposisjon.
from_schema: https://example.no/ontology/aksje-eierskap
attributes:
  identifikator:
    name: identifikator
    description: Global identifikator for instansen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Utbytte
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
  tidspunkt:
    name: tidspunkt
    description: Tidspunkt for utbytte/eierskapstransaksjon.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    alias: tidspunkt
    owner: Utbytte
    domain_of:
    - Utbytte
    - Eierskapstransaksjon
    range: date
    inlined: true
  har_utdeling:
    name: har_utdeling
    description: Utdeling knytt til utbyttet.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Utbytte
    alias: har_utdeling
    owner: Utbytte
    domain_of:
    - Utbytte
    range: Utdeling
  er_basert_paa_eierposisjon:
    name: er_basert_paa_eierposisjon
    description: Utbytte knytt til eigarposisjonen.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    domain: Utbytte
    alias: er_basert_paa_eierposisjon
    owner: Utbytte
    domain_of:
    - Utbytte
    range: Eierposisjon

```
</details>