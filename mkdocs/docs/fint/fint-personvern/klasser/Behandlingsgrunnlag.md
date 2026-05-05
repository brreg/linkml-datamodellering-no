

# Slot: behandlingsgrunnlag 



URI: [https://schema.fintlabs.no/personvern/:behandlingsgrunnlag](https://schema.fintlabs.no/personvern/:behandlingsgrunnlag)
Alias: behandlingsgrunnlag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md), [Behandling](behandling.md) |

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