

# Slot: borettslagsandeler 



URI: [https://data.norge.no/ngr/ngr-eiendom/borettslagsandeler](https://data.norge.no/ngr/ngr-eiendom/borettslagsandeler)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Borettslagsandel](borettslagsandel.md) |
| Domain Of | [EiendomContainer](eiendomcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EiendomContainer](eiendomcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ngr/ngr-eiendom/borettslagsandeler |
| native | https://data.norge.no/ngr/ngr-eiendom/borettslagsandeler |




## LinkML Source

<details>
```yaml
name: borettslagsandeler
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Borettslagsandel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>