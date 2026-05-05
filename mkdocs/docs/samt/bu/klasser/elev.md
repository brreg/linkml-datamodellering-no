

# Class: Elev 


_En person som går på skole_





URI: [samtbuskole:Elev](https://example.no/ontology/skole#Elev)





```mermaid
 classDiagram
    class Elev
    click Elev href "../Elev/"
      Person <|-- Elev
        click Person href "../Person/"
      
      Elev : horer_til_basisgruppe
        
          
    
        
        
        Elev --> "0..1" Basisgruppe : horer_til_basisgruppe
        click Basisgruppe href "../Basisgruppe/"
    

        
      Elev : identifikator
        
      Elev : navn
        
      
```





## Inheritance
* [Person](person.md)
    * **Elev**


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [horer_til_basisgruppe](horer_til_basisgruppe.md) | 0..1 <br/> [Basisgruppe](basisgruppe.md) | Basisgruppe elev tilhører |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [identifikator](identifikator.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | Global identifikator (CURIE/URI) | [Person](person.md) |
| [navn](navn.md) | 0..1 <br/> [String](string.md) | Namn på ressursen | [Person](person.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [elever](elever.md) | range | [Elev](elev.md) |
| [Elev](elev.md) | [horer_til_basisgruppe](horer_til_basisgruppe.md) | domain | [Elev](elev.md) |
| [Kontaktlaerer](kontaktlaerer.md) | [har_saerlig_ansvar_for](har_saerlig_ansvar_for.md) | range | [Elev](elev.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:Elev |
| native | samtbuskole:Elev |
| close | schema:Student |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Elev
description: En person som går på skole
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- schema:Student
is_a: Person
slots:
- horer_til_basisgruppe

```
</details>

### Induced

<details>
```yaml
name: Elev
description: En person som går på skole
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- schema:Student
is_a: Person
attributes:
  horer_til_basisgruppe:
    name: horer_til_basisgruppe
    description: Basisgruppe elev tilhører
    from_schema: https://example.no/ontology/samt-bu-skole
    close_mappings:
    - schema:memberOf
    rank: 1000
    domain: Elev
    alias: horer_til_basisgruppe
    owner: Elev
    domain_of:
    - Elev
    range: Basisgruppe
  identifikator:
    name: identifikator
    description: Global identifikator (CURIE/URI).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: identifikator
    owner: Elev
    domain_of:
    - Containerklasse
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: uriorcurie
    required: true
  navn:
    name: navn
    description: Namn på ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    alias: navn
    owner: Elev
    domain_of:
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: string

```
</details>