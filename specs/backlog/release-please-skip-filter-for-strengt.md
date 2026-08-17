# Evaluering: er release-please sitt skip-filter for strengt?

## Bakgrunn

Brukaren rapporterer at ingen av release-please-køyringane #607–#612 trigga
faktiske releasar, og ber om ei evaluering av om filteret i
`.github/workflows/release-please.yml` (steget "Sjekk om siste commit skal
trigge release-please") er for strengt, eller om commit-meldings-syntaksen
treng betre dokumentasjon.

## Metode

Henta køyringshistorikk og steg-for-steg-status via `gh run list`/`gh api`
for runs #607–#617, og kryssjekka mot faktisk commit-innhald (`git log`,
`git show --stat`) for kvar av dei.

## Funn

### Alle 6 runs (#607–#612) vart korrekt/ukorrekt hoppa over — blanda biletet

| # | Commit | Type/scope | Rører `*-schema.yaml`? | Hoppa over korrekt? |
|---|---|---|---|---|
| **607** | `fix(lenkjesjekk): rett anker-lenkje, ADMS-term...` | fix, scope="lenkjesjekk" | **Ja — 1 skjema** (`common-ap-no-schema.yaml`, éin linje: gjenoppretta kanonisk ADMS-term `PrivateIndividual(s)`, truleg som eit incidental biprodukt av lenkjesjekk-fiksen) | **✗ FEIL — skulle trigga** |
| 608 | `fix(lenkjesjekk): ekskluder NGR-vokabularnamnerom...` | fix, scope="lenkjesjekk" | Nei | ✓ Korrekt |
| 609 | `fix(lenkjesjekk): rett resterande brotne lenkjer...` | fix, scope="lenkjesjekk" | Nei | ✓ Korrekt |
| 610 | `fix(modell-analyse): filtrer kjende IRI-funn...` | fix, scope="modell-analyse" | Nei (analyseskript) | ✓ Korrekt |
| 611 | `fix(ci): pin tredjeparts actions...` | fix, scope="ci" | Nei | ✓ Korrekt |
| **612** | `fix(ap-no,fint,fair,begrepskatalog): sett status til UnderDevelopment i alle skjema` | fix, scope="ap-no,fint,fair,begrepskatalog" | **Ja — 19 skjema** (dcat-ap-no, cpsv-ap-no, dqv-ap-no, dqv-core, modelldcat-ap-no, modelldcat-modell, modelldcat-katalog, skos-ap-no, xkos-ap-no, 7×fint-\*, fair-metadata, brreg-begrepskatalog) | **✗ FEIL — skulle trigga** |

Same mønster funne i éin commit til, like før denne perioden:

| Commit | Type/scope | Rører `*-schema.yaml`? | Hoppa over korrekt? |
|---|---|---|---|
| `d9a700ca` `fix(ap-no,modellkatalog): fullfør manglande badge-metadata...` | fix, scope="ap-no,modellkatalog" | **Ja — 7 skjema** (dqv-core, modelldcat-modell, digdir/kartverket/ksdigital/novari/skatteetaten-modellkatalog) | **✗ FEIL — skulle trigga** |

Stadfesta via GitHub API (`gh api .../jobs/<id>`) at "Checkout for release-please"
og alle påfølgjande steg fekk `conclusion: skipped` for run #612 — heile
`release-please-action` fekk aldri sjansen til å oppdage dei endra skjemaa.

## Rotårsak

Filteret prøver å avgjere "skal release-please køyre" ved å **tolke
scope-teksten** i commit-meldinga mot `.github/valid-scopes.txt` (individuelle
modellnamn). Regelen (linje 88 i workflowen, før denne fiksen):

```bash
grep -qE "^(feat|fix)\(($VALID_SCOPES)\):"
```

krev at heile parentesen er **nøyaktig éitt** gyldig modellnamn. Dette gjev
minst to distinkte feilmønster, stadfesta i funna over:

1. **Kommaseparerte multi-scope-commits** (`fix(a,b,c): ...`) — eit
   **etablert og mykje brukt mønster** i repoet sin historie (over 15
   tidlegare commits, dei fleste legitimt CI/verktøy-retta som
   `fix(ci,mkdocs):`, `fix(oreg,mcp-validator):`, der det er korrekt at dei
   ikkje skal trigge ein release). Regexen kan strukturelt aldri matche eit
   slikt scope, uavhengig av om innhaldet faktisk endrar skjema (`d9a700ca`,
   `2c6215e`).
2. **Eit enkelt, gyldig-lydande men ikkje-modell-scope** kan skjule ei
   incidental skjemaendring — run #607 (`fix(lenkjesjekk): ...`) hadde eit
   heilt sjølvstendig, presist scope, men retta i tillegg éi linje i
   `common-ap-no-schema.yaml` som eit naturleg biprodukt av sjølve
   lenkjesjekk-fiksen. Scope-namnet "lenkjesjekk" fortel ingenting om at ei
   skjemafil vart rørt — og kan heller ikkje gjere det, sidan scope er skrive
   *før* forfattaren nødvendigvis veit heile omfanget av endringa.

Begge mønstera viser same grunnleggjande veikskap: **scope-teksten er ein
upåliteleg proxy for kva filer som faktisk endra seg.**

