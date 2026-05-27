

# Class: Klassifikasjonsnivaa 


_Eit nivå i ein klassifikasjon (xkos:ClassificationLevel)._





URI: [xkos:ClassificationLevel](http://rdf-vocabulary.ddialliance.org/xkos#ClassificationLevel)





```mermaid
 classDiagram
    class Klassifikasjonsnivaa
    click Klassifikasjonsnivaa href "../Klassifikasjonsnivaa/"
      Klassifikasjonsnivaa : har_medlem
        
          
    
        
        
        Klassifikasjonsnivaa --> "1..*" Kategori : har_medlem
        click Kategori href "../Kategori/"
    

        
      Klassifikasjonsnivaa : id
        
          
    
        
        
        Klassifikasjonsnivaa --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Klassifikasjonsnivaa : nivaa_djupn
        
          
    
        
        
        Klassifikasjonsnivaa --> "1" NonNegativeInteger : nivaa_djupn
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Klassifikasjonsnivaa : tittel
        
          
    
        
        
        Klassifikasjonsnivaa --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      Klassifikasjonsnivaa : underordna_klassifikasjonsnivaa
        
          
    
        
        
        Klassifikasjonsnivaa --> "*" Klassifikasjonsnivaa : underordna_klassifikasjonsnivaa
        click Klassifikasjonsnivaa href "../Klassifikasjonsnivaa/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [xkos:ClassificationLevel](http://rdf-vocabulary.ddialliance.org/xkos#ClassificationLevel) |


## Eigenskapar







  
  

  
  

  
  
    
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [nivaa_djupn](nivaa_djupn.md) | 1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Djupna (nivånummer) i klassifikasjonsstrukturen (xkos:depth) |
| [har_medlem](har_medlem.md) | 1..* <br/> [Kategori](kategori.md) | Kategoriar som høyrer til dette nivået (skos:member) |





  
  

  
  
    
  

  
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |





  
  

  
  

  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [underordna_klassifikasjonsnivaa](underordna_klassifikasjonsnivaa.md) | * <br/> [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) | Underordna klassifikasjonsnivå (xkos:nextLevel) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Klassifikasjon](klassifikasjon.md) | [forste_nivaa](forste_nivaa.md) | range | [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) |
| [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) | [underordna_klassifikasjonsnivaa](underordna_klassifikasjonsnivaa.md) | range | [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) |
| [Kategori](kategori.md) | [tilhorande_klassifikasjonsnivaa](tilhorande_klassifikasjonsnivaa.md) | range | [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | xkos:ClassificationLevel |
| native | https://data.norge.no/ap-no/xkos-ap-no/Klassifikasjonsnivaa |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Klassifikasjonsnivaa
description: Eit nivå i ein klassifikasjon (xkos:ClassificationLevel).
from_schema: https://data.norge.no/ap-no/xkos-ap-no
rank: 1000
slots:
- id
- tittel
- nivaa_djupn
- har_medlem
- underordna_klassifikasjonsnivaa
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Anbefalt
  nivaa_djupn:
    name: nivaa_djupn
    in_subset:
    - Obligatorisk
    required: true
  har_medlem:
    name: har_medlem
    in_subset:
    - Obligatorisk
    required: true
  underordna_klassifikasjonsnivaa:
    name: underordna_klassifikasjonsnivaa
    in_subset:
    - Valgfri
class_uri: xkos:ClassificationLevel

```
</details>

### Induced

<details>
```yaml
name: Klassifikasjonsnivaa
description: Eit nivå i ein klassifikasjon (xkos:ClassificationLevel).
from_schema: https://data.norge.no/ap-no/xkos-ap-no
rank: 1000
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Anbefalt
  nivaa_djupn:
    name: nivaa_djupn
    in_subset:
    - Obligatorisk
    required: true
  har_medlem:
    name: har_medlem
    in_subset:
    - Obligatorisk
    required: true
  underordna_klassifikasjonsnivaa:
    name: underordna_klassifikasjonsnivaa
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Klassifikasjonsnivaa
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
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Klassifikasjonsnivaa
    domain_of:
    - Klassifikasjon
    - Klassifikasjonsnivaa
    - Klassifikasjonssamanlikning
    range: LangString
    multivalued: true
  nivaa_djupn:
    name: nivaa_djupn
    description: Djupna (nivånummer) i klassifikasjonsstrukturen (xkos:depth).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/xkos-ap-no
    rank: 1000
    slot_uri: xkos:depth
    owner: Klassifikasjonsnivaa
    domain_of:
    - Klassifikasjonsnivaa
    range: NonNegativeInteger
    required: true
  har_medlem:
    name: har_medlem
    description: Kategoriar som høyrer til dette nivået (skos:member).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/xkos-ap-no
    rank: 1000
    slot_uri: skos:member
    owner: Klassifikasjonsnivaa
    domain_of:
    - Klassifikasjonsnivaa
    range: Kategori
    required: true
    multivalued: true
  underordna_klassifikasjonsnivaa:
    name: underordna_klassifikasjonsnivaa
    description: Underordna klassifikasjonsnivå (xkos:nextLevel).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/xkos-ap-no
    rank: 1000
    slot_uri: xkos:nextLevel
    owner: Klassifikasjonsnivaa
    domain_of:
    - Klassifikasjonsnivaa
    range: Klassifikasjonsnivaa
    multivalued: true
class_uri: xkos:ClassificationLevel

```
</details>