

# Class: TypeAktivitet 


_TODO: beskriv klassen_





URI: [generated:TypeAktivitet](https://example.org/generated/TypeAktivitet)





```mermaid
 classDiagram
    class TypeAktivitet
    click TypeAktivitet href "../TypeAktivitet/"
      TypeAktivitet : aktivitetskode
        
      TypeAktivitet : id
        
          
    
        
        
        TypeAktivitet --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      TypeAktivitet : rekkefoelge
        
          
    
        
        
        TypeAktivitet --> "1" Integer : rekkefoelge
        click Integer href "../http://www.w3.org/2001/XMLSchema#integer/"
    

        
      TypeAktivitet : tekst
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [generated:TypeAktivitet](https://example.org/generated/TypeAktivitet) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [rekkefoelge](rekkefoelge.md) | 1 <br/> [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) | TODO: beskriv eigenskapen |
| [tekst](tekst.md) | 1 <br/> [Tekst1000](tekst1000.md) | TODO: beskriv eigenskapen |





  
  

  
  

  
  
    
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [aktivitetskode](aktivitetskode.md) | 0..1 <br/> [Aktivitetskode](aktivitetskode.md) | TODO: beskriv eigenskapen |





  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneratedContainer](generatedcontainer.md) | [typeAktiviteter](typeaktiviteter.md) | range | [TypeAktivitet](typeaktivitet.md) |












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
| self | generated:TypeAktivitet |
| native | generated:TypeAktivitet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TypeAktivitet
annotations:
  begrepsidentifikator:
    tag: begrepsidentifikator
    value: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
description: 'TODO: beskriv klassen'
from_schema: https://example.org/generated
rank: 1000
slots:
- id
- rekkefoelge
- aktivitetskode
- tekst
slot_usage:
  rekkefoelge:
    name: rekkefoelge
    in_subset:
    - Obligatorisk
    required: true
  aktivitetskode:
    name: aktivitetskode
    in_subset:
    - Anbefalt
  tekst:
    name: tekst
    in_subset:
    - Obligatorisk
    required: true
class_uri: generated:TypeAktivitet

```
</details>

### Induced

<details>
```yaml
name: TypeAktivitet
annotations:
  begrepsidentifikator:
    tag: begrepsidentifikator
    value: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
description: 'TODO: beskriv klassen'
from_schema: https://example.org/generated
rank: 1000
slot_usage:
  rekkefoelge:
    name: rekkefoelge
    in_subset:
    - Obligatorisk
    required: true
  aktivitetskode:
    name: aktivitetskode
    in_subset:
    - Anbefalt
  tekst:
    name: tekst
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
    owner: TypeAktivitet
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
  rekkefoelge:
    name: rekkefoelge
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:rekkefoelge
    owner: TypeAktivitet
    domain_of:
    - TypeAktivitet
    range: integer
    required: true
  aktivitetskode:
    name: aktivitetskode
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Anbefalt
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:aktivitetskode
    owner: TypeAktivitet
    domain_of:
    - TypeAktivitet
    range: Aktivitetskode
  tekst:
    name: tekst
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:tekst
    owner: TypeAktivitet
    domain_of:
    - TypeAktivitet
    range: Tekst1000
    required: true
class_uri: generated:TypeAktivitet

```
</details>