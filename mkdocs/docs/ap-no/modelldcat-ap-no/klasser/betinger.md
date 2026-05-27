

# Slot: betinger 


_Modellelement betingelsesregelen avgrensar (modelldcatno:constrains)._





URI: [modelldcatno:constrains](https://data.norge.no/vocabulary/modelldcatno#constrains)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  yes  |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](modellelement.md) |
| Domain Of | [Betingelsesregel](betingelsesregel.md) |
| Slot URI | [modelldcatno:constrains](https://data.norge.no/vocabulary/modelldcatno#constrains) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:constrains |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/betinger |




## LinkML Source

<details>
```yaml
name: betinger
description: Modellelement betingelsesregelen avgrensar (modelldcatno:constrains).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:constrains
domain_of:
- Betingelsesregel
range: Modellelement
multivalued: true

```
</details>