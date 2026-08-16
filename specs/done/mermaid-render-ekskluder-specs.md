# Ekskluder specs/ frå mermaid-render-sjekken

## Bakgrunn

Etter forrige økt sin logg-synleggjering (`specs/done/mermaid-render-diagram-logging.md`)
vart det tydeleg at `mermaid-render`-jobben (steget «Rendra kvar mermaid-blokk»
i `.github/workflows/lenkje-og-mermaid-sjekk.yml`) rapporterer to feila
diagram frå `specs/done/`:

- `specs/done/utvid-publiseringsflyt-diagram.md`, diagram nr. 2 (line 312–318)
- `specs/done/release-arbeidsflyt-diagram.md`, diagram nr. 2 (line 88–97)

Brukaren observerte at tilsvarande diagram ser ut til å rendrast fint på den
publiserte GitHub Pages-portalen, og spurde kvifor sjekken likevel feila.

**Rotårsak, del 1 — dette er ikkje portalinnhald i det heile teke:**
`mkdocs/mkdocs.yml` har `docs_dir: docs` (`mkdocs/docs/`), og verken
`utvid-publiseringsflyt-diagram.md` eller `release-arbeidsflyt-diagram.md`
finst under `mkdocs/docs/`. `specs/` er arkiverte planleggingsdokument, aldri
del av det som vert publisert. Diagramma brukaren faktisk såg rendra fint på
portalen, er difor uunngåeleg andre, urelaterte diagram.

**Rotårsak, del 2 — dei to konkrete tilfella er reelt sett to ulike feil,**
begge naturlege for korleis spesifikasjonsdokument er skrivne, ikkje feil i
sjølve dokumentasjonen:

1. `utvid-publiseringsflyt-diagram.md` sitt diagram nr. 2 er eit bevisst
   **kodeutdrag** (manglar `flowchart`/`graph`-deklarasjon, viser berre kva
   linjer som skal leggjast til eit fullstendig diagram lenger oppe i same
   dokument) — ```mermaid`-fencen er brukt for syntaksmerking i prosa, ikkje
   for rendering av eit sjølvstendig diagram.
2. `release-arbeidsflyt-diagram.md` sitt diagram nr. 2 er ei
   plasshaldar-tekst (`[diagram her]`) inni eit **utkast til ein framtidig
   markdown-seksjon**, sjølv nøsta inni ein ytre ` ```markdown `-fence (line
   88–slutt). Ein korrekt markdown-parsar (inkl. mkdocs-material sin) tolkar
   dette som bokstaveleg tekst i den ytre fencen, ikkje som ein ekte,
   sjølvstendig mermaid-blokk — men ekstraksjonssteget «Trekk ut
   mermaid-blokker frå .md-filer» er ein enkel linje-for-linje-skannar
   (`open_re`/`close_re` mot bokstaveleg ` ```mermaid `/` ``` `) som ikkje
   forstår nøsting, og fangar difor plasshaldaren opp som om han var eit
   ekte diagram.

Felles rotårsak for at begge i det heile teke vert sjekka: ekstraksjonssteget
skannar **heile repoet** via `git ls-files -z -- '*.md'`, ikkje berre den
publiserte portalen sitt kjeldeinnhald. `specs/` (både `backlog/` og `done/`)
inneheld naturleg utdrag, utkast og plasshaldarar som aldri er meint å
rendrast åleine — sjekken sitt eigentlege formål (fange broten diagram FØR
dei når portalen) gjeld difor ikkje for desse filene.

**Avklart val (chat, 2026-08-16):** Ekskluder `specs/` frå
mermaid-ekstraksjonen, i staden for å rette opp dei to konkrete filene. Dette
løyser begge tilfella utan å røre arkiverte spesifikasjonar (jf. CLAUDE.md:
"specs/done/ er unntatt — arkiverte spesifikasjonar skal stå urørte"), og
hindrar same falske-positiv-mønster i alle framtidige spesifikasjonar som
naturleg inneheld kodeutdrag/utkast/plasshaldarar med ```mermaid-fencing.

## Steg

1. Endre `git ls-files -z -- '*.md'` (line 137 i
   `.github/workflows/lenkje-og-mermaid-sjekk.yml`, steget «Trekk ut
   mermaid-blokker frå .md-filer») til å ekskludere `specs/` via git sin
   pathspec-eksklusjon: `git ls-files -z -- '*.md' ':!specs/**'` (stadfesta
   verkar korrekt: 442 av 744 sporte `.md`-filer er under `specs/`, 302 står
   att).
2. Oppdater kommentaren over (line 112–113) som i dag forklarar kvifor
   `git ls-files` er brukt, til å òg nemne `specs/`-eksklusjonen og kvifor
   (vis til denne spec-en).
3. Køyr `actionlint` mot den endra workflow-fila.
4. Verifiser lokalt: køyr ekstraksjonslogikken (eller berre
   `git ls-files -z -- '*.md' ':!specs/**'`) og stadfest at ingen
   `specs/*.md`-filer er med i manifestet, samstundes som talet på
   mermaid-blokker frå `mkdocs/docs/` og andre ikkje-spec-filer er uendra.

## Handlingsliste

- [x] Legg til `:!specs/**`-pathspec-eksklusjon i `git ls-files`-kallet
- [x] Oppdater forklarande kommentar
- [x] `actionlint` på endra workflow-fil, ingen `[expression]`-feil
- [x] Lokal verifisering: `specs/` borte frå manifestet, resten uendra

## Utført

Endra `.github/workflows/lenkje-og-mermaid-sjekk.yml` (steget «Trekk ut
mermaid-blokker frå .md-filer»):

- `git ls-files -z -- '*.md'` → `git ls-files -z -- '*.md' ':!specs/**'`
- Kommentaren over utvida til å forklare `specs/`-eksklusjonen og vise til
  denne spec-en.

`actionlint` køyrt — same pre-eksisterande `[shellcheck]`-stilråd (ubrukt
`blockfile` i eit anna steg) som før, ingen `[expression]`-feil.

Lokal verifisering: full simulering av ekstraksjonssteget mot repoet.
Manifestet inneheld **0** `specs/`-filer og **38** mermaid-blokker frå dei
same 34 ikkje-spec-filene som før (mkdocs/docs/{arkitektur, automasjon,
publisering, referanse}/*, src/linkml/fair/fair-metadata/fair-metadata.md)
— talet er identisk med før endringa, som venta sidan ingen av desse filene
var under `specs/`. Dei to falske feila
(`utvid-publiseringsflyt-diagram.md`, `release-arbeidsflyt-diagram.md`) er
no borte frå manifestet.
