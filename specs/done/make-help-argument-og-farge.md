# Plan: Tydelegare argumentvising og fargebruk i `make help`

## Bakgrunn

`make help` genererer i dag ei kategorisert target-liste via
`src/assets/scripts/makefile/help.sh`, som les `## `-kommentaren etter kvart
target i `Makefile`/`make/*.mk` og skriv ut éi linje per target:

```
  roundtrip:                      Køyr roundtrip-testar (YAML→TTL→YAML) [SCHEMA=<sti>]
```

Argumenta (`SCHEMA=<sti>` osv.) ligg i dag **inni skildringsteksten**, ofte
heilt til slutt i setninga, og notasjonen er ikkje konsekvent:

```
$ grep -hE '^[a-zA-Z_-]+:.*?## .*$' make/*.mk Makefile | grep -oE '\[[A-Z_]+=[^]]*\]' | sort -u
[CONFIRM=1]  [DOMAIN=<domain>]  [DRYRUN=1]  [FORMAT=json-schema]  [JSONSCHEMA=<sti>]
[ORG=<alias>]  [POLICY=<bronze|silver|gold>]  [PROFILE=bronze]  [SCHEMA=<sti>]
[SCHEMA=<sti>|DOMAIN=<domain>]  [SCHEMAS=<sti ...>]  [SIMILARITY_THRESHOLD=0.8]
```

Nokre target (t.d. `validate-instance`, `new-modell`) skriv obligatoriske
argument i **parentes** i staden for **hakeparentes**:

```
validate-instance: ## Valider instansfil mot skjema (SCHEMA=<sti> INSTANCE=<sti>)
new-modell:         ## Opprett katalogstruktur og boilerplate for ny domenemodell (NAME=<namn> DOMAIN=<domene>)
```

30 av 81 target har eit slikt argument-uttrykk; resten tek ingen argument.
Alle target-namn får same farge (`CLR_STEP`, cyan) og skildringa står i
terminalen sin standardfarge — det er ingen fargemessig distinksjon mellom
«dette skriv du i terminalen» og «dette er forklaringa».

**Ønskt sluttilstand:** argumentlista skal stå rett etter kallnamnet (ikkje
gøymt inni prosateksten), og fargebruk skal tydeleg skilje kommando+argument
(det brukaren skal skrive) frå hjelpetekst (det brukaren skal lese).

## Felles avklaring: korleis argumenta vert henta ut

Begge forslaga under må løyse same underliggjande spørsmål — kor kjem
arg-strengen frå?

**Alternativ 1 — regex-uttrekk frå eksisterande `[...]`/`(...)`-hale (anbefalt)**
`help.sh` utvidast til å trekkje ut ei avsluttande `[ARG=...]`- eller
`(ARG=...)`-gruppe frå skildringsteksten med eit tillegg til dagens
sed/awk-pipeline, og fjerne han frå sjølve skildringa. Krev at dei ~30
target som manglar hakeparentes for obligatoriske argument (`validate-instance`
m.fl.) vert normaliserte til éin konsekvent notasjon:
- `ARG=<verdi>` (ingen parentes) = obligatorisk
- `[ARG=<verdi>]` = valfri

Kostnad: ~13 linjer i `make/*.mk` må endrast frå `(ARG=...)` til `ARG=...`
utan parentes. Ingen nye kommentarkonvensjonar å lære.

**Alternativ 2 — eksplisitt markør i `## `-kommentaren**
Ny todelt syntaks i sjølve Makefile-kommentaren, t.d.
`target: ## [ARGS: SCHEMA=<sti>] Skildring` eller eit eige skilje-teikn
(`||`). Sjølvdokumenterande og utvidbart (t.d. kan seinare bere datatype),
men krev at **alle 81** target-linjer får kommentaren sin omskriven, og
introduserer eit nytt format brukarar/bidragsytarar må læra når dei legg
til nye target.

Alternativ 1 gjev same visuelle sluttresultat med ~1/6 av diff-storleiken.
Denne specen legg alternativ 1 til grunn i mockupane under, men forslaga
er uavhengige av kva for alternativ ein vel.

