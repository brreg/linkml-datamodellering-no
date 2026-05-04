

# Slot: borettslagsandeler 



URI: [https://data.norge.no/linkml/ngr-eiendom/borettslagsandeler](https://data.norge.no/linkml/ngr-eiendom/borettslagsandeler)
Alias: borettslagsandeler

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Borettslagsandel](Borettslagsandel.md) |
| Domain Of | [EiendomContainer](EiendomContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EiendomContainer](EiendomContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-eiendom/borettslagsandeler |
| native | https://data.norge.no/linkml/ngr-eiendom/borettslagsandeler |




## LinkML Source

<details>
```yaml
name: borettslagsandeler
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: borettslagsandeler
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Borettslagsandel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>