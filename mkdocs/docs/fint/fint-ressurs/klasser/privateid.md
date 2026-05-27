

# Slot: privateid 


_Angir om eininga er eigd av organisasjonen eller privatperson._





URI: [res:privateid](https://schema.fintlabs.no/ressurs/privateid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [DigitalEnhet](digitalenhet.md) |
| Slot URI | [res:privateid](https://schema.fintlabs.no/ressurs/privateid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:privateid |
| native | https://schema.fintlabs.no/ressurs/:privateid |




## LinkML Source

<details>
```yaml
name: privateid
description: Angir om eininga er eigd av organisasjonen eller privatperson.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:privateid
domain_of:
- DigitalEnhet
range: boolean

```
</details>