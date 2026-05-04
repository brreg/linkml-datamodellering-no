

# Slot: overordnet 



URI: [https://schema.fintlabs.no/administrasjon/:overordnet](https://schema.fintlabs.no/administrasjon/:overordnet)
Alias: overordnet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Funksjon](Funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Prosjektart](Prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Ansvar](Ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Ansvar](Ansvar.md), [Funksjon](Funksjon.md), [Prosjektart](Prosjektart.md), [Organisasjonselement](Organisasjonselement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:overordnet |
| native | https://schema.fintlabs.no/administrasjon/:overordnet |




## LinkML Source

<details>
```yaml
name: overordnet
alias: overordnet
domain_of:
- Ansvar
- Funksjon
- Prosjektart
- Organisasjonselement
range: string

```
</details>