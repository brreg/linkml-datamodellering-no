# Plan: erstatt "resolusjon"/"resolverer"/"resolvbar" med "dereferering" i IRI-sjekken

## Bakgrunn og motivasjon

`modell-analyse`-workflowen sin `iri-resolution`-jobb skriv "IRI-resolusjonssjekk"
til `GITHUB_STEP_SUMMARY`. "Resolusjonssjekk" er ikkje eit etablert norsk ord —
"resolusjon" tyder anten "vedtak" eller "oppløysing" (biletoppløysing) på norsk,
ikkje "at ein URI hentar ut ein ressurs over HTTP".

Brukaren har valt erstattingsuttrykk: **"dereferering"** (norsk substantiv for
verbet "å dereferere") — den presise Linked Data-termen for at ein IRI faktisk
gir ein ressurs når han hentast over HTTP — **etterfølgt av det engelske
uttrykket i parentes** ved hovudoverskrifter/første omtale: "IRI-dereferering
(IRI resolution)".

## Omfang

Same ordstamme ("resolusjon"/"resolverer"/"resolvbar") finst i fem filer knytt
til denne konkrete sjekken. Andre bruk av "resolv*" i repoet (avrotize sin
`dependency_resolver`, mermaid-lenkjesjekken, linkml sin import-oppløysing) er
**ikkje** i omfanget — dei gjeld andre, urelaterte konsept og har alt eigne
etablerte omgrep (t.d. "oppløysing" for linkml-import-resolusjon).

Python-identifikatorar (`KNOWN_UNRESOLVABLE_PATTERNS`, `is_known_unresolvable`)
er engelsk kode — uendra, i tråd med resten av fila sin identifikator-konvensjon.
Filnamnet `iri-resolution-report.md` og make-målet `analyse-iri-resolution`
er tekniske identifikatorar, ikkje norsk prosa — uendra.

## Steg

1. **`src/assets/scripts/makefile/check-iri-resolution.py`**
   - Docstring (linje 3-4): "Testar HTTP-resolusjon..." → "Testar IRI-dereferering
     (IRI resolution) for IRI-ane..."; "ikkje resolverer" → "ikkje let seg derefere"
   - Linje 38: "ikkje-resolvbare" → "ikkje-dereferbare"
   - Linje 45: "resolvbart" → "dereferbart"
   - Linje 161: `"# IRI-resolusjonssjekk\n"` → `"# IRI-dereferering (IRI resolution)\n"`
   - Linje 165: "ikkje-resolvbare" → "ikkje-dereferbare"
   - Linje 177: "Alle IRI-ar resolverte." → "Alle IRI-ar let seg derefere."
   - Linje 186: "IRI-ar resolverte ikkje" → "IRI-ar let seg ikkje derefere"
   - Linje 234 (referanse til `specs/done/iri-resolusjon-innhaldsforhandling.md`):
     **uendra** — arkivert filnamn, jf. DRY-unntaket for `specs/done/`

2. **`src/assets/scripts/makefile/summarise-modell-analyse.py`**
   - Regex `IRI_ALL_OK`/`IRI_FAILED` må matche den nye teksten frå steg 1
     (elles sluttar sammendrag-parsinga å fungere)
   - `CHECKS`-lista sin etikett: `"IRI-resolusjon"` → `"IRI-dereferering"`

3. **`.github/workflows/modell-analyse.yml`**
   - Linje 4 (kommentar): "IRI-resolusjon" → "IRI-dereferering (IRI resolution)"
   - Linje 137 (steg-namn): "Test IRI-resolusjon" → "Test IRI-dereferering (IRI resolution)"
   - Linje 142 (step summary-overskrift): "## IRI-resolusjonssjekk" → "## IRI-dereferering (IRI resolution)"

4. **`make/91-modell-analyse.mk`**
   - Linje 4 (kommentar): "IRI-resolusjon" → "IRI-dereferering (IRI resolution)"
   - Linje 44 (`make help`-tekst): "resolverer over HTTP(S)" → "let seg derefere over HTTP(S)"

5. **`COMMANDS.md`**
   - Linje 300: "ikkje resolverer" → "ikkje let seg derefere"
   - Linje 312: "HTTP-resolusjon" → "IRI-dereferering (IRI resolution)"; "ikkje-resolvbare"
     → "ikkje-dereferbare"; "utelatne frå resolusjonssjekken" → "utelatne frå testen"

6. **Verifiser** — køyr `make analyse-iri-resolution > /tmp/iri-report.md` og
   `make analyse-sammendrag` (etter at rapportfilene finst) for å stadfeste at
   regex-endringane i steg 2 framleis parsar rapporten korrekt.

## Handlingsliste

- [x] Steg 1: `check-iri-resolution.py`
- [x] Steg 2: `summarise-modell-analyse.py`
- [x] Steg 3: `modell-analyse.yml`
- [x] Steg 4: `91-modell-analyse.mk`
- [x] Steg 5: `COMMANDS.md`
- [x] Steg 6: verifiser med `make analyse-iri-resolution` + `make analyse-sammendrag`

## Utført

Alle seks steg gjennomførte. Verifisert med `make analyse-iri-resolution DOMAIN=fair`
(ny overskrift "# IRI-dereferering (IRI resolution)" og teksten "let seg ikkje
derefere" vert rett generert) og deretter `summarise-modell-analyse.py` mot
den genererte rapporten (parsa "1"/"6" korrekt for den nye "IRI-dereferering"-
etiketten, dvs. dei oppdaterte regexane matchar den nye teksten).
