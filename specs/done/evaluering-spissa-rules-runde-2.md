# Evaluering runde 2: meir spissa Claude Code-rules

## Bakgrunn

Oppfølging av `specs/done/evaluering-nye-skills-og-rules.md`, som etablerte
`.claude/rules/make-conventions.md` og `.claude/rules/ci-workflows.md` i
tillegg til dei to opphavlege rules (`linkml-schema.md`, `mkdocs-portal.md`).
Brukaren ønskjer no ein ny, full gjennomgang med sikte på **meir spissa**
rules — smalare `paths:`-scope, meir presist innhald — og peika sjølv på to
konkrete kandidatar: Jinja2-malar og containerhandtering.

## Metode

Gjennomgått for denne runda:

- Alle fire eksisterande rules (fullt innhald og `paths:`-scope)
- `make/01-containers.mk` (alle container-wrapparar: `LINKML_RUN`,
  `AVROTIZE_RUN`, `ASYNCAPI_RUN`, `PYTHON_RUN`, `DOCS_RUN`)
- Alle `Dockerfile*` og `requirements*.txt` under `src/assets/containers/`
- Alle 10 Jinja2-malar under `src/assets/templates/docgen/`
- `CODEOWNERS.md` (frontmatter-format) og tilhøyrande bug
- `src/mcp-linkml-validator/policies/` (README + 5 policy-YAML)
- `mkdocs/lib/scripts/` mot eksisterande rule-dekning
- Alle 21 filer i `bugs/` for containerrelaterte fallgruver
- `CONTRIBUTING.md` § "Nye verktøyavhengigheiter"

## Funn

Dei to eksisterande generiske rules (`make-conventions.md`,
`mkdocs-portal.md`) bundlar fleire delvis usamanhengande underemne under
same brei `paths:`-scope. Det gir støy: ein assistent som redigerer éin ting
(t.d. ein Jinja2-mal) lastar automatisk kontekst om noko heilt anna (t.d.
heading-slug-fella i statiske `.md`-sider). To konkrete, høgverdi
splitt-/nyoppretting-kandidatar peikar seg ut, pluss ein smal, bug-grunngjeven
kandidat og eitt konkret gap i ein eksisterande rule.

## Anbefaling

### C1 — Jinja2-malar (splitt ut frå `mkdocs-portal.md`)

`mkdocs-portal.md` sin `paths:` dekker i dag både `mkdocs/**` (publish.sh-
mekanikk, heading-slug-fella, lenkjereglar — relevant for `.md`-sider og
`publish.sh`) og `src/assets/templates/docgen/**` (Jinja2 whitespace-kontroll
— relevant **berre** for `.jinja2`-filer). Desse to har ulikt naturleg scope
og bør splittast:

- **Ny rule** `.claude/rules/jinja2-templates.md`, scopa strengt til
  `src/assets/templates/docgen/**`. Inneheld heile "Jinja2-template
  whitespace-kontroll"-seksjonen (flytta, ikkje duplisert): hovudregelen om
  ingen indentasjon av Jinja-blokker, `{%-`/`-%}`-whitespace-kontroll,
  tabell-/variabel-/if-blokk-mønstra, og feilsøkingslista.
- `mkdocs-portal.md` sin `paths:` misser `src/assets/templates/docgen/**` og
  held berre `mkdocs/**` — resten av innhaldet er urørt.

### C2 — Containerhandtering (ny rule)

Ingen eksisterande rule dekker `src/assets/containers/**` (9 `Dockerfile*` +
`requirements-python-test.txt`) eller sjølve container-invokerings-mønsteret
i `make/01-containers.mk`. `make-conventions.md` dekker generatormønster
(batching/wrapper-target), ikkje **korleis containerane sjølve vert kalla**.

- **Ny rule** `.claude/rules/container-images.md`, scopa til
  `src/assets/containers/**` og `make/01-containers.mk`. Innhald:
  - `WORK_MOUNT`-mønsteret (`-v "$(CURDIR):/work" -w /work`) og kvifor
    `DOCS_RUN` bryt mønsteret med selektive delmonteringar
  - Kvifor miljøvariablar (`LOGLVL`, `CLR_STEP`/`CLR_RST`/`CLR_OK`/`CLR_ERR`,
    `BATCH_GENERATE_WORKERS`, `GITHUB_REPOSITORY`) må vidareførast
    eksplisitt med `-e <NAVN>` (utan verdi) for å arve frå `os.environ` —
    ikkje hardkodast
  - **BUG-10** (`bugs/podman-interactive-stdin-konsumerer-while-lokke.md`):
    `podman run -i` (brukt av `PYTHON_RUN` for pipe/heredoc-input) **et
    stdin frå omsluttande `while read -r x; do ... done < <(...)`-løkker**
    — konsumerer resten av prosess-substitusjonen sin fd 0, slik at berre
    første element vert prosessert, stille og utan feilkode. Må ha
    `< /dev/null` (eller `<<< "$$var"`) på kvart `$(PYTHON_RUN)`-kall inni
    ei slik løkke, elles brukast `for x in $$(...)`-mønsteret i staden. Dette
    er den mest lumske, reelt oppdaga containerfella i repoet — verdt å
    fange opp automatisk før ho vert reintrodusert i eit nytt target.
  - Attribution-plikta frå `CONTRIBUTING.md` § "Nye verktøyavhengigheiter":
    nytt verktøy i `Dockerfile*`/`requirements*.txt` som endar i eit
    publisert containerbilete → sjekk lisens, oppdater
    `mkdocs/docs/om.md` ved behov

