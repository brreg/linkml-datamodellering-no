# Avhengighetstre på index.md

## Bakgrunn

Kvar skjema sin `index.md` i dokumentasjonsportalen bør vise eit avhengighetstre som syner kva andre skjema dette skjemaet importerer — både direkte og transitivt. Dette hjelper brukarar å forstå modelldependencies og kva klasser/slots som er tilgjengelege via import.

Importkjeda er allereie dokumentert i `mkdocs/docs/ap-no-arkitektur.md` (linjer 11-30), men denne er skrive for hand og må oppdaterast manuelt. Me treng ein automatisk mekanisme som:

1. Les `imports:`-seksjonen frå kvart skjema
2. Matcherer mot importkjeda i `ap-no-arkitektur.md`
3. Genererer eit kompakt avhengighetstre per skjema
4. Viser dette på `index.md` for kvart skjema

## Noverande situasjon

- Importkjeda er dokumentert statisk i `ap-no-arkitektur.md` (linjer 11-30)
- Kvar skjema importerer ein eller fleire andre skjema via `imports:`-lista
- `mkdocs/publish.sh` har allereie ein `build_dependency_graph`-funksjon (linje 174-199)
- Funksjonen viser **berre direkte importar** som flat liste (t.d. `linkml:types`, `ap-no/dcat-ap-no/dcat-ap-no`)
- Ingen **transitive** avhengigheiter vert viste (t.d. at `dcat-ap-no` importerer `common-ap-no`)

## Målbilete

Den eksisterande "Avhengigheiter"-seksjonen skal utvidas frå flat liste til eit **hierarkisk tre** som viser både direkte og transitive importar:

**Før (flat liste):**
```
## Avhengigheiter

### Importerer

linkml:types
ap-no/dcat-ap-no/dcat-ap-no
ap-no/dqv-ap-no/dqv-ap-no
```

**Etter (hierarkisk tre):**
```
## Avhengigheiter

### Importerer

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

linkml:types
    └── common-ap-no
        ├── dqv-core
        │   └── dcat-ap-no
        │       └── dqv-ap-no
        └── dcat-ap-no
```

!!! note "Leseretning"
    Diagrammet ovanfor viser avhengigheiter **frå høgre til venstre**. Dette skjemaet 
    importerer `dcat-ap-no` og `dqv-ap-no`, som igjen automatisk inkluderer alle sine 
    avhengigheiter (`common-ap-no` og `linkml:types`).

*Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*

## Tiltak

### 1. Lag `mkdocs/docs/importhierarki.md` med fullstendig importkjede

**Fil:** `mkdocs/docs/importhierarki.md`

Ny fil som erstattar importkjede-seksjonen i `ap-no-arkitektur.md` og samlar **alle** importkjeder:

**Innhald:**

1. **Introduksjon og leseretning:**
   ```markdown
   # Importhierarki
   
   Dette dokumentet viser det komplette importhierarkiet for alle skjema i repoet.
   
   ## Korleis lese diagramma
   
   **Viktig:** Diagramma må lesast **frå høgre til venstre**. 
   
   Når du importerer eit skjema vil det automatisk inkludere alle avhengigheiter det har 
   til venstre for seg i treet. 
   
   **Eksempel:**
   
   Dersom du importerer `dcat-ap-no`:
   ```
   linkml:types
       └── common-ap-no
           └── dcat-ap-no  ← du importerer dette
   ```
   
   ...så får du automatisk med deg både `common-ap-no` og `linkml:types` (alle avhengigheiter 
   til venstre).
   ```

2. **ASCII-tree-syntaks per domene:**
   - **AP-NO-hierarki** (flytta frå `ap-no-arkitektur.md` linjer 11-30)
   - **FINT-hierarki** (frå `CLAUDE.md`, detaljert)
   - **Offentlege register (oreg)** (frå `CLAUDE.md`, detaljert)
   - **SAMT-hierarki** (dersom relevant)
   - **FAIR-metadata** (dersom relevant)

3. **Lenke til `ap-no-arkitektur.md`** for AP-NO-spesifikke arkitektoniske val

