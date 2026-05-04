

# Slot: dataobjektId 


_Einingsens ID i datakatalogen (t.d. ObjectId i Azure AD)._





URI: [res:dataobjektId](https://schema.fintlabs.no/ressurs/dataobjektId)
Alias: dataobjektId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [DigitalEnhet](DigitalEnhet.md) |
| Slot URI | [res:dataobjektId](https://schema.fintlabs.no/ressurs/dataobjektId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DigitalEnhet](DigitalEnhet.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:dataobjektId |
| native | https://schema.fintlabs.no/ressurs/:dataobjektId |




## LinkML Source

<details>
```yaml
name: dataobjektId
description: Einingsens ID i datakatalogen (t.d. ObjectId i Azure AD).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:dataobjektId
alias: dataobjektId
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: Identifikator
inlined: true

```
</details>