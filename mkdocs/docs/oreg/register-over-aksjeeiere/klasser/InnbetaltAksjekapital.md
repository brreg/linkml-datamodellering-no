

# Class: InnbetaltAksjekapital 


_Innbetalt aksjekapital._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltAksjekapital](https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltAksjekapital)





```mermaid
 classDiagram
    class InnbetaltAksjekapital
    click InnbetaltAksjekapital href "../InnbetaltAksjekapital/"
      InnbetaltAksjekapital : belop
        
          
    
        
        
        InnbetaltAksjekapital --> "0..1" Decimal : belop
        click Decimal href "../http://www.w3.org/2001/XMLSchema#decimal/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [belop](belop.md) | 0..1 <br/> [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) | Monetært beløp |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AksjeeierContainer](aksjeeiercontainer.md) | [innbetalt_aksjekapitaler](innbetalt_aksjekapitaler.md) | range | [InnbetaltAksjekapital](innbetaltaksjekapital.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltAksjekapital |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltAksjekapital |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InnbetaltAksjekapital
description: Innbetalt aksjekapital.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
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
rank: 1000
attributes:
  belop:
    name: belop
    description: Monetært beløp.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
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