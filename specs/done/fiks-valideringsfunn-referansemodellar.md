# Fiks alle valideringsfunn i referansemodellane

## Bakgrunn

Dei fire modellane i `src/linkml/referanse/` (`referansemodell`, `referansemodell-bronze`,
`referansemodell-silver`, `referansemodell-gold`) er meint som annoterte, pedagogiske
eksempel på gyldig LinkML-modellering og på korleis policy-nivåa (bronze/silver/gold)
verkar — sjå toppkommentarane og `.claude/rules/linkml-schema.md`. Sidan dei er
referansepunkt for nye utviklarar, skal dei vere **fri for valideringsfunn** (både
`warning` og `error`), slik at eit `make lint` / `make mcp-linkml-valider-modell`-køyr
mot kvar av dei gir eit reint resultat.

`version:`-felta har rykt fram sidan valideringsresultata sist vart fanga (t.d.
`referansemodell` v1.3.0 → v1.5.0), så dei eksisterande `validation/<versjon>/<policy>.json`-
filene var forelda. Denne specen er basert på eit ferskt køyr av `make lint` og
`make mcp-linkml-valider-modell` for alle fire skjema (2026-09-01), som også har
skrive oppdaterte (men enno **ikkje fiksa**) resultat til
`src/linkml/referanse/<modell>/validation/<versjon>/<policy>.json`.

**Dette er ein plan** — ingen skjemaendringar er utført enno. Fiksane under skal
gjennomførast som eit eige steg, med `specs/backlog/fiks-valideringsfunn-referansemodellar.md`
oppdatert etter kvart delsteg og flytta til `specs/done/` når alt er grønt.

---

## Funn per modell (ferskt køyr, 2026-09-01)

### 1. `referansemodell` (v1.5.0, policy: bronze)

| Type | Kjelde | Funn |
|---|---|---|
| lint | `make lint` | `warning`: Slot `ressursar` manglar `description` (attributt i `ReferanseContainer`) |
| policy | `make mcp-linkml-valider-modell` | `warning` (`all_classes_have_concept_ref`): Klasse `Ressurs` manglar `annotations.begrepsidentifikator` |

### 2. `referansemodell-bronze` (v1.2.0, policy: bronze)

| Type | Kjelde | Funn |
|---|---|---|
| lint | `make lint` | 4× `warning`: Slot `ressursar` + subsets `Obligatorisk`, `Anbefalt`, `Valgfri` manglar `description` |
| policy | `make mcp-linkml-valider-modell` | Ingen funn (0 warning, 0 error) |

### 3. `referansemodell-silver` (v2.1.0, policy: silver)

| Type | Kjelde | Funn |
|---|---|---|
| lint | `make lint` | 13× `warning`: 10 containerattributtar (`katalogar`, `katalogpostar`, `datasett`, `distribusjoner`, `datatenestar`, `aktorar`, `kvalitetsmaal`, `kvalitetsmaalingar`, `kvalitetsdimensjonar`, `kvalitetsmerknader`) + 3 subsets (`Obligatorisk`, `Anbefalt`, `Valgfri`) manglar `description` |
| policy | `make mcp-linkml-valider-modell` | 4× `warning`: `schema.annotations.oppdateringsfrekvens` manglar; `Datasett` manglar slot med `dct:accessRights`; `Datasett` manglar slot med `dcatap:applicableLegislation`; `Distribusjon` manglar slot med `dct:license` |

### 4. `referansemodell-gold` (v2.1.0, policy: gold)

| Type | Kjelde | Funn |
|---|---|---|
| lint | `make lint` | Same 13× `warning` som silver (identisk struktur, ikkje enno retta) |
| policy | `make mcp-linkml-valider-modell` | 4× **`error`** (same krav som silver, men oppgradert): `schema.annotations.oppdateringsfrekvens` manglar; `Datasett` manglar slot med `dct:accessRights`; `Datasett` manglar slot med `dcatap:applicableLegislation`; `Distribusjon` manglar slot med `dct:license` — `valid: false` |

