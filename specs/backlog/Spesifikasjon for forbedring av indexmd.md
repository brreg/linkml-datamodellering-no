# Tillegg til spesifikasjon – lokale/importerte klassar og valideringspresentasjon

## Lokale og importerte klassar

### Anbefaling

Gjer skilnaden synleg direkte i seksjonshovudet.

Eksempel:

Classes (19 lokale)

Deretter ei kort forklaring:

«Denne oversikta viser berre klassar definert i cpsv-ap-no. Importerte klassar frå common-ap-no og andre avhengigheiter er utelatne frå lista, men kan inngå i valideringsresultat, diagram og andre analysar.»

### Vidare anbefaling

Bruk same mønster for andre seksjonar:

- Classes (19 lokale)
- Slots (65 lokale)
- Enumerations (0 lokale)
- Types (7 lokale)

Importerte element blir framleis dokumenterte separat gjennom eigne referansar til importerte modellar.

---

## Revidert anbefaling for valideringsresultat

### Tidlegare vurdering

Å flytte heile valideringsrapporten høgare opp i dokumentet er lite eigna for store modellar.

For omfattande modellar kan valideringsseksjonen innehalde mange feil, åtvaringar og detaljar som skaper unødvendig visuell støy for vanlege lesarar.

### Ny anbefaling

Behald den detaljerte valideringsrapporten lenger ned i dokumentet.

Vis i staden eit kort samandrag tidleg på sida, til dømes etter metadata.

Eksempel:

Valideringsstatus

❌ Ikkje godkjent
3 feil · 23 åtvaringar

Sjå detaljert rapport lenger ned.

### Presentasjon av detaljrapport

Detaljrapporten bør visast i ei kollapsbar blokk.

Eksempel:

<details>
<summary>Vis valideringsdetaljar (3 feil, 23 åtvaringar)</summary>

... detaljerte resultat ...

</details>

### Alternativ løysing

Dersom generatoren støttar interne lenker:

- Vis eit kort samandrag nær toppen.
- Legg inn lenke til seksjonen «Valideringsresultat» lenger ned.

Dette gir:

- rask oversikt over modellstatus
- mindre scrolling
- mindre visuell støy
- full sporbarheit for dei som ønskjer detaljane

### Akseptansekriterium

- Modellstatus er synleg utan mykje scrolling.
- Full valideringsrapport er framleis tilgjengeleg.
- Store rapportar dominerer ikkje dokumentet visuelt.
- Dokumentet fungerer godt også for modellar med mange valideringsfunn.
