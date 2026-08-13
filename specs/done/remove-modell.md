# Nytt make-target: remove-modell

## Bakgrunn

`make new-modell` scaffoldar ein ny domenemodell (skjema, `build.yaml`,
`examples/`, `description.md`) og oppdaterer `.github/valid-scopes.txt`
automatisk. Det finst ingen tilsvarande motpart for å **fjerne** ein modell —
sletting må i dag gjerast manuelt, og det er lett å gløyme følgjefilene og
referansane som må ryddast opp samstundes.

Ein gjennomgang av repoet (sjå samandrag under) synte at rein `rm -rf` av
modellkatalogen dekkjer det meste, men ikkje alt:

**Treng manuell/automatisk oppfølging:**
- `.github/valid-scopes.txt` er ei committa, auto-generert fil
  (`make update-valid-scopes`) som listar modellnamn brukt til å validere
  commit-scope i `.github/workflows/release-please.yml`. Vert ikkje
  automatisk oppdatert av ei manuell `rm -rf`.
- Andre `build.yaml`-filer kan liste modellen under `submodels:`
  (i dag brukt av `src/linkml/ap-no/dqv-ap-no/build.yaml` → `dqv-core` og
  `src/linkml/ap-no/modelldcat-ap-no/build.yaml` → `modelldcat-modell`,
  `modelldcat-katalog`). Sletting av ein submodel utan å fjerne referansen
  frå foreldre-manifestet gir ei broten referanse i portalen.
- Andre skjema kan importere modellen via `imports:` (uvanleg for ein
  ordinær domenemodell, men ikkje strukturelt umogleg).
- Dersom `build.yaml` har `publish_external: true` og modellen har ei
  `published-uris.lock`-fil, sporar denne fila det einaste lokale beviset
  på kva som er publisert til Felles Datakatalog/Felles Begrepskatalog.
  Repoet **pushar aldri** til eksterne system (sjå prinsippet i
  `CLAUDE.md`), så ei rein sletting fjernar ikkje den eksterne oppføringa —
  ho vert ståande att, foreldrelaus, til nokon avpubliserer henne manuelt i
  det eksterne systemet.

**Treng IKKJE oppfølging (ordnar seg sjølv eller er irrelevant):**
- `generated/<domain>/<modell>/` og `mkdocs/docs/<domain>/<modell>/` er
  `.gitignore`-a byggoutput. `mkdocs/publish.sh` sitt steg 1 fjernar
  domenekatalogar frå `mkdocs/docs/` som ikkje lenger finst i `generated/`
  ved neste `make docs-publish`.
- `CODEOWNERS.md` brukar domenenivå-glob (t.d. `src/linkml/oreg/**`), ikkje
  per-modell-stiar — treng berre endring dersom modellen er den **siste** i
  eit heilt domene som skal fjernast (utanfor scope for dette tiltaket).
- README.md sine domeneoversiktstabellar er på domenenivå, ikkje per modell.

**Mål:** eit `make remove-modell`-target som utfører desse sjekkane
automatisk, varslar om blokkerande/ikkje-blokkerande funn, og gjer sjølve
filslettinga — parallelt motstykke til `make new-modell`.

## Design

**Kommandoform** (mirrorar `new-modell` sin signatur):

```bash
make remove-modell NAME=<modell> DOMAIN=<domain> [CONFIRM=1]
```

- **Utan `CONFIRM=1`** (standard): køyrer alle sjekkar, viser ei
  dry-run-oversikt over kva som ville blitt sletta og eventuelle åtvaringar,
  men gjer ingen filsystemendringar. Dette er default nettopp fordi
  operasjonen — i motsetnad til `make clean` (byggoutput, regenererbart) —
  slettar kjeldeinnhald som ikkje kan gjenskapast automatisk.
- **Med `CONFIRM=1`**: køyrer sjekkane; blokkerande funn (submodels- eller
  imports-referansar) stoppar likevel operasjonen uavhengig av `CONFIRM`.
  Ikkje-blokkerande åtvaringar (publish_external) tillèt sletting å halde
  fram, men vert framleis printa. Deretter: fysisk sletting av
  modellkatalogen + `make update-valid-scopes`.

Same flagg-stil som eksisterande `DRYRUN=1`/`ORG=`-mønster i
`gen-modelldcat-elements` (sjå `COMMANDS.md`), men med motsett polaritet av
gode grunnar: destruktive operasjonar bør krevje eksplisitt opt-in for å
utføre, ikkje eksplisitt opt-in for å førehandsvise.

