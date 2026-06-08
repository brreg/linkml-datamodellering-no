# Spesifikasjon: mcp-linkml-begrep-generator

## Bakgrunn og mål

`specs/begrep-modellering.md` beskriv korleis begreper vert modellert lokalt i
LinkML-format før dei vert publiserte til Felles Begrepskatalog. Manuell oppretting
av YAML-instansfiler krev at brukaren kjenner strukturen i skos-ap-no-skjemaet,
URI-mønster, LOS-tema-slugar og kjeldekodane i FBK-vokabularet.

Målet med `mcp-linkml-begrep-generator` er å gje ein AI-assistent eit sett
MCP-verktøy for å:

1. **Generere** ei gyldig `BegrepContainer`-YAML-blokk frå strukturerte parametrar
2. **Validere** ei ferdig instansfil mot skos-ap-no-skjemaet
3. **Søkje** i den statiske lista over gyldige LOS-tema utan netverkskall

Serveren er eit *tillegg* til mcp-linkml-validator — han handterer
begreps-domenespesifikk logikk som ein generell validator ikkje kjenner.

---

## Plassering og filstruktur

```
src/mcp-linkml-begrep-generator/
├── Dockerfile
├── requirements.txt
├── server.py            ← stdio JSON-RPC 2.0, same mønster som mcp-linkml-generator
├── generator.py         ← logikk for å byggje YAML-blokkar frå parametrar
├── los_tema.py          ← statisk liste over gyldige LOS-tema
└── profiles/
    ├── default.yaml     ← standardprofil (ingen org-spesifikke standardverdiar)
    └── <org>.yaml       ← ein profil per organisasjon/katalog (t.d. brreg.yaml)
```

---

## Containeroppsett

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "server.py"]
```

`requirements.txt`:
```
pyyaml>=6.0
linkml>=1.8
```

Serveren køyrer som ein podman-container med stdio-transport — same mønster som
dei to eksisterande MCP-serverane.

---

## MCP-verktøy

Serveren eksponerer fire verktøy:

```
opprett_begrep    ← byggjer YAML frå strukturerte parametrar (brukar profil)
valider_begrep    ← køyrer linkml-validate på ei YAML-fil
list_profiles     ← listar tilgjengelege profiler med namn og skildring
list_los_tema     ← returnerer statisk liste over gyldige LOS-tema
```

---

### `opprett_begrep`

Byggjer ein komplett `BegrepContainer`-YAML-blokk (som kan limast inn i ei
instansfil) frå parametrar. Alle obligatoriske felt i SKOS-AP-NO-Begrep vert
inkluderte; valfrie felt vert inkluderte dersom dei er oppgjevne.

#### Påkravde parametrar

| Parameter | Type | Beskriving |
|---|---|---|
| `base_uri` | string | Base-URI for organisasjonen, t.d. `https://begrep.brreg.no` |
| `slug` | string | Kort identifikator for begrepet, t.d. `foretaksnavn` |
| `anbefalt_term_nb` | string | Anbefalt term på bokmål |
| `definisjon_nb` | string | Definisjonstekst på bokmål |
| `kjelde_relasjon` | enum | Ein av `direct-from-source`, `self-composed`, `derived-from-source` |
| `utgjevar_uri` | string | URI til utgjevande organisasjon (t.d. Enhetsregisteret-URI) |
| `fagomrade_uri` | string | URI til LOS-tema (bruk `list_los_tema` for gyldige verdiar) |

#### Valfrie parametrar

| Parameter | Type | Beskriving |
|---|---|---|
| `profil` | string | Profilnamn (standard: `default`). Profilen set standardverdiar for URI-mønster, kjelde_relasjon, utgjevar_uri m.m. |
| `anbefalt_term_nn` | string | Anbefalt term på nynorsk |
| `anbefalt_term_en` | string | Anbefalt term på engelsk |
| `definisjon_nn` | string | Definisjonstekst på nynorsk |
| `definisjon_en` | string | Definisjonstekst på engelsk |
| `kontaktpunkt_uri` | string | URI til kontaktpunkt-objekt (profilen set standard om utelate) |
| `merknad` | string[] | Merknadstekstar |
| `eksempel` | string[] | Eksempelstrengjer |
| `sja_ogsa_omgrep` | string[] | URI-ar til relaterte begreper (kan vere FBK-URI-ar) |

