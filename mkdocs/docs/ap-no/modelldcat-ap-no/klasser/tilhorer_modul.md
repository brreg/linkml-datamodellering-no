

# Slot: tilhorer_modul 


_Modul dette elementet tilhøyrer (modelldcatno:belongsToModule)._





URI: [modelldcatno:belongsToModule](https://data.norge.no/vocabulary/modelldcatno#belongsToModule)
Alias: tilhorer_modul

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modul](modul.md) |
| Domain Of | [Modellelement](modellelement.md), [Eigenskap](eigenskap.md), [Merknad](merknad.md) |
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