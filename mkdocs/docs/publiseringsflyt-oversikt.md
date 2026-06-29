# Publiseringsflyt-oversikt

**Status:** Dokumentasjon  
**Dato:** 2026-06-29  
**Kontekst:** Klargjering av publiseringsflyt til eksterne system — kva repoet faktisk publiserer og kva som skjer eksternt.

---

## Bakgrunn

Dette dokumentet dokumenterer den faktiske publiseringsflyten frå repoet til GitHub Pages og vidare til eksterne katalogar (Felles Begrepskatalog, Felles Datakatalog). Det er skrive for å tydeleggjere "pull, ikkje push"-prinsippet og klargjere kvar ansvaret ligg for kvar del av flyten.

---

## Publiseringsflyt: Oversikt

```mermaid
flowchart TB
    subgraph Lokalt
        A[Rediger YAML<br/>src/linkml/] --> B[make convert-data]
        B --> C[generated/<br/>TTL/JSON/OWL/...]
    end
    
    subgraph CI
        D[Push til main] --> E[GitHub Actions<br/>generate.yml]
        E --> F[Genererte artefaktar]
        F --> G[GitHub Pages Deploy]
    end
    
    subgraph GitHub
        G --> H[GitHub Pages<br/>brreg.github.io/linkml-datamodellering-no/]
        I[GitHub Releases<br/>v1.0.0] --> J[Versjonerte artefaktar]
    end
    
    subgraph Eksterne system
        H -.->|Høsting<br/>ekstern prosess| K[Felles Begrepskatalog<br/>data.norge.no/concepts]
        H -.->|Høsting<br/>ekstern prosess| L[Felles Datakatalog<br/>data.norge.no/models]
    end
    
    C --> D
    F --> I
    
    style H fill:#90EE90
    style K fill:#FFE4B5
    style L fill:#FFE4B5
```

**Nøkkel:**
- **Solid pil (→):** Automatisk, kontrollert av repoet
- **Stipla pil (-.->):** Ekstern prosess, **ikkje** kontrollert av repoet

---

## Kvar genererte filer endar

### 1. `generated/` (lokal build)

**Kvar:** `/generated/<domain>/<modell>/`

**Innhald:**
- SHACL shapes (`.ttl`)
- JSON Schema (`.json`)
- OWL ontologi (`.ttl`)
- Python-klassar (`.py`)
- Protobuf (`.proto`)
- Dokumentasjon (`docs/`)
- PlantUML-diagram (`.puml`, `.svg`)
- ER-diagram (`.md`)

**Git-status:** Ignorert (i `.gitignore`) — vert ikkje sjekka inn

**Formål:** Lokal testing og verifisering før push

---

### 2. GitHub Pages (automatisk publisering)

**URL:** `https://brreg.github.io/linkml-datamodellering-no/`

**Kvar kom det frå:** CI-jobben `generate.yml` (kjører på push til `main`)

**Innhald:**
- Alle genererte artefaktar (same som `generated/`)
- Begrepskatalogar: `.ttl`-filer frå `src/linkml/begrepskatalog/*/data/`
- Modellkatalogar: `.ttl`-filer frå `src/linkml/modellkatalog/*/data/`
- MkDocs-dokumentasjonsportal

**Versjonering:** Peikar alltid til siste versjon på `main` — **ikkje versjonsstabil**

**Formål:**
- Dokumentasjonsportal for menneskelege brukarar
- Høstingsendepunkt for Felles Begrepskatalog / Felles Datakatalog

---

### 3. GitHub Releases (versjonerte artefaktar)

**URL:** `https://github.com/brreg/linkml-datamodellering-no/releases`

**Kvar kom det frå:** `release-please` opprettar release ved merge av release-PR

**Innhald:**
- Source code (`.zip`, `.tar.gz`)
- (Potensielt) bundla artefaktar som release assets

**Versjonering:** Semantisk versjonering (`v1.0.0`, `v1.1.0`, osv.) — **versjonsstabil**

**Formål:**
- Stabile URI-ar for import frå eksterne repo
- Historisk arkiv av tidlegare versjonar

---

## Kva repoet IKKJE gjer

### ❌ Pusher ikkje direkte til data.norge.no

Repoet har **ikkje**:
- API-credentials for Felles Begrepskatalog
- API-credentials for Felles Datakatalog
- Direkteintegrasjon mot data.norge.no

Repoet publiserer artefaktar til **GitHub Pages**, og det er opp til Felles Begrepskatalog/Datakatalog å høste derifrå.

### ❌ Pusher ikkje til schema-registry

Repoet publiserer ikkje SHACL-shapes, JSON Schema eller OWL-ontologiar til eksterne schema-registries (t.d. Apicurio Registry). Slike integrasjonar krev spesialtilpassingar per målsystem og ligg utanfor repoets ansvarsfelt.

### ❌ Har ikkje kontroll over høstingstidspunkt

Når Felles Begrepskatalog/Datakatalog høstar data frå GitHub Pages er **utanfor repoets kontroll**. Det er ein ekstern prosess som kvar organisasjon må koordinere med Digitaliseringsdirektoratet.

---

## Publisering til Felles Begrepskatalog / Felles Datakatalog

### Slik fungerer det

#### Steg 1-3: Repoet sitt ansvar (automatisk)

