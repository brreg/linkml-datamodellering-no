# Løys CodeQL-funn: unused-import i genererte pythongen-model.py-filer

## Bakgrunn

GitHub sin CodeQL-skanning (`.github/workflows/codeql.yml`) har 24 opne
funn (`gh api repos/brreg/linkml-datamodellering-no/code-scanning/alerts`,
`state=open`, alert-nummer #70–#93). Alle 24 er av same regel,
**`py/unused-import`**, og alle ligg i berre to filer:

- `mkdocs/docs/felles/brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-model.py` (12 funn)
- `mkdocs/docs/felles/brreg-felles-digital-adresse/brreg-felles-digital-adresse-model.py` (12 funn)

Døme på meldingar: `Import of 'dataclasses' is not used.`,
`Import of 're' is not used.`, `Import of 'EnumDefinitionImpl' is not
used.`, `Import of 'JsonObj'/'as_dict' is not used.` osv. — alle på
importlinjer i toppen av kvar fil.

### Rot-årsak

Desse to filene er **ikkje handskrivne** — dei er `pythongen.py` (LinkML)
sin genererte Python-representasjon av skjemaa, kopiert av
`mkdocs/publish.sh` frå `generated/felles/<modell>/` til
`mkdocs/docs/felles/<modell>/` for at dokumentasjonsportalen skal kunne
lenke til/vise dei. Dei vart lagt til i commit `d0b75e38` (splitten av
`brreg-felles-adresse`, sjå `specs/done/splitt-brreg-felles-adresse.md`),
som del av det vanlege `make domain-felles` + `make docs-publish`-løpet.

`pythongen.py` skriv **alltid** eit fast importoppsett øvst i fila
(`dataclasses`, `re`, `date`/`datetime`/`time`, `Dict`/`List`,
`JsonObj`/`as_dict`, `EnumDefinition`/`PermissibleValue`/
`PvFormulaOptions`, `EnumDefinitionImpl`, `camelcase`/`sfx`/`underscore`,
`bnode`/`empty_dict`/`empty_list`, `extended_float`/`extended_int`/
`extended_str`, `Namespace`, og typane brukt i `range`-slots som
`String`/`Uriorcurie`/`Integer`) **uavhengig av** om det konkrete skjemaet
faktisk brukar enums, mønstertypar, bnodes osv. Dei to nye adressemodellane
har berre enkle klassar/slots (ingen `enums:`), så mesteparten av dette
faste importoppsettet vert ståande ubrukt — eit strukturelt trekk ved
generatoren, ikkje ein feil i noko vi eig eller vedlikeheld.

**Stadfesta at dette er eit generelt, ikkje eit isolert, problem:** det
finst frå før éin tredje generert `*-model.py`-fil i repoet,
`mkdocs/docs/oreg/register-over-aksjeeiere/register-over-aksjeeiere-model.py`
(same `python: true`-generator, også utan `enums:`), som har **identisk**
ubrukte importar (`dataclasses`, `re`, `EnumDefinitionImpl` m.fl. — verifisert
ved grep, ingen faktisk bruk utover importlinja). Denne fila har **ingen**
CodeQL-funn i det heile (verken opne, fiksa eller avviste) — mest sannsynleg
fordi ho vart lagt til i ein commit/periode som aldri vart fanga opp av ein
full CodeQL-analyse av akkurat denne fila. Dette viser at kvart **nye**
skjema med `python: true` og utan `enums:` vil trigge same batch på ~12
`py/unused-import`-funn neste gong CodeQL skannar det, med mindre roten
vert retta no.

### Kvifor "fiks" ikkje betyr å redigere .py-filene

Å fjerne dei ubrukte importlinjene direkte i dei to `-model.py`-filene
ville vore verkelaust: filene vert **fullstendig regenererte og
overskrivne** ved neste `make domain-felles`/`make docs-publish`
(pythongen køyrer på nytt frå skjemaet, ikkje inkrementelt), så endringa
ville forsvinne ved neste normale byggjekøyring. Dette er difor ikkje eit
tilfelle der `error_handler`/eksplisitt logging (jf. CLAUDE.md § «Ingen
stille feil») eller vanleg kodeoppgradering er rett verktøy — problemet må
løysast på **skannings-nivå**, ikkje i det genererte artefaktet sjølv.

### Presedens: `paths-ignore` finst alt for akkurat denne kategorien

`.github/workflows/codeql.yml` har alt eit `paths-ignore`-oppsett i
CodeQL-konfigurasjonen, nettopp for å skjerme generert/tredjeparts-innhald
frå skanning:

```yaml
config: |
  paths-ignore:
    - mkdocs/node_modules/**
    - mkdocs/site/**
    - generated/**
```

`generated/**` er alt ekskludert — men `mkdocs/docs/<domain>/<modell>/`
er nettopp ein **kopi** av delar av `generated/<domain>/<modell>/`
(kopiert av `mkdocs/publish.sh`, sjå `.claude/rules/mkdocs-portal.md`
§ «Steg 2»), og er difor det same innhaldet under eit anna stinamn som
`paths-ignore`-lista ikkje fangar opp i dag. Det er dette hòlet som er
rot-årsaka til at akkurat desse to filene vart skanna og flagga.

**Viktig avgrensing:** `mkdocs/docs/` inneheld **òg** handskrive innhald
som skal halde fram med å verte skanna, t.d.
`mkdocs/docs/javascripts/nav-active-fix.js` og
`mkdocs/docs/javascripts/toc-active-click-fix.js`. Eksklusjonen må difor
vere **presis** — berre dei genererte `*-model.py`-filene under
domene-/skjema-undermappene — ikkje heile `mkdocs/docs/**`.

## Steg

1. **Utvid `paths-ignore` i `.github/workflows/codeql.yml`** med eit
   mønster som fangar opp genererte pythongen-filer under
   dokumentasjonsportalen, uavhengig av domene/modellnamn og mappedjupn:
   ```yaml
   config: |
     paths-ignore:
       - mkdocs/node_modules/**
       - mkdocs/site/**
       - generated/**
       - mkdocs/docs/**/*-model.py
   ```
   Grunngjeving for mønsteret: `*-model.py` er suffikset `pythongen.py`
   alltid brukar (jf. filnamnmønsteret i `mkdocs/lib/scripts/`/`publish.sh`
   som kopierer artefakta), og finst **ikkje** brukt av noko handskrive
   Python-skript i repoet elles (verifiser med
   `grep -rl -- "-model\.py$" --include="*.py" .` at ingen falske treff
   oppstår før merge).
2. **Køyr actionlint mot den endra fila** (obligatorisk etter CI-endring,
   jf. CLAUDE.md § «Actionlint etter CI-endring»):
   ```bash
   podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/codeql.yml
   ```
   Berre `[expression]`/schemafeil er blokkerande — eventuelle
   `[shellcheck]`-funn (usannsynleg i denne fila, ingen `run:`-steg vert
   endra) treng ikkje rettast som del av denne endringa.
3. **Stadfest ingen utilsikta treff** — køyr eit lokalt tørrsøk for å
   dobbeltsjekke at mønsteret `mkdocs/docs/**/*-model.py` berre matchar dei
   forventa genererte filene, og ikkje noko under `mkdocs/docs/javascripts/`
   eller anna handskrive innhald:
   ```bash
   find mkdocs/docs -iname "*-model.py"
   # Forventa: berre dei skjema-genererte *-model.py-filene (i dag 3 stk,
   # aukar over tid etter kvart som fleire skjema får python: true)
   ```
4. **Vent på neste CodeQL-køyring** (trigga automatisk ved push til
   `main`, jf. `on.push.branches: [main]` i workflowen) og stadfest at dei
   24 opne funna (`#70`–`#93`) går over til status `fixed` automatisk —
   GitHub lukkar eit code scanning-funn når staden det galdt fell ut av
   analyseomfanget ved neste skanning. Sjekk med:
   ```bash
   gh api repos/brreg/linkml-datamodellering-no/code-scanning/alerts --paginate \
     --jq '[.[] | select(.state=="open")] | length'
   ```
   Forventa resultat: `0` (eller berre nye, ikkje-relaterte funn oppstått
   sidan denne specen vart skriven).
5. **Fallback dersom funna ikkje lukkar seg automatisk** — dersom dei 24
   framleis står som `open` etter neste push-utløyste køyring (t.d. fordi
   GitHub sin auto-lukkingslogikk krev at heile filbanen forsvinn frå
   analysen i **same** commit som koden vart lagt til, ikkje berre at
   `paths-ignore` vert utvida i ein seinare commit), informer brukaren om
   at dei må avvisast manuelt via GitHub sitt Security-fane
   (Code scanning alerts → filtrer på `py/unused-import` → merk dei 24
   funna → "Dismiss alert" → grunngjeving "Used in tests"/"Won't fix" med
   fritekst-kommentar som viser til denne specen). LLM skal **ikkje**
   utføre denne avvisinga sjølv via `gh api`-PATCH-kall — det er ei
   tilstandsendrande handling mot eit delt GitHub-system og skal
   godkjennast/utførast av brukaren, jf. CLAUDE.md sine reglar om
   handlingar med verknad utanfor det lokale miljøet.

## Merknad — kvifor ikkje ekskludere heile `generated/`-kopien i staden

Eit alternativ ville vore å ekskludere heile
`mkdocs/docs/<domain>/<modell>/` (alle genererte artefakt-undermapper) i
staden for berre `*-model.py`. Dette er **ikkje** valt, sidan:

- Ingen av dei andre kopierte artefakttypane (`.ttl`, `.json`, `.yaml`,
  `.md`, `.svg`, `.puml`) vert i det heile teke med i CodeQL sine
  python/javascript-typescript/actions-analysar — dei er ikkje
  køyrbar kode, så eit breiare eksklusjonsmønster ville ikkje endra talet
  på funn, berre gjort `paths-ignore`-lista mindre presis og vanskelegare
  å resonnere om seinare (kvifor er heile mappa ekskludert, når berre éin
  filtype nokon gong var problemet?).
- Eit smalt, eksplisitt mønster (`*-model.py`) gjer det tydeleg for
  framtidige lesarar av workflow-fila **kvifor** unntaket finst (generert
  Python-kode, ikkje "alt under mkdocs/docs skal ignorerast").

## Handlingsliste

- [x] Steg 1: Utvid `paths-ignore` i `.github/workflows/codeql.yml`
- [x] Steg 2: Køyr actionlint mot endra fil — ingen funn
- [x] Steg 3: Stadfest ingen utilsikta treff (`find mkdocs/docs -iname "*-model.py"`) — berre dei 3 kjende genererte filene matchar, ingen handskrivne filer råka
- [ ] Steg 4: Vent på neste CodeQL-køyring (etter at brukaren har committa/pusha denne endringa), stadfest 24 funn lukka automatisk
- [ ] Steg 5 (berre om nødvendig): informer brukaren om manuell avvising via Security-fana

## Utført (delvis)

- **Steg 1:** `.github/workflows/codeql.yml` sin `paths-ignore` er utvida
  med `mkdocs/docs/**/*-model.py`.
- **Steg 2:** `actionlint` (via podman, `docker.io/rhysd/actionlint:latest`)
  køyrt mot den endra fila — ingen funn.
- **Steg 3:** `find mkdocs/docs -iname "*-model.py"` stadfesta at berre dei
  3 kjende genererte filene (`register-over-aksjeeiere`,
  `brreg-felles-geografisk-adresse`, `brreg-felles-digital-adresse`)
  matchar mønsteret. Eit tilleggssøk (`grep -rl -- "-model\.py$" --include="*.py" .`)
  stadfesta at ingen handskrive `.py`-fil i repoet endar på `-model.py` —
  ingen risiko for utilsikta eksklusjon av kode som burde vore skanna.

**Attståande (krev handling utanfor denne økta):**

Steg 4–5 krev at endringa i `.github/workflows/codeql.yml` faktisk vert
commita og pusha til `main` (LLM utfører ikkje git-operasjonar, jf.
CLAUDE.md), og at ei ny CodeQL-køyring skjer deretter — dette kan difor
ikkje stadfestast i denne økta. Spesifikasjonen vert ståande i
`specs/backlog/` (ikkje flytta til `specs/done/`) til steg 4 er stadfesta,
eventuelt steg 5 er utført av brukaren.

**Stadfesta av brukar 2026-09-04** (jf.
`specs/done/evaluering-gjentakande-monster-backlog.md`, P6): steg 4/5 sin
CI-åtferd er stadfesta. Flytta til `specs/done/`.
