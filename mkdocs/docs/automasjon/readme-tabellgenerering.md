# README-tabellgenerering

## Kvifor auto-genererte tabellar?

README.md inneheld tre tabellar som gir oversikt over repoets struktur. Desse tabellane vert **automatisk genererte** for å sikre:

- **Konsistens** — identisk format og struktur på tvers av alle entries
- **Redusert vedlikehald** — nye skjema og domene dukkar opp automatisk
- **Færre feil** — ingen manuell kopiering av filstiar eller lenkjer

Tabellane vert genererte av `src/assets/scripts/makefile/generate-readme-tables.sh` og sett inn mellom HTML-kommentarar i README.md. CI køyrer scriptet automatisk ved endringar i `src/linkml/`, men du kan også køyre det manuelt.

---

## Tabelloversikt og kjelder

| # | Tabell | Innhald | Kjelde | Funksjon i generate-readme-tables.sh |
|---|---|---|---|---|
| 1 | **Skjematabell** | Alle LinkML-skjemaer per domene med skildringar og dokumentasjonslenkjer | **100 % auto-generert** frå skjemafiler via `extract-schema-metadata.py` | `generate_schema_table()` (linje 25-92) |
| 2 | **Begrepskatalog-tabell** | Automatisk genererte begrepskatalogar per organisasjon | **100 % auto-generert** frå skjemafiler | `generate_begrepskatalog_table()` (linje 94-124) |
| 3 | **Modellkatalog-tabell** | Automatisk genererte modellkatalogar per organisasjon | **100 % auto-generert** frå skjemafiler | `generate_modellkatalog_table()` (linje 126-156) |

---

## 1. Skjematabell

### Kva tabellen inneheld

```markdown
| Domene | Skjema | Skildring | Dokumentasjon |
|---|---|---|---|
| [fair](fair/) | [fair-metadata](fair/fair-metadata/) | **FAIR**-metadataoverbygning | [www.go-fair.org](https://...) |
| [ap-no](ap-no/) | [dcat-ap-no](ap-no/dcat-ap-no/) | Standard for beskrivelse av datasett, ... | [data.norge.no](https://...) |
```

### Korleis han vert generert

**100 % auto-generert:**
- **Skjemafiler vert auto-oppdaga** frå `src/linkml/<domene>/<skjema>/<skjema>-schema.yaml` (linje 35-57)
- **Skildringar vert henta** frå `description:`-feltet i kvar skjemafil via `extract-schema-metadata.py` (linje 72)
- **Dokumentasjonslenkjer vert henta** frå første URI i `see_also:`-lista via `extract-schema-metadata.py` (linje 75)

Scriptet finn alle `*-schema.yaml`-filer under `src/linkml/<domene>/<skjema>/`, men inkluderer berre **hovudskjema** der filnamnet matcher katalognamnet (t.d. `modelldcat-ap-no/modelldcat-ap-no-schema.yaml` vert inkludert, men `modelldcat-ap-no/modelldcat-katalog-schema.yaml` vert hoppa over).

**Domene som vert inkluderte:** fair, ap-no, referanse, ngr, oreg, fint, samt (linje 30)

**Domene som vert ekskluderte:** modellkatalog, begrepskatalog (desse har eigne tabellar)

### Korleis legge til nytt skjema

**Steg 1:** Opprett skjemaet med `make new-modell NAME=<skjema> DOMAIN=<domene>`

**Steg 2:** Fyll inn `description:` og `see_also:` i skjemafila `src/linkml/<domene>/<skjema>/<skjema>-schema.yaml`:

```yaml
description: >-
  Kort skildring av skjemaet som vises i README-tabellen.
  Multiline-format er støtta.

see_also:
  - https://www.eksempel.no/dokumentasjon
```

**Steg 3:** Køyr `make readme-tables` — README.md vert oppdatert automatisk

### Eksempel

Dersom du opprettar `src/linkml/oreg/folkeregisteret/folkeregisteret-schema.yaml`:

```yaml
# I src/linkml/oreg/folkeregisteret/folkeregisteret-schema.yaml
id: https://data.norge.no/oreg/folkeregisteret
name: folkeregisteret
title: Folkeregisteret
description: >-
  Personopplysningar frå Folkeregisteret ved Skatteetaten.
  Inneheld namn, adresse, fødselsnummer og relasjonar.
see_also:
  - https://www.skatteetaten.no/person/folkeregisteret/
```

Resultatet vert:

```markdown
| [oreg](oreg/) | [folkeregisteret](oreg/folkeregisteret/) | Personopplysningar frå Folkeregisteret ved Skatteetaten. Inneheld namn, adresse, fødselsnummer og relasjonar. | [skatteetaten.no](https://www.skatteetaten.no/person/folkeregisteret/) |
```

---

## 2. Begrepskatalog-tabell

### Kva tabellen inneheld

```markdown
| Domene | Begrepskatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [begrepskatalog](...) | [brreg-begrepskatalog](...) | Brønnøysundregistra | Begrepskatalog for Brønnøysundregistra sine begrep | [`gen-begrepskatalog-instance`](...) |
```

### Korleis han vert generert

**100 % auto-generert:**
- **Begrepskatalogfiler vert auto-oppdaga** frå `src/linkml/begrepskatalog/` (linje 102-123)
- **Organisasjonsnamn vert ekstraherast** frå `title:`-feltet i skjemafila ved å fjerne " - Begrepskatalog" (linje 107-114)

### Korleis legge til ny begrepskatalog

**Steg 1:** Opprett begrepskatalog-skeleton (sjå [Ny organisasjon](../kom-i-gang/ny-org.md))

**Steg 2:** Fyll inn `title:` i skjemafila `src/linkml/begrepskatalog/<katalog>/<katalog>-schema.yaml`:

```yaml
title: "Organisasjonsnamn - Begrepskatalog"
```

Organisasjonsnamnet vert ekstraherast automatisk ved å fjerne " - Begrepskatalog" frå `title`.

**Steg 3:** Køyr `make readme-tables`

### Eksempel

```yaml
# I src/linkml/begrepskatalog/statped-begrepskatalog/statped-begrepskatalog-schema.yaml
id: https://data.norge.no/begrepskatalog/statped
name: statped-begrepskatalog
title: "Statped - Begrepskatalog"
```

Resultatet vert:

```markdown
| [begrepskatalog](...) | [statped-begrepskatalog](...) | Statped | Begrepskatalog for Statped sine begrep | [`gen-begrepskatalog-instance`](...) |
```

---

## 3. Modellkatalog-tabell

### Kva tabellen inneheld

```markdown
| Domene | Modellkatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [modellkatalog](...) | [brreg-modellkatalog](...) | Brønnøysundregistra | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar | [`gen-modellkatalog-instance`](...) |
```

### Korleis han vert generert

**100 % auto-generert:**
- **Modellkatalogfiler vert auto-oppdaga** frå `src/linkml/modellkatalog/` (linje 134-155)
- **Organisasjonsnamn vert ekstraherast** frå `title:`-feltet i skjemafila ved å fjerne " - Modellkatalog" (linje 138-146)

### Korleis legge til ny modellkatalog

**Steg 1:** Opprett modellkatalog-skeleton (sjå [Ny organisasjon](../kom-i-gang/ny-org.md))

**Steg 2:** Fyll inn `title:` i skjemafila `src/linkml/modellkatalog/<katalog>/<katalog>-schema.yaml`:

```yaml
title: "Organisasjonsnamn - Modellkatalog"
```

Organisasjonsnamnet vert ekstraherast automatisk ved å fjerne " - Modellkatalog" frå `title`.

**Steg 3:** Køyr `make readme-tables`

### Eksempel

Dersom du opprettar `src/linkml/modellkatalog/statped-modellkatalog/`:

```yaml
# I src/linkml/modellkatalog/statped-modellkatalog/statped-modellkatalog-schema.yaml
id: https://data.norge.no/modellkatalog/statped
name: statped-modellkatalog
title: "Statped - Modellkatalog"
```

Resultatet vert:

```markdown
| [modellkatalog](...) | [statped-modellkatalog](...) | Statped | Modellkatalog for Statped sine informasjonsmodellar | [`gen-modellkatalog-instance`](...) |
```

---

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

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py \
  src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml title

# Output: Brønnøysundregistra - Modellkatalog
```

---

## CI-integrasjon

### Automatisk køyring

GitHub Actions-workflowen `.github/workflows/update-readme.yml` køyrer `generate-readme-tables.sh` automatisk ved endringar i:
- `src/linkml/**/*.yaml`
- `src/assets/scripts/makefile/generate-readme-tables.sh`
- `src/assets/scripts/makefile/extract-schema-metadata.py`

Workflowen commitar og pushar oppdatert README.md direkte til same PR.

### Manuell køyring

```bash
make readme-tables
```

Dette køyrer `src/assets/scripts/makefile/generate-readme-tables.sh README.md` og oppdaterer README.md i arbeidskatalogen.

---

## Feilsøking

### Skjemaet mitt dukkar ikkje opp i skjematabellen

**Sjekkliste:**

1. **Er skjemafila på rett stad?** → Skal vere `src/linkml/<domene>/<skjema>/<skjema>-schema.yaml`
2. **Matcher filnamnet katalognamnet?** → Filnamnet skal vere `<skjema>-schema.yaml` og katalogen skal heite `<skjema>`
3. **Er domenet i domene-rekkefølgja?** → Sjå linje 30 i `generate-readme-tables.sh`:

   ```bash
   DOMAIN_ORDER=("fair" "ap-no" "referanse" "ngr" "oreg" "fint" "samt")
   ```

   Dersom domenet ditt ikkje er i denne lista, legg det til.

4. **Har du sett `description:`-feltet?** → Sjå [Korleis legge til nytt skjema](#korleis-legge-til-nytt-skjema)

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

**Debugging:** Test metadata-ekstraksjon direkte:

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py \
  src/linkml/<domene>/<skjema>/<skjema>-schema.yaml description
```

Dersom output er tom, sjekk YAML-syntaksen i skjemafila.

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

**Debugging:** Test metadata-ekstraksjon direkte:

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py \
  src/linkml/<domene>/<skjema>/<skjema>-schema.yaml see_also
```

### Organisasjonsnamnet for modellkatalog/begrepskatalog er feil

Organisasjonsnamnet vert ekstraherast frå `title:`-feltet i skjemafila ved å fjerne " - Modellkatalog" eller " - Begrepskatalog":

```bash
python3 src/assets/scripts/makefile/extract-schema-metadata.py \
  src/linkml/modellkatalog/<katalog>/<katalog>-schema.yaml title

# Forventar: "Organisasjonsnamn - Modellkatalog"
```

Dersom `title:` ikkje følgjer mønsteret, vert organisasjonsnamnet "Ukjend". Korriger `title:`-feltet i skjemafila:

```yaml
# Riktig
title: "Brønnøysundregistra - Modellkatalog"

# Feil (manglar " - Modellkatalog")
title: "Brønnøysundregistra"
```

---

## Relaterte filer

| Fil | Rolle |
|---|---|
| [`README.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/README.md) | Målfil for auto-genererte tabellar |
| [`src/assets/scripts/makefile/generate-readme-tables.sh`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/assets/scripts/makefile/generate-readme-tables.sh) | Genereringsscript |
| [`src/assets/scripts/makefile/extract-schema-metadata.py`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/assets/scripts/makefile/extract-schema-metadata.py) | Metadata-ekstraksjon frå YAML-skjema |
| [`.github/workflows/update-readme.yml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/.github/workflows/update-readme.yml) | CI-workflow for automatisk oppdatering |
| [`Makefile`](https://github.com/brreg/linkml-datamodellering-no/blob/main/Makefile) | `make readme-tables`-target |

---

## Relatert dokumentasjon

- [Ny domenemodell](../kom-i-gang/ny-domenemodell.md)
- [Ny organisasjon](../kom-i-gang/ny-org.md)
- [CONTRIBUTING.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md)
