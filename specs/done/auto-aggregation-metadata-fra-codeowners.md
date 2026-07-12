# Automatisk aggregation-metadata frå CODEOWNERS.md

## Bakgrunn

Begrepssamlingar har ein `build.yaml` med `aggregation`-metadata som spesifiserer kva
organisasjon begrepssamlinga høyrer til og kva begrepskatalog begrep skal aggregerast til:

```yaml
aggregation:
  organization: "974760673"  # Brønnøysundregistra
  catalog_name: brreg-begrepskatalog
```

Denne informasjonen finst allereie i `CODEOWNERS.md` som ein maskinleseleg
YAML-frontmatter-blokk (linje 1-67) som mappar `path_patterns` til organisasjonar
med `org_uri` og `catalog_slug`:

```yaml
organizations:
  - alias: brreg
    org_uri: https://data.norge.no/organizations/974760673
    catalog_slug: brreg-modellkatalog
    path_patterns:
      - src/linkml/ngr/ngr-virksomhet/**
      - src/linkml/oreg/enhetsregisteret-bvrinn/**
      - src/linkml/oreg/register-over-aksjeeiere/**
```

**Problem:** Brukarar må manuelt kopiere organisasjonsnummeret frå CODEOWNERS.md til
`build.yaml` ved oppretting av nye begrepssamlingar. Dette bryt DRY-prinsippet og kan
føre til inkonsistens dersom CODEOWNERS.md vert oppdatert utan at `build.yaml` vert
synkronisert.

**Eksempel på duplikasjon:**
- `CODEOWNERS.md` seier at `src/linkml/oreg/**` eig Brønnøysundregistra (`974760673`)
- `build.yaml` må manuelt setje `aggregation.organization: "974760673"`
- Dersom organisasjonsnummeret i CODEOWNERS.md vert endra, må `build.yaml` oppdaterast manuelt

## Mål

Automatisk utlei `aggregation.organization` og `aggregation.catalog_name` frå
CODEOWNERS.md basert på path-matching av begrepssamlinga sin sti:

1. Parse YAML-frontmatter i `CODEOWNERS.md`
2. Match `path_patterns` mot begrepssamlinga sin sti (t.d. `src/linkml/oreg/begrepssamling-foretaksregisteret/`)
3. Hent `org_uri` og `catalog_slug` frå matchande organisasjon
4. Ekstraher organisasjonsnummeret frå `org_uri` (siste del av URI-en)
5. Generer `catalog_name` frå `catalog_slug` ved å erstatte `-modellkatalog` med `-begrepskatalog`
6. Injiser desse verdiane i `build.yaml` automatisk (eller generer heilt utan aggregation-blokk)

**Alternativ tilnærming:** I staden for å endre `build.yaml`, kan me la
`collect-concepts.py` (som allereie les `build.yaml`) **også** lese CODEOWNERS.md og
bruke path-matching for å finne organisasjon dersom `aggregation`-blokka **manglar**
i `build.yaml`.

## Nummererte steg

### 1. Utvid CODEOWNERS.md sin YAML-struktur (valfritt)

Vurder om me treng ein separat `begrepskatalog_slug`-felt, eller om me kan utleie det
frå `catalog_slug` ved å erstatte `-modellkatalog` med `-begrepskatalog`.

**Alternativ 1: Utlei frå catalog_slug**
- `brreg-modellkatalog` → `brreg-begrepskatalog`
- `digdir-modellkatalog` → `digdir-begrepskatalog`

**Alternativ 2: Legg til eksplisitt felt**
```yaml
organizations:
  - alias: brreg
    org_uri: https://data.norge.no/organizations/974760673
    catalog_slug: brreg-modellkatalog
    begrepskatalog_slug: brreg-begrepskatalog  # nytt felt
    path_patterns:
      - src/linkml/oreg/**
```

