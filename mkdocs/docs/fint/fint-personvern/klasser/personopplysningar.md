

# Slot: personopplysningar 



URI: [pvn:personopplysningar](https://schema.fintlabs.no/personvern/personopplysningar)
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
| Slot URI | [pvn:personopplysningar](https://schema.fintlabs.no/personvern/personopplysningar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:personopplysningar |
| native | https://schema.fintlabs.no/personvern/:personopplysningar |




## LinkML Source

<details>
```yaml
name: personopplysningar
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:personopplysningar
domain_of:
- PersonvernContainer
range: Personopplysning
multivalued: true
inlined: true
inlined_as_list: true

```
</details>