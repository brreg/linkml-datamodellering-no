# Plan: splitt validering + per-domene-modellanalyse ut i eiga jobb i generate-matrisa

## Bakgrunn

I `generate / oreg`-matrisejobben tek "Valider alle skjema for oreg"
~16 s og "Køyr modellanalyse per skjema for oreg" ~19 s — til saman ~35 s
som i dag køyrer **sekvensielt før** "Generer alle artefakter for
domenet" (den faktiske generator-pipelinen, som tek fleire minutt per
domene, jf. `specs/done/effektiviser-generate-workflow-koyretid.md`).
Brukaren spør om desse to stega kan splittast ut i ei eiga jobb i
matrisa (eller parallelliserast på annan måte) slik at dei ikkje lenger
legg klokketid til domenejobben sin kritiske sti.

Dette er strukturelt same idé som `specs/done/parallelliser-modellanalyse-
tvers-domene.md` (som flytta det tilsvarande **cross-domain**-steget frå
`publish`-jobben til si eiga jobb, parallelt med heile `generate`-
matrisa) — denne specen ser på det **domene-interne** tilfellet: kan dei
to stega flyttast ut av **kvar enkelt** `generate`-matrisejobb, parallelt
med "Generer alle artefakter" for same domene?

## Kartlegging — avhengigheiter

**Ingen reell funksjonell avhengigheit hindrar splitting:**

- "Valider alle skjema" (`run-validation.sh` → `mcp-linkml-validator`
  sitt `flatten-and-validate.bash`) les berre kjeldeskjemaet
  (`src/linkml/<domain>/<schema>/`) — ikkje noko frå `generated/`
- "Køyr modellanalyse per skjema" (etter batchinga i
  `specs/done/effektiviser-modellanalyse-koyretid.md`) les òg berre
  kjeldeskjemaet
- "Generer alle artefakter" (`generate-domain`-actionen: gen-shacl,
  gen-doc, gen-owl osv.) treng **ikkje** valideringsresultatet eller
  modellanalyse-rapportane som input — desse vert berre lesne av
  `mkdocs/publish.sh` seinare, i `publish`-jobben, når heile
  `generated/<domain>/`-treet skal serverast

**Viktig skilje mellom dei to stega — ulik feilsemantikk:**

- **Validering er ei hard sperre**: feilar minst eitt manifest, gjer
  scriptet `exit 1` og **stoppar heile domenejobben** (line 325-328 i
  dagens `generate.yml`) — medvite, jf. kommentaren "Feilar difor bygget
  ved reell valideringsfeil". Dette må halde fram å blokkere heile
  workflowen (via `publish` sin `needs:`-graf), sjølv etter ei splitting.
- **Modellanalyse er reint informativ** — feilar aldri hardt
  (`::warning::`, ikkje `exit 1`).

**Images:** `src/assets/containers/images.json` sine `always_required`-
image er nett `linkml-local`, `python-pytest` og `mcp-linkml-validator` —
akkurat dei tre validering+modellanalyse treng. Ei ny jobb treng difor
**ikkje** den domene-spesifikke `detect-required-images`-logikken (som er
laga for dei *valfrie* generator-avhengige imaga som `gen-domain` bruker)
— berre eit statisk `pull-images`-kall med desse tre, same mønster som
`modellanalyse-tvers-domene`-jobben alt brukar for `python-pytest`.

## Tiltak 1 (anbefalt) — Eiga matrise-jobb «valider-og-analyser» per domene

Ny jobb, same domene-matrise som `generate`:

```yaml
valider-og-analyser:
  name: "valider-og-analyser / ${{ matrix.domain }}"
  needs: [ensure-images, checkout-source]
  strategy:
    matrix:
      domain: ${{ fromJson(needs.checkout-source.outputs.domains) }}
    fail-fast: false
  steps:
    - download source
    - Oppgrader crun
    - Logg inn på GHCR
    - Last images (linkml-local, python-pytest, mcp-linkml-validator — statisk liste)
    - Valider alle skjema for ${{ matrix.domain }}          # flytta verbatim, framleis exit 1 ved feil
    - Kopier valideringsloggar til generated/                # flytta verbatim
    - Køyr modellanalyse per skjema for ${{ matrix.domain }}  # flytta verbatim (alt batcha/parallell internt)
    - upload-artifact: generated-<domain>-checks  (path: generated/${{ matrix.domain }}/)
```

`generate`-jobben mistar dei to stega — vert att med berre cache-sjekk +
"Generer alle artefakter" + upload, dvs. reindyrka til sjølve
artefaktgenereringa.

