

# Slot: organisasjonsId 


_Unikt internnummer for organisasjonselementet._





URI: [adm:organisasjonsId](https://schema.fintlabs.no/administrasjon/organisasjonsId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:organisasjonsId](https://schema.fintlabs.no/administrasjon/organisasjonsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:organisasjonsId |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonsId |




## LinkML Source

<details>
```yaml
name: organisasjonsId
description: Unikt internnummer for organisasjonselementet.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:organisasjonsId
domain_of:
- Organisasjonselement
range: Identifikator
inlined: true

```
</details>