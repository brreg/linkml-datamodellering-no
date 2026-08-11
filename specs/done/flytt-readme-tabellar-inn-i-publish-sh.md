# Flytt README.md-tabellgenerering inn i publish.sh, flytt "Publisert N domene(r)"-melding

## Bakgrunn

Brukaren limte inn to `make docs-publish`-loggar — ein ønska rekkjefølgje
og loggen frå siste faktiske køyring — og bad om at rekkjefølgja på kalla
vert justert til å matche den ønska loggen. Etter avklaring med brukaren
(fire spørsmål, sjå under) gjeld dette to konkrete endringar:

1. **README.md-tabellgenerering** (`src/assets/scripts/makefile/generate-readme-tables.sh`)
   køyrer i dag frå `make/50-docs.mk` sin `docs-publish`-target, **før**
   `mkdocs/publish.sh` i det heile vert starta. Han skal i staden køyrast
   **inne i** `publish.sh`, rett etter Steg 1 (opprydding), tidtatt
   individuelt via det etablerte `timed_run`-hjelpemiddelet — same mønster
   som `write_index_from_readme` og `generate_validation_docs` alt følgjer
   (jf. `specs/done/flytt-steg3-til-steg1-med-timing.md`). Han må køyrast
   **før** `write_index_from_readme`, sidan `index.md` vert kopiert direkte
   frå `README.md` — dersom tabellane ikkje er oppdaterte fyrst, kopierer
   `write_index_from_readme` ein utdatert versjon.
2. **"Publisert N domene(r) til mkdocs/docs/"**-meldinga vert i dag logga
   heilt til slutt i scriptet, etter at Steg 3 (mkdocs.yml-generering) er
   ferdig. Ho skildrar derimot resultatet av Steg 2
   (domene/skjema-innhaldet er det som vert "publisert" til
   `mkdocs/docs/`), så ho skal flyttast til rett etter
   domene/skjema-genereringsloopen, **før** `✓ Steg 2 ferdig`-logglinja.

**Eksplisitt avklara med brukaren at følgande IKKJE skal endrast** (jf.
spørsmål 3 og oppfølgingsspørsmålet):

- `make docs-build` skal **ikkje** kallast frå `docs-publish`/`publish.sh`
  eller tidtakast saman med han — held fram som eit heilt separat
  `make`-kall (CI: `make docs-publish && make docs-build`).
- Ingen omnummerering av eksisterande steg — "Steg 2: Generer innhald per
  domene og skjema (parallelt)" og "Steg 3: Generer mkdocs.yml" held fram
  uendra. Den nye README-tabellgenereringa får **ikkje** eit eige
  steg-nummer; han inngår i den same, umerkte tidtakings-blokka som
  `index.md`/`valideringsregler.md` alt gjer (individuelt tidtatt via
  `timed_run`, utan eige `log_step`-banner).
- **"Oppdatert mkdocs/mkdocs.yml"**-meldinga vert **verande** heilt til
  slutt, etter Steg 3 — ho skildrar Steg 3 sitt resultat, og Steg 3 køyrer
  *etter* Steg 2. Å flytte henne til før `✓ Steg 2 ferdig` (som i den
  fyrste lima loggen brukaren viste) ville gjort loggen faktisk feil:
  fila er ikkje generert enno på det tidspunktet. Berre
  "Publisert N domene(r)"-meldinga flyttar.

## Mål

- `generate-readme-tables.sh` køyrer frå `publish.sh`, rett etter Steg 1,
  tidtatt via `timed_run`, **før** `write_index_from_readme`.
- `make/50-docs.mk` sin `docs-publish`-target kallar berre `publish.sh`
  (ikkje lenger `generate-readme-tables.sh` direkte).
- "Publisert N domene(r) til mkdocs/docs/" loggast rett etter
  domene/skjema-genereringsloopen i Steg 2, før `✓ Steg 2 ferdig`.
- "Oppdatert mkdocs/mkdocs.yml" står uendra, etter Steg 3.
- Ingen endring i generert `mkdocs/docs/`-innhald (identisk output, berre
  annan rekkjefølgje/logging internt).

## Steg

1. I `make/50-docs.mk` sin `docs-publish`-target: fjern dei tre linjene
   som gjeld README-tabellgenerering (`log_info "Oppdaterer
   README.md-tabellar..."`, `log_debug "Kommando:
   generate-readme-tables.sh README.md"`, `bash
   src/assets/scripts/makefile/generate-readme-tables.sh README.md`).
   Behald `log_info "Publiserer mkdocs-portal..."` +
   `bash mkdocs/publish.sh`.
2. I `mkdocs/publish.sh`: legg til
   `timed_run "Oppdater README.md-tabellar" bash "$REPO_ROOT/src/assets/scripts/makefile/generate-readme-tables.sh" "$REPO_ROOT/README.md"`
   rett før den eksisterande
   `timed_run "Generer index.md frå README.md" write_index_from_readme`
   -linja (bruk `$REPO_ROOT`-baserte stiar, ikkje relative — `publish.sh`
   sin arbeidskatalog kan ikkje takast for gitt slik han vert kalla frå
   `make/50-docs.mk`).