### C3 — CODEOWNERS.md-frontmatter (ny, smal rule)

`CODEOWNERS.md` startar med ein ```yaml`-fence som **ser ut som**, men
**ikkje er**, ekte YAML-frontmatter (`---\n...\n---`) — fila sin eigen
dokumentasjon kallar det feilaktig "frontmatter". Dette gav ein reell,
deterministisk bug (**BUG-16**,
`bugs/codeowners-frontmatter-format-mismatch.md`): éin av tre parallelle
parsarar i repoet gjekk feil på nettopp denne forvekslinga.

- **Ny rule** `.claude/rules/codeowners-format.md`, scopa til `CODEOWNERS.md`
  åleine. Kort innhald: fence-format (ikkje `---`-frontmatter), peikar til
  den kanoniske, delte parsaren (`src/assets/scripts/utils/codeowners.py::load_codeowners()`)
  som **skal** brukast av nye script i staden for eiga parsing, og BUG-16 som
  åtvaring mot å reintrodusere feilen.

### Gap i eksisterande rule (ikkje ny rule, berre utvid scope)

`make-conventions.md` sin peikar til "ingen stille feil" er i dag scopa til
`make/**` og `src/assets/scripts/**` — men CLAUDE.md nemner eksplisitt **òg**
`mkdocs/lib/scripts/**` som eit stad `error_handler.log_error()`/eksplisitt
unntakshandtering skal brukast, og fire av fem script der brukar faktisk
`except`/`error_handler` alt. `mkdocs-portal.md` (som elles dekker
`mkdocs/**`) nemner ikkje denne konvensjonen i det heile. **Anbefaling:**
legg `mkdocs/lib/scripts/**` til `paths:` i `make-conventions.md` — ikkje ei
ny rule, berre ei presisering av ein eksisterande.

### Vurdert, ikkje anbefalt

- **`src/mcp-linkml-validator/policies/**`** (bronze/silver/gold-YAML + eit
  370-linjers README): README-et er alt eit godt strukturert, sjølvstendig
  referansedokument med full Digdir-regel-/FAIR-mapping. Policy-filer
  endrast sjeldan og er høgstakes — ei automatisk-lasta rule ville berre
  duplisere README-et utan å leggje til noko nytt. Les README direkte ved
  behov i staden.

## Prioritert handlingsliste

| # | Tiltak | Fil | Merknad |
|---|---|---|---|
| 1 | Avklar med brukar kva for kandidatar (C1/C2/C3/gap) som skal realiserast | — | Sjå ope spørsmål under |
| 2 | Opprett `.claude/rules/jinja2-templates.md`, fjern Jinja2-seksjonen + `src/assets/templates/docgen/**` frå `mkdocs-portal.md` sin `paths:` | `.claude/rules/jinja2-templates.md`, `.claude/rules/mkdocs-portal.md` | Berre dersom C1 er ønskt |
| 3 | Opprett `.claude/rules/container-images.md` | `.claude/rules/container-images.md` | Berre dersom C2 er ønskt |
| 4 | Opprett `.claude/rules/codeowners-format.md` | `.claude/rules/codeowners-format.md` | Berre dersom C3 er ønskt |
| 5 | Utvid `paths:` i `make-conventions.md` med `mkdocs/lib/scripts/**` | `.claude/rules/make-conventions.md` | Låg innsats, tett gap |

## Opent spørsmål

Kva for kandidatar (C1, C2, C3, gap-fiksen) ønskjer du å realisere no?

## Utført

Alle fire kandidatar realiserte:

- `.claude/rules/jinja2-templates.md` — ny rule, scopa til
  `src/assets/templates/docgen/**`. Jinja2 whitespace-kontroll-seksjonen
  flytta hit (ikkje duplisert).
- `.claude/rules/mkdocs-portal.md` — Jinja2-seksjonen fjerna,
  `src/assets/templates/docgen/**` fjerna frå `paths:`, description
  oppdatert med tilvising til den nye rula.
- `.claude/rules/container-images.md` — ny rule, scopa til
  `src/assets/containers/**` og `make/01-containers.mk`. WORK_MOUNT-mønster,
  eksplisitt env-vidareføring, BUG-10 (podman `-i`-stdin-fella),
  attribution-plikt.
- `.claude/rules/codeowners-format.md` — ny, smal rule scopa til
  `CODEOWNERS.md`. BUG-16-fella (fence vs. ekte frontmatter) og tilvising
  til den kanoniske parsaren.
- `.claude/rules/make-conventions.md` — `paths:` utvida med
  `mkdocs/lib/scripts/**`, description oppdatert.
