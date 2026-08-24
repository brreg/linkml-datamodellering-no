# Evaluering: «Modellanalyse»-seksjon per skjema i index.md + per-skjema-køyring i generate-workflowen

## Bakgrunn

Brukaren ønskjer:

1. Ei ny overskrift **`## Modellanalyse`** rett etter `## Valideringsresultat`
   i kvar modell sin genererte `index.md`
2. At «modellanalyse» kan køyrast **for kvart enkelt skjema**, som ein del
   av **generate**-workflowen (`.github/workflows/generate.yml`)

### Kva finst frå før

`make/91-modell-analyse.mk` (jf. `specs/done/modell-analyse-workflow.md` og
`specs/done/modell-analyse-domain-datatype-help.md`, begge arkiverte) har
seks `.PHONY`-target som alle skannar `src/linkml/`:

| Target | Skript | `--name`-støtte (per skjema) | Nettverk |
|---|---|---|---|
| `analyse-similar-classes-domain` | `find-similar-names.py --kind class --scope domain` | Ja | Nei |
| `analyse-similar-classes-all` | same, `--scope all` | Ja | Nei |
| `analyse-similar-slots-domain` | `find-similar-names.py --kind slot --scope domain` | Ja | Nei |
| `analyse-similar-slots-all` | same, `--scope all` | Ja | Nei |
| `analyse-iri-dereferering` | `check-iri-resolution.py --check dereferering` | **Nei** — berre `--domain` | Ja (HTTP HEAD/GET) |
| `analyse-innhaldsforhandling` | `check-iri-resolution.py --check innhaldsforhandling` | **Nei** — berre `--domain` | Ja (HTTP) |
| `analyse-sammendrag` | `summarise-modell-analyse.py` | Nei (les ferdige rapportfiler, skannar ikkje skjema) | Nei |

Desse køyrer i dag **berre** i `.github/workflows/modell-analyse.yml` —
`workflow_dispatch` + vekentleg cron (måndag 07:00 UTC), heilt fråkopla frå
`generate.yml`. Kvart script skriv éin markdown-rapport til stdout; workflowen
omdirigerer til fil, limer inn i `$GITHUB_STEP_SUMMARY` og lastar opp som
artefakt. Rapportane feilar **aldri** CI (informative, ikkje ein
valideringspolicy).

**Viktig, alt implementert:** `find-similar-names.py` (klasse-/slot-likskap)
støttar allereie eit `--name <modell>`-flagg (kombinert med valfri
`--domain`) som avgrensar samanlikninga til éin navngjeven modell mot resten
av kandidatane i scopet. Per-skjema-køyring av **desse to** analysane er
altså allereie mogleg lokalt i dag: `make analyse-similar-classes-domain
DOMAIN=oreg NAME=enhetsregisteret-bvrstiftelsesdokument`. Det som manglar er
(a) at resultatet hamnar i `generated/` slik at `index.md` kan vise det, og
(b) at `check-iri-resolution.py` ikkje har noko `--name`-ekvivalent.

### Korleis index.md vert bygd (mønsteret å følgje)

`mkdocs/lib/generate_index.sh` byggjer kvar modell sin `index.md` ved å
kalle éi funksjon per seksjon, i rekkjefølgje, inn i eitt `{ ... } >
"$out/index.md"`-block. Kvar seksjon er isolert i ei eiga fil under
`mkdocs/lib/sections/*.sh`, nummerert i ein kommentar (`# ... (seksjon N i
index.md)`). Relevant utsnitt av rekkjefølgja:

```
generate_artifacts_table "$out" "$schema"        # seksjon 16
generate_validation_results "$domain" "$schema"  # seksjon 17
generate_changelog "$domain" "$schema"           # seksjon 18 (Versjonslog)
generate_contact_info "$domain" "$schema"        # seksjon 19 (Kontakt)
```

`generate_validation_results` (i `mkdocs/lib/sections/valideringsresultat.sh`)
er malen å kopiere:

