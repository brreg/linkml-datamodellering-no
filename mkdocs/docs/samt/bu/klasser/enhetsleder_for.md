

# Slot: enhetsleder_for 


_Enhet rektor er enhetsleder for_





URI: [samtbuskole:enhetsleder_for](https://example.no/ontology/skole#enhetsleder_for)
Alias: enhetsleder_for

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rektor](rektor.md) | Høgaste akademiske leder av en skole |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skole](skole.md) |
| Domain | [Rektor](rektor.md) |
| Domain Of | [Rektor](rektor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:enhetsleder_for |
| native | samtbuskole:enhetsleder_for |
| close | org:headOf |




## LinkML Source

<details>
```yaml
name: enhetsleder_for
description: Enhet rektor er enhetsleder for
from_schema: https://example.no/ontology/samt-bu-skole
close_mappings:
- org:headOf
rank: 1000
domain: Rektor
alias: enhetsleder_for
domain_of:
- Rektor
range: Skole

```
</details>