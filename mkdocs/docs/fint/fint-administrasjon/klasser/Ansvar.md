

# Slot: ansvar 



URI: [https://schema.fintlabs.no/administrasjon/:ansvar](https://schema.fintlabs.no/administrasjon/:ansvar)
Alias: ansvar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AdministrasjonContainer](AdministrasjonContainer.md), [Kontostreng](Kontostreng.md), [Fullmakt](Fullmakt.md), [Organisasjonselement](Organisasjonselement.md), [Arbeidsforhold](Arbeidsforhold.md) |

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