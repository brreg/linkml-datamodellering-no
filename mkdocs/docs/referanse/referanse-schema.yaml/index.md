# referanse-schema.yaml

[![Versjon](https://img.shields.io/badge/versjon-1.0.0-blue)]()
[![Status](https://img.shields.io/badge/status-UnderDevelopment |-blue)]()
[![Validering](https://img.shields.io/badge/bronze-ukjent-lightgrey)]()
[![Lisens](https://img.shields.io/badge/NLOD-2.0-blue)]()

---

## Modellmetadata

| Felt | Verdi |
| --- | --- |
| Schema URI | [https://example.org/linkml/referanse](https://example.org/linkml/referanse) |
| Versjon | 1.0.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgjevar | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | http://purl.org/adms/status/UnderDevelopment |
| Endringsdato | TODO |
| Utgivelsesdato | TODO |
| Imports | linkml:types<br>../ap-no/dcat-ap-no/dcat-ap-no-schema |


---

## Avhengigheiter

### Imports

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types  # direkte import
└── common-ap-no-schema  # transitiv import
    └── dcat-ap-no-schema  # direkte import
```

!!! note "Leseretning"
    Diagrammet ovanfor viser avhengigheiter **frå høgre til venstre**. Dette skjemaet
    importerer dei skjemaa som står lengst til høgre, som igjen automatisk inkluderer
    alle sine avhengigheiter lengre til venstre i treet.

*Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*


---

## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Ressurs](klasser/ressurs.md) | Ein generisk ressurs med tittel, skildring og utgjevar |











## Slots

| Slot | Description |
| --- | --- |
| [beskrivelse](klasser/beskrivelse.md) | Kortfatta skildring av ressursen |
| [id](klasser/id.md) | Unik URI-identifikator for ressursen |
| [tittel](klasser/tittel.md) | Namn eller tittel på ressursen |
| [utgjevar](klasser/utgjevar.md) | Organisasjon ansvarleg for ressursen (referert med URI) |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) |  |
| [Metadata](klasser/metadata.md) | Klasser som beskriv metadata om ressursar, ikkje sjølve datainnhaldet |
| [Obligatorisk](klasser/obligatorisk.md) |  |
| [Valgfri](klasser/valgfri.md) |  |

---

## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| ER-diagram (Mermaid) | [referanse-schema.yaml-erdiagram.md](referanse-schema.yaml-erdiagram.md) |

---

## Valideringsresultat

*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*

---

## Kontakt

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

