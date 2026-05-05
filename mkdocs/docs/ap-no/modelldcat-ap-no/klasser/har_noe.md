

# Slot: har_noe 


_Modellelement som inngår i valet (modelldcatno:hasSome)._





URI: [modelldcatno:hasSome](https://data.norge.no/vocabulary/modelldcatno#hasSome)
Alias: har_noe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](modellelement.md) |
| Domain Of | [Valg](valg.md) |
| Slot URI | [modelldcatno:hasSome](https://data.norge.no/vocabulary/modelldcatno#hasSome) |

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
| self | modelldcatno:hasSome |
| native | https://data.norge.no/linkml/modelldcat-ap-no/har_noe |




## LinkML Source

<details>
```yaml
name: har_noe
description: Modellelement som inngår i valet (modelldcatno:hasSome).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:hasSome
alias: har_noe
domain_of:
- Valg
range: Modellelement
multivalued: true

```
</details>