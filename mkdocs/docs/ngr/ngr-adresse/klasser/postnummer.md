

# Slot: postnummer 


_Firesifra postnummer (locn:postCode)._





URI: [locn:postCode](http://www.w3.org/ns/locn#postCode)
Alias: postnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Poststed](Poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Poststed](Poststed.md) |
| Slot URI | [locn:postCode](http://www.w3.org/ns/locn#postCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:postCode |
| native | https://data.norge.no/linkml/ngr-adresse/postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Firesifra postnummer (locn:postCode).
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: locn:postCode
alias: postnummer
domain_of:
- Poststed
range: string

```
</details>