**Merk:** `gold`-skjemaet har alt lagt til ein `lisens`-slot (`dct:license`) på
`Katalog` og `Datasett` (sjå diff mot silver), men **ikkje** på `Distribusjon` —
som er nett den klassen policyen sjekkar. Sjå `src/mcp-linkml-validator/policies/README.md`
linje 140-143, 200-212 for kjelde til kvart krav.

---

## Steg

### Steg 1 — `referansemodell`

1.1. Legg til `description:` på attributtet `ressursar` i `ReferanseContainer`
   (t.d. «Ressursane som inngår i datafila.»).

1.2. Legg til `annotations.begrepsidentifikator` på klassen `Ressurs`, med same
   TODO-placeholder-mønster som `referansemodell-bronze` alt brukar:
   `https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO/concepts/TODO`.
   Oppdater kommentaren over `Ressurs` (linje 51) som i dag seier at annotasjonen
   «kan leggjast til» — endre til at TODO-placeholderen er venta mønster inntil
   klassen har ei reell begrepsdefinisjon.

### Steg 2 — `referansemodell-bronze`

2.1. Legg til `description:` på attributtet `ressursar` i `ReferanseBronseContainer`.

2.2. Legg til `description:` på subsets `Obligatorisk`, `Anbefalt`, `Valgfri`
   (t.d. «Obligatorisk felt per bronsepolicyen.», tilsvarande for dei to andre).

### Steg 3 — `referansemodell-silver`

3.1. Legg til `description:` på alle 10 containerattributt i `ReferanseSolvContainer`
   og på dei 3 subsets (same mønster som steg 2.2).

3.2. Legg til prefiks `dcatap: http://data.europa.eu/r5r/` i `prefixes:`-blokka
   (manglar i dag — silver har berre `linkml`, `ex`, `dct`, `dcat`, `foaf`, `dqv`).

3.3. Legg til `annotations.oppdateringsfrekvens` på skjemanivå, med ein URI frå
   EUs Frequency Named Authority List (t.d.
   `http://publications.europa.eu/resource/authority/frequency/IRREG` — same
   mønster som `frekvens`-sloten i `dcat-ap-no-schema.yaml`).

3.4. Legg til ny slot `tilgangsrettigheter` (`slot_uri: dct:accessRights`,
   `range: uriorcurie`) og knyt han til `Datasett` (`slots:` + `slot_usage`
   med `in_subset: [Anbefalt]` — matchar at kravet er `warning`, ikkje `error`,
   på silver).

3.5. Legg til ny slot `gjeldende_lovgivning` (`slot_uri: dcatap:applicableLegislation`,
   `range: uriorcurie`, `multivalued: true`) og knyt han til `Datasett` på same
   måte (`in_subset: [Anbefalt]`).

3.6. Legg til ny slot `lisens` (`slot_uri: dct:license`, `range: uriorcurie`) og
   knyt han til `Distribusjon` (`in_subset: [Anbefalt]`). Skildringstekst kan
   gjenbrukast frå gold-varianten («Lisens som regulerer bruken av ressursen.»).

3.7. Oppdater dei eksisterande kommentarane som listar kva krav kvart felt
   dekkjer (t.d. `# silver: katalog_tittel, ... → error`), slik at dei nye
   slotsa også er dokumenterte med rett sjekk-kode
   (`silver_datasett_tilgangsrettigheter`/`silver_datasett_lovgivning`/
   `silver_distribusjon_lisens` → `warning`), for å halde fram den
   sjølvforklarande stilen i fila.

### Steg 4 — `referansemodell-gold`

4.1. Legg til `description:` på alle 10 containerattributt i `ReferanseGullContainer`
   og på dei 3 subsets — identisk med steg 3.1.

4.2. Legg til prefiks `dcatap: http://data.europa.eu/r5r/` — identisk med steg 3.2.

4.3. Legg til `annotations.oppdateringsfrekvens` på skjemanivå — identisk verdi
   som steg 3.3 (eller ein annan gyldig frekvens-URI).

