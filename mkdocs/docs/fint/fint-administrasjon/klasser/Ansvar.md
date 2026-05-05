

# Slot: ansvar 



URI: [https://schema.fintlabs.no/administrasjon/:ansvar](https://schema.fintlabs.no/administrasjon/:ansvar)
Alias: ansvar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Organisasjonselement](organisasjonselement.md), [Arbeidsforhold](arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:ansvar |
| native | https://schema.fintlabs.no/administrasjon/:ansvar |




## LinkML Source

<details>
```yaml
name: ansvar
alias: ansvar
domain_of:
- AdministrasjonContainer
- Kontostreng
- Fullmakt
- Organisasjonselement
- Arbeidsforhold
range: string

```
</details>