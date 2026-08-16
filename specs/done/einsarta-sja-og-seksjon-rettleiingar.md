# Einsarta «Relatert dokumentasjon»-seksjon for alle Rettleiingar-sider

## Bakgrunn

Kartla alle 24 filene under «Rettleiingar»-nav-punktet (sannkjelda er
`mkdocs/publish.sh` line 562–590, ikkje `mkdocs.yml`, jf. CLAUDE.md).
Nedst i dei fleste filene finst ein seksjon med lenkjer til anna
dokumentasjon, men overskrifta og forma varierer sterkt, og fire lenkjer
peikar på filer som ikkje lenger finst på den oppgjevne stien.

### Full oversikt over overskrifter i bruk

| Overskrift | Filer | Tal |
|---|---|---|
| `## Sjå òg` | kom-i-gang/index.md, ny-begrepsmodell.md, arkitektur/index.md, arkitektur-oversikt.md, publisering/index.md, publisering-oversikt.md, publisering-begrep.md, publisering-modell.md, automasjon/index.md, artefakt-generering.md, monitorering.md | 11 |
| `## Sjå også` (stavevariant) | automasjon/index-md-struktur.md | 1 |
| `## Referansar` | arkitektur/ap-no-arkitektur.md | 1 |
| `## Relaterte dokument` | automasjon/modellmanifest-generering.md | 1 |
| `## Relatert dokumentasjon` | automasjon/readme-tabellgenerering.md | 1 |
| Ingen eigen overskrift, berre inline feit tekst («Fullstendig oversikt:», «Rapporter nye problem:») | kom-i-gang/ny-org.md, ny-domenemodell.md | 2 |
| Ingen slik seksjon i det heile | kom-i-gang/build-config.md, kommandoar.md, arkitektur/importhierarki.md, ekstern-bruk.md, arkitektur/valideringsregler.md (auto-generert), om.md | 6 |
| Anna føremål («For bidragsytarar») | index.md (toppnivå) | 1 |

**Avklart val (chat):** Einsarta overskrifta til **`## Relatert
dokumentasjon`** (ikkje `## Sjå òg`, sjølv om den var talmessig
dominerande). Grunngjeving: brei nok til å dekkje det innhaldet faktisk er
(andre rettleiingssider, spec-ar, policy-YAML, eksterne standardar),
naturleg nynorsk, og finst alt brukt éin stad i portalen
(`automasjon/readme-tabellgenerering.md`) — ikkje eit heilt nytt omgrep.

### Kvalitetsproblem utover sjølve overskrifta

1. **`arkitektur/ap-no-arkitektur.md` sin «Referansar»-seksjon har ingen
   faktiske lenkjer** — alle 10 oppføringane er berre plassnamn i
   backticks (t.d. `` `specs/done/avvik-dcat-ap-no.md` — detaljert
   kartlegging DCAT-AP-NO``), ikkje `[tekst](sti)`-markdown-lenkjer. Ikkje
   klikkbare.
2. **`automasjon/index-md-struktur.md` sin «Sjå også»-seksjon har same
   problem** — `CLAUDE.md`, `COMMANDS.md` og
   `mkdocs/docs/kom-i-gang/ny-domenemodell.md` er feittekst, ikkje lenkjer.

### Broten lenkjer funne (4 stk — kjeldene har flytta frå `specs/`/`specs/backlog/` til `specs/done/` utan at lenkjene vart oppdaterte)

| Fil | Broten lenkje | Korrekt sti |
|---|---|---|
| `kom-i-gang/ny-begrepsmodell.md` | `specs/begrep-modellering.md` | `specs/done/begrep-modellering.md` |
| `publisering/publisering-begrep.md` | `specs/publisering-felles-begrepskatalog.md` | `specs/done/publisering-felles-begrepskatalog.md` |
| `publisering/publisering-modell.md` | `specs/publisering-felles-datakatalog.md` | `specs/done/publisering-felles-datakatalog.md` |
| `arkitektur/ap-no-arkitektur.md` | `specs/backlog/spraaktagging-langstring.md` | `specs/done/spraaktagging-langstring.md` |

**Alle andre lenkjer stadfesta OK:**
- Alle 29 relative portallenkjer resolverer til faktisk eksisterande filer
  (verifisert programmatisk mot filsystemet, respekterer mkdocs sin
  relative-sti-semantikk frå kvar kjeldefil).
- Alle absolutte GitHub-blob-lenkjer (`BUGS.md`, `GOVERNANCE.md`,
  `CONTRIBUTING.md`, `COMMANDS.md`, policy-YAML-filer, øvrige
  `specs/done/*.md`) stadfesta å finnast lokalt.
- Alle 4 eksterne lenkjer (SKOS-AP-NO-spesifikasjonen,
  data.norge.no/nb/docs/sharing-data, data.norge.no/specification/
  modelldcat-ap-no, data.norge.no/models) stadfesta `200 OK`.

### Merk — unntak frå CLAUDE.md § Relative vs. absolutte lenkjer i portalinnhald

