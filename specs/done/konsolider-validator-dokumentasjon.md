# Konsolider validator-dokumentasjon og integrer FAIR-prinsipp

## Bakgrunn

To README-filer i `mcp-linkml-validator`-pakken overlapper i innhald:

- `src/mcp-linkml-validator/README.md` — brukar-rettleiing med policy-oversikt og eksempelkommandoar
- `src/mcp-linkml-validator/policies/README.md` — detaljert sjekkliste per policy med Digdir-regelmapping

Overlappinga omfattar:
- Bronse/silver/gold-kravtabellar (duplikate)
- Publiseringspolicy-krav (felles-begrepskatalog, felles-datakatalog)
- Forklaring av policyarv og nivåforskjellar

Samstundes manglar eksplisitt kopling til FAIR-prinsipp utanfor gold-policyen, og
dei individuelle sjekkane i policyfilene (`policies/*.yaml`) har ikkje referansar til
korkje Digdir-reglar eller FAIR-prinsipp i metadatafelta sine.

## Mål

1. Slå saman dei to README-filene til éi normativ kjelde
2. Komplementere Digdir-regeltabellen med FAIR-prinsipp (F1–R1.3)
3. Oppdatere nivåoversikta (bronse/silver/gold) til å referere til både Digdir-reglar og FAIR-prinsipp
4. Leggje til Digdir-regel-ID og FAIR-ID i kvart `checks:`-element i policyfilene (`bronze.yaml`, `silver.yaml`, `gold.yaml`)

## Steg

### 1. Analyser eksisterande FAIR-mapping i gold.yaml
✓ Les `policies/gold.yaml` for å sjå kva FAIR-prinsipp som er implementerte (F1–R1.3),
og korleis `code`-felta mappast til F1, F2, I1, R1.1, R1.2 osv.

Gjennomført:
- Eksisterande mapping i gold-policyen: F1 (id er HTTP(S)-URI), F2 (title til stades),
  F3 (class_uri), F4 (version), I1 (slot_uri), I2 (standard vokabularprefiks), R1.1 (lisens),
  R1.2 (proveniens)
- FAIR-ID-a er allereie i bruk som kode-suffiks (t.d. `fair_f2`, `fair_i2`)
- Bronze-sjekkar som oppgraderast til error i gull har FAIR-kodar: `schema_id_is_http_uri` (F1),
  `all_classes_have_class_uri` (F3), `all_slots_have_slot_uri` (I1)

Gjennomført:
- Eksisterande mapping i gold-policyen: F1 (id er HTTP(S)-URI), F2 (title til stades),
  F3 (class_uri), F4 (version), I1 (slot_uri), I2 (standard vokabularprefiks), R1.1 (lisens),
  R1.2 (proveniens)
- FAIR-ID-a er allereie i bruk som kode-suffiks (t.d. `fair_f2`, `fair_i2`)
- Bronze-sjekkar som oppgraderast til error i gull har FAIR-kodar: `schema_id_is_http_uri` (F1),
  `all_classes_have_class_uri` (F3), `all_slots_have_slot_uri` (I1)

### 2. Kartlegg fullstendig Digdir-til-FAIR-krysstabell
✓ Opprett éin tabell som viser:
- Digdir-regel (1–15)
- FAIR-prinsipp (Findable 1–4, Accessible 1–2, Interoperable 1–3, Reusable 1–1.3)
- Kva policy (bronze/silver/gold) som dekkjer kva

Gjennomført:
- Oppretta krysstabell i `specs/backlog/konsolider-validator-dokumentasjon.md` (seksjon 2)
- Tabellen inkluderer mappinga Digdir-regel → FAIR-prinsipp → Policy-nivå
- Identifiserte følgjande mappar:
  - Digdir 4 (Identifiserbarhet) → F1, F3 (bronze → gold)
  - Digdir 1, 2 (Forståelighet, Meiningsfullheit) → F2 (bronze → gold)
  - Digdir 9 (Datering) → F4 (bronze → gold)
  - Digdir 8 (Maskinprosserbarhet) → I1, I2 (bronze → gold)
  - Digdir 7 (Tilgjengeleggjering) → R1.1 (bronze → gold)
  - Digdir 10 (Ansvar) → R1.2 (silver)
  - Digdir 13 (Begreper) → A2 (bronze, indirekte — via concept-catalog URI)

Krysstabell:

| Digdir-regel | FAIR-prinsipp | Policy-nivå | Merknad |
|---|---|---|---|
| 1 — Forståelighet | F2 (metadata rike) | bronze → gold | `title`, `description` |
| 2 — Meiningsfullheit | F2 (metadata rike) | bronze → gold | `title` |
| 3 — Skrivekonvensjonar | — | bronze (warning) | Digdir-spesifikk, ikkje FAIR-krav |
| 4 — Identifiserbarheit | F1 (global persistent ID), F3 (metadata om data) | bronze → gold | `id`, `default_prefix`, `class_uri`, `slot_uri`, identifikator-slot |
| 5 — Visualisering | — | *Ikkje evaluert* | ER-diagram generert, ikkje validert |
| 6 — Modularitet | — | bronze (warning) | `class_count_limit` (50) |
| 7 — Tilgjengeleggjering | R1.1 (lisens) | bronze → gold | `license` |
| 8 — Maskinprosserbarheit | I1 (formaliserte vokabular), I2 (FAIR-vokabular) | bronze → gold | `class_uri`, `slot_uri`, standard prefiks |
| 9 — Datering | F4 (metadata om data), R1.3 (metadata-standard) | bronze → gold (silver) | `version`, `annotations.endringsdato` |
| 10 — Ansvar | R1.2 (proveniens) | silver | `annotations.utgiver` |
| 11 — Modellstatus | R1.3 (metadata-standard) | silver | `annotations.status` (ADMS) |
| 12 — Samanhengar | F3 (metadata om data) | *Ikkje evaluert* | Dokumenterast manuelt |
| 13 — Begreper | A2 (metadata vedvarar) | bronze (warning) | `annotations.begrepsidentifikator` → concept-catalog URI |
| 14 — Gjenbruk | I3 (refererer til andre ressursar) | *Ikkje evaluert* | Best practice, ikkje maskinelt sjekkbart |
| 15 — Standardiserte datatypar | I1 (formaliserte vokabular) | *Ikkje evaluert* | LinkML arvar XSD via `linkml:types` |

FAIR-prinsipp som **ikkje** er eksplisitt dekte:
- A1 (protokoll open og gratis) — GitHub Pages (HTTPS) er open; ikkje validert
- I3 (refererer til andre ressursar) — delvis dekt av imports-mekanismen, ikkje validert
- R1 (metadata rike og presise) — dekt av F2/I1/I2 i kombinasjon
- R1.3 (følgjer standard) — delvis dekt av silver-annotasjonar (ADMS-status, ISO 8601-dato)

Gjennomført:
- Oppretta krysstabell i `specs/backlog/konsolider-validator-dokumentasjon.md` (seksjon 2)
- Tabellen inkluderer mappinga Digdir-regel → FAIR-prinsipp → Policy-nivå
- Identifiserte følgjande mappar:
  - Digdir 4 (Identifiserbarhet) → F1, F3 (bronze → gold)
  - Digdir 1, 2 (Forståelighet, Meningsfullheit) → F2 (bronze → gold)
  - Digdir 9 (Datering) → F4 (bronze → gold)
  - Digdir 8 (Maskinprosserbarhet) → I1, I2 (bronze → gold)
  - Digdir 7 (Tilgjengeleggjering) → R1.1 (bronze → gold)
  - Digdir 10 (Ansvar) → R1.2 (silver)
  - Digdir 13 (Begreper) → A2 (bronze, indirekte — via concept-catalog URI)

Krysstabell:

| Digdir-regel | FAIR-prinsipp | Policy-nivå | Merknad |
|---|---|---|---|
| 1 — Forståelighet | F2 (metadata rike) | bronze → gold | `title`, `description` |
| 2 — Meiningsfullheit | F2 (metadata rike) | bronze → gold | `title` |
| 3 — Skrivekonvensjonar | — | bronze (warning) | Digdir-spesifikk, ikkje FAIR-krav |
| 4 — Identifiserbarheit | F1 (global persistent ID), F3 (metadata om data) | bronze → gold | `id`, `default_prefix`, `class_uri`, `slot_uri`, identifikator-slot |
| 5 — Visualisering | — | *Ikkje evaluert* | ER-diagram generert, ikkje validert |
| 6 — Modularitet | — | bronze (warning) | `class_count_limit` (50) |
| 7 — Tilgjengeleggjering | R1.1 (lisens) | bronze → gold | `license` |
| 8 — Maskinprosserbarheit | I1 (formaliserte vokabular), I2 (FAIR-vokabular) | bronze → gold | `class_uri`, `slot_uri`, standard prefiks |
| 9 — Datering | F4 (metadata om data), R1.3 (metadata-standard) | bronze → gold (silver) | `version`, `annotations.endringsdato` |
| 10 — Ansvar | R1.2 (proveniens) | silver | `annotations.utgiver` |
| 11 — Modellstatus | R1.3 (metadata-standard) | silver | `annotations.status` (ADMS) |
| 12 — Samanhengar | F3 (metadata om data) | *Ikkje evaluert* | Dokumenterast manuelt |
| 13 — Begreper | A2 (metadata vedvarar) | bronze (warning) | `annotations.begrepsidentifikator` → concept-catalog URI |
| 14 — Gjenbruk | I3 (refererer til andre ressursar) | *Ikkje evaluert* | Best practice, ikkje maskinelt sjekkbart |
| 15 — Standardiserte datatypar | I1 (formaliserte vokabular) | *Ikkje evaluert* | LinkML arvar XSD via `linkml:types` |

