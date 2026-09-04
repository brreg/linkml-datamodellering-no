# Evaluering: kandidatar for nye Claude Code-skills og -rules

## Bakgrunn

I samband med ein samtale om skilnaden mellom Claude Code sine to
kontekstmekanismar — **rules** (`.claude/rules/*.md`, automatisk lasta basert
på filsti via `paths:` i frontmatter) og **skills** (eksplisitt kalla, anten
via slash-kommando eller ved at Claude tolkar oppgåva som eit treff mot
skill-skildringa) — ønskte brukaren ei evaluering av repoet slik det står i
dag, med ei konkret anbefaling om kva som bør fangast opp i nye rules og/eller
nye skills.

Repoet har i dag **to** rules (`linkml-schema.md`, scopa til `src/linkml/**`,
og `mkdocs-portal.md`, scopa til `mkdocs/**` og
`src/assets/templates/docgen/**`) og **ingen** skills i `.claude/skills/`.

## Metode

Gjennomgått for denne evalueringa:

- Dei to eksisterande rules-filene (fullt innhald)
- `CLAUDE.md` (heile fila, alltid lasta)
- `COMMANDS.md` (alle ~90 dokumenterte `make`-target — **ikkje** auto-lasta
  noko stad i dag)
- `CONVENTIONS.md`, `GOVERNANCE.md`, `PRINCIPLES.md`, `SCOPE.md`
- Katalogstruktur: `make/*.mk` (11 filer), `specs/backlog/` (22 opne),
  `specs/done/` (539 arkiverte), `bugs/` (21 kjende feil)
- Eksisterande MCP-serverar (`mcp-linkml-modell-utkast`,
  `mcp-linkml-begrep-utkast`, `mcp-linkml-validator`) som allereie fungerer
  som eksplisitt-kalla verktøy, altså funksjonelt nært skills

## Funn

Repoet er svært modent og allereie sterkt optimalisert for LLM-samarbeid:
CLAUDE.md pålegg ein fast arbeidsflyt (les tilbake → avklar → spec → utfør →
avslutt), 539 arkiverte spesifikasjonar dokumenterer presedens for nesten
kvart tenkeleg scenario, og dei fleste operasjonelle behov er allereie
dekte av veldokumenterte `make`-target som utviklaren typisk køyrer sjølv
direkte (ikkje noko Claude treng "pakke inn").

Dette avgrensar kor mykje nytt som reelt sett manglar. To konkrete gap peikar
seg likevel ut:

1. **`COMMANDS.md` lastar ikkje automatisk.** Konvensjonane der (ingen stille
   feil / `run_logged`, batching-mønster, wrapper-target-mønster) er nettopp
   den typen detaljerte, fil-scopa reglar rules-mekanismen er laga for — men
   dei finst i dag berre som eit dokument Claude må hugse å lese sjølv.
2. **Éin fleirtrinns, dømmekraft-krevjande arbeidsflyt manglar orkestrering.**
   "Ny domenemodell"-prosessen er dokumentert som statisk tekst
   (`mkdocs/docs/kom-i-gang/ny-domenemodell.md`) og delvis automatisert via
   `make new-modell`, men koplinga mellom scaffolding → modellering etter
   `linkml-schema`-rule → validering → spec-arbeidsflyt er ikkje pakka saman
   noko stad. Dette er nettopp den typen arbeid ein skill er meint for.

## Anbefaling

### A. Nye rules (auto-last, filsti-scopa)

| # | Rule | Scope (`paths:`) | Innhald | Grunngjeving |
|---|---|---|---|---|
| A1 | `make-conventions.md` | `make/**`, `src/assets/scripts/**` | "Ingen stille feil" (`run_logged`, `error_handler.log_error`), batching- og wrapper-target-mønstra frå `COMMANDS.md` §§ Logging/Batching/Wrapper-target | Einaste reelle kunnskapsgap: desse konvensjonane er presise og fil-scopa, men finst i dag berre i eit dokument som ikkje lastar automatisk |
| A2 | `ci-workflows.md` | `.github/workflows/**` | Actionlint-plikta (podman-kommandoen, `[expression]` vs `[shellcheck]`-skiljet) — i dag ein enkeltbullet i alltid-lasta CLAUDE.md | Flytting sparar CLAUDE.md-plass utan tap av dekning, sidan regelen berre er relevant ved nettopp desse filene |

