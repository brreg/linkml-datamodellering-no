# Evaluering: VS Code-plugin for LinkML-modellering

## Bakgrunn

Brukaren ønskjer ei vurdering av om ein eigen VS Code-utviding kan gjere det
enklare å redigere LinkML-skjema i repoet. To konkrete forslag vart nemnde:

1. **Context-aware autocomplete** — foreslå faktiske klasse-/slot-/enum-namn
   (t.d. ved skriving av `range:`, `is_a:`, `mixins:`) i staden for at
   forfattaren må hugse eller søkje dei opp manuelt.
2. **Eit sidepanel** som listar alle tilgjengelege types/slots/enums i den
   aktive modellen, slik at ein slepp å scrolle opp og ned i skjemafila.

Brukaren bad òg om forslag til andre funksjonar som kan forenkle
brukaropplevinga ved LinkML-modellering i dette repoet spesifikt.

**Kvifor dette er eit reelt problem her, ikkje generisk YAML-friksjon:**
Repoet har 47 skjemafiler organisert i eit djupt importhierarki
(jf. [PRINCIPLES.md § 3](../../PRINCIPLES.md#3-modularitet-via-import-hierarki)).
Eit typisk skjema (t.d. `src/linkml/samt/samt-bu/samt-bu-schema.yaml`)
importerer klasser frå andre filer (`../../ap-no/dqv-ap-no/dqv-ap-no-schema`)
og brukar dei som `range:`-verdiar (`Kontaktopplysning`, `Aktoer`,
`RegulativRessurs`) utan at definisjonen finst i same fil. Standard
YAML-støtte i VS Code (Red Hat sin `vscode-yaml` + LinkML sin publiserte
metamodell-JSON-Schema, `https://w3id.org/linkml/meta.schema.json`)
validerer berre at *strukturen* følgjer LinkML-metamodellen (at `range` er
ein streng, at `multivalued` er ein bool) — han har ingen kunnskap om kva
klassar/slots/enums som faktisk er definerte andre stader i akkurat dette
skjemaet sin importgraf. Det er nøyaktig dette gapet brukaren sine to
forslag peiker på, og det ingen generisk YAML-utviding kan tette.

## Research — finst dette alt?

Websøk (sjå kjelder) fann **ingen dedikert LinkML VS Code-utviding eller
language server**, verken i `linkml/linkml`-organisasjonen på GitHub, i VS
Code Marketplace, eller elles. Einaste eksisterande editor-integrasjon er
den generiske YAML-JSON-Schema-oppskrifta over (nemnd i LinkML sin eigen
FAQ), som altså ikkje gjev modell-spesifikk autocomplete eller navigasjon.
Ei eiga utviding for dette repoet ville difor ikkje duplisere eksisterande
verktøy — det er eit reelt, udekt gap i LinkML-økosystemet.

## Vurdering av dei to foreslåtte funksjonane

Begge er **teknisk gjennomførbare utan tung infrastruktur**, fordi kjernebehovet
— "kva klasse-/slot-/enum-namn finst i denne fila og alt ho (transitivt)
importerer" — kan løysast med ein enkel YAML-parser (t.d. `yaml`-npm-pakken)
som følgjer `imports:`-lista rekursivt og les `classes:`/`slots:`/`enums:`/
`types:` frå kvar fil. Dette krev **ikkje** at `linkml`-Python-pakken er
installert eller køyrd — det er reint strukturell YAML-lesing, ikkje ei
semantisk LinkML-kompilering.

| Funksjon | Vurdering |
|---|---|
| Autocomplete for `range:`/`is_a:`/`mixins:`/element i `slots:`-lister | Gjennomførbart som ein `CompletionItemProvider` mot ein indeks bygd av YAML-parseren. Bør òg slå opp linkml-innebygde typar (`string`, `integer`, `uri`, …) og godt kjende eksterne namn (`linkml:types`). |
| Sidepanel med types/slots/enums | Gjennomførbart som ein `TreeDataProvider` (VS Code sitt standard sidepanel-API), gruppert per kategori og kjeldefil (lokal vs. importert), med klikk-til-å-hoppe-til-definisjon. |

**Konklusjon:** begge er verdt å byggje, og heng saman — sidepanelet og
autocomplete kan dele same underliggjande indeks (éin parser, to
presentasjonar), som held implementasjonen DRY internt i extensionen.

## Andre forslag (utover dei to nemnde)

Rangert etter venta nytte for **dette** repoet spesifikt:

1. **Sanntids namnekollisjonsvarsel — direkte respons på eit dokumentert,
   gjentakande problem.** `specs/done/evaluering-gjentakande-monster-backlog.md`
   (mønster P2) syner at "lokalt slot/klasse skuggar eit alt importert namn"
   har ramma repoet **tre gonger uavhengig** (BUG-6, BUG-7, og
   javazone-demo-kollisjonen), og at feilen normalt dukkar først opp djupt
   inne i ein generator med ei kryptisk "Conflicting URIs"-melding. Repoet
   har alt eit script som fangar akkurat dette:
   `src/assets/scripts/makefile/check-import-duplicates.py`, kalla via
   `make check-import-duplicates SCHEMA=<sti>`. Ein VS Code-kommando
   ("Sjekk importkollisjonar") som køyrer dette Makefile-målet ved lagring
   og viser resultatet i Problems-panelet, ville flytte denne
   feilklassen frå "oppdaga ved generator-krasj" til "oppdaga i det
   sekundet du lagrar" — utan å reimplementere sjølve sjekk-logikken
   (DRY, jf. `check-import-duplicates.py` sin eigen grunngjeving for
   kvifor han bruker `SchemaLoader` direkte). Krev podman/`make`, ikkje
   ein rein TS-indeks — sjå arkitekturavsnittet under.
2. **Hover-dokumentasjon** — vis skildring, `range`, `multivalued`,
   `slot_uri`/`class_uri` når musepeikaren står over eit slot-/klassenamn,
   bygd på same indeks som autocomplete/sidepanel.
3. **Go to definition / find references på tvers av filer** (F12/Shift-F12)
   for `range:`-, `is_a:`- og `mixins:`-verdiar — nyttig nettopp fordi
   definisjonen ofte ligg i ei anna fil enn bruksstaden.
4. **Snippets for standardkonstruksjonar** — containerklasse med
   `tree_root: true`, `attributes:`-blokk, silver-nivå-annotasjonar — i tråd
   med reglane i `.claude/rules/linkml-schema.md`, så nye bidragsytarar
   slepp å kopiere frå ei anna fil kvar gong.
5. **Task-integrasjon for eksisterande Makefile-targets** — CodeLens-knapp
   over `id:`-lina eller kommandopalett-oppføringar for
   `make lint SCHEMA=...`, `make validate-instance ...`, `make roundtrip ...`
   og `make mcp-linkml-valider-modell ...`, med output i Problems-panelet.
   Dette er ei rein wrapping av eksisterande targets (jf. CLAUDE.md sitt
   krav om å alltid bruke Makefile-targets), ikkje ny valideringslogikk.
6. **Import-graf-visualisering** — ein enkel Mermaid-graf (webview) som
   viser kva skjema importerer kva, nyttig i eit repo med så djupt
   importhierarki og for å oppdage utilsikta/sirkulære importar.

## Arkitekturval

To tydeleg ulike lag med ulike krav:

**Lag A — strukturell indeksering (autocomplete, sidepanel, hover, go-to-def,
import-graf):** Bør implementerast som **rein TypeScript-kode i sjølve
extensionen**, med ein vanleg YAML-parsar (t.d. `js-yaml`) som følgjer
`imports:` rekursivt og bygger ein indeks over klassar/slots/enums/typar per
fil. Dette krev **ikkje** at `linkml`-pakken er installert lokalt — extensionen
les berre YAML-strukturen. Dette bryt ikkje prinsippet *"Ingen avhengigheiter
skal installerast lokalt"* i CLAUDE.md, sidan det prinsippet gjeld
modelleringsverktøy (linkml, generatorar), ikkje redigeringsverktøy for
IDE-en — men **bygginga** av extensionen (npm install, `vsce package`) bør
likevel køyrast i ein podman-container (t.d. eit `node:22`-basert
Makefile-mål, same mønster som andre containerbygg i repoet), slik at ingen
Node.js-installasjon er nødvendig på vertsmaskina for å byggje/pakke
extensionen.

**Lag B — semantisk validering (namnekollisjon, full lint/policy-sjekk):**
Må gå via eksisterande `make`-targets (`check-import-duplicates`, `lint`,
`validate-instance`, `roundtrip`, `mcp-linkml-valider-modell`) som køyrer
i `linkml-local`-containeren, sidan desse bruker `linkml.utils.schemaloader`
direkte og ikkje kan reimplementerast trygt i TypeScript. Desse
funksjonane bør trigge på lagring eller på eksplisitt kommando — **ikkje**
på kvart tastetrykk, sidan kvart kall startar ein `podman run`.

## Prioritert handlingsliste (dersom brukaren vel å gå vidare)

| # | Steg | Merknad |
|---|---|---|
| 1 | Vel plassering: eige repo (t.d. `vscode-linkml-modellering`) vs. undermappe i dette repoet (t.d. `tools/vscode-linkml/`) | Sjå `## Avgjerder` for tilråding |
| 2 | Prototyp Lag A: YAML-parser + importgraf-oppløysing + `TreeDataProvider`-sidepanel | Kjernefunksjon nr. 2 frå brukaren |
| 3 | Legg til `CompletionItemProvider` for `range:`/`is_a:`/`mixins:`/`slots:`-lister basert på same indeks | Kjernefunksjon nr. 1 frå brukaren |
| 4 | Legg til hover- og definition-provider (punkt 2-3 i «Andre forslag») | Gjenbruk av same indeks |
| 5 | Legg til Task-integrasjon mot `make lint`/`make validate-instance`/`make roundtrip` (punkt 5) | Ren wrapping, ingen ny logikk |
| 6 | Legg til kommando som køyrer `make check-import-duplicates` og viser resultat i Problems-panelet (punkt 1) | Høgast venta nytte — treff eit dokumentert, gjentakande problem |
| 7 | Vurder import-graf-visualisering og snippets (punkt 4 og 6) basert på faktisk bruk av 2-6 | Lågare prioritet, stretch |
| 8 | Bygg/pakke-mål i eigen Makefile-fragment (t.d. `make/xx-vscode-extension.mk`) som køyrer npm/`vsce package` i ein `node:22`-container | Held bygginga podman-basert, jf. arkitekturavsnittet |

## Avgjerder

- **Tilrår undermappe i dette repoet (`tools/vscode-linkml/`) framfor eige
  repo, som utgangspunkt for eit prototypesteg.** Grunngjeving: extensionen
  er tett kopla til dette repoets konkrete konvensjonar (Makefile-targets,
  `.claude/rules/linkml-schema.md`-reglar, importhierarki-struktur) og har
  liten verdi generalisert til eit anna LinkML-repo før han er prøvd ut her.
  Dette er ei tilråding, ikkje eit bindande val — brukaren avgjer endeleg
  plassering før steg 1 i handlingslista vert sett i gang, sidan det
  påverkar repo-struktur og eventuell separat publisering til Marketplace.
- **Skil eksplisitt mellom «Lag A» (rein TS-indeksering, ingen
  linkml-avhengigheit) og «Lag B» (må gå via podman/`make`).** Grunngjeving:
  utan dette skiljet er det freistande å la autocomplete-funksjonen kalle
  `linkml`/`SchemaLoader` direkte for "å vere sikker på at ho stemmer med
  faktisk LinkML-semantikk" — noko som ville krevje anten ein lokalt
  installert Python/linkml-avhengigheit (bryt CLAUDE.md-prinsippet) eller
  ein `podman run` per tastetrykk (uaktuelt responstid-messig). Den reine
  YAML-strukturelle tilnærminga er "god nok" for autocomplete/navigasjon,
  medan semantisk validering (kollisjonar, policy-nivå) framleis skal gå
  via dei containeriserte Makefile-targeta som alt finst.
- **Prioriterte namnekollisjonsvarsel (Lag B, punkt 6) høgast av
  «andre forslag».** Grunngjeving: det er einaste forslaget knytt til eit
  konkret, dokumentert, fleire-gonger-gjentakande produksjonsproblem
  (`evaluering-gjentakande-monster-backlog.md` mønster P2), ikkje ei
  generell DX-forbetring — og løysinga finst alt som eit script, så
  meirarbeidet er avgrensa til UI-integrasjon (ikkje ny logikk).

## Utført

Vurderinga er fullført basert på: (1) websøk etter eksisterande LinkML VS
Code-utvidingar/language server — ingen dedikert verktøy funne, verken i
`linkml/linkml`-organisasjonen eller Marketplace, (2) gjennomgang av LinkML
sin eigen FAQ om editor-støtte (generisk YAML+JSON-Schema-oppskrift via
`w3id.org/linkml/meta.schema.json`, som berre validerer metamodell-struktur,
ikkje modell-spesifikt innhald), (3) inspeksjon av eit representativt
skjema i repoet (`src/linkml/samt/samt-bu/samt-bu-schema.yaml`) for å
stadfeste at cross-file `range:`-referansar via `imports:` er normalen, og
(4) kryssjekk mot `specs/done/evaluering-gjentakande-monster-backlog.md` og
`src/assets/scripts/makefile/check-import-duplicates.py`/
`make check-import-duplicates` for å grunngi det høgast prioriterte
tilleggsforslaget (sanntids namnekollisjonsvarsel) i eit dokumentert,
gjentakande problem. Ingen kodeendringar er gjort i sjølve modelleringa —
dette er ei rein evaluerings-/vurderingsoppgåve, med ei prioritert
handlingsliste klar til bruk dersom brukaren vel å gå vidare med eit
prototypesteg. Ingen ny/endra Claude Code-rule er vurdert nødvendig —
arbeidet avslører ikkje eit konkret, gjentakande åtferdsmønster i denne
økta, berre ei produktvurdering.