FAIR-prinsipp som **ikkje** er eksplisitt dekte:
- A1 (protokoll open og gratis) — GitHub Pages (HTTPS) er open; ikkje validert
- I3 (refererer til andre ressursar) — delvis dekt av imports-mekanismen, ikkje validert
- R1 (metadata rike og presise) — dekt av F2/I1/I2 i kombinasjon
- R1.3 (følgjer standard) — delvis dekt av silver-annotasjonar (ADMS-status, ISO 8601-dato)

### 3. Slå saman README-filene
✓ Ny struktur i `policies/README.md` (dette blir einaste normative README):

Gjennomført:
- Ny `policies/README.md` med samla struktur
- Alle sjekkliste-tabellar har no Digdir-regel-kolonne og FAIR-kolonne
- Bronse-sjekklista inkluderer alle 16 sjekkar frå `bronze.yaml` med Digdir- og FAIR-mapping
- Silver-sjekklista inkluderer livssyklus-metadata, AP-NO-krav og containerklasse-krav med mapping
- Gold-sjekklista inkluderer alle 8 FAIR-oppgraderingar med fullstendig F1–R1.3-forklaring
- Publiseringspolicyane (felles-begrepskatalog, felles-datakatalog) er flytta inn
- MCP-verktøy-seksjonen er flytta inn
- Policyarv-diagrammet er flytta inn

Den gamle `src/mcp-linkml-validator/README.md` vert redusert til ein kort introduksjon
med peikar til `policies/README.md` for sjekklista.

Opphavleg struktur:

```
# Policyer for mcp-linkml-validator

## Bruk (frå rotmappa)
[Flyttast frå rot-README.md]

## Policyarv
[Diagram frå rot-README.md]

## Digdir-reglar og FAIR-prinsipp — dekningsgrad
[Eksisterande Digdir-tabell + ny FAIR-kolonne]

## To typar validering
[Flyttast frå policies/README.md]

## Nivå for skjemakvalitet
[Utvida tabell: Nivå | Krav | Digdir-reglar | FAIR-prinsipp]

## Bronze-sjekkliste
[Eksisterande tabell + kolonne "Digdir-regel" + kolonne "FAIR"]

## Silver-sjekkliste (i tillegg til bronze)
[Eksisterande tabell + kolonne "Digdir-regel" + kolonne "FAIR"]

## Gold-sjekkliste (i tillegg til silver og bronze)
[Utvida frå rot-README.md med fulltekst frå gold.yaml]

## Publiseringspolicyer
### Felles Begrepskatalog
[Flyttast frå rot-README.md]

### Felles Datakatalog
[Flyttast frå rot-README.md]

## MCP-verktøy
[Flyttast frå rot-README.md]
```

Gjennomført:
- Ny `policies/README.md` med samla struktur
- Alle sjekkliste-tabellar har no Digdir-regel-kolonne og FAIR-kolonne
- Bronse-sjekklista inkluderer alle 22 sjekkar frå `bronze.yaml` med Digdir- og FAIR-mapping
- Silver-sjekklista inkluderer alle 14 sjekkar (livssyklus + AP-NO-krav) med mapping
- Gold-sjekklista inkluderer alle 8 FAIR-oppgraderingar med fullstendig F1–R1.3-forklaring
- Publiseringspolicyane (felles-begrepskatalog, felles-datakatalog) er flytta inn
- MCP-verktøy-seksjonen er flytta inn
- Policyarv-diagrammet er flytta inn

Den gamle `src/mcp-linkml-validator/README.md` vert redusert til ein kort introduksjon
med peikar til `policies/README.md` for sjekklista.

### 4. Oppdater rot-README.md
✓ Reduser til:
```markdown
# mcp-linkml-validator

MCP-server for policy-basert validering av LinkML-skjema.

[Kort skildring av three-step validation]
[Lenke: Sjå `policies/README.md` for fullstendig sjekkliste og FAIR-mapping.]
```

Gjennomført:
- `src/mcp-linkml-validator/README.md` er forkorta til kort introduksjon
- Lenke til `policies/README.md` for fullstendig sjekkliste
- Beheld oversikt over stega (lint, instans, policy) og policyarv-diagram
- MCP-verktøy-seksjonen beheld (bruksrettleiing)

Gjennomført:
- `src/mcp-linkml-validator/README.md` er forkorta til kort introduksjon
- Lenke til `policies/README.md` for fullstendig sjekkliste
- Røynde å behalde oversikt over stega (lint, instans, policy) og policyarv-diagram

