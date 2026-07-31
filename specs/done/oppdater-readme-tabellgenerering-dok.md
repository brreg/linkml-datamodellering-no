# Oppdater mkdocs/docs/readme-tabellgenerering.md basert på siste versjon av generate-readme-tables.sh

## Bakgrunn

`mkdocs/docs/readme-tabellgenerering.md` dokumenterer korleis `src/assets/scripts/makefile/generate-readme-tables.sh` fungerer og korleis nye domene/skjema/modellkatalogar vert lagde til i README-tabellane.

Dokumentasjonen vart oppretta før scriptet vart refaktorert til å bruke `extract-schema-metadata.py` for dynamisk metadata-ekstraksjon. Følgjande endringar har skjedd i scriptet sidan dokumentasjonen vart skrive:

### Endringar i `generate-readme-tables.sh`

1. **Fjerna hardkoda skildringar og dokumentasjonslenkjer** — `DESCRIPTIONS` og `DOC_LINKS`-arrayane er fjerna. Scriptet henter no `description` og `see_also` direkte frå kvar skjemafil via `extract-schema-metadata.py` (linje 72-84).

2. **Dynamisk organisasjonsnamn for modellkatalogar og begrepskatalogar** — Tidlegare var organisasjonsnamn hardkoda i `ORGS`-arrayet. No henter scriptet `title`-feltet frå kvar skjemafil og ekstrahrer organisasjonsnamnet ved å fjerne " - Modellkatalog" / " - Begrepskatalog" med `sed` (linje 138-146 og linje 107-114).

3. **Tre separate tabellar** — Scriptet genererer no:
   - Skjematabell (hovuddomene: fair, ap-no, referanse, ngr, oreg, fint, samt)
   - Begrepskatalog-tabell (eige domene)
   - Modellkatalog-tabell (eige domene)

   Tidlegare dokumentasjon nemner berre to tabellar (domene, skjema, artefakt, modellkatalog).

4. **Avhengighet av `extract-schema-metadata.py`** — Scriptet brukar no Python-scriptet `src/assets/scripts/makefile/extract-schema-metadata.py` for å hente:
   - `description` (multiline eller einlinjes)
   - `see_also` (første URI)
   - `title` (for organisasjonsnamn)

## Føremål

Oppdatere `mkdocs/docs/readme-tabellgenerering.md` slik at dokumentasjonen stemmer med faktisk oppførsel i `generate-readme-tables.sh`.

## Endringar som må gjerast

### 1. Fjern seksjon om hardkoda DESCRIPTIONS og DOC_LINKS

**Fjern eller oppdater:**
- Tabell på linje 17-22 — rad 2 skal endre frå "**Hybrid:** Skjemafiler auto-oppdaga, skildringar og lenkjer hardkoda" til "100 % auto-generert frå skjemafiler"
- Seksjon "Korleis legge til nytt skjema" (linje 79-122) — fjern steg 2 og 3 om å hardkode `DESCRIPTIONS` og `DOC_LINKS`, erstatt med instruksjon om å setje `description:` og `see_also:` i skjemafila

**Ny instruksjon skal vere:**

```markdown
### Korleis legge til nytt skjema

**Steg 1:** Opprett skjemaet med `make new-model NAME=<skjema> DOMAIN=<domene>`

**Steg 2:** Fyll inn `description:` og `see_also:` i skjemafila `src/linkml/<domene>/<skjema>/<skjema>-schema.yaml`:

```yaml
description: >-
  Kort skildring av skjemaet som vises i README-tabellen.
  Multiline-format er støtta.

see_also:
  - https://www.eksempel.no/dokumentasjon
```

**Steg 3:** Køyr `make readme-tables` — README.md vert oppdatert automatisk
```

### 2. Oppdater seksjon om modellkatalog-tabell og legg til begrepskatalog-tabell

**Oppdater linje 159-206:**
- Endre frå "**Hybrid:** Modellkatalogfiler auto-oppdaga, organisasjonsnamn hardkoda"
- Til "**100 % auto-generert:** Modellkatalogfiler auto-oppdaga, organisasjonsnamn ekstraherast frå `title`-feltet i skjemafila"

