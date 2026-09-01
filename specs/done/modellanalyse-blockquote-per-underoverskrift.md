# Plan: eiga blockquote per underoverskrift i Modellanalyse

## Bakgrunn

Brukaren ønskjer at kvar `###`-underoverskrift under `## Modellanalyse` i
kvar modell sin genererte `index.md` skal få si eiga blockquote (`>`) som
forklarar kva den konkrete analysen avdekkjer og kva konsekvensar funn der
kan ha. I dag finst det berre éi felles blockquote for heile
`## Modellanalyse`-seksjonen (generisk, dekkjer alle ni analysane under
eitt) — ingen av dei ni underoverskriftene har eiga forklarande tekst.

Avklart med brukaren:
- Blockquote-teksten skal vere **statisk per underoverskrift** (éin fast
  tekst per analysetype, lik i alle modellar) — ikkje dynamisk generert
  frå faktiske funn i den enkelte modellen.
- Gjeld **alle** dei ni eksisterande underoverskriftene.

## Kartlegging

`## Modellanalyse`-seksjonen kjem **ikkje** frå ein Jinja2-template i
`src/assets/templates/docgen/` (verifisert: `index.md.jinja2` har ingen
referanse til "Modellanalyse"). Han vert generert av rein Python i
`mkdocs/lib/scripts/generate-modellanalyse-md.py`, `main()`-funksjonen,
frå `REPORTS`-lista (line 53-117). Kvar oppføring i `REPORTS` er ein tuple
`(rapportfil, heading, objekttype, cross_domain_relpath, cross_domain_label)`.

Dei ni underoverskriftene (heading-feltet i `REPORTS`, med line-referanse
til noverande fil):

| Heading | REPORTS-line |
|---|---|
| Isolerte klasser | 55-60 |
| Klasser ikkje kopla til containerklassen | 61-67 |
| Ubrukte slots | 68-74 |
| Ubrukte types | 75-81 |
| Ubrukte enumerations | 82-88 |
| Ubrukte subsets | 89-95 |
| Liknande klassenavn | 96-102 |
| Liknande slotnavn | 103-109 |
| Liknande typenavn | 110-116 |

Overskrifta sjølv vert bygd runtime i løkka (line 174-199): `### {heading}`
(rapport manglar) eller `### {heading} ({count_table_rows(body)})` (rapport
funnen), etterfølgt av rapportkroppen (tabell) eller ei
"*Rapport ikkje tilgjengeleg for denne bygginga.*"-melding.

Eksisterande blockquote-mønster i same fil (line 159-172, den generelle
seksjons-blockquoten) — ei Python-liste med **tom streng før og etter**
`>`-linja, for å sikre blank linje rundt blockquoten (Markdown-krav for
korrekt rendering). Dette mønsteret skal gjenbrukast for kvar
underoverskrift-blockquote. Sidan fila er rein Python (ikkje Jinja2), gjeld
ikkje Jinja2-whitespace-reglane i `.claude/rules/mkdocs-portal.md` direkte —
berre prinsippet om blank linje før/etter `>`-linja.

Fallback-scriptet `mkdocs/lib/sections/modellanalyse.sh` (line 21-25, brukt
når `analyse_dir` manglar heilt) skriv berre den generelle seksjons-
blockquoten og ingen underoverskrifter — treng ingen endring, sidan det
ikkje finst underoverskrifter å knyte blockquotes til i det tilfellet.

## Plan

1. **Utvid `REPORTS`-tuplane** i `generate-modellanalyse-md.py` med eit nytt
   felt, `blockquote_text`, med éi forklarande setning eller to per
   analysetype (kva analysen ser etter + kva konsekvens eit funn kan ha).
   Forslag til tekst (norsk bokmål, jf. modelleringsspråk-konvensjonen):

   - **Isolerte klasser**: "Analysen identifiserer klassar som ikkje har
     nokon strukturell kopling til andre klassar i skjemaet — verken via
     arv eller ved å bli refererte av ein slot. Eit funn kan tyde på ei
     gløymd eller ubrukt klasse, eller ei klasse som manglar ein slot som
     skal kople han til resten av modellen."
   - **Klasser ikkje kopla til containerklassen**: "Analysen sjekkar om
     kvar klasse i skjemaet er nåbar frå containerklassen
     (`tree_root`) via slot-referansar. Ei klasse som ikkje er nåbar dukkar
     ikkje opp i instansar eller JSON-Schema generert frå containerklassen,
     og kan vere daud kode i skjemaet."
   - **Ubrukte slots**: "Analysen finn slots definerte lokalt i skjemaet
     som ingen klasse faktisk brukar. Slike slots aukar
     vedlikehaldsbyrda og kan forvirre lesarar om kva som er i aktiv bruk —
     vurder å fjerne dei eller kople dei til rette klassar."
   - **Ubrukte types**: "Analysen finn types definerte lokalt i skjemaet
     som ingen slot brukar som `range`. Ein ubrukt type er ei daud
     definisjon som bør fjernast eller takast i bruk."
   - **Ubrukte enumerations**: "Analysen finn enumerations definerte
     lokalt i skjemaet som ingen slot brukar som `range`. Ein ubrukt
     enumeration er ei daud definisjon som bør fjernast eller takast i
     bruk."
   - **Ubrukte subsets**: "Analysen finn subsets definerte lokalt i
     skjemaet som ingen klasse eller slot er merkt med. Eit ubrukt subset
     gjev ingen reell gruppering og bør fjernast eller takast i bruk."
   - **Liknande klassenavn**: "Analysen samanliknar klassenamn i dette
     skjemaet mot klassenamn i andre skjema i same domene, og flaggar par
     med høg navnelikskap. Eit funn kan tyde på utilsikta duplisering av
     same omgrep under ulike namn — vurder konsolidering eller import i
     staden for ny lokal definisjon."
   - **Liknande slotnavn**: same resonnement som over, for slotnamn.
   - **Liknande typenavn**: same resonnement som over, for typenamn.

