# README-tabellgenerering

## Kvifor auto-genererte tabellar?

README.md inneheld fire tabellar som gir oversikt over repoets struktur. Desse tabellane vert **automatisk genererte** for å sikre:

- **Konsistens** — identisk format og struktur på tvers av alle entries
- **Redusert vedlikehald** — nye skjema og domene dukkar opp automatisk
- **Færre feil** — ingen manuell kopiering av filstiar eller lenkjer

Tabellane vert genererte av `src/assets/scripts/generate-readme-tables.sh` og sett inn mellom HTML-kommentarar i README.md. CI køyrer scriptet automatisk ved endringar i `src/linkml/`, men du kan også køyre det manuelt.

---

## Tabelloversikt og kjelder

| # | Tabell | Innhald | Kjelde | Funksjon i generate-readme-tables.sh |
|---|---|---|---|---|
| 1 | **Domenetabell** | Oversikt over alle domene med skildringar og dokumentasjonslenkjer | 100 % hardkoda | `generate_domain_table()` (linje 21-38) |
| 2 | **Skjematabell** | Alle LinkML-skjema per domene med skildringar og dokumentasjonslenkjer | **Hybrid:** Skjemafiler auto-oppdaga frå `src/linkml/`, skildringar og lenkjer hardkoda | `generate_schema_table()` (linje 40-148) |
| 3 | **Artefakttabell** | Alle genererte artefaktar, deira brukstilfelle, W3C-semantikk og manifest-flagg | 100 % hardkoda | `generate_artifacts_table()` (linje 150-175) |
| 4 | **Modellkatalogtabell** | Automatisk genererte modellkatalogar per organisasjon | **Hybrid:** Modellkatalogfiler auto-oppdaga frå `src/linkml/modellkatalog/`, organisasjonsnamn hardkoda | `generate_modellkatalog_table()` (linje 177-204) |

---

## 1. Domenetabell

### Kva tabellen inneheld

```markdown
| Domene | Skildring | Dokumentasjon |
|---|---|---|
| [fair](fair/) | **FAIR**-metadataoverbygning ... | [FAIR principles](...) |
| [ap-no](ap-no/) | Norske W3C-applikasjonsprofiler ... | [RDF-baserte ...](...) |
```

### Korleis han vert generert

**Innhaldet er 100 % hardkoda** i `generate-readme-tables.sh` (linje 27-37).

### Korleis legge til nytt domene

1. Opprett domene-katalog: `src/linkml/<domene>/`
2. Rediger `generate-readme-tables.sh`:

```bash
generate_domain_table() {
  echo "| Domene | Skildring | Dokumentasjon |"
  echo "|---|---|---|"
  cat <<'EOF'
...
| [nytt-domene](nytt-domene/) | Skildring av domenet | [Dokumentasjon](https://...)
EOF
}
```

3. Køyr `make readme-tables` for å oppdatere README.md

---

## 2. Skjematabell

### Kva tabellen inneheld

```markdown
| Domene | Skjema | Skildring | Dokumentasjon |
|---|---|---|---|
| [fair](fair/) | [fair-metadata](fair/fair-metadata/) | **FAIR**-metadataoverbygning | [...](...) |
```

### Korleis han vert generert

**Hybrid:**
- **Skjemafiler vert auto-oppdaga** frå `src/linkml/` (linje 101-122)
- **Skildringar og dokumentasjonslenkjer er hardkoda** (linje 45-93)

Scriptet finn alle `*-schema.yaml`-filer under `src/linkml/<domene>/<skjema>/`, men inkluderer berre **hovudskjema** der filnamnet matcher katalognamnet (t.d. `modelldcat-ap-no/modelldcat-ap-no-schema.yaml` vert inkludert, men `modelldcat-ap-no/modelldcat-katalog-schema.yaml` vert hoppa over).

### Korleis legge til nytt skjema

**Steg 1:** Opprett skjemaet med `make new-model NAME=<skjema> DOMAIN=<domene>`

**Steg 2:** Legg til skildring og dokumentasjonslenkje i `generate-readme-tables.sh`:

```bash
# Hardkoda skildringar
declare -A DESCRIPTIONS=(
  ...
  ["mitt-nye-skjema"]="Kort skildring av skjemaet"
)

# Hardkoda dokumentasjonslenkjer (valfritt)
declare -A DOC_LINKS=(
  ...
  ["mitt-nye-skjema"]="[doc-lenke](https://...)"
)
```

**Steg 3:** Køyr `make readme-tables`

### Eksempel

Dersom du opprettar `src/linkml/oreg/folkeregisteret/folkeregisteret-schema.yaml`:

```bash
# I generate-readme-tables.sh:
declare -A DESCRIPTIONS=(
  ...
  ["folkeregisteret"]="Personopplysningar frå Folkeregisteret"
)

declare -A DOC_LINKS=(
  ...
  ["folkeregisteret"]="[skatteetaten.no/folkeregisteret](https://www.skatteetaten.no/...)"
)
```

Resultatet vert:

```markdown
| [oreg](oreg/) | [folkeregisteret](oreg/folkeregisteret/) | Personopplysningar frå Folkeregisteret | [skatteetaten.no/folkeregisteret](https://...) |
```

---