1. **Lokal redigering:** Du redigerer YAML-filer i `src/linkml/begrepskatalog/*/data/` eller `src/linkml/modellkatalog/*/data/`
2. **Generering:** `make convert-data` konverterer YAML til SKOS/Turtle eller ModelDCAT-AP-NO
3. **Publisering til GitHub Pages:** CI publiserer `.ttl`-filen til `https://brreg.github.io/linkml-datamodellering-no/...`

#### Steg 4: Ekstern prosess (manuell koordinering)

4. **Høsting frå Felles Begrepskatalog/Datakatalog:** Organisasjonen må registrere høstingsendepunktet på [admin.fellesdatakatalog.digdir.no](https://admin.fellesdatakatalog.digdir.no) (krev ID-porten-innlogging og Altinn-rolle)

**Status i PoC-fasen:** Steg 1-3 er implementerte. Steg 4 må koordinerast manuelt med Digitaliseringsdirektoratet for kvar organisasjon.

---

## Kva styrer publisering til GitHub Pages?

### `manifest.yaml` — per datafil

Kvar datafil under `src/linkml/*/data/<katalog>/` har ein `manifest.yaml`:

```yaml
publish_external: true  # eller false
data_policy: felles-begrepskatalog  # eller felles-datakatalog
```

**`publish_external: true`** betyr:
- Datafila vert konvertert til `.ttl` og publisert til GitHub Pages
- Datafila må validere med `felles-begrepskatalog`- eller `felles-datakatalog`-policy (null feil)

**`publish_external: false`** betyr:
- Datafila vert **ikkje** publisert til GitHub Pages
- Datafila vert berre validert lokalt

---

## Workflow: frå commit til synleg på data.norge.no

### 1. Utviklar lager pullrequest til `main`

```bash

# Oppdater main
git switch main
git pull origin main
# Lag ny arbeidsbranch
git switch -c feature/mi-endring
# Gjer endringar
git add src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml
git commit -m "feat(brreg-begrepskatalog): legg til nytt begrep 'aksjonær'"
# Push branch
git push -u origin feature/mi-endring
# Opprett Pull Request til main i github GUIet

```

### 2. CI kjører validering og generering

GitHub Actions (`generate.yml`):
1. Validerer datafila: `make mcp-validate POLICY=felles-begrepskatalog`
2. Genererer `.ttl`-fil: `make convert-data`
3. Publiserer til GitHub Pages: `actions/deploy-pages@v1`

**Tidsbruk:** ~3–5 minutt (avhengig av storleik på endringar)

### 3. GitHub Pages er oppdatert

`https://brreg.github.io/linkml-datamodellering-no/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog.ttl` inneheld no den oppdaterte datafila i SKOS/Turtle-format.

### 4. Felles Begrepskatalog høstar (ekstern prosess)

**Kven:** Digitaliseringsdirektoratet / Felles Begrepskatalog-systemet  
**Når:** Avhengig av høstingsintervall (t.d. dagleg, ukentleg)  
**Korleis:** HTTP GET frå GitHub Pages-URL  
**Kontroll:** Repoet har ingen kontroll over når/om høsting skjer

**Tidsbruk:** Varierer — frå minutt til dagar, avhengig av høstingsoppsett

### 5. Synleg på data.norge.no

Begrepet visast på [data.norge.no/concepts](https://data.norge.no/concepts) etter at høsting og indeksering er fullført.

---

## Feilsøking

### Problem: "Eg har pusha til main, men ser ikkje endringane på GitHub Pages"

**Løysing:**
1. Sjekk at CI-jobben `generate` er grøn: https://github.com/brreg/linkml-datamodellering-no/actions
2. Sjekk at `publish_external: true` i `manifest.yaml`
3. Vent 3–5 minutt for at GitHub Pages skal oppdaterast
4. Hard-refresh i nettlesaren (Ctrl+Shift+R)

### Problem: "GitHub Pages er oppdatert, men eg ser ikkje endringane på data.norge.no"

**Løysing:**
1. Verifiser at høstingsendepunktet er registrert på [admin.fellesdatakatalog.digdir.no](https://admin.fellesdatakatalog.digdir.no)
2. Kontakt Digitaliseringsdirektoratet (dataopen@digdir.no) for å verifisere høstingsstatus
3. Vurder manuell høsting via admin-grensesnittet ("Høst no"-knappen)

**NB:** Repoet har ingen måte å verifisere om høsting faktisk skjer — det er utanfor repoets kontroll.

---

## Oppsummering

| Steg | Ansvarleg | Automatisk? | Verifiserbart? |
|---|---|---|---|
| 1. Rediger YAML | Utviklar | Nei | Ja (lokal validering) |
| 2. Pullrequest til `main` | Utviklar | Nei | Ja (GitHub) |
| 3. CI genererer artefaktar | GitHub Actions | Ja | Ja (Actions-logg) |
| 4. Publiser til GitHub Pages | GitHub Actions | Ja | Ja (sjekk URL) |
| 5. Høsting frå Felles Begrepskatalog/Datakatalog | Utviklar i den enkelte virksomhet | Nei | Nei (ikkje tilgjengeleg for repoet) |
| 6. Synleg på data.norge.no | Digitaliseringsdirektoratet | Ja (etter høsting) | Ja (manuell sjekk) |

**Konklusjon:** Repoet kontrollerer steg 1-5. Steg 6 er eksterne prosessar som må koordinerast med Digitaliseringsdirektoratet.
