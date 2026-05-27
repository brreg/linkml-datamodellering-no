

# Class: Klassifikasjonssamanlikning 


_Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence)._





URI: [xkos:Correspondence](http://rdf-vocabulary.ddialliance.org/xkos#Correspondence)





```mermaid
 classDiagram
    class Klassifikasjonssamanlikning
    click Klassifikasjonssamanlikning href "../Klassifikasjonssamanlikning/"
      Klassifikasjonssamanlikning : bestar_av
        
          
    
        
        
        Klassifikasjonssamanlikning --> "1..*" Kategorisamanlikning : bestar_av
        click Kategorisamanlikning href "../Kategorisamanlikning/"
    

        
      Klassifikasjonssamanlikning : id
        
          
    
        
        
        Klassifikasjonssamanlikning --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Klassifikasjonssamanlikning : identifikator_literal
        
          
    
        
        
        Klassifikasjonssamanlikning --> "1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Klassifikasjonssamanlikning : samanliknar
        
          
    
        
        
        Klassifikasjonssamanlikning --> "1..*" Klassifikasjon : samanliknar
        click Klassifikasjon href "../Klassifikasjon/"
    

        
      Klassifikasjonssamanlikning : tittel
        
          
    
        
        
        Klassifikasjonssamanlikning --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      Klassifikasjonssamanlikning : utgjevar
        
          
    
        
        
        Klassifikasjonssamanlikning --> "1" Organisasjon : utgjevar
        click Organisasjon href "../Organisasjon/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [xkos:Correspondence](http://rdf-vocabulary.ddialliance.org/xkos#Correspondence) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [identifikator_literal](identifikator_literal.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [utgjevar](utgjevar.md) | 1 <br/> [Organisasjon](organisasjon.md) | Organisasjon som er ansvarleg utgjevar (dct:publisher) |
| [samanliknar](samanliknar.md) | 1..* <br/> [Klassifikasjon](klassifikasjon.md) | Klassifikasjonar som er samanlikna i korrespondansen (xkos:compares) |
| [bestar_av](bestar_av.md) | 1..* <br/> [Kategorisamanlikning](kategorisamanlikning.md) | Kategorisamanlikningar som inngår i klassifikasjonssamanlikninga (xkos:madeOf... |





  
  

  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | xkos:Correspondence |
| native | https://data.norge.no/ap-no/xkos-ap-no/Klassifikasjonssamanlikning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Klassifikasjonssamanlikning
description: Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence).
from_schema: https://data.norge.no/ap-no/xkos-ap-no
rank: 1000
slots:
- id
- identifikator_literal
- tittel
- utgjevar
- samanliknar
- bestar_av
slot_usage:
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Obligatorisk
    required: true
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  utgjevar:
    name: utgjevar
    in_subset:
    - Obligatorisk
    required: true
  samanliknar:
    name: samanliknar
    in_subset:
    - Obligatorisk
    required: true
  bestar_av:
    name: bestar_av
    in_subset:
    - Obligatorisk
    required: true
class_uri: xkos:Correspondence

```
</details>

### Induced

<details>
```yaml
name: Klassifikasjonssamanlikning
description: Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence).
from_schema: https://data.norge.no/ap-no/xkos-ap-no
rank: 1000
slot_usage:
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Obligatorisk
    required: true
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  utgjevar:
    name: utgjevar
    in_subset:
    - Obligatorisk
    required: true
  samanliknar:
    name: samanliknar
    in_subset:
    - Obligatorisk
    required: true
  bestar_av:
    name: bestar_av
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Klassifikasjonssamanlikning
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Klassifikasjon
    - Klassifikasjonsnivaa
    - Kategori
    - Klassifikasjonssamanlikning
    - Kategorisamanlikning
    - Organisasjon
    - Tidsrom
    range: uriorcurie
    required: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: Klassifikasjonssamanlikning
    domain_of:
    - Klassifikasjon
    - Klassifikasjonssamanlikning
    range: string
    required: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Klassifikasjonssamanlikning
    domain_of:
    - Klassifikasjon
    - Klassifikasjonsnivaa
    - Klassifikasjonssamanlikning
    range: LangString
    required: true
    multivalued: true
  utgjevar:
    name: utgjevar
    description: Organisasjon som er ansvarleg utgjevar (dct:publisher).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/xkos-ap-no
    rank: 1000
    slot_uri: dct:publisher
    owner: Klassifikasjonssamanlikning
    domain_of:
    - Klassifikasjon
    - Klassifikasjonssamanlikning
    range: Organisasjon
    required: true
  samanliknar:
    name: samanliknar
    description: Klassifikasjonar som er samanlikna i korrespondansen (xkos:compares).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/xkos-ap-no
    rank: 1000
    slot_uri: xkos:compares
    owner: Klassifikasjonssamanlikning
    domain_of:
    - Klassifikasjonssamanlikning
    range: Klassifikasjon
    required: true
    multivalued: true
  bestar_av:
    name: bestar_av
    description: Kategorisamanlikningar som inngår i klassifikasjonssamanlikninga
      (xkos:madeOf).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/xkos-ap-no
    rank: 1000
    slot_uri: xkos:madeOf
    owner: Klassifikasjonssamanlikning
    domain_of:
    - Klassifikasjonssamanlikning
    range: Kategorisamanlikning
    required: true
    multivalued: true
class_uri: xkos:Correspondence

```
</details>