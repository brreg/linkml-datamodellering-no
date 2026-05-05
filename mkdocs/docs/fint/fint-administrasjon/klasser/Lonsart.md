

# Slot: lonsart 



URI: [https://schema.fintlabs.no/administrasjon/:lonsart](https://schema.fintlabs.no/administrasjon/:lonsart)
Alias: lonsart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fravaerstype](fravaerstype.md), [Fastlonn](fastlonn.md), [Fasttillegg](fasttillegg.md), [Variabellonn](variabellonn.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:lonsart |
| native | https://schema.fintlabs.no/administrasjon/:lonsart |




## LinkML Source

<details>
```yaml
name: lonsart
alias: lonsart
domain_of:
- Fravaerstype
- Fastlonn
- Fasttillegg
- Variabellonn
range: string

```
</details>