

# Slot: personopplysningar 



URI: [https://schema.fintlabs.no/personvern/:personopplysningar](https://schema.fintlabs.no/personvern/:personopplysningar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personopplysning](personopplysning.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonvernContainer](personverncontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:personopplysningar |
| native | https://schema.fintlabs.no/personvern/:personopplysningar |




## LinkML Source

<details>
```yaml
name: personopplysningar
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
owner: PersonvernContainer
domain_of:
- PersonvernContainer
range: Personopplysning
multivalued: true
inlined: true
inlined_as_list: true

```
</details>