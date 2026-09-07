# Evaluering: ny Claude Code-rule for koding av MCP-serverar

## Bakgrunn

Brukaren bad om ei vurdering av om det finst grunnlag for ei ny Claude
Code-rule eller skill knytta til **koding av MCP-serverar**
(`src/mcp-linkml-validator/`, `src/mcp-linkml-modell-utkast/`,
`src/mcp-linkml-begrep-utkast/`), basert på etablert praksis i repoet.

Per steg 1 i `.claude/skills/ny-rule/SKILL.md` krevst konkret grunngjeving
(registrert bug, spec-funn eller observert hending) — ikkje spekulativ
"beste praksis". Gjennomgang av `specs/done/` (17 mcp-relaterte specs),
`bugs/` og faktisk kjeldekode i dei tre server-mappene gav fire konkrete
funn:

### 1. `KeyError: 'result'` — manglande `error`-sjekk i JSON-RPC-konsument

`specs/done/mcp-validator-feilvising-og-relativ-import-bug.md`: eit filter
i `flatten-and-validate.bash` føresette ubetinga at eit JSON-RPC-svar frå
MCP-serveren hadde eit `result`-felt (`r['result']['content'][0]['text']`),
og kræsja med kryptisk `KeyError: 'result'` når serveren i staden returnerte
`{"error": {...}}` — noko som gøymde den reelle feilmeldinga
(`Unknown CURIE prefix: https`, jf. BUG-15) frå brukaren.

### 2. Delvis identifikatorsanering — inkonsistens mellom saneringspunkt

`specs/done/mcp-generate-identifikator-sanitering.md` (`converter.py` i
`mcp-linkml-modell-utkast`): slot-namn vart saniterte (bindestrek →
understrek, translitterering), men type-, enum- og klassenamn vart tekne
rått frå `$defs`-nøklane fire separate stader (`_collect_types()`,
`_resolve_ref()`, `_collect_enums()`, `_collect_classes()`). Resultatet var
at `E-postadresse` vart generert som eit ugyldig Python-identifikatornamn,
og at `gen-python` feila. Feilen oppstod fordi saneringslogikken vart lagt
til på *eitt* av fleire stader eit namn vert utleidd, ikkje alle.

### 3. Etablert namnekonvensjon `mcp-linkml-<funksjon>`

`specs/done/mcp-server-namngjeving.md` og
`specs/done/mcp-target-navnekonvensjon.md`: alle tre serverane, deira
Makefile-target og image-namn følgjer i dag konsekvent mønsteret
`mcp-linkml-<funksjon>` (`mcp-linkml-validator`, `mcp-linkml-modell-utkast`,
`mcp-linkml-begrep-utkast`) etter ei eksplisitt namneoppgradering — dette
er ein etablert, handheva konvensjon, ikkje eit tilfeldig mønster.

### 4. Duplisert JSON-RPC-stdio-protokoll på tvers av alle tre serverar

Direkte inspeksjon av kjeldekoden (denne økta) stadfestar at alle tre
`server.py`-filene implementerer **nesten identisk**
JSON-RPC 2.0-over-stdio-boilerplate uavhengig av kvarandre:
ein `send()`-hjelpefunksjon (skriv JSON + newline til stdout, flush), same
`initialize`/`initialized`/`tools/list`-handtering, same
`tools/call`-dispatch med feilinnpakking (`{"jsonrpc": "2.0", "id":
msg.get("id"), "error": {...}}`), og same `main()`-løkke som les
linje-for-linje frå `sys.stdin` med parse-feil-handtering. Dette er tre
uavhengige implementasjonar av same mekanikk — over CLAUDE.md sin eigen
DRY-terskel (3+ identiske tilfelle). Det finst alt presedens for å
konsolidere delt JSON-RPC-mekanikk i dette repoet
(`specs/done/konsolider-mcp-modell-utkast-jsonrpc.md`), men den
konsolideringa gjaldt kallar-sida (request-bygging/respons-ekstrahering i
`src/assets/scripts/makefile/`), ikkje sjølve dispatch-løkka inne i
serverane.

**Ingen eksisterande rule dekker `src/mcp-*/**`** — `container-images.md`
dekker Dockerfile/containerinvokering, `make-conventions.md` dekker
`src/assets/scripts/**` (kallar-sida), men Python-kjeldekoden *inne i*
MCP-serverane manglar automatisk lasta kontekst.

## Avgjerd: mekanisme

Følgjer avgjerdstreet i `specs/done/evaluering-nye-skills-og-rules.md`:
mønstra over er **stiscoperte** (gjeld berre `src/mcp-*/**`) og skal lastast
**automatisk** ved arbeid med desse filene — dette er ei rule, ikkje ein
skill (ingen eksplisitt "opprett ny MCP-server"-arbeidsflyt er observert
eller etterspurt) og ikkje CLAUDE.md direkte (gjeld ikkje ubetinga uansett
filsti).

**Ny fil**, ikkje utviding av eksisterande rule: filsti-scopet
(`src/mcp-*/**`) er distinkt frå alle sju eksisterande rules.

