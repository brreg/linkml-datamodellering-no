

# Slot: person 



URI: [https://schema.fintlabs.no/utdanning/:person](https://schema.fintlabs.no/utdanning/:person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtUngdom](OtUngdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  no  |
| [Laerling](Laerling.md) | Ein lærling i yrkesopplæring |  no  |
| [Skoleressurs](Skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  no  |
| [Elev](Elev.md) | Ein elev registrert i skulesystemet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Elev](Elev.md), [Skoleressurs](Skoleressurs.md), [Laerling](Laerling.md), [OtUngdom](OtUngdom.md) |

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