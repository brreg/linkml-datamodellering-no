

# Slot: heimeside 


_Heimeside for ressursen eller organisasjonen (foaf:homepage)._





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
Alias: heimeside

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
| Range | [Uri](uri.md) |
| Domain Of | [LovpalagtTjeneste](lovpalagttjeneste.md), [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [OffentligOrganisasjon](offentligorganisasjon.md), [Katalog](katalog.md) |
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