// Fiks: TOC-menypunktet du klikkar på vert ikkje markert aktivt før neste
// scroll-hendsing (mkdocs-material sin innebygde TOC-scrollspy samplar
// aktiv overskrift før scroll-posisjonen har nådd målet ved
// navigation.instant-hopp, og fell attende til overskrifta over — sjå
// specs/backlog/toc-aktivt-element-ved-klikk.md for grunngjeving).
// Set difor aktiv-klasse umiddelbart ved klikk, uavhengig av scrollspy-timing.
document$.subscribe(function () {
  var toc = document.querySelector('[data-md-component="toc"]');
  if (!toc) return;
  toc.querySelectorAll(".md-nav__link").forEach(function (link) {
    link.addEventListener("click", function () {
      toc.querySelectorAll(".md-nav__link--active").forEach(function (active) {
        active.classList.remove("md-nav__link--active");
      });
      link.classList.add("md-nav__link--active");
    });
  });
});
