

# Slot: identifikator_literal 


_Tekstleg identifikator for ressursen (dct:identifier)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: identifikator_literal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Kodeelement](kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |  yes  |
| [Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Aktor](aktor.md), [Modelkatalog](modelkatalog.md), [Informasjonsmodell](informasjonsmodell.md), [Modellelement](modellelement.md), [Eigenskap](eigenskap.md), [Merknad](merknad.md), [Kodeelement](kodeelement.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | https://data.norge.no/linkml/modelldcat-ap-no/identifikator_literal |




## LinkML Source

<details>
```yaml
name: identifikator_literal
description: Tekstleg identifikator for ressursen (dct:identifier).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:identifier
alias: identifikator_literal
domain_of:
- Aktor
- Modelkatalog
- Informasjonsmodell
- Modellelement
- Eigenskap
- Merknad
- Kodeelement
range: string

```
</details>