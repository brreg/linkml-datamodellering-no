

# Slot: dekningsomrade 


_Geografisk dekningsområde (dct:spatial)._





URI: [dct:spatial](http://purl.org/dc/terms/spatial)
Alias: dekningsomrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [OffentligOrganisasjon](offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  yes  |
| [LovpalagtTjeneste](lovpalagttjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [LovpalagtTjeneste](lovpalagttjeneste.md), [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [OffentligOrganisasjon](offentligorganisasjon.md), [Katalog](katalog.md) |
| Slot URI | [dct:spatial](http://purl.org/dc/terms/spatial) |

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
| self | dct:spatial |
| native | https://data.norge.no/linkml/cpsv-ap-no/dekningsomrade |




## LinkML Source

<details>
```yaml
name: dekningsomrade
description: Geografisk dekningsområde (dct:spatial).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:spatial
alias: dekningsomrade
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- OffentligOrganisasjon
- Katalog
range: Konsept
multivalued: true

```
</details>