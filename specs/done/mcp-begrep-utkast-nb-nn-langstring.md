# Generering av nb og nn for alle LangString-slots i mcp-linkml-begrep-utkast

## Bakgrunn

`mcp-linkml-begrep-utkast` genererer i dag YAML-blokkar for SKOS-AP-NO Begrep-instansar
der brukaren kan velje å spesifisere bokmål (`nb`), nynorsk (`nn`) og/eller engelsk (`en`)
for fleire felt. Men for slots med datatype `LangString` (t.d. `anbefalt_term`, `merknad`,
`eksempel`) skal det generere både `nb` og `nn`-varianten automatisk dersom brukaren
ikkje har oppgjeve nynorsk-teksten eksplisitt.

**Problem:** I dag genereres berre dei språka brukaren oppgjev. Dersom brukaren ikkje
spesifiserer `merknad`-tekst på nynorsk, vert det ikkje generert nokon `nn`-variant for
`merknad`-sloten — sjølv om denne sloten har `range: LangString` og dermed skal ha
fleirspråkleg innhald.

**LangString-slots i SKOS-AP-NO:**

Følgjande slots i `skos-ap-no-schema.yaml` og `common-ap-no-schema.yaml` har
`range: LangString` og må genererast med både `nb` og `nn`:

| Slot | Definert i klasse | Multivalued | Obligatorisk/Anbefalt/Valgfri | slot_uri |
|---|---|---|---|---|
| `anbefalt_term` | `Begrep` | Ja | Obligatorisk | `skos:prefLabel` |
| `definisjon` | `Begrep` | Ja | Anbefalt | `skos:definition` |
| `merknad` | `Begrep` | Ja | Anbefalt | `skos:scopeNote` |
| `tillate_term` | `Begrep` | Ja | Anbefalt | `skos:altLabel` |
| `eksempel` | `Begrep` | Ja | Valgfri | `skos:example` |
| `forkasta_term` | `Begrep` | Ja | Valgfri | `skos:hiddenLabel` |
| `verdiomrade` | `Begrep` | Ja | Valgfri | `skosno:valueRange` |
| `tekst` | `Definisjon` | Nei | Obligatorisk | `rdf:value` |
| `kjelde_tekst` | `Definisjon` | Ja | Valgfri | `dct:bibliographicCitation` |

**Forventet oppførsel:**
- Alle `LangString`-slots skal genererast med **både `nb` og `nn`** i YAML-output
- Dersom brukaren ikkje har oppgjeve `nn`-tekst, bruk `nb`-teksten som fallback (slik
  det allereie vert gjort for `definisjon` i dag)
- `en` er valfri og skal berre inkluderast om brukaren har oppgjeve engelsk tekst
- `mcp-linkml-begrep-utkast` genererer primært `Begrep`- og `Definisjon`-objekt, så
  fokuset er på desse slots:
  - `anbefalt_term` (allereie delvis implementert, må utvidas)
  - `definisjon` (allereie implementert korrekt via `definisjon_nb`/`definisjon_nn`)
  - `merknad` (array av LangString — må implementerast)
  - `tillate_term` (array av LangString — må implementerast)
  - `eksempel` (array av LangString — må implementerast)
  - `forkasta_term` (array av LangString — må implementerast)
  - `verdiomrade` (array av LangString — må implementerast)
  - `tekst` (single LangString i `Definisjon` — allereie implementert korrekt)
  - `kjelde_tekst` (array av LangString i `Definisjon` — må implementerast)

## Mål

Oppdatere `generator.py` i `src/mcp-linkml-begrep-utkast/` slik at:

1. Alle `LangString`-verdiar (inkl. arrayfelt som `merknad` og `eksempel`) genereres
   med både bokmål og nynorsk
2. Dersom brukaren ikkje har oppgjeve nynorsk-tekst (`_nn`-parameteren er tom), bruk
   bokmål-teksten som fallback
3. Engelsk (`en`) inkluderast berre når eksplisitt oppgjeve av brukaren
4. YAML-output forblir bakoverkompatibel — eksisterande profiler og klientar skal
   fungere utan endring

## Nummererte steg

### 1. Analyser status quo i `generator.py`

