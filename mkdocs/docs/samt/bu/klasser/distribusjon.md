

# Class: Distribusjon 


_Ein spesifikk representasjon/nedlastbar form av eit datasett._





URI: [dcat:Distribution](http://www.w3.org/ns/dcat#Distribution)





```mermaid
 classDiagram
    class Distribusjon
    click Distribusjon href "../Distribusjon/"
      Distribusjon : beskrivelse
        
      Distribusjon : dokumentasjon
        
      Distribusjon : endringsdato
        
      Distribusjon : filstorrelse
        
      Distribusjon : format
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : format
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : gjeldende_lovgivning
        
          
    
        
        
        Distribusjon --> "*" RegulativRessurs : gjeldende_lovgivning
        click RegulativRessurs href "../RegulativRessurs/"
    

        
      Distribusjon : i_samsvar_med
        
          
    
        
        
        Distribusjon --> "*" Standard : i_samsvar_med
        click Standard href "../Standard/"
    

        
      Distribusjon : id
        
      Distribusjon : komprimeringsformat
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : komprimeringsformat
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : lisens
        
          
    
        
        
        Distribusjon --> "0..1" Konsept : lisens
        click Konsept href "../Konsept/"
    

        
      Distribusjon : medietype
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : medietype
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : nedlastningslenke
        
      Distribusjon : pakkeformat
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : pakkeformat
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : policy
        
          
    
        
        
        Distribusjon --> "0..1" OdrlPolicy : policy
        click OdrlPolicy href "../OdrlPolicy/"
    

        
      Distribusjon : rettigheter
        
          
    
        
        
        Distribusjon --> "0..1" Rettighetserklaring : rettigheter
        click Rettighetserklaring href "../Rettighetserklaring/"
    

        
      Distribusjon : sjekksum
        
          
    
        
        
        Distribusjon --> "0..1" Sjekksum : sjekksum
        click Sjekksum href "../Sjekksum/"
    

        
      Distribusjon : sprak
        
          
    
        
        
        Distribusjon --> "*" Spraak : sprak
        click Spraak href "../Spraak/"
    

        
      Distribusjon : status
        
          
    
        
        
        Distribusjon --> "0..1" Konsept : status
        click Konsept href "../Konsept/"
    

        
      Distribusjon : tidsopplosning
        
      Distribusjon : tilgangs_url
        
      Distribusjon : tilgangstjeneste
        
          
    
        
        
        Distribusjon --> "*" Datatjeneste : tilgangstjeneste
        click Datatjeneste href "../Datatjeneste/"
    

        
      Distribusjon : tilgjengelighet
        
          
    
        
        
        Distribusjon --> "0..1" Konsept : tilgjengelighet
        click Konsept href "../Konsept/"
    

        
      Distribusjon : tittel
        
      Distribusjon : utgivelsesdato
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Distribution](http://www.w3.org/ns/dcat#Distribution) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tilgangs_url](tilgangs_url.md) | 1..* <br/> [Uri](uri.md) | URL for tilgang til distribusjonen |





  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [format](format.md) | 0..1 <br/> [Mediatype](mediatype.md) | Filformat eller medietype (dct:format) |
| [lisens](lisens.md) | 0..1 <br/> [Konsept](konsept.md) | Lisens for bruk av ressursen |
| [status](status.md) | 0..1 <br/> [Konsept](konsept.md) | Status for ressursen frå eit kontrollert vokabular (adms:status) |
| [tilgjengelighet](tilgjengelighet.md) | 0..1 <br/> [Konsept](konsept.md) | Planlagt tilgjengelegheit for ressursen |





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  

  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |
| [dokumentasjon](dokumentasjon.md) | * <br/> [Uri](uri.md) | Lenke til dokumentasjon om ressursen |
| [endringsdato](endringsdato.md) | 0..1 <br/> [Date](date.md) | Dato for siste endring av ressursen (dct:modified) |
| [filstorrelse](filstorrelse.md) | 0..1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Filstørrelse i bytes |
| [gjeldende_lovgivning](gjeldende_lovgivning.md) | * <br/> [RegulativRessurs](regulativressurs.md) | Lovgjeving som gjeld for ressursen |
| [i_samsvar_med](i_samsvar_med.md) | * <br/> [Standard](standard.md) | Standard ressursen er i samsvar med |
| [komprimeringsformat](komprimeringsformat.md) | 0..1 <br/> [Mediatype](mediatype.md) | Komprimeringsformat brukt i distribusjonen |
| [medietype](medietype.md) | 0..1 <br/> [Mediatype](mediatype.md) | Medietype i samsvar med IANA-registeret |
| [nedlastningslenke](nedlastningslenke.md) | * <br/> [Uri](uri.md) | Direkte nedlastingslenke for distribusjonsfila |
| [pakkeformat](pakkeformat.md) | 0..1 <br/> [Mediatype](mediatype.md) | Pakkeformat brukt i distribusjonen |
| [policy](policy.md) | 0..1 <br/> [OdrlPolicy](odrlpolicy.md) | ODRL-policy som regulerer bruk av ressursen |
| [rettigheter](rettigheter.md) | 0..1 <br/> [Rettighetserklaring](rettighetserklaring.md) | Rettar knytte til ressursen |
| [sjekksum](sjekksum.md) | 0..1 <br/> [Sjekksum](sjekksum.md) | Sjekksum for distribusjonsfila |
| [sprak](sprak.md) | * <br/> [Spraak](spraak.md) | Språk brukt i ressursen (dct:language) |
| [tidsopplosning](tidsopplosning.md) | 0..1 <br/> [Duration](duration.md) | Minste tidsoppløysing i datasettet |
| [tilgangstjeneste](tilgangstjeneste.md) | * <br/> [Datatjeneste](datatjeneste.md) | Datatjeneste som gjev tilgang til distribusjonen |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [utgivelsesdato](utgivelsesdato.md) | 0..1 <br/> [Date](date.md) | Dato ressursen vart første gong publisert (dct:issued) |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Containerklasse](containerklasse.md) | [datasettdistribusjoner](datasettdistribusjoner.md) | range | [Distribusjon](distribusjon.md) |
| [Datasett](datasett.md) | [datasettdistribusjon](datasettdistribusjon.md) | range | [Distribusjon](distribusjon.md) |
| [Datasett](datasett.md) | [eksempeldata](eksempeldata.md) | range | [Distribusjon](distribusjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Distribution |
| native | samtbuskole:Distribusjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Distribusjon
description: Ein spesifikk representasjon/nedlastbar form av eit datasett.
from_schema: https://example.no/ontology/samt-bu-skole
slots:
- id
- tilgangs_url
- beskrivelse
- format
- lisens
- status
- tilgjengelighet
- dokumentasjon
- endringsdato
- filstorrelse
- gjeldende_lovgivning
- i_samsvar_med
- komprimeringsformat
- medietype
- nedlastningslenke
- pakkeformat
- policy
- rettigheter
- sjekksum
- sprak
- tidsopplosning
- tilgangstjeneste
- tittel
- utgivelsesdato
slot_usage:
  tilgangs_url:
    name: tilgangs_url
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Anbefalt
  format:
    name: format
    in_subset:
    - Anbefalt
  lisens:
    name: lisens
    in_subset:
    - Anbefalt
  status:
    name: status
    in_subset:
    - Anbefalt
  tilgjengelighet:
    name: tilgjengelighet
    in_subset:
    - Anbefalt
class_uri: dcat:Distribution

```
</details>

### Induced

<details>
```yaml
name: Distribusjon
description: Ein spesifikk representasjon/nedlastbar form av eit datasett.
from_schema: https://example.no/ontology/samt-bu-skole
slot_usage:
  tilgangs_url:
    name: tilgangs_url
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Anbefalt
  format:
    name: format
    in_subset:
    - Anbefalt
  lisens:
    name: lisens
    in_subset:
    - Anbefalt
  status:
    name: status
    in_subset:
    - Anbefalt
  tilgjengelighet:
    name: tilgjengelighet
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: Distribusjon
    domain_of:
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
    - Frekvens
    - ProvenanceStatement
    - OdrlPolicy
    - ProvAktivitet
    - ProvAttributering
    - Tidsinstant
    - KatalogisertRessurs
    - Aktor
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
    - Katalogpost
    range: uriorcurie
    required: true
  tilgangs_url:
    name: tilgangs_url
    description: URL for tilgang til distribusjonen.
    in_subset:
    - Obligatorisk
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:accessURL
    alias: tilgangs_url
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: uri
    required: true
    multivalued: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Anbefalt
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:description
    alias: beskrivelse
    owner: Distribusjon
    domain_of:
    - RegulativRessurs
    - Gebyr
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    range: LangString
    multivalued: true
  format:
    name: format
    description: Filformat eller medietype (dct:format).
    in_subset:
    - Anbefalt
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:format
    alias: format
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    range: Mediatype
  lisens:
    name: lisens
    description: Lisens for bruk av ressursen.
    in_subset:
    - Anbefalt
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:license
    alias: lisens
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalog
    range: Konsept
  status:
    name: status
    description: Status for ressursen frå eit kontrollert vokabular (adms:status).
    in_subset:
    - Anbefalt
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: adms:status
    alias: status
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalogpost
    range: Konsept
  tilgjengelighet:
    name: tilgjengelighet
    description: Planlagt tilgjengelegheit for ressursen.
    in_subset:
    - Anbefalt
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcatap:availability
    alias: tilgjengelighet
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    range: Konsept
  dokumentasjon:
    name: dokumentasjon
    description: Lenke til dokumentasjon om ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: foaf:page
    alias: dokumentasjon
    owner: Distribusjon
    domain_of:
    - Gebyr
    - Distribusjon
    - Datasett
    - Datatjeneste
    range: uri
    multivalued: true
  endringsdato:
    name: endringsdato
    description: Dato for siste endring av ressursen (dct:modified).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:modified
    alias: endringsdato
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Katalogpost
    - Katalog
    range: date
  filstorrelse:
    name: filstorrelse
    description: Filstørrelse i bytes.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:byteSize
    alias: filstorrelse
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: NonNegativeInteger
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    description: Lovgjeving som gjeld for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcatap:applicableLegislation
    alias: gjeldende_lovgivning
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalog
    range: RegulativRessurs
    multivalued: true
  i_samsvar_med:
    name: i_samsvar_med
    description: Standard ressursen er i samsvar med.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:conformsTo
    alias: i_samsvar_med
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    - Datatjeneste
    - Katalogpost
    range: Standard
    multivalued: true
  komprimeringsformat:
    name: komprimeringsformat
    description: Komprimeringsformat brukt i distribusjonen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:compressFormat
    alias: komprimeringsformat
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Mediatype
  medietype:
    name: medietype
    description: Medietype i samsvar med IANA-registeret.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:mediaType
    alias: medietype
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Mediatype
  nedlastningslenke:
    name: nedlastningslenke
    description: Direkte nedlastingslenke for distribusjonsfila.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:downloadURL
    alias: nedlastningslenke
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: uri
    multivalued: true
  pakkeformat:
    name: pakkeformat
    description: Pakkeformat brukt i distribusjonen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:packageFormat
    alias: pakkeformat
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Mediatype
  policy:
    name: policy
    description: ODRL-policy som regulerer bruk av ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: odrl:hasPolicy
    alias: policy
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: OdrlPolicy
  rettigheter:
    name: rettigheter
    description: Rettar knytte til ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:rights
    alias: rettigheter
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalog
    range: Rettighetserklaring
  sjekksum:
    name: sjekksum
    description: Sjekksum for distribusjonsfila.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: spdx:checksum
    alias: sjekksum
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Sjekksum
  sprak:
    name: sprak
    description: Språk brukt i ressursen (dct:language).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:language
    alias: sprak
    owner: Distribusjon
    domain_of:
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Katalogpost
    - Katalog
    range: Spraak
    multivalued: true
  tidsopplosning:
    name: tidsopplosning
    description: Minste tidsoppløysing i datasettet.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:temporalResolution
    alias: tidsopplosning
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Duration
  tilgangstjeneste:
    name: tilgangstjeneste
    description: Datatjeneste som gjev tilgang til distribusjonen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dcat:accessService
    alias: tilgangstjeneste
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Datatjeneste
    multivalued: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:title
    alias: tittel
    owner: Distribusjon
    domain_of:
    - Standard
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalogpost
    - Katalog
    range: LangString
    multivalued: true
  utgivelsesdato:
    name: utgivelsesdato
    description: Dato ressursen vart første gong publisert (dct:issued).
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: dct:issued
    alias: utgivelsesdato
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Katalogpost
    - Katalog
    range: date
class_uri: dcat:Distribution

```
</details>