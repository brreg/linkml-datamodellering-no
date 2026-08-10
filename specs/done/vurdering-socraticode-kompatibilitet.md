# Vurdering: SocratiCode-kompatibilitet med repoet

**Kjelde:** [github.com/giancarloerra/socraticode](https://github.com/giancarloerra/SocratiCode)
**Dato vurdert:** 2026-08-10 (utvida same dato)
**Konklusjon (opphavleg):** Ikkje kompatibelt — tilrådd ikkje adoptert
**Konklusjon (etter tiltaksvurdering):** Teknisk mogleg å gjere podman-kompatibelt via
eigen `.mcp.json`-integrasjon (same mønster som dei tre eksisterande MCP-tenarane) —
men **ikkje** via Claude Code-plugin-sporet, som viser seg å vere identisk med
npx-sporet. Sjå «Tiltaksvurdering» og «Ny anbefaling» nedanfor.
**Konklusjon (etter utvida lisensvurdering):** AGPL-3.0 er **ikkje eit hinder** dersom
det eigenbygde biletet held seg strengt lokalt (aldri publisert) — men **vert** eit
reelt, uavklart spørsmål dersom det nokon gong vert publisert til `ghcr.io/brreg/*`
etter same mønster som dei tre andre MCP-bileta. Sjå «Lisensvurdering (utvida)» nedanfor.

---

## Bakgrunn

SocratiCode er eit open-source "codebase intelligence"-verktøy for AI-assistentar: hybrid
semantisk + BM25-kodesøk, polyglot avhengigheitsgraf, symbol-nivå impact-analyse og
call-flow-sporing, retta mot store (dokumentert opp til ~40 mill. linjer) fleirspråklege
kodebasar. Det distribuerast som eit MCP-verktøy/Claude Code-plugin. Brukaren ba om ei
vurdering av om det er kompatibelt med dette repoet.

## Funn

### 1. Installasjonsmodell krev lokale avhengigheiter

Standard installasjon er `npx -y socraticode` (MCP-config) eller
`claude plugin install socraticode@socraticode`. Begge krev **Node.js 18+ installert
lokalt** — MCP-tenaren køyrer direkte på vertsmaskina via `npx`, ikkje i ein container.
Dette bryt CLAUDE.md sitt prinsipp: *"Ingen avhengigheter skal installeres lokalt. Alt
skal kjøres som containere med podman i WSL2."*

### 2. Container-motor er Docker, ikkje podman

SocratiCode sin standard `managed`-modus krev ein køyrande **Docker**-daemon for
automatisk å styre `socraticode-qdrant`- og `socraticode-ollama`-containerane (pull image,
start/stopp, persistente volum, `--restart unless-stopped`). Verktøyet har ingen
dokumentert støtte for podman.

Til samanlikning er alle tre eksisterande MCP-tenarane i dette repoet
(`.mcp.json`: `linkml-modell-utkast`, `linkml-validator`, `linkml-begrep-utkast`) 100 %
podman-baserte — kvar startast som `podman run -i --rm ...` med eksplisitte
read-only/read-write mount, utan noka avhengigheit til Docker eller Node.js på
vertsmaskina. SocratiCode sin installasjonsflyt er ikkje forenleg med dette mønsteret utan
ei ustøtta workaround (t.d. podman sin Docker-kompatible socket).

### 3. Anna driftsmodell enn repoets MCP-tenarar

Repoets MCP-tenarar er eingongs stdio-prosessar (`podman run -i --rm`, startar/stoppar
per kall). SocratiCode køyrer derimot langvarige bakgrunnscontainerar
(fil-watcher + inkrementell indeksering, containerar med `--restart unless-stopped`) —
ein vedvarande infrastruktur-modell som ikkje finst andre stader i repoet.

### 4. Funksjonelt fokus er urelatert til repoets domene

Repoet er eit avgrensa sett LinkML-skjema (YAML) med genererte artefakter — ikkje ein
stor programvare-kodebase med komplekse kall-grafar på tvers av språk. SocratiCode sin
kjerneverdi (symbol-nivå impact-analyse, call-flow-sporing, avhengigheitsgraf for
polyglot kode) er bygd for tradisjonell kildekode og gjev marginal verdi for eit
skjemadrive repo av denne storleiken. Repoet har allereie eit fullverdig sett
domenespesifikke MCP-verktøy (`linkml-modell-utkast`, `linkml-begrep-utkast`,
`linkml-validator`) som løyser dei faktiske behova (skjemagenerering, begrepsutkast,
validering).

### 5. Lisens

AGPL-3.0 (dual-lisensiert, kommersiell variant tilgjengeleg). Sjå eiga, utvida
lisensvurdering under («Lisensvurdering (utvida)») — oppdatert etter tiltaksvurderinga,
sidan biletbygging og eventuell publisering endrar risikobiletet samanlikna med rein
lokal bruk.

## Konklusjon

SocratiCode er **ikkje kompatibelt** med repoets førande prinsipp:

- Krev lokal installasjon av Node.js/npm — bryt "Ingen avhengigheter skal installeres lokalt"
- Krev Docker som container-motor — bryt "Alt skal kjøres som containere med podman i WSL2"
- Løyser eit generisk kodebase-søkeproblem urelatert til repoets faktiske innhald

**Tilråding (opphavleg, no delvis oppdatert — sjå under):** Ikkje adopter SocratiCode i
dette repoet utan vidare tiltak. Dersom behovet er raskare kodenavigering for
AI-assistentar, er dette betre løyst med eksisterande verktøy (Grep/Glob/Explore-agent i
Claude Code) gitt repoets avgrensa storleik, eller ved å utvide dei eksisterande
podman-baserte MCP-tenarane dersom konkrete søkebehov oppstår.

---

## Tiltaksvurdering: kan vi gjere SocratiCode podman-kompatibelt?

Brukaren ba om ei vurdering av konkrete tiltak for å få SocratiCode til å køyre i dette
repoet — primært som Claude Code-plugin, subsidiært som ein eigendefinert MCP-tenar
(tilsvarande dei tre eksisterande i `.mcp.json`).

### A — Claude Code-plugin-sporet: undersøkt og forkasta

Henta og inspisert SocratiCode sin eigen `.claude-plugin/plugin.json` og `.mcp.json`
direkte frå kjelderepoet:

```json
// .claude-plugin/plugin.json
{ "mcpServers": "./.mcp.json", ... }

// .mcp.json
{ "mcpServers": { "socraticode": { "command": "npx", "args": ["-y", "socraticode"] } } }
```

**Funn:** "Claude Code-plugin" er **ikkje** ein alternativ køyremodell — det er ein tynn
installasjonswrapper rundt **nøyaktig same** `npx -y socraticode`-kommando som
MCP-sporet, pluss medfølgjande skills/agent-instruksjonar. Pluginet endrar ingenting ved
Node.js- eller Docker-avhengigheita.

I tillegg installerast Claude Code-plugin **globalt per brukar**
(`claude plugin marketplace add` + `claude plugin install`, utanfor repoet sin
versjonskontroll) — i motsetnad til `.mcp.json`, som er sjekka inn i repoet og verkar
automatisk for alle som opnar det. Eit plugin-basert oppsett ville altså krevje at kvar
enkelt bidragsytar (og kvar AI-agent-økt) gjer eit manuelt, repo-eksternt
installasjonssteg for å få tilgang — noko som bryt med repoet sitt prinsipp om at
verktøytilgang skal vere reproduserbart frå sjølve repoet.

**Konklusjon A:** Plugin-sporet gjev **ingen teknisk fordel** framfor MCP-sporet, og er
dessutan mindre reproduserbart. Forkasta som primærspor.

### B — MCP-server-sporet: teknisk gjennomførbart

Gjennomgang av full `## Environment Variables`-seksjon i README avdekte at dei to
tidlegare identifiserte blokkerande punkta (Docker-styrt Qdrant og Ollama) **begge** har
eksplisitt støtta "extern"-modus som gjer at SocratiCode-prosessen sjølv aldri treng
tilgang til eit Docker/podman-socket:

| Variabel | Verdi som fjernar Docker-avhengigheita | Kjelde i README |
|---|---|---|
| `QDRANT_MODE` | `external` — "user-provided remote or cloud Qdrant (no Docker management)" | § Qdrant Configuration |
| `OLLAMA_MODE` | `external` — "user-managed Ollama instance (native, remote, etc.)" | § Ollama Configuration |

Kombinert med `QDRANT_URL`/`OLLAMA_URL` peika mot eigendrivne endepunkt, vert
SocratiCode-prosessen ein rein HTTP-klient mot to REST/gRPC-tenester — ikkje ein
Docker-orkestrator. Det opnar for ein arkitektur der **alle tre komponentane** køyrer som
podman-containerar, i tråd med repoet sitt eksisterande MCP-mønster
(`src/assets/containers/Dockerfile.mcp-linkml`, multi-stage, non-root-brukar):

1. **Qdrant og Ollama som langlevde podman-containerar** — starta av eit nytt
   Makefile-target (t.d. `make socraticode-up` / `socraticode-down`), t.d.
   `podman run -d --name socraticode-qdrant --restart=always -p 16333:6333 docker.io/qdrant/qdrant:v1.17.0`
   og tilsvarande for Ollama. Dette er eit **nytt driftsmønster** for repoet — dei tre
   eksisterande MCP-tenarane er eingongs `--rm`-prosessar per stdio-kall, ikkje
   langlevde bakgrunnstenester. Krev eigen oppstart/helsesjekk-logikk for å følgje
   "ingen stille feil"-prinsippet (t.d. sjekke at containeren svarar før MCP-kallet går
   vidare).
2. **SocratiCode-MCP-tenaren i eigen podman-container** — ein ny
   `Dockerfile.mcp-socraticode` (t.d. `FROM node:20-alpine`, `RUN npm install -g
   socraticode` i byggjesteget, non-root-brukar — same struktur som
   `Dockerfile.mcp-linkml`), registrert i `.mcp.json` med
   `env: { QDRANT_MODE: external, QDRANT_URL: ..., OLLAMA_MODE: external, OLLAMA_URL: ... }`
   og `--network=host` (native podman i WSL2, ikkje podman-machine-VM, så
   host-nettverk fungerer utan ekstra videresending).
3. **Repo-mount** — same mønster som `linkml-begrep-utkast`: repoet monterast read-only
   inn i containeren for indeksering.

**Konklusjon B:** Dette er **teknisk gjennomførbart** utan å bryte
podman-only-prinsippet, og fylgjer repoet sin eksisterande Dockerfile-konvensjon for dei
to av tre komponentar. Det attståande avviket er at Qdrant/Ollama må køyre som
**langlevde** containerar (ny driftsmodell), ikkje som eingongskall.

### C — Attståande avvegingar (uendra frå opphavleg vurdering)

- **Nytt driftsmønster:** langlevde bakgrunnscontainerar med `--restart` er noko nytt i
  repoet og krev eige vedlikehald (oppstart, healthcheck, opprydding) utanfor dagens
  `podman run -i --rm`-mønster.
- **Funksjonelt fokus framleis urelatert til repoets domene:** konklusjon 4 frå den
  opphavlege vurderinga står ved lag — repoet er eit avgrensa sett LinkML-YAML-skjema,
  ikkje ein stor polyglot kodebase. Den tekniske gjennomførbarheita løyser
  *kompatibilitets*-spørsmålet, ikkje *verdi*-spørsmålet.
- **Lisens (AGPL-3.0):** sjå eiga utvida vurdering under — konklusjonen er avhengig av
  om det eigenbygde biletet vert publisert eller halde strengt lokalt.
- **Førstegongs modell-nedlasting:** Ollama-embeddingmodellen (`nomic-embed-text`,
  ca. 270 MB) må lastast ned ved fyrste indeksering — eingongskostnad, men eit ekstra
  steg i oppsettet.

## Lisensvurdering (utvida)

Brukaren ba spesifikt om ei evaluering av lisensen i lys av tiltaksvurderinga over. Dette
er **ikkje juridisk rådgjeving** — dersom brukaren ønskjer å gå vidare med publisering,
bør konklusjonane under stadfestast av nokon med juridisk kompetanse på opphavsrett/OSS-lisensiering.

### Kva AGPL-3.0 faktisk krev

AGPL-3.0 byggjer på GPLv3, med eitt tillegg (§13, "Remote Network Interaction"): dersom
du **endrar** programmet og let brukarar samhandle med den endra versjonen over nettverk,
må du tilby dei kjeldekoden til di endra utgåve. Dette tettar det såkalla
"SaaS-smotthòlet" som vanleg GPL har (å køyre uendra/endra programvare som ei
nettverksteneste utan å "conveye"/distribuere kopiar reknast normalt ikkje som noko som
utløyser kjeldekode-plikter under GPLv3 åleine). Utover §13 gjeld dei vanlege
GPL-familie-pliktene: dei utløysast av **conveying** (distribusjon av kopiar — t.d. å
pushe eit containerbilete til eit offentleg register), ikkje av rein intern/privat bruk.

### Scenario 1 — Strengt lokal bruk (biletet vert aldri publisert)

Dersom `Dockerfile.mcp-socraticode` berre vert bygd og køyrd **lokalt** (kvar utviklar/
CI-runner bygger sjølv via `podman build`, biletet vert aldri pusha til noko register):

- Ingen "conveying" skjer — AGPL/GPL-pliktene gjeld distribusjon, ikkje privat/intern bruk.
- Det er heller ingen ekstern "brukar" som "interacts with it remotely through a computer
  network" i §13-forstand: MCP-tenaren er ein lokal stdio-prosess kalla av Claude Code på
  same maskin/WSL2-instans som utviklaren — ikkje ei nettverkseksponert teneste for andre.
- **Konklusjon Scenario 1:** Ingen realistisk AGPL-forplikting. Dette samsvarar med den
  opphavlege vurderinga (verktøyet som eit reint lokalt AI-utviklarverktøy).

### Scenario 2 — Publisert etter same mønster som dei tre andre MCP-verktøya

Repoet sin `release.yml` publiserer i dag alle tre eksisterande MCP-bilete offentleg til
`ghcr.io/brreg/mcp-linkml-*` ved kvar release (stadfesta med `grep` mot
`.github/workflows/release.yml`, sjå t.d. linje 52-117: `podman push
ghcr.io/${{ github.repository_owner }}/mcp-linkml-validator:...`). **Dersom eit
`mcp-socraticode`-bilete vart bygd og publisert etter same mønster**, endrar det
lisensbiletet vesentleg:

- Å pushe eit bilete som inneheld den npm-pakka `socraticode` (uendra eller ikkje) til eit
  offentleg register **er conveying** under GPL-familien — det utløyser standard
  GPL-plikter: behalde opphavsrettnotisar, inkludere lisensteksten, og gjere
  Corresponding Source tilgjengeleg (enkelt løyst her, sidan kjeldekoden allereie er
  offentleg på GitHub — ei tilvising held).
- Meir usikkert: å pakke ei tredjeparts AGPL-pakke inn i eit **eige-bygd, eige-namngjeve**
  bilete (`ghcr.io/brreg/mcp-socraticode`) saman med eiga orkestreringskode
  (Dockerfile, Makefile-mål, miljøvariabel-oppsett) kan i nokre tolkingar reknast som å
  skape eit derivert/kombinert verk, ikkje berre "mere aggregation" — særleg dersom noko
  av SocratiCode sin eigen kjeldekode vert patcha eller endra i biletbygginga. Held ein
  seg til `npm install -g socraticode` **uendra**, som ein reint separat prosess (ikkje
  lenkja inn i eigen kode), styrkjer det argumentet for "mere aggregation" — men dette er
  ikkje 100 % avklart i rettspraksis, og bør ikkje leggjast til grunn utan juridisk
  stadfesting dersom det skal publiserast under `brreg`-namnerommet.
- **Omdømme-/styringsdimensjon utover det reint juridiske:** dei tre eksisterande
  MCP-bileta inneheld kode BRREG sjølv har skrive (Python-serverar wrapa i container).
  Eit `mcp-socraticode`-bilete ville i hovudsak vere ein wrapper rundt eit tredjeparts,
  kommersielt dual-lisensiert produkt — å publisere det offentleg under
  `ghcr.io/brreg/` er ei anna type handling enn å publisere eigenutvikla verktøy, og bør
  vurderast som eit eige, medvite val (t.d. ev. dialog med SocratiCode sin
  vedlikehaldar), ikkje som eit automatisk biprodukt av å følgje eksisterande
  Dockerfile-konvensjon.
- **Konklusjon Scenario 2:** Mogleg å gjere AGPL-korrekt (lisenstekst + kjeldetilvising),
  men **tilrådd unngått** — både pga. den juridiske gråsona rundt kombinerte verk, og
  fordi det inneber å distribuere eit tredjeparts kommersielt produkt under eit offentleg
  `brreg`-namnerom utan openbert behov.

### Sideverktøy: Qdrant og Ollama

Qdrant-biletet (Apache License 2.0) og Ollama-biletet (MIT) vert i den føreslåtte
arkitekturen berre pulla og køyrde **uendra** frå sine offisielle, upubliserte-av-oss
kjelder (`docker.io/qdrant/qdrant`, Ollama sitt offisielle bilete) — dei vert korkje endra
eller republiserte av repoet. Begge lisensane er permissive og uproblematiske i denne
bruken; dei er ikkje omfatta av AGPL-vurderinga over.

### Samla lisenskonklusjon

| | Halde strengt lokalt (aldri publisert) | Publisert til `ghcr.io/brreg/mcp-socraticode` |
|---|---|---|
| AGPL §13 (nettverksklausul) | Gjeld ikkje — ingen ekstern nettverksbrukar | Truleg ikkje (MCP-tenaren er framleis ein lokal stdio-prosess for kvar brukar av biletet) |
| GPL-familiens "conveying"-plikter | Gjeld ikkje — ingen distribusjon skjer | Gjeld — krev lisenstekst + kjeldetilvising, handterbart |
| Juridisk gråsone (kombinert/derivert verk) | Irrelevant | Uavklart nok til å tilrå varsemd |
| Tilråding | **Trygt** | **Unngå** — bygg lokalt per utviklar/CI-runner, ikkje legg til i `release.yml` |

**Konklusjon:** Lisensen er **ikkje eit hinder** for det tilrådde pilotoppsettet
(strengt lokal `podman build`, aldri publisert), men **vert** eit reelt spørsmål dersom
nokon seinare vel å føye `mcp-socraticode` til den same publiseringsflyten som dei tre
andre MCP-bileta i `release.yml`. Dette er no eksplisitt lagt inn som ei avgrensing i
tilrådinga under.

## Ny anbefaling

**Ikkje adopter via Claude Code-plugin** — det sporet gjev ingen teknisk fordel og er
mindre reproduserbart enn repoet sitt eksisterande `.mcp.json`-mønster.

**Vurder MCP-server-sporet som eit pilotforsøk, ikkje som standardoppsett** — det er no
verifisert teknisk gjennomførbart å halde seg 100 % innanfor podman (`QDRANT_MODE=external`
+ `OLLAMA_MODE=external` fjernar Docker-avhengigheita heilt), men krev:
(a) ein ny `Dockerfile.mcp-socraticode` etter eksisterande mønster,
(b) to nye langlevde podman-containerar (Qdrant, Ollama) med tilhøyrande
Makefile-oppstart/helsesjekk — eit driftsmønster repoet ikkje har i dag,
(c) ei eiga avveging av om verdien (semantisk kodesøk/impact-analyse) er stor nok for
eit skjemadrive repo av denne storleiken til å rettferdiggjere den nye infrastrukturen, og
(d) **eit eksplisitt lisensvilkår:** `mcp-socraticode`-biletet skal **berre byggjast
lokalt** (`podman build` per utviklar/CI-runner) og **aldri** leggjast til
publiseringssteget i `release.yml`/`ghcr.io/brreg/*` saman med dei tre andre
MCP-bileta — sjå «Lisensvurdering (utvida)» over for grunngjeving. Dersom nokon seinare
vurderer å publisere det likevel, må det handterast som ei eiga, medviten avgjerd (ikkje
eit automatisk biprodukt av å følgje eksisterande Dockerfile-/release-konvensjon), og bør
stadfestast juridisk først.

Dersom brukaren ønskjer å gå vidare, er neste steg å skrive ein eigen
implementasjonsspec for punkt (a)-(b) over — dette dokumentet dekkjer berre
gjennomførbarheitsvurderinga, ikkje sjølve implementasjonen.

## Utført

Opphavleg vurdering fullført basert på gjennomgang av SocratiCode sin README
(`Prerequisites`, `Quick Start`, `Docker Resources`, `License`-seksjonane) og
samanlikning med repoets eksisterande MCP-oppsett (`.mcp.json`) og førande prinsipp
(`CLAUDE.md`).

Tiltaksvurdering (fyrste utvidinga) fullført basert på: (1) henting av SocratiCode sin
eigen `.claude-plugin/plugin.json` og `.mcp.json` frå kjelderepoet via `gh api` for å
verifisere plugin- vs. MCP-køyremodellen, (2) full gjennomgang av
`## Environment Variables`-seksjonen i README for `QDRANT_MODE`/`OLLAMA_MODE=external`,
og (3) samanlikning med repoets eksisterande Dockerfile-konvensjon
(`src/assets/containers/Dockerfile.mcp-linkml`).

Utvida lisensvurdering (denne utvidinga) fullført basert på: (1) analyse av AGPL-3.0 sitt
faktiske innhald (§13-nettverksklausulen vs. GPL-familiens generelle
"conveying"-plikter), (2) `grep` mot `.github/workflows/release.yml` som stadfesta at
repoet alt publiserer dei tre eksisterande MCP-bileta offentleg til `ghcr.io/brreg/*`
ved kvar release — eit funn som direkte endrar risikobiletet dersom same mønster vart
følgt for eit `mcp-socraticode`-bilete, og (3) vurdering av lisensane til dei to
sideverktøya (Qdrant: Apache-2.0, Ollama: MIT), som er upåverka sidan dei berre køyrast
uendra frå offisielle bilete. Ingen kodeendringar er gjort — dette er framleis ei rein
kartleggings-/vurderingsoppgåve; eventuell implementasjon krev eige brukarsamtykke og
eigen spec, og eventuell publisering krev i tillegg juridisk stadfesting (jf.
lisensvurderinga).
