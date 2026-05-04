

# Slot: har_type 


_Type modellelement for eigenskapen (modelldcatno:hasType)._





URI: [modelldcatno:hasType](https://data.norge.no/vocabulary/modelldcatno#hasType)
Alias: har_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NoenAv](NoenAv.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Realisering](Realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Assosiasjon](Assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [Sammensetning](Sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [Spesialisering](Spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Rolle](Rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Avhengighet](Avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Eigenskap](Eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Samling](Samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Valg](Valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [Abstraksjon](Abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [AlleAv](AlleAv.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Attributt](Attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](Modellelement.md) |
| Domain Of | [Eigenskap](Eigenskap.md) |
| Slot URI | [modelldcatno:hasType](https://data.norge.no/vocabulary/modelldcatno#hasType) |

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
| self | modelldcatno:hasType |
| native | https://data.norge.no/linkml/modelldcat-ap-no/har_type |




## LinkML Source

<details>
```yaml
name: har_type
description: Type modellelement for eigenskapen (modelldcatno:hasType).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:hasType
alias: har_type
domain_of:
- Eigenskap
range: Modellelement
multivalued: true

```
</details>