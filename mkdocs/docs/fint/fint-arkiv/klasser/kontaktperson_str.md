

# Slot: kontaktperson_str 


_Kontaktperson hos ein organisasjon som er avsender, mottakar eller sakspart._





URI: [ark:kontaktperson](https://schema.fintlabs.no/arkiv/kontaktperson)
Alias: kontaktperson_str

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md) |
| Slot URI | [ark:kontaktperson](https://schema.fintlabs.no/arkiv/kontaktperson) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:kontaktperson |
| native | https://schema.fintlabs.no/arkiv/:kontaktperson_str |




## LinkML Source

<details>
```yaml
name: kontaktperson_str
description: Kontaktperson hos ein organisasjon som er avsender, mottakar eller sakspart.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:kontaktperson
alias: kontaktperson_str
domain_of:
- Korrespondansepart
- Part
range: string

```
</details>