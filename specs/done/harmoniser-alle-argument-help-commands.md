# Plan: Harmoniser alle argument-plasshaldarar i `make help`/`COMMANDS.md`

## Bakgrunn

Oppfølging av dei føregåande argument-harmoniseringane denne økta
([[argumentnavn-avvik-revisjon]], [[namn-navn-konsistens-make-help]] m.fl.).
Brukaren peika ut eit «riktig mønster» — `DOMAIN=<domene>` — og bad om ein
full gjennomgang av **alle** argument i `help.sh` (dvs. kjeldekommentarane
i `make/*.mk` som `help.sh` renderer) og `COMMANDS.md`, samt ei evaluering
av om `NAME` bør bytast til `SCHEMA` der argumentet gjeld eit
LinkML-modellnamn.

## Full kartlegging

Talet på førekomstar per argument-plasshaldar, henta med
`grep -ohE '[A-Z][A-Z_]*=<[^>]*>' make/*.mk Makefile COMMANDS.md`
(reint interne make-variablar som `PYTHONWARNINGS`, `TEST_FILTER`,
`LOGLVL` og konkrete eksempelverdiar som `SCHEMA=src/linkml/...` er
utelatne — dei er ikkje generiske plasshaldarar):

| Argument | `make help`-kjelde (`make/*.mk`) | `COMMANDS.md` | Status |
|---|---|---|---|
| `DOMAIN` | `<domain>` × 26, `<domene>` × 4 | `<domain>` × 9 | **Brotet mønster** — engelsk dominerer (26+9=35), berre dei 4 nyleg retta `new-modell`/`remove-modell`-førekomstane brukar korrekt `<domene>` |
| `SCHEMA` | `<sti>` × 32, `<sti-til-skjema>` × 1 | `<sti>` × 14 | Nesten konsistent — éin outlier (`mcp-linkml-valider-modell` sin `log_error`) |
| `INPUT` | `<sti-til-json>` × 2 | `<sti>` × 1 | **Mismatch** — COMMANDS.md mindre presis enn kjelda |
| `POLICY` | `<policy>` × 2, `<bronze\|silver\|gold>` × 1 | `<policy>` × 1, `<bronze\|silver\|gold\|felles-datakatalog\|felles-begrepskatalog>` × 1 | **Inkonsistent stil** — generisk ord vs. utskrive verdiliste, og verdilista i COMMANDS.md er meir fullstendig enn kjelda sin variant |
| `INSTANCE` | `<sti>` × 6 | `<sti>` × 2 | Konsistent |
| `ORG` | `<alias>` × 5 | `<alias>` × 3 | Konsistent (jf. [[valider-modellkatalog-org-alias]]) |
| `NAME` | `<modell>` × 4, `<begrepssamling-navn>` × 3, `<katalognavn>` × 2 | Same fordeling | Konsistent internt (jf. [[namn-navn-konsistens-make-help]]), men sjå **tiltak F** — fasit er å droppe det redundante `-navn`-suffikset sidan `NAME=` alt seier at det er eit namn |
| `MANIFEST` | `<sti>` × 2 | `<sti>` × 1 | Konsistent |
| `JSONSCHEMA` | `<sti>` × 1 | `<sti>` × 1 | Konsistent |
| `FORMAT` | `json-schema` (konkret verdi) × 2 | same × 1 | Konsistent — konkret eksempelverdi, ikkje ein omsetjbar plasshaldar |
| `PROFILE` | `bronze` × 2 | `default` × 1 | Begge er konkrete eksempelverdiar (ikkje plasshaldarar) — ulik verdi er ikkje eit brot, berre ulikt valt eksempel |
| `CONFIRM`, `DRYRUN` | `1` (flagg) | same | Ikkje aktuelt — reine boolske flagg |
| `SIMILARITY_THRESHOLD` | `0.8` (konkret verdi) | (ikkje dokumentert i COMMANDS.md) | `analyse-similar-*`-targeta manglar heilt i COMMANDS.md — eige, mindre funn, ikkje kjerneomfang her |

## Plan

### A — `DOMAIN=<domain>` → `DOMAIN=<domene>` (hovudtiltaket, 44 førekomstar)

