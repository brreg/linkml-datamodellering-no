# release-please.yml hoppar over tag/release-oppretting ved eigen PR-merge

## Bakgrunn

Brukar oppdaga at `dcat-ap-no-schema.yaml` sitt `version:`-felt (`2.13.0`)
ikkje har nokon tilsvarande git-tag/GitHub Release. Undersøking av faktisk
GitHub Actions-historikk (via `gh run view`/`gh pr view`/`gh api`, ikkje
gjetting) avdekte ein strukturell feil i `.github/workflows/release-please.yml`
som råkar **kvar einaste** release-please-PR-merge, ikkje berre denne eine.

## Rotårsak

`check_commit_type`-steget (linje ~40-60) avgjer om
`googleapis/release-please-action@v5` skal køyre, basert på **berre siste
commit-melding** på ein push-hending:

```bash
FIRST_LINE=$(echo "$COMMIT_MSG" | head -n 1)
# 1. Hopp over ikkje-releasande typar (style|docs|chore|test|ci|build|perf|refactor)
# 2. Tillat feat/fix utan scope
# 3. Tillat feat/fix med gyldig modell-scope
# 4. Elles: hopp over
```

Denne guarden vart laga for å hoppe over ordinære, ikkje-releasande pushar
(sparer CI-tid). Han råkar derimot **òg sjølve merge-commiten** når
release-please-PR-en («chore: release main», auto-merga med `--squash` frå
steget «Informer om release-PR og aktiver auto-merge») lander på `main` —
commit-meldinga («Merge pull request #N frå
brreg/release-please--branches--main») matchar aldri `^(feat|fix)`, så
guarden set `skip=true` for akkurat denne pushen.

**Konsekvens:** `googleapis/release-please-action@v5` sitt steg — det einaste
steget som kan detektere «ein release-PR vart nettopp merga, opprett
tag+release no» — vert **aldri køyrt** for merge-pushen. Og kritisk:
**denne detekteringa skjer berre éin gong, rett etter merge.** Ein seinare,
tilfeldig triggera køyring (t.d. neste gyldig-scopa commit) plukkar det
**ikkje** opp retroaktivt — stadfesta empirisk (sjå under).

### Stadfesting via faktisk GitHub Actions-historikk

**Merge av PR #50** (`run 30760777425`, 2026-08-02T18:17:18Z):
```
Sjekk om siste commit skal trigge release-please | success (→ skip=true)
Run googleapis/release-please-action@v5           | skipped
Opprett per-schema git-tags                       | skipped
```

**15 sekund seinare** — ein commit med meldinga
*"fix(samt-bu): trigger ny release-please køyring for å verifisere om d..."*
vart pusha (stadfestar at nokon **alt hadde oppdaga symptomet** og prøvde eit
manuelt work-around med ein dummy-commit). Køyringa (`run 30760785731`):
```
Sjekk om siste commit skal trigge release-please | success (→ skip=false, samt-bu er gyldig scope)
Run googleapis/release-please-action@v5           | success
Oppdater schema-versjonar i release-PR            | skipped  ← releases_created/prs_created var IKKJE sanne
Opprett per-schema git-tags                       | skipped
```

Sjølv om `release-please-action` fekk køyre denne gongen, fann han **ikkje**
noko å gjere — den ferske merge-tilstanden var alt «forbi» frå hans
perspektiv. Work-around-forsøket løyste altså ikkje problemet.

### Full omfang — verifisert med eksakt tag-oppslag

Første sjekk (`git/refs/tags/{tag}` utan eksakt matching) gav falske
positive — dette GitHub-endepunktet returnerer eit **array av prefiks-treff**
når det ikkje finst noko eksakt treff (t.d. matchar `dcat-ap-no-v2.13.0` mot
alle `dcat-ap-no-v2.1*`-tags). Retta ved å bruke
`git/ref/tags/{tag}` (eintal «ref», eksakt match, 404 elles) og
verifisert mot ein kjend eksisterande tag (`samt-bu-v1.8.0` → funnen
korrekt).

**Alle 16 pakkane i PR #50 sin body manglar tag/release:**

