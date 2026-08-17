# Bug: LinkML sin `DocGenerator.link_mermaid()` limer `../` framanfor absolutte eksterne URL-ar

**ID:** BUG-13
**Status:** `upstream`
**Komponent:** `linkml` (`linkml/generators/docgen.py`, `DocGenerator.link_mermaid()`)
**Oppdaga:** 2026-08-13

## Symptom

I genererte klasse-/slot-sider (`mkdocs/docs/**/klasser/*.md`) sitt mermaid
`classDiagram` peikar `click <Typenavn> href "..."`-direktiv for elementære
`linkml:types`-typar som er **importerte, ikkje lokalt omdefinerte** i
skjemaet (t.d. `uri`, `uriorcurie`, `string`) til ei broten pseudo-relativ
lenkje der ein absolutt ekstern URL har fått eit `../`-prefiks limt framanfor
seg:

```
click Uri href "../http://www.w3.org/2001/XMLSchema#anyURI/"
click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
```

Strippar ein det feilaktige `../`-prefikset, resolverer resten til ein ekte,
gyldig lenkje til W3C sin XSD-spesifikasjon
(`https://www.w3.org/2001/XMLSchema#anyURI`) — det tilsikta lenkjemålet.
Med `../` framanfor vert han i staden ei ugyldig, ikkje-navigerbar sti som
nettlesaren tolkar relativt til gjeldande side.

Reprodusert i `mkdocs/docs/ap-no/cpsv-ap-no/klasser/offentligorganisasjon.md`
(lokal byggartefakt datert 2026-08-11, før `mkdocs/lib/copy_artifacts.sh`
sin href-ombygging frå `25bb4321` vart innført) — sjå
`specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md` for
full utleiing og fleire eksempel (`adresse.md`, `rektor.md`).

## Berørte skjema

Alle skjema som brukar minst éin elementær `linkml:types`-type på ein slot
**utan** at typen er lokalt omdefinert i skjemaet sin eigen `types:`-blokk —
stadfesta for `ap-no/cpsv-ap-no` og `oreg/enhetsregisteret-bvrinn` (`string`,
`uri`, `uriorcurie`) og for `samt/samt-bu` (`string`, `uriorcurie`,
`boolean`, `date`, `double`, `float`), men rotårsaka er generisk i `gen-doc`
og gjeld praktisk talt alle domenemodellar i repoet. Stadfesta ved ein fersk
`make gen-docs`-køyring 2026-08-13 (rå `generated/<domain>/<schema>/docs/*.md`,
før `copy_artifacts.sh` har rørt filene) at mønsteret held identisk for alle
desse — ikkje berre dei tre opphavleg testa typane.

## Rot-årsak (stadfesta ved kjeldekodelesing)

Stadfesta mot lokalt installert `linkml==1.10.0rc4`
(`site-packages/linkml/generators/docgen.py`):

```python
# docgen.py:537-543 — _is_external()
def _is_external(self, element: Element) -> bool:
    if element is None:
        return False
    if element.from_schema == "https://w3id.org/linkml/types" and not self.genmeta:
        return True
    else:
        return False

# docgen.py:480-481 — link(), for TypeDefinition-element som er "eksterne"
if self._is_external(e):
    return self.uri_link(e)
    # → uri_link() returnerer f"[{curie}]({uri})", der `uri` er den fullt
    #   ekspanderte URI-en, t.d. "http://www.w3.org/2001/XMLSchema#anyURI"

# docgen.py:446-459 — link_mermaid(), brukt av class_diagram.md.jinja2
def link_mermaid(self, e):
    md_link = self.link(e)                       # "[xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI)"
    if not md_link.endswith(")"):
        return md_link
    link = md_link.rsplit("(")[-1][:-1]           # "http://www.w3.org/2001/XMLSchema#anyURI"
    link = link.removesuffix(".md")               # ingen endring (endar ikkje på .md)
    return f"../{link}/"                          # "../http://www.w3.org/2001/XMLSchema#anyURI/"
```

