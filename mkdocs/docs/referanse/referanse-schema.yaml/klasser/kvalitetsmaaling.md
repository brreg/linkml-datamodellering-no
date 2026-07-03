

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
    

        
      Kvalitetsmaaling : har_boolean_verdi
        
          
    
        
        
        Kvalitetsmaaling --> "0..1" Boolean : har_boolean_verdi
        click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"
    

        
      Kvalitetsmaaling : har_merknad
        
          
    
        
        
        Kvalitetsmaaling --> "*" LangString : har_merknad
        click LangString href "../LangString/"
    

        
      Kvalitetsmaaling : har_numerisk_verdi
        
          
    
        
        
        Kvalitetsmaaling --> "0..1" Double : har_numerisk_verdi
        click Double href "../http://www.w3.org/2001/XMLSchema#double/"
    

        
      Kvalitetsmaaling : har_tekst_verdi
        
          
    
        
        
        Kvalitetsmaaling --> "0..1" String : har_tekst_verdi
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
| [har_boolean_verdi](har_boolean_verdi.md) | 0..1 <br/> [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) | Målt verdi som sann/usann (xsd:boolean) |
| [har_numerisk_verdi](har_numerisk_verdi.md) | 0..1 <br/> [xsd:double](http://www.w3.org/2001/XMLSchema#double) | Målt verdi som desimaltal eller heiltal (xsd:double) |
| [har_tekst_verdi](har_tekst_verdi.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Målt verdi som fritekst (rdfs:Literal) |





  
  

  
  

  
  

  
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [har_kvalitetsmaaling](har_kvalitetsmaaling.md) | range | [Kvalitetsmaaling](kvalitetsmaaling.md) |








## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:QualityMeasurement |
| native | https://data.norge.no/ap-no/dqv-core/Kvalitetsmaaling |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetsmaaling
description: Ei konkret måling av eit kvalitetsmål for eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
slots:
- id
- er_kvalitetsmaaling_av
- har_boolean_verdi
- har_numerisk_verdi
- har_tekst_verdi
- har_merknad
slot_usage:
  er_kvalitetsmaaling_av:
    name: er_kvalitetsmaaling_av
    in_subset:
    - Obligatorisk
    required: true
  har_boolean_verdi:
    name: har_boolean_verdi
    in_subset:
    - Anbefalt
  har_numerisk_verdi:
    name: har_numerisk_verdi
    in_subset:
    - Anbefalt
  har_tekst_verdi:
    name: har_tekst_verdi
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
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
slot_usage:
  er_kvalitetsmaaling_av:
    name: er_kvalitetsmaaling_av
    in_subset:
    - Obligatorisk
    required: true
  har_boolean_verdi:
    name: har_boolean_verdi
    in_subset:
    - Anbefalt
  har_numerisk_verdi:
    name: har_numerisk_verdi
    in_subset:
    - Anbefalt
  har_tekst_verdi:
    name: har_tekst_verdi
    in_subset:
    - Anbefalt
  har_merknad:
    name: har_merknad
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: Unik URI-identifikator for ressursen.
    from_schema: https://example.org/linkml/referanse
    rank: 1000
    slot_uri: dct:identifier
    identifier: true
    owner: Kvalitetsmaaling
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Tekstdel
    - KatalogisertRessurs
    - Aktoer
    - Kontaktopplysning
    - Tidsrom
    - Standard
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Ressurs
    range: uriorcurie
    required: true
  er_kvalitetsmaaling_av:
    name: er_kvalitetsmaaling_av
    description: Kvalitetsmålet denne målinga er ei måling av.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqv:isMeasurementOf
    owner: Kvalitetsmaaling
    domain_of:
    - Kvalitetsmaaling
    range: Kvalitetsmaal
    required: true
  har_boolean_verdi:
    name: har_boolean_verdi
    description: Målt verdi som sann/usann (xsd:boolean).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqv:value
    owner: Kvalitetsmaaling
    domain_of:
    - Kvalitetsmaaling
    range: boolean
  har_numerisk_verdi:
    name: har_numerisk_verdi
    description: Målt verdi som desimaltal eller heiltal (xsd:double).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqv:value
    owner: Kvalitetsmaaling
    domain_of:
    - Kvalitetsmaaling
    range: double
  har_tekst_verdi:
    name: har_tekst_verdi
    description: Målt verdi som fritekst (rdfs:Literal).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
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
    from_schema: https://data.norge.no/ap-no/common-ap-no
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