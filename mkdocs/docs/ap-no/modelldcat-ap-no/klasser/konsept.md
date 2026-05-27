

# Class: Konsept 


_Referanse til eit SKOS-omgrep frå eit kontrollert vokabular._





URI: [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept)





```mermaid
 classDiagram
    class Konsept
    click Konsept href "../Konsept/"
      Konsept : id
        
          
    
        
        
        Konsept --> "1" Uriorcurie : id
        click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Aktor](aktor.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Lisensdokument](lisensdokument.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Modellkatalog](modellkatalog.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Informasjonsmodell](informasjonsmodell.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Informasjonsmodell](informasjonsmodell.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Informasjonsmodell](informasjonsmodell.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [Informasjonsmodell](informasjonsmodell.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Informasjonsmodell](informasjonsmodell.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Modellelement](modellelement.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Objekttype](objekttype.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [RootObjekttype](rootobjekttype.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Datatype](datatype.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [EnkelType](enkeltype.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Kodeliste](kodeliste.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Modul](modul.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Eigenskap](eigenskap.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Attributt](attributt.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Assosiasjon](assosiasjon.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Rolle](rolle.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Spesialisering](spesialisering.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Sammensetning](sammensetning.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Realisering](realisering.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Abstraksjon](abstraksjon.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Avhengighet](avhengighet.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Samling](samling.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Valg](valg.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [AlleAv](alleav.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [NoenAv](noenav.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |
| [Kodeelement](kodeelement.md) | [begrep](begrep.md) | range | [Konsept](konsept.md) |










## See Also

* [https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be](https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be)



## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:Concept |
| native | https://data.norge.no/ap-no/common-ap-no/Konsept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Konsept
description: Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
from_schema: https://data.norge.no/ap-no/common-ap-no
see_also:
- https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be
slots:
- id
class_uri: skos:Concept

```
</details>

### Induced

<details>
```yaml
name: Konsept
description: Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
from_schema: https://data.norge.no/ap-no/common-ap-no
see_also:
- https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/ap-no/common-ap-no
    identifier: true
    owner: Konsept
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
class_uri: skos:Concept

```
</details>