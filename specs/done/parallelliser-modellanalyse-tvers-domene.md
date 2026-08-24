# Plan: køyr "Køyr modellanalyse på tvers av domene" parallelt med generate-matrisa

## Bakgrunn

Etter batchinga i `specs/done/effektiviser-modellanalyse-koyretid.md` tok
"Køyr modellanalyse på tvers av domene"-steget i `publish`-jobben ~30-40 s
(38,4 s målt lokalt) — ned frå tre separate kontainarkall, men framleis eit
**sekvensielt** steg som køyrer etter at HEILE `generate`-matrisa (alle
domene, fleire minutt kvar) alt er ferdig, og **før** "Publiser og bygg
dokumentasjonsportal". Brukaren spør om dette kan parallelliserast slik at
det ikkje lenger legg ekstra klokketid til heile workflowen.

Dette er ei oppfølging av "Tiltak 5"-diskusjonen i den arkiverte specen
over, men ei anna løysing enn den som vart skissert der: Tiltak 5 vurderte
å bakgrunne det **domene-scopa** per-skjema-steget mot artefaktgenereringa
**innanfor same jobb**. Denne specen gjeld det **cross-domain**-steget
(`--scope all`) i `publish`-jobben, og løysinga er å flytte det til ein
**heilt separat GitHub Actions-jobb** — sidan `find-similar-names.py
--scope all` berre les kjeldeskjema (`src/linkml/`, tilgjengeleg frå
`source`-artefaktet med det same), ikkje noko frå `generate`-matrisa sin
`generated/`-output, finst det **ingen reell avhengigheit** som tvingar
steget til å vente på matrisa i det heile.

## Tiltak

Ny jobb `modellanalyse-tvers-domene` i `.github/workflows/generate.yml`,
`needs: [ensure-images, checkout-source]` (same startpunkt som `generate`-
matrisa, ikkje avhengig av henne) — køyrer difor **samstundes** med
`generate`-matrisa i staden for etterpå:

1. Last ned `source`-artefaktet, oppgrader crun, logg inn på GHCR, last
   `python-pytest`-imaget (same mønster som resten av workflowen)
2. `make analyse-similar-alle-domene-batch OUT_DIR=generated/modell-
   analyse-tvers-domene`
3. Last opp resultatet som eit nytt artefakt
   (`generated-modell-analyse-tvers-domene`)

`publish`-jobben: lagt til i `needs:` (ventar på jobben, men ho er alt
ferdig lenge før `generate`-matrisa er det for eit repo av denne
storleiken), nytt steg lastar ned artefaktet rett til
`generated/modell-analyse-tvers-domene/` (same stad
`mkdocs/publish.sh` alt forventar — ingen endring der). Det gamle
in-line-steget i `publish`-jobben er fjerna.

## Utført

- Ny jobb `modellanalyse-tvers-domene` lagt til i `generate.yml`, plassert
  parallelt med `generate`-matrisa (begge `needs: [ensure-images,
  checkout-source]`)
- `publish`-jobben: `needs` utvida med `modellanalyse-tvers-domene`, nytt
  nedlastingssteg for artefaktet, gamalt in-line-steg fjerna
- `actionlint` køyrd og godkjend (reint) etter endringa
- Verifisert lokalt: `make analyse-similar-alle-domene-batch
  OUT_DIR=generated/modell-analyse-tvers-domene` (same kommando den nye
  jobben køyrer) produserer dei tre forventa filene; `make docs-publish`
  + `make docs-build` med resultatet stadfesta at
  `mkdocs/docs/modellanalyse/*.md` framleis vert generert korrekt og at
  `validation.links`-sjekken framleis er grøn — ingen endring i
  sluttresultatet, berre i **når** i workflowen arbeidet skjer.
- Kan ikkje verifisere den faktiske veggklokke-gevinsten utan ei reell
  CI-køyring (GitHub Actions-jobbschedulering, ikkje noko som kan
  simulerast lokalt) — forventa resultat er at heile
  `modellanalyse-tvers-domene`-jobben (nedlasting + oppsett + ~38 s
  analyse + opplasting) overlappar fullstendig med `generate`-matrisa
  (som tek fleire minutt per domene, jf. «Funn» i
  `specs/done/effektiviser-generate-workflow-koyretid.md`), og dermed
  ikkje lenger bidreg synleg til total workflow-tid. Følg opp med ei
  faktisk måling i neste CI-køyring.
