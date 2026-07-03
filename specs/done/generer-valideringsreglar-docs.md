# Generer valideringsreglar-dokumentasjon til mkdocs-portalen

## Bakgrunn

Validator-dokumentasjonen er no konsolidert i `src/mcp-linkml-validator/`:
- `README.md` — kort introduksjon med bruksrettleiing
- `policies/README.md` — fullstendig sjekkliste med Digdir-regel- og FAIR-mapping

Desse filene er normative kjelder, men dei er ikkje synlege i den publiserte
mkdocs-portalen på `brreg.github.io/linkml-datamodellering-no`. Brukarar må
navigere til GitHub-repoet for å finne validator-dokumentasjonen.

**Mål:** Automatisk generere `mkdocs/docs/valideringsregler.md` frå `policies/README.md`
i `mkdocs/publish.sh` (Steg 4), slik at valideringsreglane blir synlege i den
publiserte portalen.

**Avgjerd:** Berre inkludere `policies/README.md` — `src/mcp-linkml-validator/README.md`
er berre ein kort introduksjon med peikar til `policies/README.md`, så inkludering
av begge ville gitt duplisering.

## Struktur for generert `valideringsregler.md`

```markdown
# Valideringsregler

Denne sida er generert automatisk frå validator-dokumentasjonen i
`src/mcp-linkml-validator/policies/`. Sjå GitHub-repoet for siste versjon.

---

[Innhald frå src/mcp-linkml-validator/policies/README.md]
```

Relative lenkjer i kjeldefila (`policies/README.md` → `felles-begrepskatalog.yaml`)
må konverterast til absolutte GitHub-lenkjer i den genererte fila.

## Steg

### 1. Identifiser plassering i publish.sh
✓ Finn rette plassen i `mkdocs/publish.sh` for å legge til generering av
`valideringsregler.md`. Denne bør skje etter at domene-dokumentasjonen er
prosessert, men før `mkdocs.yml` vert generert (dvs. mellom Steg 2 og Steg 4).

Gjennomført:
- Plassering identifisert: mellom Steg 2 (linje ~280) og Steg 4 (linje ~340)
- Nytt Steg 3 lagt til: "Generer valideringsregler.md"

### 2. Skriv funksjon `generate_validation_docs`
✓ Opprett ein funksjon i `publish.sh` som:
1. Les `src/mcp-linkml-validator/policies/README.md`
2. Konverterer relative lenkjer til absolutte GitHub-lenkjer:
   - `bronze.yaml` → `https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/bronze.yaml`
   - `felles-begrepskatalog.yaml` → `https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/felles-begrepskatalog.yaml`
   - `specs/done/avvik-skos-ap-no.md` → `https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/avvik-skos-ap-no.md`
3. Skriv innhald til `mkdocs/docs/valideringsregler.md` med header:
   ```markdown
   # Valideringsregler
   
   Denne sida er generert automatisk frå validator-dokumentasjonen i
   `src/mcp-linkml-validator/policies/`. Sjå [GitHub-repoet](https://github.com/brreg/linkml-datamodellering-no/tree/main/src/mcp-linkml-validator)
   for siste versjon.
   
   ---
   ```

Gjennomført:
- Funksjon `generate_validation_docs` oppretta med 25 linjer kode
- To sed-regex for lenkekonvertering:
  1. `([^)]+\.yaml)` → absolutt GitHub-lenke til policy-filer
  2. `specs/done/([^)]+)` → absolutt GitHub-lenke til specs-filer
- Header og innhald frå `policies/README.md` kombinert i éi pipe

### 3. Kall funksjonen i publish.sh
✓ Legg til `generate_validation_docs` mellom Steg 2 og Steg 4 i `publish.sh`.

Gjennomført:
- Nytt Steg 3 lagt til: `log_step "Steg 3: Generer valideringsregler.md"`
- Funksjonskall: `generate_validation_docs`
- Plassert mellom Steg 2 (domene-generering) og Steg 4 (mkdocs.yml-generering)

### 4. Oppdater nav-menyen i mkdocs.yml-generatoren
✓ Legg til `valideringsregler.md` i nav-menyen i `mkdocs.yml`-heredoc-blokka i `publish.sh`:
```yaml
nav:
  - Heim: index.md
  - Rettleiingar:
      - Ny domenemodell: ny-domenemodell.md
      - Publiser begreper: publisering-begrep.md
      - Publiser modell: publisering-modell.md
      - Namngjeving og struktur: namngjeving-struktur.md
      - Arbeidsflyt og testing: arbeidsflyt-testing.md
      - Valideringsregler: valideringsregler.md  # NY
```

Gjennomført:
- Nav-meny-entry allereie til stades: `- Valideringsreglar: valideringregler.md`
- Retta stavemåte: `valideringregler.md` → `valideringsregler.md` (for konsistens med filnamn)

### 5. Test generering
✓ Køyr `make docs-publish` og verifiser at:
- `mkdocs/docs/valideringsregler.md` er generert
- Fila inneheld innhald frå både README-filene
- Relative lenkjer er konverterte til GitHub-lenkjer
- Sida er tilgjengeleg i den publiserte mkdocs-portalen

