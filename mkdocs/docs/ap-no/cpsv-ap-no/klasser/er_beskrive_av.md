

# Slot: er_beskrive_av 


_Datasett som beskriv ressursen._





URI: [cccevno:isDescribedBy](https://data.norge.no/vocabulary/cccevno#isDescribedBy)
Alias: er_beskrive_av

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Dokumentasjonstype](dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Hendelse](hendelse.md), [Dokumentasjonstype](dokumentasjonstype.md), [Tjenesteresultattype](tjenesteresultattype.md) |
| Slot URI | [cccevno:isDescribedBy](https://data.norge.no/vocabulary/cccevno#isDescribedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cccevno:isDescribedBy |
| native | https://data.norge.no/linkml/cpsv-ap-no/er_beskrive_av |




## LinkML Source

<details>
```yaml
name: er_beskrive_av
description: Datasett som beskriv ressursen.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cccevno:isDescribedBy
alias: er_beskrive_av
domain_of:
- OffentligTjeneste
- Tjeneste
- Hendelse
- Dokumentasjonstype
- Tjenesteresultattype
range: uri
multivalued: true

```
</details>