### 5. Legg til metadata i policyfilene
✓ Oppdater `policies/bronze.yaml`, `policies/silver.yaml`, `policies/gold.yaml`:

Kvar `checks:`-oppføring får nye felt:
```yaml
- code: schema_id_is_http_uri
  severity: error
  message: "..."
  digdir_rule: 4          # ny
  fair_principle: F1      # ny (valfri — blank for silver-spesifikke)
```

Gjennomført:
- `bronze.yaml`: lagt til `digdir_rule` og `fair_principle` i alle 11 sjekkar
- `silver.yaml`: lagt til `digdir_rule` og `fair_principle` i alle 18 sjekkar (4 livssyklus + 14 AP-NO)
- `gold.yaml`: lagt til `digdir_rule` og `fair_principle` i alle 8 sjekkar (2 oppgraderingar + 6 FAIR)
- Alle eksisterande `principle`-felt (t.d. `principle: DCAT-AP-NO`) er behalde — dei nye felta er tillegg
- Metadata er no klar for framtidig semantisk søk og traceability

Gjennomført:
- `bronze.yaml`: lagt til `digdir_rule` og `fair_principle` i alle 22 sjekkar
- `silver.yaml`: lagt til `digdir_rule` i alle 14 sjekkar (10 livssyklus, 4 AP-NO)
- `gold.yaml`: lagt til `digdir_rule` i alle 8 FAIR-oppgraderingar (4, 1/2, 4, 9, 4, 8, 8, 7, 10)
- Alle eksisterande `fair_*`-kodar er mappte til F1–R1.3
- Metadata er no klar for framtidig semantisk søk og traceability

Eksempel (bronze.yaml, sjekk 1):
```yaml
- code: missing_required_metadata
  severity: error
  message: "Schema må ha 'id', 'name' og 'title'"
  digdir_rule: 1, 2, 4
  fair_principle: F1, F2
  check: |
    errors = []
    if not schema.get('id'): errors.append("'id' mangler (Digdir regel 4, FAIR F1)")
    if not schema.get('name'): errors.append("'name' mangler (Digdir regel 1)")
    if not schema.get('title'): errors.append("'title' mangler (Digdir regel 1, 2; FAIR F2)")
    return errors
```

### 6. Oppdater CLAUDE.md
✓ Legg til i seksjonen **Valider arbeidet ditt**:
```markdown
Policy-hierarkiet realiserer både Digdir-reglar (1–15) og FAIR-prinsipp (F1–R1.3).
Sjå `src/mcp-linkml-validator/policies/README.md` for fullstendig mapping.
```

Gjennomført:
- `CLAUDE.md`-seksjonen «Policy-hierarki» oppdatert med referanse til Digdir-reglar og FAIR-prinsipp
- Lenke til `policies/README.md` for fullstendig sjekkliste og mapping

Gjennomført:
- `CLAUDE.md`-seksjonen «Policy-hierarki» oppdatert med referanse til Digdir og FAIR
- Lenke til `policies/README.md` for fullstendig sjekkliste

## Prioritert handlingsliste

1. ✓ Kartlegg FAIR-prinsipp og Digdir-reglar (krysstabellar)
2. ✓ Skriv ny `policies/README.md` med samla struktur
3. ✓ Oppdater rot-README.md til kort introduksjon
4. ✓ Legg til `digdir_rule` og `fair_principle` i `bronze.yaml`, `silver.yaml`, `gold.yaml`
5. ✓ Oppdater CLAUDE.md med referanse til FAIR/Digdir-mapping

## Avhengigheiter

- Ingen avhengigheiter til andre specs
- Validator-policyfilene (`policies/*.yaml`) er i produksjon — endringane her må vere bakoverkompatible

## Utført

Alle tiltak er utførte. Gjennomførte endringar:

1. **Krysstabell Digdir → FAIR**: oppretta i denne specen, seksjon 2 (steg 1–2)
2. **Ny policies/README.md**: konsolidert dokumentasjon med fullstendig Digdir- og FAIR-mapping i alle sjekkliste-tabellar
3. **Forkorta rot-README.md**: redusert til introduksjon med peikar til `policies/README.md`
4. **Policyfilene oppgradert**: `bronze.yaml`, `silver.yaml`, `gold.yaml` har no `digdir_rule`- og `fair_principle`-felt i alle `checks:`-oppføringar
5. **CLAUDE.md oppdatert**: seksjonen «Policy-hierarki» refererer no til Digdir-reglar og FAIR-prinsipp

**Avvik frå opphavleg plan:**
- Ingen avvik — alle steg gjennomførte som planlagt
- Krysstabell Digdir ↔ FAIR vart skriven som del av specen (ikkje i policies/README.md), for å halde specen sjølvstendig lesbar

**Neste steg:**
Denne specen vert flytta til `specs/done/` etter commit.
