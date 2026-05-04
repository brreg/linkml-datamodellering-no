

# Slot: arbeidsforhold 



URI: [https://schema.fintlabs.no/administrasjon/:arbeidsforhold](https://schema.fintlabs.no/administrasjon/:arbeidsforhold)
Alias: arbeidsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AdministrasjonContainer](AdministrasjonContainer.md), [Fastlonn](Fastlonn.md), [Fasttillegg](Fasttillegg.md), [Variabellonn](Variabellonn.md), [Fravaer](Fravaer.md), [Arbeidslokasjon](Arbeidslokasjon.md), [Organisasjonselement](Organisasjonselement.md), [Personalressurs](Personalressurs.md) |

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