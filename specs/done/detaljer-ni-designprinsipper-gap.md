# Meir detaljert gap-vurdering for "Ni designprinsipper for informasjonsmodellar"

## Bakgrunn

Brukaren peikte på `mkdocs/docs/arkitektur/standardetterleving.md` linje 54
("Ni designprinsipper for informasjonsmodellar" | ✅ | "I hovudsak utført.")
og ønskte ei meir detaljert beskriving av kva som faktisk står att.

Kjeldespecen `specs/done/avvik-prinsipper-informasjonsmodeller.md` (sist
oppdatert 2026-06-19) har full prinsipp-for-prinsipp-vurdering, men
`standardetterleving.md` sitt "Attverande gap"-avsnitt (rad 70-81) listar
berre 4 gap — ingen av dei knytt til dei 9 designprinsippa.

## Verifisering mot dagens repo-tilstand (2026-08-27)

Kjeldespecen er over to månadar gammal. Verifiserte følgjande mot faktisk
skjematilstand før oppdatering av doc-sida:

| Tidlegare gap (juni) | Status no |
|---|---|
| P1: `tema`-slot inkonsistent (uriorcurie vs Konsept) | **Lukka** — `dcat-ap-no` har no `range: Konsept`. `xkos-ap-no` har ikkje lenger `tema`-slot. Berre `cpsv-ap-no` brukar framleis `dct:subject` for `tema` (ikkje `dcat:theme`) — mindre presisjonsavvik, låg prioritet |
| P2: `description.md` manglar i 22/28 skjema | **I hovudsak lukka** — alle skjema har no `description.md`, unntatt tre interne test-/referanseskjema (`referansemodell-bronze/silver/gold`, brukt av MCP-validatoren, ikkje publiserte domenemodellar) |
| P3: `begrepsidentifikator` manglar på domenemodell-klassar | **Framleis ope** — finst berre i `oreg/*` (7 skjema) og `samt-bu`. Manglar heilt i `ngr-*` (4 skjema), `fint-*` (6 skjema), alle AP-NO-profilar (`dcat-ap-no`, `skos-ap-no`, `cpsv-ap-no`, `dqv-ap-no`, `modelldcat-*`, `xkos-ap-no`), `modellkatalog/*` (6 skjema) |
| P6: ingen `owl:sameAs`/cross-referanse for overlappande klassar | **Framleis ope** — `samt-bu` brukar `exact_mappings`/`close_mappings` (terminologimapping for SAMT-BU), men ingen kryssreferanse finst for det opphavlege problemet (NGR `Virksomhet`/DCAT `Aktor`/FINT-tilsvarande) |
| P7: FINT-skjema over 50-klassegrensa | **Framleis ope (akseptert avvik)** — `fint-utdanning` har 72 klassar, `fint-administrasjon` 34 |
| P8: `annotations.status` manglar i `dqv-core`/`modelldcat-modell` | **Lukka** — begge har no `status` |

## Tiltak

1. Utvid "Vurdering"-cella for rad 54 i Pilar 3-tabellen med konkrete
   attverande punkt (P3 og P6), i staden for berre "I hovudsak utført."
2. Legg til to nye rader i "Attverande gap"-tabellen (linje 72-77):
   - `begrepsidentifikator` manglar på domenemodell-klassar (P3)
   - Ingen `owl:sameAs`/kryssreferanse for semantisk overlappande klassar (P6)
3. Ikkje legg til FINT-klassegrensa (P7) som gap — det er eksplisitt eit
   akseptert avvik (jf. kjeldespec), ikkje eit uløyst problem.
4. Oppdater kjeldespecen (`avvik-prinsipper-informasjonsmodeller.md`) sitt
   "Samandrag"/"Prioritert handlingsliste" berre dersom avvik der reelt er
   feil — ikkje pålagt av denne oppgåva, då `specs/done/` normalt er urørt.
   **Avgjerd:** ikkje rør `specs/done/`-fila; ho er allereie internt
   konsistent (dei opne punkta ho listar stemmer framleis).

## Utført

- Verifiserte alle seks tidlegare rapporterte gap mot faktisk skjematilstand
- Oppdaterte `mkdocs/docs/arkitektur/standardetterleving.md`:
  - Rad 54 (Pilar 3-tabellen): utvida vurdering med konkrete attverande punkt
  - "Attverande gap"-tabellen: lagt til gap #5 (begrepsidentifikator, P3) og
    #6 (owl:sameAs-kryssreferanse, P6)
