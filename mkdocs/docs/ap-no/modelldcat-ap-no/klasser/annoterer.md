

# Slot: annoterer 


_Modellelement denne merknaden gjeld (modelldcatno:annotates)._





URI: [modelldcatno:annotates](https://data.norge.no/vocabulary/modelldcatno#annotates)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](modellelement.md) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [modelldcatno:annotates](https://data.norge.no/vocabulary/modelldcatno#annotates) |

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
| self | modelldcatno:annotates |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/annoterer |




## LinkML Source

<details>
```yaml
name: annoterer
description: Modellelement denne merknaden gjeld (modelldcatno:annotates).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:annotates
domain_of:
- Merknad
range: Modellelement
multivalued: true

```
</details>