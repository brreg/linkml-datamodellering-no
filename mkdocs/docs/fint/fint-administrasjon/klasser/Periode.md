

# Slot: periode 



URI: [https://schema.fintlabs.no/administrasjon/:periode](https://schema.fintlabs.no/administrasjon/:periode)
Alias: periode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Lonn](lonn.md), [Fravaer](fravaer.md) |

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