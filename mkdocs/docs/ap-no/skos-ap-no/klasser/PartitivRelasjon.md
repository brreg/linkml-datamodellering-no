

# Class: PartitivRelasjon 


_Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep._





URI: [skosno:PartitiveConceptRelation](https://data.norge.no/vocabulary/skosno#PartitiveConceptRelation)





```mermaid
 classDiagram
    class PartitivRelasjon
    click PartitivRelasjon href "../PartitivRelasjon/"
      PartitivRelasjon : har_heilskapleg_omgrep
        
          
    
        
        
        PartitivRelasjon --> "*" Begrep : har_heilskapleg_omgrep
        click Begrep href "../Begrep/"
    

        
      PartitivRelasjon : har_partitivt_omgrep
        
          
    
        
        
        PartitivRelasjon --> "*" Begrep : har_partitivt_omgrep
        click Begrep href "../Begrep/"
    

        
      PartitivRelasjon : id
        
          
    
        
        
        PartitivRelasjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      PartitivRelasjon : inndelingskriterium
        
          
    
        
        
        PartitivRelasjon --> "*" LangString : inndelingskriterium
        click LangString href "../LangString/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [skosno:PartitiveConceptRelation](https://data.norge.no/vocabulary/skosno#PartitiveConceptRelation) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_partitivt_omgrep](har_partitivt_omgrep.md) | * <br/> [Begrep](begrep.md) | Delomgrepet i ein partitiv relasjon (skosno:hasPartitiveConcept) |
| [har_heilskapleg_omgrep](har_heilskapleg_omgrep.md) | * <br/> [Begrep](begrep.md) | Heilskapleg omgrep i ein partitiv relasjon (skosno:hasComprehensiveConcept) |





  
  

  
  

  
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [inndelingskriterium](inndelingskriterium.md) | * <br/> [LangString](langstring.md) | Inndelingskriterium for ein generisk eller partitiv relasjon (dct:description... |





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Begrep](begrep.md) | [har_partitiv_relasjon](har_partitiv_relasjon.md) | range | [PartitivRelasjon](partitivrelasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skosno:PartitiveConceptRelation |
| native | https://data.norge.no/linkml/skos-ap-no/PartitivRelasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PartitivRelasjon
description: Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep.
from_schema: https://data.norge.no/linkml/skos-ap-no
rank: 1000
slots:
- id
- har_partitivt_omgrep
- har_heilskapleg_omgrep
- inndelingskriterium
slot_usage:
  har_partitivt_omgrep:
    name: har_partitivt_omgrep
    in_subset:
    - Obligatorisk
  har_heilskapleg_omgrep:
    name: har_heilskapleg_omgrep
    in_subset:
    - Obligatorisk
  inndelingskriterium:
    name: inndelingskriterium
    in_subset:
    - Anbefalt
class_uri: skosno:PartitiveConceptRelation

```
</details>

### Induced

<details>
```yaml
name: PartitivRelasjon
description: Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep.
from_schema: https://data.norge.no/linkml/skos-ap-no
rank: 1000
slot_usage:
  har_partitivt_omgrep:
    name: har_partitivt_omgrep
    in_subset:
    - Obligatorisk
  har_heilskapleg_omgrep:
    name: har_heilskapleg_omgrep
    in_subset:
    - Obligatorisk
  inndelingskriterium:
    name: inndelingskriterium
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    alias: id
    owner: PartitivRelasjon
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Organisasjon
    - VCardKontakt
    - Begrep
    - Definisjon
    - AssosiativRelasjon
    - GeneriskRelasjon
    - PartitivRelasjon
    - Samling
    range: uriorcurie
    required: true
  har_partitivt_omgrep:
    name: har_partitivt_omgrep
    description: Delomgrepet i ein partitiv relasjon (skosno:hasPartitiveConcept).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/skos-ap-no
    rank: 1000
    slot_uri: skosno:hasPartitiveConcept
    alias: har_partitivt_omgrep
    owner: PartitivRelasjon
    domain_of:
    - PartitivRelasjon
    range: Begrep
    multivalued: true
  har_heilskapleg_omgrep:
    name: har_heilskapleg_omgrep
    description: Heilskapleg omgrep i ein partitiv relasjon (skosno:hasComprehensiveConcept).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/skos-ap-no
    rank: 1000
    slot_uri: skosno:hasComprehensiveConcept
    alias: har_heilskapleg_omgrep
    owner: PartitivRelasjon
    domain_of:
    - PartitivRelasjon
    range: Begrep
    multivalued: true
  inndelingskriterium:
    name: inndelingskriterium
    description: Inndelingskriterium for ein generisk eller partitiv relasjon (dct:description).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/skos-ap-no
    rank: 1000
    slot_uri: dct:description
    alias: inndelingskriterium
    owner: PartitivRelasjon
    domain_of:
    - GeneriskRelasjon
    - PartitivRelasjon
    range: LangString
    multivalued: true
class_uri: skosno:PartitiveConceptRelation

```
</details>