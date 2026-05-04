

# Slot: objekt 



URI: [https://schema.fintlabs.no/administrasjon/:objekt](https://schema.fintlabs.no/administrasjon/:objekt)
Alias: objekt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AdministrasjonContainer](AdministrasjonContainer.md), [Kontostreng](Kontostreng.md), [Fullmakt](Fullmakt.md), [Arbeidsforhold](Arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:objekt |
| native | https://schema.fintlabs.no/administrasjon/:objekt |




## LinkML Source

<details>
```yaml
name: objekt
alias: objekt
domain_of:
- AdministrasjonContainer
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: string

```
</details>