

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
| [OffentligTjeneste](offentligtjeneste.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [temaomrade](temaomrade.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [er_klassifisert_av](er_klassifisert_av.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [malgruppe](malgruppe.md) | range | [Konsept](konsept.md) |
| [OffentligTjeneste](offentligtjeneste.md) | [sektor](sektor.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [status](status.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [temaomrade](temaomrade.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [er_klassifisert_av](er_klassifisert_av.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [malgruppe](malgruppe.md) | range | [Konsept](konsept.md) |
| [Tjeneste](tjeneste.md) | [sektor](sektor.md) | range | [Konsept](konsept.md) |
| [Hendelse](hendelse.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Hendelse](hendelse.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Livshendelse](livshendelse.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Livshendelse](livshendelse.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Virksomhetshendelse](virksomhetshendelse.md) | [tema](tema.md) | range | [Konsept](konsept.md) |
| [Virksomhetshendelse](virksomhetshendelse.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [OffentligOrganisasjon](offentligorganisasjon.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [OffentligOrganisasjon](offentligorganisasjon.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Tjenestekanal](tjenestekanal.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Dokumentasjonstype](dokumentasjonstype.md) | [klassifisering](klassifisering.md) | range | [Konsept](konsept.md) |
| [Dokumentasjonstype](dokumentasjonstype.md) | [utstedingsstad](utstedingsstad.md) | range | [Konsept](konsept.md) |
| [Tjenesteresultattype](tjenesteresultattype.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Gebyr](gebyr.md) | [valuta](valuta.md) | range | [Konsept](konsept.md) |
| [Regel](regel.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [RegulativRessurs](regulativressurs.md) | [type_concept](type_concept.md) | range | [Konsept](konsept.md) |
| [Deltagelse](deltagelse.md) | [har_rolle](har_rolle.md) | range | [Konsept](konsept.md) |
| [Katalog](katalog.md) | [dekningsomraade](dekningsomraade.md) | range | [Konsept](konsept.md) |
| [Katalog](katalog.md) | [oppdateringsfrekvens](oppdateringsfrekvens.md) | range | [Konsept](konsept.md) |










## See Also

* [https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be](https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be)



## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:Concept |
| native | https://data.norge.no/linkml/common-ap-no/Konsept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Konsept
description: Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
from_schema: https://data.norge.no/linkml/common-ap-no
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
from_schema: https://data.norge.no/linkml/common-ap-no
see_also:
- https://data.norge.no/concepts/02131737-bb20-3204-93e0-46678b7d57be
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/common-ap-no
    identifier: true
    owner: Konsept
    domain_of:
    - Mediatype
    - Konsept
    - Begrepssamling
    - OffentligTjeneste
    - Tjeneste
    - Hendelse
    - Aktor
    - Kontaktpunkt
    - Tjenestekanal
    - Dokumentasjonstype
    - Tjenesteresultattype
    - Tjenesteresultattypeliste
    - Gebyr
    - Regel
    - RegulativRessurs
    - Deltagelse
    - Adresse
    - Katalog
    range: uriorcurie
    required: true
class_uri: skos:Concept

```
</details>