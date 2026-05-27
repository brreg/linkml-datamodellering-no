

# Slot: anleggseiendommer 



URI: [https://data.norge.no/ngr/ngr-eiendom/anleggseiendommer](https://data.norge.no/ngr/ngr-eiendom/anleggseiendommer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Anleggseiendom](anleggseiendom.md) |
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
| self | https://data.norge.no/ngr/ngr-eiendom/anleggseiendommer |
| native | https://data.norge.no/ngr/ngr-eiendom/anleggseiendommer |




## LinkML Source

<details>
```yaml
name: anleggseiendommer
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Anleggseiendom
multivalued: true
inlined: true
inlined_as_list: true

```
</details>