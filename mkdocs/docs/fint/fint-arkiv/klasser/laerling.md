

# Slot: laerling 


_Referanse til Laerling (Utdanning)._





URI: [fint:laerling](https://schema.fintlabs.no/laerling)
Alias: laerling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  yes  |
| [Person](person.md) | Fysiske private personar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Person](person.md), [Virksomhet](virksomhet.md) |
| Slot URI | [fint:laerling](https://schema.fintlabs.no/laerling) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:laerling |
| native | https://schema.fintlabs.no/:laerling |




## LinkML Source

<details>
```yaml
name: laerling
description: Referanse til Laerling (Utdanning).
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:laerling
alias: laerling
domain_of:
- Person
- Virksomhet
range: uriorcurie
multivalued: true

```
</details>