`DocGenerator` har altså ei medviten, eiga grein for typar importerte uendra
frå `linkml:types` (`_is_external()`): dei skal lenkjast **eksternt** til
W3C/XSD sin definisjon, ikkje til ei lokal side — `gen-doc` genererer difor
korrekt aldri ei eiga side for desse typane. Feilen ligg utelukkande i siste
steget av `link_mermaid()`: metoden hentar URL-en ut av den markdown-lenkja
`link()` returnerte og limer på `../` + avsluttande `/` **ukritisk**, utan å
sjekke om verdien alt er ein absolutt URL (`http://`/`https://`). For lokale
element (klassar, enum, slots, lokalt omdefinerte typar) er denne
antakinga korrekt — der er verdien alltid ein relativ filsti. For eksterne
`linkml:types`-typar er ho feil, og øydelegg ein elles gyldig ekstern lenkje.

Denne bugen oppstår i eit **reint** `make gen-doc`-steg, før noko
etterprosessering i dette repoet (`copy_artifacts.sh` o.l.) rører ved
utdataet.

## Workaround

**Implementert 2026-08-13** i `mkdocs/lib/copy_artifacts.sh`
(`copy_schema_artifacts()`), som to sekvensielle `sed`-passeringar over
`click`-hrefane i staden for den tidlegare eine, blindt navnebaserte
regelen frå `25bb4321`:

```bash
# Steg 1: absolutte eksterne URL-ar — fjern feilaktig ../-prefiks og
# avsluttande / (denne bugen), behald resten av URL-en uendra
sed -i -E 's|click ([A-Za-z0-9_]+) href "\.\./(https?://[^"]+)/"|click \1 href "\2"|g'
# Steg 2: attverande hrefar (framleis ../-prefiksa — eksterne URL-ar er det
# ikkje lenger etter steg 1) — bygg om frå navnet, som før (25bb4321)
sed -i -E 's|click ([A-Za-z0-9_]+) href "\.\./[^"]*"|click \1 href "../\L\1\E/"|g'
```

Rekkjefølgja er sjølvavgrensande: steg 1 fjernar `../`-prefikset frå
eksterne URL-ar, så steg 2 sin uendra `\.\./`-føresetnad matchar berre
attverande, genuint lokale hrefar — ingen betinga logikk/gren trengst.
Verifisert både isolert (syntetisk fixture) og direkte mot reelle
`generated/ap-no/cpsv-ap-no` og `generated/samt/samt-bu`: `offentligorganisasjon.md`,
`adresse.md` og `rektor.md` har no `click Uri/Uriorcurie/String href
"http://www.w3.org/2001/XMLSchema#..."` (reine, resolverbare URL-ar, HTTP
2xx/3xx stadfesta direkte mot `w3.org`), medan lokale klasse-/slot-lenkjer
(`../adresse/`, `../langstring/` osv.) er uendra korrekte.

`mkdocs/lib/scripts/check-mermaid-click-hrefs.py` er samstundes oppdatert
til å validere absolutte eksterne hrefar med eit direkte HTTP-oppslag mot
målserveren (`check_external_url()`) i staden for å slå dei opp mot
portalen sin eigen `sitemap.xml` (der dei aldri ville finnast), og
`tests/test_make.sh::test_copy_artifacts_click_href` er utvida med ein
eksplisitt forventingstabell som dekkjer både lokale og eksterne hrefar.

Sjå `specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md`
(steg 3-6) for full implementasjons- og verifiseringslogg.

## Løysing

Upstream-fix i `linkml` sin `docgen.py`, der `link_mermaid()` sjekkar om
`link` alt startar med `http://`/`https://` (t.d. via
`link.startswith(("http://", "https://"))`) og i så fall returnerer han
uendra, i staden for å pakke han inn i `f"../{link}/"`. Ingen GitHub-issue er
identifisert pr. 2026-08-13.

Når upstream-fix er på plass: stadfest at ein fersk `make gen-doc`-køyring
ikkje lenger produserer `../http://`/`../https://`-prefiksa hrefar for
eksterne `linkml:types`-typar, og at intern workaround i
`copy_artifacts.sh` kan forenklast/fjernast tilsvarande. Oppdater denne fila
til `Status: løyst`.