**Legg til ny seksjon før modellkatalog-seksjonen:**

```markdown
## 4. Begrepskatalog-tabell

### Kva tabellen inneheld

```markdown
| Domene | Begrepskatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [begrepskatalog](...) | [brreg-begrepskatalog](...) | Brønnøysundregistra | Begrepskatalog for Brønnøysundregistra sine begrep | [`gen-begrepskatalog-instance`](...) |
```

### Korleis han vert generert

**100 % auto-generert:**
- **Begrepskatalogfiler vert auto-oppdaga** frå `src/linkml/begrepskatalog/`
- **Organisasjonsnamn vert ekstraherast** frå `title`-feltet i skjemafila (regex: `/^(.+) - Begrepskatalog/`)

### Korleis legge til ny begrepskatalog

**Steg 1:** Opprett begrepskatalogskeleton (sjå [Ny organisasjon](ny-org.md))

**Steg 2:** Fyll inn `title:` i skjemafila `src/linkml/begrepskatalog/<katalog>/<katalog>-schema.yaml`:

```yaml
title: "Organisasjonsnamn - Begrepskatalog"
```

Organisasjonsnamnet vert ekstraherast automatisk ved å fjerne " - Begrepskatalog" frå `title`.

**Steg 3:** Køyr `make readme-tables`

### Eksempel

```yaml
# I src/linkml/begrepskatalog/statped-begrepskatalog/statped-begrepskatalog-schema.yaml
title: "Statped - Begrepskatalog"
```

Resultatet vert:

```markdown
| [begrepskatalog](...) | [statped-begrepskatalog](...) | Statped | Begrepskatalog for Statped sine begrep | [`gen-begrepskatalog-instance`](...) |
```
```

### 3. Oppdater modellkatalog-seksjon tilsvarande

**Steg 2** skal endre frå hardkoding av `ORGS`-arrayet til:

```markdown
**Steg 2:** Fyll inn `title:` i skjemafila `src/linkml/modellkatalog/<katalog>/<katalog>-schema.yaml`:

```yaml
title: "Organisasjonsnamn - Modellkatalog"
```

Organisasjonsnamnet vert ekstraherast automatisk ved å fjerne " - Modellkatalog" frå `title`.
```

### 4. Oppdater tabelloversikt (linje 17-22)

Legg til rad for begrepskatalog-tabell:

```markdown
| # | Tabell | Innhald | Kjelde | Funksjon i generate-readme-tables.sh |
|---|---|---|---|---|
| 1 | **Skjematabell** | Alle LinkML-skjemaer per domene med skildringar og dokumentasjonslenkjer | **100 % auto-generert** frå skjemafiler via `extract-schema-metadata.py` | `generate_schema_table()` (linje 25-92) |
| 2 | **Begrepskatalog-tabell** | Automatisk genererte begrepskatalogar per organisasjon | **100 % auto-generert** frå skjemafiler | `generate_begrepskatalog_table()` (linje 94-124) |
| 3 | **Modellkatalog-tabell** | Automatisk genererte modellkatalogar per organisasjon | **100 % auto-generert** frå skjemafiler | `generate_modellkatalog_table()` (linje 126-156) |
```

(Fjern domenetabell og artefakttabell frå oversikta — desse er ikkje lenger auto-genererte via scriptet.)

### 5. Legg til seksjon om avhengigheter

**Legg til ny seksjon før "CI-integrasjon":**

```markdown
## Avhengigheter

`generate-readme-tables.sh` brukar Python-scriptet `extract-schema-metadata.py` for å hente metadata frå LinkML-skjemafiler:

**`src/assets/scripts/makefile/extract-schema-metadata.py`**

Støtta felt:
- `description` — multiline eller einlinjes YAML-verdi, strippar `>-` og `>` og konverter til einlinjes tekst
- `see_also` — første URI frå lista
- `title` — einlinjes YAML-verdi
- `annotations.utgiver` — einlinjes YAML-verdi

**Bruk:**

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py <skjemafil> <felt>
```

**Eksempel:**

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py \
  src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml description