## Steg

1. Opprett `.claude/rules/mcp-server-python.md` med frontmatter scopa til
   `src/mcp-*/**`, strukturert som dei fire funna over (problem → forbod →
   framgangsmåte → referanse til konkret spec/bug), etter malen skildra i
   `.claude/skills/ny-rule/SKILL.md` steg 4:
   - **Feil-før-resultat ved parsing av JSON-RPC-svar**: kvar kode (bash,
     python) som les eit JSON-RPC-svar frå ein av desse MCP-serverane skal
     sjekke `"error"`-nøkkelen før han føreset `"result"` finst.
   - **Sanering av utleidde identifikatorar må skje på *alle* stader eit
     namn vert utleidd**: når ein converter/generator lagar nye
     klasse-/slot-/type-/enum-namn frå ekstern input, må same
     saneringsfunksjon kallast på *alle* stadene namnet vert produsert
     (ikkje berre den første/opplagde).
   - **Namnekonvensjon**: nye MCP-serverar/tools/targets skal følgje
     `mcp-linkml-<funksjon>`-mønsteret.
   - **Kjend DRY-gjeld**: dokumenter den observerte JSON-RPC-boilerplate-
     dupliseringa på tvers av dei tre `server.py`-filene som eit kjent
     avvik — konsolider til eit delt modul dersom ein fjerde MCP-server
     vert lagt til, eller dersom dispatch-logikken i éin av dei tre vert
     endra vesentleg (jf. DRY-terskelen i CLAUDE.md og presedensen i
     `specs/done/konsolider-mcp-modell-utkast-jsonrpc.md`). **Ikkje**
     utfør konsolideringa no — det er ei separat, større endring utanfor
     scope for denne rule-opprettinga.
2. Logg denne avgjerda (rule vs. skill, ny fil vs. utviding) i
   `## Avgjerder` under.
3. Generer commit-melding, legg til `## Utført`, flytt spec til
   `specs/done/`.

## Prioritert handlingsliste

- [x] Opprett `.claude/rules/mcp-server-python.md`
- [x] Verifiser frontmatter-format mot eksisterande rules (samanlikn
      `container-images.md`)

## Avgjerder

- **Rule, ikkje skill, og ny fil (ikkje utviding av ein eksisterande
  rule).** Grunngjeving: mønstra er stiscoperte til `src/mcp-*/**` og skal
  lastast automatisk, ikkje køyrast ved eksplisitt kall — ingen observert
  "opprett ny MCP-server"-arbeidsflyt som ville grunngjeve ein skill. Ingen
  av dei sju eksisterande rules dekker `src/mcp-*/**`, så eit nytt
  filsti-scope krev ny fil (jf. steg 3 i `.claude/skills/ny-rule/SKILL.md`).
- **Fire funn samla i éi rule-fil, ikkje fire separate rules.** Alle fire
  deler same filsti-scope (`src/mcp-*/**`) og gjeld same tema (kodepraksis
  for MCP-server-Python), same struktur som andre fleir-seksjons-rules i
  repoet (t.d. `container-images.md` sine fire seksjonar).
- **Konsolidering av den duplika JSON-RPC-boilerplate-en er dokumentert
  som kjend gjeld, ikkje utført no.** Grunngjeving: brukaren sin instruks
  var å evaluere/dokumentere praksis for framtidig kodearbeid, ikkje å
  utføre eit sjølvstendig refaktoreringstiltak. Faktisk konsolidering er
  ei separat, større endring (3 filer, testdekning må verifiserast) som
  krev eiga spec og brukargodkjenning, i tråd med CLAUDE.md sitt
  DRY-avsnitt.

## Utført

Oppretta `.claude/rules/mcp-server-python.md`, scopa til `src/mcp-*/**`,
med fire seksjonar grunngjevne i konkrete spec-/bug-funn:

1. **Feil-før-resultat ved JSON-RPC-parsing** — grunngjeve i
   `specs/done/mcp-validator-feilvising-og-relativ-import-bug.md`
   (`KeyError: 'result'`-kræsj som gøymde BUG-15).
2. **Identifikatorsanering på alle utleiingsstader** — grunngjeve i
   `specs/done/mcp-generate-identifikator-sanitering.md`
   (`E-postadresse`-bindestrek-bug i `converter.py`).
3. **Namnekonvensjon `mcp-linkml-<funksjon>`** — grunngjeve i
   `specs/done/mcp-server-namngjeving.md` og
   `specs/done/mcp-target-navnekonvensjon.md`.
4. **Kjend DRY-gjeld: triplisert JSON-RPC-dispatch-boilerplate** —
   stadfesta empirisk (grep mot alle tre `server.py`) denne økta,
   dokumentert som kjent avvik med tilvising til presedens
   (`specs/done/konsolider-mcp-modell-utkast-jsonrpc.md`) — konsolidering
   **ikkje** utført, berre dokumentert som handlingspunkt for neste gong
   ein fjerde server vert lagt til eller dispatch-logikk vert endra
   vesentleg.

Ingen kodeendring i sjølve MCP-serverane — berre ny rule-fil.
