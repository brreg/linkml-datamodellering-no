

# Class: InnbetaltAksjekapital 


_Innbetalt aksjekapital._





URI: [aksje:InnbetaltAksjekapital](https://example.no/ontology/aksje#InnbetaltAksjekapital)





```mermaid
 classDiagram
    class InnbetaltAksjekapital
    click InnbetaltAksjekapital href "../InnbetaltAksjekapital/"
      InnbetaltAksjekapital : belop
        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [belop](belop.md) | 0..1 <br/> [Decimal](Decimal.md) | Monetært beløp |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](Containerklasse.md) | [innbetalt_aksjekapitaler](innbetalt_aksjekapitaler.md) | range | [InnbetaltAksjekapital](InnbetaltAksjekapital.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:InnbetaltAksjekapital |
| native | aksje:InnbetaltAksjekapital |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InnbetaltAksjekapital
description: Innbetalt aksjekapital.
from_schema: https://example.no/ontology/aksje-eierskap
slots:
- belop

```
</details>

### Induced

<details>
```yaml
name: InnbetaltAksjekapital
description: Innbetalt aksjekapital.
from_schema: https://example.no/ontology/aksje-eierskap
attributes:
  belop:
    name: belop
    description: Monetært beløp.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    alias: belop
    owner: InnbetaltAksjekapital
    domain_of:
    - Utdeling
    - Vederlag
    - InnbetaltAksjekapital
    - InnbetaltOverkurs
    range: decimal
    inlined: true

```
</details>