4.4. Legg til ny slot `tilgangsrettigheter` (som steg 3.4), knytt til `Datasett`.
   Sidan kravet er `error` på gold (obligatorisk, ikkje anbefalt), set
   `required: true` og `in_subset: [Obligatorisk]` i `slot_usage` for å reflektere
   at gold-nivået krev feltet reelt, ikkje berre at slotten finst.

4.5. Legg til ny slot `gjeldende_lovgivning` (som steg 3.5), knytt til `Datasett`
   med `required: true`, `in_subset: [Obligatorisk]`.

4.6. Legg `lisens` (alt definert i skjemaet, brukt av `Katalog`/`Datasett`) til
   `Distribusjon` sine `slots:` òg, med `slot_usage.in_subset: [Anbefalt]` —
   policyen krev berre at slotten finst på klassen, ikkje at han er obligatorisk
   (jf. `Katalog`/`Datasett`-bruken av `lisens` som er `Anbefalt`, ikkje
   `Obligatorisk`, i det same skjemaet i dag).

4.7. Oppdater kommentarane (som steg 3.7), med `error` som alvorsgrad sidan
   dette er gold.

### Steg 5 — Verifiser

5.1. Køyr `make lint SCHEMA=<sti>` for alle fire skjema — forventa 0 problem kvar.

5.2. Køyr `make mcp-linkml-valider-modell SCHEMA=<sti>` for alle fire skjema
   (POLICY vert auto-detektert frå `build.yaml`) — forventa `valid: true`,
   `errorCount: 0`, `warningCount: 0` for alle.

5.3. Køyr `make roundtrip SCHEMA=<sti>` for alle fire skjema for å sikre at
   dei nye slotsa ikkje bryt JSON/TTL-serialisering.

5.4. Køyr `make validate DOMAIN=referanse` for å sikre at ingen import-kollisjonar
   eller strukturfeil er introduserte (relevant sidan `dcatap:`-prefiks vert lagt
   til i to skjema som ikkje importerer `dcat-ap-no-schema`).

### Steg 6 — Avslutning

6.1. Legg til `## Utført`-seksjon i denne specen med resultatet av steg 5.

6.2. Generer utkast til commit-melding (conventional commits, jf. CLAUDE.md).

6.3. Flytt specen til `specs/done/`.

---

## Handlingsliste

| # | Tiltak | Fil | Type funn | Avhengigheit |
|---|---|---|---|---|
| 1.1 | `description` på `ressursar` | `referansemodell/referansemodell-schema.yaml` | lint warning | — |
| 1.2 | `begrepsidentifikator` på `Ressurs` | `referansemodell/referansemodell-schema.yaml` | policy warning | — |
| 2.1 | `description` på `ressursar` | `referansemodell-bronze/referansemodell-bronze-schema.yaml` | lint warning | — |
| 2.2 | `description` på 3 subsets | `referansemodell-bronze/referansemodell-bronze-schema.yaml` | lint warning | — |
| 3.1 | `description` på 10 attributt + 3 subsets | `referansemodell-silver/referansemodell-silver-schema.yaml` | lint warning | — |
| 3.2 | Legg til `dcatap:`-prefiks | `referansemodell-silver/referansemodell-silver-schema.yaml` | føresetnad for 3.5 | — |
| 3.3 | `annotations.oppdateringsfrekvens` | `referansemodell-silver/referansemodell-silver-schema.yaml` | policy warning | — |
| 3.4 | Ny slot `tilgangsrettigheter` på `Datasett` | `referansemodell-silver/referansemodell-silver-schema.yaml` | policy warning | — |
| 3.5 | Ny slot `gjeldende_lovgivning` på `Datasett` | `referansemodell-silver/referansemodell-silver-schema.yaml` | policy warning | 3.2 |
| 3.6 | Ny slot `lisens` på `Distribusjon` | `referansemodell-silver/referansemodell-silver-schema.yaml` | policy warning | — |
| 3.7 | Oppdater forklarande kommentarar | `referansemodell-silver/referansemodell-silver-schema.yaml` | konsistens | 3.4-3.6 |
| 4.1 | `description` på 10 attributt + 3 subsets | `referansemodell-gold/referansemodell-gold-schema.yaml` | lint warning | — |
| 4.2 | Legg til `dcatap:`-prefiks | `referansemodell-gold/referansemodell-gold-schema.yaml` | føresetnad for 4.5 | — |
| 4.3 | `annotations.oppdateringsfrekvens` | `referansemodell-gold/referansemodell-gold-schema.yaml` | policy error | — |
| 4.4 | Ny slot `tilgangsrettigheter` på `Datasett` (obligatorisk) | `referansemodell-gold/referansemodell-gold-schema.yaml` | policy error | — |
| 4.5 | Ny slot `gjeldende_lovgivning` på `Datasett` (obligatorisk) | `referansemodell-gold/referansemodell-gold-schema.yaml` | policy error | 4.2 |
| 4.6 | Legg eksisterande `lisens`-slot til `Distribusjon` | `referansemodell-gold/referansemodell-gold-schema.yaml` | policy error | — |
| 4.7 | Oppdater forklarande kommentarar | `referansemodell-gold/referansemodell-gold-schema.yaml` | konsistens | 4.4-4.6 |
| 5 | Verifiser lint + policy + roundtrip + validate for alle fire | alle fire skjema | — | 1-4 |
| 6 | Avslutning: `## Utført`, commit-melding, flytt til `specs/done/` | denne specen | — | 5 |

