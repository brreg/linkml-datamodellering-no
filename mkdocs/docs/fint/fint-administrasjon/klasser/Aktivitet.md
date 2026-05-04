

# Slot: aktivitet 



URI: [https://schema.fintlabs.no/administrasjon/:aktivitet](https://schema.fintlabs.no/administrasjon/:aktivitet)
Alias: aktivitet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontostreng](Kontostreng.md), [Fullmakt](Fullmakt.md), [Arbeidsforhold](Arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:aktivitet |
| native | https://schema.fintlabs.no/administrasjon/:aktivitet |




## LinkML Source

<details>
```yaml
name: aktivitet
alias: aktivitet
domain_of:
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: string

```
</details>