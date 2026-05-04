

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/administrasjon/:beskrivelse](https://schema.fintlabs.no/administrasjon/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Rolle](Rolle.md) | Rettighet eller type fullmakt |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Lonn](Lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Lonn](Lonn.md), [Rolle](Rolle.md), [Periode](Periode.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:beskrivelse |
| native | https://schema.fintlabs.no/administrasjon/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
alias: beskrivelse
domain_of:
- Lonn
- Rolle
- Periode
range: string

```
</details>