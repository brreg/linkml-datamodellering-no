# Vurdering: flytt `src/templates/` — til `mkdocs/` eller `src/assets/`?

## Bakgrunn og mål

`src/templates/docgen/` inneheld 10 Jinja2-malar som `gen-doc` brukar til å
produsere markdown-dokumentasjon frå LinkML-skjema. Målet er at `src/` skal
vere mest mogleg rein og lettforståeleg for nye utviklerar.

Noverande `src/`-rotstruktur:

```
src/
├── assets/                    ← build-infrastruktur (containers + scripts)
├── linkml/                    ← skjema (kjeldekode)
├── mcp-linkml-begrep-utkast/  ← MCP-server
├── mcp-linkml-modell-utkast/  ← MCP-server
├── mcp-linkml-validator/      ← MCP-server
└── templates/                 ← Jinja2-malar for gen-doc
```

`templates/` er det einaste topp-nivå-underkatalogen i `src/` som ikkje
representerer ein sjølvstendig komponent (server eller schemas) og ikkje
høyrer naturleg saman med andre greiner — det er eit lite støttedirektory
med 10 Jinja2-filer.

---

## Referansar (alle stader som må endrast ved ei eventuell flytting)

| Fil | Referanse |
|---|---|
| `Makefile` linje 81 | `--template-directory src/templates/docgen` |
| `.github/workflows/generate.yml` linje 12 | trigger-sti `src/templates/**` |
| `.github/workflows/generate.yml` linje 126 | cache-nøkkel `src/templates/**` |
| `.github/workflows/generate.yml` linje 204 | mkdocs cache-nøkkel `src/templates/**` |
| `README.md` linje 194 | katalogtre-omtale |
| `COMMANDS.md` | same tre-oppføring |

---

## Alternativ 1 — flytt til `src/assets/templates/docgen/`

`src/assets/` er allereie build-infrastruktur-direktoriet: `containers/` har
Dockerfiles, `scripts/` har hjelpeskript. Å legge til `templates/` som eit
tredje underdir er konsistent med det eksisterande mønsteret.

```
src/assets/
├── containers/     ← runtime-miljø (Dockerfiles)
├── scripts/        ← automatiseringsskript
└── templates/      ← Jinja2-malar for gen-doc
    └── docgen/
```

**For:**
- Reduserer `src/`-rota frå 6 til 5 topp-nivåoppføringer — `templates/`
  forsvinn som eige konsept
- Konsistent plassering: templates er build-pipeline-støtte på same nivå som
  scripts og containers
- assets/README.md seier "kjeldekode brukt i samband med LinkML-kommandoar" —
  dette passar for templates
- `gen-docgen-examples.py` ligg allereie i `src/assets/scripts/` og er ein
  del av same docgen-pipeline; nærleiken er ein bonus
- CI-triggeren for `src/templates/**` kan refaktorerast til
  `src/assets/templates/**` utan å endre logikken (assets-containere er
  allereie spesifisert separat i generate.yml)

**Mot:**
- Namnvalet `assets/` er kanskje litt ope (templates er ikkje typisk "assets"),
  men assets/README.md sin noverande forklaring dekkjer det
- Ei ekstra level djupare sti i Makefile og CI

---

## Alternativ 2 — flytt til `mkdocs/templates/docgen/`

`mkdocs/` er portalkonfig-direktoriet med `overrides/` (Material-tema), 
`publish.sh`, `Dockerfile.mkdocs` og statiske sider.

**For:**
- `mkdocs/` er allereie samlingsstad for alt portaltilknytt
- Jinja2-malar i to lag: `overrides/` (portal-layout) og `templates/docgen/`
  (schema→markdown)

**Mot:**
- `gen-doc` er eit *byggepipeline-steg* (schema → artefakt i `generated/`),
  ikkje eit portalmonterings-steg (generated/ → mkdocs/site/).
  At outputen hamnar i mkdocs er ein nedstrømseffekt.
- `mkdocs/overrides/` er eit veldefinert Material-for-MkDocs-konsept; å blande
  inn docgen-malar der svekkjer det konseptet.
- CI-triggerane for `src/linkml/**` og `mkdocs/**` er i dag kvar sine jobbar —
  å flytte templates til mkdocs ville kreve koordinering på tvers av jobbar.

---

## Vurdering og tilråding

**Tilråding: flytt til `src/assets/templates/docgen/`.**

Grunngjevinga for **ikkje** mkdocs (alternativ 2 er avvist i tidlegare iterasjon
av denne spesifikasjonen) held framleis: templates tener byggepipelinen, ikkje
portalmonterings-steget.

Flytt til `src/assets/` (alternativ 1) er derimot ein klar forbetring:
- Det einaste formålet med `src/templates/` som eige topp-nivåkatalog er å
  eksistere. Det er ingen semantisk skilnad mellom `assets/scripts/` og
  `assets/templates/` — begge er støttekode for byggepipelinen.
- Nye utviklerar som opnar `src/` vil sjå fire tydelege konsept: `linkml/`
  (skjema), `mcp-*/` (verktøy), `assets/` (infrastruktur). `templates/` er
  infrastruktur og høyrer heime der.

---

## Endringsplan

Ny plassering: `src/assets/templates/docgen/`

| # | Fil | Endring |
|---|---|---|
| 1 | `src/assets/templates/docgen/` | Flytt heile `src/templates/docgen/` hit |
| 2 | `Makefile` linje 81 | `src/templates/docgen` → `src/assets/templates/docgen` |
| 3 | `generate.yml` linje 12 | `src/templates/**` → `src/assets/templates/**` |
| 4 | `generate.yml` linje 126 | `src/templates/**` → `src/assets/templates/**` |
| 5 | `generate.yml` linje 204 | `src/templates/**` → `src/assets/templates/**` |
| 6 | `README.md` linje 194 | flytt tre-oppføring frå rota til under `assets/` |
| 7 | `COMMANDS.md` | same som README |
| 8 | `src/assets/README.md` | oppdater omtale til å nemne `templates/` |

`mkdocs/docs/index.md` er generert frå README av `publish.sh` og vert
automatisk korrekt etter at README er oppdatert.

Ingen endringar i skjema, datafiler, MCP-serverar, policies eller tests.