2. **Oppdater bygginga av `lines`** i løkka (noverande line 174-199) slik
   at blockquote-teksten vert sett inn rett under kvar `### {heading}`-linje
   (før rapportkroppen/fallback-meldinga), med tom linje før og etter,
   etter same mønster som den eksisterande seksjons-blockquoten (line
   159-172). Blockquoten skal visast **uavhengig av** om rapportfila vart
   funnen eller ikkje (henne forklarar analysetypen generelt, ikkje det
   konkrete resultatet i denne bygginga).
3. **Oppdater moduldocstringen** til å nemne den nye per-underoverskrift-
   blockquoten kort (éin-to setningar, jf. eksisterande stil i docstringen
   for tidlegare tiltak som `[[modellanalyse-antal-i-deloverskrifter]]`).
4. **Verifiser**:
   - Køyr `generate-modellanalyse-md.py` direkte mot ein reell
     `model-analyse/`-katalog (t.d. for `dcat-ap-no` eller `samt-bu`) —
     stadfest at alle ni underoverskrifter no har eiga blockquote rett
     under seg, med korrekt blank linje før/etter (`>`-syntaks renderer
     rett), både for rapportar med funn, rapportar utan funn, og
     manglande rapportfiler.
   - `make gen-schema-docs SCHEMA=<eit skjema med reelle
     modellanalyse-rapportar>` + `make docs-publish` + `make docs-build`,
     og inspiser generert `index.md` visuelt (`mkdocs serve` eller bygd
     HTML) — stadfest at blockquotene renderer korrekt som blockquotes
     (ikkje som vanleg tekst), og at `validation.links`-sjekken i mkdocs
     framleis er grøn.

## Avklart

- Blockquote-teksten for `Liknande klassenavn`/`-slotnavn`/`-typenavn`
  skal **ikkje** nemne at ei fullstendig cross-domain-analyse finst —
  den eksisterande fotnota (line 194-199) tek seg av "kor finn eg meir"
  uendra. Blockquoten held seg til "kva/kvifor", slik forslaget i steg 1
  over alt gjer.

## Utført

Alle 4 steg gjennomførte i `mkdocs/lib/scripts/generate-modellanalyse-md.py`:

1. Kvar av dei ni oppføringane i `REPORTS` utvida med eit nytt
   `blockquote_text`-felt (statisk forklaringstekst, jf. forslaga i Plan
   over, ordrett brukt). Similar-*-oppføringane nemner ikkje
   cross-domain-motparten (jf. § Avklart).
2. Løkka i `main()` pakkar no ut det nye feltet og set inn
   `f"> {blockquote_text}"` (med tom linje før og etter) rett under kvar
   `### {heading}`/`### {heading} ({count})`-linje, både i
   "rapport funnen"- og "rapport manglar"-sporet.
3. Moduldocstring utvida med eit kort avsnitt om
   per-underoverskrift-blockquoten, med lenkje til denne specen.
4. **Verifisert i to omgangar**:
   - Direkte køyring av scriptet mot eit mellombels testkatalog med tre
     case — ein rapport med funn (`isolerte-klasser`), ein tom rapport
     (`ubrukte-slots`), og ein manglande rapportfil
     (`ikkje-tilkopla-container`). Alle ni underoverskrifter fekk korrekt
     eiga blockquote rett under seg med blank linje før/etter, inkludert
     dei tre similar-*-analysane der blockquoten korrekt ikkje nemner
     cross-domain-sida (fotnota under står uendra).
   - **Full pipeline køyrd** mot `samt-bu` (`generated/samt` var ikkje
     til stades i utgangspunktet, bygd frå botnen): `make
     analyse-similar-domene-batch DOMAIN=samt` + `make
     analyse-lokal-modellanalyse-domene DOMAIN=samt` (skreiv alle ni
     rapportfilene) → `make gen-schema-docs DOMAIN=samt` → `make
     docs-publish` (7 domene publiserte, ingen nye åtvaringar utover
     kjende, urelaterte lenkje-åtvaringar for andre sider) → `make
     docs-build` (161,94 s, bygde utan feil). Inspiserte generert
     `mkdocs/docs/samt/samt-bu/index.md` og bygd
     `mkdocs/site/samt/samt-bu/index.html`: alle ni underoverskrifter
     har eiga `<blockquote><p>...</p></blockquote>` rett under
     `<h3 id="...">`-overskrifta, med eigen ankerlenkje i sidenavigasjonen
     (t.d. `#isolerte-klasser-0`). `validation.links`-sjekken i mkdocs
     framleis grøn for denne sida.

**Avvik frå opphavleg plan:** ingen.
