

# Class: Kontaktopplysning 


_Kontaktinformasjon for ein aktør._





URI: [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind)





```mermaid
 classDiagram
    class Kontaktopplysning
    click Kontaktopplysning href "../kontaktopplysning/"
      Kontaktopplysning : har_epost
        
          
    
        
        
        Kontaktopplysning --> "0..1" String : har_epost
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Kontaktopplysning : har_kontaktside
        
          
    
        
        
        Kontaktopplysning --> "0..1" String : har_kontaktside
        click String href "http://www.w3.org/2001/XMLSchema#string"
    

        
      Kontaktopplysning : id
        
          
    
        
        
        Kontaktopplysning --> "1" Uriorcurie : id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      Kontaktopplysning : navn_vcard
        
          
    
        
        
        Kontaktopplysning --> "1..*" LangString : navn_vcard
        click LangString href "../langstring/"
    

        
      
```

!!! note "Om diagrammet"
    Klikk på attributt-radene i klasseboksen ovanfor opnar same side som
    klassenamnet — Mermaid sin `classDiagram`-syntaks støttar berre éin
    klikkbar lenkje per klasseboks, ikkje éin per attributt (BUG-14).
    `## Eigenskapar`-tabellen lenger nede på sida er fasiten for
    slot-spesifikke lenkjer.




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind) |

## Eigenskapar

### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [navn_vcard](navn_vcard.md) | 1..* <br/> [LangString](langstring.md) | Formatert namn (vCard). |

### Anbefalt

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [har_epost](har_epost.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | E-postadresse til kontaktpunktet. |
| [har_kontaktside](har_kontaktside.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Nettside for kontakt. |

### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. |






## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Datasettserie](datasettserie.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Datatjeneste](datatjeneste.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |
| [Katalog](katalog.md) | [kontaktpunkt](kontaktpunkt.md) | range | [Kontaktopplysning](kontaktopplysning.md) |








## In Subsets


* [Metadata](metadata.md)




## See Also

* [https://data.norge.no/concepts/9c17b5e3-6763-3650-a741-b879e7bbdecc](https://data.norge.no/concepts/9c17b5e3-6763-3650-a741-b879e7bbdecc)



## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:Kind |
| native | https://data.norge.no/ap-no/dcat-ap-no/Kontaktopplysning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kontaktopplysning
description: Kontaktinformasjon for ein aktør.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
see_also:
- https://data.norge.no/concepts/9c17b5e3-6763-3650-a741-b879e7bbdecc
slots:
- id
- navn_vcard
- har_epost
- har_kontaktside
slot_usage:
  navn_vcard:
    name: navn_vcard
    in_subset:
    - Obligatorisk
    required: true
  har_epost:
    name: har_epost
    in_subset:
    - Anbefalt
  har_kontaktside:
    name: har_kontaktside
    in_subset:
    - Anbefalt
class_uri: vcard:Kind

```
</details>

### Induced

<details>
```yaml
name: Kontaktopplysning
description: Kontaktinformasjon for ein aktør.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dcat-ap-no
see_also:
- https://data.norge.no/concepts/9c17b5e3-6763-3650-a741-b879e7bbdecc
slot_usage:
  navn_vcard:
    name: navn_vcard
    in_subset:
    - Obligatorisk
    required: true
  har_epost:
    name: har_epost
    in_subset:
    - Anbefalt
  har_kontaktside:
    name: har_kontaktside
    in_subset:
    - Anbefalt
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Kontaktopplysning
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
  navn_vcard:
    name: navn_vcard
    description: Formatert namn (vCard).
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: vcard:fn
    owner: Kontaktopplysning
    domain_of:
    - Kontaktopplysning
    range: LangString
    required: true
    multivalued: true
  har_epost:
    name: har_epost
    description: E-postadresse til kontaktpunktet.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: vcard:hasEmail
    owner: Kontaktopplysning
    domain_of:
    - Kontaktopplysning
    range: string
  har_kontaktside:
    name: har_kontaktside
    description: Nettside for kontakt.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dcat-ap-no
    slot_uri: vcard:hasURL
    owner: Kontaktopplysning
    domain_of:
    - Kontaktopplysning
    range: string
class_uri: vcard:Kind

```
</details>