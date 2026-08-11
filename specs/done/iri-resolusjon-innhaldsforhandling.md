# IRI-resolusjonssjekk: legg til innhaldsforhandlingstestar

## Bakgrunn

`analyse-iri-resolution` (frå `specs/done/modell-analyse-workflow.md`) testar i
dag berre om IRI-ar (id/default_prefix/prefixes) svarar med ein 2xx/3xx-status.
Brukaren vil i tillegg teste **innhaldsforhandling** (content negotiation) —
eit kjent gap dokumentert i
`specs/backlog/avvik-peikarar-til-offentlege-ressursar.md` (avvik 4):

1. `Accept: text/turtle` skal gi RDF Turtle-representasjonen av ressursen.
2. `Accept-Language: nb` skal gi HTML-representasjonen på norsk bokmål.
3. `Accept-Language: en` skal gi HTML-representasjonen på engelsk.

Avklarte val (spurt via AskUserQuestion før arbeidet starta):

- **Omfang:** Berre IRI-ar repoet sjølv eig — kvart skjema sin `id` og
  `default_prefix` — ikkje `prefixes:`-verdiar til tredjeparts vokabular
  (dct:, xsd:, foaf: osv.), sidan repoet ikkje kan fikse innhaldsforhandling
  hjå eksterne vokabular-utgivarar.
- **Turtle-kriterium:** Følg redirects automatisk (urllib gjer dette som
  standard, og vidarefører `Accept`/`Accept-Language`-headerane til
  redirect-target, jf. `HTTPRedirectHandler.redirect_request`). Sjekk om
  **sluttresponsen** sin `Content-Type` inneheld "turtle" — både eit direkte
  200-svar med rett Content-Type og eit 303-følgt-av-200 tel som bestått.
- **Språk-kriterium:** Sjekk om sluttresponsen sin `Content-Language`-header
  startar med `nb`/`en` (case-insensitive). Ingen HTML-parsing.

Desse testane køyrer **uavhengig** av basis-resolusjonssjekken (same IRI kan
dukke opp i begge seksjonar) — enklare kode, og tydelegare rapport per
testtype.

## Steg

1. Oppdater `src/assets/scripts/makefile/check-iri-resolution.py`:
   - Legg til ein delt `_open(url, method, headers)`-hjelpefunksjon (erstattar
     `_request`) som byggjer request med `User-Agent` + valfrie ekstra
     headerar.
   - Legg til `check_turtle(url)` og `check_language(url, lang)`.
   - Samle `id`/`default_prefix` per skjema separat frå den fulle
     `prefixes`-samlinga (eksisterande basis-sjekk er uendra).
   - Print ein ny `## Innhaldsforhandling`-seksjon med tabell
     `IRI | Test | Resultat | Referert av` og ei oppsummeringslinje.
2. Oppdater `COMMANDS.md` sin skildring av `analyse-iri-resolution`.
3. Test scriptet lokalt via `make analyse-iri-resolution` og sjekk at begge
   seksjonar (resolusjon + innhaldsforhandling) vert produserte korrekt.

Ingen endring naudsynt i `.github/workflows/modell-analyse.yml` eller
`make/91-modell-analyse.mk` — begge er allereie generiske nok (target-namnet
og pipe-til-fil-mønsteret er uendra, rapporten berre vert lengre).

## Handlingsliste

- [x] Steg 1: `check-iri-resolution.py`
- [x] Steg 2: `COMMANDS.md`
- [x] Steg 3: Lokal test

## Utført

**Dato:** 2026-08-11

Alle tre steg gjennomførte. Lokal køyring av `make analyse-iri-resolution`
stadfestar at begge seksjonar (`# IRI-resolusjonssjekk` og `##
Innhaldsforhandling`) genererer korrekt markdown.

**Funn:** 216 av 216 innhaldsforhandlingstestar (72 eigne IRI-ar × 3 testar)
feila — `data.norge.no` returnerer `text/html` uansett `Accept`-header og set
aldri `Content-Language`. Dette stadfestar (automatiserer) det kjende gapet
frå avvik 4 i `specs/backlog/avvik-peikarar-til-offentlege-ressursar.md`:
infrastrukturen hjå `data.norge.no` støttar ikkje innhaldsforhandling i dag.
Ikkje ein feil i sjølve sjekken — informativt resultat som viser eit reelt,
allereie dokumentert gap som ligg utanfor repoet si råderett å fikse åleine.
