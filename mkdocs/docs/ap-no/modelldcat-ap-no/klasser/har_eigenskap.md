

# Slot: har_eigenskap 


_Eigenskapar modellelementet har (modelldcatno:hasProperty)._





URI: [modelldcatno:hasProperty](https://data.norge.no/vocabulary/modelldcatno#hasProperty)
Alias: har_eigenskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnkelType](EnkelType.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Kodeliste](Kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Modellelement](Modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [RootObjekttype](RootObjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Datatype](Datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Objekttype](Objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [Modul](Modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eigenskap](Eigenskap.md) |
| Domain Of | [Modellelement](Modellelement.md) |
| Slot URI | [modelldcatno:hasProperty](https://data.norge.no/vocabulary/modelldcatno#hasProperty) |

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
| self | modelldcatno:hasProperty |
| native | https://data.norge.no/linkml/modelldcat-ap-no/har_eigenskap |




## LinkML Source

<details>
```yaml
name: har_eigenskap
description: Eigenskapar modellelementet har (modelldcatno:hasProperty).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:hasProperty
alias: har_eigenskap
domain_of:
- Modellelement
range: Eigenskap
multivalued: true

```
</details>