

# Slot: enhetskostnad 


_Kostnad per ressurs._





URI: [res:enhetskostnad](https://schema.fintlabs.no/ressurs/enhetskostnad)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Applikasjonsressurs](applikasjonsressurs.md) |
| Slot URI | [res:enhetskostnad](https://schema.fintlabs.no/ressurs/enhetskostnad) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:enhetskostnad |
| native | https://schema.fintlabs.no/ressurs/:enhetskostnad |




## LinkML Source

<details>
```yaml
name: enhetskostnad
description: Kostnad per ressurs.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:enhetskostnad
domain_of:
- Applikasjonsressurs
range: integer

```
</details>