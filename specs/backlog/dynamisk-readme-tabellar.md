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

**Status quo (2026-07-30):** ✅ Heilt dynamisk — henta frå `description` og `see_also` i skjema-YAML.

**Migrasjon utført i commit 53def559:**
- `scripts/migrate-schema-metadata.sh` kopierte frå hardkoda `DESCRIPTIONS[]` og `DOC_LINKS[]` til `description` og `see_also` i skjema-YAML
- `src/assets/scripts/makefile/extract-schema-metadata.py` hentar metadata frå YAML
- `generate_schema_table()` i `generate-readme-tables.sh` brukar `extract-schema-metadata.py` i staden for hardkoda arrays

**Kan genererast dynamisk:**
- **Domenenamn og skjemanamn:** Allereie dynamisk via `find src/linkml -name "*-schema.yaml"`
- **Skildring:** Hentast frå `description`-feltet i `*-schema.yaml`
- **Dokumentasjonslenkjer:** Hentast frå `see_also`-feltet i `*-schema.yaml`

**Konklusjon:** 100% dynamisk generering realisert. Vedlikehald skjer no direkte i skjema-YAML.

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

| Tabell | Dynamisk genererbar? | Kva krevst? | Status (2026-07-30) |
|---|---|---|---|
| Domene-tabell | **Nei** | Treng strukturert `domain.yaml` for skildringar og eksterne lenkjer | ❌ Ikkje implementert |
| Skjema-tabell | **Ja** | Dynamisk via `description` og `see_also` frå skjema | ✅ **Implementert** (commit 53def559) |
| Artefakt-tabell | **Nei** | Treng strukturert `artifacts.yaml` for narrativ forklaring og brukstilfelle | ❌ Ikkje implementert |
| Begrepskatalog-tabell | **Ja** | Hent `title` frå skjema | ✅ **Implementert** (tiltak 1) |
| Modellkatalog-tabell | **Ja** | Hent `title` frå skjema | ✅ **Implementert** (tiltak 1) |

## Tiltak

### 1. ✅ Dynamisk generering av begrepskatalog-tabell og modellkatalog-tabell (FULLFØRT)

**Akseptansekriterium:** Ingen hardkoda `ORGS[]`-array — organisasjonsnamn hentast frå `title` i skjemaet.

**Utført (2026-07-30):**

1. Utvida `extract-schema-metadata.py`:
   - La til `extract_title()` og `extract_annotations_utgiver()`
   - Støttar no `title`, `annotations.utgiver` i tillegg til `description` og `see_also`

2. Endra `generate_begrepskatalog_table()`:
   - Fjerna `ORGS[]`-array
   - Hentar `title` frå skjema via `extract-schema-metadata.py`
   - Ekstraher organisasjonsnamn med `sed 's/ - Begrepskatalog.*//'`
   - Fallback til "Ukjend" dersom mønster ikkje passar

3. Endra `generate_modellkatalog_table()`:
   - Fjerna `ORGS[]`-array
   - Hentar `title` frå skjema via `extract-schema-metadata.py`
   - Ekstraher organisasjonsnamn med `sed 's/ - Modellkatalog.*//'`
   - Fallback til "Ukjend" dersom mønster ikkje passar

4. Oppdatert AUTO-GENERATED-kommentarar:
   - Alle kommentarar inneheld no script/funksjon-referanse
   - Regex-basert matching i scriptet støttar både gamalt og nytt format
   - Genererer automatisk nye kommentarar med korrekt format

5. Verifisering:
   - Køyrde `make readme-tables`
   - Sjekka diff: organisasjonsnamn vert henta korrekt frå `title`-felt
   - Eksempel: "Registerenheten i Brønnøysund" (tidlegare "Brønnøysundregistra"), "Novari IKS" (tidlegare "Novari")

### 2. ✅ Dynamisk generering av skjema-tabell (FULLFØRT)

**Akseptansekriterium:** Skill i skjemaet kan brukast i staden for hardkoda `DESCRIPTIONS[]` og `DOC_LINKS[]`.

**Utført i commit 53def559:**

