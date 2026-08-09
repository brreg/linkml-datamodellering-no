# Plan: Flytt mkdocs-docs-filer til seksjonskatalogar

**Kortnamn:** `mkdocs-flytt-md-filer-til-seksjonar`
**Dato:** 2026-08-09

---

## Bakgrunn

Nav-menyen i `mkdocs/publish.sh` (linje 544–572) grupperer rettleiingssidene
under fire overskrifter — «Kom i gang», «Arkitektur», «Publisering» og
«Automasjon» — og kvar seksjon har allereie ei landingsside
(`kom-i-gang/index.md`, `arkitektur/index.md`, `publisering/index.md`,
`automasjon/index.md`, oppretta i `specs/done/mkdocs-seksjon-index-sider/`).

Sjølve innhaldssidene ligg derimot framleis flatt i `mkdocs/docs/`-rota, slik
at filstrukturen ikkje speglar nav-strukturen. Målet er å flytte kvar
innhaldsside inn i katalogen for seksjonen han høyrer til, og rette alle
lenker (internt i mkdocs-portalen, i genereringsskripta, og i repo-rot-
dokumentasjon som peikar inn i `mkdocs/docs/`) som elles ville brote.

**Avklarte avgjerder:**
- `mkdocs/docs/valideringregler_old.md` (foreldra fil, ikkje i nav) vert
  **sletta** som del av opprydding.
- Tre lenker som er broten *frå før* (uavhengig av flyttinga) vert retta i
  same runde sidan linjene uansett vert redigerte:
  - `ny-org.md` og `ny-domenemodell.md`: `valideringregler.md` → `valideringsregler.md` (manglar «s»)
  - `publisering-oversikt.md`: `../GOVERNANCE.md` → `../../GOVERNANCE.md` (eitt nivå for lite)
  - `ny-begrepsmodell.md`: `begrep/index.md` → `../begrepskatalog/index.md` (feil katalognamn, og treng `../` etter flytting)

---

## Filflytting

| Fil (i dag: `mkdocs/docs/<fil>`) | Ny plassering |
|---|---|
| `ny-org.md` | `kom-i-gang/ny-org.md` |
| `ny-domenemodell.md` | `kom-i-gang/ny-domenemodell.md` |
| `ny-begrepsmodell.md` | `kom-i-gang/ny-begrepsmodell.md` |
| `build-config.md` | `kom-i-gang/build-config.md` |
| `kommandoar.md` | `kom-i-gang/kommandoar.md` |
| `arkitektur-oversikt.md` | `arkitektur/arkitektur-oversikt.md` |
| `importhierarki.md` | `arkitektur/importhierarki.md` |
| `valideringsregler.md` (auto-generert) | `arkitektur/valideringsregler.md` |
| `ap-no-arkitektur.md` | `arkitektur/ap-no-arkitektur.md` |
| `ekstern-bruk.md` | `arkitektur/ekstern-bruk.md` |
| `publisering-oversikt.md` | `publisering/publisering-oversikt.md` |
| `publisering-begrep.md` | `publisering/publisering-begrep.md` |
| `publisering-modell.md` | `publisering/publisering-modell.md` |
| `artefakt-generering.md` | `automasjon/artefakt-generering.md` |
| `index-md-struktur.md` | `automasjon/index-md-struktur.md` |
| `modellmanifest-generering.md` | `automasjon/modellmanifest-generering.md` |
| `readme-tabellgenerering.md` | `automasjon/readme-tabellgenerering.md` |
| `monitorering.md` | `automasjon/monitorering.md` |

`index.md` og `om.md` vert verande i `mkdocs/docs/`-rota (einskildside, ikkje
del av ei firedelt seksjonsgruppe). `valideringregler_old.md` vert sletta.

`valideringsregler.md` er unntaket: han er **auto-generert** av
`mkdocs/publish.sh` Steg 3 (frå `src/mcp-linkml-validator/policies/README.md`)
kvar gong `make docs-publish` køyrer, og er difor i `.gitignore`. Flyttinga
gjeld likevel — output-stien i genereringsskriptet må endrast.

---

## Steg

1. **Flytt filene** med `git mv` til katalogane i tabellen over (behald
   fil-historikk). `mkdocs/docs/valideringregler_old.md` slettast med `git rm`.

