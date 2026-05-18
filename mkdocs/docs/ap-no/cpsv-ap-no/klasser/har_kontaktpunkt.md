

# Slot: har_kontaktpunkt 


_Kontaktpunkt for tenesta eller organisasjonen._





URI: [cv:contactPoint](http://data.europa.eu/m8g/contactPoint)
Alias: har_kontaktpunkt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hendelse](hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |  yes  |
| [Virksomhetshendelse](virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |  no  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Livshendelse](livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktpunkt](kontaktpunkt.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Hendelse](hendelse.md), [Katalog](katalog.md) |
| Slot URI | [cv:contactPoint](http://data.europa.eu/m8g/contactPoint) |

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
| self | cv:contactPoint |
| native | https://data.norge.no/linkml/cpsv-ap-no/har_kontaktpunkt |




## LinkML Source

<details>
```yaml
name: har_kontaktpunkt
description: Kontaktpunkt for tenesta eller organisasjonen.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:contactPoint
alias: har_kontaktpunkt
domain_of:
- OffentligTjeneste
- Tjeneste
- Hendelse
- Katalog
range: Kontaktpunkt
multivalued: true

```
</details>