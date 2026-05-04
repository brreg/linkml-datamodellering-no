

# Slot: periode 



URI: [https://schema.fintlabs.no/administrasjon/:periode](https://schema.fintlabs.no/administrasjon/:periode)
Alias: periode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Lonn](Lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Lonn](Lonn.md), [Fravaer](Fravaer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:periode |
| native | https://schema.fintlabs.no/administrasjon/:periode |




## LinkML Source

<details>
```yaml
name: periode
alias: periode
domain_of:
- Lonn
- Fravaer
range: string

```
</details>