Reint engelsk ord i elles norsk tekst — ikkje eit bokmål/nynorsk-spørsmål
(«domene» er identisk i begge skriftspråk), berre eit tilfelle av at
plasshaldaren aldri vart omsett. `README.md` sitt eksempel (`DOMAIN=domene`)
og dei 4 alt retta `new-modell`/`remove-modell`-førekomstane stadfestar at
`<domene>` er den tilsikta forma.

**`make/*.mk` (26 førekomstar, kjelde til `make help`):**

| Fil | Førekomstar | Kontekst |
|---|---|---|
| `make/11-generator-targets.mk` | 15 | `[DOMAIN=<domain>\|SCHEMA=<sti>]` i alle `gen-*`-## kommentarar |
| `make/30-instances.mk` | 1 | `gen-informasjonsmodell-instance` ## kommentar |
| `make/20-domain-targets.mk` | 1 | `gen-linkml-convert` ## kommentar |
| `make/40-validation.mk` | 6 | 3× ## kommentar (`validate-bronze/-data/-examples`) + 3× tilsvarande `log_error` |
| `make/70-scaffolding.mk` | 3 | `new-begrepssamling` ## kommentar + 2× `log_error` |

**Dokumentasjon (18 førekomstar):**

| Fil | Førekomstar |
|---|---|
| `COMMANDS.md` | 9 |
| `mkdocs/docs/kom-i-gang/kommandoar.md` | 5 |
| `mkdocs/docs/kom-i-gang/ny-domenemodell.md` | 3 |
| `mkdocs/docs/kom-i-gang/ny-org.md` | 1 |

Alle er identisk tekstlege `DOMAIN=<domain>`-treff (eller
`[DOMAIN=<domain>|SCHEMA=<sti>]` for `gen-*`-gruppa) — reint
søk-og-erstatt, ingen semantiske vurderingar naudsynte.

### B — `POLICY`: standardiser til generisk `<policy>`, dropp inline enum-liste

`mcp-linkml-valider-modell` sin `## `-kommentar viser
`[POLICY=<bronze|silver|gold>]` — ei **ufullstendig** liste (manglar
`felles-datakatalog`/`felles-begrepskatalog`, som COMMANDS.md sin
tilsvarande rad-prosa alt nemner korrekt). Framfor å halde ei
5-verdis-liste synkronisert to (eller fleire) stader, anbefalt løysing:
bruk generisk `POLICY=<policy>` konsekvent i **alle** `## `-kommentarar og
`COMMANDS.md`-kommandocelle, og la gyldige verdiar stå i **prosa-skildringa**
(slik `mcp-linkml-valider-modell`-raden i COMMANDS.md alt gjer). Same
mønster som `<sti>`, `<alias>`, `<domene>`, `<modell>` — éin generisk,
omsetjbar plasshaldar, ikkje ei verdi-oppslagsliste som kan drifte frå
den faktiske policy-lista i `src/mcp-linkml-validator/policies/`.

