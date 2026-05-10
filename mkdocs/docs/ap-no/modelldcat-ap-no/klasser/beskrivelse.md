

# Slot: beskrivelse 


_Fritekstbeskrivelse av ressursen (dct:description)._





URI: [dct:description](http://purl.org/dc/terms/description)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Modelkatalog](modelkatalog.md), [Informasjonsmodell](informasjonsmodell.md), [Modellelement](modellelement.md), [Eigenskap](eigenskap.md) |
| Slot URI | [dct:description](http://purl.org/dc/terms/description) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:description |
| native | https://data.norge.no/linkml/common-ap-no/beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Fritekstbeskrivelse av ressursen (dct:description).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: dct:description
alias: beskrivelse
domain_of:
- Modelkatalog
- Informasjonsmodell
- Modellelement
- Eigenskap
range: LangString
multivalued: true

```
</details>