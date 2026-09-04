---
name: make-conventions
description: Batching- og wrapper-target-mønster for make/*.mk-generatorar, src/assets/scripts/** og mkdocs/lib/scripts/**, pluss peikar til "ingen stille feil"-prinsippet. Lastast automatisk ved arbeid med filer under make/, src/assets/scripts/ eller mkdocs/lib/scripts/.
paths:
  - "make/**"
  - "src/assets/scripts/**"
  - "mkdocs/lib/scripts/**"
---

## Ingen stille feil

Sjå CLAUDE.md § "Ingen stille feil" for full regel: aldri `> /dev/null 2>&1`
rundt ein kommando som kan feile — bruk `run_logged "<label>" <kommando>` frå
`LOG_FUNCTIONS` (`make/00-settings.mk`). I Python: bruk
`error_handler.log_error()` for uventa unntak, og skriv alltid ei linje til
stderr ved bevisste, mjuke fallback-verdiar.

## Batching vs. parallellisering

To ulike mekanismar — ikkje forveksle:

- **Batching** styrer kor mange **kontainarar** som startast i det heile —
  fleire kommandoar samlar N skjema inn i **éin** `podman run`-prosess i
  staden for éin per skjema (t.d. `batch-generate.py --generator <format>`,
  `batch-lint.py`). Gevinsten er størst for `linkml`-baserte kommandoar, der
  import av `linkml`/`linkml_runtime` (~5-8 s) elles vert betalt på nytt for
  kvart einaste skjema uavhengig av kor lite arbeid sjølve kallet gjer.
- **Parallellisering** styrer kor mange skjema som køyrer **samstundes**
  (fleire prosessar) — handtert av `run-domain-pipeline.sh` for
  `domain-*`-targeta (fase-parallellisering), ikkje eit brukarstyrt jobb-tal.

Sjekk "Batching"-kolonna i `COMMANDS.md` for mekanismen til eit gitt
`gen-*`/`validate-*`-target før du legg til eit nytt.

## Wrapper-target-mønster

Nokre target gjer ikkje arbeidet sjølv, men **delegerer** via eit rekursivt
`$(MAKE) <target>`-kall i oppskrifta — usynleg i `make help`-output. Tre
variantar, ikkje forveksle:

1. **Reelle wrapper-target** — delegerer heile jobben til eit internt target.
   T.d. `mcp-linkml-valider-modell` → `_mcp-valider-modell-with-header`
   (POLICY-deteksjon frå `build.yaml`), `gource-preview`/`gource-video` →
   `_gource-render` (delt render-oppskrift, ulike flagg), `new-modell` med
   `.json`-input → `roundtrip-json-schema` (sjølvverifisering etter
   generering).
2. **"Bygg image berre viss det manglar"-vakt** — same `$(MAKE)`-mønster
   brukt for lat biletbygging: `podman image exists ... || $(MAKE)
   build-docker-*`. **Kontrasterande mønster:** fleire smoke-/test-/
   gource-target listar i staden `build-docker-*` som ein vanleg
   Make-prerequisite (`target: build-docker-x`) — sidan `build-docker-*` er
   `.PHONY`, byggjer desse biletet **på nytt kvar gong** dei køyrer. Vel
   medvite mellom desse to mønstra når du legg til eit nytt target som er
   avhengig av eit container-image — ikkje berre av stil.
3. **Konseptuelle wrapparar** (ikkje `$(MAKE)`-kall) — t.d.
   `validate-informasjonsmodell-instance`/`validate-modellkatalog-instance`
   vert omtala som "convenience wrapper" for `validate-instance`, men kallar
   **ikkje** `make validate-instance` via `$(MAKE)`. Dei gjenbruker same
   underliggande `linkml validate`-logikk direkte, med SCHEMA/INSTANCE-stiar
   auto-utleia frå høvesvis `SCHEMA=`/`ORG=`.

Full referanse med alle target-namn og grunngjeving: `COMMANDS.md` §§
"Logging", "Batching" og "Wrapper-target".
