

# Slot: matrikkelnumre 



URI: [https://data.norge.no/linkml/ngr-eiendom/matrikkelnumre](https://data.norge.no/linkml/ngr-eiendom/matrikkelnumre)
Alias: matrikkelnumre

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Matrikkelnummer](Matrikkelnummer.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/matrikkelnumre |
| native | https://data.norge.no/linkml/ngr-eiendom/matrikkelnumre |




## LinkML Source

<details>
```yaml
name: matrikkelnumre
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: matrikkelnumre
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Matrikkelnummer
multivalued: true
inlined: true
inlined_as_list: true

```
</details>