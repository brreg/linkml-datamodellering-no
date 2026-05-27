

# Slot: jobbtittel 


_Namn som beskriv jobben eller stillinga._





URI: [adm:jobbtittel](https://schema.fintlabs.no/administrasjon/jobbtittel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:jobbtittel](https://schema.fintlabs.no/administrasjon/jobbtittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:jobbtittel |
| native | https://schema.fintlabs.no/administrasjon/:jobbtittel |




## LinkML Source

<details>
```yaml
name: jobbtittel
description: Namn som beskriv jobben eller stillinga.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:jobbtittel
domain_of:
- Personalressurs
range: string

```
</details>