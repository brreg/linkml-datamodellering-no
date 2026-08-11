# Modell-analyse-workflow: liknande namn og IRI-resolusjon

## Bakgrunn

Brukaren har bede om ein ny GitHub Actions-workflow med fem jobbar:

1. Klasser med liknande namn — same domene
2. Klasser med liknande namn — alle domene
3. Slots med liknande namn — same domene
4. Slots med liknande namn — alle domene
5. Test av alle IRI-ar i LinkML-modellane, med logging av dei som ikkje resolverer

Avklarte val (spurt via AskUserQuestion før arbeidet starta):

- **Likskapsmetode:** Fuzzy string-likskap via Python `difflib.SequenceMatcher`
  (ratio på lowercased namn), terskel 80 % som default, overstyrbar via
  `SIMILARITY_THRESHOLD`.
- **IRI-omfang:** `prefixes:`-verdiar + skjemaets eige `id` og
  `default_prefix` — ikkje `class_uri`/`slot_uri`/`see_also`/
  `begrepsidentifikator` (fleire av desse er ikkje meint å opne i nettlesar).
- **Trigger/feiloppførsel:** Same mønster som
  `.github/workflows/lenkje-og-mermaid-sjekk.yml` — vekentleg cron +
  `workflow_dispatch`, loggar til job summary + artefakt, feilar aldri CI.

Klasse-/slot-samanlikninga brukar berre namn **definerte lokalt** i kvart
skjema sin `classes:`/`slots:`-blokk (ikkje importerte namn frå andre
skjema) — elles ville importhierarkiet (t.d. alle AP-NO-profilar som
importerer `common-ap-no-schema`) skapt enorm støy av "duplikat" som i
røynda er éin delt definisjon.

## Steg

1. Skriv `src/assets/scripts/makefile/find-similar-names.py` — eitt script,
   parametrisert med `--kind {class,slot}` og `--scope {domain,all}`, brukt
   av alle fire namne-jobbane (DRY — éi kjelde for samanlikningslogikken).
2. Skriv `src/assets/scripts/makefile/check-iri-resolution.py` — samlar
   unike IRI-ar frå `prefixes`/`id`/`default_prefix` på tvers av alle skjema,
   testar HTTP-resolusjon (HEAD, fallback GET ved 405), rapporterer feil med
   kva skjema som refererer IRI-en. Ingen nye avhengigheiter (stdlib
   `urllib`).
3. Legg til `make/91-modell-analyse.mk` med fem `.PHONY`-target:
   `analyse-similar-classes-domain`, `analyse-similar-classes-all`,
   `analyse-similar-slots-domain`, `analyse-similar-slots-all`,
   `analyse-iri-resolution`. Alle køyrer via `$(PYTHON_RUN)` (containerisert
   Python, jf. `specs/done/containerisering-python-kall.md`).
4. Inkluder `make/91-modell-analyse.mk` i `Makefile`.
5. Dokumenter dei nye targeta i `COMMANDS.md`.
6. Skriv `.github/workflows/modell-analyse.yml` med fem jobbar (éin per
   make-target), same trigger-/rapporteringsmønster som
   `lenkje-og-mermaid-sjekk.yml` (job summary + artefakt-opplasting,
   `continue-on-error`/`|| true` slik at funn aldri feilar CI).
7. Køyr `actionlint` mot den nye workflow-fila (obligatorisk etter CI-endring
   per CLAUDE.md).
8. Test scripta lokalt via `make analyse-similar-classes-domain` osv. og
   `make analyse-iri-resolution` (sistnemnde krev nettverkstilgang —
   verifiser i det minste at scriptet køyrer og produserer gyldig output;
   full IRI-resolusjon kan vere nettverksavgrensa i utviklingsmiljøet).

## Handlingsliste

- [x] Steg 1: `find-similar-names.py`
- [x] Steg 2: `check-iri-resolution.py`
- [x] Steg 3: `make/91-modell-analyse.mk`
- [x] Steg 4: Inkluder i `Makefile`
- [x] Steg 5: `COMMANDS.md`
- [x] Steg 6: `.github/workflows/modell-analyse.yml`
- [x] Steg 7: `actionlint`
- [x] Steg 8: Lokal test

## Utført

**Dato:** 2026-08-11

Alle åtte steg gjennomførte som planlagt. Nøkkelval undervegs:

- **Header-linje til stderr:** `make/91-modell-analyse.mk` sender
  `print_header`-linja til stderr (`1>&2`) slik at `make <target> >
  rapport.md` gir ein rein markdown-fil utan å endre den delte
  `print_header`-makroen brukt av alle andre target.
- **Ingen `|| true` i workflowen:** scripta returnerer alltid kode 0 for
  faktiske funn (det er sjølve rapportinnhaldet, ikkje ein feiltilstand) —
  berre ekte script-/byggefeil skal framleis synast som jobbfeil i CI.

**Lokal verifisering (`make build-docker-python` + alle fem `analyse-*`-target):**

- `analyse-similar-classes-domain`: 72 par (525 klasser sjekka)
- `analyse-similar-classes-all`: 191 par
- `analyse-similar-slots-domain`: 177 par (1198 slots sjekka)
- `analyse-similar-slots-all`: 526 par
- `analyse-iri-resolution`: 17 av 122 IRI-ar resolverte ikkje — i hovudsak
  forventa: `https://w3id.org/linkml/` og fleire `data.norge.no/vocabulary/
  ngr-*`-namespace-IRI-ar returnerer 404 som bare namespace-URI (utan
  konkret ressurssti), `https://example.org/vocab/` og
  `https://fint.example.org/` er plasshaldar-domene i referansemodell-/
  FINT-skjema, og `schema.fintlabs.no` blokkerer med 403. Dette er forventa
  støy for ein informativ sjekk av denne typen, ikkje feil i sjølve
  scriptet.

Ingen eksisterande filer vart endra utover dei planlagde tilføyingane
(`Makefile`, `COMMANDS.md`).