2. **Rett interne lenker mellom dei flytta filene** — same-seksjon-lenker
   held fram uendra (bare filnamn), kryss-seksjon-lenker treng eitt
   `../<seksjon>/`-prefiks, og lenker frå ei flytta fil opp til rot-nivå
   (`index.md`, `om.md`, andre domenekatalogar som `begrepskatalog/`,
   `CONVENTIONS.md`, `GOVERNANCE.md`) treng eitt ekstra `../`-nivå.
   Fullstendig liste over lenker som må endrast:

   | Fil | Linje | Frå | Til |
   |---|---|---|---|
   | `kom-i-gang/ny-org.md` | 124 | `](valideringregler.md)` | `](../arkitektur/valideringsregler.md)` |
   | `kom-i-gang/ny-domenemodell.md` | 172 | `](valideringregler.md)` | `](../arkitektur/valideringsregler.md)` |
   | `kom-i-gang/ny-domenemodell.md` | 362 | `](publisering-begrep.md)` | `](../publisering/publisering-begrep.md)` |
   | `kom-i-gang/ny-begrepsmodell.md` | 212, 251 | `](publisering-begrep.md)` | `](../publisering/publisering-begrep.md)` |
   | `kom-i-gang/ny-begrepsmodell.md` | 257 | `](begrep/index.md)` | `](../begrepskatalog/index.md)` |
   | `arkitektur/ekstern-bruk.md` | 134 | `](build-config.md)` | `](../kom-i-gang/build-config.md)` |
   | `arkitektur/valideringsregler.md` | 100 | `](../../CONVENTIONS.md...)` | `](../../../CONVENTIONS.md...)` |
   | `publisering/publisering-oversikt.md` | 107 | `](ekstern-bruk.md#...)` | `](../arkitektur/ekstern-bruk.md#...)` |
   | `publisering/publisering-oversikt.md` | 121 | `](../GOVERNANCE.md)` | `](../../GOVERNANCE.md)` |
   | `publisering/publisering-oversikt.md` | 394 | `](monitorering.md)` | `](../automasjon/monitorering.md)` |
   | `publisering/publisering-begrep.md` | 328 | `](ny-begrepsmodell.md)` | `](../kom-i-gang/ny-begrepsmodell.md)` |
   | `publisering/publisering-modell.md` | 212 | `](ny-domenemodell.md)` | `](../kom-i-gang/ny-domenemodell.md)` |
   | `automasjon/artefakt-generering.md` | 13 | `](importhierarki.md)` | `](../arkitektur/importhierarki.md)` |
   | `automasjon/artefakt-generering.md` | 270 | `](arkitektur-oversikt.md)` | `](../arkitektur/arkitektur-oversikt.md)` |
   | `automasjon/modellmanifest-generering.md` | 230–231 | `](../../specs/done/...)` | `](../../../specs/done/...)` |
   | `automasjon/readme-tabellgenerering.md` | 108, 155, 345 | `](ny-org.md)` | `](../kom-i-gang/ny-org.md)` |
   | `automasjon/readme-tabellgenerering.md` | 344 | `](ny-domenemodell.md)` | `](../kom-i-gang/ny-domenemodell.md)` |
   | `automasjon/monitorering.md` | 357, 402 | `](publisering-oversikt.md)` | `](../publisering/publisering-oversikt.md)` |
   | `automasjon/monitorering.md` | 400 | `](publisering-begrep.md)` | `](../publisering/publisering-begrep.md)` |
   | `automasjon/monitorering.md` | 401 | `](publisering-modell.md)` | `](../publisering/publisering-modell.md)` |
   | `arkitektur/arkitektur-oversikt.md` | 214, 252 | `](artefakt-generering.md)` | `](../automasjon/artefakt-generering.md)` |
   | `arkitektur/arkitektur-oversikt.md` | 215, 254 | `](monitorering.md)` | `](../automasjon/monitorering.md)` |
   | `arkitektur/arkitektur-oversikt.md` | 221, 227, 253 | `](publisering-oversikt.md)` | `](../publisering/publisering-oversikt.md)` |

   Lenker som **ikkje** skal endrast (same seksjon etter flytting):
   `ny-org.md`→`ny-domenemodell.md`, `ny-domenemodell.md`→`build-config.md`,
   `ap-no-arkitektur.md`↔`importhierarki.md`,
   `publisering-oversikt.md`→`publisering-begrep.md`/`publisering-modell.md`,
   `artefakt-generering.md`↔`index-md-struktur.md`↔`modellmanifest-generering.md`,
   `artefakt-generering.md`→`monitorering.md`.

