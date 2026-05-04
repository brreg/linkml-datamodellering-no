

# Slot: er_beskrive_av 


_Datasett som beskriv ressursen._





URI: [cccevno:isDescribedBy](https://data.norge.no/vocabulary/cccevno#isDescribedBy)
Alias: er_beskrive_av

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hendelse](Hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Livshendelse](Livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |
| [Virksomhetshendelse](Virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Dokumentasjonstype](Dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |  yes  |
| [Tjenesteresultattype](Tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Hendelse](Hendelse.md), [Dokumentasjonstype](Dokumentasjonstype.md), [Tjenesteresultattype](Tjenesteresultattype.md) |
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