

# Class: Standard 


_Ein standard eller spesifikasjon som eit datasett er i samsvar med._





URI: [dct:Standard](http://purl.org/dc/terms/Standard)





```mermaid
 classDiagram
    class Standard
    click Standard href "../Standard/"
      Standard : er_i_kvalitetsdimensjon
        
          
    
        
        
        Standard --> "*" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../Kvalitetsdimensjon/"
    

        
      Standard : har_merknad
        
          
    
        
        
        Standard --> "*" LangString : har_merknad
        click LangString href "../LangString/"
    

        
      Standard : har_referanse
        
          
    
        
        
        Standard --> "*" Uri : har_referanse
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Standard : har_versjonsnummer
        
          
    
        
        
        Standard --> "0..1" String : har_versjonsnummer
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Standard : id
        
          
    
        
        
        Standard --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Standard : tittel
        
          
    
        
        
        Standard --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:Standard](http://purl.org/dc/terms/Standard) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |





  
  

  
  

  
  
    
  

  
  
    
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | * <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld |
| [har_referanse](har_referanse.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Referanse til ekstern ressurs (rdfs:seeAlso) |





  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment) |
| [har_versjonsnummer](har_versjonsnummer.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Versjonsnummer for ressursen (owl:versionInfo) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Distribusjon](distribusjon.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](standard.md) |
| [Datasett](datasett.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](standard.md) |
| [Datatjeneste](datatjeneste.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](standard.md) |
| [Katalogpost](katalogpost.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](standard.md) |
| [SamtBuContainer](samtbucontainer.md) | [standarder](standarder.md) | range | [Standard](standard.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:Standard |
| native | https://data.norge.no/ap-no/dqv-ap-no/Standard |




## Examples
### Example: Standard-dcat-ap-no

```yaml
id: dqv:dcat-ap-no
tittel:
- DCAT-AP-NO
er_i_kvalitetsdimensjon:
- dqv:kvalitetsdim-completeness
har_referanse:
- https://data.norge.no/specification/dcat-ap-no#

```



## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Standard
description: Ein standard eller spesifikasjon som eit datasett er i samsvar med.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
slots:
- id
- tittel
- er_i_kvalitetsdimensjon
- har_referanse
- har_merknad
- har_versjonsnummer
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    in_subset:
    - Anbefalt
  har_referanse:
    name: har_referanse
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
  har_versjonsnummer:
    name: har_versjonsnummer
    in_subset:
    - Valgfri
class_uri: dct:Standard

```
</details>

### Induced

<details>
```yaml
name: Standard
description: Ein standard eller spesifikasjon som eit datasett er i samsvar med.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    in_subset:
    - Anbefalt
  har_referanse:
    name: har_referanse
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
  har_versjonsnummer:
    name: har_versjonsnummer
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Standard
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
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Standard
    domain_of:
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    - Standard
    range: LangString
    required: true
    multivalued: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: 'Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.

      '
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-ap-no
    slot_uri: dqv:inDimension
    owner: Standard
    domain_of:
    - Kvalitetsmerknad
    - Standard
    range: Kvalitetsdimensjon
    required: false
    multivalued: true
  har_referanse:
    name: har_referanse
    description: Referanse til ekstern ressurs (rdfs:seeAlso).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:seeAlso
    owner: Standard
    domain_of:
    - RegulativRessurs
    - Standard
    range: uri
    multivalued: true
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:comment
    owner: Standard
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
  har_versjonsnummer:
    name: har_versjonsnummer
    description: Versjonsnummer for ressursen (owl:versionInfo).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: owl:versionInfo
    owner: Standard
    domain_of:
    - Standard
    range: string
class_uri: dct:Standard

```
</details>