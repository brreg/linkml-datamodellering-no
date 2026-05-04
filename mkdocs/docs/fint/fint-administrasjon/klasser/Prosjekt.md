

# Slot: prosjekt 



URI: [https://schema.fintlabs.no/administrasjon/:prosjekt](https://schema.fintlabs.no/administrasjon/:prosjekt)
Alias: prosjekt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Prosjektart](Prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AdministrasjonContainer](AdministrasjonContainer.md), [Kontostreng](Kontostreng.md), [Prosjektart](Prosjektart.md), [Fullmakt](Fullmakt.md), [Arbeidsforhold](Arbeidsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:prosjekt |
| native | https://schema.fintlabs.no/administrasjon/:prosjekt |




## LinkML Source

<details>
```yaml
name: prosjekt
alias: prosjekt
domain_of:
- AdministrasjonContainer
- Kontostreng
- Prosjektart
- Fullmakt
- Arbeidsforhold
range: string

```
</details>