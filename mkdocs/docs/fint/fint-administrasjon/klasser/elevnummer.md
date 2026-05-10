

# Slot: elevnummer 


_Skulens interne elevnummer._





URI: [fint:elevnummer](https://schema.fintlabs.no/elevnummer)
Alias: elevnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Elev](elev.md) |
| Slot URI | [fint:elevnummer](https://schema.fintlabs.no/elevnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:elevnummer |
| native | https://schema.fintlabs.no/:elevnummer |




## LinkML Source

<details>
```yaml
name: elevnummer
description: Skulens interne elevnummer.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:elevnummer
alias: elevnummer
domain_of:
- Elev
range: Identifikator
inlined: true

```
</details>