

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/okonomi/:beskrivelse](https://schema.fintlabs.no/okonomi/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Transaksjon](transaksjon.md), [Periode](periode.md) |

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