

# Slot: diverse 



URI: [https://schema.fintlabs.no/administrasjon/:diverse](https://schema.fintlabs.no/administrasjon/:diverse)
Alias: diverse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:diverse |
| native | https://schema.fintlabs.no/administrasjon/:diverse |




## LinkML Source

<details>
```yaml
name: diverse
alias: diverse
domain_of:
- AdministrasjonContainer
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: string

```
</details>