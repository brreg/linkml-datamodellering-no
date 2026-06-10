

# Class: PartitivRelasjon 


_Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep._





URI: [skosno:PartitiveConceptRelation](https://data.norge.no/vocabulary/skosno#PartitiveConceptRelation)





```mermaid
 classDiagram
    class PartitivRelasjon
    click PartitivRelasjon href "../PartitivRelasjon/"
      PartitivRelasjon : beskrivelse
        
          
    
        
        
        PartitivRelasjon --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      PartitivRelasjon : har_heilskapleg_omgrep
        
          
    
        
        
        PartitivRelasjon --> "*" Begrep : har_heilskapleg_omgrep
        click Begrep href "../Begrep/"
    

        
      PartitivRelasjon : har_partitivt_omgrep
        
          
    
        
        
        PartitivRelasjon --> "*" Begrep : har_partitivt_omgrep
        click Begrep href "../Begrep/"
    

        
      PartitivRelasjon : id
        
          
    
        
        
        PartitivRelasjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
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
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Begrep](begrep.md) | [har_partitiv_relasjon](har_partitiv_relasjon.md) | range | [PartitivRelasjon](partitivrelasjon.md) |
| [BegrepContainer](begrepcontainer.md) | [partitive_relasjonar](partitive_relasjonar.md) | range | [PartitivRelasjon](partitivrelasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skosno:PartitiveConceptRelation |
| native | https://data.norge.no/ap-no/skos-ap-no/PartitivRelasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PartitivRelasjon
description: Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep.
from_schema: https://data.norge.no/ap-no/skos-ap-no
slots:
- id
- har_partitivt_omgrep
- har_heilskapleg_omgrep
- beskrivelse
slot_usage:
  har_partitivt_omgrep:
    name: har_partitivt_omgrep
    in_subset:
    - Obligatorisk
  har_heilskapleg_omgrep:
    name: har_heilskapleg_omgrep
    in_subset:
    - Obligatorisk
  beskrivelse:
    name: beskrivelse
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
from_schema: https://data.norge.no/ap-no/skos-ap-no
slot_usage:
  har_partitivt_omgrep:
    name: har_partitivt_omgrep
    in_subset:
    - Obligatorisk
  har_heilskapleg_omgrep:
    name: har_heilskapleg_omgrep
    in_subset:
    - Obligatorisk
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
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
    from_schema: https://data.norge.no/ap-no/skos-ap-no
    slot_uri: skosno:hasPartitiveConcept
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
    from_schema: https://data.norge.no/ap-no/skos-ap-no
    slot_uri: skosno:hasComprehensiveConcept
    owner: PartitivRelasjon
    domain_of:
    - PartitivRelasjon
    range: Begrep
    multivalued: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: PartitivRelasjon
    domain_of:
    - GeneriskRelasjon
    - PartitivRelasjon
    - Samling
    range: LangString
    multivalued: true
class_uri: skosno:PartitiveConceptRelation

```
</details>