Undersøk korleis `opprett_begrep()` i dag handterer `merknad` og `eksempel`:

- Kva datatype er dei (liste av strenger eller LangString-objekt)?
- Vert dei i dag serialiserte som reine strenger eller som `{språkkode: tekst}`-objekt?
- Korleis fungerer `anbefalt_term`-generering i dag (linje 82-87)?

### 2. Utvid `opprett_begrep()`-parametrar med nynorsk-støtte

Legg til parametrar for nynorsk-versjonar av alle LangString-array-slots:

```python
def opprett_begrep(
    profile: dict,
    slug: str,
    anbefalt_term_nb: str,
    definisjon_nb: str,
    fagomrade_uri: str,
    *,
    # ... eksisterande ...
    # LangString-slots — array-typar
    merknad_nb: list | None = None,
    merknad_nn: list | None = None,
    merknad_en: list | None = None,
    tillate_term_nb: list | None = None,
    tillate_term_nn: list | None = None,
    tillate_term_en: list | None = None,
    eksempel_nb: list | None = None,
    eksempel_nn: list | None = None,
    eksempel_en: list | None = None,
    forkasta_term_nb: list | None = None,
    forkasta_term_nn: list | None = None,
    forkasta_term_en: list | None = None,
    verdiomrade_nb: list | None = None,
    verdiomrade_nn: list | None = None,
    verdiomrade_en: list | None = None,
    kjelde_tekst_nb: list | None = None,
    kjelde_tekst_nn: list | None = None,
    kjelde_tekst_en: list | None = None,
    # ... resten ...
) -> str:
```

Fjern `merknad` og `eksempel` som enkle `list`-parametrar og erstatt med språkdelte
listar (`merknad_nb`, `merknad_nn`, `merknad_en` osv.). Legg til språkdelte parametrar
for `tillate_term`, `forkasta_term`, `verdiomrade` og `kjelde_tekst` også.

### 3. Implementer LangString-fallback-logikk

Lag ein hjelpefunksjon for å handtere LangString-array-generering:

```python
def _build_langstring_array(nb_texts: list, nn_texts: list, en_texts: list) -> list:
    """
    Genererer LangString-objekt for kvar tekst i nb-lista, med nn-fallback
    dersom nn_texts manglar eller er kortare enn nb_texts.
    """
    result = []
    for i, nb_text in enumerate(nb_texts):
        nn_text = nn_texts[i] if i < len(nn_texts) and nn_texts[i] else nb_text
        lang_obj = {"nb": nb_text, "nn": nn_text}
        if i < len(en_texts) and en_texts[i]:
            lang_obj["en"] = en_texts[i]
        result.append(lang_obj)
    return result
```

### 4. Bruk hjelpefunksjonen i `opprett_begrep()`

Erstatt direkte tildeling av alle LangString-array-slots med kall til
`_build_langstring_array()`:

```python
if merknad_nb:
    begrep_dict["merknad"] = _build_langstring_array(
        merknad_nb or [],
        merknad_nn or [],
        merknad_en or []
    )

if tillate_term_nb:
    begrep_dict["tillate_term"] = _build_langstring_array(
        tillate_term_nb or [],
        tillate_term_nn or [],
        tillate_term_en or []
    )

if eksempel_nb:
    begrep_dict["eksempel"] = _build_langstring_array(
        eksempel_nb or [],
        eksempel_nn or [],
        eksempel_en or []
    )

if forkasta_term_nb:
    begrep_dict["forkasta_term"] = _build_langstring_array(
        forkasta_term_nb or [],
        forkasta_term_nn or [],
        forkasta_term_en or []
    )

if verdiomrade_nb:
    begrep_dict["verdiomrade"] = _build_langstring_array(
        verdiomrade_nb or [],
        verdiomrade_nn or [],
        verdiomrade_en or []
    )
```

For `kjelde_tekst` (som høyrer til `Definisjon`-objektet, ikkje `Begrep`), legg til
tilsvarande logikk i definisjonsblokka nedanfor `definisjoner = []`.

### 5. Oppdater `anbefalt_term`-generering for konsistens

Sjekk om `anbefalt_term` i dag vert serialisert som rein streng-array eller
LangString-array. Dersom den skal vere LangString (sjekk skjema), oppdater til
same mønster som `merknad`/`eksempel`.