Påverka: `make/40-validation.mk` (`mcp-linkml-valider-modell` ## kommentar).

### C — `INPUT=<sti-til-json>`: gjer COMMANDS.md like presis som kjelda

`mcp-linkml-begrep-utkast` sin kjelde seier `<sti-til-json>` (presist —
argumentet må vere ei JSON-fil), men COMMANDS.md forkortar til generisk
`<sti>`. Rett COMMANDS.md til `<sti-til-json>` for å matche kjelda.

### D — `mcp-linkml-valider-modell` sin feilmelding: `<sti-til-skjema>` → `<sti>`

`make/40-validation.mk:202` sin `log_error`-melding brukar
`SCHEMA=<sti-til-skjema>`, einaste staden i heile repoet som ikkje bruker
standard `<sti>` for eit `SCHEMA=`-argument. Rett til `<sti>` for
konsistens med dei andre 32 `SCHEMA=<sti>`-førekomstane.

### E — `analyse-similar-*` manglar i COMMANDS.md (mindre, valfritt tillegg)

4 target (`analyse-similar-classes-domain/-all`,
`analyse-similar-slots-domain/-all`) med `[SIMILARITY_THRESHOLD=0.8]` er
ikkje dokumenterte i COMMANDS.md i det heile. Ikkje del av kjerneomfanget
(gjeld manglande dekning, ikkje eit plasshaldar-avvik), men nemnt sidan
det dukka opp under kartlegginga — kan takast som eit lite tillegg.

### F — `NAME=`: fasit for plasshaldarordet (droppar redundant `-navn`-suffiks)

Brukaren har stadfesta fasiten for alle `NAME=`-plasshaldarar:

| Target | Gjeld | Noverande | **Fasit** |
|---|---|---|---|
| `new-modell`, `remove-modell` | LinkML-modell | `NAME=<modell>` | `NAME=<modell>` — **uendra**, alt korrekt |
| `new-begrepssamling` | Begrepssamling | `NAME=<begrepssamling-navn>` | `NAME=<begrepssamling>` |
| `new-begrepskatalog` | (Legacy) begrepskatalog | `NAME=<katalognavn>` | `NAME=<katalog>` |

Grunngjeving: `NAME=` seier alt at verdien er eit namn — å i tillegg
skrive `-navn`/`navn` inn i sjølve plasshaldarordet (`<begrepssamling-navn>`,
`<katalognavn>`) er redundant. Mønsteret vert dermed reint
**`NAME=<konseptet-det-gjeld>`**, same struktur som `DOMAIN=<domene>`,
`ORG=<alias>`, `SCHEMA=<sti>` — plasshaldaren namngjev **kva slags ting**
det er (ein modell, ei begrepssamling, ein katalog), ikkje at det er eit
namn (det seier variabelnamnet `NAME` alt).

**Påverka stader:**

| Fil | Endring |
|---|---|
| `make/70-scaffolding.mk` | `new-begrepssamling`: `## `-kommentar + 2×`log_error` (3 førekomstar av `<begrepssamling-navn>` → `<begrepssamling>`). `new-begrepskatalog`: `## `-kommentar + `log_error` (2 førekomstar av `<katalognavn>` → `<katalog>`) |
| `COMMANDS.md` | Rad for `new-begrepssamling` (linje 147, 2 førekomstar inkl. output-kolonna) og `new-begrepskatalog` (linje 148, 2 førekomstar) |
| `mkdocs/docs/kom-i-gang/kommandoar.md` | Rad for `new-begrepskatalog` (1 førekomst — `new-begrepssamling` er ikkje dokumentert der frå før) |
| `src/assets/scripts/scaffolding/new-begrepskatalog.sh` | `log_error`-melding (1 førekomst) |

**Utanfor omfang (medvite, ikkje del av tiltak F):** `<katalognavn>` og
`<begrepssamling-navn>` opptrer òg som **stiillustrasjonar** i lengre
mkdocs-rettleiingar (`ny-begrepsmodell.md`, `publisering-begrep.md`,
`README.md` m.fl.), t.d. `src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml`.
Desse skildrar filstruktur, ikkje sjølve `NAME=`-argumentet, og er eit
vesentleg større, separat sveip (fleire rettleiingssider, mange
førekomstar per side) enn resten av denne specen sitt konsekvent avgrensa
omfang (`make/*.mk` + `COMMANDS.md`, med `mkdocs/kommandoar.md` berre der
han speglar ei `COMMANDS.md`-rad). Tek dette som eiga oppfølgings-spec
dersom ønskt.

## Evaluering: bør `NAME` bytast til `SCHEMA` for `new-modell`/`remove-modell`?

**Spørsmålet:** `new-modell`/`remove-modell` sitt `NAME=<modell>` gjeld
namnet på ein LinkML-modell (t.d. `tilskudd` → `tilskudd-schema.yaml`).
Bør dette argumentet heite `SCHEMA` i staden for `NAME`, sidan det gjeld
eit skjemanamn?

**Mot (anbefalt å halde `NAME`):**

- Alle 32+14 = 46 eksisterande `SCHEMA=`-førekomstar i repoet betyr
  eintydig **«sti til ei EKSISTERANDE skjemafil»** (`SCHEMA=<sti>`,
  t.d. `SCHEMA=src/linkml/oreg/tilskudd/tilskudd-schema.yaml`) — brukt av
  validerings-/genererings-target som opererer på skjema som alt finst.
- `new-modell` sitt argument er stikk motsett: eit **kort namn på ein
  modell som IKKJE finst enno** (`tilskudd`, ikkje ein sti, og fila
  eksisterer ikkje før kommandoen har køyrt). `SCHEMA=tilskudd` ville sett
  ut som ein (ugyldig, ufullstendig) sti-verdi, og bryte den elles
  eintydige `SCHEMA=<sti>`-konvensjonen.
- Å bruke `SCHEMA` for «namnet på noko nytt» og `SCHEMA` for «stien til
  noko eksisterande» samstundes ville gjere `SCHEMA` **meir** tvitydig,
  ikkje mindre — stikk i strid med heile føremålet med denne
  harmoniseringsrunden.
- `NAME` er derimot alt eintydig brukt for «kort identifikator på noko
  nytt som skal opprettast» på tvers av alle scaffolding-target
  (`new-modell`, `new-begrepssamling`, `new-begrepskatalog`) — eit
  konsistent, veletablert mønster i seg sjølv, stadfesta av
  [[namn-navn-konsistens-make-help]].

**For (mogleg motargument):**

- Kunne redusert tal på ulike toppnivå-argumentnamn ein brukar må lære.
- Om ein *hadde* innført eit slikt bytte, kunne plasshaldarteksten skilje
  det frå sti-varianten (t.d. `SCHEMA=<modellnamn>` i staden for
  `SCHEMA=<sti>`) — men det flyttar berre tvitydigheita frå variabelnamnet
  til plasshaldarteksten, og krev at brukaren likevel les nøye kva som
  faktisk vert forventa.

**Konklusjon:** Behald `NAME` for `new-modell`/`remove-modell`. Eit bytte
til `SCHEMA` ville løyst eit ikkje-eksisterande problem (dei to
konsepta — «sti til eksisterande fil» vs. «namn på ny modell» — er
allereie tydeleg skilde av kvarandre sine plasshaldartekstar, `<sti>` vs.
`<modell>`) og samstundes innført ei ny, reell tvitydigheit i `SCHEMA`
sin etablerte tyding andre stader.

## Filer som vert påverka (ved utføring)

- `make/11-generator-targets.mk`, `make/20-domain-targets.mk`,
  `make/30-instances.mk`, `make/40-validation.mk`, `make/70-scaffolding.mk`
  (tiltak A, B, D, F)
- `src/assets/scripts/scaffolding/new-begrepskatalog.sh` (tiltak F)
- `COMMANDS.md`, `mkdocs/docs/kom-i-gang/kommandoar.md`,
  `mkdocs/docs/kom-i-gang/ny-domenemodell.md`,
  `mkdocs/docs/kom-i-gang/ny-org.md` (tiltak A, C, F)
- Ingen kodeendring for tiltak E dersom det vert teke — reint tillegg av
  manglande rader i `COMMANDS.md`

## Handlingsliste

1. [x] A: Erstatt `DOMAIN=<domain>` → `DOMAIN=<domene>` i alle 44
   førekomstar (5 `make/*.mk`-filer + 4 dokumentasjonsfiler)
2. [x] B: Standardiser `POLICY` til generisk `<policy>` i
   `mcp-linkml-valider-modell` sin `## `-kommentar
3. [x] C: Rett `INPUT=<sti>` → `INPUT=<sti-til-json>` i `COMMANDS.md`
4. [x] D: Rett `SCHEMA=<sti-til-skjema>` → `SCHEMA=<sti>` i
   `make/40-validation.mk` sin `log_error`-melding
5. [x] E: **ikkje naudsynt** — `analyse-similar-*`/`analyse-iri-resolution`/
   `analyse-sammendrag` var alt dokumenterte i COMMANDS.md § «Modell-analyse»
   (linje 308-313) — feil i det opphavlege søket under kartlegginga
6. [x] F: Rett `NAME=<begrepssamling-navn>` → `NAME=<begrepssamling>` og
   `NAME=<katalognavn>` → `NAME=<katalog>` i `make/70-scaffolding.mk`,
   `COMMANDS.md`, `mkdocs/docs/kom-i-gang/kommandoar.md` og
   `src/assets/scripts/scaffolding/new-begrepskatalog.sh`
7. [x] NAME→SCHEMA-bytte for `new-modell`/`remove-modell`: **ikkje
   utført** — evalueringa over konkluderer med å halde `NAME`
8. [x] Verifiser med `make help` at alle `DOMAIN=`- og `NAME=`-førekomstar
   viser oppdaterte plasshaldarar, og at dei matchar tilsvarande rad i
   `COMMANDS.md`

## Utført

**A** — Alle 44 planlagde `DOMAIN=<domain>` → `DOMAIN=<domene>` retta:
`make/11-generator-targets.mk` (15), `make/30-instances.mk` (1),
`make/20-domain-targets.mk` (1), `make/40-validation.mk` (6),
`make/70-scaffolding.mk` (3), `COMMANDS.md` (9),
`mkdocs/docs/kom-i-gang/kommandoar.md` (5), `ny-domenemodell.md` (3),
`ny-org.md` (1). Bare `DOMAIN=`-syntaksen vart endra — frittståande
`<domain>` brukt som stiillustrasjon (t.d. `generated/<domain>/<modell>/`)
er urørt, sidan det er ei anna, mykje større klasse av tekst enn sjølve
argumentsyntaksen.

**B** — `mcp-linkml-valider-modell` sin `## `-kommentar:
`[POLICY=<bronze|silver|gold>]` → `[POLICY=<policy>]`. COMMANDS.md sin
prosa-forklaring var alt korrekt (full 5-verdis liste i teksten, ikkje i
kommandocella) — ingen endring naudsynt der.

**C** — `COMMANDS.md`: `INPUT=<sti>` → `INPUT=<sti-til-json>` for
`mcp-linkml-begrep-utkast`.

**D** — `make/40-validation.mk` sin `log_error` for
`mcp-linkml-valider-modell`: `SCHEMA=<sti-til-skjema>` → `SCHEMA=<sti>`.

**F** — `NAME=<begrepssamling-navn>` → `NAME=<begrepssamling>` og
`NAME=<katalognavn>` → `NAME=<katalog>` i `make/70-scaffolding.mk` (## +
`log_error`), `COMMANDS.md` (kommando- **og** output-kolonne, for
radintern konsistens), `mkdocs/docs/kom-i-gang/kommandoar.md` (same).

**Uventa funn under sluttverifiseringa (retta i tillegg):**
- `src/assets/scripts/scaffolding/new-begrepssamling.sh` hadde to
  `log_error`-meldingar med **både** `DOMAIN=<domain>` (engelsk) **og**
  `NAME=<begrepssamling-namn>` (nynorsk «namn», aldri fanga opp av
  [[namn-navn-konsistens-make-help]] sidan den specen berre dekte
  `make/70-scaffolding.mk`, ikkje det underliggande scriptet) — retta til
  `DOMAIN=<domene> NAME=<begrepssamling>`.
- `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md` linje 23 hadde sjølve
  kommandoeksempelet `make new-begrepskatalog NAME=<katalognavn>` — retta
  til `NAME=<katalog>`. Dei mange **stiillustrasjons**-førekomstane av
  `<katalognavn>` elles i same fil (t.d.
  `src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml`) er
  urørte, i tråd med den medvitne avgrensinga i tiltak F.

**Verifisert:** `make help` viser ingen attverande gamle former. Full
repo-søk stadfestar at ingen levande fil (utanfor `specs/done/` og denne
specen sjølv, som medvite dokumenterer før-tilstanden) har
`DOMAIN=<domain>`, `NAME=<begrepssamling-navn>`, `NAME=<begrepssamling-namn>`
eller `NAME=<katalognavn>` att. `make mcp-linkml-valider-modell -n` og
`make validate-bronze -n` køyrer framleis korrekt — reint tekstlege
plasshaldarendringar, ingen funksjonsendring.