1. Migreringsscript (`scripts/migrate-schema-metadata.sh`):
   - Kopierte frå hardkoda `DESCRIPTIONS[]` til `description` i 23 skjema
   - Kopierte frå hardkoda `DOC_LINKS[]` til `see_also` i 19 skjema
   - Bevarte eksisterande `description` der den var meir omfattande enn hardkoda versjon

2. Metadata-ekstraktor (`src/assets/scripts/makefile/extract-schema-metadata.py`):
   - Hentar `description` og `see_also` frå `*-schema.yaml`
   - Returnerer JSON-objekt til `generate_schema_table()`

3. Oppdatert `generate_schema_table()` i `generate-readme-tables.sh`:
   - Fjerna hardkoda `DESCRIPTIONS[]` og `DOC_LINKS[]`
   - Hentar metadata via `extract-schema-metadata.py`
   - Formaterer tabell med dynamisk henta data

4. Verifisering:
   - Køyrde `make readme-tables`
   - Samanlikna generert `README.md` med tidlegare versjon
   - Identisk innhald (ingen diff) → vellukka migrasjon

### 3. ❌ Strukturert metadata for domene og artefaktar (AVVIST)

**Akseptansekriterium:** Avgjer om `domain.yaml` og `artifacts.yaml` skal implementerast.

**Vurdering (2026-07-30):**

- Domene-tabell og artefakt-tabell inneheld **manuelt kuratert narrativ** (som `mkdocs/docs/*.md`)
- Desse tabellane er stabile — nye domene eller artefakttypar vert lagt til sjeldent
- Dynamisk generering ville krevje nye metadatafiler (`domain.yaml`, `artifacts.yaml`) utan nemneverdig nytte
- **Konklusjon:** `generate_domain_table()` og `generate_artifacts_table()` fjerna frå scriptet — desse tabellane skal **ikkje** vere auto-genererte

**Utført:**
- Fjerna `generate_domain_table()` frå `generate-readme-tables.sh`
- Fjerna `generate_artifacts_table()` frå `generate-readme-tables.sh`
- Fjerna `IN_DOMAIN_TABLE` og `IN_ARTIFACTS_TABLE` frå hovudlogikken
- Domene-tabell og artefakt-tabell i `README.md` vert no vedlikehaldne manuelt

## Oppsummering (oppdatert 2026-07-30)

**✅ Fullført:**
- Skjema-tabell er 100% dynamisk (commit 53def559)
- Begrepskatalog-tabell er 100% dynamisk (tiltak 1)
- Modellkatalog-tabell er 100% dynamisk (tiltak 1)

**❌ Avvist (manuelt vedlikehald):**
- Domene-tabell inneheld manuelt kuratert narrativ — `generate_domain_table()` fjerna frå scriptet
- Artefakt-tabell inneheld manuelt kuratert narrativ — `generate_artifacts_table()` fjerna frå scriptet

**Resultat:**
- Tre av fem tabellar er no 100% dynamisk genererte
- To tabellar (domene, artefaktar) vert vedlikehaldne manuelt som del av dokumentasjonen

## Konvensjon: AUTO-GENERATED-kommentarar

Alle `BEGIN AUTO-GENERATED` og `END AUTO-GENERATED`-kommentarar skal innehalde script-/funksjon-referanse:

```markdown
<!-- BEGIN AUTO-GENERATED: <script-sti> [funksjon] -->
...
<!-- END AUTO-GENERATED: <script-sti> [funksjon] -->
```

**Eksempel (frå `README.md`):**

```markdown
<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_schema_table -->
| Domene | Skjema | Skildring | Dokumentasjon |
|---|---|---|---|
...
<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_schema_table -->
```

**Rasjonale:**
- Gjer det enkelt å finne kjelda til generert innhald
- Tydeleggjer kva funksjon som produserer kva bolkar (nyttig i store scripts med fleire funksjoner)
- Eintydig signal til menneske og maskin om kvar grensa går mellom manuelt og generert innhald

**Utrulling:**
- Alle nye AUTO-GENERATED-kommentarar skal følgje denne konvensjonen
- Eksisterande kommentarar skal oppdaterast opportunistisk (når scriptet vert endra)
