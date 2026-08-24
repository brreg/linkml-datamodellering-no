# Fast rekkjefølge og 0-funn-filtrering i Modellanalyse-seksjonen

## Bakgrunn

`mkdocs/lib/scripts/generate-modellanalyse-md.py` genererer `## Modellanalyse`-
seksjonen i kvar modell sin `index.md`, ut frå ei fast `REPORTS`-liste
(linje 52–109) som avgjer rekkjefølga deloverskriftene vert skrivne i. Alle
åtte deloverskrifter vert i dag **alltid** skrivne (`main()`, linje 164–190),
sjølv når rapporten har 0 funn — det finst inga skjul-logikk.

Brukaren ønskjer:

1. Fast rekkjefølge på deloverskriftene: Isolerte klassar → Ubrukte slots →
   Ubrukte types → Ubrukte enumerations → Ubrukte subsets → Liknande
   klassenavn → Liknande slotnavn → Liknande typenavn.
2. Berre vis deloverskrifter med **meir enn 0 funn**.
3. Dersom **alle** modellanalysane har 0 funn: ikkje vis nokon
   deloverskrifter i det heile — skriv i staden eit lite avsnitt under
   `## Modellanalyse` som listar opp kva testar som er køyrde og
   konkluderer med 0 funn totalt.
4. Fjern ordet "lokale" frå fire av overskriftene: "Ubrukte lokale slots" →
   "Ubrukte slots", "Ubrukte lokale enumerations" → "Ubrukte enumerations",
   "Ubrukte lokale types" → "Ubrukte types", "Ubrukte lokale subsets" →
   "Ubrukte subsets".
5. Fjern teksten "(same domene)" frå dei tre "Liknande ...navn (same
   domene)"-overskriftene: "Liknande klassenavn (same domene)" → "Liknande
   klassenavn", "Liknande slotnavn (same domene)" → "Liknande slotnavn",
   "Liknande typenavn (same domene)" → "Liknande typenavn".

**Todelt utføring (brukarønskt rekkjefølge):** Punkt 1+4 (rekkjefølge og
overskriftstekst — reint tuple-innhald i `REPORTS`-lista) skal utførast og
committast **først**, som Fase 1. Brukaren verifiserer resultatet (t.d.
via lokal `mkdocs serve`/genereringskøyring) **før** Fase 2 (punkt 2+3 —
to-pass filtrerings- og alt-0-funn-logikken i `main()`) vert starta. Dei to
fasene skal difor handterast som separate arbeidsøkter/commits, ikkje éin
samla endring — sjå `## Steg` under for fase-inndelinga.

**Presisering frå research (viktig, endrar omfang):** "Liknande typenavn
(same domene)" (basert på `make analyse-similar-types-domain`) finst
**allereie** i `REPORTS`-lista (linje 67–73, posisjon 3 i dagens
rekkjefølge) — dette er altså ikkje ei ny deloverskrift som må leggjast
til, berre flyttast til rett plass i rekkjefølga. Ingen ny rapport-
integrasjon er naudsynt.

**Heading-tekst for "Isolerte klassar" haldast uendra:** eksisterande
overskrift er "Isolerte klassar" (nynorsk pluralform), ikkje "Isolerte
klasser" som i brukaren sin uformelle omtale. Sidan `mkdocs/docs/`-innhald
er dokumentasjonsdomenet og skal følgje nynorsk (jf. CLAUDE.md §
Skriftspråk), beheld vi denne skrivemåten uendra.

**Fire overskrifter mistar ordet "lokale":** "Ubrukte lokale slots",
"Ubrukte lokale enumerations", "Ubrukte lokale types" og "Ubrukte lokale
subsets" vert korta til "Ubrukte slots", "Ubrukte enumerations", "Ubrukte
types" og "Ubrukte subsets". Dette er ei eksplisitt brukarønskt
tekstendring, ikkje ei nynorsk/bokmål-retting — dei fire tilhøyrande
rapportfilnamna (`ubrukte-slots-report.md` m.fl.) og `objekttype`-verdiane
brukt i eventuelle framtidige fotnotetekstar er uendra, berre `heading`-
strengen i kvar `REPORTS`-tuple.

