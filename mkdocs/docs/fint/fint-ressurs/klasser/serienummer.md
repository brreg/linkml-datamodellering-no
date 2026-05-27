

# Slot: serienummer 


_Unikt serienummer frå einingsprodusentens._





URI: [res:serienummer](https://schema.fintlabs.no/ressurs/serienummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [DigitalEnhet](digitalenhet.md) |
| Slot URI | [res:serienummer](https://schema.fintlabs.no/ressurs/serienummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:serienummer |
| native | https://schema.fintlabs.no/ressurs/:serienummer |




## LinkML Source

<details>
```yaml
name: serienummer
description: Unikt serienummer frå einingsprodusentens.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:serienummer
domain_of:
- DigitalEnhet
range: string

```
</details>