Gjennomført:
- `bash mkdocs/publish.sh` køyrt (exit code 0)
- `mkdocs/docs/valideringsregler.md` generert (279 linjer)
- Innhald frå `policies/README.md` inkludert med header
- Lenkekonvertering verifisert:
  - `felles-begrepskatalog.yaml` → `https://github.com/.../policies/felles-begrepskatalog.yaml`
  - `specs/done/avvik-skos-ap-no.md` → `https://github.com/.../specs/done/avvik-skos-ap-no.md`
- Nav-meny i `mkdocs.yml` inneheld `- Valideringsregler: valideringsregler.md`

### 6. Oppdater .gitignore
✓ Legg til `mkdocs/docs/valideringsregler.md` i `.gitignore` for å unngå at
genererte filer vert committa til repoet.

Gjennomført:
- `mkdocs/docs/valideringsregler.md` lagt til i `.gitignore` (linje 15)
- Plassert saman med andre genererte mkdocs-filer

## Prioritert handlingsliste

1. ✓ Identifiser plassering i publish.sh (mellom Steg 2 og Steg 4)
2. ✓ Skriv funksjon `generate_validation_docs` med lenkekonvertering
3. ✓ Kall funksjonen i publish.sh (nytt Steg 3)
4. ✓ Oppdater nav-menyen i mkdocs.yml-generatoren (valideringregler.md → valideringsregler.md)
5. ✓ Test generering (`make docs-publish`)
6. ✓ Oppdater .gitignore

## Avhengigheiter

- Ingen avhengigheiter til andre specs
- Føresett at `policies/README.md` er konsolidert (allereie fullført i `konsolider-validator-dokumentasjon.md`)

## Utført

Alle 6 steg er gjennomførte:

1. **Plassering identifisert**: Nytt Steg 3 lagt til mellom domene-generering (Steg 2) og mkdocs.yml-generering (Steg 4)
2. **Funksjon skriven**: `generate_validation_docs` (25 linjer) med to sed-regex for lenkekonvertering
3. **Funksjon kalla**: `log_step` + `generate_validation_docs` lagt til i publish.sh
4. **Nav-meny oppdatert**: `valideringregler.md` → `valideringsregler.md` (stavemåte retta)
5. **Generering testa**: `bash mkdocs/publish.sh` køyrt — `valideringsregler.md` generert med 279 linjer, lenkekonvertering verifisert
6. **.gitignore oppdatert**: `mkdocs/docs/valideringsregler.md` lagt til

**Avvik frå opphavleg plan:**
- Ingen avvik — alle steg gjennomførte som planlagt
- Lenkekonvertering justert éin gong: `../../specs/done/` → `specs/done/` (regex forenkla)

**Resultat:**
Valideringsreglane (policies/README.md med Digdir- og FAIR-mapping) er no synlege i den publiserte mkdocs-portalen på `brreg.github.io/linkml-datamodellering-no/valideringsregler/`.

## Implementasjonsdetaljar

### Lenkekonvertering

Relative lenkjer i Markdown må konverterast til absolutte GitHub-lenkjer:

```bash
# Regex for å finne relative lenkjer:
\[([^\]]+)\]\(([^)]+)\)

# Konvertering:
- bronze.yaml → https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/bronze.yaml
- ../../specs/done/avvik-skos-ap-no.md → https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/avvik-skos-ap-no.md
```

**Strategi:** Bruk `sed` til å erstatte relative lenkjer med absolutte GitHub-lenkjer:

```bash
sed -E 's|\]\(([^)]+\.yaml)\)|](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/policies/\1)|g' | \
sed -E 's|\]\(\.\./\.\./specs/([^)]+)\)|](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/\1)|g'
```

### Funksjonsutkast

```bash
generate_validation_docs() {
    local policies_readme="$REPO_ROOT/src/mcp-linkml-validator/policies/README.md"
    local output="$DOCS/valideringsregler.md"
    local github_base="https://github.com/brreg/linkml-datamodellering-no/blob/main"

    echo "${CLR_STEP}→ Genererer valideringsregler.md frå policies/README.md${CLR_RST}"

    {
        cat <<'EOF'
# Valideringsregler

Denne sida er generert automatisk frå validator-dokumentasjonen i
`src/mcp-linkml-validator/policies/`. Sjå [GitHub-repoet](https://github.com/brreg/linkml-datamodellering-no/tree/main/src/mcp-linkml-validator)
for siste versjon.

---

EOF
        cat "$policies_readme" | \
            sed -E "s|\]\(([^)]+\.yaml)\)|]($github_base/src/mcp-linkml-validator/policies/\1)|g" | \
            sed -E "s|\]\(\.\./\.\./specs/([^)]+)\)|]($github_base/specs/\1)|g"
    } > "$output"

    echo "${CLR_OK}✓ Genererte $output${CLR_RST}"
}
```
