

# Slot: organisasjonsnummer 



URI: [https://schema.fintlabs.no/arkiv/:organisasjonsnummer](https://schema.fintlabs.no/arkiv/:organisasjonsnummer)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md), [Korrespondansepart](korrespondansepart.md), [Part](part.md), [Enhet](enhet.md) |

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