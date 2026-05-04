

# Slot: navigerbar 


_Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable)._





URI: [modelldcatno:navigable](https://data.norge.no/vocabulary/modelldcatno#navigable)
Alias: navigerbar

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
| Range | [Boolean](Boolean.md) |
| Domain Of | [Eigenskap](Eigenskap.md) |
| Slot URI | [modelldcatno:navigable](https://data.norge.no/vocabulary/modelldcatno#navigable) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:navigable |
| native | https://data.norge.no/linkml/modelldcat-ap-no/navigerbar |




## LinkML Source

<details>
```yaml
name: navigerbar
description: Om eigenskapen er navigerbar i begge retningar (modelldcatno:navigable).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:navigable
alias: navigerbar
domain_of:
- Eigenskap
range: boolean

```
</details>