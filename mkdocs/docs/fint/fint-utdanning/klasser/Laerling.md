

# Slot: laerling 



URI: [https://schema.fintlabs.no/utdanning/:laerling](https://schema.fintlabs.no/utdanning/:laerling)
Alias: laerling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |
| [AvlagtProve](AvlagtProve.md) | Ei avlagt prøve for ein lærling |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AvlagtProve](AvlagtProve.md), [Person](Person.md), [Virksomhet](Virksomhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:laerling |
| native | https://schema.fintlabs.no/utdanning/:laerling |




## LinkML Source

<details>
```yaml
name: laerling
alias: laerling
domain_of:
- AvlagtProve
- Person
- Virksomhet
range: string

```
</details>