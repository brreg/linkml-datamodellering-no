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

Dette vart opphavleg tolka som ei samspel-avgrensing mellom
`navigation.instant` og TOC-scrollspy — **utelukka** ved diagnostisk
test, sjå steg 5/6 under.

**Endeleg rotårsak, stadfesta ved live DOM-inspeksjon (steg 7):**
mkdocs-material sin innebygde TOC-scrollspy definerer "aktiv" som
*"siste overskrift du har scrolla **forbi**"* — klassen som vert lagt
til er `md-nav__link--passed md-nav__link--active`, ikkje berre
`--active`. Eit klikk på ei TOC-lenkje hoppar deg **til** overskrifta
(ho vert synleg øvst i viewporten), men ho har ikkje vorte *passert*
enno — så scrollspyen held fram med å vise **føregåande** overskrift
som aktiv heilt til brukaren scrollar vidare og den klikka overskrifta
faktisk scrollar forbi toppen av viewporten. Dette stadfesta brukaren
sitt opphavlege symptom nøyaktig (steg 7-notat under).

Klikk-fiksen frå fyrste forsøk (steg 1-4) **var lasta og køyrde**
(stadfesta via `document.querySelectorAll('script[src*="toc-active"]').length
→ 1`, ingen konsoll-feil), men tapte kappløpet: han set aktiv-klassen
synkront i klikk-handteraren, men scrollspyen sin eigen rekalkulering —
trigga av sjølve hopp-scrollen — køyrer rett etterpå og overskriv
resultatet att til føregåande overskrift, for raskt til å sjå med auga
i DevTools (stadfesta ved at den klikka lenkja stod utan aktiv-klasse
rett etter klikk i brukaren sin DOM-snapshot).

## Fiks

Ein eingongs `classList.add()` ved klikk held difor ikkje — han taper
kappløpet mot scrollspyen sin etterfølgjande rekalkulering. Fiksen
(`toc-active-click-fix.js`, omskriven i steg 8) handhevar i staden eit
**vedvarande overstyringsgrep**:

- Ved klikk: set den klikka lenkja som `override`, og legg til
  `--active` på henne
- Ein `MutationObserver` på `[data-md-component="toc"]` (`class`-attributt,
  `subtree: true`) rettar automatisk opp att kvar gong scrollspyen prøver
  å setje ei anna lenkje aktiv, så lenge `override` er sett
- Ei debounce-basert scroll-lytting sleper overstyringa når scrollinga
  har vore stille i 150ms **og** ei ny, ekte scroll-hendsing skjer
  deretter (skil hopp-scrollen frå seinare, genuin lesing/scrolling)
- Bind seg på nytt for kvar `document$`-hending, sidan TOC-DOM-noda vert
  bytt ut ved kvar instant-navigering (og no også ved vanleg
  side-navigering, sidan `navigation.instant` står avslått, sjå steg 5)

**Rotårsak 2, stadfesta ved live instrumentering (steg 9):** klikk-fiksen frå
steg 8 løyste heller ikkje problemet — og live-instrumentering synte kvifor:
ein isolert testlyttar registrert med vanleg
`link.addEventListener("click", fn)` (bubble-fasen) **fyrte aldri**, sjølv
om materials eigne class-mutasjonar (observert via MutationObserver) synte
at klikket vart handsama normalt. Dette stadfestar at mkdocs-material sin
eigen klikk-handterar på TOC-lenkjene kallar `stopImmediatePropagation()`
(eller tilsvarande) i bubble-fasen, som hindrar ALLE seinare-registrerte
bubble-fase-lyttarar frå å køyre — inkludert både steg 1-fiksen og
steg 8-fiksen, som begge brukte `addEventListener("click", ...)` utan
`capture: true`. Dette er den faktiske årsaka til at *ingen* av dei to
førre forsøka nokon gong fekk køyrt klikk-koden sin i det heile — ikkje
eit kappløp-timing-problem slik steg 4 antok.