`publish`-jobben:
- `needs` utvida med `valider-og-analyser` (berre jobb-namnet — sjå
  eige avsnitt under om kvifor dette er nok, utan å liste enkelt-domene)
- `merge-generated-artifacts`-actionen må utvidast: i dag gjer ho
  **éin** `mv generated-merged/generated-$domain generated/$domain` per
  domene (eitt artefakt = éin flytting). Med to artefakt per domene
  (`generated-<domain>` frå `generate`, `generated-<domain>-checks` frå
  den nye jobben) må ho i staden **flytte det eine, så kopiere/slå saman
  innhaldet frå det andre inn i same katalog** — trygt sidan dei skriv
  til **ikkje-overlappande** underkatalogar (`docs/`, `*.ttl` osv. frå
  `generate`, versus `*/validation/`, `*/model-analyse/` frå den nye
  jobben)

**Caching:** **ikkje** cache den nye jobben. Sidan modellanalyse-delen
alt er batcha ned til ~19 s og valideringa til ~16 s (til saman ~35 s),
er cache-kompleksiteten (eigen cache-key-formel, koordinert med
`generate`-jobben sin separate cache, risiko for cache-inkonsistens
mellom dei to jobbane) ikkje verdt det — køyr han friskt kvar gong, same
avgjerd som vart teken for `modellanalyse-tvers-domene`
(`specs/done/parallelliser-modellanalyse-tvers-domene.md`).

**Stadfesta: `needs: [generate, valider-og-analyser]` på jobb-nivå er
NOK til å blokkere `publish` heilt dersom validering feilar for eitt
einaste domene** — dette krev ingen ekstra logikk å byggje. GitHub
Actions handterer ei matrise-jobb som **éi logisk eining** i
`needs`-grafen: ein nedstraums-jobb sin implisitte standardvilkår er
`success()` for **alle** jobbane han treng, og for ei matrise-jobb betyr
det **alle matrise-beina** hennar. `fail-fast: false` (alt sett på begge
matrisene) endrar berre om GitHub Actions kansellerer **andre** bein ved
fyrste feil (han gjer det ikkje — alle domene får køyre/rapportere) —
han endrar **ikkje** om `publish` køyrer etterpå. Feilar
`valider-og-analyser` for t.d. `oreg` åleine, vert heile `publish`-jobben
hoppa over ("skipped" i Actions-UI), akkurat som `generate` alt gjer i
dag dersom validering (i dagens sekvensielle steg-plassering) feilar for
eitt domene. Det trengst altså **ingen** liste over enkelt-domene i
`needs:` — berre dei to jobb-namna.

**Vurdert og forkasta: separate jobbar for validering og modellanalyse
kvar for seg** (i staden for éi kombinert jobb). Ville gitt reinare
feilsemantikk (ei jobb per bekymring), men **doblar** talet på nye
jobb-instansar (2×9=18 i staden for 1×9=9 for eit repo med 9 domene) —
dobbel jobb-oppsett-overhead (runner-oppstart, checkout, crun-oppgradering,
GHCR-innlogging, image-pull) for eit steg-par som til saman berre tek
~35 s. Marginal gevinst, ikkje verdt kompleksiteten. Éi kombinert jobb
(validering **og** modellanalyse) held oppsett-overheaden nede på éin
ekstra jobb per domene.

**Kjend, ikkje-triviell risiko — jobb-oppsett-overhead kan ete opp
gevinsten:** ei HEILT NY GitHub Actions-jobb har fast kostnad (runner-
tildeling, `download-artifact`, crun-oppgradering, GHCR-innlogging,
image-pull) FØR sjølve arbeidet startar. For `modellanalyse-tvers-
domene`-jobben (same oppsettsmønster, køyrer éin gong for heile repoet)
vart denne overheaden aldri isolert målt eksplisitt — berre stadfesta at
sjølve analysesteget tok den forventa tida. **For denne specen sitt
tiltak, som multipliserer med talet på domene (9), er det ikkje
sjølvsagt at netto veggklokke-gevinst er positiv** dersom
jobb-oppsettet i seg sjølv tek fleire titals sekund. Dette kan **ikkje**
verifiserast lokalt (GitHub Actions-jobbschedulering/runner-tildeling er
ikkje noko `make`/podman-kommandoar kan simulere) — mål faktisk
veggklokketid i neste CI-køyring før tiltaket reknast som stadfesta
vellukka.

## Tiltak 2 (alternativ, lågare jobb-overhead, men ny og uprøvd teknikk i dette repoet) — Bakgrunn dei to stega i SAME jobb