- Finn kjeldefila via ein liten helper i `metadata_parsers.sh`
  (`get_validation_json_path`) som peikar til
  `generated/<domain>/<schema>/validation/<siste-versjon>/<policy>.json`
- Om fila finst: deleger heile formateringa til eit eige Python-script,
  `mkdocs/lib/scripts/generate-validation-md.py <json> <domain> <schema>`,
  som skriv den ferdige `## Valideringsresultat`-blokka til stdout
- Om ikkje: skriv ein fallback-`## Valideringsresultat`-blokk med forklarande
  tekst («ikkje tilgjengeleg enno»)

**Kritisk skilnad frå valideringsresultat:** valideringsrapportar er
**committa i git**, versjonslåste per skjemaversjon
(`src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json>`), og
`generate.yml` kopierer berre den nyaste versjonen inn i `generated/` (steget
«Kopier valideringsloggar til generated/»). Dei er determinstiske gitt
skjema+eksempeldata, og verdt å arkivere.

Modellanalyse-rapportar (liknande navn, IRI-dereferering) er **ikkje**
determinstiske gitt berre det eine skjemaet — dei avheng av resten av
repoet (andre skjema i same domene) og, for IRI-sjekkane, av ekstern
nettverkstilstand. Dei bør difor **ikkje** committast per skjema slik
valideringsloggar er — dei bør reknast friskt i CI og leggjast rett i
`generated/`, som eit ephemeral build-artefakt (same status som
ER-diagram-SVG-ar, gen-doc-markdown osv.).

## Evaluering / designval

### 1. Kva analysar skal takast med i den embedda per-skjema-seksjonen?

**Tilråding: berre `analyse-similar-classes-domain` og
`analyse-similar-slots-domain`, køyrt med `--name <skjema>`.** Grunngjeving:

- **Cache-korrektheit.** `generate.yml` sin `generate`-jobb er ein matrise
  **per domene**, og `generated/<domain>/` er cacha på ein nøkkel utleia av
  `hashFiles('src/linkml/<domain>/**')` (+ ein delt «infra»-hash). Ein
  `--scope domain`-analyse avheng berre av skjema **innanfor same domene**
  — konsistent med cache-nøkkelen. Ein `--scope all`-analyse (på tvers av
  alle domene) ville avhengt av **andre** domene sitt innhald, som cache-
  nøkkelen ikkje fangar opp: endrar domene B eit klassenavn, ville domene A
  sin cacha `generated/`-katalog halde fram med å vise eit utdatert
  «liknande klassenavn i domene B»-funn heilt til domene A sjølv får ei
  skjemaendring. Dette er ikkje berre unøyaktig — det er ein reell
  cache-korrektheitsbug. `--scope all` bør difor **ikkje** embeddast per
  skjema; han høyrer heime i den vekentlege, ucacha, heile-repo-jobben han
  alt køyrer i.
- **Kostnad.** Å køyre `--scope all` for **kvart** skjema i **kvar** domene-
  jobb multipliserer kostnaden til `O(skjema i domenet) × O(alle skjema i
  repoet)`, langt dyrare enn den vekentlege jobben sin eine
  `O(alle skjema i repoet)`-køyring.
- **Nettverksavhengige sjekkar (`analyse-iri-dereferering`,
  `analyse-innhaldsforhandling`) bør òg haldast utanfor.** Å køyre HTTP-kall
  per skjema på **kvar push til main** (i staden for vekentleg) aukar
  nettverkstrafikk og flakiness-eksponering monaleg, og resultatet ville
  uansett bli cacha saman med resten av `generated/<domain>/` — ein IRI som
  sluttar å resolvere ville ikkje synast i det embedda resultatet før neste
  skjemaendring i domenet, sjølv om han i realiteten er broten **no**. Den
  vekentlege jobben gir eit ærlegare, alltid-friskt bilete for nettverksstatus
  enn eit cacha, skjema-endrings-utløyst per-skjema-øyeblikksbilete ville
  gjort. Dette er ikkje eit cache-korrektheitsproblem (IRI-sjekken avheng
  berre av eige domene + nettverk, ikkje andre domene), men eit
  ferskleiks-/kost-avvegingsproblem.

  → Den embedda `## Modellanalyse`-seksjonen bør i staden **lenke** til den
  vekentlege `modell-analyse.yml`-køyringa (Actions-fana) for IRI- og
  cross-domain-funn, i staden for å duplisere dei.