---

## Utført

Alle steg (1-6) er gjennomførte 2026-09-01:

- **Steg 1** (`referansemodell`): `description` lagt til på `ressursar`;
  `annotations.begrepsidentifikator`-TODO lagt til på `Ressurs`.
- **Steg 2** (`referansemodell-bronze`): `description` lagt til på `ressursar`
  og på subsets `Obligatorisk`/`Anbefalt`/`Valgfri`.
- **Steg 3** (`referansemodell-silver`): `description` lagt til på 10
  containerattributt + 3 subsets; `dcatap:`-prefiks lagt til;
  `annotations.oppdateringsfrekvens` sett til
  `http://publications.europa.eu/resource/authority/frequency/IRREG`;
  nye slots `tilgangsrettigheter` (`dct:accessRights`), `gjeldende_lovgivning`
  (`dcatap:applicableLegislation`) på `Datasett`, og `lisens` (`dct:license`)
  på `Distribusjon` — alle `in_subset: [Anbefalt]`; forklarande kommentarar
  oppdaterte.
- **Steg 4** (`referansemodell-gold`): identisk med steg 3, men
  `tilgangsrettigheter`/`gjeldende_lovgivning` sett som `required: true`,
  `in_subset: [Obligatorisk]` (gold-nivå krev feltet, ikkje berre slotten);
  eksisterande `lisens`-slot lagt til `Distribusjon` sine `slots:`.
- **Steg 5** (verifisering): `make lint` og `make mcp-linkml-valider-modell`
  gir `✓ No problems found` / `valid: true, errorCount: 0, warningCount: 0`
  for alle fire skjema. `make roundtrip` (JSON + TTL) OK for alle fire.
  `make validate DOMAIN=referanse` → `✓ Ingen import-kollisjonar funne (4 skjema sjekka)`.
- **Steg 6**: denne seksjonen, commit-melding under, og flytting til `specs/done/`.

Ingen avvik frå planen — alle tiltak i handlingslista er utførte som skildra.

---

## Kjelder

- `src/mcp-linkml-validator/policies/README.md` (§ bronze, § silver, § gold) —
  full sjekkliste og Digdir-/FAIR-mapping per krav.
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` (linje 1100-1135) —
  eksisterande slotnamn-konvensjon (`tilgangsrettigheter`, `gjeldende_lovgivning`)
  for `dct:accessRights` / `dcatap:applicableLegislation` i DCAT-AP-NO-domenet,
  gjenbrukt her for namnekonsistens på tvers av repoet.
- `.claude/rules/linkml-schema.md` — containerklasse- og slot-konvensjonar brukt
  i alle fiksane over.
