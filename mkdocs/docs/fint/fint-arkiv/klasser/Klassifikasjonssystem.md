

# Slot: klassifikasjonssystem 



URI: [https://schema.fintlabs.no/arkiv/:klassifikasjonssystem](https://schema.fintlabs.no/arkiv/:klassifikasjonssystem)
Alias: klassifikasjonssystem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |  no  |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  no  |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md), [Arkivdel](arkivdel.md), [Klasse](klasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:klassifikasjonssystem |
| native | https://schema.fintlabs.no/arkiv/:klassifikasjonssystem |




## LinkML Source

<details>
```yaml
name: klassifikasjonssystem
alias: klassifikasjonssystem
domain_of:
- ArkivContainer
- Arkivdel
- Klasse
range: string

```
</details>