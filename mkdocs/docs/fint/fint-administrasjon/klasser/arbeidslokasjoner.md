

# Slot: arbeidslokasjoner 



URI: [https://schema.fintlabs.no/administrasjon/:arbeidslokasjoner](https://schema.fintlabs.no/administrasjon/:arbeidslokasjoner)
Alias: arbeidslokasjoner

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidslokasjon](Arbeidslokasjon.md) |
| Domain Of | [AdministrasjonContainer](AdministrasjonContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdministrasjonContainer](AdministrasjonContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:arbeidslokasjoner |
| native | https://schema.fintlabs.no/administrasjon/:arbeidslokasjoner |




## LinkML Source

<details>
```yaml
name: arbeidslokasjoner
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: arbeidslokasjoner
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Arbeidslokasjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>