# Konfigurerbar lenke-tekst for offisiell referanse

## Bakgrunn

Kvar LinkML-modell kan ha ein `external_spec_url` i `manifest.yaml` som peikar til den
offisielle spesifikasjonen. Denne vert vist i ein "Offisiell referanse"-boks i
`mkdocs/docs/<domain>/<schema>/index.md`.

For tida er lenke-teksten hardkoda til skjemanamnet (t.d. `cpsv-ap-no`), men det er
ønskjeleg å kunne konfigurere ein meir deskriptiv tekst, t.d.
"Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)" for
`https://data.norge.no/specification/cpsv-ap-no`.

**Noverande oppførsel:**

```markdown
!!! info "Offisiell referanse"
    📘 [cpsv-ap-no](https://informasjonsforvaltning.github.io/cpsv-ap-no/)
```

**Ønskt oppførsel:**

```markdown
!!! info "Offisiell referanse"
    📘 [Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)](https://data.norge.no/specification/cpsv-ap-no)
```

## Løysing

### 1. Utvid `manifest.yaml`-format med valfritt felt `external_spec_label`

Legg til eit valfritt felt `external_spec_label` i `manifest.yaml`:

```yaml
external_spec_url: https://data.norge.no/specification/cpsv-ap-no
external_spec_label: "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)"
```

Dersom `external_spec_label` manglar, fall tilbake til noverande oppførsel (skjemanamn).

### 2. Oppdater `metadata_parsers.sh` med `get_external_spec_label()`

Legg til ein funksjon som hentar `external_spec_label` frå manifest:

```bash
get_external_spec_label() {
    local manifest="$1"
    [ ! -f "$manifest" ] && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('external_spec_label', ''))" 2>/dev/null || echo ""
}
```

### 3. Oppdater `external_reference.sh` til å bruke konfigurerbar label

Endre `generate_external_reference()` til å hente og bruke `external_spec_label`:

```bash
generate_external_reference() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"
    local external_spec=$(get_external_spec_url "$manifest")

    [ -z "$external_spec" ] && return 0

    local label=$(get_external_spec_label "$manifest")
    [ -z "$label" ] && label="$schema"  # Fallback til skjemanamn

    echo "---"
    echo ""
    echo "!!! info \"Offisiell referanse\""
    echo "    📘 [$label]($external_spec)"
    echo ""
}
```

### 4. Dokumenter i `manifest-config.md`

Legg til dokumentasjon om `external_spec_label` i `mkdocs/docs/manifest-config.md`:

```markdown
#### `external_spec_label` (valfritt)

Lenke-tekst for den offisielle spesifikasjonen. Dersom utelatt, vert skjemanamnet brukt.

**Eksempel:**

```yaml
external_spec_url: https://data.norge.no/specification/cpsv-ap-no
external_spec_label: "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)"
```
```

### 5. Oppdater `cpsv-ap-no/manifest.yaml` som døme

Legg til `external_spec_label` i `cpsv-ap-no/manifest.yaml`:

```yaml
external_spec_url: https://informasjonsforvaltning.github.io/cpsv-ap-no/
external_spec_label: "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)"
```

(Merk: URL-en i manifest er `https://informasjonsforvaltning.github.io/cpsv-ap-no/`,
ikkje `https://data.norge.no/specification/cpsv-ap-no` som brukaren nemnde — beheld
eksisterande URL.)

## Handlingsliste

- [x] Legg til `get_external_spec_label()` i `mkdocs/lib/utils/metadata_parsers.sh`
- [x] Oppdater `generate_external_reference()` i `mkdocs/lib/sections/external_reference.sh`
- [x] Legg til `external_spec_label` i `src/linkml/ap-no/cpsv-ap-no/manifest.yaml`
- [x] Dokumenter `external_spec_label` i `mkdocs/docs/manifest-config.md`
- [x] Test med `make docs-publish` og verifiser at lenke-teksten er korrekt i
      `mkdocs/docs/ap-no/cpsv-ap-no/index.md`

## Utført

Alle tiltak er utførte:

1. `get_external_spec_label()` lagt til i `mkdocs/lib/utils/metadata_parsers.sh` — hentar
   `external_spec_label` frå manifest med Python YAML-parsing
2. `generate_external_reference()` oppdatert i `mkdocs/lib/sections/external_reference.sh` —
   brukar `external_spec_label` dersom sett, elles fallback til skjemanamn
3. `external_spec_label` lagt til i `src/linkml/ap-no/cpsv-ap-no/manifest.yaml` med verdien
   "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)"
4. Dokumentasjon lagt til i `mkdocs/docs/manifest-config.md` med brukstilfelle og døme
5. Testa med `make docs-publish` — lenke-teksten i `mkdocs/docs/ap-no/cpsv-ap-no/index.md`
   er no "Spesifikasjon for tjeneste- og hendelsesbeskrivelser (CPSV-AP-NO)" i staden for
   "cpsv-ap-no". Fallback-oppførsel fungerer korrekt for skjema utan `external_spec_label`
   (t.d. `dcat-ap-no` viser framleis "dcat-ap-no").

## Alternativ

**Alternativ 1: Bruk `schema.title` i staden for nytt felt**

I staden for `external_spec_label`, bruk `title`-feltet frå skjemaet sjølv
(`cpsv-ap-no-schema.yaml`). Dette vil vere meir DRY, men krev parsing av YAML-skjemaet
i `publish.sh`, som kan vere tregare enn `manifest.yaml`-parsing.

**Vurdering:** Avvis — `title` i skjemaet er ein kort tittel for modellen (t.d.
"CPSV-AP-NO"), ikkje ein deskriptiv lenke-tekst for den offisielle spesifikasjonen.
Desse to har ulike formål og bør vere separate.

**Alternativ 2: Hardkod lenke-tekst per skjema i `external_reference.sh`**

Bruk ein case-statement i `external_reference.sh` for å mappe skjemanamn til
lenke-tekst.

**Vurdering:** Avvis — bryt DRY-prinsippet og gjer det vanskelegare å vedlikehalde.