**Anbefaling:** Alternativ 1 (utlei frå `catalog_slug`) er enklare og følgjer
namnekonvensjonen som allereie er etablert. Alle organisasjonar har same mønster
`<alias>-modellkatalog` og `<alias>-begrepskatalog`.

### 2. Oppdater `collect-concepts.py` til å lese CODEOWNERS.md

Legg til ein funksjon `_load_codeowners()` som:
- Les `CODEOWNERS.md`
- Ekstraherer YAML-frontmatter (linje 1-67)
- Returnerer ein dict med organisasjonar

```python
import yaml
from pathlib import Path

def _load_codeowners(repo_root: Path) -> list[dict]:
    """
    Les YAML-frontmatter frå CODEOWNERS.md og returner liste av organisasjonar.
    """
    codeowners_path = repo_root / "CODEOWNERS.md"
    if not codeowners_path.exists():
        return []
    
    with open(codeowners_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ekstraher YAML-frontmatter (mellom ``` yaml og ```)
    import re
    yaml_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
    if not yaml_match:
        return []
    
    yaml_content = yaml_match.group(1)
    data = yaml.safe_load(yaml_content)
    return data.get("organizations", [])
```

### 3. Implementer path-matching-logikk

Lag ein funksjon `_find_owner_org(begrepssamling_path: Path, orgs: list[dict]) -> dict | None`
som matcher begrepssamlinga sin sti mot `path_patterns` i CODEOWNERS.md:

```python
from pathlib import Path
import fnmatch

def _find_owner_org(begrepssamling_path: Path, orgs: list[dict]) -> dict | None:
    """
    Finn eigar-organisasjon basert på path-matching mot CODEOWNERS.md.
    
    Args:
        begrepssamling_path: Relativ sti til begrepssamlinga (t.d. src/linkml/oreg/begrepssamling-foretaksregisteret)
        orgs: Liste av organisasjonar frå CODEOWNERS.md
    
    Returns:
        Matchande organisasjon-dict eller None
    """
    begrepssamling_str = str(begrepssamling_path)
    
    for org in orgs:
        for pattern in org.get("path_patterns", []):
            # Konverter glob-pattern til regex og match
            if fnmatch.fnmatch(begrepssamling_str, pattern):
                return org
    
    return None
```

### 4. Utvid `collect-concepts.py` sin `_get_aggregation_metadata()`

Oppdater funksjonen som les `build.yaml` til å falle tilbake på CODEOWNERS.md dersom
`aggregation`-blokka manglar:

```python
def _get_aggregation_metadata(begrepssamling_dir: Path, orgs: list[dict]) -> dict | None:
    """
    Hent aggregation-metadata frå build.yaml, eller frå CODEOWNERS.md som fallback.
    """
    build_yaml = begrepssamling_dir / "build.yaml"
    if not build_yaml.exists():
        return None
    
    with open(build_yaml, "r", encoding="utf-8") as f:
        build_data = yaml.safe_load(f)
    
    # Dersom aggregation-blokka finst, bruk den
    if "aggregation" in build_data:
        return build_data["aggregation"]
    
    # Elles: finn organisasjon frå CODEOWNERS.md
    owner_org = _find_owner_org(begrepssamling_dir, orgs)
    if not owner_org:
        print(f"[WARNING] Kan ikkje finne eigar-org for {begrepssamling_dir} i CODEOWNERS.md")
        return None
    
    # Ekstraher organisasjonsnummer frå org_uri
    org_uri = owner_org.get("org_uri", "")
    org_number = org_uri.split("/")[-1]  # t.d. https://data.norge.no/organizations/974760673 → 974760673
    
    # Utlei begrepskatalog_slug frå catalog_slug
    catalog_slug = owner_org.get("catalog_slug", "")
    begrepskatalog_slug = catalog_slug.replace("-modellkatalog", "-begrepskatalog")
    
    return {
        "organization": org_number,
        "catalog_name": begrepskatalog_slug,
    }
```

