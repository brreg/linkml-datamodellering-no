

# Slot: deltek_i 


_Deltakingar aktøren er del av._





URI: [cv:participates](http://data.europa.eu/m8g/participates)
Alias: deltek_i

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktor](Aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |  yes  |
| [OffentligOrganisasjon](OffentligOrganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Deltagelse](Deltagelse.md) |
| Domain Of | [Aktor](Aktor.md) |
| Slot URI | [cv:participates](http://data.europa.eu/m8g/participates) |

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
| self | cv:participates |
| native | https://data.norge.no/linkml/cpsv-ap-no/deltek_i |




## LinkML Source

<details>
```yaml
name: deltek_i
description: Deltakingar aktøren er del av.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:participates
alias: deltek_i
domain_of:
- Aktor
range: Deltagelse
multivalued: true

```
</details>