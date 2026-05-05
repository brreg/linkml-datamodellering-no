

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/arkiv/:gyldighetsperiode](https://schema.fintlabs.no/arkiv/:gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknadstype](merknadstype.md) | Namn på type merknad |  no  |
| [Klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |  no  |
| [Rolle](rolle.md) | Rolla til ein arkivressurs |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Saksstatus](saksstatus.md) | Status til saksmappa |  no  |
| [KorrespondansepartType](korrespondanseparttype.md) | Type korrespondansepart |  no  |
| [DokumentType](dokumenttype.md) | Type dokument |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Kva rolle dokumentet har i høve registreringa (t |  no  |
| [Skjermingshjemmel](skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |  no  |
| [JournalpostType](journalposttype.md) | Namn på type journalpost |  no  |
| [JournalStatus](journalstatus.md) | Status til journalposten |  no  |
| [Variantformat](variantformat.md) | Angiving av kva variant eit dokument førekjem i |  no  |
| [DokumentStatus](dokumentstatus.md) | Status til eit dokument |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Format](format.md) | Dokumentets filformat |  no  |
| [AdministrativEnhet](administrativenhet.md) | Administrativ eining med ansvar for saksbehandling |  no  |
| [Tilgangsrestriksjon](tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |  no  |
| [Saksmappetype](saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |  no  |
| [PartRolle](partrolle.md) | Rolla til ein part |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [AdministrativEnhet](administrativenhet.md), [DokumentStatus](dokumentstatus.md), [DokumentType](dokumenttype.md), [Format](format.md), [JournalpostType](journalposttype.md), [JournalStatus](journalstatus.md), [Klassifikasjonstype](klassifikasjonstype.md), [KorrespondansepartType](korrespondanseparttype.md), [Merknadstype](merknadstype.md), [PartRolle](partrolle.md), [Rolle](rolle.md), [Saksmappetype](saksmappetype.md), [Saksstatus](saksstatus.md), [Skjermingshjemmel](skjermingshjemmel.md), [Tilgangsgruppe](tilgangsgruppe.md), [Tilgangsrestriksjon](tilgangsrestriksjon.md), [TilknyttetRegistreringSom](tilknyttetregistreringsom.md), [Variantformat](variantformat.md), [Begrep](begrep.md), [Identifikator](identifikator.md) |

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