### 6. Oppdater `server.py` med nye parametrar

I `TOOL_OPPRETT_BEGREP` (linje 35+), erstatt `merknad` og `eksempel` med språkdelte
parametrar, og legg til parametrar for dei andre LangString-slottane:

```json
"merknad_nb": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Merknadstekstar på bokmål (valfri).",
    "default": [],
},
"merknad_nn": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Merknadstekstar på nynorsk (valfri, fallback til nb).",
    "default": [],
},
"merknad_en": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Merknadstekstar på engelsk (valfri).",
    "default": [],
},
"tillate_term_nb": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Tillaten alternativ term på bokmål (valfri).",
    "default": [],
},
"tillate_term_nn": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Tillaten alternativ term på nynorsk (valfri, fallback til nb).",
    "default": [],
},
"tillate_term_en": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Tillaten alternativ term på engelsk (valfri).",
    "default": [],
},
"eksempel_nb": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Eksempelstrengjer på bokmål (valfri).",
    "default": [],
},
"eksempel_nn": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Eksempelstrengjer på nynorsk (valfri, fallback til nb).",
    "default": [],
},
"eksempel_en": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Eksempelstrengjer på engelsk (valfri).",
    "default": [],
},
"forkasta_term_nb": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Forkasta term på bokmål (valfri).",
    "default": [],
},
"forkasta_term_nn": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Forkasta term på nynorsk (valfri, fallback til nb).",
    "default": [],
},
"forkasta_term_en": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Forkasta term på engelsk (valfri).",
    "default": [],
},
"verdiomrade_nb": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Verdiområde på bokmål (valfri).",
    "default": [],
},
"verdiomrade_nn": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Verdiområde på nynorsk (valfri, fallback til nb).",
    "default": [],
},
"verdiomrade_en": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Verdiområde på engelsk (valfri).",
    "default": [],
},
"kjelde_tekst_nb": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Bibliografisk kjelde på bokmål (valfri).",
    "default": [],
},
"kjelde_tekst_nn": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Bibliografisk kjelde på nynorsk (valfri, fallback til nb).",
    "default": [],
},
"kjelde_tekst_en": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Bibliografisk kjelde på engelsk (valfri).",
    "default": [],
},
```

Oppdater `_handle_opprett_begrep()` (linje 261+) til å sende alle nye parametrar til
`opprett_begrep()` med `arguments.get("<param>") or []` for kvar.

### 7. Oppdater README.md

Erstatt tabellen under «Valfrie (kan setjast av profilen)» med dei nye parametrane:

```markdown
| `merknad_nb` | string[] | Merknadstekstar på bokmål |
| `merknad_nn` | string[] | Merknadstekstar på nynorsk (fallback: nb) |
| `merknad_en` | string[] | Merknadstekstar på engelsk |
| `tillate_term_nb` | string[] | Tillaten alternativ term på bokmål |
| `tillate_term_nn` | string[] | Tillaten alternativ term på nynorsk (fallback: nb) |
| `tillate_term_en` | string[] | Tillaten alternativ term på engelsk |
| `eksempel_nb` | string[] | Eksempelstrengjer på bokmål |
| `eksempel_nn` | string[] | Eksempelstrengjer på nynorsk (fallback: nb) |
| `eksempel_en` | string[] | Eksempelstrengjer på engelsk |
| `forkasta_term_nb` | string[] | Forkasta term på bokmål |
| `forkasta_term_nn` | string[] | Forkasta term på nynorsk (fallback: nb) |
| `forkasta_term_en` | string[] | Forkasta term på engelsk |
| `verdiomrade_nb` | string[] | Verdiområde på bokmål |
| `verdiomrade_nn` | string[] | Verdiområde på nynorsk (fallback: nb) |
| `verdiomrade_en` | string[] | Verdiområde på engelsk |
| `kjelde_tekst_nb` | string[] | Bibliografisk kjelde på bokmål |
| `kjelde_tekst_nn` | string[] | Bibliografisk kjelde på nynorsk (fallback: nb) |
| `kjelde_tekst_en` | string[] | Bibliografisk kjelde på engelsk |
```

