

# Slot: identitet 


_Identitetar knytt til rettigheta._





URI: [res:identitet](https://schema.fintlabs.no/ressurs/identitet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identitet](identitet.md) |
| Domain Of | [Rettighet](rettighet.md) |
| Slot URI | [res:identitet](https://schema.fintlabs.no/ressurs/identitet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:identitet |
| native | https://schema.fintlabs.no/ressurs/:identitet |




## LinkML Source

<details>
```yaml
name: identitet
description: Identitetar knytt til rettigheta.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:identitet
domain_of:
- Rettighet
range: Identitet
multivalued: true

```
</details>