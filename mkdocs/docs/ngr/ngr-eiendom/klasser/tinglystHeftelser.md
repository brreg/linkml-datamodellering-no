

# Slot: tinglystHeftelser 



URI: [https://data.norge.no/linkml/ngr-eiendom/tinglystHeftelser](https://data.norge.no/linkml/ngr-eiendom/tinglystHeftelser)
Alias: tinglystHeftelser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TinglystHeftelse](TinglystHeftelse.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/tinglystHeftelser |
| native | https://data.norge.no/linkml/ngr-eiendom/tinglystHeftelser |




## LinkML Source

<details>
```yaml
name: tinglystHeftelser
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: tinglystHeftelser
owner: EiendomContainer
domain_of:
- EiendomContainer
range: TinglystHeftelse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>