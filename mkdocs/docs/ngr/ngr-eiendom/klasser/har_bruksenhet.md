

# Slot: har_bruksenhet 


_Brukseining(ar) i bygningen._





URI: [ngre:harBruksenhet](https://data.norge.no/vocabulary/ngr-eiendom#harBruksenhet)
Alias: har_bruksenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bygning](bygning.md) | Ein bygning registrert i Matrikkelen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bruksenhet](bruksenhet.md) |
| Domain Of | [Bygning](bygning.md) |
| Slot URI | [ngre:harBruksenhet](https://data.norge.no/vocabulary/ngr-eiendom#harBruksenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:harBruksenhet |
| native | https://data.norge.no/linkml/ngr-eiendom/har_bruksenhet |




## LinkML Source

<details>
```yaml
name: har_bruksenhet
description: Brukseining(ar) i bygningen.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:harBruksenhet
alias: har_bruksenhet
domain_of:
- Bygning
range: Bruksenhet
multivalued: true

```
</details>