**Dette er ikkje eit dokumentasjonsproblem.** Å dokumentere "skriv aldri
fleire scope i éin feat/fix-commit" ville vore urealistisk og skadeleg for
commit-hygiene — ei repo-brei feltendring som råkar 19 modellar er ei
legitim, atomisk, gjennomgåande endring, og å tvinge han til 19 separate
commits berre for å tekkjast eit regex-filter er feil løysing på feil nivå.

**Den eigentlege innsikta:** `release-please-action` sjølv avgjer kva for
pakkar som får versjonsbump basert på **filstiar som faktisk endra seg**,
ikkje på commit-scope-teksten. Pre-filteret prøver å *gjette* det same
svaret frå ein tekstleg proxy (scope-namnet), og gjettinga kan bli feil —
det burde i staden spørje det same spørsmålet direkte.

## Tilråding

Erstatt scope-tolkinga i regel 2–4 med eit direkte sjekk av **faktisk endra
filer** i siste commit:

```bash
# 2. feat/fix (uansett scope, fleire scope, feilstava scope, eller ingen
#    scope) — trigg berre dersom commiten faktisk endrar minst éin
#    *-schema.yaml. release-please-action avgjer sjølv kva pakkar som får
#    versjonsbump basert på filsti, ikkje commit-scope.
if echo "$FIRST_LINE" | grep -qE '^(feat|fix)(\(.*\))?:'; then
  CHANGED_SCHEMAS=$(git diff --name-only HEAD~1 HEAD -- 'src/linkml/*/*/*-schema.yaml')
  if [ -n "$CHANGED_SCHEMAS" ]; then
    echo "skip=false" >> $GITHUB_OUTPUT
  else
    echo "skip=true" >> $GITHUB_OUTPUT
  fi
  exit 0
fi

# 3. Elles: ikkje feat/fix — hopp over
echo "skip=true" >> $GITHUB_OUTPUT
```

Dette gjer `.github/valid-scopes.txt` overflødig for denne gata (feltet er
uansett generert dynamisk og kan framleis brukast som menneskeleg
referansedokumentasjon over gyldige modellnamn, sjølv om det ikkje lenger
handhevar noko programmatisk). Krev `fetch-depth: 2` på "Checkout for
scope-sjekk"-steget for at `HEAD~1` skal vere tilgjengeleg (same mønster som
`specs/done/auto-datoannotasjonar-release.md` brukte for same problem).

**Regel 1 (skip ikkje-releasande typar: style/docs/chore/test/ci/build/perf/refactor)
skal IKKJE endrast** — han er riktig og uavhengig av dette problemet.
`refactor`-commits som strukturelt flyttar skjemainnhald (t.d. denne økta sin
`refactor(ap-no): flytt dqv-core...`) skal framleis ikkje trigge ein
versjonsbump, i tråd med Conventional Commits-semantikk (ingen funksjonell
endring).

## Konsekvens: allereie tapte releasar

24 unike modellar fekk reelt skjemainnhald endra utan at release-please nokon
gong fekk sjansen til å oppdage det:
- **23 modellar** frå `d9a700ca`/`2c6215e` (status-annotasjon,
  utgiver/lisens/dato-metadata)
- **`common-ap-no`** frå `292d32d` (kanonisk ADMS-term-retting)

Desse er framleis "usynkroniserte" — `version`/`endringsdato` i sjølve
skjemafilene reflekterer ikkje at `fix`-nivå-innhald vart lagt til. Når
filteret er fiksa, vil **neste** feat/fix-commit som rører desse skjemaa
fange dei opp automatisk (sidan release-please uansett samanliknar heile
commit-historikken mot manifestet, ikkje berre siste commit) — men dersom
brukar ønskjer ein umiddelbar catch-up-release, krev det anten:
- Ein ny, triviell `fix(<scope>):`-commit som råkar dei aktuelle skjemaa
  (naturleg vil skje ved neste reelle endring), eller
- Manuell `workflow_dispatch`-triggering av `release-please.yml` (hoppar
  forbi heile skip-filteret, jf. `if:`-vilkåret på steget etterpå)

Begge krev handling brukaren må ta sjølv (LLM skal aldri pushe/trigge CI).

## Handlingsliste

- [x] Erstatt scope-basert regel 2–4 i `release-please.yml` med filbasert sjekk (`git diff --name-only HEAD~1 HEAD -- 'src/linkml/*/*/*-schema.yaml'`)
- [x] Legg til `fetch-depth: 2` på "Checkout for scope-sjekk"
- [x] `actionlint` mot `release-please.yml` — ingen `[expression]`-feil, berre pre-eksisterande `[shellcheck]`-stilråd
- [x] Verifisert lokalt mot 10 faktiske historiske commits (`git diff`-simulering av heile gate-logikken): alle 3 kjende feilklassifiseringar (`292d32d`, `d9a700ca`, `2c6215e`) gjev no korrekt `skip=false`; alle stadfesta korrekte skip (`91875312`, `6cb82bf`, `8b437b6`, `5802d13`) og korrekt type-skip (`refactor`-commiten `46792cdc`) er uendra
- [ ] Vurder å fjerne/behalde `.github/valid-scopes.txt`-generering (allereie ubrukt for gating, men kan behaldast som referanse — ikkje kritisk)
- [ ] Brukar avgjer: manuelt `workflow_dispatch` no, eller vent på neste naturlege feat/fix-commit, for å fange opp dei 24 modellane frå `d9a700ca`/`2c6215e`/`292d32d`