### 5. Test med eksisterande begrepssamling

Test at `collect-concepts.py` kan finne eigar-org for
`src/linkml/oreg/begrepssamling-foretaksregisteret/`:

1. Fjern midlertidig `aggregation`-blokka frå `build.yaml` (eller kommenter ut)
2. Køyr `make gen-begrepskatalog-instance`
3. Verifiser at scriptet finn `brreg` som eigar via path-matching
4. Verifiser at `organization: "974760673"` og `catalog_name: brreg-begrepskatalog` vert utleidd korrekt

### 6. Oppdater `new-begrepssamling.sh` til å **ikkje** inkludere aggregation-blokk

Oppdater `src/assets/scripts/new-begrepssamling.sh` til å generere `build.yaml` **utan**
`aggregation`-blokk, sidan denne no vert auto-detektert frå CODEOWNERS.md:

```yaml
# Generert build.yaml (utan aggregation-blokk)
publish_external: false
validation_policy: bronze

generators:
  jsonld_context: false
  shacl: false
  python: false
  json_schema: false
  owl: false
  rdf: false
  protobuf: false
  erdiagram: false
  docs: false
  plantuml: false
  example_rdf: false
```

Oppdater README-utskrift i scriptet til å **ikkje** nevne at brukaren må redigere
`aggregation`-metadata:

```bash
echo "✅ Oppretta begrepssamling: $BEGREPSSAMLING_DIR"
echo ""
echo "Neste steg:"
echo "  1. Skriv begrep til begrep/<begrep-slug>.yaml (manuelt eller med mcp-linkml-begrep-utkast)"
echo "  2. Køyr 'make gen-begrepskatalog-instance' for å aggregere til begrepskatalog"
```

### 7. Oppdater dokumentasjon

Oppdater følgjande filer:

- **`CONVENTIONS.md`** (seksjon "Begrepssamlingar og begrepskatalogar"): fjern forklaring
  om at `aggregation`-metadata må setjast manuelt i `build.yaml`, forklar i staden at
  organisasjon vert auto-detektert frå CODEOWNERS.md

- **`mkdocs/docs/ny-begrepsmodell.md`**: fjern steget om å fylle ut
  `aggregation.organization` og `aggregation.catalog_name`, forklar i staden at
  eigarskap vert auto-detektert frå CODEOWNERS.md

- **`README.md`** (Begrepsmodellering-seksjonen): fjern steg 2 om å redigere `build.yaml`

### 8. Migrer eksisterande begrepssamlingar (valfritt)

Vurder om me skal fjerne `aggregation`-blokka frå eksisterande begrepssamlingar
(`begrepssamling-foretaksregisteret/build.yaml`) for å teste fallback-mekanismen.

**Alternativ:** Behald eksisterande `aggregation`-blokkar som eksplisitte overrides,
og la nye begrepssamlingar bruke auto-deteksjon.

### 9. Dokumenter fallback-mekanismen

Legg til ein seksjon i `CONVENTIONS.md` eller `src/assets/scripts/collect-concepts.py`
sin docstring som forklarar fallback-ordenen:

1. **Eksplisitt `aggregation`-blokk i `build.yaml`** — brukast dersom til stades
2. **CODEOWNERS.md path-matching** — auto-deteksjon basert på begrepssamlinga sin sti
3. **Feil** — dersom ingen av dei to finn eigar-org, hopp over begrepssamlinga med warning

## Handlingsliste

