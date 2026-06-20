# Arkitekturoversikt

Diagramma under viser dei vesentlege delane av repoet og korleis dei spiller
saman med eksterne offentlege tenester. Dette er ein orienteringsskisse, ikkje
ein endringsplan — sjå `specs/README.md` for konvensjonen om kva som høyrer
under `backlog/`, `done/`, `rejected/` og `bugs/`.

Skissa er delt i to diagram (i staden for eitt breidt) for å halde tekstboksane
store og lesbare: del 1 dekkjer den interne flyten frå kildeskjema til
publiserte artefaktar, del 2 dekkjer korleis nasjonale katalogar, KUDAF og
verksemder hentar frå dei publiserte punkta. Usynlege lenkjer (`~~~`) brukast
berre for å tvinge nodar utan reell relasjon til å stable seg vertikalt i
staden for å spre seg i breidda — dei representerer ikkje ein avhengigheit.

## Del 1 — Frå kildeskjema til publiserte artefaktar

```mermaid
%%{init: {'themeVariables': {'fontSize': '20px'}}}%%
flowchart TB
    subgraph KILDE["src/linkml/ — kildeskjema"]
        direction TB
        PADKILDE[" "]
        COMMON["ap-no/common<br/>felles slot-definisjonar"]
        APNO["ap-no/*<br/>dcat-ap-no, skos-ap-no,<br/>modelldcat-ap-no, cpsv-ap-no,<br/>dqv-ap-no, xkos-ap-no"]
        FAIR["fair/fair-metadata"]
        FINTCOMMON["fint/fint-common"]
        DOMENE["domenemodeller<br/>ngr-*, oreg-*, fint-*, samt-bu<br/>(tree_root containerklasser)"]
        BEGREP["begrepskatalog/*<br/>SKOS-AP-NO-Begrep + data/*.yaml"]
        MODELLKAT["modellkatalog/*<br/>ModelDCAT-AP-NO"]

        PADKILDE ~~~ COMMON
        COMMON --> APNO
        APNO --> DOMENE
        FAIR --> DOMENE
        FINTCOMMON --> DOMENE
        APNO --> BEGREP
        APNO --> MODELLKAT

   

    end

    subgraph MCP["MCP-servere (lokalt, podman)"]
        direction TB
        PADMCP[" "]
        AI["KI-assistent<br/>(Claude m.fl.)"]
        MCPMOD["mcp-linkml-modell-utkast"]
        MCPBEGREP["mcp-linkml-begrep-utkast"]
        MCPVAL["mcp-linkml-validator<br/>bronze/silver/gold/<br/>felles-datakatalog/felles-begrepskatalog"]

        PADMCP ~~~ AI
        AI --> MCPMOD
        AI --> MCPBEGREP
        AI --> MCPVAL

    end

    MCPMOD -.->|"genererer utkast til"| DOMENE
    MCPBEGREP -.->|"genererer utkast til"| BEGREP
    MCPVAL -.->|"validerer"| DOMENE
    MCPVAL -.->|"validerer"| BEGREP
    MCPVAL -.->|"validerer"| MODELLKAT
    MCPVAL ~~~ PADKILDE

    MCPVAL -.->|"valideringsresultat"| GHPAGES

    subgraph CI["GitHub Actions"]
        direction TB
        PADCI[" "]
        WFVALIDATE["validate.yml<br/>PR-validering"]
        WFGENERATE["generate.yml<br/>bygg artefakter + mkdocs"]
        WFRELEASE["release.yml<br/>container-images"]
        WFRELEASEPLEASE["release-please.yml<br/>versjonering"]
        PADCI ~~~ WFVALIDATE
        PADCI ~~~ WFGENERATE
        PADCI ~~~ WFRELEASE
        PADCI ~~~ WFRELEASEPLEASE

    end

    DOMENE -->|"push / PR"| WFVALIDATE
    DOMENE --> WFGENERATE
    WFGENERATE --> GHPAGES
    PADKILDE ~~~ PADCI
    BEGREP ~~~ PADCI
    MODELLKAT ~~~ PADCI

    subgraph PUBLISERT["Publiserte pull-punkt"]
        direction LR
        PADPUB[" "]
        GHPAGES["GitHub Pages<br/>dokumentasjonsportal"]
        GHRELEASES["GitHub Releases"]
        GHCR["GHCR<br/>container-images"]
        RAWGH["raw.githubusercontent.com"]
        PADPUB ~~~ GHPAGES
        PADPUB ~~~ GHRELEASES
        PADPUB ~~~ GHCR
        PADPUB ~~~ RAWGH
    end

    WFRELEASE --> GHCR
    WFRELEASEPLEASE -->|"tag → release"| GHRELEASES
    PADCI ~~~ PADPUB
    WFVALIDATE ~~~ PADPUB
    WFGENERATE ~~~ PADPUB
    WFRELEASE ~~~ PADPUB
    WFRELEASEPLEASE ~~~ PADPUB

    DOMENE -.->|"importerer via tag-URL"| RAWGH
    APNO -.->|"importerer via tag-URL"| RAWGH

    classDef default fill:#000000,color:#ffffff,stroke:#ffffff;
    classDef ekstern fill:#3a0a0a,color:#ffffff,stroke:#e74c3c;
    classDef ci fill:#0a1f3a,color:#ffffff,stroke:#5b9bd5;
    classDef mcp fill:#0a3a1f,color:#ffffff,stroke:#2ecc71;
    classDef usynlig fill:none,stroke:none,color:transparent;
    class GHPAGES,GHRELEASES,GHCR,RAWGH ekstern
    class WFVALIDATE,WFGENERATE,WFRELEASE,WFRELEASEPLEASE ci
    class MCPMOD,MCPBEGREP,MCPVAL,AI mcp
    class PADKILDE,PADMCP,PADCI,PADPUB usynlig

    style KILDE fill:#000000,color:#ffffff,stroke:#ffffff
    style MCP fill:#000000,color:#ffffff,stroke:#ffffff
    style CI fill:#000000,color:#ffffff,stroke:#ffffff
    style PUBLISERT fill:#000000,color:#ffffff,stroke:#ffffff
```

