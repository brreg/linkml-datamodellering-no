

# Slot: horer_til_basisgruppe 


_Basisgruppe elev tilhører_





URI: [samtbuskole:horerTilBasisgruppe](https://example.no/ontology/skole#horerTilBasisgruppe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elev](elev.md) | En person som går på skole |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Basisgruppe](basisgruppe.md) |
| Domain | [Elev](elev.md) |
| Domain Of | [Elev](elev.md) |
| Slot URI | [samtbuskole:horerTilBasisgruppe](https://example.no/ontology/skole#horerTilBasisgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:horerTilBasisgruppe |
| native | samtbu:horer_til_basisgruppe |
| close | schema:memberOf |




## LinkML Source

<details>
```yaml
name: horer_til_basisgruppe
description: Basisgruppe elev tilhører
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- schema:memberOf
rank: 1000
domain: Elev
slot_uri: samtbuskole:horerTilBasisgruppe
domain_of:
- Elev
range: Basisgruppe

```
</details>