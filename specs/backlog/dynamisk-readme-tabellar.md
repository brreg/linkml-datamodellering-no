# Dynamisk generering av README-tabellar

**Status:** Backlog  
**Dato:** 2026-07-30  
**Ansvarleg:** Audun Vindenes Egge

## Bakgrunn

`src/assets/scripts/makefile/generate-readme-tables.sh` genererer fem tabellar i `README.md`:

1. **Domene-tabell** — oversikt over domene (fair, ap-no, ngr, fint osv.)
2. **Skjema-tabell** — oversikt over skjema per domene
3. **Artefakt-tabell** — oversikt over genererte artefaktar (JSON-LD, SHACL, OWL osv.)
4. **Begrepskatalog-tabell** — oversikt over begrepskatalog-katalogar
5. **Modellkatalog-tabell** — oversikt over modellkatalog-katalogar

**Problem:** Store delar av desse tabellane er hardkoda i scriptet. Dette gjer vedlikehald tungvint og aukar risikoen for inkonsistens mellom kjeldekode og dokumentasjon.

**Mål:** Identifisere kva som kan genererast dynamisk frå kjeldekode og YAML-metadata, og redusere hardkoding.

## Analyse

### 1. Domene-tabell (linje 21-38)

**Status quo:** Heilt hardkoda i heredoc-blokk.

**Kan genererast dynamisk:**
- **Domenenamn:** `find src/linkml -maxdepth 1 -type d` (ekskluder spesialkatalogar)
- **Dokumentasjonslenkjer:** Kan konstruerast frå domenenamn (`<domain>/`)

**Kan IKKJE genererast dynamisk:**
- **Skildring:** Narrativ tekst som forklarer kva domenet er (t.d. "FAIR-metadataoverbygning", "Norske W3C-applikasjonsprofiler"). Ingen strukturert kjelde for dette.
- **Domene-ekstern dokumentasjonslenkje:** Lenkjer til go-fair.org, data.norge.no, informasjonsforvaltning.github.io osv.

**Konklusjon:** Treng ein strukturert kjelde for domene-metadata (t.d. `src/linkml/<domain>/domain.yaml`) for å generere dynamisk. Utan dette må skildringar vere hardkoda.

### 2. Skjema-tabell (linje 40-148)

**Status quo:** Delvis dynamisk (finn skjema via `find`), delvis hardkoda (skildringar og dokumentasjonslenkjer i assosiative arrays).

**Kan genererast dynamisk:**
- **Domenenamn og skjemanamn:** Allereie dynamisk via `find src/linkml -name "*-schema.yaml"`
- **Skildring:** Kan hentast frå `description`-feltet i `*-schema.yaml`
- **Dokumentasjonslenkjer:** `see_also`-feltet i `*-schema.yaml` (dersom det finst)

**Kan IKKJE genererast dynamisk:**
- **Manuelt kuraterte skildringar:** Mange skildringar i `DESCRIPTIONS[]` er kortare og meir presise enn `description`-feltet i skjemaet (t.d. "Offentlege tenester og hendingar" vs. lang bokmålsforklaring)
- **Ekstra kontekst:** Lenkjer til eksterne standardar (data.norge.no, go-fair.org osv.) er ikkje alltid i `see_also`

**Konklusjon:** Dynamisk generering er mogleg, men krev at `description` og `see_also` i skjema er oppdaterte og presise. Hardkoda array kan nyttast som fallback.

### 3. Artefakt-tabell (linje 150-175)

**Status quo:** Heilt hardkoda i heredoc-blokk.

**Kan genererast dynamisk:**
- **Artefakttype, filnamn, manifest-flag og generator:** Kan hentast frå `build.yaml` (seksjonen `generators:`) for kvart skjema
- **Brukstilfelle:** Kan hentast frå ein strukturert kjelde (t.d. `src/assets/metadata/artifacts.yaml`)

**Kan IKKJE genererast dynamisk:**
- **Narrativ forklaring:** "Mapping frå JSON til RDF — brukast saman med API", "Validering av RDF-data mot skjema i triple stores" osv.

**Konklusjon:** Treng ein strukturert kjelde (`artifacts.yaml`) som mappat artefakttype til brukstilfelle, W3C-semantisk-flagg og generatorkommando. Utan dette må narrativ tekst vere hardkoda.

### 4. Begrepskatalog-tabell (linje 177-202)

**Status quo:** Delvis dynamisk (finn katalogar via `find`), delvis hardkoda (organisasjonsnamn i `ORGS[]`).

**Kan genererast dynamisk:**
- **Katalognamn:** Allereie dynamisk via `find src/linkml/begrepskatalog -name "*-schema.yaml"`
- **Organisasjonsnamn:** Kan hentast frå `title`-feltet i `*-schema.yaml` (t.d. "Brønnøysundregistra - Begrepskatalog" → "Brønnøysundregistra")
- **Utgjevar:** Kan hentast frå `annotations.utgiver` i skjemaet

**Kan IKKJE genererast dynamisk:**
- **Skildring:** "Begrepskatalog for $org sine begrep" kan genererast, men er eit trivialt template

**Konklusjon:** Dynamisk generering er fullt mogleg ved å hente `title` og `annotations.utgiver` frå skjemaet.

### 5. Modellkatalog-tabell (linje 204-234)

**Status quo:** Delvis dynamisk (finn katalogar via `find`), delvis hardkoda (organisasjonsnamn i `ORGS[]`).

**Kan genererast dynamisk:**
- **Katalognamn:** Allereie dynamisk via `find src/linkml/modellkatalog -name "*-schema.yaml"`
- **Organisasjonsnamn:** Kan hentast frå `title`-feltet i `*-schema.yaml` (t.d. "Brønnøysundregistra - Modellkatalog" → "Brønnøysundregistra")
- **Utgjevar:** Kan hentast frå `annotations.utgiver` i skjemaet

