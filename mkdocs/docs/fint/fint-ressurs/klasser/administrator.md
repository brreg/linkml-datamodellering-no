

# Slot: administrator 


_Referanse til Organisasjonselement som administrerer eininga._





URI: [res:administrator](https://schema.fintlabs.no/ressurs/administrator)
Alias: administrator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [DigitalEnhet](digitalenhet.md) |
| Slot URI | [res:administrator](https://schema.fintlabs.no/ressurs/administrator) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DigitalEnhet](digitalenhet.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:administrator |
| native | https://schema.fintlabs.no/ressurs/:administrator |




## LinkML Source

<details>
```yaml
name: administrator
description: Referanse til Organisasjonselement som administrerer eininga.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:administrator
alias: administrator
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: uriorcurie
required: true

```
</details>