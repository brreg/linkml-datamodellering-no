

# Slot: organisasjonsnummer 



URI: [https://schema.fintlabs.no/arkiv/:organisasjonsnummer](https://schema.fintlabs.no/arkiv/:organisasjonsnummer)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Korrespondansepart](Korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Part](Part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md), [Korrespondansepart](Korrespondansepart.md), [Part](Part.md), [Enhet](Enhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:organisasjonsnummer |
| native | https://schema.fintlabs.no/arkiv/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
alias: organisasjonsnummer
domain_of:
- SoeknadDrosjeloeyve
- Korrespondansepart
- Part
- Enhet
range: string

```
</details>