**Oppdater `ap-no-arkitektur.md`:**
- Slett linjer 11-30 (importkjede-blokka)
- Erstatt med lenke: `Sjå [Importhierarki](../importhierarki.md#ap-no-hierarki) for fullstendig oversikt.`

**Legg til i `mkdocs/publish.sh`:**
- Legg `importhierarki.md` til i `nav:` under `Rettleiingar:` (i heredoc-blokka som genererer `mkdocs.yml`)

### 2. Lag Python-script for å parse importkjeda frå `importhierarki.md`

**Fil:** `src/assets/scripts/parse-dependency-tree.py`

Script skal:
- Lese `mkdocs/docs/importhierarki.md` og parse alle ASCII-tree-blokkar
- Parse ASCII-tree-strukturen til ein Python-dict med relasjonen `skjema → [importer_dette_skjemaet_direkte]`
- Returnere ein lookup-funksjon: `get_dependency_subtree(schema_name, imports_list) → tree_str`
- Handtere fleire domene-hierarki (AP-NO, FINT, oreg osv.)

**Input:** 
- `schema_name`: `samt-bu`
- `imports_list`: `["linkml:types", "ap-no/dcat-ap-no/dcat-ap-no", "ap-no/dqv-ap-no/dqv-ap-no"]`

**Output:**
```
linkml:types
    └── common-ap-no
        ├── dqv-core
        │   └── dcat-ap-no
        │       └── dqv-ap-no
        └── dcat-ap-no
```

Script skal:
1. Identifisere kva domene `samt-bu` høyrer til (ved å sjekke kva i `imports_list` som ikkje er `linkml:types`)
2. Hente rett hierarki frå `importhierarki.md` (i dette tilfellet AP-NO-hierarkiet)
3. Bygge eit subset-tre som berre viser den delen av hierarkiet som er relevant for dette skjemaet

### 3. Erstatt `build_dependency_graph`-funksjonen i `publish.sh`

**Fil:** `mkdocs/publish.sh` (linje 174-199)

Erstatt eksisterande funksjon som berre viser flat liste med ny implementasjon:

```bash
build_dependency_graph() {
    local domain="$1"
    local schema="$2"
    local schema_path="$REPO_ROOT/src/linkml/$domain/$schema/${schema}-schema.yaml"

    # Parse direkte importar frå dette skjemaet
    local imports=""
    if [ -f "$schema_path" ]; then
        imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_path" | grep -E "^  - " | sed 's/^  - //' | sed 's/-schema$//' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
    fi

    # Output
    if [ -n "$imports" ]; then
        echo "## Avhengigheiter"
        echo ""
        echo "### Importerer"
        echo ""
        echo "Dette skjemaet importerer følgjande skjema (direkte og transitivt):"
        echo ""
        echo "\`\`\`"
        # Kall Python-script for å bygge hierarkisk tre
        python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" "$schema" "$imports"
        echo "\`\`\`"
        echo ""
        echo "!!! note \"Leseretning\""
        echo "    Diagrammet ovanfor viser avhengigheiter **frå høgre til venstre**. Dette skjemaet"
        echo "    importerer dei skjemaa som står lengst til høgre, som igjen automatisk inkluderer"
        echo "    alle sine avhengigheiter lengre til venstre i treet."
        echo ""
        echo "*Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*"
        echo ""
        echo ""
    fi
}
```

**Endring:** Lenka til "fullstendig importkjede" peikar no til `importhierarki.md` i staden for `ap-no-arkitektur.md`.

### 4. Handter edge cases i Python-scriptet

- **Skjema utan imports:** Returner tom streng (vis ikkje Avhengigheiter-seksjon)
- **Skjema som berre importerer `linkml:types`:** Vis berre `linkml:types` (éin linje)
- **Skjema som importerer frå fleire domene:** Bygg separate tre per domene og slå saman
- **Manglande skjemanamn i `importhierarki.md`:** Fallback til flat liste av direkte imports (same som noverande output)

### 5. Valider output på eksisterande skjema