### 2. Kor skal per-skjema-analysen køyrast?

**Tilråding: eit nytt, cache-gardert steg i `generate.yml` sin
`generate`-jobb**, syskensteg til det eksisterande «Kopier valideringsloggar
til generated/»-steget (same `if: steps.cache-generated.outputs.cache-hit
!= 'true'`-mønster), **ikkje** som ein ny LinkML-`generators:`-type i
`build.yaml`/`make/10-generator-macros.mk`.

Grunngjeving mot generator-makro-systemet: `make/10-generator-macros.mk` +
`make/11-generator-targets.mk` er bygd spesifikt for å wrappe ekte
LinkML-kodegenerering (`linkml generate <type>`, éin container per
generator-type, styrt av `build.yaml` sin `generators:`-blokk). Modellanalyse
er ikkje LinkML-kodegenerering — det er eit frittståande Python-script med
eiga cross-skjema-samanlikningslogikk, som alt har sitt eige, veletablerte
`make/91-modell-analyse.mk`-modul. Å tvinge det inn i generator-makroen ville
lagt unødvendig kompleksitet til eit system bygd for noko anna, utan å vinne
noko — `make/91-modell-analyse.mk` sine eksisterande target (med `--name`)
er alt akkurat det byggesteget treng.

Konkret nytt steg (etter «Kopier valideringsloggar til generated/», før
«Generer alle artefakter for domenet»):

```yaml
- name: Køyr modellanalyse per skjema for ${{ matrix.domain }}
  if: steps.cache-generated.outputs.cache-hit != 'true'
  run: |
    set -uo pipefail   # ikkje -e — éin skjemafeil skal ikkje stoppe resten
    for schema_dir in src/linkml/${{ matrix.domain }}/*/; do
      schema_name=$(basename "$schema_dir")
      [ -f "$schema_dir/${schema_name}-schema.yaml" ] || continue
      out="generated/${{ matrix.domain }}/$schema_name/model-analyse"
      mkdir -p "$out"
      make analyse-similar-classes-domain DOMAIN=${{ matrix.domain }} NAME="$schema_name" \
        > "$out/similar-classes-domain-report.md" \
        || echo "::warning::analyse-similar-classes-domain feila for $schema_name"
      make analyse-similar-slots-domain DOMAIN=${{ matrix.domain }} NAME="$schema_name" \
        > "$out/similar-slots-domain-report.md" \
        || echo "::warning::analyse-similar-slots-domain feila for $schema_name"
    done
```

`python-pytest`-imaget (som `find-similar-names.py` køyrer i via
`$(PYTHON_RUN)`) er alt bygd/pulla tidlegare i jobben (brukt av
valideringssteget) — ingen ny image-avhengigheit.

### 3. Cache-nøkkel og path-filter må oppdaterast — medviten reversering

`generate.yml` sin `on.push.paths`-blokk ekskluderer i dag eksplisitt:

```
- '!src/assets/scripts/makefile/check-iri-resolution.py'
- '!src/assets/scripts/makefile/find-similar-names.py'
- '!make/91-modell-analyse.mk'
```

— dokumentert i `specs/done/generate-workflow-path-filtrering.md` som
«verifisert IKKJE i kallgrafen» til `generate.yml`. Cache-nøkkelen for
`generated/<domain>/` (i «Cache genererte artefakter»-steget) listar tilsvarande
`make/91-modell-analyse.mk` som eit av dei **medvite utelatne** filsetta,
jf. `specs/done/docs-only-endring-cache-miss-alle-domene.md`.

Med denne spec-en vert **`find-similar-names.py`** og
**`make/91-modell-analyse.mk`** genuint del av kallgrafen (`generate`-jobben
kallar dei no direkte). Begge desse eksklusjonane må **reverserast**:

