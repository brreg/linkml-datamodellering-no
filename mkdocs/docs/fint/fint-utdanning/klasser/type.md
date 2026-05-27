

# Slot: type 


_Beskriv kva slags type._





URI: [fint:type](https://schema.fintlabs.no/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kontaktperson](kontaktperson.md), [Varsel](varsel.md), [OtStatus](otstatus.md) |
| Slot URI | [fint:type](https://schema.fintlabs.no/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:type |
| native | https://schema.fintlabs.no/:type |




## LinkML Source

<details>
```yaml
name: type
description: Beskriv kva slags type.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:type
domain_of:
- Kontaktperson
- Varsel
- OtStatus
range: string

```
</details>