| Pakke | Venta versjon (frå PR-body) |
|---|---|
| cpsv-ap-no | 1.10.0 |
| dcat-ap-no | 2.13.0 |
| dqv-ap-no | 1.15.0 |
| modelldcat-ap-no | 1.14.0 |
| skos-ap-no | 2.16.0 |
| brreg-begrepskatalog | 1.6.1 |
| fair-metadata | 1.6.0 |
| fint-administrasjon | 4.5.1 |
| fint-common | 4.4.0 |
| brreg-modellkatalog | 1.5.1 |
| ngr-adresse | 1.6.0 |
| ngr-eiendom | 1.6.0 |
| ngr-person | 1.6.0 |
| ngr-virksomhet | 1.6.0 |
| register-over-aksjeeiere | 1.7.0 |
| samt-bu | 1.9.0 |

Alle desse skjema-filene sitt `version:`-felt vart alt oppdatert **før**
merge (steget «Oppdater schema-versjonar i release-PR» køyrer på open
PR-branch), men ingen av dei fekk faktisk tag/release/artefaktopplasting.

**Merk — sjekk om nyare PR-ar har same problem:** PR #50 er ikkje
nødvendigvis den einaste ramma syklusen. Denne spec-en verifiserer berre
denne eine, men mønsteret er strukturelt — kvar einaste merga
release-please-PR sidan denne guarden vart innført kan vere ramma.
Uavklart om det finst fleire; sjå Steg 5.

## Føreslått fiks

Legg til eit unntak i `check_commit_type` slik at merge-commits frå
`release-please--branches--main` **aldri** vert hoppa over, uavhengig av
commit-meldingsform — dette gir `release-please-action` sjansen sin til å
detektere og fullføre den ferske merga alltid, ikkje berre når neste
tilfeldige commit-scope tilfeldigvis matchar.

```bash
# Etter eksisterande steg 1-3, før steg 4 («elles: hopp over»):
# Aldri hopp over release-please sin eigen merge-commit — han er den einaste
# sjansen release-please-action får til å detektere ei nyleg merga PR og
# fullføre tag/release-oppretting. commit-meldinga matchar aldri feat/fix-
# mønsteret over, og ville elles blitt hoppa over av steg 4.
if echo "$FIRST_LINE" | grep -qE '^Merge pull request #[0-9]+ from .*/release-please--branches--main'; then
  echo "skip=false" >> $GITHUB_OUTPUT
  echo "Siste commit er release-please sin eigen PR-merge — held fram"
  exit 0
fi
```

(Plasser dette som eit **nytt punkt 3.5**, mellom eksisterande punkt 3 og 4,
sidan det skal evaluerast før den generelle catch-all-en i punkt 4.)

## Remedieringsplan for dei 16 orphan-pakkane

**Vedtak (avklart med brukar):** prøv `workflow_dispatch` fyrst — workflowen
støttar alt manuell triggering (`on: workflow_dispatch:`), og
`release-please-action`-steget sitt køyre-vilkår
(`(push && skip!=true) || workflow_dispatch`) **omgår guarden heilt** for
manuelle køyringar. Dette bruker den eksisterande, korrekte pipelinen
(tag + GitHub Release + artefaktopplasting), i staden for at eg
handlagar bare git-tags som ville mangla changelog og opplasta artefakt.

**Uvisse:** ukjent om `release-please-action` sin interne tilstand
(manifest + samanlikning mot faktiske tags) framleis vil detektere og
fullføre den forlatne PR #50-tilstanden så lenge etterpå, eller om han i
staden startar ein heilt ny syklus / ikkje finn noko å gjere. Må
verifiserast empirisk ved faktisk køyring.

## Steg

1. **Rett `check_commit_type` i `.github/workflows/release-please.yml`** —
   legg til unntaket for release-please sin eigen merge-commit (sjå
   «Føreslått fiks» over).

2. **Køyr actionlint** (obligatorisk etter CI-endring per `CLAUDE.md`):
   ```bash
   podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/release-please.yml
   ```

3. **Triggar `workflow_dispatch` manuelt** for å prøve å fullføre dei 16
   forlatne releasane:
   ```bash
   gh workflow run release-please.yml --repo brreg/linkml-datamodellering-no
   ```
   Overvak køyringa (`gh run watch`) og rapporter faktisk utfall — kva vart
   oppretta, kva vart ikkje.

