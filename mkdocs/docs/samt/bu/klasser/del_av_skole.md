

# Slot: del_av_skole 


_Skolen basisgruppa tilhører_





URI: [org:unitOf](http://www.w3.org/ns/org#unitOf)
Alias: del_av_skole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Basisgruppe](basisgruppe.md) | Skoleklasse som hovedsaklig samler elever i ulike fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skole](skole.md) |
| Domain | [Basisgruppe](basisgruppe.md) |
| Domain Of | [Basisgruppe](basisgruppe.md) |
| Slot URI | [org:unitOf](http://www.w3.org/ns/org#unitOf) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | org:unitOf |
| native | samtbuskole:del_av_skole |
| close | schema:isPartOf |




## LinkML Source

<details>
```yaml
name: del_av_skole
description: Skolen basisgruppa tilhører
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- schema:isPartOf
rank: 1000
domain: Basisgruppe
slot_uri: org:unitOf
alias: del_av_skole
domain_of:
- Basisgruppe
range: Skole

```
</details>