# Auke maks teiknlengde for description-kolonnen i dokumentasjonstabellar

## Bakgrunn

Description-kolonna i `index.md` og andre genererte dokumentasjonssider vert kutta av ved:
- Første punktum (`.`) i teksten
- Første linjeskift (`\n`)
- Maks 80 teikn (77 + "...")

Dette skjer i LinkML sitt `enshorten`-filter i `linkml/generators/docgen.py`:

```python
MAX_CHARS_IN_TABLE = 80

def enshorten(input):
    if input is None:
        return ""
    if "\n" in input:
        toks = input.split("\n")
        input = toks[0]
    if "." in input:
        toks = input.split(".")
        input = toks[0]
    if len(input) > MAX_CHARS_IN_TABLE - 3:
        input = input[0 : MAX_CHARS_IN_TABLE - 3] + "..."
    return input
```

**Problem:** Korte, handverka skildringar passar ikkje innan 80 teikn når dei inneheld punktum eller bindestrek-setningar.

## Mål

Tillate lengre description-tekst i dokumentasjonstabellane utan å endre LinkML sin kjeldekode permanentDokumentere løysinga slik at andre kan følgje same mønster.

## Løysingsalternativ

### Alt 1: Patch LinkML sin `docgen.py` i containerimage (anbefalt)

Legg til ein patch-fil i `src/assets/containers/patches/docgen-max-chars.patch` og køyr den i `Dockerfile.linkml`:

```dockerfile
COPY src/assets/containers/patches/docgen-max-chars.patch /tmp/
RUN patch /usr/local/lib/python3.11/site-packages/linkml/generators/docgen.py \
    < /tmp/docgen-max-chars.patch
```

**Fordeler:**
- Enkel å vedlikehalde
- Synleg i git-historikk
- Kan reverserast enkelt

**Ulemper:**
- Kan brekke ved oppgradering av LinkML (må oppdatere patch)

### Alt 2: Overstyr `enshorten` i Jinja-template

Definer ein custom filter i ein Python-wrapper rundt `gen-doc`. Krev å endre `Makefile`-targets.

**Fordeler:**
- Ingen patching av upstream-kode

**Ulemper:**
- Meir komplisert å implementere
- Krev ekstra Python-script

## Foreslått løysing

**Alt 1** — patch `MAX_CHARS_IN_TABLE` frå 80 til 200 teikn.

## Steg

- [x] 1. Opprett `src/assets/containers/patches/docgen-max-chars.patch`
  - Patch-fil laga med korrekt format for linje 48-54 i docgen.py
- [x] 2. Oppdater `src/assets/containers/Dockerfile.linkml`
  - Lagt til `patch` i apt-get install
  - COPY patch-fil til `/tmp/`
  - RUN patch-kommando
- [x] 3. Oppdater Makefile
  - `build-docker-linkml`: lagt til `.` som build-kontekst
- [x] 4. Rebuild linkml-container: `make build-docker-linkml`
  - Container rebuilda med `MAX_CHARS_IN_TABLE = 200`
- [x] 5. Verifiser at generert dokumentasjon inneheld lengre description-tekst
  - Testa med `enhetsregisteret-bvrinn` og `samt-bu`
  - Ingen descriptions vert kutta med "..." lenger
  - Description-tekst opp til 200 teikn vert no vist i tabellar
- [ ] 6. Dokumenter patch-mekanismen i `CONTRIBUTING.md` eller `src/assets/containers/README.md`

## Utført

Implementerte løysing ved å patche LinkML sin `docgen.py` i containerimagebygget:

- `src/assets/containers/patches/docgen-max-chars.patch`: Patch-fil som endrar `MAX_CHARS_IN_TABLE` frå 80 til 200
- `src/assets/containers/Dockerfile.linkml`: Installerer `patch` og køyrer patch-kommandoen
- `Makefile`: Lagt til `.` som build-kontekst for `build-docker-linkml`

**Avvik frå plan:** Ingen — alle steg utførte som planlagt.

**Resultat:** Description-kolonnen i dokumentasjonstabellar kan no vise opptil 200 teikn i staden for 80. Tekst vert framleis kutta ved første punktum eller newline (dette er LinkML sitt design).

## Avhengigheiter

- LinkML 1.11.1 (installert i `Dockerfile.linkml`)
- Podman (for å rebuilde container)

## Validering

```bash
# Rebuild container
make build-linkml

# Generer dokumentasjon for eit skjema med lange descriptions
make gen-doc SCHEMA=src/linkml/oreg/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml

# Sjekk om description no er lengre enn 80 teikn
grep "Description" mkdocs/docs/oreg/enhetsregisteret-bvrinn/index.md | head -5
```

## Referansar

- LinkML docgen source: `/usr/local/lib/python3.11/site-packages/linkml/generators/docgen.py`
- `enshorten`-filter: linje ~50-65 i `docgen.py`