- Fjern `!src/assets/scripts/makefile/find-similar-names.py` og
  `!make/91-modell-analyse.mk` frå `on.push.paths`
- Legg `src/assets/scripts/makefile/find-similar-names.py` og
  `make/91-modell-analyse.mk` til i cache-nøkkelen sin «infra»-hash
  (`hashFiles(...)`-lista i «Cache genererte artefakter»-steget)

`check-iri-resolution.py` sin eksklusjon (både i path-filter og cache-nøkkel)
skal **stå urørt** — han er framleis ikkje i kallgrafen, jf. avgjerda i punkt
1 om å halde IRI-sjekkane utanfor den embedda seksjonen.

### 4. `check-iri-resolution.py` manglar `--name`

Uviktig for denne spec-en sidan IRI-sjekkar ikkje skal embeddast (punkt 1),
men notert for framtidig referanse: dersom IRI-dereferering seinare skal
kunne køyrast per skjema (t.d. som eit eige `make`-target ein skjemaforfattar
kan køyre lokalt før commit, ikkje nødvendigvis embedda i index.md), manglar
scriptet i dag eit `--name`-ekvivalent til `find-similar-names.py` sitt.
Ikkje del av denne spec-en sin handlingsliste.

### 5. Rendering i index.md

Same to-lags mønster som `## Valideringsresultat`:

- **`mkdocs/lib/scripts/generate-modellanalyse-md.py`** — tek
  `generated/<domain>/<schema>/model-analyse/`-katalogen (eller dei to
  konkrete rapportfilene) som input, skriv éi samla `## Modellanalyse`-blokk
  med `###`-underoverskrifter (`### Liknande klassenavn (same domene)`,
  `### Liknande slotnavn (same domene)`) og ei kort forklarande innleiing
  (i tråd med korleis `valideringsresultat.sh` sin fallback-tekst forklarer
  kva seksjonen viser). Legg til ei linje som peikar til den vekentlege
  `modell-analyse.yml`-køyringa for IRI-dereferering, innhaldsforhandling og
  cross-domain-funn (jf. punkt 1).
- **`mkdocs/lib/sections/modellanalyse.sh`** — kopi av
  `valideringsresultat.sh` sitt mønster: kall ein ny
  `get_model_analyse_dir()`-helper i `metadata_parsers.sh` (analogt med
  `get_validation_json_path`, men peikar til
  `generated/<domain>/<schema>/model-analyse/`), deleger til Python-scriptet
  om katalogen finst, elles skriv ein fallback `## Modellanalyse`-blokk
  («ikkje tilgjengeleg enno — krev at generate-workflowen har køyrt»).

### 6. Innkopling i `generate_index.sh`

```
generate_validation_results "$domain" "$schema"   # seksjon 17
generate_modell_analyse "$domain" "$schema"        # NY seksjon 18
generate_changelog "$domain" "$schema"             # vert seksjon 19
generate_contact_info "$domain" "$schema"          # vert seksjon 20
```

Oppdater dei nummererte kommentarane i `versjonslog.sh` (18→19) og
`kontakt.sh` (19→20) for å halde nummereringa konsistent (kosmetisk, men
etablert konvensjon i dette laget).

## Steg

1. Legg til nytt steg «Køyr modellanalyse per skjema for
   `${{ matrix.domain }}`» i `.github/workflows/generate.yml` sin
   `generate`-jobb (rett etter «Kopier valideringsloggar til generated/»),
   cache-gardert, skriv `similar-classes-domain-report.md` og
   `similar-slots-domain-report.md` til
   `generated/<domain>/<schema>/model-analyse/` per skjema (design i punkt 2).
2. Oppdater cache-nøkkelen i «Cache genererte artefakter»-steget: legg
   `find-similar-names.py` og `make/91-modell-analyse.mk` til «infra»-hash-lista.
3. Fjern `!src/assets/scripts/makefile/find-similar-names.py` og
   `!make/91-modell-analyse.mk` frå `on.push.paths` i `generate.yml`. La
   `!src/assets/scripts/makefile/check-iri-resolution.py` stå urørt.
