

# Slot: klassifikasjonssystem 


_Klassifikasjonssystem._





URI: [ark:klassifikasjonssystem](https://schema.fintlabs.no/arkiv/klassifikasjonssystem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |  yes  |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  yes  |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klassifikasjonssystem](klassifikasjonssystem.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md), [Arkivdel](arkivdel.md), [Klasse](klasse.md) |
| Slot URI | [ark:klassifikasjonssystem](https://schema.fintlabs.no/arkiv/klassifikasjonssystem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:klassifikasjonssystem |
| native | https://schema.fintlabs.no/arkiv/:klassifikasjonssystem |




## LinkML Source

<details>
```yaml
name: klassifikasjonssystem
description: Klassifikasjonssystem.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:klassifikasjonssystem
domain_of:
- ArkivContainer
- Arkivdel
- Klasse
range: Klassifikasjonssystem

```
</details>