3. **Oppdater dei fire seksjons-`index.md`-sidene** (`kom-i-gang/index.md`,
   `arkitektur/index.md`, `publisering/index.md`, `automasjon/index.md`) —
   dei lenkjer i dag til systersidene sine med eitt `../`-prefiks (skreve i
   påvente av denne flyttinga). Fjern `../`-prefikset sidan sidene no ligg i
   same katalog.

4. **Oppdater `mkdocs/publish.sh`:**
   - Nav-yaml (linje 544–572): legg til seksjonskatalog-prefiks framfor kvart
     filnamn (t.d. `- Bli modelleigar: kom-i-gang/ny-org.md`).
   - `generate_valideringsregler_md()` (rundt linje 117–124): endre
     `output="$DOCS/valideringsregler.md"` til
     `output="$DOCS/arkitektur/valideringsregler.md"`.

5. **Oppdater `mkdocs/lib/scripts/generate-validation-md.py`** (rundt linje
   83–86): relativ lenke frå `<domain>/<schema>/index.md` til
   `valideringsregler.md` må endrast frå `../../valideringsregler/` til
   `../../arkitektur/valideringsregler/` (kommentaren over må òg oppdaterast).

6. **Oppdater `.gitignore`** (linje 16): `mkdocs/docs/valideringsregler.md`
   → `mkdocs/docs/arkitektur/valideringsregler.md`.

7. **Oppdater repo-rot-dokumentasjon** som lenkjer inn i `mkdocs/docs/` med
   dei gamle flate stiane (`specs/done/` er unntatt — arkiverte spesifikasjonar
   rørast ikkje):

   | Fil | Frå | Til |
   |---|---|---|
   | `CLAUDE.md:48` | `mkdocs/docs/importhierarki.md` | `mkdocs/docs/arkitektur/importhierarki.md` |
   | `CLAUDE.md:365` | `mkdocs/docs/ny-domenemodell.md` | `mkdocs/docs/kom-i-gang/ny-domenemodell.md` |
   | `PRINCIPLES.md:30` | `mkdocs/docs/importhierarki.md` | `mkdocs/docs/arkitektur/importhierarki.md` |
   | `GOVERNANCE.md:161` | `mkdocs/docs/ny-org.md` | `mkdocs/docs/kom-i-gang/ny-org.md` |
   | `CODEOWNERS.md:147` | `mkdocs/docs/ny-org.md` | `mkdocs/docs/kom-i-gang/ny-org.md` |
   | `CONTRIBUTING.md:18,49` | `mkdocs/docs/ny-org.md` | `mkdocs/docs/kom-i-gang/ny-org.md` |
   | `CONTRIBUTING.md:20` | `mkdocs/docs/ny-domenemodell.md` | `mkdocs/docs/kom-i-gang/ny-domenemodell.md` |
   | `CONTRIBUTING.md:119` | `mkdocs/docs/monitorering.md#release-arbeidsflyt` | `mkdocs/docs/automasjon/monitorering.md#release-arbeidsflyt` |
   | `CONVENTIONS.md:219` | `mkdocs/docs/ekstern-bruk.md` | `mkdocs/docs/arkitektur/ekstern-bruk.md` |
   | `BUGS.md:12` | `mkdocs/docs/ny-domenemodell.md#kjende-avgrensingar` | `mkdocs/docs/kom-i-gang/ny-domenemodell.md#kjende-avgrensingar` |
   | `bugs/informasjonsmodell-instance-stale-metadata-sti.md:47,61` | `mkdocs/docs/artefakt-generering.md` | `mkdocs/docs/automasjon/artefakt-generering.md` |
   | `bugs/valideringslogg-json-inkonsistent-skjema.md:65` | `mkdocs/docs/artefakt-generering.md` | `mkdocs/docs/automasjon/artefakt-generering.md` |
   | `specs/backlog/plan-demo-repo-dcat-ap-no.md` | flate stiar til `ekstern-bruk.md`/`ny-domenemodell.md` | tilsvarande seksjonssti |
   | `specs/backlog/rename-schema-til-linkml-yaml.md` | flate stiar til fleire av dei flytta filene | tilsvarande seksjonssti |

8. **Rett dei tre pre-eksisterande broten lenkene** (jf. avklarte avgjerder
   over) — inkludert i steg 2-tabellen (`ny-org.md`, `ny-domenemodell.md`,
   `ny-begrepsmodell.md`).

9. **Slett `mkdocs/docs/valideringregler_old.md`.**