Steg 10-fiksen registrerer difor klikk-lyttaren i **capture-fasen**
(`toc.addEventListener("click", fn, true)`, delegert via `closest()` på
TOC-containeren) — capture-fase-lyttarar køyrer FØR bubble-fase-handterarar
i det heile, og er difor upåverka av at materials handterar seinare kallar
stopImmediatePropagation() i bubble-fasen. `overrideHref` (URL-fragment)
vert brukt i staden for ein direkte DOM-node-referanse, og lenkja vert
re-henta på nytt frå `toc` ved kvar handheving — robust dersom
mkdocs-material nokon gong skulle byte ut TOC-DOM-noda (ikkje stadfesta at
dette skjer, men billeg å gardere mot).

**Rotårsak 3, den endelege (steg 11-13):** Sjølv capture-fase-fiksen
løyste ikkje problemet — og sidan capture-fase-lyttarar per spesifikasjon
ALLTID køyrer før bubble-fase-handterarar, kunne `stopImmediatePropagation()`
ikkje lenger vere forklaringa. Ein global `document`-nivå klikk-loggar
avslørte den verkelege årsaka: mkdocs-material legg TOC-innhaldet i DOM-en
**meir enn éin stad** (truleg éin kopi i sekundær skrivebord-sidefelt og
éin kopi integrert i primær-navigasjonsdraget for nettbrett-/mobilbreidde,
båe til stades samstundes i DOM-en, vist/skjult reint via CSS). Både
steg 1- og steg 10-fiksen batt seg til
`document.querySelector('[data-md-component="toc"]')`, som alltid hentar
**den fyrste** av desse kopiane i dokumentrekkjefølgje — mens brukaren sine
faktiske klikk trefte ein HEILT ANNAN, duplikat DOM-node. Stadfesta direkte:
`document.querySelector('[data-md-component="toc"] a[href="..."]') === <den faktisk klikka lenkja>`
→ `false`. Dette forklarer samtlege tre førre feilslegne forsøk fullt ut,
heilt uavhengig av kappløp- eller fase-spørsmåla som vart forfølgt undervegs.

Steg 13-fiksen droppar difor heile ideen om å finne "TOC-containeren".
Han delegerer reint på `document` sjølv (framleis capture-fasen), og
handhevar/synkroniserer aktiv-klassen på **alle** lenkjer i heile
dokumentet som deler klikka sin `href` — uavhengig av kor mange kopiar av
TOC-en som finst. `document$.subscribe`-innpakninga vart òg fjerna: sidan
bindinga no er til `document` sjølv (som aldri vert bytt ut, verken ved
vanleg eller instant-navigering), ville re-abonnering berre hopa opp
duplikate lyttarar over tid.

## Handlingsliste

1. [x] Opprett `mkdocs/docs/javascripts/toc-active-click-fix.js` med klikk-fiksen
2. [x] Legg til `extra_javascript:`-blokk i `publish.sh` sin `mkdocs.yml`-heredoc
3. [x] Statisk verifisering av DOM-selector mot mkdocs-material 9.7 (via
   `src/assets/containers/Dockerfile.mkdocs`) — `data-md-component="toc"`
   er stabil sidan mkdocs-material v8+
4. [x] Brukaren verifiserte live i nettlesar etter ny køyring av
   generate-workflowen — **fiksen løyste ikkje problemet**. Klikk-fiksen
   set `md-nav__link--active` synkront i klikk-handteraren, men
   mkdocs-material sin eigen scrollspy (IntersectionObserver-driven,
   ikkje klikk-driven) held fram med å re-evaluere aktiv lenkje på kvar
   scroll-hendsing under sjølve hopp-animasjonen — og overskriv difor
   klikk-fiksen sitt resultat før scrollen har nådd fram, akkurat slik
   root-årsak-avsnittet skildrar for det opphavlege symptomet. Fiksen var
   difor for enkel: han vinn berre den fyrste rendringa, ikkje kappløpet
   mot etterfølgjande observer-oppdateringar.
5. [x] Diagnostisk test: kommenterte ut `navigation.instant` i
   `theme.features` (`publish.sh` linje ~517) for å isolere om det er
   samspelet mellom `navigation.instant` og TOC-scrollspyen som er
   årsaka. Kunne **ikkje** byggjast/testast i dette verktøymiljøet (sjå
   Avgrensingar). **Brukaren stadfesta i nettlesar: problemet
   vedvarer framleis uendra med `navigation.instant` avslått.**
   `navigation.instant` er difor **utelukka** som (einaste) årsak —
   ikkje eit SPA-navigasjon-samspel-problem. `navigation.instant` er
   ståande avslått i påvente av vidare feilsøking (kan slåast på att
   når rotårsaka er stadfesta og retta).
