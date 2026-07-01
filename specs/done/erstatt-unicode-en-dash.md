# Erstatt Unicode en-dash (U+2013) med ASCII hyphen (U+002d)

## Bakgrunn

VS Code-linter gjev advarsel om at U+2013 ("-", en-dash) kan forvekslast med
U+002d ("-", ASCII hyphen-minus) i kjeldekode. En-dash er ein typografisk
symbol som vert brukt i løpande tekst (t.d. "2020-2026"), medan ASCII hyphen
er standardteiknet i programmeringsspråk og markup.

I dette repoet er U+2013 brukt inkonsekvent — både i Markdown-dokumentasjon,
YAML-filer, Python-scripts og shell-scripts. Dette skapar forvirring og kan
føre til usynlege feil (t.d. YAML-parsing som tolkar en-dash som ein annan
karakter enn hyphen).

**Omfang:**
- 159 filer påverka
- 267 førekomstar i Markdown-filer (`.md`)
- 83 førekomstar i YAML-filer (`.yml`, `.yaml`)
- 11 førekomstar i shell-scripts (`.sh`, `.bash`)
- 1 førekomst i Python-filer (`.py`)

**Kjelde:** VS Code-advarsel ved redigering av `specs/backlog/validering-automatisk-release-trigger.md`.

---

## Design

### Strategi: Global søk-og-erstatt med validering

En-dash (-) skal erstattast med ASCII hyphen (-) i **alle** tekstfiler i
repoet, med følgjande unntak:

- **`generated/`-katalogen:** Alltid ekskludert (byggoutput).
- **`.git/`-katalogen:** Alltid ekskludert (git-internals).
- **Binære filer:** Automatisk ekskludert av `grep`/`sed`.

### Filtypar som skal oppdaterast

| Filtype | Mønster | Antal linjer påverka |
|---|---|---|
| Markdown | `*.md` | 267 |
| YAML | `*.yml`, `*.yaml` | 83 |
| Shell | `*.sh`, `*.bash` | 11 |
| Python | `*.py` | 1 |

**Total:** 362 linjer i 159 filer.

### Ersatt-kommando

```bash
find . -type f \
  \( -name "*.md" -o -name "*.py" -o -name "*.yml" -o -name "*.yaml" -o -name "*.sh" -o -name "*.bash" \) \
  ! -path "./generated/*" ! -path "./.git/*" \
  -exec sed -i 's/-/-/g' {} +
```

`sed -i 's/-/-/g'` erstattar alle førekomstar av en-dash med hyphen in-place.

### Validering etter erstatning

1. **Grep-sjekk:** Verifiser at ingen U+2013 finst igjen:
   ```bash
   grep -r $'-' --include="*.md" --include="*.py" --include="*.yml" --include="*.yaml" --include="*.sh" --include="*.bash" . 2>/dev/null
   ```
   Output skal vere tom.

2. **YAML-validering:** Køyr `make validate` for å sikre at YAML-filer framleis
   er gyldige (en-dash i YAML-verdiar kan ha vore tolka annleis).

3. **Git-diff:** Gjennomgå diff for å sjå at berre en-dash → hyphen-erstatning
   skjedde, ingen utilsikta endringar.

### Oppdatering av CLAUDE.md

Legg til regel under «Dokumentasjonsportal (mkdocs)» eller «Namngjeving»:

```markdown
### Teiknsett

- **ASCII hyphen (U+002d, "-")** skal brukast i all kjeldekode, YAML-filer,
  shell-scripts og Markdown-dokumentasjon.
- **Unicode en-dash (U+2013, "-")** skal **ikkje** brukast — det kan
  forvekslast med ASCII hyphen og skape parsing-problem i YAML og andre format.
- **Em-dash (U+2014, "—")** kan brukast i løpande prosa der typografisk
  distinksjon er ønskt, men bør unngåast i teknisk dokumentasjon.
```

---

## Avhengigheiter

- Ingen — dette er ein rein tekstleg erstatning utan funksjonelle endringar.
- `make validate` må køyrast etter erstattinga for å sikre at YAML framleis er gyldig.

---

## Tiltak

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 1 | Køyr `find ... -exec sed` for å erstatte U+2013 med U+002d | 159 filer | Høg | ✓ |
| 2 | Valider at ingen U+2013 finst igjen med `grep` | 1 kommando | Høg | ✓ |
| 3 | Køyr `make validate` for å sikre at YAML framleis er gyldig | CI-sjekk | Høg | ✓ |
| 4 | Gjennomgå git diff for utilsikta endringar | manuell review | Medium | ✓ |
| 5 | Legg til teiknsett-regel i CLAUDE.md | 1 seksjon | Medium | ✓ |
| 6 | Commit med melding som forklarer kvifor erstatning vart gjort | 1 commit | Høg | ✓ |

## Utført

Alle tiltak er utførte. Resultat:
- 139 filer endra (362 linjer)
- 0 gjenverande U+2013-førekomstar
- YAML-validering passerer (make domain-validate-bronze DOMAIN=samt)
- Git diff viser berre en-dash → hyphen-erstatning, ingen utilsikta endringar
- CLAUDE.md oppdatert med teiknsett-regel under "Namngjeving"
