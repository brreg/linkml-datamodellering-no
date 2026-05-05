

# Slot: organisasjonselement 



URI: [https://schema.fintlabs.no/administrasjon/:organisasjonselement](https://schema.fintlabs.no/administrasjon/:organisasjonselement)
Alias: organisasjonselement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Ansvar](ansvar.md), [Fullmakt](fullmakt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:organisasjonselement |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonselement |




## LinkML Source

<details>
```yaml
name: organisasjonselement
alias: organisasjonselement
domain_of:
- AdministrasjonContainer
- Ansvar
- Fullmakt
range: string

```
</details>