**Tre overskrifter mistar teksten "(same domene)":** "Liknande klassenavn
(same domene)", "Liknande slotnavn (same domene)" og "Liknande typenavn
(same domene)" vert korta til "Liknande klassenavn", "Liknande slotnavn"
og "Liknande typenavn". Berre `heading`-strengen i dei tre `similar-*-
domain-report.md`-tuplene vert endra — `objekttype`-verdien (brukt i
cross-domain-fotnoteteksten "*For fullstendig analyse av klassenavn på
tvers av domene sjå ...*") inneheld alt ikkje teksten "(same domene)" og
er uendra. Sjølve rapportfilnamna og cross-domain-sti/-lenkjetekst er
òg uendra.

**Talet på funn (`count_table_rows()`, linje 126–133)** er allereie ein
generisk tabellrad-teljar som fungerer identisk for alle åtte rapporttypar
(returnerer 0 når rapporten ikkje har nokon tabell, t.d.
"Ingen liknande klassenavn funne (12 sjekka).", eller berre header+
skiljerad). Denne kan gjenbrukast direkte for filtreringslogikken —
ingen endring naudsynt i sjølve teljefunksjonen.

**Manglande rapportfil (`body is None`, t.d. byggfeil) skal framleis
alltid visast** — dette er ikkje det same som eit stadfesta 0-funn (jf.
moduldocstring linje 39–41: "ikkje '(0)', som ville sett ut som eit
stadfesta nullfunn"). Filtrering på ">0 funn" gjeld difor berre rapportar
som faktisk vart lesne og har `count_table_rows(body) == 0` — ikkje
manglande rapportar. Konsekvens: "alle modellanalysar har 0 funn"-tilstanden
(punkt 3) inntreff berre når **alle åtte** rapportfiler vart funne og lesne,
og **alle** returnerer count 0. Dersom éin rapport manglar, vert han vist
som i dag ("*Rapport ikkje tilgjengeleg for denne bygginga.*"), og resten
filtrerast normalt (0-funn skjult, >0-funn vist) — sjølv om det då kan
hende at ingen deloverskrifter vert viste utanom den manglande.

**Eksisterande intro-avsnitt** (den generelle "> Modellanalysen
samanliknar..."-blokkquoten, linje 156–161) skal **framleis visast** i
begge tilfelle (også ved alt-0-funn) — det nye samandraget frå punkt 3 kjem
**i tillegg**, ikkje i staden for, sidan intro-teksten forklarer kva
analysen generelt gjer, medan samandraget konkret listar dei åtte
testnamna og konkluderer med totaltalet.

## Verifiseringsgrunnlag (lokalt tilgjengeleg, ingen ny `make`-køyring naudsynt)

- `generated/samt/samt-bu/model-analyse/` — alle åtte rapportar finst, alle
  har 0 funn. Brukast til å verifisere alt-0-funn-samandraget (punkt 3).
- `generated/ap-no/dcat-ap-no/model-analyse/` — `ubrukte-slots-report.md`
  har 2 reelle funn (4 `|`-linjer = header+skiljerad+2 rader), resten 0.
  Brukast til å verifisere at berre "Ubrukte lokale slots" vert vist (dei
  andre skjult), i rett posisjon i rekkjefølga (punkt 1–2).

## Steg

### Fase 1 — rekkjefølge og overskriftstekst (utførast og verifiserast av brukar først)

1. I `mkdocs/lib/scripts/generate-modellanalyse-md.py`: omorganiser
   rekkjefølga på dei åtte tuple-oppføringane i `REPORTS`-lista
   (linje 52–109) til: `isolerte-klasser-report.md`,
   `ubrukte-slots-report.md`, `ubrukte-types-report.md`,
   `ubrukte-enums-report.md`, `ubrukte-subsets-report.md`,
   `similar-classes-domain-report.md`, `similar-slots-domain-report.md`,
   `similar-types-domain-report.md`. Samstundes: rett `heading`-strengen i
   dei fire "ubrukte lokale"-oppføringane frå "Ubrukte lokale slots" →
   "Ubrukte slots", "Ubrukte lokale enumerations" → "Ubrukte
   enumerations", "Ubrukte lokale types" → "Ubrukte types", "Ubrukte
   lokale subsets" → "Ubrukte subsets". Resten av tuple-innhaldet
   (rapportfilnamn, objekttype, cross-domain-sti/-tekst) og overskrifta
   "Isolerte klassar" er uendra. Filtrerings-/alt-0-funn-logikken i
   `main()` (Fase 2) er **ikkje** ein del av dette steget.

2. I same `REPORTS`-liste: rett `heading`-strengen i dei tre `similar-*-
   domain-report.md`-oppføringane frå "Liknande klassenavn (same
   domene)" → "Liknande klassenavn", "Liknande slotnavn (same domene)" →
   "Liknande slotnavn", "Liknande typenavn (same domene)" → "Liknande
   typenavn". `objekttype`-verdien og cross-domain-sti/-lenkjetekst i
   same tuple er uendra.

3. Verifiser med `python3 mkdocs/lib/scripts/generate-modellanalyse-md.py
   generated/ap-no/dcat-ap-no/model-analyse ap-no dcat-ap-no` (direkte,
   utan `make`/podman) — forvent: alle åtte deloverskrifter framleis
   viste (ingen filtrering enno), no i ny rekkjefølge, med dei fire
   "Ubrukte ..."-overskriftene utan "lokale".

4. Verifiser med `python3 mkdocs/lib/scripts/generate-modellanalyse-md.py
   generated/samt/samt-bu/model-analyse samt samt-bu` (denne katalogen har
   alle tre `similar-*-domain-report.md`-filene, i motsetnad til
   dcat-ap-no) — forvent: dei tre "Liknande ..."-overskriftene vist utan
   "(same domene)".

5. **Stopp her.** Legg fram diff + verifiseringsutdrag for brukaren og
   vent på eksplisitt godkjenning før Fase 2 startast.

### Fase 2 — filtrering på >0 funn og alt-0-funn-samandrag (startast berre etter godkjenning av Fase 1)

4. I `main()` (linje 136–200): byt ut den direkte skriv-medan-du-itererer-
   løkka (linje 164–190) med ein to-pass-struktur:
   - **Pass 1:** for kvar oppføring i `REPORTS`, les rapportfila (som i
     dag) og bygg ei liste med `(heading, count, body, cross_domain_relpath,
     cross_domain_label, objekttype)` — `count` er `None` når `body is
     None` (manglande/uleseleg fil), elles `count_table_rows(body)`.
   - Rekn ut `all_zero`: sann berre når **alle** oppføringar har
     `count == 0` (dvs. ingen `None`-verdiar og ingen `count > 0`).
   - **Pass 2:**
     - Dersom `all_zero`: ikkje skriv nokon `###`-deloverskrifter. Skriv i
       staden eitt kort avsnitt under intro-blokkquoten som listar opp dei
       åtte overskriftstekstane (kommaseparert eller punktliste) og
       konkluderer med at alle er køyrde og har funne 0 avvik totalt.
       Nynorsk, kort (2–4 setningar).
     - Elles: iterer oppføringane i rekkjefølge. Hopp over oppføringar med
       `count == 0`. For `count is None` (manglande rapport): behald
       eksisterande fallback-tekst ("*Rapport ikkje tilgjengeleg for denne
       bygginga.*") utan parentestal. For `count > 0`: behald eksisterande
       `### {heading} ({count})` + rapportkropp + eventuell
       cross-domain-fotnote, uendra format.
   - Slutt-fotnota om IRI-dereferering (linje 191–195) og
     "ÅTVARING: ingen modellanalyse-rapportar funne"-sjekken (linje
     197–198) er uendra i begge grenene.

5. Verifiser med `python3 mkdocs/lib/scripts/generate-modellanalyse-md.py
   generated/samt/samt-bu/model-analyse samt samt-bu` (direkte, utan
   `make`/podman) — forvent: ingen `###`-deloverskrifter, berre intro +
   nytt samandragsavsnitt med 0-funn-konklusjon.

6. Verifiser med `python3 mkdocs/lib/scripts/generate-modellanalyse-md.py
   generated/ap-no/dcat-ap-no/model-analyse ap-no dcat-ap-no` — forvent:
   kun `### Ubrukte slots (2)` vist (dei sju andre skjult sidan dei har 0
   funn), plassert på rett stad i den nye rekkjefølga.

7. Full pipeline-verifisering (valfritt, krev podman utanfor sandkasse):
   `make docs-publish` for eitt domene og inspiser generert `index.md`
   manuelt for å stadfeste at `modellanalyse.sh` sitt kall til scriptet
   framleis fungerer uendra.

8. Ingen eksisterande testar dekkjer denne pipelinen (verifisert i tidlegare
   research — ingen treff i `tests/` på `generate-modellanalyse-md` eller
   `Modellanalyse`), så ingen testoppdatering er naudsynt.

## Handlingsliste

**Fase 1 (utført, ventar på brukargodkjenning):**
- [x] Omorganiser `REPORTS`-lista til ny rekkjefølge
- [x] Fjern "lokale" frå dei fire "Ubrukte lokale ..."-overskriftene
- [x] Fjern "(same domene)" frå dei tre "Liknande ...navn (same
      domene)"-overskriftene
- [x] Verifiser mot `generated/ap-no/dcat-ap-no/model-analyse` (rekkjefølge
      + overskriftstekst, ingen filtrering enno) — bekrefta rett
      rekkjefølge og overskriftstekst, eksisterande manglande-rapport-
      fallback uendra (dei tre "Liknande ..."-rapportane finst ikkje for
      dette domenet, viser som før "Rapport ikkje tilgjengeleg")
- [x] Verifiser mot `generated/samt/samt-bu/model-analyse` (alle åtte
      rapportar finst, inkl. alle tre `similar-*-domain-report.md`) —
      bekrefta rett rekkjefølge og overskriftstekst for alle åtte
      (inkl. "(same domene)" fjerna), funntal i parentes uendra
- [x] Legg fram for brukar og vent på godkjenning før Fase 2 — brukar
      godkjente Fase 1-resultatet og valde å **ikkje** gå vidare med Fase 2

**Fase 2 — droppa etter brukarønske, ikkje utført:**
- [ ] ~~Innfør to-pass-struktur i `main()`: bygg `(heading, count, body,
      ...)`-liste, rekn ut `all_zero`, filtrer/skriv i pass 2~~
- [ ] ~~Skriv nytt samandragsavsnitt for alt-0-funn-tilfellet (nynorsk)~~
- [ ] ~~Verifiser mot `generated/samt/samt-bu/model-analyse`
      (alt-0-funn-sti)~~
- [ ] ~~Verifiser mot `generated/ap-no/dcat-ap-no/model-analyse`
      (filtrering + rekkjefølge med eitt reelt funn)~~

## Utført

Kun **Fase 1** vart utført. Brukaren stadfesta at Modellanalyse-
seksjonen skal stå slik han vart etter Fase 1 — punkt 2 (skjul
deloverskrifter med 0 funn) og punkt 3 (alt-0-funn-samandrag) i
"Brukaren ønskjer" over vart **ikkje** realisert og er ikkje planlagt
vidare.

Endringar i `mkdocs/lib/scripts/generate-modellanalyse-md.py`
(`REPORTS`-lista, linje 52–109):
- Ny rekkjefølge: Isolerte klassar → Ubrukte slots → Ubrukte types →
  Ubrukte enumerations → Ubrukte subsets → Liknande klassenavn →
  Liknande slotnavn → Liknande typenavn
- "Ubrukte lokale X" → "Ubrukte X" (fire overskrifter)
- "Liknande X (same domene)" → "Liknande X" (tre overskrifter)
- Alle åtte deloverskrifter vert framleis alltid viste, uavhengig av
  funntal — filtreringslogikk (Fase 2) vart ikkje innført

Verifisert med direkte scriptkøyring (`python3
generate-modellanalyse-md.py <dir> <domain> <schema>`, utan
`make`/podman) mot `generated/ap-no/dcat-ap-no/model-analyse` (eitt
reelt funn i Ubrukte slots, tre "Liknande ..."-rapportar manglar) og
`generated/samt/samt-bu/model-analyse` (alle åtte rapportar finst, alle
0 funn) — rett rekkjefølge og overskriftstekst i begge, eksisterande
funntal-i-parentes og manglande-rapport-fallback uendra.

Ingen testar måtte oppdaterast (ingen eksisterande test dekkjer denne
pipelinen).