Køyr `make docs-publish` og sjekk at:
- **`samt-bu/index.md`** viser rett avhengighetstre (inkl. transitive deps via `dcat-ap-no` og `dqv-ap-no`)
- **`dcat-ap-no/index.md`** viser tre med `common-ap-no` og `dqv-core`
- **`common-ap-no/index.md`** viser berre `linkml:types`
- **`fint-administrasjon/index.md`** viser FINT-hierarkiet (dersom det finst)
- **Skjema som importerer frå fleire domene** (dersom det finst) viser fleire tre

Verifiser at lenka til `importhierarki.md` fungerer frå alle skjema sine `index.md`-filer.

## Avhengigheiter

Ingen. Dette er ein standalone-feature.

## Prioritert handlingsliste

- [x] 1. Lag `mkdocs/docs/importhierarki.md` med fullstendig importkjede (alle domene)
- [x] 2. Oppdater `ap-no-arkitektur.md`: slett importkjede-blokka, legg til lenke til `importhierarki.md`
- [x] 3. Legg `importhierarki.md` til i `mkdocs/publish.sh` sin nav-meny (heredoc-blokk for `mkdocs.yml`)
- [x] 4. Lag `src/assets/scripts/parse-dependency-tree.py` med parsing-logikk
- [x] 5. Erstatt `build_dependency_graph` i `mkdocs/publish.sh` (linje 174-199) til å kalle scriptet
- [x] 6. Handter edge cases i Python-scriptet (ingen imports, ukjende skjema, fallback til flat liste)
- [x] 7. Valider på eksisterande skjema (køyr `make docs-publish` og sjekk `samt-bu`, `dcat-ap-no`, `common-ap-no`, FINT)

## Utført

Alle tiltak er utførte. Implementasjonen inkluderer:

1. **Ny dokumentasjonsfil:** `mkdocs/docs/importhierarki.md` med fullstendig importkjede for AP-NO, FINT og oreg
2. **Oppdatert arkitekturdokumentasjon:** `ap-no-arkitektur.md` peikar no til `importhierarki.md`
3. **Nav-meny:** `importhierarki.md` er lagt til i MkDocs-navigasjon
4. **Python-script:** `src/assets/scripts/parse-dependency-tree.py` parsar importkjeda og byggjer hierarkisk tre
5. **Oppdatert `build_dependency_graph`:** Funksjonen kallar no Python-scriptet og viser transitive avhengigheiter
6. **Edge cases handterte:**
   - Skjema utan standard filnamn (t.d. `common/common-ap-no-schema.yaml`) vert funne via glob-mønster
   - Skjema med ulike indentering i `imports:`-lista (0 eller 2 blanke teikn) vert handterte
   - Filtrering til relevante delar av hierarkiet (berre viser dei skjemaa som faktisk vert importerte)
7. **Validert:** Køyrd `make docs-publish` og verifisert output på `samt-bu`, `dcat-ap-no`, `common-ap-no`, `fint-administrasjon`, `enhetsregisteret-bvrinn`

**Avvik frå opphavleg plan:**
- Importkjede-diagrammet i `importhierarki.md` vart justert for å reflektere den faktiske strukturen (dqv-ap-no er søsken til dcat-ap-no, ikkje barn)
- To bugfiksar i `build_dependency_graph`: glob-mønster for filsøk og regex for imports-parsing

## Notat

### Kvifor ein ny `importhierarki.md`?

`ap-no-arkitektur.md` er spesifikk for AP-NO-profilene og handlar om arkitektoniske val og avvik. Importkjeda høyrer heime i ein generell, domene-uavhengig fil som:
- Dekkjer **alle** skjema (AP-NO, FINT, oreg, SAMT, FAIR)
- Kan lenkast til frå alle skjema sine `index.md`-filer
- Er enkel å finne for brukarar som lagar domenemodeller

`CLAUDE.md` har allereie ein forenkla versjon, men denne skal vere meir detaljert og maskinlesbar (ASCII-tree-syntaks som Python-scriptet kan parse).

### Framtidige forbetringar

Dette er eit første steg. Senere kan me vurdere:
- Visuell graf (Mermaid/PlantUML) i staden for ASCII-tre
- Lenking til kvar importert skjema sin index.md
- Vise kva klasser/slots som kjem frå kvar import
- Automatisk generere `importhierarki.md` frå skjema-filene (i staden for manuell vedlikehald)
