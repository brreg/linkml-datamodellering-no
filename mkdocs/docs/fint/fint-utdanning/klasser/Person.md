

# Slot: person 



URI: [https://schema.fintlabs.no/utdanning/:person](https://schema.fintlabs.no/utdanning/:person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  no  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  no  |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  no  |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Elev](elev.md), [Skoleressurs](skoleressurs.md), [Laerling](laerling.md), [OtUngdom](otungdom.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:person |
| native | https://schema.fintlabs.no/utdanning/:person |




## LinkML Source

<details>
```yaml
name: person
alias: person
domain_of:
- Elev
- Skoleressurs
- Laerling
- OtUngdom
range: string

```
</details>