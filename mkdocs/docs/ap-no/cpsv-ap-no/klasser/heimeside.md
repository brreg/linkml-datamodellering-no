

# Slot: heimeside 


_Heimeside for ressursen eller organisasjonen (foaf:homepage)._





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
Alias: heimeside

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [OffentligOrganisasjon](OffentligOrganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [OffentligOrganisasjon](OffentligOrganisasjon.md), [Katalog](Katalog.md) |
| Slot URI | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage) |

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
| self | foaf:homepage |
| native | https://data.norge.no/linkml/cpsv-ap-no/heimeside |




## LinkML Source

<details>
```yaml
name: heimeside
description: Heimeside for ressursen eller organisasjonen (foaf:homepage).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: foaf:homepage
alias: heimeside
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
- OffentligOrganisasjon
- Katalog
range: uri
multivalued: true

```
</details>