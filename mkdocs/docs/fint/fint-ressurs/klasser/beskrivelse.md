

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/ressurs/:beskrivelse](https://schema.fintlabs.no/ressurs/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  no  |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Applikasjon](applikasjon.md), [Applikasjonsressurs](applikasjonsressurs.md), [Rettighet](rettighet.md), [Periode](periode.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:beskrivelse |
| native | https://schema.fintlabs.no/ressurs/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
alias: beskrivelse
domain_of:
- Applikasjon
- Applikasjonsressurs
- Rettighet
- Periode
range: string

```
</details>