I staden for ei ny jobb: start validering + modellanalyse som
**bakgrunnsprosessar** heilt i starten av den eksisterande `generate`-
jobben (før "Generer alle artefakter"), la dei køyre vidare **på tvers av
steg-grensa** (`disown`/`setsid` slik at dei ikkje vert drepne når steget
sin eigen shell-prosess avsluttar), og legg til eit nytt steg **etter**
"Generer alle artefakter" som ventar på ein fullført-markørfil og
handhevar valideringa sin `exit 1`-sperre basert på den lagra exit-koden.

**Fordelar:** ingen ny jobb → ingen ny runner-oppsett-overhead, ingen
endring i `merge-generated-artifacts`, ingen cache-koordinering mellom
jobbar.

**Ulemper:** dette er ein **heilt ny teknikk i dette repoet** — det finst
i dag ingen stad i `.github/workflows/`/`.github/actions/` som bakgrunnar
ein prosess i eitt steg og hentar resultatet i eit seinare steg (verifisert
ved grep). Sjølv om steg i same jobb deler filsystem/runner, må
prosess-overleving på tvers av steg-grensa **stadfestast empirisk i reell
CI** før ein kan stole på han — og feilar denne mekanismen stille (t.d.
fordi runneren sitt shell-oppsett drep bakgrunnsprosessar ved steg-slutt
likevel), ville valideringa sin harde sperre **slutte å fungere
korrekt** utan at det er openbert — ein alvorleg regresjonsrisiko på ei
sjekk som i dag medvite skal stoppe bygget.

## Anbefaling

**Start med Tiltak 1** (kombinert `valider-og-analyser`-jobb, ikkje
cacha) — det er den GitHub Actions-native, veldokumenterte
parallellitetsmekanismen (same mønster som alt er verifisert i
`specs/done/parallelliser-modellanalyse-tvers-domene.md`), og unngår heilt
den nye, uprøvde prosess-overlevings-risikoen frå Tiltak 2 på ei sjekk som
i dag er ei medviten, hard byggje-sperre. Mål faktisk veggklokke-effekt i
neste reelle CI-køyring (jf. risikoavsnittet over) — dersom jobb-
oppsettoverheaden viser seg å ete opp mesteparten av dei ~35 sekunda, bør
Tiltak 2 vurderast som oppfølging (då med eit dedikert, isolert
eksperiment i eit draft-PR før det landar, sidan mekanismen er uprøvd).

## Handlingsliste (Tiltak 1)

1. Ny jobb `valider-og-analyser` i `generate.yml`
   (`needs: [ensure-images, checkout-source]`, same domene-matrise som
   `generate`), flytt dei to stega + deira førestillingar
   (crun/ghcr-login/image-pull) dit uendra
2. Fjern dei to stega (og deira `if: cache-hit`-vakter, sidan denne
   jobben no eig dei) frå `generate`-jobben
3. Utvid `.github/actions/merge-generated-artifacts` til å handtere to
   artefakt per domene (flytt det eine, kopier/slå saman det andre inn i
   same katalog)
4. `publish`-jobben: legg `valider-og-analyser` til i `needs`
5. **Køyr `actionlint` mot `generate.yml`** (og
   `merge-generated-artifacts/action.yml` viss den også er ein workflow-
   fil actionlint dekkjer) etter kvar endring
6. Verifiser lokalt så langt råd er (`make -n`/dry-run av dei nye
   steg-samansetjingane, `bash -n` på nye/endra shell-blokker) — sjølve
   veggklokke-gevinsten kan berre stadfestast i reell CI, jf.
   risikoavsnittet
7. Følg opp med ei reell CI-måling: samanlikn total `generate / oreg`-
   jobbtid + `valider-og-analyser / oreg`-jobbtid (parallelt) mot dagens
   sekvensielle sum, og heile workflowen sin totale veggklokketid før/etter

## Opne spørsmål (avklar ved implementering, ikkje i denne specen)

- Eksakt namngjeving på den nye jobben/artefaktet (`valider-og-analyser`,
  `generated-<domain>-checks`) — arbeidsnamn, juster for konsistens ved
  implementering.
- Skal `merge-generated-artifacts` sin nye "kopier/slå saman"-gren i det
  heile handtere eit manglande artefakt-fall (t.d. logge ei åtvaring)?
  **Avklart:** `needs`-grafen gjer dette spørsmålet i praksis ugyldig —
  `publish` køyrer aldri i det heile dersom `valider-og-analyser` feila
  for noko domene (sjå eige avsnitt i Tiltak 1), så merge-steget vil
  aldri møte eit delvis/manglande artefakt frå ein feila jobb. Ei
  defensiv åtvaring der kan framleis leggjast til som god vane (t.d. ved
  eit artefakt som forsvann av andre grunnar, som opplastingsfeil), men
  er ikkje eit krav for at feilsemantikken skal vere korrekt.