# Output: Adresseinformasjon frå Det sentrale folkeregisteret (DSF)
```
```

### 6. Oppdater feilsøking-seksjonen (linje 230-262)

**Fjern:**
- "Skildringa mi vert ikkje vist" — ikkje lenger relevant
- "Dokumentasjonslenkja mi vert ikkje vist" — ikkje lenger relevant

**Legg til:**

```markdown
### Skildringa mi vert ikkje vist

Sjekk at `description:`-feltet er sett i skjemafila:

```bash
grep -A 5 "^description:" src/linkml/<domene>/<skjema>/<skjema>-schema.yaml
```

Dersom `description:` manglar, legg det til:

```yaml
description: >-
  Kort skildring av skjemaet.
```

### Dokumentasjonslenkja mi vert ikkje vist

Sjekk at `see_also:`-feltet er sett i skjemafila og inneheld minst éin URI:

```bash
grep -A 3 "^see_also:" src/linkml/<domene>/<skjema>/<skjema>-schema.yaml
```

Dersom `see_also:` manglar, legg det til:

```yaml
see_also:
  - https://www.eksempel.no/dokumentasjon
```

### Organisasjonsnamnet for modellkatalog/begrepskatalog er feil

Organisasjonsnamnet vert ekstraherast frå `title:`-feltet i skjemafila ved å fjerne " - Modellkatalog" eller " - Begrepskatalog":

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py \
  src/linkml/modellkatalog/<katalog>/<katalog>-schema.yaml title

# Forventar: "Organisasjonsnamn - Modellkatalog"
```

Dersom `title:` ikkje følgjer mønsteret, vert organisasjonsnamnet "Ukjend". Korriger `title:`-feltet i skjemafila.
```

## Handlingsliste

- [x] Oppdater tabelloversikt (linje 17-22) — fjern domene- og artefakttabellar, legg til begrepskatalog
- [x] Fjern seksjon 1 (Domenetabell) og seksjon 3 (Artefakttabell) — desse vert ikkje genererte av scriptet
- [x] Oppdater seksjon 2 (Skjematabell) — fjern hardkoda DESCRIPTIONS/DOC_LINKS, legg til dynamisk metadata-ekstraksjon
- [x] Legg til ny seksjon 4 (Begrepskatalog-tabell) med dokumentasjon om `title`-ekstraksjon
- [x] Oppdater seksjon 5 (Modellkatalog-tabell, tidlegare 4) med `title`-ekstraksjon
- [x] Legg til seksjon "Avhengigheter" med dokumentasjon om `extract-schema-metadata.py`
- [x] Oppdater feilsøking-seksjonen — fjern DESCRIPTIONS/DOC_LINKS-feil, legg til metadata-feil
- [x] Verifiser at alle linjenummer-referansar til scriptet stemmer med faktisk linje i `generate-readme-tables.sh`

## Utført

**Dato:** 2026-07-31

Fullstendig omskriving av `mkdocs/docs/readme-tabellgenerering.md` for å reflektere siste versjon av `generate-readme-tables.sh`:

**Hovudendringar:**
1. Fjerna seksjonar om domenetabell og artefakttabell (ikkje lenger auto-genererte)
2. Oppdatert tabelloversikt til tre tabellar: skjema, begrepskatalog, modellkatalog
3. Omskriven skjematabell-seksjon til å dokumentere dynamisk metadata-ekstraksjon via `extract-schema-metadata.py`
4. Lagt til ny seksjon om begrepskatalog-tabell med `title`-ekstraksjon
5. Oppdatert modellkatalog-seksjon med `title`-ekstraksjon i staden for hardkoda ORGS-array
6. Lagt til "Avhengigheter"-seksjon med dokumentasjon om `extract-schema-metadata.py`
7. Oppdatert feilsøking-seksjon med debugging-kommandoar for metadata-ekstraksjon
8. Verifisert linjenummer-referansar mot faktisk linje i scriptet

**Resultat:**
Dokumentasjonen stemmer no med faktisk oppførsel i `generate-readme-tables.sh` (versjon per 2026-07-31).
