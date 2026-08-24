# Publiser side om standardetterleving i mkdocs-portalen

## Bakgrunn

Brukaren ønsker ei kartlegging av korleis repoet realiserer/etterlever dei
norske rettleiarane og standardane dokumentert på digdir.no, publisert som
ei ny side i mkdocs-portalen.

Research før denne spec-en avdekte at kartleggingsarbeidet **allereie er
gjort**: `specs/backlog/rammeverk-informasjonsforvaltning.md` er ei fullført
spesifikasjon (har eiga `## Utført`-seksjon, datert 2026-08-11) som
syntetiserer 17 eksisterande `avvik-*.md`-kartlegginger og legg til 7 nye
delkartlegginger, strukturert etter Digdirs
[Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626)
(3 pilarar: Veiledere, Standarder og spesifikasjoner, Informasjonsmodellar,
pluss 4 kjerneprinsipp). Commit `d748c713` hevda filen vart flytta til
`specs/done/`, men ho ligg framleis i `specs/backlog/` — ei feilplassering,
ikkje eit ufullført arbeid.

Denne spec-en gjer difor to ting:
1. **Rettar feilplasseringa** — flyttar den ferdige kartlegginga til `specs/done/`.
2. **Publiserer innhaldet** som ei ny, portalvend side under Arkitektur-seksjonen
   i mkdocs, kondensert og omskrive for eit eksternt publikum (nynorsk
   portalspråk, lenkjer i staden for intern spec-sjargong).

Brukarval frå avklaringsspørsmål:
- **Omfang:** berre samle det som alt er dekt — ikkje søk opp nye,
  ikkje-nemnde digdir.no-rettleiarar i denne runden.
- **Plassering:** ny side under det eksisterande "Arkitektur"-avsnittet i
  mkdocs-navigasjonen (saman med Valideringsreglar, AP-NO arkitektur og avvik).
- Eksisterande dekning som IKKJE skal duplisererast, berre lenkjast til:
  - Digdir sine 15 modelleringsreglar + FAIR-prinsipp → `arkitektur/valideringsregler.md`
    (auto-generert av `publish.sh` frå `src/mcp-linkml-validator/policies/README.md`
    — må IKKJE handredigerast)
  - AP-NO-profilane (DCAT/SKOS/ModelDCAT/CPSV/DQV/XKOS) → `arkitektur/ap-no-arkitektur.md`
  - «Slik blir du en god datatilbyder», sjekkliste, «Orden i eget hus»,
    trafikklyssystem → `publisering/publisering-oversikt.md`

## Steg

1. **Flytt feilplassert spec:** `specs/backlog/rammeverk-informasjonsforvaltning.md`
   → `specs/done/rammeverk-informasjonsforvaltning.md` (reint filflytt, ingen
   innhaldsendring — han er alt merkt utført).
2. **Skriv ny side** `mkdocs/docs/arkitektur/standardetterleving.md`:
   - Kort innleiing (kva rammeverket er, kvifor repoet måler seg mot det)
   - Tabell pilar 1 (Veiledere, 7 ressursar) med status + lenkjer
   - Tabell pilar 2 (Standarder og spesifikasjoner, 11 + CPSV-AP-NO) med status + lenkjer
   - Tabell pilar 3 (Informasjonsmodellar, 5) med status + lenkjer
   - Kjerneprinsipp-tabell (4 prinsipp: Orden i eget hus, «Kun én gang»,
     Maskinell datautveksling, Felles standardar)
   - Kort "Attverande gap"-liste (TBX-AP-NO-eksport, `Representasjonspunkt`
     `class_uri`, Person/Enhet-kryssreferanse, URI-peikarar) — transparent om
     kva som ikkje er 100 % dekt
   - "Sjå også"-seksjon: lenkjer til valideringsregler.md, ap-no-arkitektur.md,
     publisering-oversikt.md (relative, portalinterne) og dei 18 `avvik-*.md`/
     `rammeverk-informasjonsforvaltning.md`-filene i `specs/done/` (absolutte
     GitHub-lenkjer, per lenkjeregelen i `.claude/rules/mkdocs-portal.md` —
     `specs/` er ikkje portalinnhald)
   - Følg nynorsk-språkkonvensjonen for dokumentasjon (jf. CLAUDE.md § Skriftspråk)
3. **Legg til i nav:** registrer ny side i `mkdocs/publish.sh` sin heredoc-nav
   under `- Arkitektur:` (rundt linje 622-628), etter "AP-NO arkitektur og avvik".
4. **Legg til i oversiktstabellen:** ny rad i `mkdocs/docs/arkitektur/index.md`
   sin sidetabell.
5. **Valider:**
   - Sjekk at alle interne relative lenkjer peikar til filer som faktisk finst
   - Sjekk at ingen ankerlenkjer brukar handskrivne æ/ø/å-slugs (jf.
     `.claude/rules/mkdocs-portal.md` § Ankerlenkjer)
   - Køyr `make docs-build` (podman) og verifiser at sida byggjer utan
     lenkjefeil, og les gjennom generert HTML/markdown
6. **Avslutning:** commit-meldingsutkast, `## Utført`-seksjon i denne spec-en,
   flytt til `specs/done/`.

## Handlingsliste

- [x] Flytt `specs/backlog/rammeverk-informasjonsforvaltning.md` → `specs/done/`
- [x] Skriv `mkdocs/docs/arkitektur/standardetterleving.md`
- [x] Oppdater nav i `mkdocs/publish.sh`
- [x] Oppdater sidetabell i `mkdocs/docs/arkitektur/index.md`
- [x] Valider lenkjer + `make docs-build`
- [x] Commit-melding + flytt denne spec-en til `specs/done/`

## Utført

Alle steg fullførte 2026-08-24:

- `specs/backlog/rammeverk-informasjonsforvaltning.md` flytta til `specs/done/`
  (var feilaktig verande i backlog sidan 2026-08-11 trass i at spec-en alt
  hadde ei `## Utført`-seksjon og commit-meldinga hevda flyttinga).
- Ny side `mkdocs/docs/arkitektur/standardetterleving.md` skriven: 3
  pilar-tabellar (Veiledere, Standarder og spesifikasjoner,
  Informasjonsmodellar) + kjerneprinsipp-tabell + attverande gap-liste,
  kondensert frå kjeldespec-en og omskrive for portalpublikum. Duplisera
  ikkje eksisterande innhald i `valideringsregler.md`/`ap-no-arkitektur.md`/
  `publisering-oversikt.md` — lenkjer dit i staden, jf. DRY-regelen.
- Sida registrert i navigasjonen (`mkdocs/publish.sh`, under Arkitektur, etter
  "AP-NO arkitektur og avvik") og i sidetabellen i
  `mkdocs/docs/arkitektur/index.md`.
- Validert med `make docs-build` (podman, køyrt med sandbox mellombels
  avslått grunna `newuidmap`-avgrensing i miljøet) — sida byggjer utan
  lenkjefeil, alle 5 tabellar rendrar korrekt, ingen nye åtvaringar utover
  pre-eksisterande `#classes`-ankerfeil på ikkje-relaterte sider.
