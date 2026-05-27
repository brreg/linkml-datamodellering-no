

# Class: AssosiativRelasjon 


_Ein assosiativ relasjon mellom to omgrep._





URI: [skosno:AssociativeConceptRelation](https://data.norge.no/vocabulary/skosno#AssociativeConceptRelation)





```mermaid
 classDiagram
    class AssosiativRelasjon
    click AssosiativRelasjon href "../AssosiativRelasjon/"
      AssosiativRelasjon : id
        
          
    
        
        
        AssosiativRelasjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      AssosiativRelasjon : relasjontype
        
          
    
        
        
        AssosiativRelasjon --> "1" LangString : relasjontype
        click LangString href "../LangString/"
    

        
      AssosiativRelasjon : til_omgrep
        
          
    
        
        
        AssosiativRelasjon --> "1..*" Begrep : til_omgrep
        click Begrep href "../Begrep/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [skosno:AssociativeConceptRelation](https://data.norge.no/vocabulary/skosno#AssociativeConceptRelation) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [til_omgrep](til_omgrep.md) | 1..* <br/> [Begrep](begrep.md) | Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept) |
| [relasjontype](relasjontype.md) | 1 <br/> [LangString](langstring.md) | Rolle eller type av den assosiative relasjonen (skosno:relationRole) |





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Begrep](begrep.md) | [er_fra_omgrep_i](er_fra_omgrep_i.md) | range | [AssosiativRelasjon](assosiativrelasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skosno:AssociativeConceptRelation |
| native | https://data.norge.no/ap-no/skos-ap-no/AssosiativRelasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AssosiativRelasjon
description: Ein assosiativ relasjon mellom to omgrep.
from_schema: https://data.norge.no/ap-no/skos-ap-no
rank: 1000
slots:
- id
- til_omgrep
- relasjontype
slot_usage:
  til_omgrep:
    name: til_omgrep
    in_subset:
    - Obligatorisk
    required: true
  relasjontype:
    name: relasjontype
    in_subset:
    - Obligatorisk
    required: true
class_uri: skosno:AssociativeConceptRelation

```
</details>

### Induced

<details>
```yaml
name: AssosiativRelasjon
description: Ein assosiativ relasjon mellom to omgrep.
from_schema: https://data.norge.no/ap-no/skos-ap-no
rank: 1000
slot_usage:
  til_omgrep:
    name: til_omgrep
    in_subset:
    - Obligatorisk
    required: true
  relasjontype:
    name: relasjontype
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: AssosiativRelasjon
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
  til_omgrep:
    name: til_omgrep
    description: Til-omgrepet i den assosiative relasjonen (skosno:hasToConcept).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/skos-ap-no
    rank: 1000
    slot_uri: skosno:hasToConcept
    owner: AssosiativRelasjon
    domain_of:
    - AssosiativRelasjon
    range: Begrep
    required: true
    multivalued: true
  relasjontype:
    name: relasjontype
    description: Rolle eller type av den assosiative relasjonen (skosno:relationRole).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/skos-ap-no
    rank: 1000
    slot_uri: skosno:relationRole
    owner: AssosiativRelasjon
    domain_of:
    - AssosiativRelasjon
    range: LangString
    required: true
class_uri: skosno:AssociativeConceptRelation

```
</details>