**Nytt script:** `src/assets/scripts/scaffolding/remove-modell.sh`
(same katalog og `REPO_ROOT`-mønster som `new-modell.sh`,
`new-modellkatalog.sh` osv. — merk `../../../..` for å nå repo-rota, jf.
BUG-fiksen i `specs/done/`-historikken der scripta ein gong hadde
`../../..` og landa feil).

**Nytt Makefile-target:** i `make/70-scaffolding.mk`, ved sida av
`new-modell`.

## Steg

1. **Valider input** — `NAME` og `DOMAIN` er obligatoriske (same feilmelding-
   mønster som `new-modell.sh`). Feil dersom
   `src/linkml/$DOMAIN/$NAME/` ikkje finst.

2. **Sjekk submodels-referansar** — grep alle `src/linkml/*/*/build.yaml`
   etter `submodels:`-blokker som listar `$NAME`. Finn treff → blokkerande
   feil som listar kva foreldre-`build.yaml` som må rettast først (fjern
   lina manuelt), uavhengig av `CONFIRM`.

3. **Sjekk imports-referansar** — grep alle andre `*-schema.yaml` sine
   `imports:`-lister etter ein sti som peikar til
   `$DOMAIN/$NAME/$NAME-schema`. Finn treff → blokkerande feil som listar
   kva skjema som importerer modellen.

4. **Sjekk publish_external / published-uris.lock** — les
   `build.yaml.publish_external` og sjekk om
   `src/linkml/$DOMAIN/$NAME/published-uris.lock` finst. Finn eitt av
   desse → ikkje-blokkerande åtvaring: forklar at eksterne
   katalogoppføringar ikkje vert automatisk fjerna (repoet pushar aldri),
   og vis til deprekeringsmønsteret i
   `mkdocs/docs/publisering/publisering-begrep.md` § «Deprekere eit
   begrep» som alternativ til sletting. Krev `CONFIRM=1` for å halde fram
   forbi denne åtvaringa.

5. **Vis dry-run-oversikt** — list alle filer/mapper som vil bli sletta
   (`find src/linkml/$DOMAIN/$NAME -type f`). Vert alltid vist, både i
   dry-run- og CONFIRM-modus.

6. **Fysisk sletting** — berre når `CONFIRM=1` er sett OG steg 2/3 ikkje
   fann blokkerande treff: `rm -rf src/linkml/$DOMAIN/$NAME`.

7. **Regenerer `.github/valid-scopes.txt`** — køyr
   `make --no-print-directory update-valid-scopes` etter sletting (same
   mønster som `new-modell.sh` sitt siste steg).

8. **Oppdater `help.sh`-kategorisering** — `Vedlikehald`-mønsteret i
   `src/assets/scripts/makefile/help.sh` er i dag
   `(update-|new-|check-)` og fangar difor ikkje opp `remove-modell`.
   Utvid til `(update-|new-|remove-|check-)` slik at targetet dukkar opp
   under rett kategori i `make help`.

9. **Dokumenter** — legg til eit kort avsnitt «Slette ein modell» i
   `mkdocs/docs/kom-i-gang/ny-domenemodell.md` (etter mønster frå
   samtalen som er grunnlaget for dette tiltaket) som viser kommandoen og
   dei fire sjekk-kategoriane frå «Bakgrunn».

10. **Testar** — legg til eit testtilfelle i `tests/test_make.sh` (eller
    tilsvarande) som: (a) scaffoldar ein midlertidig testmodell med
    `new-modell`, (b) køyrer `remove-modell` utan `CONFIRM` og verifiserer
    at filene framleis finst (dry-run), (c) køyrer med `CONFIRM=1` og
    verifiserer sletting + at `valid-scopes.txt` er oppdatert, (d)
    verifiserer at blokkerande-sjekken faktisk blokkerer ved å late
    testmodellen bli lista som submodel i eit anna `build.yaml` først.

## Handlingsliste

- [x] 1: Valider input i `remove-modell.sh` (NAME/DOMAIN påkravd, katalog må finnast)
- [x] 2: Implementer submodels-referanse-sjekk (blokkerande)
- [x] 3: Implementer imports-referanse-sjekk (blokkerande)
- [x] 4: Implementer publish_external/published-uris.lock-sjekk (åtvaring + krev CONFIRM)
- [x] 5: Implementer dry-run-oversikt over filer som vil bli sletta
- [x] 6: Implementer fysisk sletting bak `CONFIRM=1`
- [x] 7: Integrer `make update-valid-scopes` etter sletting
- [x] 8: Nytt Makefile-target `remove-modell` i `make/70-scaffolding.mk`
- [x] 9: Utvid `Vedlikehald`-mønster i `help.sh` med `remove-`
- [x] 10: Dokumenter i `mkdocs/docs/kom-i-gang/ny-domenemodell.md`
- [x] 11: Manuell testrunde (sjå Utført — vurdert som betre eigna enn `tests/test_make.sh`)
- [x] 12: Manuell verifisering med reelle testmodellar (ingen CI-filer rørte → actionlint ikkje aktuelt)
- [x] 13: Flytt spec til `specs/done/` med `## Utført`-seksjon

