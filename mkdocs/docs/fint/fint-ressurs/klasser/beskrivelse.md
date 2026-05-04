

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/ressurs/:beskrivelse](https://schema.fintlabs.no/ressurs/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurs](Applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |
| [Rettighet](Rettighet.md) | Ei namngitt rettighet |  no  |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Applikasjon](Applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Applikasjon](Applikasjon.md), [Applikasjonsressurs](Applikasjonsressurs.md), [Rettighet](Rettighet.md), [Periode](Periode.md) |

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