

# Class: Kvalitetssertifikat 


_Eit sertifikat som stadfester kvaliteten til eit datasett._





URI: [dqv:QualityCertificate](http://www.w3.org/ns/dqv#QualityCertificate)





```mermaid
 classDiagram
    class Kvalitetssertifikat
    click Kvalitetssertifikat href "../kvalitetssertifikat/"
      Kvalitetsmerknad <|-- Kvalitetssertifikat
        click Kvalitetsmerknad href "../kvalitetsmerknad/"
      
      Kvalitetssertifikat : er_i_kvalitetsdimensjon
        
          
    
        
        
        Kvalitetssertifikat --> "*" Kvalitetsdimensjon : er_i_kvalitetsdimensjon
        click Kvalitetsdimensjon href "../kvalitetsdimensjon/"
    

        
      Kvalitetssertifikat : er_motivert_av
        
          
    
        
        
        Kvalitetssertifikat --> "1" DqvMotivasjon : er_motivert_av
        click DqvMotivasjon href "../dqvmotivasjon/"
    

        
      Kvalitetssertifikat : har_maal
        
          
    
        
        
        Kvalitetssertifikat --> "0..1" Uriorcurie : har_maal
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      Kvalitetssertifikat : har_merknad
        
          
    
        
        
        Kvalitetssertifikat --> "*" LangString : har_merknad
        click LangString href "../langstring/"
    

        
      Kvalitetssertifikat : har_tekstdel
        
          
    
        
        
        Kvalitetssertifikat --> "*" Tekstdel : har_tekstdel
        click Tekstdel href "../tekstdel/"
    

        
      Kvalitetssertifikat : id
        
          
    
        
        
        Kvalitetssertifikat --> "1" Uriorcurie : id
        click Uriorcurie href "http://www.w3.org/2001/XMLSchema#anyURI"
    

        
      
```

!!! note "Om diagrammet"
    Klikk på attributt-radene i klasseboksen ovanfor opnar same side som
    klassenamnet — Mermaid sin `classDiagram`-syntaks støttar berre éin
    klikkbar lenkje per klasseboks, ikkje éin per attributt (BUG-14).
    `## Eigenskapar`-tabellen lenger nede på sida er fasiten for
    slot-spesifikke lenkjer.





## Inheritance
* [Kvalitetsmerknad](kvalitetsmerknad.md)
    * **Kvalitetssertifikat**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dqv:QualityCertificate](http://www.w3.org/ns/dqv#QualityCertificate) |

## Eigenskapar

### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen. | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_motivert_av](er_motivert_av.md) | 1 <br/> [DqvMotivasjon](dqvmotivasjon.md) | Motivasjonen bak kvalitetsmerknaden. | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [er_i_kvalitetsdimensjon](er_i_kvalitetsdimensjon.md) | * <br/> [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld. | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_tekstdel](har_tekstdel.md) | * <br/> [Tekstdel](tekstdel.md) | Tekstleg innhald i merknaden (0..n). | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_merknad](har_merknad.md) | * <br/> [LangString](langstring.md) | Fritekstmerknad (rdfs:comment). | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| [har_maal](har_maal.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | Datasett, distribusjon eller datatjeneste merknaden gjeld. | [Kvalitetsmerknad](kvalitetsmerknad.md) |











## In Subsets


* [Metadata](metadata.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:QualityCertificate |
| native | https://data.norge.no/ap-no/dqv-core/Kvalitetssertifikat |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kvalitetssertifikat
description: Eit sertifikat som stadfester kvaliteten til eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
is_a: Kvalitetsmerknad
class_uri: dqv:QualityCertificate

```
</details>

### Induced

<details>
```yaml
name: Kvalitetssertifikat
description: Eit sertifikat som stadfester kvaliteten til eit datasett.
in_subset:
- Metadata
from_schema: https://data.norge.no/ap-no/dqv-core
is_a: Kvalitetsmerknad
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Kvalitetssertifikat
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
  er_motivert_av:
    name: er_motivert_av
    description: Motivasjonen bak kvalitetsmerknaden.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:motivatedBy
    owner: Kvalitetssertifikat
    domain_of:
    - Kvalitetsmerknad
    range: DqvMotivasjon
    required: true
  er_i_kvalitetsdimensjon:
    name: er_i_kvalitetsdimensjon
    description: Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: dqv:inDimension
    owner: Kvalitetssertifikat
    domain_of:
    - Kvalitetsmerknad
    range: Kvalitetsdimensjon
    required: false
    multivalued: true
  har_tekstdel:
    name: har_tekstdel
    description: Tekstleg innhald i merknaden (0..n).
    in_subset:
    - Anbefalt
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:hasBody
    owner: Kvalitetssertifikat
    domain_of:
    - Kvalitetsmerknad
    range: Tekstdel
    multivalued: true
  har_merknad:
    name: har_merknad
    description: Fritekstmerknad (rdfs:comment).
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/common-ap-no
    slot_uri: rdfs:comment
    owner: Kvalitetssertifikat
    domain_of:
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    range: LangString
    multivalued: true
  har_maal:
    name: har_maal
    description: Datasett, distribusjon eller datatjeneste merknaden gjeld.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/ap-no/dqv-core
    slot_uri: oa:hasTarget
    owner: Kvalitetssertifikat
    domain_of:
    - Kvalitetsmerknad
    range: uriorcurie
class_uri: dqv:QualityCertificate

```
</details>