10. **Bygg og valider portalen på nytt:**
    ```bash
    make docs-publish
    ```
    Sjekk at:
    - `mkdocs/mkdocs.yml` nav-seksjonen viser dei nye stiane
    - `mkdocs/docs/arkitektur/valideringsregler.md` vert generert på ny plass
    - Ingen `mkdocs build --strict` / lenkesjekk-feil (dersom eit slikt
      make-target finst — sjå `COMMANDS.md`)
    - Stikkprøve: opne 2–3 sider i kvar seksjon og følg eit par interne lenker

11. **Generer commit-melding** (sjå format i CLAUDE.md) og legg til
    `## Utført`-seksjon, flytt so specen til `specs/done/`.

---

## Handlingsliste

- [x] Steg 1 — `mv` av 18 filer, `rm` av `valideringregler_old.md` (ikkje `git mv`/`git rm` — LLM utfører aldri git-kommandoar som endrar VCS-tilstand)
- [x] Steg 2 — rett interne kryss-lenker (tabell over)
- [x] Steg 3 — fjern `../`-prefiks i dei fire seksjons-`index.md`
- [x] Steg 4 — `publish.sh` nav-yaml + `generate_validation_docs()`-output
- [x] Steg 5 — `generate-validation-md.py` relativ lenke + kommentar
- [x] Steg 6 — `.gitignore`
- [x] Steg 7 — repo-rot-dokumentasjon (CLAUDE.md, PRINCIPLES.md, GOVERNANCE.md, CODEOWNERS.md, CONTRIBUTING.md, CONVENTIONS.md, BUGS.md, bugs/*.md, specs/backlog/*.md)
- [x] Steg 8 — rett tre pre-eksisterande broten lenker
- [x] Steg 9 — slett `valideringregler_old.md` (inngår i steg 1)
- [x] Steg 10 — `make docs-publish` + verifiser
- [x] Steg 11 — commit-melding + arkiver spec

---

## Utført

Alle steg gjennomførte som planlagt. Under gjennomføringa vart to avvik frå
planen oppdaga og retta:

1. **Feil i eiga utrekning (steg 2):** Lenka `../../GOVERNANCE.md` i
   `publisering/publisering-oversikt.md` skulle vore `../../../GOVERNANCE.md`
   (tre nivå opp frå `publisering/`, ikkje to). Retta og verifisert med
   `os.path.exists`.
2. **36 lenker i genererte skjemasider var ikkje omfatta av spec-en:**
   Malen `mkdocs/lib/sections/avhengigheiter.sh` genererer ei
   «Importhierarki»-lenke (`../../importhierarki.md`) i kvar
   `<domain>/<skjema>/index.md`. `mkdocs/lib/scripts/parse-dependency-tree.py`
   les òg `importhierarki.md` direkte frå disk (to stadar) for å byggje
   avhengigheitstreet. Begge oppdaterte til den nye stien
   `mkdocs/docs/arkitektur/importhierarki.md`.

Full verifisering: automatisert lenkekontroll av alle 5768 `.md`-filer i
`mkdocs/docs/` etter `make docs-publish` fann **0 broten lenker**.

**Filer endra (utover flyttinga sjølv):**
- `mkdocs/publish.sh` — nav-yaml (seksjonsprefiks) + `generate_validation_docs()` output-sti
- `mkdocs/lib/scripts/generate-validation-md.py` — relativ lenke til `valideringsregler.md`
- `mkdocs/lib/scripts/parse-dependency-tree.py` — filsti til `importhierarki.md` (2 stadar)
- `mkdocs/lib/sections/avhengigheiter.sh` — generert lenke til `importhierarki.md`
- `.gitignore` — `valideringsregler.md`-mønster
- `src/mcp-linkml-validator/policies/README.md` — CONVENTIONS.md-lenke (kjelde til generert `valideringsregler.md`)
- `CLAUDE.md`, `PRINCIPLES.md`, `GOVERNANCE.md`, `CODEOWNERS.md`, `CONTRIBUTING.md`, `CONVENTIONS.md`, `BUGS.md`, `bugs/*.md` (2 filer) — oppdaterte stiar til flytta sider
- `specs/backlog/plan-demo-repo-dcat-ap-no.md`, `specs/backlog/rename-schema-til-linkml-yaml.md` — oppdaterte stiar

**Ikkje gjort:** `mkdocs/docs/arkitektur/valideringsregler.md` er ikkje
manuelt redigert — han er gitignored og vert fullt regenerert av
`make docs-publish` frå `src/mcp-linkml-validator/policies/README.md`.
