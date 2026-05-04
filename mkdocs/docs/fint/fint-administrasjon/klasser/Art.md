

# Slot: art 



URI: [https://schema.fintlabs.no/administrasjon/:art](https://schema.fintlabs.no/administrasjon/:art)
Alias: art

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Lonsart](Lonsart.md) | Type ytelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontostreng](Kontostreng.md), [Lonsart](Lonsart.md), [Fullmakt](Fullmakt.md), [Arbeidsforhold](Arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:art |
| native | https://schema.fintlabs.no/administrasjon/:art |




## LinkML Source

<details>
```yaml
name: art
alias: art
domain_of:
- Kontostreng
- Lonsart
- Fullmakt
- Arbeidsforhold
range: string

```
</details>