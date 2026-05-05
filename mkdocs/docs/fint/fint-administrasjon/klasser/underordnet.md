

# Slot: underordnet 



URI: [https://schema.fintlabs.no/administrasjon/:underordnet](https://schema.fintlabs.no/administrasjon/:underordnet)
Alias: underordnet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Ansvar](ansvar.md), [Funksjon](funksjon.md), [Prosjektart](prosjektart.md), [Organisasjonselement](organisasjonselement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:underordnet |
| native | https://schema.fintlabs.no/administrasjon/:underordnet |




## LinkML Source

<details>
```yaml
name: underordnet
alias: underordnet
domain_of:
- Ansvar
- Funksjon
- Prosjektart
- Organisasjonselement
range: string

```
</details>