Parametrar som ikkje er oppgjevne vert fylt frå profilen. Dersom profilen heller ikkje
har ein verdi, vert dei aktuelle felta utelate frå outputen (valfrie) eller returnerer
ein feil (påkravde).

Merk at `base_uri`, `utgjevar_uri` og `fagomrade_uri` kan setjast til påkravde ved
at profilen ikkje inneheld standardverdiar — nyttig for ein `default`-profil der
brukaren alltid må oppgje desse eksplisitt.

#### Output

YAML-streng som representerer ein komplett `BegrepContainer` med:
- `begrep`-seksjon med éin `Begrep`-instans
- `definisjoner`-seksjon med eitt `Definisjon`-objekt per oppgjevne språk
- `organisasjonar`-seksjon med stub for utgjevaren
- `kontaktpunkt`-seksjon med stub for kontaktpunktet

**Eksempelkall med eksplisitte parametrar (default-profil):**
```json
{
  "profil": "default",
  "base_uri": "https://begrep.brreg.no",
  "slug": "aksjeselskap",
  "anbefalt_term_nb": "aksjeselskap",
  "anbefalt_term_nn": "aksjeselskap",
  "definisjon_nb": "selskap med begrenset ansvar for aksjeeierne",
  "kjelde_relasjon": "self-composed",
  "utgjevar_uri": "https://data.norge.no/organizations/974760673",
  "fagomrade_uri": "https://psi.norge.no/los/tema/naringsliv",
  "merknad": ["Regulert av aksjeloven av 1997."],
  "sja_ogsa_omgrep": ["https://data.norge.no/concepts/5916c2a0-e5d3-31f7-b8d4-02938091f11f"]
}
```

**Eksempelkall med org-profil (brreg) — færre påkravde parametrar:**
```json
{
  "profil": "brreg",
  "slug": "aksjeselskap",
  "anbefalt_term_nb": "aksjeselskap",
  "anbefalt_term_nn": "aksjeselskap",
  "definisjon_nb": "selskap med begrenset ansvar for aksjeeierne",
  "fagomrade_uri": "https://psi.norge.no/los/tema/naringsliv",
  "merknad": ["Regulert av aksjeloven av 1997."]
}
```

**Eksempelresultat (forkorta):**
```yaml
begrep:
  - id: https://begrep.brreg.no/aksjeselskap
    anbefalt_term:
      - aksjeselskap
      - aksjeselskap
    har_definisjon:
      - https://begrep.brreg.no/def/aksjeselskap-nb
      - https://begrep.brreg.no/def/aksjeselskap-nn
    identifikator_literal: "https://begrep.brreg.no/aksjeselskap"
    kontaktpunkt_vcard:
      - https://begrep.brreg.no/kontakt/begrepsansvarleg
    utgjevar: https://data.norge.no/organizations/974760673
    fagomrade:
      - https://psi.norge.no/los/tema/naringsliv
    merknad:
      - Regulert av aksjeloven av 1997.
    sja_ogsa_omgrep:
      - https://data.norge.no/concepts/5916c2a0-e5d3-31f7-b8d4-02938091f11f

definisjoner:
  - id: https://begrep.brreg.no/def/aksjeselskap-nb
    tekst: selskap med begrenset ansvar for aksjeeierne
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#self-composed
  - id: https://begrep.brreg.no/def/aksjeselskap-nn
    tekst: selskap med begrenset ansvar for aksjeeierne
    kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#self-composed

organisasjonar:
  - id: https://data.norge.no/organizations/974760673

kontaktpunkt:
  - id: https://begrep.brreg.no/kontakt/begrepsansvarleg
```

Brukar listar JSON-resultatet med `content[0].text` og sett det saman med
eventuelt eksisterande innhald i instansfila.

---

### `valider_begrep`

Køyrer `linkml-validate` på ei YAML-instansfil mot eit angitt skos-ap-no-skjema.
Internt: skriv YAML til ein midlertidig fil og køyrer validatoren i ein subprocess.

#### Parametrar

| Parameter | Type | Beskriving |
|---|---|---|
| `yaml_innhald` | string | Heile innhaldet i instansfila som YAML-streng |
| `skjema_sti` | string | Sti til skjemafil relativt til `/repo` (montert inn i containeren), t.d. `src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml` |

#### Output

```json
{
  "gyldig": true,
  "feiltal": 0,
  "åtvaringtal": 0,
  "hendingar": []
}
```

