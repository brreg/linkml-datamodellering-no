

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
    

        
      Elev : id
        
          
    
        
        
        Elev --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Elev : navn
        
          
    
        
        
        Elev --> "0..1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
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
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Person](person.md) |
| [navn](navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på ressursen | [Person](person.md) |





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
rank: 1000
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
rank: 1000
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
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    alias: id
    owner: Elev
    domain_of:
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
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