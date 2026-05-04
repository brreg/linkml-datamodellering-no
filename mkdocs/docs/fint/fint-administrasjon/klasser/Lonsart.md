

# Slot: lonsart 



URI: [https://schema.fintlabs.no/administrasjon/:lonsart](https://schema.fintlabs.no/administrasjon/:lonsart)
Alias: lonsart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Fravaerstype](Fravaerstype.md) | Type fråvær |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fravaerstype](Fravaerstype.md), [Fastlonn](Fastlonn.md), [Fasttillegg](Fasttillegg.md), [Variabellonn](Variabellonn.md) |

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