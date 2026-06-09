

# Class: EierskifteAktivitet 


_TODO: beskriv klassen_





URI: [generated:EierskifteAktivitet](https://example.org/generated/EierskifteAktivitet)





```mermaid
 classDiagram
    class EierskifteAktivitet
    click EierskifteAktivitet href "../EierskifteAktivitet/"
      EierskifteAktivitet : eierskiftedato
        
      EierskifteAktivitet : gjelderHeleAktiviteten
        
          
    
        
        
        EierskifteAktivitet --> "1" Boolean : gjelderHeleAktiviteten
        click Boolean href "../http://www.w3.org/2001/XMLSchema#boolean/"
    

        
      EierskifteAktivitet : hvilkeDeler
        
          
    
        
        
        EierskifteAktivitet --> "0..1" DelerEierskifte : hvilkeDeler
        click DelerEierskifte href "../DelerEierskifte/"
    

        
      EierskifteAktivitet : id
        
          
    
        
        
        EierskifteAktivitet --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      EierskifteAktivitet : organisasjonsnummerHovedenhet
        
      EierskifteAktivitet : typeEierskifte
        
          
    
        
        
        EierskifteAktivitet --> "1" TypeEierskifte : typeEierskifte
        click TypeEierskifte href "../TypeEierskifte/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [generated:EierskifteAktivitet](https://example.org/generated/EierskifteAktivitet) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [typeEierskifte](typeeierskifte.md) | 1 <br/> [TypeEierskifte](typeeierskifte.md) | TODO: beskriv eigenskapen |
| [organisasjonsnummerHovedenhet](organisasjonsnummerhovedenhet.md) | 1 <br/> [Organisasjonsnummer](organisasjonsnummer.md) | TODO: beskriv eigenskapen |
| [gjelderHeleAktiviteten](gjelderheleaktiviteten.md) | 1 <br/> [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) | TODO: beskriv eigenskapen |
| [eierskiftedato](eierskiftedato.md) | 1 <br/> [Dato](dato.md) | TODO: beskriv eigenskapen |





  
  

  
  

  
  

  
  

  
  

  
  
    
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [hvilkeDeler](hvilkedeler.md) | 0..1 <br/> [DelerEierskifte](delereierskifte.md) | TODO: beskriv eigenskapen |





  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Unik URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VirksomhetsinformasjonHovedenhet](virksomhetsinformasjonhovedenhet.md) | [eierskifte](eierskifte.md) | range | [EierskifteAktivitet](eierskifteaktivitet.md) |
| [GeneratedContainer](generatedcontainer.md) | [eierskifteAktiviteter](eierskifteaktiviteter.md) | range | [EierskifteAktivitet](eierskifteaktivitet.md) |












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
| self | generated:EierskifteAktivitet |
| native | generated:EierskifteAktivitet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EierskifteAktivitet
annotations:
  begrepsidentifikator:
    tag: begrepsidentifikator
    value: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
description: 'TODO: beskriv klassen'
from_schema: https://example.org/generated
rank: 1000
slots:
- id
- typeEierskifte
- organisasjonsnummerHovedenhet
- gjelderHeleAktiviteten
- eierskiftedato
- hvilkeDeler
slot_usage:
  typeEierskifte:
    name: typeEierskifte
    in_subset:
    - Obligatorisk
    required: true
  organisasjonsnummerHovedenhet:
    name: organisasjonsnummerHovedenhet
    in_subset:
    - Obligatorisk
    required: true
  gjelderHeleAktiviteten:
    name: gjelderHeleAktiviteten
    in_subset:
    - Obligatorisk
    required: true
  eierskiftedato:
    name: eierskiftedato
    in_subset:
    - Obligatorisk
    required: true
  hvilkeDeler:
    name: hvilkeDeler
    in_subset:
    - Anbefalt
class_uri: generated:EierskifteAktivitet

```
</details>

### Induced

<details>
```yaml
name: EierskifteAktivitet
annotations:
  begrepsidentifikator:
    tag: begrepsidentifikator
    value: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
description: 'TODO: beskriv klassen'
from_schema: https://example.org/generated
rank: 1000
slot_usage:
  typeEierskifte:
    name: typeEierskifte
    in_subset:
    - Obligatorisk
    required: true
  organisasjonsnummerHovedenhet:
    name: organisasjonsnummerHovedenhet
    in_subset:
    - Obligatorisk
    required: true
  gjelderHeleAktiviteten:
    name: gjelderHeleAktiviteten
    in_subset:
    - Obligatorisk
    required: true
  eierskiftedato:
    name: eierskiftedato
    in_subset:
    - Obligatorisk
    required: true
  hvilkeDeler:
    name: hvilkeDeler
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: Unik URI-identifikator for ressursen.
    from_schema: https://example.org/generated
    rank: 1000
    identifier: true
    owner: EierskifteAktivitet
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
  typeEierskifte:
    name: typeEierskifte
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:typeEierskifte
    owner: EierskifteAktivitet
    domain_of:
    - EierskifteAktivitet
    range: TypeEierskifte
    required: true
  organisasjonsnummerHovedenhet:
    name: organisasjonsnummerHovedenhet
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:organisasjonsnummerHovedenhet
    owner: EierskifteAktivitet
    domain_of:
    - EierskifteAktivitet
    range: Organisasjonsnummer
    required: true
  gjelderHeleAktiviteten:
    name: gjelderHeleAktiviteten
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:gjelderHeleAktiviteten
    owner: EierskifteAktivitet
    domain_of:
    - EierskifteAktivitet
    range: boolean
    required: true
  eierskiftedato:
    name: eierskiftedato
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Obligatorisk
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:eierskiftedato
    owner: EierskifteAktivitet
    domain_of:
    - EierskifteAktivitet
    range: Dato
    required: true
  hvilkeDeler:
    name: hvilkeDeler
    description: 'TODO: beskriv eigenskapen'
    in_subset:
    - Anbefalt
    from_schema: https://example.org/generated
    rank: 1000
    slot_uri: generated:hvilkeDeler
    owner: EierskifteAktivitet
    domain_of:
    - EierskifteAktivitet
    range: DelerEierskifte
class_uri: generated:EierskifteAktivitet

```
</details>