4. Skriv `mkdocs/lib/scripts/generate-modellanalyse-md.py` (design i punkt 5).
5. Skriv `mkdocs/lib/sections/modellanalyse.sh` + ny
   `get_model_analyse_dir()`-helper i `mkdocs/lib/utils/metadata_parsers.sh`.
6. Wire inn `generate_modell_analyse "$domain" "$schema"` i
   `mkdocs/lib/generate_index.sh`, rett etter `generate_validation_results`
   og før `generate_changelog`. Oppdater seksjonsnummer-kommentarane i
   `versjonslog.sh`/`kontakt.sh`.
7. Køyr `actionlint` mot den endra `generate.yml`
   (`podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/generate.yml`)
   — obligatorisk etter CI-endring per CLAUDE.md.
8. Test lokalt: køyr det nye steget sitt make-kall manuelt for eitt skjema
   (t.d. `make analyse-similar-classes-domain DOMAIN=oreg
   NAME=enhetsregisteret-bvrstiftelsesdokument`), legg resultatet i
   `generated/oreg/enhetsregisteret-bvrstiftelsesdokument/model-analyse/`,
   og køyr `make docs-publish` (eller berre kall `generate_schema_index`
   direkte) — stadfest at `## Modellanalyse` dukkar opp rett etter
   `## Valideringsresultat` i den ferdige `index.md`, og at fallback-teksten
   syner korrekt for eit skjema utan `model-analyse/`-katalog.
9. Oppdater `COMMANDS.md` § «Modell-analyse»: noter at
   `analyse-similar-classes-domain`/`analyse-similar-slots-domain` no også
   køyrer automatisk per skjema i `generate.yml`, med resultatet synleg i
   kvar modell sin dokumentasjonsside — ikkje berre i den vekentlege
   tverrgåande rapporten.

## Ikkje i scope

- **IRI-dereferering/innhaldsforhandling embedda per skjema** — nettverks-
  og ferskleiks-avveginga i punkt 1 gjer dette til eit dårleg val for eit
  cacha, push-utløyst steg. Held fram som vekentleg jobb; den embedda
  seksjonen lenkar dit i staden.
- **Cross-domain (`--scope all`) similar-name-funn embedda per skjema** —
  cache-korrektheitsproblemet i punkt 1. Held fram som vekentleg jobb.
- **`--name`-støtte i `check-iri-resolution.py`** — unødvendig når IRI-sjekkar
  ikkje er del av denne spec-en sitt scope (punkt 4).
- **`build.yaml`-opt-out-flagg for modellanalyse** — vurdert, men ingen
  presedens for opt-out på `analyse-*`-target i dag, og ingen kjend
  brukssak enno. Kan leggjast til seinare dersom eit konkret behov dukkar opp.
- **Endring av `SIMILARITY_THRESHOLD`** — held fram som `make/91-modell-analyse.mk`
  sin eksisterande default (0.8), ikkje overstyrt for det nye steget.

## Utført

Alle ni steg gjennomførte som planlagt.

1. Nytt steg «Køyr modellanalyse per skjema for `${{ matrix.domain }}`» lagt
   til i `.github/workflows/generate.yml`, rett etter «Kopier
   valideringsloggar til generated/», cache-gardert
   (`if: steps.cache-generated.outputs.cache-hit != 'true'`). Loopar over
   `src/linkml/<domain>/*/`, køyrer `analyse-similar-classes-domain` og
   `analyse-similar-slots-domain` med `DOMAIN=`/`NAME=` per skjema, skriv til
   `generated/<domain>/<schema>/model-analyse/*.md`. `set -uo pipefail`
   (ikkje `-e`) + `::warning::` på feil per skjema, slik at éin skjemafeil
   ikkje stoppar resten av loopen eller feilar jobben.