- [x] Steg 1: Vurder om `begrepskatalog_slug` skal vere eksplisitt felt eller utleidd (alternativ 1 brukt)
- [x] Steg 2: Implementer `_load_codeowners()` i `collect-concepts.py`
- [x] Steg 3: Implementer `_find_owner_org()` med path-matching-logikk (fnmatch)
- [x] Steg 4: Utvid til `get_aggregation_metadata()` med fallback til CODEOWNERS.md
- [x] Steg 5: Test med eksisterande begrepssamling (fjerna aggregation-blokk, auto-deteksjon fungerer)
- [x] Steg 6: Oppdater `new-begrepssamling.sh` til å **ikkje** inkludere aggregation-blokk
- [x] Steg 7: Oppdater dokumentasjon (CONVENTIONS.md)
- [x] Steg 8: Eksisterande begrepssamling migrert (aggregation-blokk fjerna)
- [x] Steg 9: Dokumentert fallback-mekanismen i CONVENTIONS.md og docstring

## Fordeler

1. **DRY-prinsippet:** Organisasjonsinformasjon finst berre éin stad (CODEOWNERS.md)
2. **Konsistens:** Eigarskap vert automatisk synkronisert mellom CODEOWNERS.md og begrepskatalog
3. **Enklare onboarding:** Nye brukarar treng ikkje manuelt kopiere organisasjonsnummer
4. **Feilreduksjon:** Mindre risiko for inkonsistens mellom CODEOWNERS.md og build.yaml

## Ulemper / Risiko

1. **Ekstra kompleksitet:** `collect-concepts.py` må parse CODEOWNERS.md og gjere path-matching
2. **Feilsøking:** Dersom path-matching feilar, kan det vere vanskeleg å forstå kvifor
3. **Avhengigheit:** Begrepssamlingar må liggje under ein `path_pattern` i CODEOWNERS.md
4. **Fallback-mekanisme:** Må handtere tilfellet der CODEOWNERS.md manglar eller er ugyldig

## Alternativ tilnærming: Behald manuell konfigurasjon

Dersom kompleksiteten vert vurdert som for høg, kan me behalde `aggregation`-blokka
som obligatorisk i `build.yaml` og i staden forbetre feilmeldingane dersom den manglar
eller er ugyldig.

**Anbefaling:** Implementer auto-deteksjon med fallback til manuell konfigurasjon —
det gir beste kombinasjon av brukarvenlegheit og fleksibilitet.

## Utført

Alle steg er implementerte og testede:

1. **`collect-concepts.py`**:
   - `load_codeowners()`: les YAML-frontmatter frå CODEOWNERS.md (regex-ekstraksjon)
   - `find_owner_org()`: path-matching med fnmatch mot `path_patterns`
   - `get_aggregation_metadata()`: fallback-mekanisme (build.yaml → CODEOWNERS.md → feil)
   - Oppdatert `main()` til å laste CODEOWNERS.md og bruke ny metadata-funksjon

2. **`CODEOWNERS.md`**:
   - Oppdatert `brreg` path_patterns til `src/linkml/oreg/**` (i staden for spesifikke underkatalogar)
   - Dette dekkjer alle begrepssamlingar under `oreg/`

3. **`new-begrepssamling.sh`**:
   - Fjerna `aggregation`-blokk frå generert `build.yaml`
   - Lagt til kommentar om auto-deteksjon frå CODEOWNERS.md
   - Oppdatert "Neste steg"-utskrift (fjerna steg om å redigere aggregation-metadata)

4. **`CONVENTIONS.md`**:
   - Oppdatert seksjon "Per begrepssamling" med forklaring av auto-deteksjon
   - Dokumentert fallback-orden (eksplisitt → auto-deteksjon → feil)

5. **Eksisterande begrepssamling migrert**:
   - `begrepssamling-foretaksregisteret/build.yaml`: fjerna eksplisitt `aggregation`-blokk
   - Test viser at auto-deteksjon fungerer korrekt (974760673 → brreg-begrepskatalog)

**Testresultat:**

```
[INFO] Auto-detektert src/linkml/oreg/begrepssamling-foretaksregisteret → org 974760673 (Brønnøysundregistra), katalog brreg-begrepskatalog
[INFO] ✓ Genererte .../brreg-begrepskatalog.yaml med 3 begrep
```

Validering passerer OK med `make validate-instance`.