## Del 2 — Korleis nasjonale katalogar, KUDAF og verksemder hentar frå dette repoet

```mermaid
%%{init: {'themeVariables': {'fontSize': '20px'}}}%%
flowchart BT
    GHPAGES2["GitHub Pages<br/>dokumentasjonsportal<br/>(sjå del 1)"]
    RAWGH2["raw.githubusercontent.com<br/>(sjå del 1)"]
    REPOCI["dette repoet:<br/>reusable GitHub Actions"]
    ANCHOR2[" "]

    subgraph KATALOGAR["Nasjonale katalogar og søketjenester (haustar metadata)"]
        direction BT
        BEGREPSKAT["Felles Begrepskatalog<br/>concept-catalog.fellesdatakatalog.digdir.no"]
        DATAKAT["Felles Datakatalog<br/>data.norge.no"]
        KUDAFNODE["KUDAF-datafellesskap<br/>Sikt/HK-dir, kunnskapssektoren"]
        PADKAT[" "]
        DATAKAT ~~~ BEGREPSKAT
        BEGREPSKAT ~~~ PADKAT
    end

    BEGREPSKAT -.->|"haustar begrep,<br/>sjå publisering-begrep.md"| GHPAGES2
    DATAKAT -.->|"haustar datasett-metadata,<br/>sjå publisering-modell.md"| GHPAGES2

    subgraph KONSUMENTER["Verksemder (PULL) — planlagt/framtidig"]
        direction TB
        PADKON[" "]
        PRIVATKAT["Verksemd:<br/>privat datakatalog"]
        DATAPLATTFORM["Verksemd:<br/>privat dataplattform"]
        APIGATEWAY["Verksemd:<br/>privat API-gateway"]
        PADKON ~~~ PRIVATKAT
        PRIVATKAT ~~~ DATAPLATTFORM
        DATAPLATTFORM -->|"eksponerer data via"| APIGATEWAY
    end

    subgraph EKSTERNREPO["Eksternt repo (bootstrap)"]
        direction TB
        PADEKS[" "]
        BOOTSTRAP["bootstrap.sh<br/>curl-skript"]
        EKSTERNSKJEMA["eige LinkML-skjema<br/>importerer ap-no-profil"]
        PADEKS ~~~ BOOTSTRAP
        BOOTSTRAP ~~~ EKSTERNSKJEMA
    end

    EKSTERNSKJEMA --> RAWGH2
    BOOTSTRAP -.->|"hentar mal frå"| RAWGH2
    EKSTERNSKJEMA -->|"validering/generering"| REPOCI

    ANCHOR2 ~~~ PADKAT
    ANCHOR2 ~~~ PADKON

    KUDAFNODE -.->|"haustar datasett-metadata<br/>via søke-API / SPARQL"| DATAKAT
    PRIVATKAT -.->|"søk/API for<br/>datasett-metadata"| DATAKAT
    PRIVATKAT -.->|"hentar skjema:<br/>SHACL · JSON Schema ·<br/>JSON-LD-context · OWL"| GHPAGES2
    DATAPLATTFORM -.->|"hentar skjema for<br/>validering/typing"| GHPAGES2
    DATAPLATTFORM -.->|"importerer LinkML-skjema<br/>(tag-versjonert)"| RAWGH2
    APIGATEWAY -.->|"hentar skjema for<br/>API-kontrakt"| GHPAGES2

    classDef default fill:#000000,color:#ffffff,stroke:#ffffff;
    classDef ekstern fill:#3a0a0a,color:#ffffff,stroke:#e74c3c;
    classDef ci fill:#0a1f3a,color:#ffffff,stroke:#5b9bd5;
    classDef konsument fill:#2a0a3a,color:#ffffff,stroke:#9b59b6;
    classDef usynlig fill:none,stroke:none,color:transparent;
    class GHPAGES2,RAWGH2 ekstern
    class REPOCI ci
    class PRIVATKAT,DATAPLATTFORM,APIGATEWAY konsument
    class PADKAT,PADKON,PADEKS,ANCHOR2 usynlig

    style KATALOGAR fill:#000000,color:#ffffff,stroke:#ffffff
    style EKSTERNREPO fill:#000000,color:#ffffff,stroke:#ffffff
    style KONSUMENTER fill:#000000,color:#ffffff,stroke:#ffffff
```

