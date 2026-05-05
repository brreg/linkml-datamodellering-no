

# Slot: organisasjonsnummer 


_Organisasjonsnummer er i Norge et ni-sifret registreringsnummer som tildeles av Enhetsregisteret ved Brønnøysundregistrene for en organisasjon (foretak, idrettslag og lignende)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrivatVirksomhet](privatvirksomhet.md) | Virksomhet, eller foretak, er betegnelser for en juridisk person eller en org... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [PrivatVirksomhet](privatvirksomhet.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | samtbuskole:organisasjonsnummer |
| exact | adms:identifier |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Organisasjonsnummer er i Norge et ni-sifret registreringsnummer som tildeles
  av Enhetsregisteret ved Brønnøysundregistrene for en organisasjon (foretak, idrettslag
  og lignende).
from_schema: https://example.no/ontology/samt-bu-skole
exact_mappings:
- adms:identifier
rank: 1000
slot_uri: dct:identifier
alias: organisasjonsnummer
domain_of:
- PrivatVirksomhet
range: string

```
</details>