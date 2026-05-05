

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/administrasjon/:beskrivelse](https://schema.fintlabs.no/administrasjon/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Lonn](lonn.md), [Rolle](rolle.md), [Periode](periode.md) |

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