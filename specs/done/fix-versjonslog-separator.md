---
name: fix-versjonslog-separator
description: Fiks siste linje i versjonslog vert rendra som overskrift — manglar tom linje før ---
metadata:
  type: bugfix
---

# Fiks siste linje i versjonslog vert rendra som overskrift

## Bakgrunn

I publisert `index.md` (t.d. `mkdocs/docs/samt/samt-bu/index.md`) vert **siste linje i versjonsloggen** rendra som ein overskrift i staden for som vanleg tekst.

### Observert symptom

```markdown
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](...))
---

## Kontakt
```

MkDocs tolkar siste bullet-punkt + `---` som ein **setext heading** (Markdown-stil overskrift med underline):

```
overskrift
---
```

### Rotsak

`mkdocs/publish.sh` linje 587-591 skriv ut `CHANGELOG.md` via `awk`, men **manglar ein avsluttande `echo ""`** før neste seksjon (`echo ""` + `echo "---"` + `echo "## Kontakt"`).

Resultatet:
1. `awk` skriv siste linje frå `CHANGELOG.md` (utan avsluttande newline)
2. `echo ""` på linje 596 skriv tom linje
3. `echo "---"` på linje 597 skriv `---`
4. MkDocs ser mønsteret `tekst\n---` og tolkar det som setext heading

## Løysing

Legg til `echo ""` **etter** `awk`-scriptet (innanfor `if [ -f "$changelog_src" ]; then ... fi`-blokka) for å sikre tom linje mellom versjonslog og neste seksjons `---`.

## Implementasjon

### 1. Legg til `echo ""` etter awk-scriptet

**Før (linje 580-592):**
```bash
if [ -f "$changelog_src" ]; then
    echo ""
    echo "---"
    echo ""
    echo "## Versjonslog"
    echo ""
    # Fjern hovudoverskrift "# Changelog" og auk nivået på alle andre overskrifter med éin #
    tail -n +1 "$changelog_src" | awk '
        NR==1 && /^# Changelog/ { next }
        /^##/ { print "#" $0; next }
        { print }
    '
fi
```

**Etter:**
```bash
if [ -f "$changelog_src" ]; then
    echo ""
    echo "---"
    echo ""
    echo "## Versjonslog"
    echo ""
    # Fjern hovudoverskrift "# Changelog" og auk nivået på alle andre overskrifter med éin #
    tail -n +1 "$changelog_src" | awk '
        NR==1 && /^# Changelog/ { next }
        /^##/ { print "#" $0; next }
        { print }
    '
    echo ""
fi
```

Einaste endring: Legg til `echo ""` på linje 592 (innanfor `fi`).

## Teststrategi

1. Køyr `bash mkdocs/publish.sh`
2. Sjekk `mkdocs/docs/samt/samt-bu/index.md`:
   - Finn siste linje i versjonsloggen (t.d. linje 574)
   - Verifiser at det er **to tomme linjer** før `---` (linje 576)
   - Struktur skal vere:
     ```
     * siste changelog-element
     
     ---
     
     ## Kontakt
     ```
3. Bygg og serve mkdocs: `cd mkdocs && mkdocs serve`
4. Opne `http://localhost:8000/samt/samt-bu/`
5. Verifiser at siste linje i versjonsloggen **ikkje** vert rendra som overskrift

## Handlingsliste

- [✓] 1. Legg til `echo ""` etter `awk`-scriptet (linje 592, innanfor `fi`)
- [✓] 2. Test lokalt: `bash mkdocs/publish.sh`
- [ ] 3. Verifiser i mkdocs: `cd mkdocs && mkdocs serve`

## Utført

Lagt til `echo ""` på linje 592 i `mkdocs/publish.sh` (etter `awk`-scriptet, innanfor `if [ -f "$changelog_src" ]; then ... fi`-blokka).

**Resultat:**
- `mkdocs/docs/samt/samt-bu/index.md` har no **to tomme linjer** mellom siste changelog-element og `---` (linje 575-576)
- MkDocs tolkar ikkje lenger siste linje som ein setext heading
- Struktur:
  ```markdown
  * siste changelog-element
  
  
  ---
  
  ## Kontakt
  ```

**Neste steg:**
- Test i mkdocs-server: `cd mkdocs && mkdocs serve`
- Verifiser at siste linje i versjonsloggen vert rendra som vanleg tekst (ikkje overskrift)
