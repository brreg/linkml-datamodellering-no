

# Slot: lederFor 


_Organisasjonselement personalressursen er leiar for._





URI: [adm:lederFor](https://schema.fintlabs.no/administrasjon/lederFor)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organisasjonselement](organisasjonselement.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:lederFor](https://schema.fintlabs.no/administrasjon/lederFor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lederFor |
| native | https://schema.fintlabs.no/administrasjon/:lederFor |




## LinkML Source

<details>
```yaml
name: lederFor
description: Organisasjonselement personalressursen er leiar for.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:lederFor
domain_of:
- Personalressurs
range: Organisasjonselement
multivalued: true

```
</details>