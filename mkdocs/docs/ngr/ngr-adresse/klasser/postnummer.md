

# Slot: postnummer 


_Firesifra postnummer (locn:postCode)._





URI: [locn:postCode](http://www.w3.org/ns/locn#postCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Poststed](poststed.md) | Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Poststed](poststed.md) |
| Slot URI | [locn:postCode](http://www.w3.org/ns/locn#postCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:postCode |
| native | https://data.norge.no/ngr/ngr-adresse/postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Firesifra postnummer (locn:postCode).
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: locn:postCode
domain_of:
- Poststed
range: string

```
</details>