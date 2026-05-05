

# Slot: personalansvar 


_Arbeidsforhold der personalressursen har personalansvar._





URI: [adm:personalansvar](https://schema.fintlabs.no/administrasjon/personalansvar)
Alias: personalansvar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidsforhold](arbeidsforhold.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:personalansvar](https://schema.fintlabs.no/administrasjon/personalansvar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](personalressurs.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:personalansvar |
| native | https://schema.fintlabs.no/administrasjon/:personalansvar |




## LinkML Source

<details>
```yaml
name: personalansvar
description: Arbeidsforhold der personalressursen har personalansvar.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:personalansvar
alias: personalansvar
owner: Personalressurs
domain_of:
- Personalressurs
range: Arbeidsforhold
multivalued: true

```
</details>