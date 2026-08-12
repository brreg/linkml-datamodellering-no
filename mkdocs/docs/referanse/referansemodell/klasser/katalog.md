

# Class: Katalog 


_Ei kuratert samling av metadata om datasett, datatenestar og/eller andre katalogar._





URI: [dcat:Catalog](http://www.w3.org/ns/dcat#Catalog)





```mermaid
 classDiagram
    class Katalog
    click Katalog href "../katalog/"
      KatalogisertRessurs <|-- Katalog
        click KatalogisertRessurs href "../katalogisertressurs/"
      
      Katalog : beskrivelse
        
          
    
        
        
        Katalog --> "1..*" LangString : beskrivelse
        click LangString href "../langstring/"
    

        
      Katalog : datasett
        
          
    
        
        
        Katalog --> "*" Datasett : datasett
        click Datasett href "../datasett/"
    

        
      Katalog : datatjeneste
        
          
    
        
        
        Katalog --> "*" Datatjeneste : datatjeneste
        click Datatjeneste href "../datatjeneste/"
    

        
      Katalog : dekningsomraade
        
          
    
        
        
        Katalog --> "*" Konsept : dekningsomraade
        click Konsept href "../konsept/"
    

        
      Katalog : endringsdato
        
          
    
        
        
        Katalog --> "0..1" Date : endringsdato
        click Date href "../date/"
    

        
      Katalog : gjeldende_lovgivning
        
          
    
        
        
        Katalog --> "*" RegulativRessurs : gjeldende_lovgivning
        click RegulativRessurs href "../regulativressurs/"
    

        
      Katalog : har_del
        
          
    
        
        
        Katalog --> "*" Katalog : har_del
        click Katalog href "../katalog/"
    

        
      Katalog : heimeside
        
          
    
        
        
        Katalog --> "*" Uri : heimeside
        click Uri href "../uri/"
    

        
      Katalog : id
        
          
    
        
        
        Katalog --> "1" Uriorcurie : id
        click Uriorcurie href "../uriorcurie/"
    

        
      Katalog : identifikator_literal
        
          
    
        
        
        Katalog --> "0..1" String : identifikator_literal
        click String href "../string/"
    

        
      Katalog : katalogpost
        
          
    
        
        
        Katalog --> "*" Katalogpost : katalogpost
        click Katalogpost href "../katalogpost/"
    

        
      Katalog : kontaktpunkt
        
          
    
        
        
        Katalog --> "1..*" Kontaktopplysning : kontaktpunkt
        click Kontaktopplysning href "../kontaktopplysning/"
    

        
      Katalog : lisens
        
          
    
        
        
        Katalog --> "0..1" Lisensdokument : lisens
        click Lisensdokument href "../lisensdokument/"
    

        
      Katalog : produsent
        
          
    
        
        
        Katalog --> "0..1" Aktoer : produsent
        click Aktoer href "../aktoer/"
    

        
      Katalog : rettigheter
        
          
    
        
        
        Katalog --> "0..1" Rettighetserklaring : rettigheter
        click Rettighetserklaring href "../rettighetserklaring/"
    

        
      Katalog : spraak
        
          
    
        
        
        Katalog --> "*" Konsept : spraak
        click Konsept href "../konsept/"
    

        
      Katalog : temaer
        
          
    
        
        
        Katalog --> "*" Begrepssamling : temaer
        click Begrepssamling href "../begrepssamling/"
    

        
      Katalog : tidsrom
        
          
    
        
        
        Katalog --> "*" Tidsrom : tidsrom
        click Tidsrom href "../tidsrom/"
    

        
      Katalog : tittel
        
          
    
        
        
        Katalog --> "1..*" LangString : tittel
        click LangString href "../langstring/"
    

        
      Katalog : underkatalog
        
          
    
        
        
        Katalog --> "*" Katalog : underkatalog
        click Katalog href "../katalog/"
    

        
      Katalog : utgivelsesdato
        
          
    
        
        
        Katalog --> "0..1" Date : utgivelsesdato
        click Date href "../date/"
    

        
      Katalog : utgiver
        
          
    
        
        
        Katalog --> "1" Aktoer : utgiver
        click Aktoer href "../aktoer/"
    

        
      
```





## Inheritance
* [KatalogisertRessurs](katalogisertressurs.md)
    * **Katalog**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Catalog](http://www.w3.org/ns/dcat#Catalog) |

## Eigenskapar

### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | 1..* <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description). |
| [kontaktpunkt](kontaktpunkt.md) | 1..* <br/> [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for hendvendelsar om ressursen. |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title). |
| [utgiver](utgiver.md) | 1 <br/> [Aktoer](aktoer.md) | Aktøren som er ansvarleg for å tilgjengeleggjere ressursen. |

### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [datasett](datasett.md) | * <br/> [Datasett](datasett.md) | Datasett som er del av katalogen. |
| [datatjeneste](datatjeneste.md) | * <br/> [Datatjeneste](datatjeneste.md) | Datatjeneste som er del av katalogen. |
| [dekningsomraade](dekningsomraade.md) | * <br/> [Konsept](konsept.md) | Geografisk dekningsområde. |
| [endringsdato](endringsdato.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato for siste endring av ressursen (dct:modified). |
| [heimeside](heimeside.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Heimeside for ressursen eller organisasjonen (foaf:homepage). |
| [lisens](lisens.md) | 0..1 <br/> [Lisensdokument](lisensdokument.md) | Lisens for bruk av ressursen. |
| [spraak](spraak.md) | * <br/> [Konsept](konsept.md) | Språk brukt i ressursen. |
| [temaer](temaer.md) | * <br/> [Begrepssamling](begrepssamling.md) | Temavokabular som vert brukt i katalogen. |
| [utgivelsesdato](utgivelsesdato.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato ressursen vart første gong publisert (dct:issued). |

### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gjeldende_lovgivning](gjeldende_lovgivning.md) | * <br/> [RegulativRessurs](regulativressurs.md) | Lovgjeving som gjeld for ressursen. |
| [har_del](har_del.md) | * <br/> [Katalog](katalog.md) | Delkatalog inkludert i denne katalogen. |
| [identifikator_literal](identifikator_literal.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier). |
| [underkatalog](underkatalog.md) | * <br/> [Katalog](katalog.md) | Katalog som er ein del av denne katalogen. |
| [katalogpost](katalogpost.md) | * <br/> [Katalogpost](katalogpost.md) | Katalogpostar i katalogen. |
| [produsent](produsent.md) | 0..1 <br/> [Aktoer](aktoer.md) | Aktøren som primært har skapt ressursen. |
| [rettigheter](rettigheter.md) | 0..1 <br/> [Rettighetserklaring](rettighetserklaring.md) | Rettar knytte til ressursen. |
| [tidsrom](tidsrom.md) | * <br/> [Tidsrom](tidsrom.md) | Tidsperiode ressursen dekkar. |

### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. | [KatalogisertRessurs](katalogisertressurs.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Katalog](katalog.md) | [har_del](har_del.md) | range | [Katalog](katalog.md) |
| [Katalog](katalog.md) | [underkatalog](underkatalog.md) | range | [Katalog](katalog.md) |








## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Catalog |
| native | https://data.norge.no/ap-no/dcat-ap-no/Katalog |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Katalog
description: Ei kuratert samling av metadata om datasett, datatenestar og/eller andre
  katalogar.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
is_a: KatalogisertRessurs
slots:
- beskrivelse
- kontaktpunkt
- tittel
- utgiver
- datasett
- datatjeneste
- dekningsomraade
- endringsdato
- heimeside
- lisens
- spraak
- temaer
- utgivelsesdato
- gjeldende_lovgivning
- har_del
- identifikator_literal
- underkatalog
- katalogpost
- produsent
- rettigheter
- tidsrom
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  kontaktpunkt:
    name: kontaktpunkt
    in_subset:
    - Obligatorisk
    required: true
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  utgiver:
    name: utgiver
    in_subset:
    - Obligatorisk
    required: true
  datasett:
    name: datasett
    in_subset:
    - Anbefalt
  datatjeneste:
    name: datatjeneste
    in_subset:
    - Anbefalt
  dekningsomraade:
    name: dekningsomraade
    in_subset:
    - Anbefalt
  endringsdato:
    name: endringsdato
    in_subset:
    - Anbefalt
  heimeside:
    name: heimeside
    in_subset:
    - Anbefalt
  lisens:
    name: lisens
    in_subset:
    - Anbefalt
  spraak:
    name: spraak
    in_subset:
    - Anbefalt
  temaer:
    name: temaer
    in_subset:
    - Anbefalt
  utgivelsesdato:
    name: utgivelsesdato
    in_subset:
    - Anbefalt
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    in_subset:
    - Valgfri
  har_del:
    name: har_del
    in_subset:
    - Valgfri
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Valgfri
  underkatalog:
    name: underkatalog
    in_subset:
    - Valgfri
  katalogpost:
    name: katalogpost
    in_subset:
    - Valgfri
  produsent:
    name: produsent
    in_subset:
    - Valgfri
  rettigheter:
    name: rettigheter
    in_subset:
    - Valgfri
  tidsrom:
    name: tidsrom
    in_subset:
    - Valgfri
class_uri: dcat:Catalog

```
</details>

### Induced

<details>
```yaml
name: Katalog
description: Ei kuratert samling av metadata om datasett, datatenestar og/eller andre
  katalogar.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
is_a: KatalogisertRessurs
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  kontaktpunkt:
    name: kontaktpunkt
    in_subset:
    - Obligatorisk
    required: true
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  utgiver:
    name: utgiver
    in_subset:
    - Obligatorisk
    required: true
  datasett:
    name: datasett
    in_subset:
    - Anbefalt
  datatjeneste:
    name: datatjeneste
    in_subset:
    - Anbefalt
  dekningsomraade:
    name: dekningsomraade
    in_subset:
    - Anbefalt
  endringsdato:
    name: endringsdato
    in_subset:
    - Anbefalt
  heimeside:
    name: heimeside
    in_subset:
    - Anbefalt
  lisens:
    name: lisens
    in_subset:
    - Anbefalt
  spraak:
    name: spraak
    in_subset:
    - Anbefalt
  temaer:
    name: temaer
    in_subset:
    - Anbefalt
  utgivelsesdato:
    name: utgivelsesdato
    in_subset:
    - Anbefalt
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    in_subset:
    - Valgfri
  har_del:
    name: har_del
    in_subset:
    - Valgfri
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Valgfri
  underkatalog:
    name: underkatalog
    in_subset:
    - Valgfri
  katalogpost:
    name: katalogpost
    in_subset:
    - Valgfri
  produsent:
    name: produsent
    in_subset:
    - Valgfri
  rettigheter:
    name: rettigheter
    in_subset:
    - Valgfri
  tidsrom:
    name: tidsrom
    in_subset:
    - Valgfri
attributes:
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: Katalog
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
    required: true
    multivalued: true
  kontaktpunkt:
    name: kontaktpunkt
    description: Kontaktinformasjon for hendvendelsar om ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:contactPoint
    owner: Katalog
    domain_of:
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalog
    range: Kontaktopplysning
    required: true
    multivalued: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Katalog
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
    required: true
    multivalued: true
  utgiver:
    name: utgiver
    description: Aktøren som er ansvarleg for å tilgjengeleggjere ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:publisher
    owner: Katalog
    domain_of:
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalog
    range: Aktoer
    required: true
  datasett:
    name: datasett
    description: Datasett som er del av katalogen.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:dataset
    owner: Katalog
    domain_of:
    - Katalog
    range: Datasett
    multivalued: true
  datatjeneste:
    name: datatjeneste
    description: Datatjeneste som er del av katalogen.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:service
    owner: Katalog
    domain_of:
    - Katalog
    range: Datatjeneste
    multivalued: true
  dekningsomraade:
    name: dekningsomraade
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: http://sws.geonames.org/
      vokabular_krav:
        tag: vokabular_krav
        value: bør
      sekundare_vokabular:
        tag: sekundare_vokabular
        value: http://publications.europa.eu/resource/authority/country/
      sekundare_vokabular_krav:
        tag: sekundare_vokabular_krav
        value: kan
    description: Geografisk dekningsområde. Verdien BØR veljast frå Geonames (http://sws.geonames.org/)
      eller EUs kontrollerte vokabular Continent, Country, Place (http://publications.europa.eu/resource/authority/continent/,
      http://publications.europa.eu/resource/authority/country/, http://publications.europa.eu/resource/authority/place/).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:spatial
    owner: Katalog
    domain_of:
    - Datasett
    - Datasettserie
    - Katalog
    range: Konsept
    multivalued: true
  endringsdato:
    name: endringsdato
    description: Dato for siste endring av ressursen (dct:modified).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:modified
    owner: Katalog
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Katalogpost
    - Katalog
    range: date
  heimeside:
    name: heimeside
    description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: foaf:homepage
    owner: Katalog
    domain_of:
    - Katalog
    range: uri
    multivalued: true
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
    owner: Katalog
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalog
    range: Lisensdokument
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
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:language
    owner: Katalog
    domain_of:
    - Tekstdel
    - RegulativRessurs
    - Distribusjon
    - Datasett
    - Katalogpost
    - Katalog
    range: Konsept
    multivalued: true
  temaer:
    name: temaer
    annotations:
      gyldige_verdier:
        tag: gyldige_verdier
        value: https://psi.norge.no/los/
      vokabular_krav:
        tag: vokabular_krav
        value: skal
      sekundare_vokabular:
        tag: sekundare_vokabular
        value: http://publications.europa.eu/resource/authority/eurovoc/
      sekundare_vokabular_krav:
        tag: sekundare_vokabular_krav
        value: kan
    description: Temavokabular som vert brukt i katalogen. Verdien SKAL inkludere
      Los-referansen (https://psi.norge.no/los/) for å signalisere til Felles datakatalog
      at Los vert brukt. Andre temavokabular (t.d. EuroVoc) kan òg inkluderast.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:themeTaxonomy
    owner: Katalog
    domain_of:
    - Katalog
    range: Begrepssamling
    multivalued: true
  utgivelsesdato:
    name: utgivelsesdato
    description: Dato ressursen vart første gong publisert (dct:issued).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:issued
    owner: Katalog
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Katalogpost
    - Katalog
    range: date
  gjeldende_lovgivning:
    name: gjeldende_lovgivning
    description: Lovgjeving som gjeld for ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcatap:applicableLegislation
    owner: Katalog
    domain_of:
    - Distribusjon
    - Datasett
    - Datasettserie
    - Datatjeneste
    - Katalog
    range: RegulativRessurs
    multivalued: true
  har_del:
    name: har_del
    description: Delkatalog inkludert i denne katalogen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:hasPart
    owner: Katalog
    domain_of:
    - Katalog
    range: Katalog
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: Katalog
    domain_of:
    - Aktoer
    - RegulativRessurs
    - Datasett
    - Datatjeneste
    - Katalog
    range: string
  underkatalog:
    name: underkatalog
    description: Katalog som er ein del av denne katalogen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:catalog
    owner: Katalog
    domain_of:
    - Katalog
    range: Katalog
    multivalued: true
  katalogpost:
    name: katalogpost
    description: Katalogpostar i katalogen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dcat:record
    owner: Katalog
    domain_of:
    - Katalog
    range: Katalogpost
    multivalued: true
  produsent:
    name: produsent
    description: Aktøren som primært har skapt ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:creator
    owner: Katalog
    domain_of:
    - Datasett
    - Katalog
    range: Aktoer
  rettigheter:
    name: rettigheter
    description: Rettar knytte til ressursen.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:rights
    owner: Katalog
    domain_of:
    - Distribusjon
    - Datatjeneste
    - Katalog
    range: Rettighetserklaring
  tidsrom:
    name: tidsrom
    description: Tidsperiode ressursen dekkar.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: dct:temporal
    owner: Katalog
    domain_of:
    - Datasett
    - Datasettserie
    - Katalog
    range: Tidsrom
    multivalued: true
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Katalog
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
class_uri: dcat:Catalog

```
</details>