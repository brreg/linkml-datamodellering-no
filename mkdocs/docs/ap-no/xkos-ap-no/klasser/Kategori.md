

# Class: Kategori 


_Ein kategori i ein klassifikasjon (skos:Concept)._





URI: [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept)





```mermaid
 classDiagram
    class Kategori
    click Kategori href "../Kategori/"
      Kategori : anbefalt_term
        
      Kategori : er_eksklusivt_ekvivalent_med
        
          
    
        
        
        Kategori --> "*" Kategori : er_eksklusivt_ekvivalent_med
        click Kategori href "../Kategori/"
    

        
      Kategori : er_ekvivalent_med
        
          
    
        
        
        Kategori --> "*" Kategori : er_ekvivalent_med
        click Kategori href "../Kategori/"
    

        
      Kategori : er_i_klassifikasjon
        
          
    
        
        
        Kategori --> "1" Klassifikasjon : er_i_klassifikasjon
        click Klassifikasjon href "../Klassifikasjon/"
    

        
      Kategori : er_ikkje_ekvivalent_med
        
          
    
        
        
        Kategori --> "*" Kategori : er_ikkje_ekvivalent_med
        click Kategori href "../Kategori/"
    

        
      Kategori : har_notat
        
      Kategori : id
        
      Kategori : overordna_kategori
        
          
    
        
        
        Kategori --> "*" Kategori : overordna_kategori
        click Kategori href "../Kategori/"
    

        
      Kategori : tilhorande_klassifikasjonsnivaa
        
          
    
        
        
        Kategori --> "0..1" Klassifikasjonsnivaa : tilhorande_klassifikasjonsnivaa
        click Klassifikasjonsnivaa href "../Klassifikasjonsnivaa/"
    

        
      Kategori : underordna_kategori
        
          
    
        
        
        Kategori --> "*" Kategori : underordna_kategori
        click Kategori href "../Kategori/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [anbefalt_term](anbefalt_term.md) | 1..* <br/> [LangString](LangString.md) | Føretrukke term/namn for ressursen (skos:prefLabel) |
| [er_i_klassifikasjon](er_i_klassifikasjon.md) | 1 <br/> [Klassifikasjon](Klassifikasjon.md) | Klassifikasjonen kategorien tilhøyrer (skos:inScheme) |





  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tilhorande_klassifikasjonsnivaa](tilhorande_klassifikasjonsnivaa.md) | 0..1 <br/> [Klassifikasjonsnivaa](Klassifikasjonsnivaa.md) | Klassifikasjonsnivå kategorien høyrer til (xkos:belongsTo) |
| [overordna_kategori](overordna_kategori.md) | * <br/> [Kategori](Kategori.md) | Overordna kategori (skos:broader) |
| [underordna_kategori](underordna_kategori.md) | * <br/> [Kategori](Kategori.md) | Underordna kategori (skos:narrower) |





  
  

  
  

  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_notat](har_notat.md) | * <br/> [LangString](LangString.md) | Fritekstnotat om kategorien (skos:note) |
| [er_ekvivalent_med](er_ekvivalent_med.md) | * <br/> [Kategori](Kategori.md) | Breid ekvivalens til kategori i annan klassifikasjon (uneskos:broadMatch) |
| [er_eksklusivt_ekvivalent_med](er_eksklusivt_ekvivalent_med.md) | * <br/> [Kategori](Kategori.md) | Eksklusiv breid ekvivalens (xkos:exclusivelyBroadMatch) |
| [er_ikkje_ekvivalent_med](er_ikkje_ekvivalent_med.md) | * <br/> [Kategori](Kategori.md) | Klar ikkje-ekvivalens til kategori i annan klassifikasjon (xkos:disjointMatch... |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Klassifikasjonsnivaa](Klassifikasjonsnivaa.md) | [har_medlem](har_medlem.md) | range | [Kategori](Kategori.md) |
| [Kategori](Kategori.md) | [overordna_kategori](overordna_kategori.md) | range | [Kategori](Kategori.md) |
| [Kategori](Kategori.md) | [underordna_kategori](underordna_kategori.md) | range | [Kategori](Kategori.md) |
| [Kategori](Kategori.md) | [er_ekvivalent_med](er_ekvivalent_med.md) | range | [Kategori](Kategori.md) |
| [Kategori](Kategori.md) | [er_eksklusivt_ekvivalent_med](er_eksklusivt_ekvivalent_med.md) | range | [Kategori](Kategori.md) |
| [Kategori](Kategori.md) | [er_ikkje_ekvivalent_med](er_ikkje_ekvivalent_med.md) | range | [Kategori](Kategori.md) |
| [Kategorisamanlikning](Kategorisamanlikning.md) | [kjeldeomgrep](kjeldeomgrep.md) | range | [Kategori](Kategori.md) |
| [Kategorisamanlikning](Kategorisamanlikning.md) | [maalomgrep](maalomgrep.md) | range | [Kategori](Kategori.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:Concept |
| native | https://data.norge.no/linkml/xkos-ap-no/Kategori |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kategori
description: Ein kategori i ein klassifikasjon (skos:Concept).
from_schema: https://data.norge.no/linkml/xkos-ap-no
slots:
- id
- anbefalt_term
- er_i_klassifikasjon
- tilhorande_klassifikasjonsnivaa
- overordna_kategori
- underordna_kategori
- har_notat
- er_ekvivalent_med
- er_eksklusivt_ekvivalent_med
- er_ikkje_ekvivalent_med
slot_usage:
  anbefalt_term:
    name: anbefalt_term
    in_subset:
    - Obligatorisk
    required: true
  er_i_klassifikasjon:
    name: er_i_klassifikasjon
    in_subset:
    - Obligatorisk
    required: true
  tilhorande_klassifikasjonsnivaa:
    name: tilhorande_klassifikasjonsnivaa
    in_subset:
    - Anbefalt
  overordna_kategori:
    name: overordna_kategori
    in_subset:
    - Anbefalt
  underordna_kategori:
    name: underordna_kategori
    in_subset:
    - Anbefalt
  har_notat:
    name: har_notat
    in_subset:
    - Valgfri
  er_ekvivalent_med:
    name: er_ekvivalent_med
    in_subset:
    - Valgfri
  er_eksklusivt_ekvivalent_med:
    name: er_eksklusivt_ekvivalent_med
    in_subset:
    - Valgfri
  er_ikkje_ekvivalent_med:
    name: er_ikkje_ekvivalent_med
    in_subset:
    - Valgfri
class_uri: skos:Concept

```
</details>