Kvar hending har same format som `mcp-linkml-validator`:
```json
{
  "alvorlegheit": "error",
  "kode": "required-slot",
  "mål": "Begrep.anbefalt_term",
  "melding": "Required slot 'anbefalt_term' not present"
}
```

---

### `list_profiles`

Listar tilgjengelege profiler med namn og skildring. Same mønster som
`list_profiles` i `mcp-linkml-generator`.

#### Parametrar

Ingen.

#### Output

```json
[
  {
    "name": "default",
    "description": "Standardprofil utan org-spesifikke standardverdiar."
  },
  {
    "name": "brreg",
    "description": "Profil for Registerenheten i Brønnøysund."
  }
]
```

---

### `list_los_tema`

Returnerer den statiske lista over gyldige LOS-tema-URI-ar med norske namn.
Ingen nettverkskall — lista er kompilert inn i `los_tema.py` frå
`https://psi.norge.no/los/ontologi/tema`.

#### Parametrar

Ingen.

#### Output

```json
[
  {
    "uri": "https://psi.norge.no/los/tema/naringsliv",
    "namn": "Næringsliv"
  },
  {
    "uri": "https://psi.norge.no/los/tema/naring",
    "namn": "Næring"
  }
]
```

Fullstendig liste: sjå `los_tema.py` i implementasjonen.

---

## Profiler

Profiler ligg i `profiles/<namn>.yaml` og styrer standardverdiar og URI-mønster
for `opprett_begrep`. Profil-YAML vert lesen av `load_profile(name)` i
`generator.py` — same mønster som `load_profile()` i `mcp-linkml-generator/converter.py`.

### Profil-nøklar

| Nøkkel | Beskriving |
|---|---|
| `description` | Kort skildring (vises av `list_profiles`) |
| `uri.begrep_pattern` | URI-mønster for begrep (variablar: `{base_uri}`, `{slug}`) |
| `uri.definisjon_pattern` | URI-mønster for definisjonsobjekt (+ `{lang}`) |
| `uri.kontaktpunkt_default` | Fallback-URI for kontaktpunktstub (+ `{base_uri}`) |
| `defaults.base_uri` | Standard base-URI (utelat for å gjere parameteren påkravd) |
| `defaults.utgjevar_uri` | Standard utgjevar-URI |
| `defaults.kjelde_relasjon` | Standard kjelde_relasjon (`self-composed` o.l.) |
| `languages.required` | Språk der `anbefalt_term` alltid vert inkludert |
| `languages.optional` | Språk som vert inkludert dersom parameteren er oppgjeven |
| `generation.add_header_comment` | Legg til kommentarblokk øvst i YAML-en (standard: true) |

### `profiles/default.yaml`

```yaml
version: 1
description: >
  Standardprofil utan org-spesifikke standardverdiar.
  Alle parametrar (base_uri, utgjevar_uri, fagomrade_uri) må oppgjevast eksplisitt.

uri:
  begrep_pattern: "{base_uri}/{slug}"
  definisjon_pattern: "{base_uri}/def/{slug}-{lang}"
  kontaktpunkt_default: "{base_uri}/kontakt/begrepsansvarleg"

defaults:
  kjelde_relasjon: "self-composed"

languages:
  required: [nb]
  optional: [nn, en]

generation:
  add_header_comment: true
```

### `profiles/brreg.yaml` (eksempel på org-profil)

```yaml
version: 1
description: >
  Profil for Registerenheten i Brønnøysund.
  Forhåndsset base_uri, utgjevar_uri og kontaktpunkt_uri.

uri:
  begrep_pattern: "{base_uri}/{slug}"
  definisjon_pattern: "{base_uri}/def/{slug}-{lang}"
  kontaktpunkt_default: "https://begrep.brreg.no/kontakt/begrepsansvarleg"

defaults:
  base_uri: "https://begrep.brreg.no"
  utgjevar_uri: "https://data.norge.no/organizations/974760673"
  kjelde_relasjon: "self-composed"

languages:
  required: [nb]
  optional: [nn, en]

generation:
  add_header_comment: true
```

Med `brreg`-profilen slepp brukaren å oppgje `base_uri`, `utgjevar_uri` og
`kontaktpunkt_uri` for kvart kall.

---

## Implementasjonsdetaljar

### `server.py`

