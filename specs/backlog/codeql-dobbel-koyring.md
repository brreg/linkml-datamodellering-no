# Plan: CodeQL køyrer i to kopiar per commit

**Kortnavn:** `codeql-dobbel-koyring`
**Dato:** 2026-08-10

---

## Bakgrunn

Etter at eigen `.github/workflows/codeql.yml` vart lagt til og GitHub sin
innebygde "default setup" for code scanning vart forsøkt avslått via `gh`
CLI, køyrde CodeQL framleis i to kopiar for kvar commit.

`gh workflow list --all` viste to aktive workflowar med navnet `CodeQL`:

| ID | Path | Kjelde |
|---|---|---|
| 330621843 | `.github/workflows/codeql.yml` | Eigen workflow (repoet) |
| 280134439 | `dynamic/github-code-scanning/codeql` | GitHub sin dynamiske "default setup"-workflow |

Begge trigga på same push, synkront (t.d. begge kl. 08:51:52 UTC 2026-08-10),
med `Code Quality: Push on main` frå den dynamiske jobben ved sida av
`Analyser (...)`-jobbane frå eigen workflow.

### Funn

- `gh api repos/<owner>/<repo>/code-scanning/default-setup` rapporterte
  konsekvent `"state":"not-configured"` — altså at default setup **er**
  avslått på API-nivå.
- Forsøk på å deaktivere den dynamiske workflowen direkte via
  `PUT /repos/<owner>/<repo>/actions/workflows/280134439/disable` feila med
  `422 Unable to disable this workflow` — denne dynamiske jobben kan **ikkje**
  styrast via `gh workflow disable` eller Actions-API-et sitt
  disable-endepunkt, berre via `code-scanning/default-setup`-endepunktet
  (eller Security-fana i GitHub UI).
- Dette forklarer truleg kvifor eit tidlegare forsøk via `gh` CLI kjentest
  ufullstendig: kommandoen som faktisk verka (avslå default setup) er ikkje
  den same som kommandoen for å deaktivere ein vanleg Actions-workflow.
- Sidan default-setup-status alt viste "av" på undersøkingstidspunktet, og
  siste dobbeltkøyring skjedde svært nær i tid til denne statusendringa, er
  den mest sannsynlege forklaringa at avslåinga nettopp hadde slått gjennom
  hos GitHub, og at ingen nye dupliserte køyringar vil oppstå frå neste push.

## Tiltak

1. **Verifiser med neste push** — etter neste commit til `main`, køyr:
   ```bash
   gh workflow list --all
   gh run list --workflow=codeql.yml --limit 5
   ```
   Stadfest at kun éin CodeQL-relatert køyring ("Analyser (...)"-jobbane frå
   `codeql.yml`) trigger, og at det ikkje kjem noka ny køyring med navn
   "Code Quality: Push on main" (den dynamiske default-setup-jobben) etter
   tidspunktet default setup vart avslått.
2. **Dersom framleis dobbelt** — sjekk på nytt at
   `code-scanning/default-setup` framleis viser `not-configured`. Dersom
   status har gått attende til `configured`, må default setup avslåast på
   nytt via Security-fana i GitHub UI (Settings → Code security → Code
   scanning → Default setup → Disable), sidan API/CLI-vegen synte seg
   utilstrekkeleg deaktiverbar via `gh workflow disable`.
3. **Dersom bekrefta løyst** — flytt denne specen til `specs/done/` med eit
   kort "Utført"-avsnitt som stadfestar éin køyring per commit.