Oppdater eksempelblokka (linje 22-40) med nye parameternamn.

Legg til ein seksjon «LangString-generering» som forklarar at alle LangString-slots
genereres med både `nb` og `nn`, med `nb`-tekst som fallback dersom `nn` manglar.

### 8. Test lokalt

Bygg containeren og test generering:

```bash
make mcp-begrep-build
```

Lag testinput med fleire LangString-slots:
- `merknad_nb` men utan `merknad_nn` → sjekk at `nn` får fallback til `nb`-teksten
- `tillate_term_nb` og `tillate_term_nn` → sjekk at begge språk vert genererte
- `eksempel_nb`, `forkasta_term_nb`, `verdiomrade_nb` → sjekk fallback-logikk for alle

Verifiser at YAML-outputen inneheld LangString-objekt på forma:

```yaml
merknad:
  - nb: "Merknad på bokmål"
    nn: "Merknad på bokmål"  # fallback
  - nb: "Andre merknad"
    nn: "Andre merknad"
```

### 9. Oppdater dokumentasjon i `specs/begrep-modellering.md`

Dersom specen inneheld eksempelkall eller forventet output, oppdater desse slik at
dei reflekterer den nye nb+nn-oppførselen.

## Handlingsliste

- [x] Steg 1: Analyser status quo i `generator.py`
- [x] Steg 2: Utvid parametrar med språkdelte parametrar for alle LangString-slots
- [x] Steg 3: Implementer `_build_langstring_array()` hjelpefunksjon
- [x] Steg 4: Bruk hjelpefunksjonen for alle LangString-array-slots i `opprett_begrep()`
- [x] Steg 5: Oppdater `anbefalt_term`-generering for konsistens
- [x] Steg 6: Oppdater `server.py` med alle nye parametrar in inputSchema og `_handle_opprett_begrep()`
- [x] Steg 7: Oppdater README.md med komplette parametertabell, eksempel og LangString-seksjon
- [x] Steg 8: Test lokalt med alle LangString-slots og fallback-logikk
- [x] Steg 9: Ikkje nødvendig — `specs/done/begrep-modellering.md` er arkivert

## Utført

Alle LangString-slots i `mcp-linkml-begrep-utkast` genererer no både norsk bokmål (`nb`)
og norsk nynorsk (`nn`) automatisk, med bokmål som fallback for nynorsk dersom ikkje
oppgjeve. Engelsk (`en`) inkluderast berre når eksplisitt oppgjeve.

**Endringar:**

1. **`generator.py`**:
   - Ny hjelpefunksjon `_build_langstring_array()` for å generere LangString-objekt
     med `nb`/`nn`-fallback
   - Oppdaterte parametrar: `merknad_nb/nn/en`, `tillate_term_nb/nn/en`,
     `eksempel_nb/nn/en`, `forkasta_term_nb/nn/en`, `verdiomrade_nb/nn/en`,
     `kjelde_tekst_nb/nn/en`
   - `anbefalt_term` genereres no som LangString-objekt (tidlegare: streng-array)
   - Alle LangString-array-slots brukar `_build_langstring_array()` for konsistent
     nb+nn-generering

2. **`server.py`**:
   - Oppdatert `TOOL_OPPRETT_BEGREP` inputSchema med alle nye språkdelte parametrar
   - `_handle_opprett_begrep()` sender alle nye parametrar til `opprett_begrep()`

3. **`README.md`**:
   - Ny «LangString-generering»-seksjon som forklarar nb+nn-fallback-logikken
   - Oppdatert parametertabell med alle språkdelte parametrar
   - Oppdatert eksempel-YAML for å vise LangString-objektstruktur
   - Oppdatert «NB! Etter generering»-seksjon

**Testresultat:**

Lokal test med `generator.py` direkte viser korrekt generering:
- `anbefalt_term`: `{nb: "testbegrep", nn: "testbegrep"}` (fallback)
- `merknad`: `{nb: "...", nn: "..."}` (fallback)
- `tillate_term`: `{nb: "alternativ term", nn: "alternativ omgrep"}` (begge oppgjeve)
- `eksempel`: to element med nb+nn-fallback
- `forkasta_term`, `verdiomrade`, `kjelde_tekst`: fungerer som forventa