## Forslag A — eigen argument-kolonne, éi linje per target

Argumenta får ein eigen kolonne mellom target-namn og skildring, med eiga
farge. Kolonnebreidda vert rekna ut dynamisk per kategori (som i dag), slik
at lang argumentliste i éin kategori ikkje øydelegg innrykk i ein annan.

```
Vanleg bruk:
  test                                          Køyr alle testar
  roundtrip           [SCHEMA=<sti>]             Køyr roundtrip-testar (YAML→TTL→YAML)
  clean                                          Slett alle genererte filer (generated/)

Validering:
  validate-instance   SCHEMA=<sti> INSTANCE=<sti>  Valider instansfil mot skjema
  validate-bronze     [DOMAIN=<domain>]            Valider skjema med bronze-policy
```

Fargelegend:
| Segment | Farge | Grunngjeving |
|---|---|---|
| target-namn | `CLR_STEP` (cyan) — som i dag | Uendra, alt kjent frå eksisterande output |
| argumentliste | `CLR_WARN` (gul) | Gult signaliserer «legg merke til dette» — konsekvent med bruken av `CLR_WARN` elles i byggloggen. Obligatoriske argument (ingen `[]`) og valfrie (`[]`) skil seg på syntaks, ikkje berre farge |
| skildring | `CLR_DBG` (dim) — ny bruk i help-kontekst | Dempar hjelpeteksten visuelt slik at auget først fangar opp *kva du skriv* (cyan+gul), deretter *kva det gjer* (dempa) |

**Fordelar:** kompakt, same tal linjer som i dag (81), rask å skumme.
**Ulemper:** tre kolonner krev meir breidde — lange argumentlister
(`SCHEMA=<sti> INSTANCE=<sti>`) kan tvinge fram brei terminal eller
linjebrot ved <100 kolonner. Dynamisk kolonnebreidde per kategori gjer
`help.sh` noko meir kompleks (må rekne maks breidd i to gjennomløp).

## Forslag B — to linjer per target: kall-syntaks + skildring

Første linje viser heile kall-syntaksen slik han skal skrivast
(`make <target> <argument>`), farga som éi eining. Andre linje, ekstra
innrykka, er rein hjelpetekst.

```
Vanleg bruk:
  make roundtrip [SCHEMA=<sti>]
      Køyr roundtrip-testar (YAML→TTL→YAML)

  make clean
      Slett alle genererte filer (generated/)

Validering:
  make validate-instance SCHEMA=<sti> INSTANCE=<sti>
      Valider instansfil mot skjema

  make validate-bronze [DOMAIN=<domain>]
      Valider skjema med bronze-policy
```

Fargelegend:
| Segment | Farge | Grunngjeving |
|---|---|---|
| `make ` | `CLR_DBG` (dim) | Reint syntaktisk fyllstoff, treng ikkje stikke seg fram |
| target-namn | `CLR_STEP` (cyan, bold) | Same rolle som i dag, men no visuelt kopla saman med argumenta på same linje |
| argumentliste | `CLR_WARN` (gul) | Same grunngjeving som forslag A |
| skildringslinje | standard terminalfarge eller `CLR_DBG` | Andre linja er tydeleg skilt frå første ved innrykk åleine, så mindre kontrast trengst her enn i forslag A |

**Fordelar:** heile første linje er bokstaveleg tala til å kopiere/lime inn i
terminalen (ingen mental omforming frå «kolonne-format» til kommando).
Skalerer betre for lange argumentlister — ingen kolonnejustering å halde styr
på. Tydelegare skilje kommando/dokumentasjon ettersom dei bur på fysisk
åtskilde linjer, ikkje berre ulik farge.
**Ulemper:** dobbelt så mange linjer (81 → ~162), `make help` vert
lengre å skumme/scrolle gjennom i sin heilskap (kategorisering og
`less`-piping vert viktigare).