3. Oppdater kommentaren rett over (linje ~185-190, "README→index.md og
   valideringsregler.md avheng ikkje av noko frå Steg 2 ...") til også å
   nemne README-tabellgenereringa, og til å presisere at
   README-tabellgenereringa må køyrast **før** `write_index_from_readme`
   av korrektheitsgrunnar (index.md skal reflektere oppdaterte tabellar).
4. I `mkdocs/publish.sh` sin domene/skjema-genereringsloop (Steg 2, rundt
   linje 405-448): flytt
   `log_info "${CLR_OK}Publisert ${#ALL_DOMAINS[@]} domene(r) til mkdocs/docs/${CLR_RST}"`
   til rett etter loopen er ferdig, **før** `elapsed2_ms=...`-linja og
   `✓ Steg 2 ferdig`-logglinja.
5. Fjern den tilsvarande `log_info "Publisert ..."`-linja frå slutten av
   scriptet (der han står i dag saman med "Oppdatert mkdocs.yml").
   `log_info "${CLR_OK}Oppdatert mkdocs/mkdocs.yml${CLR_RST}"` vert
   verande uendra på plass, etter Steg 3.
6. `bash -n mkdocs/publish.sh` og `bash -n make/50-docs.mk`-ekvivalent
   (Makefile har ikkje ein direkte syntakssjekk — verifiser i staden med
   `make -n docs-publish` at recipe-linjene ser korrekte ut).
7. Køyr `make docs-publish` og verifiser i loggen at:
   - README-tabellgenerering no skjer rett etter "✓ Steg 1 ferdig", før
     "Generer index.md frå README.md"
   - "Publisert N domene(r)" no står rett før "✓ Steg 2 ferdig"
   - "Oppdatert mkdocs.yml" framleis står heilt til slutt, etter
     "✓ Steg 3 ferdig"
8. Byte-for-byte-verifisering av generert `mkdocs/docs/`-innhald mot ein
   fersk baseline (same metode som
   `specs/done/flytt-steg3-til-steg1-med-timing.md`): `git stash` →
   `make docs-publish` → snapshot → gjenopprett endring → `make
   docs-publish` på nytt → `diff -rq` — forventa 0 avvik utanom det kjende
   tidsstempel-unntaket i topp-`index.md`.

## Akseptansekriterium

- [x] `generate-readme-tables.sh` køyrer frå `publish.sh`, ikkje frå
      `make/50-docs.mk`, tidtatt individuelt via `timed_run`, før
      `write_index_from_readme`
- [x] "Publisert N domene(r)" står rett etter domene/skjema-loopen, før
      `✓ Steg 2 ferdig`
- [x] "Oppdatert mkdocs.yml" står uendra etter Steg 3
- [x] Ingen omnummerering av Steg 2/Steg 3
- [x] `bash -n mkdocs/publish.sh` utan feil
- [x] Byte-for-byte identisk generert `mkdocs/docs/`-innhald mot fersk
      baseline (bortsett frå kjent tidsstempel)

## Utført

Alle 8 steg gjennomførte nøyaktig som planlagt, ingen avvik frå
antakelsane i "Bakgrunn"/"Mål".

**Verifisert korrektheit** (same metode som
`specs/done/flytt-steg3-til-steg1-med-timing.md`):
1. `git stash -u` av endringa, `make docs-publish` køyrt med committa
   (uendra) kode for ein fersk "før"-basislinje, snapshot av
   `mkdocs/docs/`, `mkdocs/mkdocs.yml` og `README.md`.
2. Endringa gjenoppretta (`git stash pop`), `make docs-publish` køyrt på
   nytt.
3. `diff -rq` mellom dei to `mkdocs/docs/`-snapshotta: **0 avvik**,
   bortsett frå det kjende `_Portalen vart sist bygd: ...`-tidsstempelet
   i topp-`index.md`. `mkdocs.yml` og `README.md` byte-for-byte identiske.

**Ny logg-rekkjefølgje** (stadfesta direkte i byggeloggen):
```
✓ Steg 1 ferdig (13.6s)
Genererer auto-genererte tabellar for .../README.md...
.../README.md er oppdatert med auto-genererte tabellar
→ Oppdater README.md-tabellar (8.09s)
→ Generer index.md frå README.md (0.05s)
→ Generer valideringsregler.md (0.02s)
***
Steg 2: Generer innhald per domene og skjema (parallelt)
***
  → ... (per-skjema-linjer)
Publisert 9 domene(r) til mkdocs/docs/
✓ Steg 2 ferdig (104.8s)
***
Steg 3: Generer mkdocs.yml
***
✓ Steg 3 ferdig (0.0s)
Oppdatert mkdocs/mkdocs.yml
```
README-tabellgenereringa køyrer no som fyrste tidtatte kall etter Steg 1
(før README→index.md-kopieringa, som planlagt av korrektheitsgrunnar),
`make/50-docs.mk` sin `docs-publish`-target kallar berre `publish.sh`, og
"Publisert N domene(r)" står no rett før `✓ Steg 2 ferdig` medan
"Oppdatert mkdocs.yml" er uendra etter Steg 3.

**Ikkje gjort:** kopling av `make docs-build` til `docs-publish`/
`publish.sh` (eksplisitt utelaten etter avklaring med brukaren — held
fram som separat `make`-kall), omnummerering av Steg 2/Steg 3 (eksplisitt
utelaten).

## Relaterte filer

- `make/50-docs.mk` — fjerna README-tabellkallet frå `docs-publish`-target
- `mkdocs/publish.sh` — nytt `timed_run`-kall for README-tabellgenerering,
  flytta "Publisert N domene(r)"-melding
- `specs/done/flytt-steg3-til-steg1-med-timing.md` — presedens for
  `timed_run`-mønster og verifiseringsmetode
