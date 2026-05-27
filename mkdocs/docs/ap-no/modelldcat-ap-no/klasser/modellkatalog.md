

# Class: Modellkatalog 


_Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog)._





URI: [dcat:Catalog](http://www.w3.org/ns/dcat#Catalog)





```mermaid
 classDiagram
    class Modellkatalog
    click Modellkatalog href "../Modellkatalog/"
      Modellkatalog : beskrivelse
        
          
    
        
        
        Modellkatalog --> "1..*" LangString : beskrivelse
        click LangString href "../LangString/"
    

        
      Modellkatalog : endringsdato
        
          
    
        
        
        Modellkatalog --> "0..1" Date : endringsdato
        click Date href "../http://www.w3.org/2001/XMLSchema#date/"
    

        
      Modellkatalog : er_del_av_katalog
        
          
    
        
        
        Modellkatalog --> "0..1" Modellkatalog : er_del_av_katalog
        click Modellkatalog href "../Modellkatalog/"
    

        
      Modellkatalog : har_del
        
          
    
        
        
        Modellkatalog --> "1..*" KatalogisertRessurs : har_del
        click KatalogisertRessurs href "../KatalogisertRessurs/"
    

        
      Modellkatalog : heimeside
        
          
    
        
        
        Modellkatalog --> "*" Uri : heimeside
        click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Modellkatalog : id
        
          
    
        
        
        Modellkatalog --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      Modellkatalog : identifikator_literal
        
          
    
        
        
        Modellkatalog --> "1" String : identifikator_literal
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      Modellkatalog : kontaktpunkt
        
          
    
        
        
        Modellkatalog --> "1..*" Kontaktopplysning : kontaktpunkt
        click Kontaktopplysning href "../Kontaktopplysning/"
    

        
      Modellkatalog : lisens
        
          
    
        
        
        Modellkatalog --> "0..1" Lisensdokument : lisens
        click Lisensdokument href "../Lisensdokument/"
    

        
      Modellkatalog : modell
        
          
    
        
        
        Modellkatalog --> "*" Informasjonsmodell : modell
        click Informasjonsmodell href "../Informasjonsmodell/"
    

        
      Modellkatalog : spraak
        
          
    
        
        
        Modellkatalog --> "*" Spraak : spraak
        click Spraak href "../Spraak/"
    

        
      Modellkatalog : tema
        
          
    
        
        
        Modellkatalog --> "*" Konsept : tema
        click Konsept href "../Konsept/"
    

        
      Modellkatalog : temaer
        
          
    
        
        
        Modellkatalog --> "*" Begrepssamling : temaer
        click Begrepssamling href "../Begrepssamling/"
    

        
      Modellkatalog : tittel
        
          
    
        
        
        Modellkatalog --> "1..*" LangString : tittel
        click LangString href "../LangString/"
    

        
      Modellkatalog : utgivelsesdato
        
          
    
        
        
        Modellkatalog --> "0..1" Date : utgivelsesdato
        click Date href "../http://www.w3.org/2001/XMLSchema#date/"
    

        
      Modellkatalog : utgiver
        
          
    
        
        
        Modellkatalog --> "1" Aktor : utgiver
        click Aktor href "../Aktor/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dcat:Catalog](http://www.w3.org/ns/dcat#Catalog) |


## Eigenskapar







  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [tittel](tittel.md) | 1..* <br/> [LangString](langstring.md) | Namn/tittel på ressursen (dct:title) |
| [beskrivelse](beskrivelse.md) | 1..* <br/> [LangString](langstring.md) | Fritekstbeskrivelse av ressursen (dct:description) |
| [har_del](har_del.md) | 1..* <br/> [KatalogisertRessurs](katalogisertressurs.md) | Del-ressurs inkludert i denne katalogen (dct:hasPart) |
| [identifikator_literal](identifikator_literal.md) | 1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Tekstleg identifikator for ressursen (dct:identifier) |
| [kontaktpunkt](kontaktpunkt.md) | 1..* <br/> [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ressursen (dcat:contactPoint) |
| [utgiver](utgiver.md) | 1 <br/> [Aktor](aktor.md) | Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher) |





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  
    
  

  
  

  
  
    
  

  
  


### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [endringsdato](endringsdato.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato for siste endring av ressursen (dct:modified) |
| [heimeside](heimeside.md) | * <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Heimeside for ressursen eller organisasjonen (foaf:homepage) |
| [lisens](lisens.md) | 0..1 <br/> [Lisensdokument](lisensdokument.md) | Lisens for bruk av ressursen (dct:license) |
| [modell](modell.md) | * <br/> [Informasjonsmodell](informasjonsmodell.md) | Informasjonsmodellar i modellkatalogen (modelldcatno:model) |
| [spraak](spraak.md) | * <br/> [Spraak](spraak.md) | Språk brukt i ressursen (dct:language) |
| [tema](tema.md) | * <br/> [Konsept](konsept.md) | Tema frå eit kontrollert vokabular (dcat:theme) |
| [utgivelsesdato](utgivelsesdato.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Dato ressursen vart første gong publisert (dct:issued) |





  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  

  
  
    
  

  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [temaer](temaer.md) | * <br/> [Begrepssamling](begrepssamling.md) | Temavokabular brukt i katalogen (dcat:themeTaxonomy) |
| [er_del_av_katalog](er_del_av_katalog.md) | 0..1 <br/> [Modellkatalog](modellkatalog.md) | Overordna modellkatalog (dct:isPartOf) |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Modellkatalog](modellkatalog.md) | [er_del_av_katalog](er_del_av_katalog.md) | range | [Modellkatalog](modellkatalog.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Catalog |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/Modellkatalog |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Modellkatalog
description: Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slots:
- id
- tittel
- beskrivelse
- har_del
- identifikator_literal
- kontaktpunkt
- utgiver
- endringsdato
- heimeside
- lisens
- modell
- spraak
- tema
- temaer
- utgivelsesdato
- er_del_av_katalog
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  har_del:
    name: har_del
    in_subset:
    - Obligatorisk
    required: true
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Obligatorisk
    required: true
  kontaktpunkt:
    name: kontaktpunkt
    in_subset:
    - Obligatorisk
    required: true
  utgiver:
    name: utgiver
    in_subset:
    - Obligatorisk
    required: true
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
  modell:
    name: modell
    in_subset:
    - Anbefalt
  spraak:
    name: spraak
    in_subset:
    - Anbefalt
  tema:
    name: tema
    in_subset:
    - Anbefalt
  utgivelsesdato:
    name: utgivelsesdato
    in_subset:
    - Anbefalt
  temaer:
    name: temaer
    in_subset:
    - Valgfri
  er_del_av_katalog:
    name: er_del_av_katalog
    in_subset:
    - Valgfri
class_uri: dcat:Catalog

```
</details>

### Induced

<details>
```yaml
name: Modellkatalog
description: Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_usage:
  tittel:
    name: tittel
    in_subset:
    - Obligatorisk
    required: true
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Obligatorisk
    required: true
  har_del:
    name: har_del
    in_subset:
    - Obligatorisk
    required: true
  identifikator_literal:
    name: identifikator_literal
    in_subset:
    - Obligatorisk
    required: true
  kontaktpunkt:
    name: kontaktpunkt
    in_subset:
    - Obligatorisk
    required: true
  utgiver:
    name: utgiver
    in_subset:
    - Obligatorisk
    required: true
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
  modell:
    name: modell
    in_subset:
    - Anbefalt
  spraak:
    name: spraak
    in_subset:
    - Anbefalt
  tema:
    name: tema
    in_subset:
    - Anbefalt
  utgivelsesdato:
    name: utgivelsesdato
    in_subset:
    - Anbefalt
  temaer:
    name: temaer
    in_subset:
    - Valgfri
  er_del_av_katalog:
    name: er_del_av_katalog
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Modellkatalog
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Standard
    - Lisensdokument
    - Lokasjon
    - Tidsperiode
    - Dokument
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: uriorcurie
    required: true
  tittel:
    name: tittel
    description: Namn/tittel på ressursen (dct:title).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:title
    owner: Modellkatalog
    domain_of:
    - Standard
    - Dokument
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    range: LangString
    required: true
    multivalued: true
  beskrivelse:
    name: beskrivelse
    description: Fritekstbeskrivelse av ressursen (dct:description).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:description
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    range: LangString
    required: true
    multivalued: true
  har_del:
    name: har_del
    description: Del-ressurs inkludert i denne katalogen (dct:hasPart).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:hasPart
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    range: KatalogisertRessurs
    required: true
    multivalued: true
  identifikator_literal:
    name: identifikator_literal
    description: Tekstleg identifikator for ressursen (dct:identifier).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:identifier
    owner: Modellkatalog
    domain_of:
    - Aktor
    - Modellkatalog
    - Informasjonsmodell
    - Modellelement
    - Eigenskap
    - Merknad
    - Kodeelement
    range: string
    required: true
  kontaktpunkt:
    name: kontaktpunkt
    description: Kontaktinformasjon for ressursen (dcat:contactPoint).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dcat:contactPoint
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: Kontaktopplysning
    required: true
    multivalued: true
  utgiver:
    name: utgiver
    description: Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:publisher
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: Aktor
    required: true
  endringsdato:
    name: endringsdato
    description: Dato for siste endring av ressursen (dct:modified).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:modified
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: date
  heimeside:
    name: heimeside
    description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: foaf:homepage
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: uri
    multivalued: true
  lisens:
    name: lisens
    description: Lisens for bruk av ressursen (dct:license).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:license
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: Lisensdokument
  modell:
    name: modell
    description: Informasjonsmodellar i modellkatalogen (modelldcatno:model).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: modelldcatno:model
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    range: Informasjonsmodell
    multivalued: true
  spraak:
    name: spraak
    description: Språk brukt i ressursen (dct:language).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:language
    owner: Modellkatalog
    domain_of:
    - Dokument
    - Modellkatalog
    - Informasjonsmodell
    range: Spraak
    multivalued: true
  tema:
    name: tema
    description: Tema frå eit kontrollert vokabular (dcat:theme).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dcat:theme
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: Konsept
    multivalued: true
  temaer:
    name: temaer
    description: Temavokabular brukt i katalogen (dcat:themeTaxonomy).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dcat:themeTaxonomy
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    range: Begrepssamling
    multivalued: true
  utgivelsesdato:
    name: utgivelsesdato
    description: Dato ressursen vart første gong publisert (dct:issued).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: dct:issued
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    - Informasjonsmodell
    range: date
  er_del_av_katalog:
    name: er_del_av_katalog
    description: Overordna modellkatalog (dct:isPartOf).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
    rank: 1000
    slot_uri: dct:isPartOf
    owner: Modellkatalog
    domain_of:
    - Modellkatalog
    range: Modellkatalog
class_uri: dcat:Catalog

```
</details>