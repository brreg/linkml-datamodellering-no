

# Class: InnbetaltOverkurs 


_Innbetalt overkurs utover pålydande._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltOverkurs](https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltOverkurs)





```mermaid
 classDiagram
    class InnbetaltOverkurs
    click InnbetaltOverkurs href "../InnbetaltOverkurs/"
      InnbetaltOverkurs : belop
        
          
    
        
        
        InnbetaltOverkurs --> "0..1" Decimal : belop
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
| [AksjeeierContainer](aksjeeiercontainer.md) | [innbetalt_overkurser](innbetalt_overkurser.md) | range | [InnbetaltOverkurs](innbetaltoverkurs.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltOverkurs |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:InnbetaltOverkurs |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InnbetaltOverkurs
description: Innbetalt overkurs utover pålydande.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
slots:
- belop

```
</details>

### Induced

<details>
```yaml
name: InnbetaltOverkurs
description: Innbetalt overkurs utover pålydande.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
attributes:
  belop:
    name: belop
    description: Monetært beløp.
    from_schema: https://example.no/ontology/aksje-eierskap
    rank: 1000
    owner: InnbetaltOverkurs
    domain_of:
    - Utdeling
    - Vederlag
    - InnbetaltAksjekapital
    - InnbetaltOverkurs
    range: decimal
    inlined: true

```
</details>