Følgjer nøyaktig same mønster som `mcp-linkml-generator/server.py`:
- stdio JSON-RPC 2.0 (éi JSON-linje per melding)
- `handle(msg)` som dispatcher på `method`
- `initialize`-respons med `protocolVersion: "2024-11-05"`

```python
TOOL_OPPRETT_BEGREP = {
    "name": "opprett_begrep",
    "description": (
        "Genererer ein komplett BegrepContainer-YAML-blokk frå strukturerte parametrar. "
        "Følgjer SKOS-AP-NO-Begrep og mønsteret i specs/begrep-modellering.md. "
        "Bruk list_profiles for å sjå tilgjengelege profiler."
    ),
    "inputSchema": { ... }  # sjå parameter-tabellane over
}

TOOL_VALIDER_BEGREP = {
    "name": "valider_begrep",
    "description": "Validerer ei YAML-instansfil mot eit skos-ap-no-skjema.",
    "inputSchema": { ... }
}

TOOL_LIST_PROFILES = {
    "name": "list_profiles",
    "description": "Listar tilgjengelege profiler med namn og skildring.",
    "inputSchema": {"type": "object", "properties": {}}
}

TOOL_LIST_LOS_TEMA = {
    "name": "list_los_tema",
    "description": "Listar gyldige LOS-tema URI-ar (statisk liste, ingen nettverkskall).",
    "inputSchema": {"type": "object", "properties": {}}
}
```

### `generator.py`

Eksporterer to funksjonar:

```python
def load_profile(name: str) -> dict:
    """Lastar ein namngitt profil frå profiles/-katalogen."""
    profile_dir = Path(__file__).parent / "profiles"
    with open(profile_dir / f"{name}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def opprett_begrep(
    profile: dict,
    slug: str,
    anbefalt_term_nb: str,
    definisjon_nb: str,
    fagomrade_uri: str,
    *,
    base_uri: str = "",             # overstyrer profil-standard
    kjelde_relasjon: str = "",      # overstyrer profil-standard
    utgjevar_uri: str = "",         # overstyrer profil-standard
    anbefalt_term_nn: str = "",
    anbefalt_term_en: str = "",
    definisjon_nn: str = "",
    definisjon_en: str = "",
    kontaktpunkt_uri: str = "",
    merknad: list[str] = [],
    eksempel: list[str] = [],
    sja_ogsa_omgrep: list[str] = [],
) -> str:
    """Returnerer ein YAML-streng med BegrepContainer-innhald."""
```

Funksjonen løyser verdiar i prioritetsrekkefølgje:
1. Eksplisitt parameter frå kallet
2. `defaults`-seksjon i profilen
3. Feil dersom verdi manglar og feltet er påkravd

Serialiserer med `yaml.dump(allow_unicode=True, default_flow_style=False, sort_keys=False)`.

#### URI-konstruksjon

URI-mønstrane vert henta frå `profile["uri"]` og interpolert med `str.format()`:

| Nøkkel i profil | Standardverdi i `default.yaml` |
|---|---|
| `uri.begrep_pattern` | `{base_uri}/{slug}` |
| `uri.definisjon_pattern` | `{base_uri}/def/{slug}-{lang}` |
| `uri.kontaktpunkt_default` | `{base_uri}/kontakt/begrepsansvarleg` |

Kontaktpunkt-URI vert berre auto-generert frå profilen dersom `kontaktpunkt_uri`
er tom streng.

#### Kjeldetype-URI

```python
_KJELDE_BASE = "https://data.norge.no/vocabulary/relationship-with-source-type"

KJELDETYPAR = {
    "direct-from-source":  f"{_KJELDE_BASE}#direct-from-source",
    "self-composed":       f"{_KJELDE_BASE}#self-composed",
    "derived-from-source": f"{_KJELDE_BASE}#derived-from-source",
}
```

### `los_tema.py`

Statisk liste henta frå `https://psi.norge.no/los/ontologi/tema`. Inkluderer
minst alle tema under hovudkategoriane næringsliv, arbeidsliv, helse, utdanning,
kultur, samferdsel, miljø, demokrati, offentleg forvaltning og økonomi.

```python
LOS_TEMA: list[dict] = [
    {"uri": "https://psi.norge.no/los/tema/naringsliv",      "namn": "Næringsliv"},
    {"uri": "https://psi.norge.no/los/tema/naring",          "namn": "Næring"},
    {"uri": "https://psi.norge.no/los/tema/naringsutvikling", "namn": "Næringsutvikling"},
    # ... (fullstendig liste i implementasjonen)
]
```

