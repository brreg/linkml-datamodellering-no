

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/arkiv/:gyldighetsperiode](https://schema.fintlabs.no/arkiv/:gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [DokumentType](DokumentType.md) | Type dokument |  no  |
| [AdministrativEnhet](AdministrativEnhet.md) | Administrativ eining med ansvar for saksbehandling |  no  |
| [KorrespondansepartType](KorrespondansepartType.md) | Type korrespondansepart |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Saksmappetype](Saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |  no  |
| [Tilgangsgruppe](Tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |  no  |
| [Klassifikasjonstype](Klassifikasjonstype.md) | Type klassifikasjonssystem |  no  |
| [DokumentStatus](DokumentStatus.md) | Status til eit dokument |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Identifikator](Identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Saksstatus](Saksstatus.md) | Status til saksmappa |  no  |
| [Skjermingshjemmel](Skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |  no  |
| [Format](Format.md) | Dokumentets filformat |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [TilknyttetRegistreringSom](TilknyttetRegistreringSom.md) | Kva rolle dokumentet har i høve registreringa (t |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Rolle](Rolle.md) | Rolla til ein arkivressurs |  no  |
| [Merknadstype](Merknadstype.md) | Namn på type merknad |  no  |
| [JournalStatus](JournalStatus.md) | Status til journalposten |  no  |
| [PartRolle](PartRolle.md) | Rolla til ein part |  no  |
| [JournalpostType](JournalpostType.md) | Namn på type journalpost |  no  |
| [Tilgangsrestriksjon](Tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |  no  |
| [Variantformat](Variantformat.md) | Angiving av kva variant eit dokument førekjem i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AdministrativEnhet](AdministrativEnhet.md), [DokumentStatus](DokumentStatus.md), [DokumentType](DokumentType.md), [Format](Format.md), [JournalpostType](JournalpostType.md), [JournalStatus](JournalStatus.md), [Klassifikasjonstype](Klassifikasjonstype.md), [KorrespondansepartType](KorrespondansepartType.md), [Merknadstype](Merknadstype.md), [PartRolle](PartRolle.md), [Rolle](Rolle.md), [Saksmappetype](Saksmappetype.md), [Saksstatus](Saksstatus.md), [Skjermingshjemmel](Skjermingshjemmel.md), [Tilgangsgruppe](Tilgangsgruppe.md), [Tilgangsrestriksjon](Tilgangsrestriksjon.md), [TilknyttetRegistreringSom](TilknyttetRegistreringSom.md), [Variantformat](Variantformat.md), [Begrep](Begrep.md), [Identifikator](Identifikator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:gyldighetsperiode |
| native | https://schema.fintlabs.no/arkiv/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- AdministrativEnhet
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
- Begrep
- Identifikator
range: string

```
</details>