function setActiveNav() {
  const path = window.location.pathname;

  document.querySelectorAll('.md-nav__link').forEach(link => {
    // fjern eksisterande active classes
    link.classList.remove('md-nav__link--active');

    // match path (ikkje hash!)
    const href = link.getAttribute('href');
    if (href && path.endsWith(href.replace(/^\.\.\//g, ''))) {
      link.classList.add('md-nav__link--active');
    }
  });
}

// Kjør både på initial load og ved SPA navigation
document$.subscribe(function () {
  setActiveNav();
});