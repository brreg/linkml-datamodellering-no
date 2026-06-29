# Arkitektur-oversikt

Dette dokumentet viser arkitekturen for publiseringsflyt frå repoet til eksterne katalogar.

---

## Publiseringsflyt til eksterne system

```mermaid
flowchart TB
    subgraph Utviklar
        A[Rediger YAML<br/>src/linkml/begrepskatalog/<br/>src/linkml/modellkatalog/]
    end
    
    subgraph "GitHub Repository"
        B[Push til main] --> C[GitHub Actions<br/>generate.yml]
        C --> D[Validering<br/>make mcp-validate]
        D --> E[Generering<br/>make convert-data]
        E --> F[Genererte artefaktar<br/>TTL / JSON Schema / OWL]
    end
    
    subgraph GitHub
        F --> G[GitHub Pages<br/>brreg.github.io/linkml-datamodellering-no/]
        F --> H[GitHub Releases<br/>v1.0.0, v1.1.0, ...]
    end
    
    subgraph "Eksterne katalogar (pull/høsting)"
        G -.->|HTTP GET<br/>Høsting konfigurert av org| I[Felles Begrepskatalog<br/>data.norge.no/concepts]
        G -.->|HTTP GET<br/>Høsting konfigurert av org| J[Felles Datakatalog<br/>data.norge.no/models]
    end
    
    A --> B
    
    style A fill:#E0E0E0
    style G fill:#90EE90
    style H fill:#87CEEB
    style I fill:#FFE4B5
    style J fill:#FFE4B5
    
    classDef external stroke:#FF6B6B,stroke-width:3px,stroke-dasharray: 5 5
    class I,J external
```

**Nøkkel:**
- **Solid pil (→):** Automatisk prosess, kontrollert av repoet
- **Stipla pil (-.->):** Ekstern prosess, **ikkje** kontrollert av repoet
- **Raud stipla ramme:** Eksterne system utanfor repoets kontroll

---

## Prinsipp: Pull, ikkje push

Repoet følgjer "pull, ikkje push"-prinsippet:

| Kva repoet GØR | Kva repoet IKKJE gjer |
|---|---|
| ✅ Publiserer artefaktar til GitHub Pages | ❌ Pusher ikkje til data.norge.no |
| ✅ Publiserer releases til GitHub | ❌ Har ikkje API-credentials for Felles Begrepskatalog |
| ✅ Validerer data mot policies | ❌ Har ikkje API-credentials for Felles Datakatalog |
| ✅ Genererer høstingsklare TTL-filer | ❌ Kontrollerer ikkje når høsting skjer |

**Kvifor?**

- **Enklare arkitektur:** Repoet treng ikkje credentials eller integrasjon mot eksterne API-ar
- **Færre avhengigheiter:** Repoet fungerer sjølv om Felles Begrepskatalog/Datakatalog er nede
- **Fleksibilitet:** Kvar organisasjon kan velje når/om dei vil høste data

---

## Dataflyt: frå YAML til data.norge.no

### Steg 1-4: Repoet sitt ansvar (automatisk)

```mermaid
sequenceDiagram
    participant Dev as Utviklar
    participant Git as GitHub
    participant CI as GitHub Actions
    participant Pages as GitHub Pages
    
    Dev->>Git: git push
    Git->>CI: Trigger generate.yml
    CI->>CI: make mcp-validate POLICY=felles-begrepskatalog
    CI->>CI: make convert-data (YAML → TTL)
    CI->>Pages: Deploy til brreg.github.io
    Pages-->>Dev: ✓ Synleg på GitHub Pages
```

**Tidsbruk:** 3–5 minutt

### Steg 5-6: Ekstern prosess (manuell koordinering)

```mermaid
sequenceDiagram
    participant Pages as GitHub Pages
    participant Admin as Admin-grensesnitt
    participant FDK as Felles Datakatalog
    participant Public as data.norge.no
    
    Admin->>FDK: Registrer høstingsendepunkt (éin gong)
    Note over Admin,FDK: Krev ID-porten + Altinn-rolle
    
    FDK->>Pages: HTTP GET (dagleg/ukentleg)
    Pages-->>FDK: TTL-fil
    FDK->>FDK: Parser og indekser
    FDK->>Public: Publiser til data.norge.no
```

**Tidsbruk:** Varierer (minutt til dagar, avhengig av høstingsoppsett)

---

## Manifest-konfigurasjon

Kvar datafil under `src/linkml/*/data/<katalog>/` har ein `manifest.yaml`:

```yaml
publish_external: true  # Publiser til GitHub Pages?
data_policy: felles-begrepskatalog  # Valideringspolicy
```

**Effekt av `publish_external`:**

| Verdi | GitHub Pages | Høstingsendepunkt | Felles Begrepskatalog/Datakatalog |
|---|---|---|---|
| `true` | ✅ Publisert | ✅ Tilgjengeleg | ⚠️ Kan høstast (dersom konfigurert) |
| `false` | ❌ Ikkje publisert | ❌ Ikkje tilgjengeleg | ❌ Kan ikkje høstast |

---

## Sjå òg

- [publiseringsflyt-oversikt.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/backlog/publiseringsflyt-oversikt.md) — detaljert dokumentasjon
- [publisering-begrep.md](publisering-begrep.md) — rettleiing for begrepskatalog
- [publisering-modell.md](publisering-modell.md) — rettleiing for modellkatalog
- [GOVERNANCE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/GOVERNANCE.md) — publiseringspolicy
