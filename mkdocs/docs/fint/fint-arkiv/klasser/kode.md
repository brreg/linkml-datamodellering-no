

# Slot: kode 


_Verdi som identifiserer omgrepet._





URI: [fint:kode](https://schema.fintlabs.no/kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KorrespondansepartType](korrespondanseparttype.md) | Type korrespondansepart |  yes  |
| [Merknadstype](merknadstype.md) | Namn på type merknad |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Format](format.md) | Dokumentets filformat |  yes  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [JournalpostType](journalposttype.md) | Namn på type journalpost |  yes  |
| [Klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |  yes  |
| [PartRolle](partrolle.md) | Rolla til ein part |  yes  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Variantformat](variantformat.md) | Angiving av kva variant eit dokument førekjem i |  yes  |
| [JournalStatus](journalstatus.md) | Status til journalposten |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [DokumentStatus](dokumentstatus.md) | Status til eit dokument |  yes  |
| [Skjermingshjemmel](skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |  yes  |
| [Rolle](rolle.md) | Rolla til ein arkivressurs |  yes  |
| [Tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |  yes  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [DokumentType](dokumenttype.md) | Type dokument |  yes  |
| [Saksmappetype](saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Tilgangsrestriksjon](tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |  yes  |
| [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Kva rolle dokumentet har i høve registreringa (t |  yes  |
| [Saksstatus](saksstatus.md) | Status til saksmappa |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Begrep](begrep.md), [DokumentStatus](dokumentstatus.md), [DokumentType](dokumenttype.md), [Format](format.md), [JournalpostType](journalposttype.md), [JournalStatus](journalstatus.md), [Klassifikasjonstype](klassifikasjonstype.md), [KorrespondansepartType](korrespondanseparttype.md), [Merknadstype](merknadstype.md), [PartRolle](partrolle.md), [Rolle](rolle.md), [Saksmappetype](saksmappetype.md), [Saksstatus](saksstatus.md), [Skjermingshjemmel](skjermingshjemmel.md), [Tilgangsgruppe](tilgangsgruppe.md), [Tilgangsrestriksjon](tilgangsrestriksjon.md), [TilknyttetRegistreringSom](tilknyttetregistreringsom.md), [Variantformat](variantformat.md) |
| Slot URI | [fint:kode](https://schema.fintlabs.no/kode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kode |
| native | https://schema.fintlabs.no/:kode |




## LinkML Source

<details>
```yaml
name: kode
description: Verdi som identifiserer omgrepet.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:kode
alias: kode
domain_of:
- Begrep
- DokumentStatus
- DokumentType
- Format
- JournalpostType
- JournalStatus
- Klassifikasjonstype
- KorrespondansepartType
- Merknadstype
- PartRolle
- Rolle
- Saksmappetype
- Saksstatus
- Skjermingshjemmel
- Tilgangsgruppe
- Tilgangsrestriksjon
- TilknyttetRegistreringSom
- Variantformat
range: string

```
</details>