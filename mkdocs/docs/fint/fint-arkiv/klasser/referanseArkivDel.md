

# Slot: referanseArkivdel 


_Referanse til arkivdelen denne arkivenheten er tilknytt._





URI: [ark:referanseArkivdel](https://schema.fintlabs.no/arkiv/referanseArkivdel)
Alias: referanseArkivdel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:referanseArkivdel](https://schema.fintlabs.no/arkiv/referanseArkivdel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:referanseArkivdel |
| native | https://schema.fintlabs.no/arkiv/:referanseArkivdel |




## LinkML Source

<details>
```yaml
name: referanseArkivdel
description: Referanse til arkivdelen denne arkivenheten er tilknytt.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:referanseArkivdel
alias: referanseArkivdel
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: string
multivalued: true

```
</details>