4. **Verifiser resultat** — sjekk kor mange av dei 16 tag-ane/releasane som
   faktisk vart oppretta (`git/ref/tags/{tag}`-oppslag, same metode som i
   Bakgrunn). Dersom framleis manglande: vurder alternativ remediering
   (manuell `gh release create` + `git tag` per pakke, eller ein tom
   `feat`/`fix`-commit med gyldig scope for å re-trigge ein normal syklus).

5. **Sjekk om fleire syklusar er ramma** — gjenta same eksakt-tag-sjekk
   (`git/ref/tags/{tag}`) mot **alle** pakkar i `.github/valid-scopes.txt`,
   ikkje berre dei 16 frå PR #50, for å avdekke om andre, eldre merge-
   syklusar òg har orphan-versjonar. Rapporter funn.

6. **Dokumenter** — legg eit avsnitt i denne spec-en (eller ein kort
   kommentar i `release-please.yml` sjølv) som forklarer kvifor unntaket i
   `check_commit_type` er naudsynt, slik at ingen fjernar det ved eit
   uhell seinare i ei forenklings-omskriving.

## Handlingsliste

- [x] 1: Rett `check_commit_type` med unntak for release-please-merge-commit
- [x] 2: `actionlint` på `release-please.yml`
- [x] 3: Triggar `workflow_dispatch`, overvak, rapporter utfall
- [x] 4: Verifiser kor mange av 16 pakkar som fekk tag/release
- [x] 5: Sjekk om fleire, eldre syklusar er ramma
- [x] 6: Dokumenter grunngjeving i kode-kommentar
- [x] 7: Flytt spec til `specs/done/`

## Utført

**1-2: CI-fiks.** Lagt til unntaket i `check_commit_type`
(`.github/workflows/release-please.yml`) som «Føreslått fiks» over —
eksakt den koden, som eit nytt punkt 0 (evaluert før dei eksisterande fire
punkta). `actionlint` viste berre pre-eksisterande `[shellcheck]`-stilråd,
ingen `[expression]`-feil — ikkje blokkerande per `CLAUDE.md`.

**3: `workflow_dispatch`.** Triggerte manuelt (`gh workflow run
release-please.yml`), overvaka med `gh run watch` (run `31718084523`,
fullførte på 2m57s). **Løyste ikkje** dei 16 orphan-pakkane —
`release-please-action` fann ingenting å gjere, sidan
`.github/release-please-manifest.json` alt hadde dei bumpa
versjonstala committa (manifestet og skjemafilene var interne konsistente
med kvarandre, men begge frikopla frå den faktiske tag-historia). Stadfesta
at automatisk sjølvlæking ikkje er mogleg for denne typen gap.

**4: Full manuell remediering (alle 16 pakkar).**

- Sette opp eit isolert `git worktree` ved commit `33627bcc` (det
  historisk korrekte punktet — stadfesta at alle 16 skjemakatalogar hadde
  hatt 87-924 diff-linjer kvar sidan den commiten, så bygging frå `HEAD`
  ville feilaktig bunta 11 dagar med urelatert, seinare arbeid inn i
  historiske releasar).
- Bygde alle 80 artefakt (JSON Schema/SHACL/OWL/JSON-LD-context/ER-diagram
  × 16 pakkar) frå worktreeen — alle lukkast.
- Ekstraherte per-pakke changelog-tekst frå PR #50 sin body (16 seksjonar,
  identisk med det `release-please-action` sjølv genererte).
- Oppretta og pusha 16 annoterte git-tags direkte mot `33627bcc`.
- Flytta changelog + artefakt til ein varig stad (`~/release-remediation-33627bcc/`,
  utanfor `/tmp` og utanfor repoet) etter at `/tmp`-scratchpaden vart
  identifisert som for flyktig for brukaren sin eigen påfølgjande
  køyring.
- Skreiv `src/assets/scripts/migreringsscript/create-missing-releases.sh`
  for at brukaren skulle køyre `gh release create`/`upload` sjølv (min
  eigen `gh`-autentisering mangla løyve til å **skrive** releases —
  `POST /releases` gav 404 sjølv med stadfesta `push`/`admin`-tilgang via
  `GET`, medan `RELEASE_PLEASE_TOKEN` som CI brukar tydelegvis har vidare
  løyve).