## Skilnaden på forslaga oppsummert

| | Forslag A (kolonne) | Forslag B (to linjer) |
|---|---|---|
| Linjer i `make help`-output | 81 (uendra) | ~162 |
| Kopier-lim-vennleg | Nei — må setje saman target+argument manuelt | Ja — heile linja er gyldig `make`-kall |
| Robust mot lange argumentlister | Nei — trong kolonnebreidd | Ja |
| Diff-storleik i `help.sh` | Middels (dynamisk kolonnebreidd) | Liten (rein linjeformatering) |
| Best eigna for | Rask oversikt over mange target samstundes | Nybyrjarar / kopiere konkrete kall |

## Handlingsliste

1. [x] Kartlegg dagens argument-notasjon i `make/*.mk` og `Makefile` (sjå «Bakgrunn»)
2. [x] Skriv to forslag med fargelegend og mockup (denne specen)
3. [ ] **Avventar val frå brukar:** forslag A, forslag B, eller ein hybrid
4. [ ] Ved val: normaliser argument-notasjon i `make/*.mk`/`Makefile` til
   `ARG=<verdi>` (obligatorisk) / `[ARG=<verdi>]` (valfri) — alternativ 1
5. [ ] Implementer valt forslag i `src/assets/scripts/makefile/help.sh`
6. [ ] Verifiser med `make help` og `make` (default-target) at output er
   lesbart både med og utan farge (`NO_COLOR=1`/ikkje-TTY — sjekk om
   `help.sh` alt handterer dette, ev. legg til)
7. [x] Oppdater `COMMANDS.md` § om `make help`-output dersom formatet
   påverkar dokumentasjonen der (sjå referanse på linje 80)

## Utført

Vald: **Forslag B** (to linjer per target: kall-syntaks + skildring).

- `src/assets/scripts/makefile/help.sh`: skil no ut avsluttande argument-grupper
  (`(...)`/`[...]`, krev "=" for å ikkje ta med vanlege parentetiske merknadar
  som `(1080p, høg kvalitet)`) frå skildringa, og skriv target som
  `make <target> <argument>` på éi kopierbar linje (`CLR_DBG` for «make »,
  `CLR_STEP` for target-namn, `CLR_WARN` for argument), med skildringa dempa
  (`CLR_DBG`) på neste, innrykka linje. Tom linje mellom kvart target-blokk.
- To avvik frå mockupen i denne specen, avgjort under implementering:
  - Alternativ 1 sitt normaliseringssteg (4) synte seg unødvendig — parentes
    for obligatoriske og hakeparentes for valfrie argument var alt ein
    konsekvent konvensjon i kjeldefilene (ikkje motstridande som først
    anteke). `help.sh` hentar difor ut heile den avsluttande gruppa
    ordrett, inkludert parentes/hakeparentes-teiknet, i staden for å
    normalisere alt til bare `ARG=<verdi>`-tokens. Ingen linjer i
    `make/*.mk`/`Makefile` måtte endrast.
  - Target-namnet er ikkje sett i **bold** cyan (berre eksisterande
    `CLR_STEP`, ikkje-feit) — ingen bold-variant finst i dagens
    fargepalett (`make/00-settings.mk`), og å innføre éin ny berre for
    dette var ikkje verdt kompleksiteten.
- Verifisert med `make help` og `make` (default-target) — begge viser
  korrekt to-linjers format med farge, inkludert kanttilfelle: fleire
  etterfølgjande argumentgrupper (`remove-modell`), nøsta hakeparentes i
  parentes (`mcp-linkml-modell-utkast`), og «eller»-uttrykk i parentes
  (`log-mcp-validate`) — alle handterte korrekt utan feilklassifisering.
- `COMMANDS.md` linje 80 sin referanse til `make help`-output er
  formatuavhengig (handlar om at delegering ikkje er synleg der) — ingen
  endring naudsynt.
- Ingen NO_COLOR/ikkje-TTY-handtering vart lagt til (var alt fråverande
  før denne endringa, uendra scope).
