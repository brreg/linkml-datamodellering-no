

# Slot: foedselsnummer 


_Fødselsnummer._





URI: [ark:foedselsnummer](https://schema.fintlabs.no/arkiv/foedselsnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md) |
| Slot URI | [ark:foedselsnummer](https://schema.fintlabs.no/arkiv/foedselsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:foedselsnummer |
| native | https://schema.fintlabs.no/arkiv/:foedselsnummer |




## LinkML Source

<details>
```yaml
name: foedselsnummer
description: Fødselsnummer.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:foedselsnummer
domain_of:
- Korrespondansepart
- Part
range: string

```
</details>