**Feilrettingar undervegs (brukaren si eiga køyring):**

1. **Line-brotne kommandoar** — brukaren limte kommandoane inn i scriptet
   utan `\`-fortsetjing, som anten forvrengde argumentverdiar (linjeskift
   inni opne anførselsteikn) eller delte ein logisk kommando i fleire
   ugyldige. Retta ved å skrive om til funksjonar + eit datasett-array,
   éin kommando per pakke.
2. **Immutable releases** — repoet har denne GitHub-funksjonen aktivert.
   `gh release create` + separat `gh release upload` feilar alltid
   (`HTTP 422: Cannot upload assets to an immutable release`) — artefakt
   må sendast med i **same** `gh release create`-kall. Retta scriptet til
   éin kombinert funksjon (`create_release_with_assets`).
3. **`cpsv-ap-no-v1.10.0` permanent blokkert** — den fyrste (feila,
   artefaktlause) releasen gjorde `tag_name`-et permanent ubrukande for
   nye releasar (stadfesta: uendra etter av/på-testing av «Enable release
   immutability»-innstillinga — ikkje ei reversibel policy-sperre, men eit
   permanent per-tag-namn-merke). Løyst ved å bumpe `version:` til
   `1.10.1` **berre i worktreeen** (ikkje på `main`/HEAD — rein historisk
   tagg-korrigering), regenerere dei to artefakta som faktisk inneheldt
   versjonstalet, og tagge/dokumentere `cpsv-ap-no-v1.10.1` i staden.
   `cpsv-ap-no-v1.10.0` står att som eit permanent hoppa-over
   versjonsnummer utan release.

**Sluttresultat — stadfesta uavhengig via GitHub API** (`immutable=false`,
6 artefakt per release, for alle 16):

```
cpsv-ap-no-v1.10.1, dcat-ap-no-v2.13.0, dqv-ap-no-v1.15.0, modelldcat-ap-no-v1.14.0,
skos-ap-no-v2.16.0, brreg-begrepskatalog-v1.6.1, fair-metadata-v1.6.0,
fint-administrasjon-v4.5.1, fint-common-v4.4.0, brreg-modellkatalog-v1.5.1,
ngr-adresse-v1.6.0, ngr-eiendom-v1.6.0, ngr-person-v1.6.0, ngr-virksomhet-v1.6.0,
register-over-aksjeeiere-v1.7.0, samt-bu-v1.9.0
```

**5: Sjekk av fleire syklusar.** Samanlikna alle 22 pakkar i
`.github/release-please-manifest.json` (ikkje berre dei 16 frå PR #50) mot
faktisk tag-eksistens (`git/ref/tags/{tag}`, eksakt match). Alle 22 har no
tag. Ingen ytterlegare orphan-syklusar funne utover det som alt er
handtert (`cpsv-ap-no-v1.10.0`-unntaket dokumentert over).

**6: Grunngjeving i kode.** Kommentarblokka i `check_commit_type` (sjå
punkt 0 i scriptet) forklarer eksplisitt kvifor unntaket er naudsynt, med
referanse til denne spec-fila.

**7: Flytting.** Denne fila vert flytta til `specs/done/` som siste steg.
`git worktree`-registreringa i `.git/worktrees/release-remediation` kunne
ikkje fjernast reint (WSL «Device or resource busy»-fillås) — sjølve
katalogen er sletta, berre harmlaus metadata-registrering heng att.

**Ope spørsmål til brukar (ikkje avgjort):** bør
`create-missing-releases.sh` (som hardkodar 16 spesifikke tag/versjon-verdiar
og ein personleg heimekatalog-sti, `~/release-remediation-33627bcc/`) bli
verande i `src/assets/scripts/migreringsscript/` som eit dokumentert
historisk spor, eller fjernast no som arbeidet er fullført? Same spørsmål
for `~/release-remediation-33627bcc/`-katalogen sjølv (ligg utanfor repoet,
ikkje versjonskontrollert).