6. [x] Konklusjon av steg 5: årsaka ligg i mkdocs-material sin
   TOC-scrollspy sjølv, ikkje eit samspel med `navigation.instant`.
7. [x] Live DOM-inspeksjon (brukaren, Elements-panel i DevTools) på
   `mkdocs/docs/oreg/javazonetalk/index.md` — klikka "Avhengigheiter":
   lenkja fekk **ikkje** `--active` (stod som rein `class="md-nav__link"`),
   medan "Python-bruk" (føregåande overskrift) var aktiv. Fyrst når
   "Avhengigheiter"-overskrifta scrolla heilt forbi (ut av viewporten
   øvst) fekk lenkja `md-nav__link--passed md-nav__link--active`.
   Stadfesta at (a) `toc-active-click-fix.js` var lasta og køyrde utan
   konsollfeil (`document.querySelectorAll('script[src*="toc-active"]').length → 1`),
   og (b) den endelege rotårsaka er "aktiv" = "siste overskrift scrolla
   forbi", ikkje eit terskel-/timing-avvik i sjølve observerbaren.
8. [x] Omskreiv `toc-active-click-fix.js` til å handheve eit vedvarande
   overstyringsgrep via `MutationObserver` + debounce-basert
   scroll-slepp (sjå § Fiks) i staden for ei eingongs klassesetjing.
   **Ikkje verifisert live** — same `podman rootless`-avgrensing hindrar
   bygg i dette verktøymiljøet (sjå Avgrensingar).
9. [x] Brukaren verifiserte live i nettlesar etter `make docs-publish && make docs-serve`
   — **problemet vedvarte framleis**, og synte i tillegg to nye
   symptomvariantar (fyrste TOC-menypunkt fekk aldri aktiv-klasse; klikk på
   nest-siste menypunkt viste siste menypunkt som aktivt) — begge
   konsistente med at scrollspyen framleis køyrde heilt uhindra. Live
   instrumentering via injisert konsoll-script stadfesta rotårsak 2 (sjå
   § Rotårsak/Fiks over): ein bubble-fase `click`-lyttar fyrer aldri på
   desse TOC-lenkjene i det heile.
10. [x] Omskreiv `toc-active-click-fix.js` til å registrere klikk-lyttaren
    i **capture-fasen** (delegert på `toc`-containeren via `closest()`)
    i staden for bubble-fasen, og til å re-henta lenkje-referansen frå
    `href` ved kvar handheving i staden for å halde på ein direkte
    node-referanse. **Ikkje verifisert live** — same
    `podman rootless`-avgrensing hindrar bygg i dette verktøymiljøet.
11. [x] Brukaren verifiserte live i nettlesar etter `make docs-publish && make docs-serve`
    — **problemet vedvarte, identisk med før**. To parallelle diagnostikkar
    utelukka reihenfølgje-teoriar frå steg 9/10:
    - Nettverksfana (cache avslått, hard refresh) stadfesta at nettlesaren
      faktisk køyrde den **nyaste** skriptversjonen (innhaldet inneheldt
      `capture`) — utelukka forelda/mellomlagra skript som årsak.
    - Ein global, `document`-nivå capture-fase klikk-loggar (upåverka av
      KVA node skriptet trudde var "TOC-containeren") stadfesta at det
      *faktiske* klikket skjedde på ein HEILT ANNAN DOM-node enn den
      `document.querySelector('[data-md-component="toc"] a[href="..."]')`
      fann: `same node as toc query result: false`.
12. [x] **Endeleg rotårsak 3, stadfesta:** mkdocs-material legg
    TOC-innhaldet i DOM-en meir enn éin stad (truleg éin kopi i det
    sekundære skrivebord-sidefeltet og éin kopi integrert i det primære
    navigasjonsdraget for nettbrett-/mobilbreidde, båe til stades
    samstundes, vist/skjult reint via CSS media queries). Alle tre
    tidlegare forsøk (steg 1, 8, 10) batt seg til `document.querySelector('[data-md-component="toc"]')`
    — som alltid hentar **den fyrste** kopien i dokumentrekkjefølgje —
    medan brukaren sine faktiske klikk skjedde på ein ANNAN, duplikat
    DOM-node. Dette forklarer alle tre førre feilslegne forsøk fullt ut:
    verken bubble- eller capture-fase-lyttaren batt til feil node kunne
    nokon gong sjå det verkelege klikket, heilt uavhengig av
    fase-spørsmålet som vart forfølgt i steg 9-10.
