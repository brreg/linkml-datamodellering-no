

# Slot: betinger 


_Modellelement betingelsesregelen avgrensar (modelldcatno:constrains)._





URI: [modelldcatno:constrains](https://data.norge.no/vocabulary/modelldcatno#constrains)
Alias: betinger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Betingelsesregel](Betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  yes  |
| [XEllerY](XEllerY.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Og](Og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Eller](Eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [Ikke](Ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](Modellelement.md) |
| Domain Of | [Betingelsesregel](Betingelsesregel.md) |
| Slot URI | [modelldcatno:constrains](https://data.norge.no/vocabulary/modelldcatno#constrains) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:constrains |
| native | https://data.norge.no/linkml/modelldcat-ap-no/betinger |




## LinkML Source

<details>
```yaml
name: betinger
description: Modellelement betingelsesregelen avgrensar (modelldcatno:constrains).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:constrains
alias: betinger
domain_of:
- Betingelsesregel
range: Modellelement
multivalued: true

```
</details>