## 3. Artefakttabell

### Kva tabellen inneheld

```markdown
| Artefakt | Generator | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag |
|---|---|---|---|---|---|
| JSON-LD kontekst | [`gen-jsonld-context`](...) | `<skjema>-context.jsonld` | Mapping frå JSON til RDF | ✓ | `jsonld_context` |
```

### Korleis han vert generert

**Innhaldet er 100 % hardkoda** i `generate-readme-tables.sh` (linje 156-174).

### Korleis legge til ny artefakttype

1. Implementer ny generator i `Makefile` og `src/assets/scripts/`
2. Legg til rad i `generate_artifacts_table()`:

```bash
generate_artifacts_table() {
  ...
  cat <<'EOF'
...
| Nytt artefakt | [`gen-nytt`](COMMANDS.md#...) | `<skjema>-nytt.ext` | Brukstilfelle | — | `nytt_flag` |
EOF
}
```

3. Køyr `make readme-tables`

---

## 4. Modellkatalogtabell

### Kva tabellen inneheld

```markdown
| Modellkatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|
| [brreg-modellkatalog](...) | Brønnøysundregistra | Modellkatalog for ... | [`gen-modellkatalog-instance`](...) |
```

### Korleis han vert generert

**Hybrid:**
- **Modellkatalogfiler vert auto-oppdaga** frå `src/linkml/modellkatalog/` (linje 193-203)
- **Organisasjonsnamn er hardkoda** (linje 183-190)

### Korleis legge til ny modellkatalog

**Steg 1:** Opprett modellkatalogen (sjå [Ny organisasjon](ny-org.md))

**Steg 2:** Legg til organisasjonsnamn i `generate-readme-tables.sh`:

```bash
declare -A ORGS=(
  ...
  ["<alias>-modellkatalog"]="Offisielt organisasjonsnamn"
)
```

**Steg 3:** Køyr `make readme-tables`

### Eksempel

Dersom du opprettar `src/linkml/modellkatalog/statped-modellkatalog/`:

```bash
# I generate-readme-tables.sh:
declare -A ORGS=(
  ...
  ["statped-modellkatalog"]="Statped"
)
```

Resultatet vert:

```markdown
| [statped-modellkatalog](...) | Statped | Modellkatalog for Statped sine informasjonsmodellar | [`gen-modellkatalog-instance`](...) |
```

---

## CI-integrasjon

### Automatisk køyring

GitHub Actions-workflowen `.github/workflows/update-readme.yml` køyrer `generate-readme-tables.sh` automatisk ved endringar i:
- `src/linkml/**/*.yaml`
- `src/assets/scripts/generate-readme-tables.sh`

Workflowen commitar og pushar oppdatert README.md direkte til same PR.

### Manuell køyring

```bash
make readme-tables
```

Dette køyrer `src/assets/scripts/generate-readme-tables.sh README.md` og oppdaterer README.md i arbeidskatalogen.

---

## Feilsøking

### Skjemaet mitt dukkar ikkje opp i skjematabellen

**Sjekkliste:**

1. **Er skjemafila på rett stad?** → Skal vere `src/linkml/<domene>/<skjema>/<skjema>-schema.yaml`
2. **Matcher filnamnet katalognamnet?** → Filnamnet skal vere `<skjema>-schema.yaml` og katalogen skal heite `<skjema>`
3. **Er domenet i domene-rekkefølgja?** → Sjå linje 96 i `generate-readme-tables.sh`:

   ```bash
   DOMAIN_ORDER=("fair" "ap-no" "referanse" "ngr" "oreg" "fint" "samt" "begrepskatalog")
   ```

   Dersom domenet ditt ikkje er i denne lista, legg det til.

4. **Har du lagt til skildring?** → Sjå [Korleis legge til nytt skjema](#korleis-legge-til-nytt-skjema)

### Skildringa mi vert ikkje vist

Sjekk at skjemanamnet i `DESCRIPTIONS`-arrayet matcher katalognamnet eksakt:

```bash
# Riktig (matcher katalognamnet)
["mitt-skjema"]="Skildring..."

# Feil (bindestreker ↔ underscore)
["mitt_skjema"]="Skildring..."
```

### Dokumentasjonslenkja mi vert ikkje vist

`DOC_LINKS`-arrayet er **valfritt**. Dersom du ikkje legg til lenkje, vert cella tom.

Dersom du legg til lenkje, bruk full Markdown-lenkeformat:

```bash
["skjemanamn"]="[Lenketekst](https://...)"
```

---

## Relaterte filer

| Fil | Rolle |
|---|---|
| [`README.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/README.md) | Målfil for auto-genererte tabellar |
| [`src/assets/scripts/generate-readme-tables.sh`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/assets/scripts/generate-readme-tables.sh) | Genereringsscript |
| [`.github/workflows/update-readme.yml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/.github/workflows/update-readme.yml) | CI-workflow for automatisk oppdatering |
| [`Makefile`](https://github.com/brreg/linkml-datamodellering-no/blob/main/Makefile) | `make readme-tables`-target |

---

## Relatert dokumentasjon

- [Ny domenemodell](ny-domenemodell.md)
- [Ny organisasjon](ny-org.md)
- [CONTRIBUTING.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md)
