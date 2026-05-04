

# Slot: tilhorer_modul 


_Modul dette elementet tilhøyrer (modelldcatno:belongsToModule)._





URI: [modelldcatno:belongsToModule](https://data.norge.no/vocabulary/modelldcatno#belongsToModule)
Alias: tilhorer_modul

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NoenAv](NoenAv.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Kodeliste](Kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Spesialisering](Spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Og](Og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Datatype](Datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Sammensetning](Sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [EnkelType](EnkelType.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Rolle](Rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Valg](Valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [Merknad](Merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |
| [AlleAv](AlleAv.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Assosiasjon](Assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [Betingelsesregel](Betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [Avhengighet](Avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Eigenskap](Eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Samling](Samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Eller](Eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [Ikke](Ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |
| [Modul](Modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Realisering](Realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [XEllerY](XEllerY.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Modellelement](Modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [RootObjekttype](RootObjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Abstraksjon](Abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [Objekttype](Objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [Attributt](Attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modul](Modul.md) |
| Domain Of | [Modellelement](Modellelement.md), [Eigenskap](Eigenskap.md), [Merknad](Merknad.md) |
| Slot URI | [modelldcatno:belongsToModule](https://data.norge.no/vocabulary/modelldcatno#belongsToModule) |

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
| self | modelldcatno:belongsToModule |
| native | https://data.norge.no/linkml/modelldcat-ap-no/tilhorer_modul |




## LinkML Source

<details>
```yaml
name: tilhorer_modul
description: Modul dette elementet tilhøyrer (modelldcatno:belongsToModule).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:belongsToModule
alias: tilhorer_modul
domain_of:
- Modellelement
- Eigenskap
- Merknad
range: Modul
multivalued: true

```
</details>