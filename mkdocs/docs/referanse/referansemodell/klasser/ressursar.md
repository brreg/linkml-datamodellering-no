

# Slot: ressursar 



URI: [https://data.norge.no/linkml/referansemodell/ressursar](https://data.norge.no/linkml/referansemodell/ressursar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferanseContainer](referansecontainer.md) | Samling av ressursar — toppnivåobjekt for datafila. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Ressurs](ressurs.md) |
| Domain Of | [ReferanseContainer](referansecontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ReferanseContainer](referansecontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/referansemodell




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/referansemodell/ressursar |
| native | https://data.norge.no/linkml/referansemodell/ressursar |




## LinkML Source

<details>
```yaml
name: ressursar
from_schema: https://data.norge.no/linkml/referansemodell
owner: ReferanseContainer
domain_of:
- ReferanseContainer
range: Ressurs
multivalued: true
inlined: true
inlined_as_list: true

```
</details>