## Utført

**1–7 (remove-modell.sh):** Implementert i
`src/assets/scripts/scaffolding/remove-modell.sh`. Submodels-sjekken brukar
`python3 -c "import yaml"` (same mønster som `new-modell.sh`) til å lese
`submodels:`-lista i alle `src/linkml/*/*/build.yaml` og samanlikne mot
modellnamnet. Imports-sjekken brukar `grep -rlE` etter
`<domain>/<modell>/<modell>-schema`-mønsteret i alle `*-schema.yaml`,
ekskludert modellen sin eigen katalog. `publish_external`/
`published-uris.lock`-sjekken er åtvarande, ikkje blokkerande — ho krev
ikkje `CONFIRM`, men vert alltid vist når treff finst. Dry-run
(`find "$SCHEMA_DIR" -type f`) vert alltid vist, uavhengig av `CONFIRM`.
Fysisk sletting (`rm -rf "$SCHEMA_DIR"`) og `make update-valid-scopes` køyrer
berre når `CONFIRM_FLAG == "--confirm"` OG ingen blokkerande funn.

**8: Makefile-target.** Lagt til `remove-modell:` i `make/70-scaffolding.mk`,
same mønster som `new-modell:` (input-validering via `LOG_FUNCTIONS`, deretter
kall til scriptet). `CONFIRM=1` → `--confirm`-flagg til scriptet, same
`$(if $(FLAG),--flag)`-mønster som `gen-modelldcat-elements` sin
`DRYRUN=1` → `--dry-run`.

**9: help.sh.** `Vedlikehald`-mønsteret utvida frå `(update-|new-|check-)` til
`(update-|new-|remove-|check-)`. Verifisert med `make help` — `remove-modell`
dukkar no opp under «Vedlikehald» ved sida av `new-modell`.

**10: Dokumentasjon.** Lagt til «Slette ein modell»-avsnitt i
`mkdocs/docs/kom-i-gang/ny-domenemodell.md` (mellom scaffolding-seksjonen og
Importhierarki), med kommandoeksempel og tabell over dei tre sjekk-typane.

**11–12: Testing.** Vurderte å leggje testtilfelle i `tests/test_make.sh`,
men fila er strukturert rundt `test_gen_*`/`test_roundtrip_*`-funksjonar som
køyrer **per oppdaga skjema** — ikkje eigna for eit scaffolding-script som
opprettar/slettar heile modellkatalogar. Valde manuell verifisering i staden,
med fire scenario mot ein midlertidig testmodell (`oreg/testfjerning`,
oppretta med `make new-modell`):

1. **Dry-run** (`make remove-modell NAME=testfjerning DOMAIN=oreg`) — synte
   riktig fil-liste, sletta ingenting, exit 0.
2. **Blokkerande submodels** — la mellombels til `- testfjerning` under
   `submodels:` i `src/linkml/ap-no/dqv-ap-no/build.yaml`; kommandoen
   blokkerte korrekt sjølv med `CONFIRM=1` (exit 1). Endringa vart
   reversert (stadfesta med `git diff` — ingen skilnad).
3. **Blokkerande imports** — la mellombels til ein import av
   `testfjerning-schema` i
   `src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml`;
   blokkerte korrekt sjølv med `CONFIRM=1`. Reversert (stadfesta med
   `git diff` — ingen skilnad).
4. **Fullstendig sletting** (`CONFIRM=1`, ingen blokkerande funn) — sletta
   katalogen og oppdaterte `.github/valid-scopes.txt` korrekt (38 → 37
   scopes).
5. **Åtvaring** — testa med ein separat testmodell
   (`oreg/testfjerning2`, `publish_external: true`): åtvaringa vart vist i
   dry-run-modus utan å blokkere, og sletting gjekk gjennom ved `CONFIRM=1`.

Alle testmodellar og mellombelse endringar er fjerna att —
`git status`/`git diff` viser ingen attverande spor i repoet.

**13: Flytting.** Denne fila vert flytta til `specs/done/remove-modell.md`
som siste steg.