Toppnivå-`index.md` (kopiert direkte frå `README.md` av `publish.sh`, sjå
`write_index_from_readme`) brukar gjennomgåande **absolutte
`brreg.github.io`-lenkjer** til andre portalsider (13 treff, inkl. i
«For bidragsytarar»-seksjonen: `README-tabellgenerering`). Dette er eit
**medvite unntak**, ikkje eit brot på den nyleg tilførte CLAUDE.md-regelen:
`README.md`/`index.md` er same fil vist i to kontekstar med **usameinelege
relative-sti-basisar** — repo-rot ved GitHub-visning av `README.md`, mot
`mkdocs/docs/`-relativt ved portal-visning av `index.md`. Ei relativ lenkje
kan berre vere korrekt i éin av dei to kontekstane samstundes; absolutt
`brreg.github.io`-lenkje er difor den einaste forma som fungerer likt begge
stader. Tilrår at dette unntaket vert lagt eksplisitt til CLAUDE.md-regelen
i ein separat, liten oppfølgingsspec — ikkje del av omfanget her.

## Steg

1. **Rett dei 4 broten lenkjene** (sjå tabell over) i høvesvis
   `kom-i-gang/ny-begrepsmodell.md`, `publisering/publisering-begrep.md`,
   `publisering/publisering-modell.md`, `arkitektur/ap-no-arkitektur.md`.
2. **Einsarta overskrifta til `## Relatert dokumentasjon`** i alle 14
   filene som i dag brukar noko anna:
   - 11 filer: `## Sjå òg` → `## Relatert dokumentasjon`
     (kom-i-gang/index.md, ny-begrepsmodell.md, arkitektur/index.md,
     arkitektur-oversikt.md, publisering/index.md, publisering-oversikt.md,
     publisering-begrep.md, publisering-modell.md, automasjon/index.md,
     artefakt-generering.md, monitorering.md)
   - `automasjon/index-md-struktur.md`: `## Sjå også` →
     `## Relatert dokumentasjon`
   - `arkitektur/ap-no-arkitektur.md`: `## Referansar` →
     `## Relatert dokumentasjon`
   - `automasjon/modellmanifest-generering.md`: `## Relaterte dokument` →
     `## Relatert dokumentasjon`
   - `automasjon/readme-tabellgenerering.md`: alt korrekt overskrift —
     inga endring.
3. **Gjer `ap-no-arkitektur.md` og `index-md-struktur.md` sine
   `## Relatert dokumentasjon`-oppføringar til faktiske lenkjer**
   (`[tekst](sti)` i staden for plassnamn i backticks/feittekst).
4. **`kom-i-gang/ny-org.md` og `ny-domenemodell.md` manglar ein eigen
   `## Relatert dokumentasjon`-seksjon** — dei har berre inline
   «Fullstendig oversikt: BUGS.md»/«Rapporter nye problem: GitHub
   Issue»-setningar. Vurder å leggje til ein minimal
   `## Relatert dokumentasjon` med relevante kryssreferansar (t.d. til
   systersida i `kom-i-gang/`), i tillegg til (ikkje i staden for) dei
   eksisterande BUGS.md/Issue-setningane.
5. `make docs-build` lokalt etter endringane for å stadfeste at mkdocs sin
   eigen `validation.links` ikkje finn nye broten interne lenkjer.

## Handlingsliste

- [x] Rett 4 broten `specs/`-lenkjer til rett `specs/done/`-sti
- [x] Einsarta 14 avvikande overskrifter til `## Relatert dokumentasjon`
- [x] Gjer `ap-no-arkitektur.md` sine 10 referansar til faktiske lenkjer
- [x] Gjer `index-md-struktur.md` sine 3 referansar til faktiske lenkjer
- [x] Legg til `## Relatert dokumentasjon`-seksjon for
      `ny-org.md`/`ny-domenemodell.md`
- [x] `make docs-build` lokalt, stadfest ingen nye broten interne lenkjer

## Utført

Alle 6 steg gjennomførte:

- 4 broten `specs/`-lenkjer retta til rett `specs/done/`-sti (i
  `ny-begrepsmodell.md`, `publisering-begrep.md`, `publisering-modell.md`,
  `ap-no-arkitektur.md`). Fann og retta òg to relaterte, tidlegare ukjende
  brot i `ap-no-arkitektur.md` som lychee aldri fanga opp (dei var
  plain-text, ikkje ekte lenkjer): `specs/bugs/langstring-rdflib-roundtrip.md`
  → `bugs/langstring-rdflib-roundtrip.md`, og ein andre stad same
  `spraaktagging-langstring.md`-feilen som i tabellen over.
- 14 filer med avvikande overskrift (`Sjå òg` × 11, `Sjå også` × 1,
  `Referansar` × 1, `Relaterte dokument` × 1) samla til
  `## Relatert dokumentasjon`. `readme-tabellgenerering.md` hadde alt rett
  overskrift.
- `ap-no-arkitektur.md` sine 10 «Referansar»-oppføringar og
  `index-md-struktur.md` sine 3 «Sjå også»-oppføringar gjort om frå
  plassnamn i backticks/feittekst til faktiske `[tekst](sti)`-lenkjer
  (rett blanding av relativ/absolutt per CLAUDE.md § Relative vs.
  absolutte lenkjer i portalinnhald).
- Lagt til minimale `## Relatert dokumentasjon`-seksjonar i `ny-org.md`
  (peikar til `ny-domenemodell.md`, `ny-begrepsmodell.md`, GOVERNANCE.md)
  og `ny-domenemodell.md` (peikar til `publisering-modell.md`,
  `importhierarki.md`, `ny-org.md`), i tillegg til dei eksisterande
  BUGS.md/GitHub Issue-setningane.
- `make docs-build` køyrt lokalt (494s) — **null WARNING/ERROR** i
  byggloggen, stadfestar at mkdocs sin eigen `validation.links` ikkje
  fann nokon nye broten interne lenkjer etter endringane.