## Forklaring av dei vesentlege delane

- **Kildeskjema** (`src/linkml/`) — LinkML-skjema organisert i eit
  importhierarki (sjå `CLAUDE.md` § "LinkML Importhierarki"): AP-NO-profilar
  og FAIR-metadata er ikkje-sjølvstendige byggeklossar som domenemodellane
  importerer. `begrepskatalog/` og `modellkatalog/` er spesialtilfelle som
  importerer AP-NO-profilar for å publisere til eksterne katalogar.
- **MCP-servere** — tre lokale containerbaserte MCP-servere lèt KI-assistentar
  generere skjemautkast frå JSON Schema, generere SKOS-begrepsutkast, og
  validere skjema/instansar mot policy-nivå, utan å forlate det lokale miljøet.
- **GitHub Actions** — validerer PR-ar, byggjer artefakt + portal ved push til
  `main`, byggjer/pushar container-images ved release-tag, og fangar
  valideringshistorikk ved release-please-versjonering.
- **Publiserte pull-punkt** — repoet **pullar aldri til, berre frå**: GitHub
  Pages er den publiserte portalen; GitHub Releases og
  `raw.githubusercontent.com` er stabile hente-punkt for skjema-import frå
  andre repo; GHCR distribuerer container-images.
- **Nasjonale katalogar** — publisering til Felles Begrepskatalog og Felles
  Datakatalog er **manuelle** steg gjort av eit menneske som følgjer
  rettleiingane i portalen — repoet pushar ikkje direkte til desse katalogane
  (jf. "Pull, ikkje push"-prinsippet i `CLAUDE.md`).
- **Eksternt repo** — andre repo kan bootstrappe seg sjølve med
  `bootstrap.sh` og importere AP-NO-profilar direkte via tag-baserte
  `raw.githubusercontent.com`-URL-ar, og validerer/genererer via dei same
  reusable GitHub Actions-workflowane som dette repoet eksponerer.
- **Konsumentar av Felles Datakatalog og publiserte skjema** — dette er
  framtidige/planlagde integrasjonar (sjå
  `specs/backlog/nasjonal-datamesh-arkitektur.md` for full vurdering), ikkje
  noko som er implementert i dette repoet i dag:
  - **KUDAF** (Sikt/HK-dir sitt datafellesskap for kunnskapssektoren) haustar
    datasett-metadata frå Felles Datakatalog sitt søk-API/SPARQL-endepunkt —
    same mønster som data.norge.no sjølv brukar for å hauste
    DCAT-AP-NO-metadata frå GitHub Pages. Repoet leverer altså data til KUDAF
    *indirekte*, via Felles Datakatalog som mellomlager/hub.
  - **Private datakatalogar** i verksemder kan søke/spørje Felles Datakatalog
    for datasett-metadata på same måte, og/eller hente skjemaartefaktar
    (SHACL, JSON Schema, JSON-LD-context, OWL) direkte frå GitHub Pages for å
    validere og typesette eigne data mot dei nasjonale profilane.
  - **Dataplattformar** i verksemder kan importere LinkML-skjema direkte via
    tag-versjonerte `raw.githubusercontent.com`-URL-ar (samme mekanisme som
    eksterne repo) for å bruke skjema i eigen pipeline, eller hente genererte
    artefaktar (JSON Schema, SHACL) frå GitHub Pages for validering.
  - **API-gateway** i verksemder kan hente JSON Schema/JSON-LD-context frå
    GitHub Pages for å validere API-kontrakta mot dei nasjonale profilane, og
    eksponerer data frå verksemda sin eigen dataplattform i samsvar med dei
    samme skjemaa.
  - Alle desse koplingane er **pull**: ingen av konsumentane mottek push frå
    dette repoet, i tråd med "Pull, ikkje push"-prinsippet.
