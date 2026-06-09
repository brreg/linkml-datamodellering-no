# Subset `Metadata` for AP-NO-klasser

## Bakgrunn

Domenemodeller som importerer dcat-ap-no, dqv-ap-no eller modelldcat-ap-no inneheld
både metadata-klasser (frå AP-NO) og datakassar (eigne domenemodell-klasser). Ei datafil
kan dermed innehalde ei blanding av begge typar instansar.

Ved å merke alle AP-NO-klassane med `in_subset: [Metadata]` vert det mogleg å skilje
metadata frå data i verktøy, visningar og eksportrutinar — t.d. filtrere ut berre
datasett-metadata frå ei datafil som elles inneheld domenedata.

## Løysing

### 1. Definer subset i `common-ap-no-schema.yaml`

Legg til `Metadata`-subset i `subsets:`-blokka i
`src/linkml/ap-no/common/common-ap-no-schema.yaml`, saman med dei eksisterande
`Obligatorisk`, `Anbefalt` og `Valgfri`:

```yaml
subsets:
  Obligatorisk:
    description: Obligatoriske eigenskapar i ein AP-NO-profil.
  Anbefalt:
    description: Anbefalte eigenskapar i ein AP-NO-profil.
  Valgfri:
    description: Valfrie eigenskapar i ein AP-NO-profil.
  Metadata:
    description: Klasser som beskriv metadata om ressursar, ikkje sjølve datainnhaldet.
```

### 2. Legg til `in_subset: [Metadata]` på alle klasser i dei tre skjemaa

`in_subset` vert lagt direkte på klassedefinisjonane (ikkje i `slot_usage`).

#### `dcat-ap-no-schema.yaml` — alle 16 klasser

- `KatalogisertRessurs`
- `Aktor`
- `Kontaktopplysning`
- `Tidsrom`
- `RegulativRessurs`
- `Identifikator`
- `Rettighetserklaring`
- `Sjekksum`
- `Gebyr`
- `Relasjon`
- `Distribusjon`
- `Datasett`
- `Datasettserie`
- `Datatjeneste`
- `Katalogpost`
- `Katalog`

#### `dqv-ap-no-schema.yaml` — alle 9 klasser

- `Kvalitetsdimensjon`
- `Kvalitetsdeldimensjon`
- `Kvalitetsmaal`
- `Kvalitetsmerknad`
- `Brukartilbakemelding`
- `Kvalitetssertifikat`
- `Kvalitetsmaaling`
- `Standard`
- `Tekstdel`

#### `modelldcat-ap-no-schema.yaml` — alle 31 klasser

- `KatalogisertRessurs`
- `Aktor`
- `Kontaktopplysning`
- `Standard`
- `Lisensdokument`
- `Lokasjon`
- `Tidsperiode`
- `Dokument`
- `Modellkatalog`
- `Informasjonsmodell`
- `Modellelement`
- `Objekttype`
- `RootObjekttype`
- `Datatype`
- `EnkelType`
- `Kodeliste`
- `Modul`
- `Eigenskap`
- `Attributt`
- `Assosiasjon`
- `Rolle`
- `Spesialisering`
- `Sammensetning`
- `Realisering`
- `Abstraksjon`
- `Avhengighet`
- `Samling`
- `Valg`
- `AlleAv`
- `NoenAv`
- `Merknad`
- `Betingelsesregel`
- `Og`
- `Eller`
- `XEllerY`
- `Ikke`
- `Kodeelement`

### Syntaks og viktig presisering

`in_subset` på klassar er ei liste. Dersom ein klasse allereie har `in_subset`-oppføring
på klassenivå, skal `Metadata` leggjast til i lista — aldri erstatte eksisterande verdiar.

Sjekk utført 2026-06-09: ingen av dei tre skjemaa har `in_subset` på klassenivå per no
(berre i `slot_usage`). Alle eksisterande `in_subset`-oppføringar er slot-innskrenkingar
(`Obligatorisk`, `Anbefalt`, `Valgfri`) og vert ikkje påverka av dette tiltaket.

Korrekt syntaks for ein klasse utan tidlegare klasse-subset:

```yaml
  Datasett:
    in_subset:
      - Metadata
    class_uri: dcat:Dataset
    ...
```

Korrekt syntaks dersom ein klasse i framtida skulle ha fleire klasse-subsets:

```yaml
  Datasett:
    in_subset:
      - Metadata
      - AnnaEksisterandeSubset
    class_uri: dcat:Dataset
    ...
```

## Bruk i domenemodeller

Etter at subsettet er innført kan verktøy og skript filtrere instansar i ei datafil
basert på om klassen er i `Metadata`-subsettet eller ikkje. Sjølve subset-definisjonen
vert arva via import-kjeda — domenemodeller treng ikkje gjere noko ekstra.

## Prioritert tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `common-ap-no-schema.yaml` | Legg til `Metadata`-subset i `subsets:`-blokka | Høg |
| 2 | `dcat-ap-no-schema.yaml` | `in_subset: [Metadata]` på alle 16 klasser | Høg |
| 3 | `dqv-ap-no-schema.yaml` | `in_subset: [Metadata]` på alle 9 klasser | Høg |
| 4 | `modelldcat-ap-no-schema.yaml` | `in_subset: [Metadata]` på alle 37 klasser | Høg |
