

# Slot: har_eigenskap 


_Eigenskapar modellelementet har (modelldcatno:hasProperty)._





URI: [modelldcatno:hasProperty](https://data.norge.no/vocabulary/modelldcatno#hasProperty)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eigenskap](eigenskap.md) |
| Domain Of | [Modellelement](modellelement.md) |
| Slot URI | [modelldcatno:hasProperty](https://data.norge.no/vocabulary/modelldcatno#hasProperty) |

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
| self | modelldcatno:hasProperty |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/har_eigenskap |




## LinkML Source

<details>
```yaml
name: har_eigenskap
description: Eigenskapar modellelementet har (modelldcatno:hasProperty).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:hasProperty
domain_of:
- Modellelement
range: Eigenskap
multivalued: true

```
</details>