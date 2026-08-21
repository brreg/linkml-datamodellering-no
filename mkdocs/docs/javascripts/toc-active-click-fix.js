// Fiks: TOC-menypunktet du klikkar på vert ikkje markert aktivt ved klikk.
//
// Rotårsak 1 (stadfesta ved live DOM-inspeksjon): mkdocs-material sin
// innebygde TOC-scrollspy definerer "aktiv" som "siste overskrift du har
// scrolla FORBI" (klassen `md-nav__link--passed` føljer `--active`) — ikkje
// overskrifta du nett hoppa til.
//
// Rotårsak 2 (stadfesta ved live instrumentering — sjå
// specs/backlog/toc-aktivt-element-ved-klikk.md, steg 13): mkdocs-material
// legg TOC-innhaldet i DOM-en **meir enn éin stad** — truleg éin kopi i det
// sekundære skrivebord-sidefeltet og éin kopi integrert i det primære
// navigasjonsdraget for nettbrett-/mobilbreidde, båe til stades samstundes
// i DOM-en og vist/skjult reint via CSS media queries (ikkje JS-styrt
// på/av-kopling). `document.querySelector('[data-md-component="toc"]')`
// hentar alltid **den fyrste** av desse i dokumentrekkjefølgje — noko som
// synte seg IKKJE vere same DOM-node som den brukaren faktisk klikkar på.
// Alle tidlegare forsøk (bubble-fase-lyttar, deretter capture-fase-lyttar,
// begge scoped til denne fyrste treffen) batt seg difor til feil node og
// fekk aldri sjå det verkelege klikket — stadfesta direkte ved
// `document.querySelector(...) === <den faktisk klikka noden>` → `false`.
//
// Fiksen unngår difor å leite etter "TOC-containeren" i det heile.
// Han delegerer reint på `document` (capture-fasen, upåverka av
// eventuelle stopImmediatePropagation-kall i bubble-fasen), og
// handhevar/synkroniserer aktiv-klassen på ALLE lenkjer som deler
// klikka sin `href` — uansett kor mange kopiar av TOC-en som finst i
// DOM-en, og uavhengig av kva for éin brukaren fysisk klikka på.
//
// Ein eingongs `classList.add()` held likevel ikkje åleine, sidan
// scrollspyen sin eigen rekalkulering (trigga av sjølve hopp-scrollen)
// køyrer rett etterpå og ville overskrive resultatet att. Fiksen handhevar
// difor eit vedvarande overstyringsgrep via ein MutationObserver, heilt til
// brukaren scrollar vidare (etter at sjølve hopp-scrollen har stabilisert
// seg) — då vert kontrollen gjeve attende til scrollspyen sin vanlege
// oppførsel.
//
// Merk: koda bind seg éin gong ved skriptlasting (ikkje inni
// `document$.subscribe`) — bindinga er til `document` sjølv, som aldri
// vert bytt ut ved instant-navigering, så ei ny binding for kvar
// side-overgang ville berre hopa opp duplikate lyttarar.
(function () {
  var overrideHref = null;
  var settleTimer = null;

  function matchingLinks(href) {
    return document.querySelectorAll('.md-nav__link[href="' + CSS.escape(href) + '"]');
  }

  function enforceOverride() {
    if (!overrideHref) return;
    var wanted = matchingLinks(overrideHref);
    if (!wanted.length) return;
    document.querySelectorAll(".md-nav__link--active").forEach(function (link) {
      if (link.getAttribute("href") !== overrideHref) {
        link.classList.remove("md-nav__link--active");
      }
    });
    wanted.forEach(function (link) {
      if (!link.classList.contains("md-nav__link--active")) {
        link.classList.add("md-nav__link--active");
      }
    });
  }

  var observer = new MutationObserver(enforceOverride);
  observer.observe(document.body, { attributes: true, attributeFilter: ["class"], subtree: true });

  function releaseOverride() {
    overrideHref = null;
    window.removeEventListener("scroll", onScroll, { passive: true });
  }

  // Debounce: kvar scroll-hendsing utsett "har stabilisert seg"-punktet.
  // Fyrste scroll-hendsing ETTER at scrollinga har vore stille i 150ms er
  // ei ekte, ny brukarhandling (ikkje del av klikk-hoppet) — då gjev vi
  // slepp på overstyringa.
  function onScroll() {
    clearTimeout(settleTimer);
    settleTimer = setTimeout(function () {
      window.addEventListener("scroll", releaseOverride, { once: true, passive: true });
    }, 150);
  }

  document.addEventListener(
    "click",
    function (event) {
      var link = event.target.closest(".md-nav__link");
      if (!link) return;

      clearTimeout(settleTimer);
      window.removeEventListener("scroll", releaseOverride, { passive: true });
      window.removeEventListener("scroll", onScroll, { passive: true });

      overrideHref = link.getAttribute("href");
      enforceOverride();

      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    },
    true
  );
})();