### Induced

<details>
```yaml
name: Kategori
description: Ein kategori i ein klassifikasjon (skos:Concept).
from_schema: https://data.norge.no/linkml/xkos-ap-no
slot_usage:
  anbefalt_term:
    name: anbefalt_term
    in_subset:
    - Obligatorisk
    required: true
  er_i_klassifikasjon:
    name: er_i_klassifikasjon
    in_subset:
    - Obligatorisk
    required: true
  tilhorande_klassifikasjonsnivaa:
    name: tilhorande_klassifikasjonsnivaa
    in_subset:
    - Anbefalt
  overordna_kategori:
    name: overordna_kategori
    in_subset:
    - Anbefalt
  underordna_kategori:
    name: underordna_kategori
    in_subset:
    - Anbefalt
  har_notat:
    name: har_notat
    in_subset:
    - Valgfri
  er_ekvivalent_med:
    name: er_ekvivalent_med
    in_subset:
    - Valgfri
  er_eksklusivt_ekvivalent_med:
    name: er_eksklusivt_ekvivalent_med
    in_subset:
    - Valgfri
  er_ikkje_ekvivalent_med:
    name: er_ikkje_ekvivalent_med
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Kategori
    domain_of:
    - Klassifikasjon
    - Klassifikasjonsnivaa
    - Kategori
    - Klassifikasjonssamanlikning
    - Kategorisamanlikning
    - Organisasjon
    - Tidsrom
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    range: uriorcurie
    required: true
  anbefalt_term:
    name: anbefalt_term
    description: Føretrukke term/namn for ressursen (skos:prefLabel).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: skos:prefLabel
    alias: anbefalt_term
    owner: Kategori
    domain_of:
    - Kategori
    range: LangString
    required: true
    multivalued: true
  er_i_klassifikasjon:
    name: er_i_klassifikasjon
    description: Klassifikasjonen kategorien tilhøyrer (skos:inScheme).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: skos:inScheme
    alias: er_i_klassifikasjon
    owner: Kategori
    domain_of:
    - Kategori
    range: Klassifikasjon
    required: true
  tilhorande_klassifikasjonsnivaa:
    name: tilhorande_klassifikasjonsnivaa
    description: Klassifikasjonsnivå kategorien høyrer til (xkos:belongsTo).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: xkos:belongsTo
    alias: tilhorande_klassifikasjonsnivaa
    owner: Kategori
    domain_of:
    - Kategori
    range: Klassifikasjonsnivaa
  overordna_kategori:
    name: overordna_kategori
    description: Overordna kategori (skos:broader).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: skos:broader
    alias: overordna_kategori
    owner: Kategori
    domain_of:
    - Kategori
    range: Kategori
    multivalued: true
  underordna_kategori:
    name: underordna_kategori
    description: Underordna kategori (skos:narrower).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: skos:narrower
    alias: underordna_kategori
    owner: Kategori
    domain_of:
    - Kategori
    range: Kategori
    multivalued: true
  har_notat:
    name: har_notat
    description: Fritekstnotat om kategorien (skos:note).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: skos:note
    alias: har_notat
    owner: Kategori
    domain_of:
    - Kategori
    range: LangString
    multivalued: true
  er_ekvivalent_med:
    name: er_ekvivalent_med
    description: Breid ekvivalens til kategori i annan klassifikasjon (uneskos:broadMatch).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: uneskos:broadMatch
    alias: er_ekvivalent_med
    owner: Kategori
    domain_of:
    - Kategori
    range: Kategori
    multivalued: true
  er_eksklusivt_ekvivalent_med:
    name: er_eksklusivt_ekvivalent_med
    description: Eksklusiv breid ekvivalens (xkos:exclusivelyBroadMatch).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: xkos:exclusivelyBroadMatch
    alias: er_eksklusivt_ekvivalent_med
    owner: Kategori
    domain_of:
    - Kategori
    range: Kategori
    multivalued: true
  er_ikkje_ekvivalent_med:
    name: er_ikkje_ekvivalent_med
    description: Klar ikkje-ekvivalens til kategori i annan klassifikasjon (xkos:disjointMatch).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/xkos-ap-no
    rank: 1000
    slot_uri: xkos:disjointMatch
    alias: er_ikkje_ekvivalent_med
    owner: Kategori
    domain_of:
    - Kategori
    range: Kategori
    multivalued: true
class_uri: skos:Concept

```
</details>