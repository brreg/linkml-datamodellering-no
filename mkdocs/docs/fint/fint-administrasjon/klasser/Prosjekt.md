

# Slot: prosjekt 



URI: [https://schema.fintlabs.no/administrasjon/:prosjekt](https://schema.fintlabs.no/administrasjon/:prosjekt)
Alias: prosjekt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Kontostreng](kontostreng.md), [Prosjektart](prosjektart.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |

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