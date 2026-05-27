

# Slot: kontaktperson_navn 


_Namn på kontaktpersonen._





URI: [fint:kontaktpersonNavn](https://schema.fintlabs.no/kontaktpersonNavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
| Domain Of | [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:kontaktpersonNavn](https://schema.fintlabs.no/kontaktpersonNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktpersonNavn |
| native | https://schema.fintlabs.no/:kontaktperson_navn |




## LinkML Source

<details>
```yaml
name: kontaktperson_navn
description: Namn på kontaktpersonen.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:kontaktpersonNavn
domain_of:
- Kontaktperson
range: Personnavn
inlined: true

```
</details>