

# Class: Distribusjon 


_Ein spesifikk representasjon/nedlastbar form av eit datasett._





URI: [dcat:Distribution](http://www.w3.org/ns/dcat#Distribution)





```mermaid
 classDiagram
    class Distribusjon
    click Distribusjon href "../Distribusjon/"
      Distribusjon : beskrivelse
        
          
    
        
        
        Distribusjon --> "*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Distribusjon : dokumentasjon
        
          
    
        
        
        Distribusjon --> "*" Uri : dokumentasjon
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Distribusjon : endringsdato
        
          
    
        
        
        Distribusjon --> "0..1" Date : endringsdato
        click Date href "../http://www.w3.org/2001/XMLSchema#date/"
    

        
      Distribusjon : filstorrelse
        
          
    
        
        
        Distribusjon --> "0..1" NonNegativeInteger : filstorrelse
        click NonNegativeInteger href "../NonNegativeInteger/"
    

        
      Distribusjon : format
        
          
    
        
        
        Distribusjon --> "0..1" Konsept : format
        click Konsept href "../Konsept/"
    

        
      Distribusjon : gjeldende_lovgivning
        
          
    
        
        
        Distribusjon --> "*" RegulativRessurs : gjeldende_lovgivning
        click RegulativRessurs href "../RegulativRessurs/"
    

        
      Distribusjon : i_samsvar_med
        
          
    
        
        
        Distribusjon --> "*" Standard : i_samsvar_med
        click Standard href "../Standard/"
    

        
      Distribusjon : id
        
          
    
        
        
        Distribusjon --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Distribusjon : komprimeringsformat
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : komprimeringsformat
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : lisens
        
          
    
        
        
        Distribusjon --> "0..1" Lisensdokument : lisens
        click Lisensdokument href "../Lisensdokument/"
    

        
      Distribusjon : medietype
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : medietype
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : nedlastningslenke
        
          
    
        
        
        Distribusjon --> "*" Uri : nedlastningslenke
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Distribusjon : pakkeformat
        
          
    
        
        
        Distribusjon --> "0..1" Mediatype : pakkeformat
        click Mediatype href "../Mediatype/"
    

        
      Distribusjon : policy
        
          
    
        
        
        Distribusjon --> "0..1" Uri : policy
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Distribusjon : rettigheter
        
          
    
        
        
        Distribusjon --> "0..1" Rettighetserklaring : rettigheter
        click Rettighetserklaring href "../Rettighetserklaring/"
    

        
      Distribusjon : romlig_opplosning
        
          
    
        
        
        Distribusjon --> "*" Float : romlig_opplosning
        click Float href "../http://www.w3.org/2001/XMLSchema#float/"
    

        
      Distribusjon : sjekksum
        
          
    
        
        
        Distribusjon --> "0..1" Sjekksum : sjekksum
        click Sjekksum href "../Sjekksum/"
    

        
      Distribusjon : spraak
        
          
    
        
        
        Distribusjon --> "*" Konsept : spraak
        click Konsept href "../Konsept/"
    

        
      Distribusjon : status
        
          
    
        
        
        Distribusjon --> "0..1" Konsept : status
        click Konsept href "../Konsept/"
    

        
      Distribusjon : tidsopplosning
        
          
    
        
        
        Distribusjon --> "0..1" Duration : tidsopplosning
        click Duration href "../Duration/"
    

        
      Distribusjon : tilgangs_url
        
          
    
        
        
        Distribusjon --> "1..*" Uri : tilgangs_url
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Distribusjon : tilgangstjeneste
        
          
    
        
        
        Distribusjon --> "*" Datatjeneste : tilgangstjeneste
        click Datatjeneste href "../Datatjeneste/"
    

        
      Distribusjon : tilgjengelighet
        
          
    
        
        
        Distribusjon --> "0..1" Konsept : tilgjengelighet
        click Konsept href "../Konsept/"
    

        
      Distribusjon : tittel
        
          
    
        
        
        Distribusjon --> "*" LangString : tittel
        click LangString href "../LangString/"
    

        
      Distribusjon : utgivelsesdato
        
          
    
        
        
        Distribusjon --> "0..1" Date : utgivelsesdato
        click Date href "../http://www.w3.org/2001/XMLSchema#date/"
    

        
      
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
| [tilgangs_url](tilgangs_url.md) | 1..* <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URL for tilgang til distribusjonen. |

### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | * <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description). |
| [format](format.md) | 0..1 <br/> [Konsept](konsept.md) | Filformat eller medietype. |
| [lisens](lisens.md) | 0..1 <br/> [Lisensdokument](lisensdokument.md) | Lisens for bruk av ressursen. |
| [status](status.md) | 0..1 <br/> [Konsept](konsept.md) | Status for ressursen. |
| [tilgjengelighet](tilgjengelighet.md) | 0..1 <br/> [Konsept](konsept.md) | Planlagt tilgjengelegheit for ressursen. |

### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [dokumentasjon](dokumentasjon.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Lenke til dokumentasjon om ressursen. |
| [endringsdato](endringsdato.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato for siste endring av ressursen (dct:modified). |
| [filstorrelse](filstorrelse.md) | 0..1 <br/> [NonNegativeInteger](nonnegativeinteger.md) | Filstørrelse i bytes. |
| [gjeldende_lovgivning](gjeldende_lovgivning.md) | * <br/> [RegulativRessurs](regulativressurs.md) | Lovgjeving som gjeld for ressursen. |
| [i_samsvar_med](i_samsvar_med.md) | * <br/> [Standard](standard.md) | Standard ressursen er i samsvar med. |
| [komprimeringsformat](komprimeringsformat.md) | 0..1 <br/> [Mediatype](mediatype.md) | Komprimeringsformat brukt i distribusjonen. |
| [medietype](medietype.md) | 0..1 <br/> [Mediatype](mediatype.md) | Medietype i samsvar med IANA-registeret. |
| [nedlastningslenke](nedlastningslenke.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Direkte nedlastingslenke for distribusjonsfila. |
| [pakkeformat](pakkeformat.md) | 0..1 <br/> [Mediatype](mediatype.md) | Pakkeformat brukt i distribusjonen. |
| [policy](policy.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | ODRL-policy som regulerer bruk av ressursen. |
| [rettigheter](rettigheter.md) | 0..1 <br/> [Rettighetserklaring](rettighetserklaring.md) | Rettar knytte til ressursen. |
| [sjekksum](sjekksum.md) | 0..1 <br/> [Sjekksum](sjekksum.md) | Sjekksum for distribusjonsfila. |
| [spraak](spraak.md) | * <br/> [Konsept](konsept.md) | Språk brukt i ressursen. |
| [tidsopplosning](tidsopplosning.md) | 0..1 <br/> [Duration](duration.md) | Minste tidsoppløysing i datasettet. |
| [tilgangstjeneste](tilgangstjeneste.md) | * <br/> [Datatjeneste](datatjeneste.md) | Datatjeneste som gjev tilgang til distribusjonen. |
| [tittel](tittel.md) | * <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title). |
| [utgivelsesdato](utgivelsesdato.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato ressursen vart første gong publisert (dct:issued). |
| [romlig_opplosning](romlig_opplosning.md) | * <br/> [xsd:float](http://www.w3.org/2001/XMLSchema#float) | Minste romleg oppløysing i datasettet, oppgjeven i meter. |

### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. |






## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [datasettdistribusjon](datasettdistribusjon.md) | range | [Distribusjon](distribusjon.md) |
| [Datasett](datasett.md) | [eksempeldata](eksempeldata.md) | range | [Distribusjon](distribusjon.md) |








## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Distribution |
| native | https://data.norge.no/ap-no/dcat-ap-no/Distribusjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Distribusjon
description: Ein spesifikk representasjon/nedlastbar form av eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
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
- spraak
- tidsopplosning
- tilgangstjeneste
- tittel
- utgivelsesdato
- romlig_opplosning
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
  nedlastningslenke:
    name: nedlastningslenke
    in_subset:
    - Valgfri
  dokumentasjon:
    name: dokumentasjon
    in_subset:
    - Valgfri
  endringsdato:
    name: endringsdato
    in_subset:
    - Valgfri
  filstorrelse:
    name: filstorrelse
    in_subset:
    - Valgfri
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    in_subset:
    - Valgfri
  i_samsvar_med:
    name: i_samsvar_med
    in_subset:
    - Valgfri
  komprimeringsformat:
    name: komprimeringsformat
    in_subset:
    - Valgfri
  medietype:
    name: medietype
    in_subset:
    - Valgfri
  pakkeformat:
    name: pakkeformat
    in_subset:
    - Valgfri
  policy:
    name: policy
    in_subset:
    - Valgfri
  rettigheter:
    name: rettigheter
    in_subset:
    - Valgfri
  romlig_opplosning:
    name: romlig_opplosning
    in_subset:
    - Valgfri
  sjekksum:
    name: sjekksum
    in_subset:
    - Valgfri
  spraak:
    name: spraak
    in_subset:
    - Valgfri
  tidsopplosning:
    name: tidsopplosning
    in_subset:
    - Valgfri
  tilgangstjeneste:
    name: tilgangstjeneste
    in_subset:
    - Valgfri
  tittel:
    name: tittel
    in_subset:
    - Valgfri
  utgivelsesdato:
    name: utgivelsesdato
    in_subset:
    - Valgfri
class_uri: dcat:Distribution

```
</details>

### Induced

<details>
```yaml
name: Distribusjon
description: Ein spesifikk representasjon/nedlastbar form av eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
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
  nedlastningslenke:
    name: nedlastningslenke
    in_subset:
    - Valgfri
  dokumentasjon:
    name: dokumentasjon
    in_subset:
    - Valgfri
  endringsdato:
    name: endringsdato
    in_subset:
    - Valgfri
  filstorrelse:
    name: filstorrelse
    in_subset:
    - Valgfri
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    in_subset:
    - Valgfri
  i_samsvar_med:
    name: i_samsvar_med
    in_subset:
    - Valgfri
  komprimeringsformat:
    name: komprimeringsformat
    in_subset:
    - Valgfri
  medietype:
    name: medietype
    in_subset:
    - Valgfri
  pakkeformat:
    name: pakkeformat
    in_subset:
    - Valgfri
  policy:
    name: policy
    in_subset:
    - Valgfri
  rettigheter:
    name: rettigheter
    in_subset:
    - Valgfri
  romlig_opplosning:
    name: romlig_opplosning
    in_subset:
    - Valgfri
  sjekksum:
    name: sjekksum
    in_subset:
    - Valgfri
  spraak:
    name: spraak
    in_subset:
    - Valgfri
  tidsopplosning:
    name: tidsopplosning
    in_subset:
    - Valgfri
  tilgangstjeneste:
    name: tilgangstjeneste
    in_subset:
    - Valgfri
  tittel:
    name: tittel
    in_subset:
    - Valgfri
  utgivelsesdato:
    name: utgivelsesdato
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Distribusjon
    domain_of:
    - Lisensdokument
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
  tilgangs_url:
    name: tilgangs_url
    description: URL for tilgang til distribusjonen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:accessURL
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
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
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
    - Ressurs
    range: LangString
    multivalued: true
  format:
    name: format
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: http://publications.europa.eu/resource/authority/file-type/
      vokabular_krav:
        tag: vokabular_krav
        value: skal
      vokabular_pattern:
        tag: vokabular_pattern
        value: ^http://publications\.europa\.eu/resource/authority/file-type/[A-Z_]+$
      enum_referanse:
        tag: enum_referanse
        value: EUFileType
      enum_dekning:
        tag: enum_dekning
        value: delvis
    description: Filformat eller medietype. Verdien SKAL veljast frå EUs kontrollerte
      vokabular File type (http://publications.europa.eu/resource/authority/file-type/).
      Enumerasjonen EUFileType i common-ap-no dekkjer dei mest brukte formata (RDF,
      JSON, CSV, PDF, osv.). For andre format, bruk URI frå EU File Type-vokabularet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:format
    owner: Distribusjon
    domain_of:
    - Tekstdel
    - Distribusjon
    - Datatjeneste
    range: Konsept
  lisens:
    name: lisens
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: http://publications.europa.eu/resource/authority/licence/
      vokabular_krav:
        tag: vokabular_krav
        value: skal
      enum_referanse:
        tag: enum_referanse
        value: EULicence
      enum_dekning:
        tag: enum_dekning
        value: delvis
    description: Lisens for bruk av ressursen. Verdien SKAL veljast frå EUs kontrollerte
      vokabular Licence (http://publications.europa.eu/resource/authority/licence/).
      For norske offentlege data er CC BY 4.0 eller NLOD 2.0 anbefalt per retningslinjene.
      Enumerasjonen EULicence i common-ap-no dekkjer dei mest brukte open source/open
      data-lisensane.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:license
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalog
    range: Lisensdokument
  status:
    name: status
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: http://purl.org/adms/status/
      vokabular_krav:
        tag: vokabular_krav
        value: skal
      vokabular_pattern:
        tag: vokabular_pattern
        value: ^http://purl\.org/adms/status/(Completed|Deprecated|UnderDevelopment|Withdrawn)$
      enum_referanse:
        tag: enum_referanse
        value: ADMSStatus
      enum_dekning:
        tag: enum_dekning
        value: full
    description: 'Status for ressursen. Verdien SKAL veljast frå ADMS Status-vokabularet
      (http://purl.org/adms/status/). Gyldige verdiar: Completed (ferdigstilt), Deprecated
      (foreldet), UnderDevelopment (under utvikling), Withdrawn (trukket tilbake).
      Sjå enumerasjonen ADMSStatus i common-ap-no.'
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: adms:status
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalogpost
    range: Konsept
  tilgjengelighet:
    name: tilgjengelighet
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: http://publications.europa.eu/resource/authority/planned-availability/
      vokabular_krav:
        tag: vokabular_krav
        value: bør
      vokabular_pattern:
        tag: vokabular_pattern
        value: ^http://publications\.europa\.eu/resource/authority/planned-availability/[A-Z_]+$
    description: 'Planlagt tilgjengelegheit for ressursen. Verdien BØR veljast frå
      EUs kontrollerte vokabular Planned availability (http://publications.europa.eu/resource/authority/planned-availability/).
      Gyldige verdiar: AVAILABLE (tilgjengeleg), EXPERIMENTAL (eksperimentell), STABLE
      (stabil), TEMPORARY (mellombels).'
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcatap:availability
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    range: Konsept
  dokumentasjon:
    name: dokumentasjon
    description: Lenke til dokumentasjon om ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: foaf:page
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
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:modified
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
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:byteSize
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: NonNegativeInteger
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    description: Lovgjeving som gjeld for ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcatap:applicableLegislation
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
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:conformsTo
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
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:compressFormat
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Mediatype
  medietype:
    name: medietype
    description: Medietype i samsvar med IANA-registeret.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:mediaType
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Mediatype
  nedlastningslenke:
    name: nedlastningslenke
    description: Direkte nedlastingslenke for distribusjonsfila.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:downloadURL
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: uri
    multivalued: true
  pakkeformat:
    name: pakkeformat
    description: Pakkeformat brukt i distribusjonen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:packageFormat
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Mediatype
  policy:
    name: policy
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: odrl:Policy
    description: ODRL-policy som regulerer bruk av ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: odrl:hasPolicy
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: uri
  rettigheter:
    name: rettigheter
    description: Rettar knytte til ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:rights
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalog
    range: Rettighetserklaring
  sjekksum:
    name: sjekksum
    description: Sjekksum for distribusjonsfila.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: spdx:checksum
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Sjekksum
  spraak:
    name: spraak
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: http://publications.europa.eu/resource/authority/language/
      vokabular_krav:
        tag: vokabular_krav
        value: skal
      vokabular_pattern:
        tag: vokabular_pattern
        value: ^http://publications\.europa\.eu/resource/authority/language/[A-Z]{3}$
      enum_referanse:
        tag: enum_referanse
        value: EULanguage
      enum_dekning:
        tag: enum_dekning
        value: delvis
    description: Språk brukt i ressursen. Verdien SKAL veljast frå EUs kontrollerte
      vokabular Language (http://publications.europa.eu/resource/authority/language/).
      Enumerasjonen EULanguage i common-ap-no dekkjer norske språk (bokmål, nynorsk,
      samiske språk). For andre språk, bruk URI frå EU Language-vokabularet (t.d.
      ENG for engelsk, SWE for svensk).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:language
    owner: Distribusjon
    domain_of:
    - Tekstdel
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Katalogpost
    - Katalog
    range: Konsept
    multivalued: true
  tidsopplosning:
    name: tidsopplosning
    description: Minste tidsoppløysing i datasettet.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:temporalResolution
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    range: Duration
  tilgangstjeneste:
    name: tilgangstjeneste
    description: Datatjeneste som gjev tilgang til distribusjonen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:accessService
    owner: Distribusjon
    domain_of:
    - Distribusjon
    range: Datatjeneste
    multivalued: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
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
    - Ressurs
    range: LangString
    multivalued: true
  utgivelsesdato:
    name: utgivelsesdato
    description: Dato ressursen vart første gong publisert (dct:issued).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:issued
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Katalogpost
    - Katalog
    range: date
  romlig_opplosning:
    name: romlig_opplosning
    description: Minste romleg oppløysing i datasettet, oppgjeven i meter.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:spatialResolutionInMeters
    owner: Distribusjon
    domain_of:
    - Distribusjon
    - Datasett
    range: float
    multivalued: true
class_uri: dcat:Distribution

```
</details>