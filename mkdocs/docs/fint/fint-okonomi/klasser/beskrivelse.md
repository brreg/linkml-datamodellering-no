

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/okonomi/:beskrivelse](https://schema.fintlabs.no/okonomi/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Transaksjon](Transaksjon.md), [Periode](Periode.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:beskrivelse |
| native | https://schema.fintlabs.no/okonomi/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
alias: beskrivelse
domain_of:
- Transaksjon
- Periode
range: string

```
</details>