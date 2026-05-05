

# Slot: kontrakt 



URI: [https://schema.fintlabs.no/administrasjon/:kontrakt](https://schema.fintlabs.no/administrasjon/:kontrakt)
Alias: kontrakt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:kontrakt |
| native | https://schema.fintlabs.no/administrasjon/:kontrakt |




## LinkML Source

<details>
```yaml
name: kontrakt
alias: kontrakt
domain_of:
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: string

```
</details>