# Spesifikasjon: Kjeldehenvisning og regeldekning i policies/README.md

## Bakgrunn

`src/mcp-linkml-validator/policies/README.md` viste policy-sjekkane med ei
`Regel`-kolonne som berre inneheldt nummer (t.d. «Digdir 10») — utan regelnamn,
utan lenkje til kjeldedokumentet og utan oversikt over kva reglar som *ikkje* er
automatisk evaluert.

Digdir sine
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(v1.0, juni 2022) er det normative grunnlaget for bronze/silver/gold-policyane.
Dokumentet inneheld 15 nummererte reglar fordelt på tre kategoriar:

| # | Namn | Kategori |
|---|---|---|
| 1 | Forståelighet | Generelle modelleringsreglar |
| 2 | Meningsfullhet | Generelle modelleringsreglar |
| 3 | Navne- og skrivekonvensjoner | Generelle modelleringsreglar |
| 4 | Identifiserbarhet | Generelle modelleringsreglar |
| 5 | Visualisering | Reglar for informasjonsmodellar |
| 6 | Modularitet | Reglar for informasjonsmodellar |
| 7 | Tilgjengeliggjøring | Reglar for informasjonsmodellar |
| 8 | Maskinprosserbarhet | Reglar for informasjonsmodellar |
| 9 | Datering | Reglar for informasjonsmodellar |
| 10 | Ansvar | Reglar for informasjonsmodellar |
| 11 | Modellstatus | Reglar for informasjonsmodellar |
| 12 | Sammenhenger mellom modeller | Reglar for informasjonsmodellar |
| 13 | Begreper | Reglar for modellelement og -eigenskapar |
| 14 | Gjenbruk | Reglar for modellelement og -eigenskapar |
| 15 | Standardiserte datatyper | Reglar for modellelement og -eigenskapar |

## Tiltak

1. Legg til innleiing med lenkje til Digdir-kjelda øvst i README.
2. Legg til ein tabell over alle 15 reglar med namn, kort skildring og kva policy som dekkjer dei (eller «Ikkje evaluert»).
3. Oppdater bronze- og silver-sjekklistene til å vise regelnamn ved sida av nummeret.
4. Legg til eit «Merk»-avsnitt som forklarer kvifor regel 5, 6, 12, 14 og 15 ikkje kan automatisk validerast.
5. Legg til nivåtabellen med Digdir-reglar per nivå.

## Utført

Alle tiltak vart utført i éin sekvens.

**Faktisk gjort:**

- Lagt til innleiingsavsnitt med lenkje til
  `https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029`
  øvst i README.
- Ny tabell **«Digdir-reglar og dekningsgrad»** med alle 15 reglar, namn,
  skildring og kolonne for kva policy/sjekk som dekkjer den.
  Reglar som ikkje er maskinelt evaluerbare (5, 6, 12, 14, 15) er markerte med
  «*Ikkje evaluert*» med forklaring.
- Oppdatert **Nivå-tabellen** med ein eigen kolonne som viser kva Digdir-reglar
  kvart nivå bør tilfredsstille (bronze: 1-4, 7, 8, 13; silver: 1-4, 7-11, 13).
- Oppdatert **bronze-sjekklista**: `Digdir-regel`-kolonnen viser no nummer + namn
  (t.d. «4 — Identifiserbarhet»).
- Oppdatert **silver-sjekklista**: `Digdir-regel`-kolonnen viser no nummer + namn
  for regel 9, 10, 11.
- Lagt til tabell over gyldige ADMS Status-verdiar i silver-seksjonen.
- Lagt til merknad om kjelda til `annotations.status`-verdiane (ADMS-vokabularet).
