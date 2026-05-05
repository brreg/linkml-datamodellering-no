

# Slot: jobber_paa_skole 


_Skolen kontaktlæreren jobber på_





URI: [samtbuskole:jobber_paa_skole](https://example.no/ontology/skole#jobber_paa_skole)
Alias: jobber_paa_skole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerer](kontaktlaerer.md) | En lærer med ansvar for ei basisgruppe og er skolens kontaktpunkt for elevane... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skole](skole.md) |
| Domain | [Kontaktlaerer](kontaktlaerer.md) |
| Domain Of | [Kontaktlaerer](kontaktlaerer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:jobber_paa_skole |
| native | samtbuskole:jobber_paa_skole |
| close | schema:worksFor, org:memberOf |




## LinkML Source

<details>
```yaml
name: jobber_paa_skole
description: Skolen kontaktlæreren jobber på
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- schema:worksFor
- org:memberOf
rank: 1000
domain: Kontaktlaerer
alias: jobber_paa_skole
domain_of:
- Kontaktlaerer
range: Skole

```
</details>