13. [x] Omskreiv `toc-active-click-fix.js` til å **ikkje** leite etter "TOC-containeren"
    i det heile — delegerer no reint på `document` (capture-fasen), og
    handhevar/synkroniserer aktiv-klassen på ALLE lenkjer som deler klikka
    sin `href`, uavhengig av kor mange kopiar av TOC-en som finst i DOM-en.
    Fjerna `document$.subscribe`-innpakninga (unødvendig og potensielt
    skadeleg — ville hopa opp duplikate `document`-lyttarar ved kvar
    instant-navigering, sidan `document` sjølv aldri vert bytt ut).
    **Ikkje verifisert live** — same `podman rootless`-avgrensing hindrar
    bygg i dette verktøymiljøet.
14. [x] Brukaren verifiserte live i nettlesar etter `make docs-publish && make docs-serve`
    — **fiksen fungerer.** TOC-menypunktet vert no markert aktivt
    umiddelbart ved klikk og held seg markert til brukaren scrollar vidare.
15. [ ] `navigation.instant` står framleis avslått i `publish.sh` (var berre
    eit diagnostisk grep frå steg 5, sidan utelukka som årsak — fiksen er
    uavhengig av han). Ståande open avgjerd: behalde avslått, eller slå på
    att no som TOC-fiksen fungerer utan omsyn til han. Sjå `publish.sh`
    linje ~517.

## Avgrensingar

`podman rootless` var utilgjengeleg i verktøymiljøet på
verifiseringstidspunktet (`newuidmap: write to uid_map failed: Operation
not permitted`) — same kjende avgrensing som dokumentert i
`specs/backlog/javazone-demo-plan.md`. Fiksen er difor verifisert
statisk (kodelesing + mkdocs-material sin dokumenterte DOM-struktur),
**ikkje** ein reell `make docs-build`/`docs-serve`-køyring i nettlesar.
Brukaren bør stadfeste i nettlesar før specen vert rekna som fullt utført.

Stadfesta på nytt ved diagnostisk-test-økta (steg 5): `make docs-publish`
feilar framleis med same `newuidmap`-feil i dette verktøymiljøet. Alle
faktiske nettlesar-verifiseringar må difor gjerast av brukaren lokalt.

## Utført

TOC-menypunktet vert no markert aktivt umiddelbart ved klikk, og held seg
markert til brukaren faktisk scrollar vidare — stadfesta live av brukaren
(steg 14). Løysinga kravde tre iterasjonar før rett rotårsak vart funnen:

1. Rotårsak 1 (scrollspy = "siste overskrift scrolla forbi") — rett
   diagnose, men fyrste fiksen (eingongs `classList.add()` ved klikk) var
   for enkel til å halde stand mot scrollspyen sin etterfølgjande
   rekalkulering.
2. Rotårsak 2-hypotesen (`stopImmediatePropagation()` i bubble-fasen)
   synte seg feil — utelukka når capture-fase-fiksen heller ikkje verka.
3. Rotårsak 3, den faktiske: mkdocs-material dupliserer TOC-innhaldet i
   DOM-en (skrivebord- og nettbrett-/mobil-integrert kopi samstundes), og
   `document.querySelector('[data-md-component="toc"]')` fann konsekvent
   feil kopi. Fiksen droppa heile ideen om å finne "containeren" og
   delegerer i staden reint på `document`, og synkroniserer alle lenkjer
   som deler klikka sin `href`.

**Open oppfølging:** `navigation.instant` står avslått i `publish.sh`
(diagnostisk grep frå eit tidlegare steg, sidan utelukka som årsak til
denne feilen). Fiksen er uavhengig av han. Vurder i ei seinare økt om han
skal slåast på att (raskare sidenavigering) eller behaldast avslått.