**Kan IKKJE genererast dynamisk:**
- **Skildring:** "Modellkatalog for $org sine informasjonsmodellar" kan genererast, men er eit trivialt template

**Konklusjon:** Dynamisk generering er fullt mogleg ved å hente `title` og `annotations.utgiver` frå skjemaet.

## Konklusjon

| Tabell | Dynamisk genererbar? | Kva krevst? |
|---|---|---|
| Domene-tabell | **Nei** | Treng strukturert `domain.yaml` for skildringar og eksterne lenkjer |
| Skjema-tabell | **Delvis** | Dynamisk via `description` og `see_also` frå skjema, men hardkoda array som fallback |
| Artefakt-tabell | **Nei** | Treng strukturert `artifacts.yaml` for narrativ forklaring og brukstilfelle |
| Begrepskatalog-tabell | **Ja** | Hent `title` og `annotations.utgiver` frå skjema |
| Modellkatalog-tabell | **Ja** | Hent `title` og `annotations.utgiver` frå skjema |

## Tiltak

### 1. Dynamisk generering av begrepskatalog-tabell og modellkatalog-tabell

**Akseptansekriterium:** Ingen hardkoda `ORGS[]`-array — organisasjonsnamn hentast frå `title` i skjemaet.

**Steg:**

1. Endre `generate_begrepskatalog_table()`:
   - Fjern `ORGS[]`-array
   - Hent `title` frå `<katalog>-schema.yaml` via `yq '.title'`
   - Ekstraher organisasjonsnamn frå `title` (før " - Begrepskatalog")
   - Bruk `annotations.utgiver` dersom organisasjonsnamn trengst verifisert

2. Endre `generate_modellkatalog_table()`:
   - Fjern `ORGS[]`-array
   - Hent `title` frå `<katalog>-schema.yaml` via `yq '.title'`
   - Ekstraher organisasjonsnamn frå `title` (før " - Modellkatalog")
   - Bruk `annotations.utgiver` dersom organisasjonsnamn trengst verifisert

3. Test:
   - Køyr `make readme-tables`
   - Verifiser at `README.md` inneheld korrekte organisasjonsnamn i begge tabellar
   - Samanlikn med tidlegare hardkoda versjon

### 2. Evaluer dynamisk generering av skjema-tabell

**Akseptansekriterium:** Skill i skjemaet kan brukast i staden for hardkoda `DESCRIPTIONS[]` og `DOC_LINKS[]`.

**Steg:**

1. Sjekk om `description` i alle skjema er presise nok til å vise i tabell:
   - Køyr `for schema in $(find src/linkml -name "*-schema.yaml" | grep -v begrepskatalog | grep -v modellkatalog); do echo "---"; echo "$schema"; yq '.description' "$schema"; done`
   - Samanlikn med hardkoda `DESCRIPTIONS[]`

2. Sjekk om `see_also` i alle skjema inneheld relevante dokumentasjonslenkjer:
   - Køyr `for schema in $(find src/linkml -name "*-schema.yaml" | grep -v begrepskatalog | grep -v modellkatalog); do echo "---"; echo "$schema"; yq '.see_also' "$schema"; done`
   - Samanlikn med hardkoda `DOC_LINKS[]`

3. Dersom `description` og `see_also` er mangelfulle:
   - Oppdater alle skjema med presise skildringar og lenkjer
   - Endre `generate_schema_table()` til å hente frå skjema i staden for array
   - Behald array som fallback dersom felt manglar

4. Dersom `description` og `see_also` IKKJE er brukbare:
   - Lat `DESCRIPTIONS[]` og `DOC_LINKS[]` vere hardkoda
   - Dokumenter dette som eit bevisst val (narrativ presisjon framfor 100% dynamisk)

### 3. Vurder strukturert metadata for domene og artefaktar

**Akseptansekriterium:** Avgjer om `domain.yaml` og `artifacts.yaml` skal implementerast.

**Steg:**

1. Vurder nytte vs. kostnad:
   - **Nytte:** 100% dynamisk generering, ingen hardkoding
   - **Kostnad:** Nye metadatafiler å vedlikehalde, aukar kompleksitet

2. Dersom nytten er høg (mange nye domene eller artefakttypar ventar):
   - Opprett `src/linkml/<domain>/domain.yaml` med felt `name`, `description`, `documentation`
   - Opprett `src/assets/metadata/artifacts.yaml` med mapping frå artefakttype til brukstilfelle
   - Endre `generate_domain_table()` og `generate_artifacts_table()` til å hente frå desse filene

3. Dersom nytten er låg (stabil domenestruktur og artefaktliste):
   - Lat hardkoda heredoc-blokkar stå
   - Dokumenter at dette er manuelt kuratert innhald (som `mkdocs/docs/*.md`)

## Oppsummering

**Umiddelbart realiserbart:**
- Begrepskatalog-tabell og modellkatalog-tabell kan genererast 100% dynamisk frå skjema-metadata

**Krev evaluering:**
- Skjema-tabell kan genererast dynamisk dersom `description` og `see_also` i skjema er oppdaterte og presise

**Krev ny infrastruktur:**
- Domene-tabell og artefakt-tabell krev strukturerte metadatafiler (`domain.yaml`, `artifacts.yaml`) for dynamisk generering

**Anbefaling:** Start med tiltak 1 (begrepskatalog/modellkatalog), deretter tiltak 2 (skjema-evaluering). Tiltak 3 (domene/artefaktar) bør berre realiserast dersom stabil hardkoding vert eit vedlikehaldsproblem.