Begge følgjer same mønster som dei to eksisterande rules — smalt scopa,
detaljert, presedens finst alt i repoet.

### B. Nye skills (eksplisitt kall)

| # | Skill | Utløysar | Innhald | Grunngjeving |
|---|---|---|---|---|
| B1 | `ny-domenemodell` | `/ny-domenemodell` eller når oppgåva tydeleg er "lag ny modell" | Spør domene/navn → `make new-modell` → modellering etter `linkml-schema`-rule → `make lint`/`make roundtrip`/`mcp-linkml-valider-modell` → påminning om CLAUDE.md sin spec-arbeidsflyt | Den einaste identifiserte fleirtrinns-arbeidsflyten med reell dømmekraft involvert (ikkje berre éin `make`-kommando) som i dag manglar samla orkestrering |

**Vurdert, men ikkje anbefalt:**

- Skills som berre wrappar eit enkelt `make gen-*`/`make domain-*`-kall
  (docs-publish, gource, mcp-røyktestar): desse køyrer utviklaren typisk sjølv
  direkte i terminalen — ei skill-pakking gir minimal meirverdi.
- Å konvertere dei to **eksisterande** rules til skills (diskutert tidlegare
  i denne økta, men supplert av dette spørsmålet): dei krev nettopp den
  deterministiske filsti-baserte auto-lastinga for å fungere som tenkt
  (garantert kontekst ved kvar redigering av `src/linkml/**`/`mkdocs/**`,
  uavhengig av korleis oppgåva er formulert). Å gjere dei eksplisitt-kalla
  ville fjerne nettopp denne garantien.
- Ein eigen "spec-arbeidsflyt"-skill for CLAUDE.md sin les-tilbake→avklar→
  spec→utfør→avslutt-prosess: denne skal gjelde **alltid**, ikkje berre ved
  eksplisitt kall — høyrer difor heime i CLAUDE.md (der han alt ligg), ikkje
  som skill.

## Prioritert handlingsliste

| # | Tiltak | Fil | Merknad |
|---|---|---|---|
| 1 | Avklar med brukar kva for kandidatar (A1/A2/B1) som skal realiserast | — | Sjå opent spørsmål under |
| 2 | Opprett `.claude/rules/make-conventions.md` | `.claude/rules/make-conventions.md` | Basert på `COMMANDS.md` §§ Logging/Batching/Wrapper-target — berre dersom A1 er ønskt |
| 3 | Opprett `.claude/rules/ci-workflows.md` | `.claude/rules/ci-workflows.md` | Flytt actionlint-bulleten frå CLAUDE.md, oppdater CLAUDE.md til å referere dit — berre dersom A2 er ønskt |
| 4 | Opprett `.claude/skills/ny-domenemodell/` | `.claude/skills/ny-domenemodell/SKILL.md` | Merk: `.claude/skills` finst i dag som ei **tom fil** (ikkje katalog) i repoet — må slettast og erstattast med katalog før skill kan opprettast — berre dersom B1 er ønskt |

## Opent spørsmål

Kva for kandidatar (A1, A2, B1 — kvar for seg) ønskjer du å realisere no?

## Utført

Alle tre kandidatar realiserte:

- `.claude/rules/make-conventions.md` — ny rule, scopa til `make/**` og
  `src/assets/scripts/**`. Batching- og wrapper-target-mønster henta frå
  `COMMANDS.md`, med kort peikar til "ingen stille feil"-prinsippet i
  CLAUDE.md (ikkje duplisert).
- `.claude/rules/ci-workflows.md` — ny rule, scopa til
  `.github/workflows/**`. Actionlint-plikta flytta hit frå CLAUDE.md.
- `CLAUDE.md` — actionlint-bulleten korta ned til ei tilvising til den nye
  rula (same mønster som dei to eksisterande rules-tilvisingane).
- `.claude/skills/ny-domenemodell/SKILL.md` — ny skill som orkestrerer heile
  flyten (avklaring → spec → scaffolding → modellering → validering →
  avslutning). `.claude/skills` fanst frå før som ei tom fil (ikkje katalog)
  og vart erstatta med katalogstruktur.
