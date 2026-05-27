

# Slot: virksomhetsId 


_Intern unik identifikator i økonomisystemet._





URI: [fint:virksomhetsId](https://schema.fintlabs.no/virksomhetsId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [fint:virksomhetsId](https://schema.fintlabs.no/virksomhetsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:virksomhetsId |
| native | https://schema.fintlabs.no/:virksomhetsId |




## LinkML Source

<details>
```yaml
name: virksomhetsId
description: Intern unik identifikator i økonomisystemet.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:virksomhetsId
domain_of:
- Virksomhet
range: Identifikator
inlined: true

```
</details>