Merk: LOS nyttar ASCII i slug-ane (`æ → a`, `ø → o`, `å → a`).

---

## Containerintegrasjon

Containeren treng tilgang til repo-rota for at `valider_begrep` skal finne
skjemafiler. Monter inn som bind-mount (same mønster som mcp-linkml-validator):

```bash
podman run --rm -i \
  -v "$(pwd):/repo:ro" \
  mcp-linkml-begrep-generator
```

`skjema_sti`-parameteren er alltid relativ til `/repo`.

### Makefile-mål

```makefile
mcp-begrep-build:
    podman build -t mcp-linkml-begrep-generator src/mcp-linkml-begrep-generator

mcp-begrep-run:
    podman run --rm -i -v "$(PWD):/repo:ro" mcp-linkml-begrep-generator

# List profiler:
#   make mcp-begrep-list-profiles
mcp-begrep-list-profiles:
    @echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
    | podman run --rm -i mcp-linkml-begrep-generator
```

---

## Release

`release.yml`-workflowen skal utvidast med ein ny jobb på same mønster som
`mcp-linkml-generator` og `mcp-linkml-validator`:

```yaml
mcp-linkml-begrep-generator:
  runs-on: ubuntu-22.04
  permissions:
    contents: read
    packages: write
  steps:
    - uses: actions/checkout@v6
    - name: Logg inn på GHCR
      run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
    - name: Bygg og push mcp-linkml-begrep-generator
      run: |
        podman build \
          -t "ghcr.io/${{ github.repository_owner }}/mcp-linkml-begrep-generator:${{ github.ref_name }}" \
          src/mcp-linkml-begrep-generator
        podman tag \
          "ghcr.io/${{ github.repository_owner }}/mcp-linkml-begrep-generator:${{ github.ref_name }}" \
          "ghcr.io/${{ github.repository_owner }}/mcp-linkml-begrep-generator:latest"
        podman push "ghcr.io/${{ github.repository_owner }}/mcp-linkml-begrep-generator:${{ github.ref_name }}"
        podman push "ghcr.io/${{ github.repository_owner }}/mcp-linkml-begrep-generator:latest"
```

---

## Implementasjonsrekkefølgje

```
1. Opprett src/mcp-linkml-begrep-generator/
2. Skriv profiles/default.yaml (utan org-spesifikke standardverdiar)
3. Skriv los_tema.py med fullstendig liste
4. Skriv generator.py med load_profile() og opprett_begrep()
5. Skriv server.py med dei fire verktøya
6. Skriv Dockerfile og requirements.txt
7. Legg til Makefile-mål (mcp-begrep-build, mcp-begrep-run, mcp-begrep-list-profiles)
8. Legg til jobb i release.yml
9. Test lokalt:
   echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
   | podman run --rm -i mcp-linkml-begrep-generator
```

---

## Avvegingar

**Profil vs. per-kall-parametrar**: Profilen er ikkje ein mal som låser ned
generatoren — alle profil-standardverdiane kan overstyrast per kall. Ein
`default`-profil utan standardverdiar for `base_uri` og `utgjevar_uri` tydeleggjer
at desse er nødvendige for kvart kall. Ein org-profil (`brreg.yaml`) sparer brukaren
for repetisjon. Nye profiler kan leggjast til utan kodeendring i `server.py`.

**Statisk vs. dynamisk LOS-liste**: LOS-datasettet er stabilt og sjeldan oppdatert.
Ein statisk `los_tema.py` er enklare å vedlikehalde og krev ingen nettverkstilgang
inne i containeren. Ved neste LOS-oppdatering er det nok å oppdatere fila og byggje
containeren på nytt.

**`valider_begrep` vs. `mcp-linkml-validator`**: `mcp-linkml-validator` er meir
generell og støttar policy-sjikt (bronze/silver/gold). `valider_begrep` er meint
for rask syntaksvalidering under utvikling — brukar bør køyre `mcp-linkml-validator`
med bronze-policy for fullstendig validering før commit.

**`kontaktpunkt`-stub**: Kontaktpunkt-objektet vert generert med berre `id`-felt
dersom `kontaktpunkt_uri` er utelaten. Brukar må fylle inn resterande felt manuelt
(t.d. `fn`, `hasEmail`) i instansfila etterpå, sidan desse er nødvendige i
SKOS-AP-NO.
