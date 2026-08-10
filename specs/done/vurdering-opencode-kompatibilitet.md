# Vurdering: OpenCode-kompatibilitet med repoet

**Kjelde:** [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
**Dato vurdert:** 2026-08-10
**Konklusjon:** Annan kategori verktøy enn dei tre tidlegare vurderte (SocratiCode,
Code-to-Knowledge-Graph, CodeGraph) — OpenCode er ein **fullverdig, alternativ
AI-agent-CLI** (som Claude Code sjølv), ikkje eit tillegg som skal vevast inn i repoet sin
podman-baserte verktøyflyt. "Kompatibilitet" handlar difor om noko anna: om ein
bidragsytar kan bruke OpenCode i staden for Claude Code til å følgje CLAUDE.md sin
arbeidsflyt i dette repoet. Delvis kompatibelt ut av boksen (CLAUDE.md-instruksjonar vert
plukka opp automatisk), men MCP-tenarane treng eit separat oppsett.

---

## Bakgrunn

OpenCode er "the open source AI coding agent" — 195 000+ GitHub-stjerner, MIT-lisensiert,
TypeScript. I motsetnad til dei tre tidlegare vurderte verktøya (som alle er MCP-tillegg/
kodebase-intelligens-verktøy meint å *utvide* eit vertsagentmiljø) er OpenCode sjølve
**vertsagenten** — ein direkte konkurrent/erstatning for Claude Code, installert som
standalone CLI eller skrivebordsapp. Brukaren ba om tilsvarande vurdering som for dei tre
førre verktøya, inkludert lisensvurdering.

## Kvifor vurderinga må rammast annleis

Dei tre førre vurderingane spurde: *"kan vi containerisere dette verktøyet og veve det inn
i repoet sin podman-baserte MCP-infrastruktur (`.mcp.json`)?"* Det spørsmålet gjev ikkje
meining for OpenCode, sidan det er sjølve agent-CLI-en ein menneskeleg bidragsytar vel å
køyre — same kategori som Claude Code sjølv. CLAUDE.md sitt prinsipp "ingen
avhengigheiter skal installerast lokalt, alt skal køyrast som containerar med podman"
gjeld repoet sin **eigen** bygge-/valideringstooling (LinkML-generatorar, MCP-tenarar) —
ikkje kva for interaktiv AI-CLI ein utviklar vel å bruke på eiga maskin. Det er same
avgrensing som vart gjort i Code-to-Knowledge-Graph-vurderinga om at "Bevel"
VS Code-utvidinga er eit personleg IDE-verktøyval utanfor repoet sin infrastruktur.

Det reelle spørsmålet vert difor: **fungerer CLAUDE.md sin arbeidsflyt korrekt dersom ein
bidragsytar brukar OpenCode i staden for Claude Code?**

## Funn

### 1. CLAUDE.md vert automatisk plukka opp — sterkast positive funn i denne serien

Henta og lest `packages/web/src/content/docs/rules.mdx` (offisiell dokumentasjon) og
`packages/core/src/instruction-context.ts` (kjeldekode) direkte frå repoet. Begge
stadfestar at OpenCode har eksplisitt, dokumentert **Claude Code-kompatibilitet**:

> **Claude Code Compatibility** — For users migrating from Claude Code, OpenCode
> supports Claude Code's file conventions as fallbacks:
> - **Project rules**: `CLAUDE.md` in your project directory (used if no `AGENTS.md` exists)
> - **Global rules**: `~/.claude/CLAUDE.md` (used if no `~/.config/opencode/AGENTS.md` exists)

Presedensrekkjefølgje: OpenCode leitar først etter `AGENTS.md` (traversert oppover frå
arbeidskatalogen), deretter `CLAUDE.md` i same katalogar. Sidan dette repoet **har**
`CLAUDE.md` og **ikkje** har `AGENTS.md`, vil OpenCode automatisk laste og følgje heile
repoet sin arbeidsflyt — spesifikasjonsprosessen, "aldri git commit/push"-regelen,
Makefile-berre-prinsippet, DRY-regelen osv. — **utan at repoet treng endrast i det heile.**
Dette kan deaktiverast eksplisitt via `OPENCODE_DISABLE_CLAUDE_CODE=1` dersom det er
uønskt, men er på som standard.

### 2. MCP-tenarane (`.mcp.json`) vert IKKJE plukka opp automatisk

`gh api search/code` for `.mcp.json` i OpenCode-repoet gav **ingen treff** — stadfesta med
gjennomgang av den offisielle MCP-dokumentasjonen
(`packages/web/src/content/docs/mcp-servers.mdx`). OpenCode brukar sitt eige
konfigurasjonsformat, `opencode.json`/`opencode.jsonc`, med eit anna skjema enn
Claude Code sin `.mcp.json`:

| | Claude Code (`.mcp.json`, brukt i dette repoet) | OpenCode (`opencode.json`) |
|---|---|---|
| Toppnøkkel | `mcpServers` | `mcp` |
| Kommandofelt | `"command": "bash", "args": [...]` (delt) | `"command": ["bash", "-c", "..."]` (éin array) |
| Påkravd felt | — | `"type": "local"`, `"enabled": true` |

Konsekvens: dei tre eksisterande podman-baserte MCP-tenarane
(`linkml-modell-utkast`, `linkml-validator`, `linkml-begrep-utkast`) vert **ikkje**
tilgjengelege for ein OpenCode-brukar utan at nokon skriv ein parallell
`opencode.json` som omset kvar av dei tre `.mcp.json`-oppføringane til OpenCode sitt
skjema. Sjølve `podman run`-kommandoane er uendra og verktøyagnostiske — det er berre
JSON-innpakkinga som må omsetjast. Dette er eit **konkret, avgrensa
vedlikehaldsarbeid** (tre små konfigurasjonsblokker), ikkje eit arkitektonisk hinder,
men det er heller ikkje noko som fungerer automatisk i dag.

### 3. Installasjonsmodell — same kategori som Claude Code sjølv, ikkje eit repo-tillegg

```bash
curl -fsSL https://opencode.ai/install | bash    # eller npm/brew/scoop/nix/pacman
```

Dette er eit lokalt installasjonssteg, men fordi OpenCode her vert vurdert som eit
**alternativ til Claude Code** (den interaktive CLI-en ein bidragsytar vel), ikkje som
eit repo-tillegg som skal vevast inn i podman-pipelinen, gjeld ikkje CLAUDE.md sitt
"ingen lokale avhengigheiter"-prinsipp her på same måte som for dei tre førre verktøya.
Same grunngjeving som for kvifor Claude Code sjølv ikkje reknast som eit brot på dette
prinsippet.

### 4. Ope kjeldekode, aktivt vedlikehalde, stort fellesskap

195 700+ stjerner, 25 000+ forkar, siste commit same dag som denne vurderinga
(2026-08-10). Byggjer på Effect/TypeScript, tilhøyrer opphavleg SST-økosystemet
(`sst.config.ts`, `flake.nix` i repoet). Dokumentasjonen finst òg omsett til norsk
(`README.no.md`, `docs/nb/rules.mdx`), noko som gjer terskelen for norske bidragsytarar
lågare enn for dei tre andre verktøya.

## Lisensvurdering

**Lisens:** [MIT License](https://github.com/anomalyco/opencode/blob/dev/LICENSE) —
stadfesta i GitHub-metadata.

Same konklusjon som for CodeGraph: MIT er fullt permissivt, ingen copyleft-plikter,
einaste krav er å behalde opphavsrett-/lisensmerknaden i kopiar. I dette tilfellet er
lisensspørsmålet i praksis **irrelevant for repoet**, sidan OpenCode aldri ville vore
distribuert, bunta inn i eller publisert saman med repoet sine eigne artefakt — det er
eit verktøy kvar enkelt bidragsytar installerer på eiga maskin, akkurat som Claude Code.
Det finst difor ikkje noko "conveying"- eller attribution-spørsmål å vurdere slik det var
for SocratiCode (AGPL-3.0) og Code-to-Knowledge-Graph (MPL-2.0).

## Samanlikning med dei tre tidlegare vurderte verktøya

| | SocratiCode | Code-to-Knowledge-Graph | CodeGraph | OpenCode |
|---|---|---|---|---|
| Kategori | MCP-tillegg (kodesøk) | JVM-bibliotek | MCP-tillegg (kodegraf) | **Fullverdig agent-CLI** |
| Lisens | AGPL-3.0 (problematisk ved publisering) | MPL-2.0 (uproblematisk) | MIT (uproblematisk) | **MIT (irrelevant — vert aldri distribuert av repoet)** |
| Skal containeriserast av repoet? | Ja, vurdert mogleg via podman | Ja, men krev nytt byggøkosystem | Ja, enklast av dei tre | **Nei — personleg CLI-val, som Claude Code sjølv** |
| Plukkar opp CLAUDE.md automatisk | N/A | N/A | N/A | **Ja, dokumentert fallback-støtte** |
| Plukkar opp `.mcp.json` automatisk | N/A | N/A | N/A | **Nei — eige skjema (`opencode.json`), krev omsetjing** |
| Dekkjer repoets faktiske innhald (YAML) | Marginalt | Marginalt | Nei (YAML ikkje støtta) | **Irrelevant — agenten sjølv er språkagnostisk** |

## Konklusjon

OpenCode er ikkje samanliknbart med dei tre førre verktøya — det er ein alternativ
AI-agent-CLI, ikkje eit tillegg som skal vevast inn i repoet sin podman-infrastruktur.
Det reelle spørsmålet — *"fungerer CLAUDE.md-arbeidsflyten viss nokon brukar OpenCode i
staden for Claude Code?"* — har eit **delvis positivt svar**:

- **CLAUDE.md-instruksjonane vert plukka opp automatisk**, dokumentert og verifisert
  direkte i kjeldekoden — den sterkaste "det fungerer ut av boksen"-konklusjonen av alle
  fire vurderingane i denne serien.
- **MCP-tenarane (`linkml-modell-utkast`, `linkml-validator`, `linkml-begrep-utkast`)
  krev eit separat `opencode.json`-oppsett** — dei vert ikkje tilgjengelege automatisk,
  sidan OpenCode brukar eit anna konfigurasjonsskjema enn `.mcp.json`.
- **Lisensen er irrelevant** for repoet, sidan verktøyet aldri distribuerast av oss.

**Tilråding:** Ikkje noko tiltak påkravd for CLAUDE.md-delen — det fungerer alt. Dersom
repoet ønskjer å støtte OpenCode-brukarar fullt ut (t.d. slik at MCP-verktøya òg er
tilgjengelege), er neste steg å leggje til ein `opencode.json` i repoterota som
omset dei tre eksisterande `.mcp.json`-oppføringane til OpenCode sitt skjema — eit lite,
isolert tillegg som ikkje endrar noko ved dei eksisterande Claude Code-brukarane sitt
oppsett. Dette er valfritt og bør berre gjerast dersom det finst reelle OpenCode-brukarar
blant bidragsytarane; det er ikkje eit hinder eller ei sikkerheitsrisiko å la det vere.

## Utført

Vurderinga er fullført basert på: (1) gjennomgang av OpenCode sin README og
installasjonsseksjon, (2) henting og lesing av `packages/core/src/instruction-context.ts`
(kjeldekode for korleis instruksjonsfiler vert oppdaga) og
`packages/web/src/content/docs/rules.mdx` (offisiell dokumentasjon) for å stadfeste
CLAUDE.md-fallback-støtte, (3) `gh api search/code`-søk etter `.mcp.json` i repoet
(ingen treff) og gjennomgang av `packages/web/src/content/docs/mcp-servers.mdx` for å
stadfeste at OpenCode brukar eit anna MCP-konfigurasjonsskjema, og (4) stadfesting av
MIT-lisens via GitHub-metadata. Ingen kodeendringar er gjort — dette er ei rein
kartleggings-/vurderingsoppgåve.
