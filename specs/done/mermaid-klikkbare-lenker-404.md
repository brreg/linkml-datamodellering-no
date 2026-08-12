# Plan: Fiks 404 på klikkbare lenkjer i mermaid-klassediagram

**Kortnamn:** `mermaid-klikkbare-lenker-404`
**Eksempel:** `mkdocs/docs/oreg/enhetsregisteret-bvrinn/klasser/innrapportering.md`
**Dato:** 2026-08-12

---

## Bakgrunn

Alle klasse- og slot-sider i dokumentasjonsportalen har eit mermaid
`classDiagram` med klikkbare `click <Namn> href "..."`-direktiv på klassenamn
og relaterte slot/type-namn. På GitHub Pages (case-sensitivt Linux-filsystem)
gir **alle** desse lenkjene 404. Feilen er verifisert konsekvent på tvers av
heile portalen — 943 genererte `.md`-filer inneheld til saman 9143
`click ... href`-direktiv, og alle er broten.

### Rotårsak

`mkdocs/lib/copy_artifacts.sh` (steg "Kopier gen-doc markdown-filer til
klasser/-underkatalog") gjer to ting etter at LinkML sin `gen-doc` har
produsert markdown med mermaid-diagram:

1. Filnamn vert gjort om til lowercase (for å unngå kollisjon på
   case-insensitive filsystem ved lokal utvikling).
2. Interne lenkjer i standard Markdown-format `[tekst](Namn.md)` vert
   omskrivne til lowercase via:
   ```bash
   find "$out/klasser" -maxdepth 1 -name "*.md" \
       -exec sed -i 's/](\([^)]*\.md\))/](\L\1)/g' {} +
   ```

Denne sed-regelen matchar **berre** `](...​.md)`-mønsteret. Mermaid
`click`-direktiv følgjer eit heilt anna format og vert aldri fanga opp:

```
click Innrapportering href "../Innrapportering/"
click Fagsystemreferanse href "../Fagsystemreferanse/"
click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
```

Dette gir to distinkte feilmønster:

- **Klasse-/slotnamn (dei fleste tilfella):** href brukar PascalCase
  (`../Innrapportering/`), men den faktiske genererte fila heiter
  `innrapportering.md` (lowercase). Case-mismatch → 404 på GitHub Pages.
- **Typar (t.d. `Uriorcurie`):** LinkML sin `gen-doc`-mermaid-generator
  brukar her URI-en til XSD-typen (`http://www.w3.org/2001/XMLSchema#anyURI`)
  som href i staden for typenamnet. Sidan URI-en vert sett inn som eit
  stiSegment i ein relativ lenkje, blir resultatet ei ugyldig, ikkje-eksisterande
  sti — sjølv om det **finst** ei gyldig side (`uriorcurie.md`) som burde
  vore målet.

`mkdocs.yml` undertrykkjer allereie åtvaringar for akkurat dette
(`validation.links.not_found: ignore`, sjå kommentar i
`mkdocs/publish.sh` rundt linje 461-465) — det vil seie at problemet var
kjent, men ikkje retta, berre skjult frå `mkdocs build`-loggen.

**Viktig avgrensing:** mkdocs sin innebygde lenkje-validator jobbar på det
*rendra HTML-treet* (`<a href>`-element) etter at Markdown er konvertert —
ikkje på rå Markdown-tekst. Mermaid-diagramma vert rendra via
`pymdownx.superfences` som eit `<pre class="mermaid">`-blokk med rå tekst
inni; `click ... href`-direktiva der er difor **usynlege** for
`validation.links`-sjekken uansett innstilling. Å skru på lenkje-validering
fangar altså opp den andre kategorien nemnd i kommentaren (systematiske
fragment-lenkjer, og eventuelle attverande `[tekst](Namn.md)`-lenkjer som
ikkje vart korrekt lowercase-omskrivne) — men **ikkje** regresjonar i
`click`-hrefs spesifikt. Den dedikerte regresjonstesten i steg 6 er difor
framleis naudsynt som eige sikkerheitsnett for mermaid-lenkjene.

### Stadfesta fiks

Alle `click <Namn> href "..."`-direktiv kan rettast med éin regel: ignorer
den eksisterande href-verdien og bygg ho på nytt frå namnet som allereie
står i `click`-statementet (som alltid samsvarar med det tilhøyrande,
lowercase-omdøypte filnamnet):

```bash
sed -E 's|click ([A-Za-z0-9_]+) href "[^"]*"|click \1 href "../\L\1\E/"|g'
```

Verifisert manuelt mot alle tre tilfella over — gir korrekt output:
```
click Innrapportering href "../innrapportering/"
click Uriorcurie href "../uriorcurie/"
click VirksomhetsinformasjonHovedenhet href "../virksomhetsinformasjonhovedenhet/"
```

Denne tilnærminga er meir robust enn å prøve å lowercase den eksisterande
href-strengen (slik den noverande `.md`-lenkje-regelen gjer), fordi ho ikkje
er avhengig av at href-verdien er velforma i utgangspunktet — ho utleier
alltid rett mål frå namnet i `click`-statementet.

---

## Steg

1. Legg til ein ny sed-regel i `mkdocs/lib/copy_artifacts.sh`, rett etter
   den eksisterande "Oppdater alle interne .md-lenkjer til lowercase"-regelen,
   som omskriv `click <Namn> href "..."` til
   `click <Namn> href "../<lowercase(Namn)>/"` for alle `.md`-filer i
   `$out/klasser`.
2. Kjør `make docs-publish` (eller tilsvarande target som kallar
   `copy_artifacts.sh`) og stadfest at genererte klasse-/slot-sider no har
   korrekte, lowercase `click ... href`-verdiar utan innbakte URI-ar.
3. Stikkprøve: opne `mkdocs/docs/oreg/enhetsregisteret-bvrinn/klasser/innrapportering.md`
   og verifiser at alle `click`-lenkjer peikar til eksisterande filer i same
   katalog (case-korrekt, lowercase, ingen URI-fragment).
4. Kjør eit fullstendig `grep -rc 'click .* href "\.\./[A-Z]' mkdocs/docs`
   (eller tilsvarande) for å stadfeste at **ingen** attverande `click`-hrefs
   inneheld store bokstavar eller `http://`-fragment.
5. **Skru på lenkje-validering i `mkdocs.yml`:** endre
   `validation.links.not_found` frå `ignore` til `warn` i heredoc-blokka i
   `mkdocs/publish.sh` (rundt linje 461-467), slik at mkdocs faktisk
   rapporterer broten interne lenkjer i staden for å skjule dei. Oppdater
   kommentaren over blokka til å reflektere at berre `unrecognized_links`
   (systematiske fragment-lenkjer utan filnamn, t.d.
   `../../ap-no/dcat-ap-no/#classes`) framleis er ei kjend, ikkje-kritisk
   avgrensing — behald `unrecognized_links: ignore` for den kategorien.
   Merk (jf. avgrensinga over) at dette **ikkje** dekkjer mermaid
   `click`-hrefs, sidan mkdocs sin lenkje-validator berre ser rendra
   `<a href>`-element, ikkje rå tekst inni fenced code-blokker.
   Køyr `make docs-build` etterpå og stadfest at build-loggen no viser
   åtvaringar for eventuelle attverande broten `.md`-lenkjer (om nokon).
   **Ope spørsmål å avklare med brukaren:** CI-steget (`generate.yml`,
   `make docs-build`) køyrer i dag utan `--strict`, så `warn` åtvarar utan
   å feile bygget. Om brukaren ønskjer at broten lenkjer skal feile CI
   (i tråd med "Ingen stille feil"-prinsippet), krev det eit eige steg —
   ikkje inkludert her utan eksplisitt tilslutning.
6. Legg til (eller oppdater) ein regresjonstest i `tests/test_make.sh` eller
   tilsvarande som stadfestar at genererte `click ... href`-verdiar i
   `klasser/*.md` samsvarar med faktiske filnamn i same katalog. Dette er
   den raske, lokale sjekken som køyrer i `validate.yml`/`generate.yml` på
   kvar PR.
7. **Ny job i `.github/workflows/lenkje-og-mermaid-sjekk.yml`** som
   evaluerer *alle* mermaid `click`-hrefs i den fullt genererte portalen —
   den periodiske, breie sjekken (køyrer likt tidspunkt/triggerpunkt som
   dei to eksisterande jobbane: `workflow_dispatch` + måndag kl. 06:00 UTC).

   **Kvifor dette må vere ein eigen job, og ikkje utvide `mermaid-render`:**
   `mermaid-render`-joben hentar mermaid-blokker via `git ls-files -- '*.md'`
   — men både `generated/` og `mkdocs/docs/<domain>/` (inkl. `klasser/`) er
   `.gitignore`-a byggoutput (stadfesta: `git check-ignore` gir treff for
   begge). Joben ser difor i dag **ingen** av dei 943 genererte
   klasse-/slot-sidene i det heile — verken for rendering-sjekk eller for
   ein framtidig click-href-sjekk.

   **Vedteke val (2026-08-12): fail-on-find.** Joben skal **feile CI**
   (`exit 1`) dersom han finn éin eller fleire broten `click`-hrefs — ikkje
   berre åtvare slik `mermaid-render`- og `lenkjesjekk`-jobbane gjer i dag.
   Grunngjeving: dette er nettopp ein klasse feil som til no har vore heilt
   usynleg i CI (jf. "Ingen stille feil"-prinsippet i CLAUDE.md), og
   sidan joben køyrer periodisk (ikkje per PR) er ei feila køyring — med
   varsling via GitHub sitt UI for feila scheduled workflows — rette
   signalet for å fange regresjonar raskt.

   **Vedteke val (2026-08-12): gjenbruk artefaktar frå `generate.yml` i
   første omgang**, i staden for å køyre ein full, uavhengig ombygging av
   portalen (`make gen-docs` for alle domene + `docs-publish`) inne i denne
   joben. `generate.yml` køyrer på kvar push til `main` og deployar direkte
   til GitHub Pages (`actions/deploy-pages` — same job, ingen separat
   nedlastbar artifact av `mkdocs/docs/` i dag). To konkrete måtar å gjenbruke
   dette på — begge oppfyller "gjenbruk, ikkje bygg på nytt", og valet
   mellom dei er ein implementasjonsdetalj å avgjere når joben skrivast:

   - **(a) Hent den live deploya sida over HTTP:** `curl`/`wget` kvar
     klasse-/slot-side frå den publiserte portalen (URL-ane finst i
     `mkdocs/sitemap.xml` som mkdocs genererer automatisk, eller kan
     utleiast frå katalogstrukturen), og parse `click`-direktiva ut av den
     rendra HTML-en (dei ligg som rå, HTML-escapa tekst inni eit
     `<pre class="mermaid">`-element). Krev ingen endring i `generate.yml`.
   - **(b) Last ned Pages-artifacten frå siste vellykka `generate.yml`-køyring
     på tvers av workflows** (t.d. via `actions/github-script` + Actions API,
     eller ein tredjeparts-action som `dawidd6/action-download-artifact`),
     pakk ut `mkdocs/site/` og les same `<pre class="mermaid">`-innhald derifrå.

   Merk: sidan `generate.yml` berre køyrer på push til `main` (ikkje på PR),
   sjekkar denne joben **den til ei kvar tid publiserte portalen** —
   konsistent med at ho er ein periodisk, breei sjekk (som `lenkjesjekk`-joben
   allereie er), ikkje ein per-PR-sjekk. Regresjonstesten i steg 6
   (`tests/test_make.sh`) er den raske, lokale sjekken som fangar feil før
   merge — denne joben er sikkerheitsnettet mot det som faktisk vart
   publisert.

   **Kva joben skal gjere:**
   - Hent HTML for kvar klasse-/slot-side, via (a) eller (b) over.
   - Finn alle `click <Namn> href "<href>"`-direktiv i mermaid-blokkene.
   - For kvar treff: løys href relativt til sida sin URL-katalog og stadfest
     med ein HEAD/GET-førespurnad (for (a)) eller filsjekk i det utpakka
     `mkdocs/site/`-treet (for (b)) at målsida **faktisk finst, med korrekt
     case** (case-sensitivt, som på GitHub Pages).
   - Generer ein markdown-rapport (tabell: fil/URL, click-namn, href,
     status) etter same mønster som `mermaid-render-report.md` og
     `lenkjesjekk-report.md`, skriv til `$GITHUB_STEP_SUMMARY`, og last opp
     som artifact (`click-href-sjekk-report`, 30 dagars retention).
   - `::error file=...::`-annotering per broten lenkje, og `exit 1` dersom
     minst éin vart funnen (jf. vedteke val over).

## Handlingsliste

- [x] Legg til sed-regel for `click ... href`-omskriving i `copy_artifacts.sh`
- [x] Kjør `make docs-publish` og stikkprøv `innrapportering.md`
- [x] Verifiser at ingen attverande `click`-hrefs har feil case eller URI-fragment
- [x] Skru på `validation.links.not_found: warn` i `mkdocs.yml`-blokka i `publish.sh`, oppdater kommentar
- [x] Legg til regresjonstest for `click`-href-korrektheit i `tests/test_make.sh`
- [x] Legg til ny job i `.github/workflows/lenkje-og-mermaid-sjekk.yml` som hentar publisert portal (gjenbruk frå `generate.yml`, ikkje full ombygging) og evaluerer alle mermaid `click`-hrefs
- [x] Vel implementasjon for gjenbruk: (a) HTTP-henting av live GitHub Pages-side, eller (b) nedlasting av Pages-artifact på tvers av workflows
- [x] Joben skal feile CI (`exit 1`) og `::error`-annotere ved funn av broten `click`-hrefs — ikkje berre åtvare
- [x] Kjør `actionlint` mot oppdatert `lenkje-og-mermaid-sjekk.yml` før arbeidet vert rekna som ferdig (jf. CLAUDE.md-krav)

## Utført

1. **`mkdocs/lib/copy_artifacts.sh`:** ny sed-regel rett etter den eksisterande
   `.md`-lenkje-lowercase-regelen, som byggjer kvar `click <Namn> href "..."`
   på nytt frå namnet i click-statementet: `s|click ([A-Za-z0-9_]+) href
   "[^"]*"|click \1 href "../\L\1\E/"|g`. Rettar både case-mismatch
   (`../Innrapportering/` → `../innrapportering/`) og URI-innbaking
   (`../http://www.w3.org/2001/XMLSchema#anyURI/` → `../uriorcurie/`).
2. **`mkdocs/publish.sh`:** `validation.links.not_found` endra frå `ignore`
   til `warn` i mkdocs.yml-heredoc-blokka; kommentaren oppdatert til å
   berre gjelde attverande `unrecognized_links`-kategori (fragment-lenkjer
   utan filnamn) og til å presisere at mermaid click-hrefs framleis er
   usynlege for denne valideringa.
3. **`make docs-publish` + `make docs-build`** køyrt og verifisert: alle
   9143 `click`-hrefs i `mkdocs/docs/**/klasser/*.md` er no lowercase utan
   URI-fragment (stadfesta med grep mot heile `mkdocs/docs/` og
   `mkdocs/site/`); `docs-build` fullførte utan feil og synleggjorde 5
   genuine, urelaterte broten `.md`-lenkjer (utanfor denne specen sitt
   omfang) via `WARNING` i build-loggen.
4. **`tests/test_make.sh`:** ny standalone regresjonstest
   `test_copy_artifacts_click_href` (kobla inn via `run_copy_artifacts_tests`,
   køyrer uavhengig av skjemaliste/containarar) — byggjer ei fiktiv
   gen-doc-fixture, køyrer den faktiske `copy_schema_artifacts`-funksjonen i
   isolert subshell, og stadfestar at kvar resulterande click-href matchar
   `../<lowercase(namn)>/`. Verifisert grønt isolert
   (`TEST_FILTER=copy-artifacts-click-href`).
5. **`mkdocs/lib/scripts/check-mermaid-click-hrefs.py`:** nytt, avhengigheitsfritt
   Python-script (berre stdlib) som hentar `sitemap.xml` frå ei gjeven
   portal-URL, filtrerer til klasse-/slot-sider, hentar kvar side parallelt,
   trekk ut mermaid `click ... href`-direktiv frå `<pre class="mermaid">`,
   og stadfestar at kvar href resolvar til ei kjend side i sitemapen.
   Skriv markdown-rapport, `::error`-annoterer per funn, returnerer exit 1
   ved minst eitt funn. Verifisert mot den faktisk deploya, enno ikkje
   oppdaterte produksjonsportalen (https://brreg.github.io/linkml-datamodellering-no)
   — skriptet fann korrekt dei kjende, endå-ikkje-utrulla broten lenkjene
   (stadfestar at deteksjonslogikken fungerer).
6. **`.github/workflows/lenkje-og-mermaid-sjekk.yml`:** ny job
   `mermaid-click-href-sjekk` — køyrer skriptet mot den publiserte portalen
   (gjenbruk, ingen ombygging), skriv `GITHUB_STEP_SUMMARY`, lastar opp
   rapport som artifact (`click-href-sjekk-report`, 30 dagar), og feilar
   jobben (`exit 1` frå scriptet, ingen `continue-on-error`) ved funn — i
   tråd med dei to vedtekne vala frå brukaren.
7. **`actionlint`** køyrt mot oppdatert workflow-fil: ingen `[expression]`-
   eller schemafeil, berre eitt pre-eksisterande `[shellcheck]`-stilråd i
   `mermaid-render`-joben (urelatert til denne endringa).

**Merk (utanfor omfang):** `make docs-publish` oppdaterte som forventa òg
tracked filer i `mkdocs/docs/referanse/referansemodell/klasser/*.md`
(denne domenekatalogen er ikkje `.gitignore`-a, i motsetnad til dei andre
domena) og `README.md` (auto-genererte tabellar). Dette er ein reell,
ønskt del av same fiks — desse filene hadde same broten click-hrefs.
