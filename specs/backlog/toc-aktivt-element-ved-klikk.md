# Spec: TOC-menypunkt vert ikkje markert aktivt ved klikk

## Bakgrunn

Brukaren rapporterte: når du klikkar på eit element i "Table of contents"
(TOC, den høgre menyen på kvar side i mkdocs-portalen) og hoppar til
overskrifta, vert menypunktet **ikkje** markert som aktivt med éin gong.
Presisering frå brukaren: menypunktet til overskrifta **over** den du
faktisk klikka på vert markert som aktivt i staden. Først når du
scrollar litt nedover — og "går inn i" innhaldsblokka under den klikka
overskrifta — hoppar markeringa over til rett menypunkt.

## Rotårsak

Git-arkeologi i `mkdocs/publish.sh` sin historie:

- Commit `53014ce4` la opphavleg til ein eigen `nav-active-fix.js` +
  `extra_javascript`-oppføring for å styre aktivt-menypunkt-markering.
- Commit `54645a49` ("forbetre visuell hierarki og navigasjon") **kommenterte
  ut** `extra_javascript`-blokka same commit som `toc.follow` vart aktivert
  i `theme.features` og eigen CSS for `.md-nav__link--active` vart lagt
  til — altså eit medvite skifte til å stole på mkdocs-material sin
  **innebygde** TOC-scrollspy, ikkje ein eigen JS-basert fiks.
- Ein seinare commit fjerna `extra_javascript`-blokka (då berre kommentarar)
  heilt frå `publish.sh`. `mkdocs/docs/javascripts/nav-active-fix.js` ligg
  difor att i repoet, men er **ikkje lasta** i det publiserte skjemaet
  (verken via `extra_javascript` eller `theme.custom_dir` — begge fråverande
  i `mkdocs.yml`-heredoc-blokka i `publish.sh`). Han er dødt, urelatert
  innhald til denne feilen (skal ikkje slettast som del av denne specen,
  jf. "minimale endringar" i CLAUDE.md — nemnt her berre til opplysning).

Den faktiske feilen er difor mkdocs-material sin eigen innebygde
TOC-scrollspy, i kombinasjon med `navigation.instant` (aktivert i
`theme.features` i `publish.sh`). `navigation.instant` fangar opp klikk
på interne lenkjer — også reine same-side-ankerlenkjer i TOC-en — og
handterer dei via sin eigen historie-/viewport-observerbare i staden for
ein vanleg nettlesar-ankerhopp. Denne observerbare sitt "kva overskrift
er aktiv no"-oppslag vert sampla **før** scroll-posisjonen faktisk har
nådd den klikka overskrifta, og fell difor attende til den **føregåande**
overskrifta (den du framleis "står i" i det augeblinket klikket vert
handsama) — akkurat symptomet brukaren skildra. Markeringa rettar seg
sjølv med neste ekte scroll-hendsing, sidan IntersectionObserver-en då
får eit nytt, korrekt sample.

Dette er ei kjend samspel-avgrensing mellom `navigation.instant` og
TOC-scrollspy i mkdocs-material (ikkje ein feil introdusert av dette
repoet sin eigen kode) — stadfesta statisk (ingen live nettlesar-test
var mogleg i verktøymiljøet, sjå Avgrensingar under).

## Fiks

Legg til eit lite, målretta skript som gjev TOC-lenkjer **umiddelbar,
optimistisk** aktiv-markering ved klikk — uavhengig av mkdocs-material
sin interne scrollspy-timing. Skriptet:

- Bind seg til `[data-md-component="toc"]` (den same, versjonsstabile
  selectoren mkdocs-material sjølv brukar internt for å finne TOC-en)
- Ved klikk på ei TOC-lenkje: fjern `md-nav__link--active` frå alle
  TOC-lenkjer, legg han til på den klikka lenkja
- Bind seg på nytt for kvar `document$`-hending (Material sin eigen
  observerbare for sidenavigering under `navigation.instant`), sidan
  DOM-noda vert bytt ut ved kvar instant-navigering

Skriptet **fightar ikkje** mot mkdocs-material sin eigen scrollspy —
det set berre eit korrekt, umiddelbart gjetta resultat som uansett er
det scrollspy-en sjølv konvergerer mot med det same brukaren scrollar
vidare. Ingen risiko for varig inkonsistens.

## Handlingsliste

1. [x] Opprett `mkdocs/docs/javascripts/toc-active-click-fix.js` med klikk-fiksen
2. [x] Legg til `extra_javascript:`-blokk i `publish.sh` sin `mkdocs.yml`-heredoc
3. [x] Statisk verifisering av DOM-selector mot mkdocs-material 9.7 (via
   `src/assets/containers/Dockerfile.mkdocs`) — `data-md-component="toc"`
   er stabil sidan mkdocs-material v8+
4. [ ] Brukaren verifiserer live i nettlesar etter `make docs-publish && make docs-serve`
   (kunne ikkje gjerast i dette verktøymiljøet — sjå Avgrensingar)

## Avgrensingar

`podman rootless` var utilgjengeleg i verktøymiljøet på
verifiseringstidspunktet (`newuidmap: write to uid_map failed: Operation
not permitted`) — same kjende avgrensing som dokumentert i
`specs/backlog/javazone-demo-plan.md`. Fiksen er difor verifisert
statisk (kodelesing + mkdocs-material sin dokumenterte DOM-struktur),
**ikkje** ein reell `make docs-build`/`docs-serve`-køyring i nettlesar.
Brukaren bør stadfeste i nettlesar før specen vert rekna som fullt utført.
