# Plan: vis funntal i parentes på alle Modellanalyse-underoverskrifter

## Bakgrunn

Brukaren ønskjer at alle `###`-underoverskriftene under `## Modellanalyse`
i kvar modell sin genererte `index.md` (dei tre `Liknande <x>namn (same
domene)`-analysane og dei fem nye `Ubrukte lokale <x>`/`Isolerte
klassar`-analysane frå
[[modellanalyse-ubrukte-lokale-definisjonar]]) viser eit **funntal i
parentes**, etter same mønster som `### Slots (13)`, `### Types (2)` osv.
lenger oppe på same side. I dag manglar alle åtte Modellanalyse-
underoverskriftene tal heilt, sjølv om kvar rapport allereie inneheld
akkurat den informasjonen (anten som tal rader i rapporten sin tabell,
eller i den avsluttande "**Totalt: N ...**"-linja).

## Kartlegging

Underoverskriftene vert bygde i
`mkdocs/lib/scripts/generate-modellanalyse-md.py`, `main()`-funksjonen
(line 145-166 i noverande versjon): for kvar oppføring i `REPORTS`
skriv scriptet `### {heading}` **før** det i det heile har lese
rapportfila, og limer så inn rapportkroppen (eller ei
"ikkje tilgjengeleg"-melding) uendra under. Talet finst ikkje som eit eige
felt nokon stad — det må utleiast frå sjølve rapportteksten.

**Rapportformatet er einsarta nok til at talet kan utleiast generisk,
utan å endre sjølve analyse-skripta** (`find-similar-names.py`,
`find-unused-local-definitions.py`): kvar rapport har anten
- eitt markdown-tabell med nøyaktig éi headerrad + éi
  `|---|---|...|`-skiljerad, der kvar attverande `|`-rad er eitt funn
  (eitt par for similar-*, eitt element for ubrukte-*/isolerte-klasser), eller
- ingen tabell i det heile, berre ei "Ingen ... funne (N sjekka)."-linje
  når det ikkje er noko å rapportere.

Funntalet er dermed **talet på `|`-linjer i rapportkroppen, minus dei to
faste header-/skiljelinjene** (0 når rapporten ikkje har nokon tabell).
Dette er robust for alle åtte rapporttypane utan å måtte parse den
menneskelesbare "Totalt: ..."-linja (som har ulik ordlyd per rapporttype)
eller innføre eit strukturert utdataformat i analyse-skripta.

**Manglande/uleseleg rapportfil** (det eksisterande
"*Rapport ikkje tilgjengeleg for denne bygginga.*"-fallback-sporet, line
149-158) har ikkje noko meiningsfullt tal å vise — her skal overskrifta
halde fram **utan** parentes, ikkje vise `(0)` (som ville sett ut som eit
stadfesta "ingen funn"-resultat, ikkje eit "vi veit ikkje"-resultat).

## Plan

1. **Ny hjelpefunksjon** `count_table_rows(body: str) -> int` i
   `generate-modellanalyse-md.py`: tel linjer i `body` som (etter
   `.strip()`) startar med `|`; returner `0` viss færre enn 2 slike linjer
   finst (ingen tabell), elles `len(pipe_lines) - 2` (trekk frå header- og
   skiljerad).
2. **Omstrukturer løkka i `main()`** (line 145-166) slik at rapportfila
   vert lesen **før** overskrifta skrivast, ikkje etter:
   - Fil funnen og lesen OK: `count = count_table_rows(body)`,
     overskrift vert `### {heading} ({count})`
   - Fil manglar eller kan ikkje lesast: overskrift vert uendra
     `### {heading}` (ingen parentes) — behald eksisterande
     ÅTVARING-logikk og fallback-teksten uendra
3. **Oppdater moduldocstringen** til å nemne funntal-utleiinga (kort — sjå
   Kartlegging over for grunngjevinga, ikkje dupliser heile resonnementet
   i koden).
4. **Verifiser**:
   - Køyr `generate-modellanalyse-md.py` direkte mot ein
     `model-analyse/`-katalog med minst éin rapport med funn og minst éin
     tom rapport ("Ingen ... funne") — stadfest at overskriftene viser
     korrekt tal i begge tilfelle
   - Køyr mot ein katalog der éin rapportfil manglar — stadfest at
     akkurat den overskrifta ikkje får parentes, medan dei andre gjer det
   - `make gen-schema-docs SCHEMA=<eit skjema med reelle
     modellanalyse-rapportar>` + `make docs-publish` + `make docs-build`,
     og inspiser generert `index.md`: alle åtte Modellanalyse-
     underoverskriftene viser tal i parentes, `validation.links`-sjekken
     i mkdocs framleis grøn

## Opne spørsmål (avklar ved implementering, ikkje i denne specen)

- Skal talet for similar-*-rapportane vise talet på **par** (dagens
  "Totalt: N par funne") eller talet på **unike klasse-/slot-/typenamn**
  involvert i minst eitt par? Kartlegginga over legg til grunn "talet på
  par" (= talet på tabellrader), som er den enklaste og mest
  konsistente tolkinga på tvers av alle åtte rapporttypane, og også det
  som talet i "Totalt: N par funne"-linja alt uttrykker.

## Utført

Alle 4 steg gjennomførte i `mkdocs/lib/scripts/generate-modellanalyse-md.py`:

1. Ny `count_table_rows(body)`-hjelpefunksjon — tel `|`-tabellrader,
   trekk frå header-/skiljerad, `0` når ingen tabell finst.
2. Løkka i `main()` omstrukturert: rapportfila vert no lesen (eller
   feilhandtert) **før** overskrifta vert bygd, slik at talet er
   tilgjengeleg når overskrifta skrivast. Manglande/uleseleg rapport gjev
   framleis overskrift **utan** parentes (ikkje `(0)`).
3. Moduldocstring utvida med eit kort avsnitt om funntal-utleiinga.
4. **Verifisert reelt** (sandbox deaktivert for podman, same grunn som
   forrige spec):
   - Direkte køyring av scriptet mot `generated/samt/samt-bu/model-
     analyse/` (alle fem nye rapportar til stades, tomme) — dei tre
     similar-*-rapportane (manglar i dette test-datasettet) fekk korrekt
     **ingen** parentes, dei fem ubrukt-/isolert-rapportane viste
     korrekt `(0)`
   - Bygde eit mellombels testkatalog med reelle
     `analyse-ubrukte-slots`/`-enums`/`analyse-isolerte-klasser`-
     rapportar for `common-ap-no-schema.yaml` — overskriftene viste
     korrekt `(18)`, `(7)`, `(2)` (matchar dei same funna verifisert i
     [[modellanalyse-ubrukte-lokale-definisjonar]]), og dei to
     ikkje-genererte rapporttypane fekk korrekt ingen parentes
   - `make docs-publish` + `make docs-build` køyrd fullt ut: generert
     `index.md` for `samt-bu` og `dcat-ap-no` viser korrekte funntal
     (t.d. `dcat-ap-no` sin "Ubrukte lokale slots (2)", som matchar dei
     to reelt ubrukte slotta stadfesta tidlegare). `docs-build` sin
     `validation.links`-sjekk framleis grøn, ingen nye åtvaringar.

**Avvik frå opphavleg plan:** ingen.
