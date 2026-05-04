

# Slot: annoterer 


_Modellelement denne merknaden gjeld (modelldcatno:annotates)._





URI: [modelldcatno:annotates](https://data.norge.no/vocabulary/modelldcatno#annotates)
Alias: annoterer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Betingelsesregel](Betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [XEllerY](XEllerY.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Ikke](Ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |
| [Og](Og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Eller](Eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [Merknad](Merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](Modellelement.md) |
| Domain Of | [Merknad](Merknad.md) |
| Slot URI | [modelldcatno:annotates](https://data.norge.no/vocabulary/modelldcatno#annotates) |

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
| self | modelldcatno:annotates |
| native | https://data.norge.no/linkml/modelldcat-ap-no/annoterer |




## LinkML Source

<details>
```yaml
name: annoterer
description: Modellelement denne merknaden gjeld (modelldcatno:annotates).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:annotates
alias: annoterer
domain_of:
- Merknad
range: Modellelement
multivalued: true

```
</details>