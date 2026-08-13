# Bug: LinkML sin `DocGenerator.link_mermaid()` limer `../` framanfor absolutte eksterne URL-ar

**ID:** BUG-13
**Status:** `open`
**Komponent:** `linkml` (`linkml/generators/docgen.py`, `DocGenerator.link_mermaid()`)
**Oppdaga:** 2026-08-13

## Symptom

I genererte klasse-/slot-sider (`mkdocs/docs/**/klasser/*.md`) sitt mermaid
`classDiagram` peikar `click <Typenamn> href "..."`-direktiv for elementære
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

Alle skjema som brukar minst éin elementær `linkml:types`-type (`string`,
`uri`, `uriorcurie`, truleg `integer`/`boolean`/`float`/`date` også) på ein
slot **utan** at typen er lokalt omdefinert i skjemaet sin eigen
`types:`-blokk — stadfesta for `ap-no/cpsv-ap-no`, `samt/samt-bu` og
`oreg/enhetsregisteret-bvrinn`, men rotårsaka er generisk i `gen-doc` og
gjeld truleg praktisk talt alle domenemodellar i repoet.

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

Ingen fullverdig workaround er på plass enno. `mkdocs/lib/copy_artifacts.sh`
sin href-ombygging (`25bb4321`, opphavleg innført for eit anna,
ikkje-relatert problem — sjå
`specs/done/mermaid-klikkbare-lenker-404.md`) rettar riktignok den
**syntaktiske** feilen (fjernar `../http://...`-forma), men gjer det ved å
kaste bort den eksterne URL-en heilt og byggje ei ny, lokal
`../<lowercase-typenamn>/`-lenkje frå click-namnet — som **alltid** 404-ar,
sidan `gen-doc` (korrekt, jf. rot-årsak over) aldri genererer ei lokal side
for desse typane. Nettoresultatet er framleis ei broten lenkje, berre av ein
annan art (semantisk umogleg lokal 404 i staden for syntaktisk ugyldig
ekstern URL).

Ein reell workaround (plan i
`specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md`, steg
3-4) må skilje på om den opphavlege href-verdien er ein absolutt URL eller
ein lokal sti, og for absolutte URL-ar berre fjerne det feilaktige
`../`-prefikset — ikkje rebygge lenkja frå click-namnet. Denne fila sin
"Workaround"-seksjon vert oppdatert når fiksen er implementert, og
`Status` endra til `upstream`.

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