## Utført

Tiltak 1 gjennomført (Handlingsliste steg 1-6 — steg 7, reell CI-måling,
kan berre gjerast av ei faktisk CI-køyring):

1. Ny jobb `valider-og-analyser` i `generate.yml`, same domene-matrise
   som `generate` (`needs: [ensure-images, checkout-source]`, ikkje
   cacha). Dei tre stega ("Valider alle skjema", "Kopier
   valideringsloggar til generated/", "Køyr modellanalyse per skjema")
   flytta **verbatim** (uendra shell-innhald) frå `generate`-jobben, med
   `if: cache-hit`-vaktene fjerna (denne jobben har ingen eigen
   cache-gate). Statisk `pull-images`-kall med dei tre `always_required`-
   imaga (`linkml-local`, `python-pytest`, `mcp-linkml-validator`) i
   staden for `detect-required-images`. Ny opplasting
   `generated-<domain>-checks`.
2. Dei tre stega fjerna frå `generate`-jobben — att er berre cache-sjekk
   + "Generer alle artefakter" + upload.
3. `.github/actions/merge-generated-artifacts/action.yml` utvida: flyttar
   framleis `generated-<domain>` (base), og kopierer/slår no i tillegg
   saman `generated-<domain>-checks` inn i same katalog (`cp -r`, trygt
   sidan innhaldet ikkje overlappar filbanar).
4. `publish`-jobben sin `needs` utvida med `valider-og-analyser`.
5. `actionlint` køyrd og godkjend (reint) mot `generate.yml`. YAML-
   syntaksen til `merge-generated-artifacts/action.yml` stadfesta gyldig
   (`yaml.safe_load`).
6. **Verifisert reelt** (sandbox deaktivert for podman, same grunn som
   dei føregåande spec-ane i denne serien):
   - Simulerte begge jobbane sitt arbeid for `samt`-domenet med dei
     faktiske kommandoane (`run-validation.sh`, kopieringssteget,
     `analyse-similar-domene-batch`, `analyse-lokal-modellanalyse-domene`,
     og — separat — det ekte `make domain-samt`), og testa den nye
     `merge-generated-artifacts`-logikken direkte på begge resultat-
     tre: `validation/` og `model-analyse/` frå den eine, `docs/`,
     `diagrams/`, `docgen-examples/` frå den andre, slo seg saman utan
     nokon filbane-konflikt
   - `make docs-publish` + `make docs-build` på det samanslåtte treet:
     generert `index.md` for `samt-bu` viser både
     `## Valideringsresultat` (frå `validation/`) og alle åtte
     Modellanalyse-underoverskrifter korrekt — ingen `ÅTVARING`, ingen
     brotne lenkjer
   - **Konkret måledata:** `make domain-samt` (den faktiske "Generer
     alle artefakter"-jobben sitt arbeid) tok **27,2 s** for dette eine-
     skjema-domenet — mindre enn dei ~35 s validering+modellanalyse
     brukar. For små domene som `samt` er difor den nye jobben sjølv den
     *lengste* av dei to, og veggklokke-gevinsten vert
     `max(35, 27) ≈ 35 s` (frå `35 + 27 = 62 s` sekvensielt) i staden
     for at heile 35-sekundersbolken forsvinn heilt inn i skuggen av
     artefaktgenereringa, slik det ville vore for eit stort domene som
     `oreg`. Stadfesta i tråd med spec-en sitt eige varsel om at
     jobb-oppsettoverhead + domenestorleik avgjer nettoeffekten — sjølve
     jobb-oppsettoverheaden (runner-tildeling, checkout, image-pull) kan
     **ikkje** målast lokalt, berre i reell CI.
   - `make roundtrip SCHEMA=samt-bu-schema.yaml`: `roundtrip-json` OK,
     `roundtrip-ttl` feilar — alt dokumentert BUG-3
     (`bugs/mappingerror-rdflib-roundtrip.md`, `samt-bu` står alt
     oppført som kjend feilande), inga ny regresjon
   - Rydda opp mellombelse biverknader av lokal testing (`make
     domain-samt` regenererte `samt-bu-manifest.yaml` og skreiv
     `src/linkml/samt/samt-bu/validation/` til kjeldetreet) — reverterte
     desse før avslutning, dei er ikkje del av denne endringa

**Avvik frå opphavleg plan:** ingen. Handlingsliste steg 7 (reell
CI-tidsmåling) attstår og krev ei faktisk køyring av workflowen — kan
ikkje gjerast frå denne økta.
