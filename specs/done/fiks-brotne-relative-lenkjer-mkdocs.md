# Fiks brotne relative lenkjer til repo-rot-dokument i mkdocs-portalen

## Bakgrunn

`mkdocs build` gav fem `WARNING - Doc file '...' contains a link '...', but
the target '...' is not found among documentation files`, alle for lenkjer
frå sider i `mkdocs/docs/` til dokument som ligg **utanfor** `docs_dir`
(`mkdocs/docs/`) — `CONVENTIONS.md`, `GOVERNANCE.md` og `specs/done/*.md`
ligg på repo-rotnivå/`specs/`, ikkje under `mkdocs/docs/`. Sidan MkDocs sin
lenkje-validator (`validation.links`, sett i `mkdocs.yml`) berre kjenner att
filer som faktisk er kopiert inn i det publiserte sidetreet, vil **ingen**
tal `../`-nivå nokosinne løyse desse lenkjene korrekt internt — dei må vere
absolutte GitHub-URL-ar. Dette er alt den etablerte konvensjonen i repoet
(t.d. `mkdocs/docs/automasjon/modellmanifest-generering.md` sin
`COMMANDS.md`-lenkje og `mkdocs/docs/publisering/publisering-oversikt.md`
sin `GOVERNANCE.md`-lenkje lenger ned i same fil brukar alt
`https://github.com/brreg/linkml-datamodellering-no/blob/main/...`).

Dei fem brotne lenkjene fordelte seg slik:

- `arkitektur/valideringsregler.md` — **generert** side (via
  `generate_validation_docs()` i `mkdocs/publish.sh`, kjelde
  `src/mcp-linkml-validator/policies/README.md`). Kjeldelenkja
  `../../../CONVENTIONS.md#...` er korrekt filsystem-relativ *frå
  policies/README.md sitt eige ståstad* (koherent på GitHub), men vart
  kopiert uendra inn i den genererte mkdocs-sida, der ho ikkje lenger
  resolverer.
- `automasjon/modellmanifest-generering.md` og
  `publisering/publisering-oversikt.md` — **statiske** rettleiingssider med
  feil-forfatta relative lenkjer (burde alltid vore absolutte GitHub-URL-ar,
  jf. konvensjonen alt brukt andre stader i same filer).

## Steg

1. **Statiske sider:** Endra `../../../specs/done/manifest-som-modelldcat-datafil.md`
   og `../../../specs/done/autogenerer-modellmanifest-i-domain-make.md` i
   `mkdocs/docs/automasjon/modellmanifest-generering.md` til absolutte
   `https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/...`-URL-ar.
2. Endra `../../../GOVERNANCE.md#onboarding-av-ny-organisasjon` og
   `../../../GOVERNANCE.md` i
   `mkdocs/docs/publisering/publisering-oversikt.md` til tilsvarande
   absolutte GitHub-URL-ar. Stadfesta at `#onboarding-av-ny-organisasjon`
   faktisk finst som overskrift i `GOVERNANCE.md` (linje 121).
3. **Generert side:** Lagt til ein tredje `sed -E`-regel i
   `generate_validation_docs()` (`mkdocs/publish.sh`) som fangar
   `../../../<ROTDOKUMENT>.md`-mønsteret (repo-rot-dokument med stor
   forbokstav, t.d. `CONVENTIONS.md`, `GOVERNANCE.md`, `SCOPE.md`,
   `PRINCIPLES.md`) og skriv dei om til `$github_base/<ROTDOKUMENT>.md`,
   same mønster som dei to eksisterande reglane for `.yaml`- og
   `specs/done/`-lenkjer. **Ikkje** endra sjølve kjeldelinja i
   `src/mcp-linkml-validator/policies/README.md` — ho er korrekt
   filsystem-relativ på GitHub og skal ikkje endrast der.
4. Verifiser sed-pipelinen manuelt mot kjeldelinja (utan å køyre full
   `make docs-publish`) for å stadfeste korrekt output inkl. anker.
5. `bash -n mkdocs/publish.sh` for syntakssjekk.

## Handlingsliste

- [x] `mkdocs/docs/automasjon/modellmanifest-generering.md`: to lenkjer →
      absolutte GitHub-URL-ar
- [x] `mkdocs/docs/publisering/publisering-oversikt.md`: to lenkjer →
      absolutte GitHub-URL-ar (anker verifisert mot GOVERNANCE.md)
- [x] `mkdocs/publish.sh`: ny sed-regel i `generate_validation_docs()` for
      `../../../<ROTDOKUMENT>.md`-mønsteret
- [x] Sed-pipeline verifisert manuelt mot CONVENTIONS.md-lenkja — korrekt
      output med anker
- [x] `bash -n` syntakssjekk OK
- [x] Full `make docs-publish` + `make docs-build` køyrt — `grep -i
      "WARNING\|ERROR"` mot byggeloggen gav null treff, alle fem
      lenkje-åtvaringane er borte

## Utført

Alle fem lenkjer retta (sjå Steg 1-3). `make docs-publish` (regenererer
`arkitektur/valideringsregler.md` via den nye sed-regelen) og deretter
`make docs-build` vart køyrt i denne økta — bygget fullførte med exit code
0, og ingen `WARNING`/`ERROR`-linjer vart funne i byggeloggen. Som bifangst
vart tidtakinga for Steg 1.4/1.5 i `make docs-publish` (frå førre økt)
verifisert samstundes: delstega summerte til 22.49s mot ei total Steg
1-tid på 22.7s.
