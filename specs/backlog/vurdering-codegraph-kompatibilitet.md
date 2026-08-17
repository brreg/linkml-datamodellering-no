# Vurdering: CodeGraph-kompatibilitet med repoet

**Kjelde:** [github.com/colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
**Dato vurdert:** 2026-08-10 (utvida same dato)
**Konklusjon:** Teknisk det mest podman-kompatible av dei tre vurderte kodebase-verktøya
(SocratiCode, Code-to-Knowledge-Graph, CodeGraph) — men framleis avgrensa reell verdi for
dette repoet, sidan YAML ikkje er eit strukturelt støtta språk.
**Status:** Brukaren har bestemt seg for å pilotere verktøyet i ein eigen branch, uavhengig
av verdivurderinga over. Sjå «Pilotplan» og full installasjonsbeskriving nedanfor.

---

## Bakgrunn

CodeGraph er eit MIT-lisensiert "codebase intelligence"-verktøy: ein nativ **Rust-kjerne**
med innebygde tree-sitter-grammatikkar som byggjer ein SQLite-basert kunnskapsgraf
(symbol, kallkantar, importar) for 20+ språk, eksponert som CLI og MCP-tenar
(`codegraph_explore`). 65 700+ GitHub-stjerner. Brukaren ba om tilsvarande vurdering som
for SocratiCode og Code-to-Knowledge-Graph, inkludert lisensvurdering.

## Funn

### 1. Installasjonsmodell: ingen Node.js/Docker påkravd, men framleis eit lokalt CLI-installasjonsskript

Standardinstallasjon er eit shell-/PowerShell-skript køyrt direkte på vertsmaskina:

```bash
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
```

Dette hentar ein **sjølvstendig, ferdigbygd binær** (bundla Node-runtime i den native
pakken — "No Node.js required" for denne installasjonsmåten) og legg `codegraph` på
`PATH`. Eit `npm i -g @colbymchenry/codegraph`-alternativ finst også for dei som har Node
frå før. Uansett metode er dette eit **installasjonssteg på vertsmaskina**, i strid med
CLAUDE.md sitt prinsipp *"Ingen avhengigheter skal installeres lokalt."* — same
grunnleggjande innvending som mot SocratiCode sin `npx`-modell, sjølv om denne varianten
ikkje krev at Node.js er installert frå før.

### 2. Ingen Docker-avhengigheit i det heile — arkitektonisk enklare enn SocratiCode

I motsetnad til SocratiCode har CodeGraph **ingen eksterne sidecar-tenester** (ingen
Qdrant, ingen Ollama, ingen vektordatabase). Alt lagrast lokalt i éin SQLite-fil
(`.codegraph/codegraph.db`) med FTS5 fulltekstsøk. README nemner ingen Docker- eller
podman-avhengigheit noko stad. Dette gjer det **arkitektonisk enklare å containerisere
sjølv** enn både SocratiCode (Docker-styrte sidecars) og Code-to-Knowledge-Graph (JVM/
Gradle + VS Code LSP-avhengigheit) — det er berre éin binær som treng eitt volummontert
katalog for persistens.

### 3. Manuell MCP-oppsett utan den globale installatoren er dokumentert og fungerer med repoets mønster

README sin «Manual Setup»-boks viser den rå MCP-kommandoen direkte, utan å gå via den
globale `codegraph install`-vegvisaren (som elles skriv til `~/.claude.json` på
brukarnivå, tilsvarande kritikken mot SocratiCode sitt plugin-spor):

```json
{
  "mcpServers": {
    "codegraph": {
      "type": "stdio",
      "command": "codegraph",
      "args": ["serve", "--mcp"]
    }
  }
}
```

Sidan `codegraph serve --mcp` er ein reint lokal stdio-prosess utan noka nettverks- eller
Docker-avhengigheit, kan denne kommandoen i prinsippet bytast ut med ein
`podman run -i --rm -v "$REPO:/repo:ro" -v "$REPO/.codegraph:/repo/.codegraph:rw"
mcp-codegraph codegraph serve --mcp` i repoet sin eigen `.mcp.json` — **same mønster som
dei tre eksisterande MCP-tenarane**, utan å røre den globale agentkonfigurasjonen i
`~/.claude.json`. Dette krev framleis ein ny `Dockerfile.mcp-codegraph` (t.d.
`FROM node:20-alpine`, `RUN npm install -g @colbymchenry/codegraph` i byggjesteget,
non-root-brukar — same struktur som `Dockerfile.mcp-linkml`), men **ikkje** noka ny
langlevd bakgrunnsteneste utover sjølve MCP-tenar-containeren — fil-overvakinga
(auto-sync) køyrer inni same prosess som MCP-serveren, så ho lever og døyr med same
`podman run -i --rm`-økt som dei eksisterande tre serverane, i motsetnad til
SocratiCode sine separat langlevde Qdrant/Ollama-containerar.

### 4. YAML er ikkje eit strukturelt støtta språk — kjerneverdien råkar ikkje repoets faktiske innhald

README sin «Language Support»-liste (20+ ikon: TypeScript, Python, Go, Rust, Java,
C#, PHP, Ruby, C/C++, Swift, Kotlin, Dart, Terraform, Nix, m.fl.) **inneheld ikkje
YAML**. Eit `grep` etter "yaml" i heile READMEen gav berre eitt reelt treff — ei
Drupal-spesifikk rammeverkskonvensjon (`*.routing.yml`), ikkje generell
YAML-strukturstøtte. Sidan dette repoet i hovudsak består av LinkML-skjema (`.yaml`),
ville CodeGraph **ikkje kunne byggje ein meiningsfull kunnskapsgraf over sjølve
skjemainnhaldet** — kjerneverdien (symbol/kallgraf/blast-radius) gjeld berre den vesle
mengda faktisk kjeldekode i repoet (`src/mcp-linkml-*/`sine Python-filer, Make/shell).
Dette er eit meir konkret og direkte stadfesta funn enn den tilsvarande
domenevurderinga for dei to andre verktøya.

### 5. Telemetri på som standard

CodeGraph samlar anonym, lokalt aggregert bruksstatistikk (kva verktøy/kommandoar vert
brukte, kva språk vert indekserte) og sender dette til eit offentleg ingest-endepunkt —
**ikkje** kode, filstiar, symbolnavn, spørjingar eller IP-adresser, ifølgje
`TELEMETRY.md`. Kan skruast av med `codegraph telemetry off`,
`CODEGRAPH_TELEMETRY=0`, eller den generelle konvensjonen `DO_NOT_TRACK=1`. Dette bryt
ikkje noko eksplisitt CLAUDE.md-prinsipp, men bør deaktiverast via miljøvariabel i
`.mcp.json` dersom verktøyet nokon gong vert teke i bruk, i tråd med repoet sin generelle
haldning om å avgrense unødvendige eksterne avhengigheiter.

## Lisensvurdering

**Lisens:** [MIT License](https://github.com/colbymchenry/codegraph/blob/main/LICENSE) —
stadfesta både i GitHub-metadata og i `LICENSE`-fila (Copyright (c) 2026 Colby Mchenry).

MIT er den mest permissive av dei tre lisensane vurderte i denne serien
(samanlikna med SocratiCode sin AGPL-3.0 og Code-to-Knowledge-Graph sin MPL-2.0):

- **Ingen copyleft-plikter i det heile** — verken fil-nivå (som MPL) eller nettverks-/
  heile-verket-nivå (som AGPL). Koden kan brukast, endrast, kombinerast og distribuerast
  fritt, inkludert i proprietær eller anna-lisensiert samanheng.
- **Einaste krav:** behalde opphavsrett- og lisensmerknaden i kopiar av programvara.
  Dette dekkjast enkelt med ei attribution-oppføring i `mkdocs/docs/om.md`, i tråd med
  CLAUDE.md sitt punkt «Nye verktøyavhengigheiter», dersom eit `mcp-codegraph`-bilete
  nokon gong vert bunta inn i eit publisert containerbilete.
- **Inga skilnad mellom lokal bruk og publisering** — i motsetnad til SocratiCode
  (der publisering til `ghcr.io/brreg/*` reiste ei open juridisk gråsone rundt AGPL),
  ville det å byggje og publisere eit `mcp-codegraph`-bilete etter same mønster som dei
  tre eksisterande MCP-bileta vore **lisensmessig trivielt** — berre éi
  attribution-linje, ingen "conveying"-vurdering, ingen grunn til å halde biletet
  utanfor `release.yml`.

**Konklusjon lisens:** MIT er **fullt kompatibelt** og det klart enklaste lisensbiletet av
dei tre verktøya vurderte i denne serien. Lisensen er **ikkje** eit hinder, korkje for
lokal bruk eller for eventuell publisering.

## Samanlikning med dei to tidlegare vurderte verktøya

| | SocratiCode | Code-to-Knowledge-Graph | CodeGraph |
|---|---|---|---|
| Lisens | AGPL-3.0 (problematisk ved publisering) | MPL-2.0 (uproblematisk) | **MIT (uproblematisk)** |
| Docker-avhengigheit | Ja (Qdrant/Ollama) | Nei, men JVM/Gradle + VS Code LSP | **Nei** |
| Podman-containeriserbart | Ja, med `QDRANT_MODE`/`OLLAMA_MODE=external` + to nye langlevde containerar | Krev nytt byggøkosystem frå botnen | **Ja, enklast — éin container, same driftsmønster som eksisterande MCP-tenarar** |
| Manuell MCP-config utan global installer | Ja (same `npx`-kommando uansett) | N/A (ikkje eit MCP-verktøy) | **Ja, dokumentert direkte i README** |
| Dekkjer repoets faktiske innhald (YAML) | Marginalt (generisk kodesøk) | Marginalt (kallgrafar for tradisjonell kode) | **Nei — YAML er ikkje eit støtta språk i det heile** |

## Konklusjon

CodeGraph er **det teknisk enklaste og lisensmessig tryggaste** av dei tre vurderte
verktøya å gjere podman-kompatibelt: ingen Docker-avhengigheit, ingen nye langlevde
sidecar-tenester, ein dokumentert manuell MCP-kommando som passar rett inn i repoet sitt
eksisterande `.mcp.json`-mønster, og ein MIT-lisens utan nokon reservasjon mot
publisering. Same grunnleggjande innvending som mot SocratiCode (installasjonsskriptet
køyrer på vertsmaskina, ikkje i container) løysast likt: byggje ein eigen
`Dockerfile.mcp-codegraph` og registrere `codegraph serve --mcp` i `.mcp.json` i staden
for å bruke den globale installatoren.

Det avgjerande motargumentet er likevel **verdien**, ikkje gjennomførbarheita: YAML er
uttrykkeleg ikkje eit strukturelt støtta språk, så CodeGraph sin kjernefunksjon (symbol-
/kallgraf-basert kodeforståing) ville ikkje omfatte hovuddelen av repoets innhald
(LinkML-skjema). Verktøyet ville i beste fall gje marginal verdi for den vesle mengda
Python/shell-kode i `src/mcp-linkml-*/` og `make/` — ei mengd som alt er godt dokumentert
manuelt (arkitekturoversikt, COMMANDS.md) og handterleg med eksisterande
Grep/Glob/Explore-agent-verktøy i Claude Code.

**Tilråding (opphavleg):** Ikkje adopter CodeGraph i dette repoet no. Dersom repoet sin
Python-kodebase (MCP-serverane) skulle vekse vesentleg i omfang og kompleksitet, er
dette verktøyet — i motsetnad til dei to andre vurderte — teknisk og lisensmessig klart
til å takast i bruk utan dei atterhalda som gjaldt for SocratiCode og
Code-to-Knowledge-Graph, ved å følgje same containeriseringsmønster som dei tre
eksisterande MCP-tenarane.

**Oppdatering:** Brukaren ønskjer å teste dette sjølv, i ein eigen branch, uavhengig av
verditilrådinga over — eit rimeleg pilotval nettopp *fordi* punkt 3 i tiltaksvurderinga
synte at det er den lågaste-kostnad-varianten av dei tre verktøya å prøve ut. Full
installasjonsbeskriving følgjer under.

---

## Pilotplan: testing i eigen branch

**Merk:** LLM skal aldri køyre `git`-kommandoar som endrar versjonskontroll-tilstand
(CLAUDE.md, «Aldri commit eller push»). Branch-oppretting, commit og eventuell sletting
av branchen er difor **brukaren sitt ansvar**. Alt under er filinnhald og kommandoar
brukaren (eller ein agent på brukaren sin instruks) kan følgje steg for steg.

### Føresetnad — opprett branchen

```bash
git checkout -b pilot/codegraph-mcp
```

### Oversikt over endringane

Pilotforsøket legg til **fem nye filer/endringar**, alle isolerte frå eksisterande
MCP-tenarar og enkle å reversere fullstendig (sjå «Reversering» heilt nedst):

1. `src/assets/containers/Dockerfile.mcp-codegraph` — ny, dedikert Dockerfile (ikkje lagt
   inn i det delte `Dockerfile.mcp-linkml`, sidan CodeGraph er Node-basert og eit
   ureversibelt pilotforsøk — held han lett å fjerne i éin operasjon)
2. `make/61-mcp-codegraph.mk` — nytt Makefile-fragment med build/init/status/run/smoke-mål
3. `.mcp.json` — ny `codegraph`-oppføring, same mønster som dei tre eksisterande
4. `CLAUDE.md` — eit nytt, markørbasert instruksjonsavsnitt som lærer agenten (inkludert
   subagentar) å bruke `codegraph_explore` konsekvent — utan dette har CodeGraph sitt
   eige måldata vist at subagentar berre plukkar opp verktøyet i ~1 av 9 køyringar
   (sjå «Agent-instruksjonar i CLAUDE.md» under)
5. `.gitignore` — ny linje for `.codegraph/` (lokal indeks-database, skal ikkje committast)

### 1 — Dockerfile

Opprett `src/assets/containers/Dockerfile.mcp-codegraph`:

```dockerfile
# Dockerfile.mcp-codegraph — PILOTFORSØK: CodeGraph MCP-server
# (kodebase-kunnskapsgraf, symbol-/kallgraf-basert kodeforståing).
# Sjå specs/done/vurdering-codegraph-kompatibilitet.md for grunngjeving og avgrensingar
# (YAML er ikkje eit strukturelt støtta språk — verdien er avgrensa til Python/shell-koden
# i repoet, t.d. src/mcp-linkml-*/).
#
# Node 22 kravd for node:sqlite (>=22.5) når pakka køyrer under vanleg npm-installasjon
# (ikkje CodeGraph sin sjølvstendige, bundla binærdistribusjon) — sjå CodeGraph sin
# README § "Embedding requirements". package.json sitt engines-felt tillèt node >=20 <25.

FROM node:22-alpine AS builder
RUN npm install -g --prefix /install @colbymchenry/codegraph@1.5.0

FROM node:22-alpine AS runtime
ENV NODE_ENV=production
COPY --from=builder /install /usr/local
RUN adduser -D codegraph
USER codegraph
WORKDIR /repo
CMD ["codegraph", "serve", "--mcp"]
```

**Versjonspinning:** `@colbymchenry/codegraph@1.5.0` er siste versjon stadfesta via
`gh api repos/colbymchenry/codegraph/contents/package.json` då denne specen vart
skriven. Oppdater versjonsnummeret eksplisitt (aldri `@latest`) dersom du vil teste ein
nyare versjon — same reproduserbarheitsprinsipp som `linkml>=1.11.1,<2.0.0`-pinninga i
`Dockerfile.mcp-linkml`.

### 2 — Makefile-fragment

Opprett `make/61-mcp-codegraph.mk`:

```make
# ==============================================================================
# make/61-mcp-codegraph.mk
#
# PILOTFORSØK — CodeGraph MCP-server (kodebase-kunnskapsgraf), testa i eigen
# branch (pilot/codegraph-mcp). Sjå
# specs/done/vurdering-codegraph-kompatibilitet.md for grunngjeving og
# avgrensingar.
#
# Reversering: slett denne fila, src/assets/containers/Dockerfile.mcp-codegraph,
# codegraph-oppføringa i .mcp.json, linja i .gitignore, `include`-linja i
# Makefile, og `podman rmi mcp-codegraph` + `rm -rf .codegraph/`.
# ==============================================================================

CODEGRAPH_DIR   := src/assets/containers
CODEGRAPH_IMAGE := mcp-codegraph
CODEGRAPH_RUN   := podman run -i --rm \
  -v "$(CURDIR):/repo:ro" \
  -v "$(CURDIR)/.codegraph:/repo/.codegraph:rw" \
  -e CODEGRAPH_TELEMETRY=0 \
  -e DO_NOT_TRACK=1 \
  -w /repo

build-docker-mcp-codegraph: ## [PILOT] Bygg container-image for CodeGraph MCP-serveren
	$(call print_header,build-docker-mcp-codegraph)
	@podman build --format docker -f $(CODEGRAPH_DIR)/Dockerfile.mcp-codegraph -t $(CODEGRAPH_IMAGE) .

codegraph-init: build-docker-mcp-codegraph ## [PILOT] Bygg/gjenbygg CodeGraph-indeksen for repoet
	$(call print_header,codegraph-init)
	@mkdir -p .codegraph
	@$(CODEGRAPH_RUN) $(CODEGRAPH_IMAGE) codegraph init /repo

codegraph-status: build-docker-mcp-codegraph ## [PILOT] Vis status for CodeGraph-indeksen
	@$(CODEGRAPH_RUN) $(CODEGRAPH_IMAGE) codegraph status /repo

mcp-codegraph-run: build-docker-mcp-codegraph ## [PILOT] Start CodeGraph MCP-serveren interaktivt (JSON-RPC på stdin/stdout)
	$(call print_header,mcp-codegraph-run)
	@$(CODEGRAPH_RUN) $(CODEGRAPH_IMAGE)

mcp-codegraph-smoke: build-docker-mcp-codegraph ## [PILOT] Røyktest CodeGraph MCP-serveren med ein initialize-melding
	$(call print_header,mcp-codegraph-smoke)
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(CODEGRAPH_RUN) $(CODEGRAPH_IMAGE)

.PHONY: build-docker-mcp-codegraph codegraph-init codegraph-status mcp-codegraph-run mcp-codegraph-smoke
```

Registrer fragmentet i root-`Makefile`, rett etter den eksisterande MCP-inkluderinga:

```diff
 include make/60-mcp.mk
+include make/61-mcp-codegraph.mk
 include make/70-scaffolding.mk
```

### 3 — `.mcp.json`

Legg til ei ny `codegraph`-oppføring i `.mcp.json`, same mønster (bash-wrapper som løyser
repo-rota via `git rev-parse`) som dei tre eksisterande oppføringane:

```json
{
  "mcpServers": {
    "linkml-modell-utkast": { "...": "uendra" },
    "linkml-validator": { "...": "uendra" },
    "linkml-begrep-utkast": { "...": "uendra" },
    "codegraph": {
      "type": "stdio",
      "command": "bash",
      "args": [
        "-c",
        "REPO=$(git rev-parse --show-toplevel) && podman run -i --rm -v \"$REPO:/repo:ro\" -v \"$REPO/.codegraph:/repo/.codegraph:rw\" -e CODEGRAPH_TELEMETRY=0 -e DO_NOT_TRACK=1 -w /repo mcp-codegraph"
      ],
      "env": {}
    }
  }
}
```

(Dei tre `"..."`-linjene over er berre plasshaldarar for å visualisere kvar den nye
oppføringa går inn — behald dei tre eksisterande blokkene uendra i den faktiske fila.)

### 4 — Agent-instruksjonar i CLAUDE.md

**Kvifor dette steget er nødvendig:** MCP-serveren si eiga `initialize`-melding gjev
hovudagenten (Claude Code-økta sjølv) bruksrettleiing automatisk — det krev ingen endring
i CLAUDE.md. Men CodeGraph sine eigne utviklarar har målt at denne automatikken **ikkje**
når fram til (a) Task-verktøy-subagentar, som får CLAUDE.md i konteksten sin men ikkje
MCP-en sine `initialize`-instruksjonar, og (b) verktøy utan MCP-klient. Utan eit eige
avsnitt i CLAUDE.md brukte subagentar CodeGraph i **~1 av 9** køyringar på ei tvinga
delegeringsoppgåve i CodeGraph sin eigen målserie — med avsnittet, konsekvent kvar gong.
Sidan dette repoet bruker Explore-agenten og Task-verktøyet aktivt (jf. den generelle
Claude Code-instruksen om å bruke Explore for brei kodebase-utforsking), er denne gapen
direkte relevant her.

Den offisielle installatoren (`codegraph install`) skriv normalt eit lite,
markørbasert avsnitt inn i `CLAUDE.md`/`AGENTS.md` automatisk. Sidan pilotoppsettet
**ikkje** brukar denne installatoren (jf. steg 3 — vi wirar MCP-serveren manuelt for å
halde oss innanfor podman-mønsteret), må avsnittet leggjast inn for hand. Innhaldet under
er henta **ordrett** frå CodeGraph sin eigen kjeldekode
(`src/installer/instructions-template.ts`, konstanten `CODEGRAPH_INSTRUCTIONS_BLOCK`) —
same tekst installatoren sjølv ville skrive:

```markdown
<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
```

**Plassering:** Legg avsnittet til heilt sist i `CLAUDE.md`, som eit nytt `##`-avsnitt.

**Viktig — behald teksten på engelsk, uendra:** Resten av `CLAUDE.md` følgjer
nynorsk-konvensjonen (jf. § «Skriftspråk»), men dette blokka bør **ikkje** omsetjast.
Grunnen er teknisk, ikkje stilistisk: blokka er markør-avgrensa
(`<!-- CODEGRAPH_START -->` / `<!-- CODEGRAPH_END -->`) nettopp fordi CodeGraph sin eigen
installatorlogikk kan finne, oppdatere og fjerne henne automatisk (t.d. ved
`codegraph upgrade` eller `codegraph uninstall`) — dersom nokon seinare køyrer den
offisielle installatoren i repoet, skriv han denne nøyaktige engelske teksten uansett.
Ei omsett utgåve ville anten verte overskriven utan varsel, eller stå att som eit
duplikat dersom markørane ikkje lenger matcha. Dette er ein tilsvarande, medviten
avgrensa unntak frå nynorsk-regelen som camelCase-unntaket for FINT-skjema — verktøyet sitt
eige format har forrang framfor repoet sin generelle stilkonvensjon for denne spesifikke,
maskinlesbare blokka.

### 5 — `.gitignore`

Legg til denne linja (indeksdatabasen er eit lokalt byggeartefakt, akkurat som
`generated/`, og skal ikkje committast):

```diff
 generated/
+.codegraph/
 config.mk
```

### Telemetri — fullstendig avstenging og verifisering

Brukaren spurde eksplisitt om kva som må gjerast for å skru av telemetri. Kort svar:
**steg 1-3 over gjer dette allereie** (miljøvariablane er sette tre stader —
`Dockerfile.mcp-codegraph` sitt runtime-miljø er ikkje eitt av dei; dei vert i staden
injiserte ved *køyretid* via `CODEGRAPH_RUN` i steg 2 og `.mcp.json` i steg 3, slik at
dei alltid gjeld uansett kven som startar containeren). Denne seksjonen dokumenterer
**kvifor** det er nok, henta frå CodeGraph sin eigen `TELEMETRY.md`:

- `DO_NOT_TRACK=1` er "the cross-tool standard — always honored", og `CODEGRAPH_TELEMETRY=0`
  er det verktøyspesifikke alternativet — **begge** er alt sette i `CODEGRAPH_RUN`
  (steg 2) og i `.mcp.json`-oppføringa (steg 3). Anten av dei åleine held; me set begge
  for redundans, sidan dei to køyrevegane (Makefile-mål vs. Claude Code-oppstart) er
  uavhengige av kvarandre.
- Ifølgje `TELEMETRY.md`: **"Off means off: when disabled, CodeGraph records nothing,
  opens no connection to the telemetry endpoint, and sends no 'opted out' ping."** — dette
  er ikkje berre eit lokalt filter; sjølve nettverkskallet vert aldri gjort.
- **Separat frå telemetri** finst ein bakgrunnssjekk mot GitHub for nye versjonar (høgst
  éin gong dagleg) — reint versjonsnummer, ingen brukar-/maskindata. `DO_NOT_TRACK=1`
  slår av denne òg, men for å gjere det eksplisitt (og sidan pilotforsøket uansett
  byggjer eit fastpinna versjonsnummer i Dockerfile — ein oppdateringssjekk gjev ingen
  verdi her) er `CODEGRAPH_NO_UPDATE_CHECK=1` lagt til begge stadene under.

Oppdater `CODEGRAPH_RUN` i `make/61-mcp-codegraph.mk` (steg 2) og kommandostrengen i
`.mcp.json` (steg 3) med denne tredje variabelen:

```diff
 CODEGRAPH_RUN   := podman run -i --rm \
   -v "$(CURDIR):/repo:ro" \
   -v "$(CURDIR)/.codegraph:/repo/.codegraph:rw" \
   -e CODEGRAPH_TELEMETRY=0 \
   -e DO_NOT_TRACK=1 \
+  -e CODEGRAPH_NO_UPDATE_CHECK=1 \
   -w /repo
```

```diff
-        "REPO=$(git rev-parse --show-toplevel) && podman run -i --rm -v \"$REPO:/repo:ro\" -v \"$REPO/.codegraph:/repo/.codegraph:rw\" -e CODEGRAPH_TELEMETRY=0 -e DO_NOT_TRACK=1 -w /repo mcp-codegraph"
+        "REPO=$(git rev-parse --show-toplevel) && podman run -i --rm -v \"$REPO:/repo:ro\" -v \"$REPO/.codegraph:/repo/.codegraph:rw\" -e CODEGRAPH_TELEMETRY=0 -e DO_NOT_TRACK=1 -e CODEGRAPH_NO_UPDATE_CHECK=1 -w /repo mcp-codegraph"
```

**Verifisering:** `codegraph telemetry status` viser gjeldande tilstand og kva som
avgjorde han. Sidan pilotoppsettet aldri køyrer `codegraph telemetry off` (som ville
persistert eit val til `~/.codegraph/telemetry.json` — ein fil som uansett ikkje
overlever ein `--rm`-container), stør telemetri-avstenginga seg **utelukkande** på
miljøvariablane ved kvar køyring, noko `status`-kommandoen stadfestar:

```bash
podman run --rm -e CODEGRAPH_TELEMETRY=0 -e DO_NOT_TRACK=1 mcp-codegraph codegraph telemetry status
```

Forvent output som stadfestar at telemetri er av og at kjelda er miljøvariabelen (ikkje
ei persistert fil-innstilling).

### 6 — Bygg og initialiser

```bash
make build-docker-mcp-codegraph
make codegraph-init      # oppretter .codegraph/ og byggjer full indeks
make codegraph-status    # stadfest at indekseringa fullførte
```

### 7 — Røyktest MCP-serveren isolert (før du koplar han til Claude Code)

```bash
make mcp-codegraph-smoke
```

Forvent eit JSON-RPC `initialize`-svar med `serverInfo.name` lik noko i retning
`"codegraph"` og ei liste over tilgjengelege verktøy (`codegraph_explore` m.fl.) i
`capabilities`. Feilar dette steget, ikkje gå vidare til steg 8 — feilsøk her fyrst.

### 8 — Kopl til og verifiser i Claude Code

```bash
claude mcp list       # stadfest at "codegraph" er registrert frå .mcp.json
```

Start ein ny Claude Code-økt i repoet (MCP-serverar vert lasta ved sesjonsstart), og be
agenten teste verktøyet direkte, t.d.:

> "Bruk codegraph_explore til å forklare korleis `src/mcp-linkml-begrep-utkast/server.py`
> heng saman med `generator.py`"

Sidan YAML ikkje er strukturelt støtta (jf. «Funn 4» over), test **berre** mot
Python-/shell-innhaldet i `src/mcp-linkml-*/` og `make/` — ikkje forvent meiningsfulle
resultat mot `.yaml`-skjemafiler.

**Verifiser at subagentar òg brukar verktøyet** (dette er heile poenget med steg 4 —
CLAUDE.md-avsnittet): be hovudagenten delegere ei kodeutforskingsoppgåve eksplisitt til
Explore-agenten eller via Task-verktøyet, t.d.:

> "Bruk ein subagent til å finne ut korleis `validator.py` heng saman med resten av
> `mcp-linkml-modell-utkast`"

Undersøk deretter (t.d. via transkriptet) om subagenten faktisk kalla `codegraph_explore`
i staden for å falle tilbake til Grep/Read. Dersom subagenten ikkje brukar verktøyet,
stadfest at `<!-- CODEGRAPH_START -->`-avsnittet frå steg 4 faktisk vart lagra i
`CLAUDE.md` og at det ligg **innanfor** dei filgrensene subagenten får context frå.

### Feilsøking

| Symptom | Sannsynleg årsak | Fiks |
|---|---|---|
| `codegraph-init` feilar med "Permission denied" mot `.codegraph/` | UID-mismatch mellom containerbrukaren `codegraph` (alpine sin fyrste `adduser -D`, typisk UID 1000) og vertsbrukaren | Køyr `podman unshare chown -R 1000:1000 .codegraph` på verten, eller legg til `--user "$(id -u):$(id -g)"` i `CODEGRAPH_RUN` |
| MCP-serveren startar, men `codegraph_explore` returnerer "no index found" | `.codegraph/` vart ikkje montert inn, eller `codegraph-init` vart aldri køyrt | Stadfest at `.codegraph/`-katalogen finst i repo-rota og inneheld `codegraph.db`; køyr `make codegraph-init` på nytt |
| Uventa nettverkstrafikk / du vil dobbeltsjekke at telemetri er av | `CODEGRAPH_TELEMETRY`/`DO_NOT_TRACK`/`CODEGRAPH_NO_UPDATE_CHECK` vart ikkje ført gjennom | Sjå eige avsnitt «Telemetri — fullstendig avstenging og verifisering» over; køyr `codegraph telemetry status`-kommandoen der for å stadfeste |
| `claude mcp list` viser ikkje `codegraph` | `.mcp.json` er ugyldig JSON, eller Claude Code-økta vart ikkje restarta etter endringa | Valider JSON-en (`python3 -m json.tool .mcp.json`), start ein heilt ny økt |
| Hovudagenten brukar verktøyet, men subagentar (Task/Explore) gjer det ikkje | CLAUDE.md-avsnittet frå steg 4 manglar, eller ligg utanfor det subagenten les | Stadfest at `<!-- CODEGRAPH_START -->`-blokka faktisk vart lagt til i `CLAUDE.md` og er intakt |

### Reversering (dersom pilotforsøket ikkje held fram)

```bash
rm src/assets/containers/Dockerfile.mcp-codegraph
rm make/61-mcp-codegraph.mk
rm -rf .codegraph/
podman rmi mcp-codegraph
```

Fjern deretter manuelt: `include make/61-mcp-codegraph.mk`-linja i root-`Makefile`,
`codegraph`-oppføringa i `.mcp.json`, `.codegraph/`-linja i `.gitignore`, og heile
`<!-- CODEGRAPH_START -->` … `<!-- CODEGRAPH_END -->`-blokka i `CLAUDE.md` (markørane
gjer denne siste fjerninga eintydig — alt mellom dei kan slettast trygt). Brukaren
byter så tilbake til hovudbranchen og slettar `pilot/codegraph-mcp` sjølv (git-operasjon,
utanfor LLM sitt mandat).

---

## Utført

Vurderinga er fullført basert på gjennomgang av CodeGraph sin README (Get Started,
Language Support, How It Works, MCP Tools, Configuration, Telemetry, Verified releases,
Supported Platforms, License-seksjonane), stadfesting av `LICENSE`-fila via `gh api`, og
samanlikning med repoets eksisterande MCP-oppsett (`.mcp.json`,
`src/assets/containers/Dockerfile.mcp-linkml`) og førande prinsipp (`CLAUDE.md`). Ingen
kodeendringar er gjort — dette er ei rein kartleggings-/vurderingsoppgåve.

**Pilotplan (denne utvidinga)** fullført basert på: (1) stadfesting av eksakt versjon og
`engines`-krav via `gh api repos/colbymchenry/codegraph/contents/package.json`
(`@colbymchenry/codegraph@1.5.0`, `node >=20.0.0 <25.0.0`), (2) gjennomgang av
`make/60-mcp.mk`, `make/00-settings.mk`, `make/01-containers.mk` og root-`Makefile` for å
kopiere dei eksisterande MCP-konvensjonane presist (variabelnavn, `podman run`-mønster med
delt `:ro`-repo-mount + smalare `:rw`-undermontering, `print_header`-bruk,
`.PHONY`-registrering), og (3) samanlikning med `.mcp.json` sin eksisterande
`bash -c`-wrapper-stil for dei tre andre serverane. Ingen filer er endra i repoet — heile
installasjonsbeskrivinga er skriven som klar-til-bruk innhald i denne specen, sidan
branch-oppretting og faktisk filskriving i ein ny branch er brukaren sitt eige steg (jf.
CLAUDE.md sitt forbod mot at LLM utfører git-operasjonar).

**CLAUDE.md-instruksjonar og fullstendig telemetriavstenging (denne utvidinga)**
fullført basert på: (1) henting av `src/mcp/server-instructions.ts` frå CodeGraph-repoet,
som stadfesta at hovudagenten alt får bruksrettleiing automatisk via MCP sin
`initialize`-respons, (2) henting av `src/installer/instructions-template.ts` — den
**ordrette** kjelda til det markørbaserte `CODEGRAPH_START`/`CODEGRAPH_END`-avsnittet
lagt inn i steg 4, saman med grunngjevinga i kjeldekodekommentarane for kvifor avsnittet
finst (målt subagent-brukstal: ~1/9 utan, konsekvent med), og (3) full lesing av
`TELEMETRY.md` for å stadfeste at `CODEGRAPH_TELEMETRY=0` + `DO_NOT_TRACK=1` er
tilstrekkeleg og at det ikkje krevst noka persistert tilstandsfil
(`~/.codegraph/telemetry.json`) sidan miljøvariablane vert sette ved kvar containerstart,
pluss identifisering av den separate `CODEGRAPH_NO_UPDATE_CHECK`-variabelen for
oppdateringssjekken. Framleis ingen filer endra i repoet — alt er spec-innhald klart til
bruk når brukaren sjølv opprettar piloteringsbranchen.
