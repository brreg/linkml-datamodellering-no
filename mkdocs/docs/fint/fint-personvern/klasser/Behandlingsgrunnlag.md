

# Slot: behandlingsgrunnlag 



URI: [https://schema.fintlabs.no/personvern/:behandlingsgrunnlag](https://schema.fintlabs.no/personvern/:behandlingsgrunnlag)
Alias: behandlingsgrunnlag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](Behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |
| [PersonvernContainer](PersonvernContainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PersonvernContainer](PersonvernContainer.md), [Behandling](Behandling.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:behandlingsgrunnlag |
| native | https://schema.fintlabs.no/personvern/:behandlingsgrunnlag |




## LinkML Source

<details>
```yaml
name: behandlingsgrunnlag
alias: behandlingsgrunnlag
domain_of:
- PersonvernContainer
- Behandling
range: string

```
</details>