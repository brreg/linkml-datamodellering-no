# Bug: Mermaid sin `classDiagram` støttar berre eitt `click`-mål per klasseboks

**ID:** BUG-14
**Status:** `open`
**Komponent:** `mermaid` (`classDiagram`-syntaks)
**Oppdaga:** 2026-08-12

## Symptom

I genererte klasse-/slot-sider (`mkdocs/docs/**/klasser/*.md`) sitt mermaid
`classDiagram` er kvar klasse rendra som éin boks med klassenavnet øvst og
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
enkelte medlemsrader — kun eitt `click <Klassenavn> href "..."`-direktiv per
klasseboks, som gjeld heile boksen (tittel + medlemsliste) samla. Dette er
ei grunnleggjande avgrensing i sjølve Mermaid-syntaksen, ikkje noko
LinkML sin `gen-doc` eller dette repoet sin `copy_artifacts.sh` kan
kompensere for ved å endre `href`-verdien — det finst rett og slett ingen
per-rad-target å peike han til.

Dette er difor **ikkje** ein regresjon i `copy_artifacts.sh` eller i LinkML
sin `gen-doc`, og kan ikkje løysast med same slags href-korrigering som
BUG-13.

## Workaround

**Avklart med brukaren 2026-08-13: alternativ (a) — aksepter som kjend
avgrensing.** Ingen kodeendring for å fjerne eller omgå sjølve
click-avgrensinga (jf. dei to forkasta alternativa under). Grunngjeving:
dette er ei arkitektonisk avgrensing i Mermaid sjølv, ikkje ein feil i
dette repoet sin kode, og `## Eigenskapar`-tabellen lenger nede på same
side gir allereie korrekte slot-spesifikke lenkjer — brukarar har eit
fungerande alternativ rett under diagrammet. Kostnaden ved (b)/(c) står
ikkje i forhold til eit rent visuelt/UX-problem med eit fungerande
arbeidsrundt alt til stades på sida.

**Implementert 2026-08-13** i
`src/assets/templates/docgen/class_diagram.md.jinja2`: ei
`!!! note "Om diagrammet"`-admonition (mkdocs-material admonition-syntaks)
vert no generert rett etter mermaid-diagrammet, guarda på
`schemaview.class_induced_slots(element.name)|length > 0` slik at han berre
vises for klassar som faktisk har attributt-rader i eiga diagramboks (der
tvitydigheita finst). Teksten viser til denne bugen og peikar til
`## Eigenskapar`-tabellen som fasit for slot-spesifikke lenkjer.

Verifisert med fersk `make gen-docs` (`cpsv-ap-no`, `samt-bu`),
`copy_artifacts.sh`-kopiering og full `make docs-build`: notatet rendrar
korrekt som `<div class="admonition note">` i den bygde HTML-utdataen for
`offentligorganisasjon.md` og `rektor.md`, utan feil eller åtvaringar.

Sjå `specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md`,
steg 9, for full detalj.

Forkasta alternativ:

- ~~(b) Fjern det misvisande visuelle inntrykket~~ — ville kravd endring av
  `gen-doc`-malen eller eit eige post-prosesseringssteg for å fjerne
  attributt-rader frå klasseboksen, ei større endring for eit reint
  kosmetisk/UX-problem.
- ~~(c) Anna diagramtype/verktøy (PlantUML)~~ — ville kravd å promotere
  PlantUML til primærdiagram i staden for mermaid portalomfattande, langt
  utanfor omfanget til denne bugen.

## Løysing

Ingen kjend permanent løysing — dette er ei arkitektonisk avgrensing i
Mermaid sin `classDiagram`-syntaks, ikkje ein bug som kan fiksast oppstraums
med mindre Mermaid sjølv legg til støtte for per-medlem-click. Ingen
GitHub-issue er identifisert pr. 2026-08-13. Denne bugen vert truleg
verande `open`/`upstream` permanent, med intern mitigering (jf.
`Workaround` over) som einaste realistiske tiltak.