2. Cache-nøkkelen sin «infra»-hash utvida med `make/91-modell-analyse.mk`.
   **Avvik frå plan:** `find-similar-names.py` trong **ikkje** leggjast til
   eksplisitt — han er alt dekt av det breie `src/assets/scripts/**`-mønsteret
   som allereie står i hash-lista, sidan han ligg under den globen. Berre
   `.mk`-fila (som listar eksplisitte `make/*.mk`-filnavn, ikkje ein glob)
   trong leggjast til.
3. `!src/assets/scripts/makefile/find-similar-names.py` og
   `!make/91-modell-analyse.mk` fjerna frå `on.push.paths`.
   `!src/assets/scripts/makefile/check-iri-resolution.py` urørt. Toppkommentaren
   oppdatert til å forklare kvifor.
4. `mkdocs/lib/scripts/generate-modellanalyse-md.py` skriven — les dei to
   rapportfilene, strip kvar sin eigen `# ...`-toppoverskrift, nestar dei
   under `### `-underoverskrifter i éi samla `## Modellanalyse`-blokk med
   forklarande sitatblokk og ei lenke til den vekentlege
   `modell-analyse.yml`-workflowen for IRI-/cross-domain-funn. Gracefully
   fallback («Rapport ikkje tilgjengeleg for denne bygginga») per manglande
   rapportfil, aldri exit ≠ 0.
5. `mkdocs/lib/sections/modellanalyse.sh` skriven (kopi av
   `valideringsresultat.sh` sitt mønster). `get_model_analyse_dir()`-helper
   lagt til i `mkdocs/lib/utils/metadata_parsers.sh` (analogt med
   `get_validation_json_path`, men utan versjons-underkatalog — modellanalyse
   er ikkje versjonslåst/committa).
6. `generate_modell_analyse "$domain" "$schema"` kopla inn i
   `mkdocs/lib/generate_index.sh` rett etter `generate_validation_results`,
   før `generate_changelog`. Seksjonsnummer-kommentarane oppdaterte i
   `versjonslog.sh` (18→19) og `kontakt.sh` (19→20).
7. `actionlint` køyrt mot `.github/workflows/generate.yml` — ingen funn
   (tomt output, exit 0).
8. Testa lokalt: `make analyse-similar-classes-domain`/`analyse-similar-slots-domain`
   med `DOMAIN=oreg NAME=enhetsregisteret-bvrstiftelsesdokument` produserte
   reelle, meiningsfulle funn (19 klassepar, fleire slotpar — m.a.
   `InternasjonalAdresse`/`Person`/`Stedsadresse`/`Vegadresse`/`Virksomhet`
   100 % like andre `enhetsregisteret-bvrinn(felles)`-klassar). Testa
   `generate_modell_analyse` direkte (kjelda `metadata_parsers.sh` +
   `modellanalyse.sh`) for både eit skjema med rapport (korrekt
   `## Modellanalyse`-blokk med begge underseksjonane) og eit skjema utan
   (`enhetsregisteret-bvrbekreftelse`, korrekt fallback-tekst). Testa
   `generate-modellanalyse-md.py` direkte — stadfesta korrekt stripping av
   kjelderapportane sine eigne H1-overskrifter.

   **Avvik frå plan:** køyrde **ikkje** full `make docs-publish` end-to-end
   (ville kravd å generere heile `generated/`-treet for alle 10 oreg-skjema
   pluss alle andre domene — uforholdsmessig kostnad for å verifisere ei
   éin-linjes, mønster-tru kopling til ein alt fungerande call-site). Testa i
   staden kvart nytt lag isolert (Python-script → shell-seksjonsfunksjon →
   fallback-sti), som til saman dekkjer same logikk `generate_index.sh` sitt
   eine nye kall utløyser. Testfilene i `generated/oreg/.../model-analyse/`
   sletta att etter verifisering (byggoutput, `.gitignore`-dekt).
9. `COMMANDS.md` § «Modell-analyse» oppdatert: forklarer `DOMAIN=`/`NAME=`
   og noterer at dei to domene-scopa analysane no også køyrer automatisk per
   skjema i `generate.yml`, synleg i kvar modell sin dokumentasjonsside.

Ingen filer utover dei planlagde vart endra.
