---
name: mcp-server-python
description: Kodepraksis for Python-kjeldekoden i dei tre MCP-serverane (JSON-RPC-feilhandtering, identifikatorsanering, namnekonvensjon, kjend DRY-gjeld i dispatch-boilerplate). Lastast automatisk ved arbeid med filer under src/mcp-*/.
paths:
  - "src/mcp-*/**"
---

## Sjekk `error` før du føreset `result` i eit JSON-RPC-svar

Alle tre MCP-serverane returnerer på feil eit korrekt JSON-RPC 2.0-svar
utan `result`-felt: `{"jsonrpc": "2.0", "id": ..., "error": {...}}`. Kode
som konsumerer eit slikt svar (bash-filter, Python-klient, test) og
ubetinga føreset at `result` finst — t.d. `r['result']['content'][0]['text']`
utan først å sjekke `r.get('error')` — kræsjar med ein kryptisk
`KeyError: 'result'` og gøymer den faktiske feilmeldinga frå brukaren.

**Fell aldri tilbake til** å indeksere rett inn i `result` utan først å
sjekke om `error` finst i responsen.

Rett mønster:

```python
r = json.loads(line)
if r.get("id") == expected_id:
    if "error" in r:
        print(r["error"]["message"], file=sys.stderr)
        sys.exit(1)
    print(r["result"]["content"][0]["text"])
```

Konkret hending: `src/mcp-linkml-validator/flatten-and-validate.bash`
kræsja slik og gøymde `Unknown CURIE prefix: https` (BUG-15) bak eit
uforklarleg `KeyError: 'result'`. Sjå
`specs/done/mcp-validator-feilvising-og-relativ-import-bug.md`.

## Sanering av utleidde identifikatorar må skje på *alle* utleiingsstader

Når ein converter/generator lagar nye LinkML-identifikatorar (klasse-,
slot-, type- eller enum-namn) frå ekstern input (t.d. `$defs`-nøklar i
JSON Schema), er det ikkje nok å sanere (translitterere, erstatte
bindestrek) på éin stad. Same namn vert ofte produsert fleire separate
stader i koden (t.d. når ein type både registrerast i eit oppslag *og*
refererast frå ein annan stad via `$ref`) — dersom saneringa berre er lagt
til éin av desse stadene, oppstår eit ugyldig LinkML/Python-identifikatornamn
akkurat der ho manglar.

**Fell aldri tilbake til** å anta at sanering av éin utleiingsstad (t.d.
slot-namn) dekker alle dei andre (type-namn, enum-namn, klassenamn,
referanseoppløysing).

Framgangsmåte: bruk **éi** delt saneringsfunksjon, og grep gjennom heile
fila etter alle stader eit namn hentast direkte frå kjeldedata (nøklar i
eit `dict`, `$ref`-oppløysing, fallback-namn) — kall funksjonen på kvar
einaste ein, ikkje berre den mest opplagde.

Konkret hending: `converter.py` i `mcp-linkml-modell-utkast` saniterte
slot-namn, men ikkje type-/enum-/klassenamn (fire separate stader:
`_collect_types()`, `_resolve_ref()`, `_collect_enums()`,
`_collect_classes()`). `E-postadresse` vart generert som eit ugyldig
Python-identifikatornamn, og `gen-python` feila. Sjå
`specs/done/mcp-generate-identifikator-sanitering.md`.

## Namnekonvensjon: `mcp-linkml-<funksjon>`

Nye MCP-server-mapper, Makefile-target og image-namn skal følgje det
etablerte mønsteret `mcp-linkml-<funksjon>` (t.d. `mcp-linkml-validator`,
`mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`) — ikkje
`mcp-<funksjon>` eller `mcp-linkml-<domene>-<funksjon>`. Hjelpetarget følgjer
`mcp-linkml-<funksjon>-<operasjon>` (t.d. `mcp-linkml-validate-smoke`). Sjå
`specs/done/mcp-server-namngjeving.md` og
`specs/done/mcp-target-navnekonvensjon.md` for grunngjeving og full
namneoppgraderingshistorikk.

## Kjend DRY-gjeld: JSON-RPC-dispatch-boilerplate er duplisert tre gonger

Alle tre `server.py`-filene implementerer **uavhengig av kvarandre** same
JSON-RPC 2.0-over-stdio-mekanikk: ein `send()`-hjelpefunksjon,
`initialize`/`initialized`/`tools/list`-handtering, `tools/call`-dispatch
med feilinnpakking, og ei `main()`-løkke som les linje for linje frå
`sys.stdin` med parse-feil-handtering. Dette er over CLAUDE.md sin eigen
DRY-terskel (3+ identiske tilfelle), men er **ikkje** konsolidert enno —
konsolideringa som alt er gjort
(`specs/done/konsolider-mcp-modell-utkast-jsonrpc.md`) gjaldt kallar-sida
(request-bygging i `src/assets/scripts/makefile/`), ikkje sjølve
dispatch-løkka inne i serverane.

**Ikkje** legg til ein fjerde uavhengig kopi av denne mekanikken. Dersom du
legg til ein ny MCP-server, eller gjer ei vesentleg endring i
dispatch-logikken til éin av dei tre eksisterande, konsolider
`send()`/`initialize`/`tools-list`/`main()`-løkka til eit delt modul (t.d.
`src/assets/scripts/utils/mcp_jsonrpc_stdio.py`, i tråd med korleis
`linkml_relative_import_patch.py` alt er delt på tvers av fleire
kallestader) — spør brukaren om godkjenning først, jf. CLAUDE.md sitt
DRY-avsnitt ("Omskriv aldri eksisterande kode... med DRY som einaste
grunngjeving utan å spørje brukaren om løyve først").
