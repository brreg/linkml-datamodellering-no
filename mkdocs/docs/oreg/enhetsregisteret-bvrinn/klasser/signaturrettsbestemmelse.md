

# Class: Signaturrettsbestemmelse 


_TODO: beskriv klassen_





URI: [generated:Signaturrettsbestemmelse](https://example.org/generated/Signaturrettsbestemmelse)





```mermaid
 classDiagram
    class Signaturrettsbestemmelse
    click Signaturrettsbestemmelse href "../Signaturrettsbestemmelse/"
      Signaturrettsbestemmelse : id
        
          
    
        
        
        Signaturrettsbestemmelse --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Signaturrettsbestemmelse : regel
        
      Signaturrettsbestemmelse : rollesett
        
          
    
        
        
        Signaturrettsbestemmelse --> "1..*" Rollesett : rollesett
        click Rollesett href "../Rollesett/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [generated:Signaturrettsbestemmelse](https://example.org/generated/Signaturrettsbestemmelse) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [regel](regel.md) | 1 <br/> [SignaturrettEllerProkuraregel](signaturrettellerprokuraregel.md) | TODO: beskriv eigenskapen |
| [rollesett](rollesett.md) | 1..* <br/> [Rollesett](rollesett.md) | TODO: beskriv eigenskapen |





  
  

  
  

  
  





  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Signaturrett](signaturrett.md) | [signaturrettsbestemmelsse](signaturrettsbestemmelsse.md) | range | [Signaturrettsbestemmelse](signaturrettsbestemmelse.md) |
| [GeneratedContainer](generatedcontainer.md) | [signaturrettsbestemmelseer](signaturrettsbestemmelseer.md) | range | [Signaturrettsbestemmelse](signaturrettsbestemmelse.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| begrepsidentifikator | https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO |




### Schema Source


* from schema: https://example.org/generated




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | generated:Signaturrettsbestemmelse |
| native | generated:Signaturrettsbestemmelse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Signaturrettsbestemmelse
annotations:
  begrepsidentifikator:
    tag: begrepsidentifikator
    value: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
description: 'TODO: beskriv klassen'
from_schema: https://example.org/generated
rank: 1000
slots:
- id
- regel
- rollesett
slot_usage:
  regel:
    name: regel
    in_subset:
    - Obligatorisk
    required: true
  rollesett:
    name: rollesett
    in_subset:
    - Obligatorisk
    required: true
class_uri: generated:Signaturrettsbestemmelse

```
</details>

### Induced

<details>
```yaml
name: Signaturrettsbestemmelse
annotations:
  begrepsidentifikator:
    tag: begrepsidentifikator
    value: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
description: 'TODO: beskriv klassen'
from_schema: https://example.org/generated
rank: 1000
slot_usage:
  regel:
    name: regel
    in_subset:
    - Obligatorisk
    required: true
  rollesett:
    name: rollesett
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: Unik URI-identifikator for ressursen.
    from_schema: https://example.org/generated
    rank: 1000
    identifier: true
    owner: Signaturrettsbestemmelse
    domain_of:
    - Innrapportering
    - VirksomhetsinformasjonHovedenhet
    - Forretningsadresse
    - Stedsadresse
    - Vegadresse
    - Adressenummer
    - Varslingsadresse
    - Mobilnummer
    - Postadresse
    - Postboksadresse
    - InternasjonalAdresse
    - Kontaktopplysning
    - Telefonnummer
    - VirksomhetsinformasjonUnderenhet
    - Beliggenhetsadresse
    - Aktivitet
    - TypeAktivitet
    - Omdanning
    - Rolletypegruppe
    - Rolle
    - Rolleinnehaver
    - Ansvarsandel
    - Broek
    - Virksomhet
    - Person
    - Prokura
    - Prokurabestemmelse
    - Rollesett
    - SignaturberettigetEllerProkurist
    - Signaturrett
    - Signaturrettsbestemmelse
    - Foretaksinformasjon
    - EierskifteAktivitet
    - DelerEierskifte
    - Matrikkelnummer
    - Innsender
    - Fagsystemreferanse
    - Signering
    - Gebyransvarlig
    range: uriorcurie
    required: true
  regel:
    name: regel
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:regel
    owner: Signaturrettsbestemmelse
    domain_of:
    - Prokurabestemmelse
    - Signaturrettsbestemmelse
    range: SignaturrettEllerProkuraregel
    required: true
  rollesett:
    name: rollesett
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:rollesett
    owner: Signaturrettsbestemmelse
    domain_of:
    - Prokurabestemmelse
    - Signaturrettsbestemmelse
    range: Rollesett
    required: true
    multivalued: true
class_uri: generated:Signaturrettsbestemmelse

```
</details>