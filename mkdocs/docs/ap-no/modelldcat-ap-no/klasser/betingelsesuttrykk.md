

# Slot: betingelsesuttrykk 


_Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression)._





URI: [modelldcatno:constraintExpression](https://data.norge.no/vocabulary/modelldcatno#constraintExpression)
Alias: betingelsesuttrykk

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
| Range | [LangString](LangString.md) |
| Domain Of | [Betingelsesregel](Betingelsesregel.md) |
| Slot URI | [modelldcatno:constraintExpression](https://data.norge.no/vocabulary/modelldcatno#constraintExpression) |

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
| self | modelldcatno:constraintExpression |
| native | https://data.norge.no/linkml/modelldcat-ap-no/betingelsesuttrykk |




## LinkML Source

<details>
```yaml
name: betingelsesuttrykk
description: Formelt uttrykk for betingelsesregelen (modelldcatno:constraintExpression).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:constraintExpression
alias: betingelsesuttrykk
domain_of:
- Betingelsesregel
range: LangString
multivalued: true

```
</details>