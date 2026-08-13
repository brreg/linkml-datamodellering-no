# Bug: Mermaid sin `classDiagram` støttar berre eitt `click`-mål per klasseboks

**ID:** BUG-14
**Status:** `open`
**Komponent:** `mermaid` (`classDiagram`-syntaks)
**Oppdaga:** 2026-08-12

## Symptom

I genererte klasse-/slot-sider (`mkdocs/docs/**/klasser/*.md`) sitt mermaid
`classDiagram` er kvar klasse rendra som éin boks med klassenamnet øvst og
kvar eigenskap (slot) som ei medlemsrad under, t.d. for `Adresse`:

```
class Adresse
click Adresse href "../adresse/"
  Adresse : full_adresse
  Adresse : id
  Adresse : land
  Adresse : postnummer
  Adresse : poststad
```

Eit klikk på **kva som helst** inni boksen — tittelen `Adresse` eller ei av
medlemsradene `full_adresse`, `id`, `land`, `postnummer`, `poststad` — utløyser
**same** `href` (`../adresse/`), sjølv om visuelt kvar medlemsrad ser ut som
ho skulle vore individuelt klikkbar til si eiga side (t.d.
`full_adresse.md`). `## Eigenskapar`-tabellen lenger nede på same side
lenkjer derimot korrekt til kvar enkelt slot-side.

Gjeld systematisk for **alle** klassar med minst éin attributt i heile
portalen, ikkje berre `Adresse` — verifisert også for `Rektor`
(`mkdocs/docs/samt/samt-bu/klasser/rektor.md`). Sjå
`specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md`
("Problem B") for full utleiing.

## Berørte skjema

Alle skjema/klassar med minst éin attributt i det genererte mermaid
`classDiagram`-et — i praksis alle domenemodellar i repoet.

## Rot-årsak

Mermaid sin `classDiagram`-syntaks har **ingen** eigen `click`-mekanisme for
enkelte medlemsrader — kun eitt `click <Klassenamn> href "..."`-direktiv per
klasseboks, som gjeld heile boksen (tittel + medlemsliste) samla. Dette er
ei grunnleggjande avgrensing i sjølve Mermaid-syntaksen, ikkje noko
LinkML sin `gen-doc` eller dette repoet sin `copy_artifacts.sh` kan
kompensere for ved å endre `href`-verdien — det finst rett og slett ingen
per-rad-target å peike han til.

Dette er difor **ikkje** ein regresjon i `copy_artifacts.sh` eller i LinkML
sin `gen-doc`, og kan ikkje løysast med same slags href-korrigering som
BUG-13.

## Workaround

Ingen intern mitigering er valt eller implementert enno. Alternativ under
vurdering (jf.
`specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md`,
steg 8):

- **(a) Aksepter avgrensinga** — legg til ei kort forklarande linje ved
  diagramma (eller i `mkdocs/docs/index.md` sine "Kjende avgrensingar") om
  at `## Eigenskapar`-tabellen under diagrammet er fasiten for
  slot-spesifikke lenkjer.
- **(b) Fjern det misvisande visuelle inntrykket** — generer diagram utan
  attributt-rader inni klasseboksen (kun klassenamn + relasjonspiler til
  andre klassar/typar).
- **(c) Anna diagramtype/verktøy** som støttar per-medlem-click, t.d.
  PlantUML (som repoet alt genererer parallelt via `make gen-plantuml`) —
  vurder om PlantUML-diagrammet kan promoterast som primærdiagram i staden
  for mermaid.

Denne fila sin `Workaround`-seksjon vert oppdatert når eit alternativ er
vald og implementert.

## Løysing

Ingen kjend permanent løysing — dette er ei arkitektonisk avgrensing i
Mermaid sin `classDiagram`-syntaks, ikkje ein bug som kan fiksast oppstraums
med mindre Mermaid sjølv legg til støtte for per-medlem-click. Ingen
GitHub-issue er identifisert pr. 2026-08-13. Denne bugen vert truleg
verande `open`/`upstream` permanent, med intern mitigering (jf.
`Workaround` over) som einaste realistiske tiltak.
