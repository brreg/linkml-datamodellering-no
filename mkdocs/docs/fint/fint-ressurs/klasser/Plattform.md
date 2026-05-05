

# Slot: plattform 



URI: [https://schema.fintlabs.no/ressurs/:plattform](https://schema.fintlabs.no/ressurs/:plattform)
Alias: plattform

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  no  |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Applikasjon](applikasjon.md), [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:plattform |
| native | https://schema.fintlabs.no/ressurs/:plattform |




## LinkML Source

<details>
```yaml
name: plattform
alias: plattform
domain_of:
- Applikasjon
- DigitalEnhet
- Enhetsgruppe
range: string

```
</details>