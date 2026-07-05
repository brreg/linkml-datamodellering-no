---
name: fix-index-md-table-separator
description: Fiks tre feil i index.md-generering — ekstra tabellelement etter Subsets og Generated artifacts, og manglande kontaktinfo
metadata:
  type: bugfix
---

# Fiks index.md-genereringsfeil

## Bakgrunn

I publisert index.md for `samt-bu` (og truleg andre skjema) er det tre feil:

1. **Subsets-tabellen** har fått ei ekstra rad med innholdet `---` på slutten
2. **Generated artifacts-tabellen** har fått ei ekstra rad med innholdet `---` på slutten
3. **Kontakt-seksjonen** viser berre "Support: GitHub Issues" (men dette er faktisk ikkje reproducerbart i gjeldande `mkdocs/docs/samt/samt-bu/index.md` — kan vere eit timing-problem eller brukar såg gammal versjon)

### Rotsak

MkDocs sin Markdown-parser tolkar `---` som ein ekstra tabellelement når det **manglar tom linje før** `---`-separatoren.

Eksempel frå `mkdocs/docs/samt/samt-bu/index.md`:

```markdown
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |
---                                    ← Manglar tom linje før — vert tolka som tabellelement

## Generated artifacts
```

Resultatet er at MkDocs rendrer ein ekstra rad med berre `---` i tabellen.

### Kvifor skjer dette?

I `mkdocs/publish.sh`:

- Linje 487-488: Embeddar `## Classes` og resten frå gen-doc `index.md` (inkluderer `## Subsets`)
- Linje 531-537: Skriv `echo "---"` rett etter embedding av klasseliste → manglar `echo ""` før `echo "---"`
- Linje 567-571: Skriv `echo "---"` rett etter artefakttabellen → same problem

## Løysing

Legg til `echo ""` (tom linje) **før** kvar `echo "---"` som kjem direkte etter ein tabell.

## Implementasjon

### 1. Fiks Subsets-tabellseparator (linje 531)

**Før:**
```bash
if $has_artifact; then
    echo "---"
    echo ""
    echo "## Generated artifacts"
```

**Etter:**
```bash
if $has_artifact; then
    echo ""
    echo "---"
    echo ""
    echo "## Generated artifacts"
```

### 2. Fiks Generated artifacts-tabellseparator (linje 567)

**Før:**
```bash
    fi
else
    echo "---"
    echo ""
    echo "## Valideringsresultat"
```

**Etter:**
```bash
    fi
else
    echo ""
    echo "---"
    echo ""
    echo "## Valideringsresultat"
```

### 3. Fiks manglande tom linje før validering med resultat (linje 562)

**Før:**
```bash
if [ -f "$validation_json" ]; then
    echo "---"
    echo ""
    python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
```

**Etter:**
```bash
if [ -f "$validation_json" ]; then
    echo ""
    echo "---"
    echo ""
    python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
```

### 4. Fiks manglande tom linje før versjonslog (linje 576)

**Før:**
```bash
if [ -f "$changelog_src" ]; then
    echo "---"
    echo ""
    echo "## Versjonslog"
```

**Etter:**
```bash
if [ -f "$changelog_src" ]; then
    echo ""
    echo "---"
    echo ""
    echo "## Versjonslog"
```

### 5. Fiks manglande tom linje før kontakt (linje 590)

**Før:**
```bash
fi

# Steg 5: Kontaktinformasjon
# Hent utgjevar frå metadata (gendoc_index er allereie lest)
echo "---"
echo ""
echo "## Kontakt"
```

**Etter:**
```bash
fi

# Steg 5: Kontaktinformasjon
# Hent utgjevar frå metadata (gendoc_index er allereie lest)
echo ""
echo "---"
echo ""
echo "## Kontakt"
```

## Teststrategi

1. Køyr `make docs-publish`
2. Sjekk `mkdocs/docs/samt/samt-bu/index.md`:
   - Verifiser at `---` på linje 339 (etter Subsets) har tom linje før
   - Verifiser at `---` på linje 357 (etter Generated artifacts) har tom linje før
3. Bygg og serve mkdocs lokalt: `cd mkdocs && mkdocs serve`
4. Opne `http://localhost:8000/samt/samt-bu/` i nettlesar
5. Verifiser at Subsets-tabellen **ikkje** har ein ekstra rad med `---`
6. Verifiser at Generated artifacts-tabellen **ikkje** har ein ekstra rad med `---`

## Handlingsliste

- [✓] 1. Legg til `echo ""` før `echo "---"` på linje 531
- [✓] 2. Legg til `echo ""` før `echo "---"` på linje 567
- [✓] 3. Legg til `echo ""` før `echo "---"` på linje 562
- [✓] 4. Legg til `echo ""` før `echo "---"` på linje 576
- [✓] 5. Legg til `echo ""` før `echo "---"` på linje 590
- [✓] 6. Test lokalt med `make docs-publish && cd mkdocs && mkdocs serve`

## Utført

Alle fem endringar vart implementerte i `mkdocs/publish.sh`:

1. Linje 531: Lagt til `echo ""` før `echo "---"` (før Generated artifacts-seksjonen)
2. Linje 564 og 569: Lagt til `echo ""` før `echo "---"` (før Valideringsresultat-seksjonen — både for json-varianten og fallback-varianten)
3. Linje 580: Lagt til `echo ""` før `echo "---"` (før Versjonslog-seksjonen)
4. Linje 595: Lagt til `echo ""` før `echo "---"` (før Kontakt-seksjonen)

**Resultat:**
- Subsets-tabellen har **ikkje lenger** ein ekstra rad med `---` på slutten
- Generated artifacts-tabellen har **ikkje lenger** ein ekstra rad med `---` på slutten
- Alle seksjons-separatorar har no korrekt Markdown-formatering (tom linje før `---`)

**Testat:**
- `mkdocs/docs/samt/samt-bu/index.md` har tom linje før alle `---` (linje 339, 358, osv.)
- MkDocs rendrer no tabellane korrekt utan ekstra element
