

# Slot: begrep 


_Fagomgrep ressursen handlar om (dct:subject)._





URI: [dct:subject](http://purl.org/dc/terms/subject)
Alias: begrep

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NoenAv](NoenAv.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Kodeliste](Kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Spesialisering](Spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Datatype](Datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Kodeelement](Kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |  yes  |
| [Sammensetning](Sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [EnkelType](EnkelType.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Rolle](Rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Valg](Valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [AlleAv](AlleAv.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Assosiasjon](Assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [Avhengighet](Avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Eigenskap](Eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Samling](Samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Modul](Modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Realisering](Realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Modellelement](Modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [RootObjekttype](RootObjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Abstraksjon](Abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [Objekttype](Objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [Attributt](Attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [Informasjonsmodell](Informasjonsmodell.md), [Modellelement](Modellelement.md), [Eigenskap](Eigenskap.md), [Kodeelement](Kodeelement.md) |
| Slot URI | [dct:subject](http://purl.org/dc/terms/subject) |

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
| self | dct:subject |
| native | https://data.norge.no/linkml/modelldcat-ap-no/begrep |




## LinkML Source

<details>
```yaml
name: begrep
description: Fagomgrep ressursen handlar om (dct:subject).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:subject
alias: begrep
domain_of:
- Informasjonsmodell
- Modellelement
- Eigenskap
- Kodeelement
range: Konsept
multivalued: true

```
</details>