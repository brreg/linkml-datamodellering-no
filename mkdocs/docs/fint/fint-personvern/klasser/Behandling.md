

# Slot: behandling 



URI: [https://schema.fintlabs.no/personvern/:behandling](https://schema.fintlabs.no/personvern/:behandling)
Alias: behandling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](Tjeneste.md) | Teneste eller system som behandlar personopplysningar |  no  |
| [Samtykke](Samtykke.md) | Tillating til behandling av personopplysning |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Samtykke](Samtykke.md), [Tjeneste](Tjeneste.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:behandling |
| native | https://schema.fintlabs.no/personvern/:behandling |




## LinkML Source

<details>
```yaml
name: behandling
alias: behandling
domain_of:
- Samtykke
- Tjeneste
range: string

```
</details>