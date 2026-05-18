

# Slot: eigenskapsmerknad 


_Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote)._





URI: [modelldcatno:propertyNote](https://data.norge.no/vocabulary/modelldcatno#propertyNote)
Alias: eigenskapsmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [modelldcatno:propertyNote](https://data.norge.no/vocabulary/modelldcatno#propertyNote) |

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
| self | modelldcatno:propertyNote |
| native | https://data.norge.no/linkml/modelldcat-ap-no/eigenskapsmerknad |




## LinkML Source

<details>
```yaml
name: eigenskapsmerknad
description: Fritekstmerknad om ein eigenskap (modelldcatno:propertyNote).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:propertyNote
alias: eigenskapsmerknad
domain_of:
- Merknad
range: LangString
multivalued: true

```
</details>