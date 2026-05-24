

# Class: Kommune 


_En kommune er et geografisk avgrenset område som utgjør en egen politisk og administrativ enhet innen en statsdannelse._





URI: [samtbuskole:Kommune](https://example.no/ontology/skole#Kommune)





```mermaid
 classDiagram
    class Kommune
    click Kommune href "../Kommune/"
      Skoleeier <|-- Kommune
        click Skoleeier href "../Skoleeier/"
      
      Kommune : id
        
          
    
        
        
        Kommune --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Kommune : kommunenummer
        
          
    
        
        
        Kommune --> "0..1" String : kommunenummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Kommune : navn
        
          
    
        
        
        Kommune --> "0..1" String : navn
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      
```





## Inheritance
* [Skoleeier](skoleeier.md)
    * **Kommune**


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [kommunenummer](kommunenummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Kommunenummer er en nummerrekke som identifiserer kommuner eller kommunefrie ... |




### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen | [Skoleeier](skoleeier.md) |
| [navn](navn.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Namn på ressursen | [Skoleeier](skoleeier.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SamtBuContainer](samtbucontainer.md) | [kommuner](kommuner.md) | range | [Kommune](kommune.md) |










## See Also

* [https://data.norge.no/concepts/5b7fd4f2-39f6-39ed-9540-e6c2491ef633](https://data.norge.no/concepts/5b7fd4f2-39f6-39ed-9540-e6c2491ef633)



## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:Kommune |
| native | samtbuskole:Kommune |
| exact | org:Organization |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kommune
description: En kommune er et geografisk avgrenset område som utgjør en egen politisk
  og administrativ enhet innen en statsdannelse.
from_schema: https://example.no/ontology/samt-bu-skole
see_also:
- https://data.norge.no/concepts/5b7fd4f2-39f6-39ed-9540-e6c2491ef633
exact_mappings:
- org:Organization
rank: 1000
is_a: Skoleeier
slots:
- kommunenummer

```
</details>

### Induced

<details>
```yaml
name: Kommune
description: En kommune er et geografisk avgrenset område som utgjør en egen politisk
  og administrativ enhet innen en statsdannelse.
from_schema: https://example.no/ontology/samt-bu-skole
see_also:
- https://data.norge.no/concepts/5b7fd4f2-39f6-39ed-9540-e6c2491ef633
exact_mappings:
- org:Organization
rank: 1000
is_a: Skoleeier
attributes:
  kommunenummer:
    name: kommunenummer
    description: Kommunenummer er en nummerrekke som identifiserer kommuner eller
      kommunefrie områder.
    from_schema: https://example.no/ontology/samt-bu-skole
    close_mappings:
    - skos:notation
    rank: 1000
    slot_uri: dcat:identifier
    owner: Kommune
    domain_of:
    - Kommune
    range: string
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: Kommune
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
    - SamtBuContainer
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
    owner: Kommune
    domain_of:
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    range: string

```
</details>