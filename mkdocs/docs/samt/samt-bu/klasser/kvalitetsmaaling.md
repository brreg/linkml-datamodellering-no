

# Class: Kvalitetsmaaling 


_Ei konkret måling av eit kvalitetsmål for eit datasett._





URI: [dqv:QualityMeasurement](http://www.w3.org/ns/dqv#QualityMeasurement)





```mermaid
 classDiagram
    class Kvalitetsmaaling
    click Kvalitetsmaaling href "../Kvalitetsmaaling/"
      Kvalitetsmaaling : er_kvalitetsmaaling_av
        
          
    
        
        
        Kvalitetsmaaling --> "1" Kvalitetsmaal : er_kvalitetsmaaling_av
        click Kvalitetsmaal href "../Kvalitetsmaal/"
    

        
      Kvalitetsmaaling : har_merknad
        
          
    
        
        
        Kvalitetsmaaling --> "*" LangString : har_merknad
        click LangString href "../LangString/"
    

        
      Kvalitetsmaaling : har_verdi
        
          
    
        
        
        Kvalitetsmaaling --> "0..1" String : har_verdi
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Kvalitetsmaaling : id
        
          
    
        
        
        Kvalitetsmaaling --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:QualityMeasurement](http://www.w3.org/ns/dqv#QualityMeasurement) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [er_kvalitetsmaaling_av](er_kvalitetsmaaling_av.md) | 1 <br/> [Kvalitetsmaal](kvalitetsmaal.md) | Kvalitetsmålet denne målinga er ei måling av |





  
  

  
  

  
  
    
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_verdi](har_verdi.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Målt verdi (xsd:boolean, xsd:double, xsd:nonNegativeInteger eller rdfs:Litera... |





  
  

  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [har_kvalitetsmaaling](har_kvalitetsmaaling.md) | range | [Kvalitetsmaaling](kvalitetsmaaling.md) |
| [SamtBuContainer](samtbucontainer.md) | [kvalitetsmaalinger](kvalitetsmaalinger.md) | range | [Kvalitetsmaaling](kvalitetsmaaling.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:QualityMeasurement |
| native | https://data.norge.no/linkml/dqv-ap-no/Kvalitetsmaaling |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsmaaling
description: Ei konkret måling av eit kvalitetsmål for eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
slots:
- id
- er_kvalitetsmaaling_av
- har_verdi
- har_merknad
slot_usage:
  er_kvalitetsmaaling_av:
    name: er_kvalitetsmaaling_av
    in_subset:
    - Obligatorisk
    required: true
  har_verdi:
    name: har_verdi
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
class_uri: dqv:QualityMeasurement

```
</details>

### Induced

<details>
```yaml
name: Kvalitetsmaaling
description: Ei konkret måling av eit kvalitetsmål for eit datasett.
from_schema: https://data.norge.no/linkml/dqv-ap-no
slot_usage:
  er_kvalitetsmaaling_av:
    name: er_kvalitetsmaaling_av
    in_subset:
    - Obligatorisk
    required: true
  har_verdi:
    name: har_verdi
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: Kvalitetsmaaling
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
  er_kvalitetsmaaling_av:
    name: er_kvalitetsmaaling_av
    description: Kvalitetsmålet denne målinga er ei måling av.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    slot_uri: dqv:isMeasurementOf
    owner: Kvalitetsmaaling
    domain_of:
    - Kvalitetsmaaling
    range: Kvalitetsmaal
    required: true
  har_verdi:
    name: har_verdi
    description: Målt verdi (xsd:boolean, xsd:double, xsd:nonNegativeInteger eller
      rdfs:Literal avhengig av kvalitetsmålet).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/linkml/dqv-ap-no
    slot_uri: dqv:value
    owner: Kvalitetsmaaling
    domain_of:
    - Kvalitetsmaaling
    range: string
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/common-ap-no
    slot_uri: rdfs:comment
    owner: Kvalitetsmaaling
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
class_uri: dqv:QualityMeasurement

```
</details>