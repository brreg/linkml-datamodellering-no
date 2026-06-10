

# Slot: tilknyttet_basisgruppe 


_Basisgruppe kontaktlærer er tilknyttet_





URI: [samtbuskole:tilknyttetBasisgruppe](https://example.no/ontology/skole#tilknyttetBasisgruppe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerer](kontaktlaerer.md) | En lærer med ansvar for ei basisgruppe og er skolens kontaktpunkt for elevane... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Basisgruppe](basisgruppe.md) |
| Domain | [Kontaktlaerer](kontaktlaerer.md) |
| Domain Of | [Kontaktlaerer](kontaktlaerer.md) |
| Slot URI | [samtbuskole:tilknyttetBasisgruppe](https://example.no/ontology/skole#tilknyttetBasisgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:tilknyttetBasisgruppe |
| native | samtbu:tilknyttet_basisgruppe |
| close | schema:teaches |




## LinkML Source

<details>
```yaml
name: tilknyttet_basisgruppe
description: Basisgruppe kontaktlærer er tilknyttet
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- schema:teaches
rank: 1000
domain: Kontaktlaerer
slot_uri: samtbuskole:tilknyttetBasisgruppe
domain_of:
- Kontaktlaerer
range: Basisgruppe

```
</details>