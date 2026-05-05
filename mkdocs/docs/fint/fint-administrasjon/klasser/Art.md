

# Slot: art 



URI: [https://schema.fintlabs.no/administrasjon/:art](https://schema.fintlabs.no/administrasjon/:art)
Alias: art

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Lonsart](lonsart.md) | Type ytelse |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Lonsart](lonsart.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |

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