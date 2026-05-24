

# Slot: har_antall_aksjer 


_Tal aksjar._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:har_antall_aksjer](https://data.norge.no/linkml/register-over-aksjeeiere/:har_antall_aksjer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aksjekapital](aksjekapital.md) | Den registrerte aksjekapitalen i eit aksjeselskap |  no  |
| [Aksjepost](aksjepost.md) | Samling aksjar eigd av ein aksjeeigar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Aksjekapital](aksjekapital.md), [Aksjepost](aksjepost.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:har_antall_aksjer |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:har_antall_aksjer |




## LinkML Source

<details>
```yaml
name: har_antall_aksjer
description: Tal aksjar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain_of:
- Aksjekapital
- Aksjepost
range: integer
inlined: true

```
</details>