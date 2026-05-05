

# Slot: arbeidsforhold 



URI: [https://schema.fintlabs.no/administrasjon/:arbeidsforhold](https://schema.fintlabs.no/administrasjon/:arbeidsforhold)
Alias: arbeidsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Fastlonn](fastlonn.md), [Fasttillegg](fasttillegg.md), [Variabellonn](variabellonn.md), [Fravaer](fravaer.md), [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Personalressurs](personalressurs.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:arbeidsforhold |
| native | https://schema.fintlabs.no/administrasjon/:arbeidsforhold |




## LinkML Source

<details>
```yaml
name: arbeidsforhold
alias: arbeidsforhold
domain_of:
- AdministrasjonContainer
- Fastlonn
- Fasttillegg
- Variabellonn
- Fravaer
- Arbeidslokasjon
- Organisasjonselement
- Personalressurs
range: string

```
</details>