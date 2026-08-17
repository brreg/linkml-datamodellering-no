# Vurdering: gjer submodels til heilt eigne modellkatalogar

## Bakgrunn

`specs/done/modellkatalog-fleire-skjema-evaluering.md` (arkivert) evaluerte om
delt katalog for submodels (`dqv-core` i `dqv-ap-no/`, `modelldcat-katalog`/
`modelldcat-modell` i `modelldcat-ap-no/`) er eit problem, og konkluderte
"behald `submodels:`-mekanismen som ho er, ikkje innfør eit tredje
grupperingsnivå".

`specs/backlog/release-please-endringsdato-dekning-evaluering.md` viste
etterpå at denne konklusjonen kvilte på ein feil premiss — påstanden om at
"versjonering... er urørt" av mekanismen stemmer ikkje: `dqv-core` og
`modelldcat-katalog` har stått fast på `version: "1.0.0"` sidan dei vart
oppretta, fordi release-please sitt pakke-omgrep er katalogbasert og ikkje
kjenner `submodels:`. Den specen føreslo som mellombels fiks å la submodels
**spegle** versjonen til hovudpakken sin (via `extra-files`).

Brukaren føreslår no eit anna, meir grunnleggjande alternativ: **behald dei to
eksisterande nivåa (domene/modell), men lat kvar submodell få sin eigen,
fullstendig sjølvstendige modellkatalog** — same struktur og handsaming som
alle andre 38 modellar i repoet. Grunngjevinga: importtreet
(`imports:`-lista i kvart skjema) uttrykkjer alt avhengigheitene eksplisitt,
så fysisk samlokalisering i same mappe er ikkje naudsynt for å halde
relasjonen synleg.

## Vurdering

### 1. Held den opphavlege grunngjevinga for `submodels:` ved lag?

Den arkiverte evalueringa peika på to legitime bruksområde: sirkulær-import-
unngåing (`dqv-core`) og logisk spesifikasjonsseparasjon
(`modelldcat-katalog`/`-modell`). Eit sentralt poeng vart oversett då: **det
er eksistensen av dqv-core som ei sjølvstendig, importerbar eining** som løyser
sirkulær-importen mellom `dcat-ap-no` og `dqv-ap-no` — ikkje at fila ligg
fysisk *inni* `dqv-ap-no/`-mappa. Verifisert direkte mot faktiske
`imports:`-lister:

```
dcat-ap-no-schema.yaml   → ../dqv-ap-no/dqv-core-schema      (i dag)
skos-ap-no-schema.yaml   → ../dqv-ap-no/dqv-core-schema      (i dag)
dqv-core-schema.yaml     → ../common-ap-no/common-ap-no-schema  (uendra ved flytting)
```

Flyttar `dqv-core-schema.yaml` til ei eiga søskenmappe
(`src/linkml/ap-no/dqv-core/`), endrar **kven som importerer kven** seg ikkje
i det heile — berre stien til to import-liner (`dcat-ap-no`, `skos-ap-no`)
må oppdaterast. `dqv-core` sine eigne imports (`../common-ap-no/...`) er
uendra sidan avstanden til søskenmapper under same domene er identisk uansett
kva for søskenmappe fila ligg i. **Sirkulær-import-risikoen vert altså ikkje
reintrodusert** — fysisk samlokalisering var aldri det som løyste problemet,
berre eit implisitt biprodukt av korleis fila opphavleg vart oppretta.

Same verifikasjon for `modelldcat-katalog`/`-modell`-kjeda
(`modelldcat-ap-no → modelldcat-katalog → modelldcat-modell → dcat-ap-no`):
kjeda er lineær (ikkje sirkulær) i utgangspunktet, og flytting krev berre
oppdatering av 2 import-linjer (`modelldcat-ap-no-schema.yaml`:
`./modelldcat-katalog-schema` → `../modelldcat-katalog/modelldcat-katalog-schema`;
`modelldcat-katalog-schema.yaml`: `./modelldcat-modell-schema` →
`../modelldcat-modell/modelldcat-modell-schema`).

**Konklusjon:** grunngjevinga for `submodels:` var eigentleg alltid ei
grunngjeving for "eige skjema", ikkje for "same mappe som ein annan modell".
Brukarens alternativ løyser same underliggjande problem (unngå sirkulær
import / halde spesifikasjonsdelar fysisk separate) med same middel
(eige skjema, eige import-punkt) — berre utan den unødvendige
samlokaliseringa.

### 2. Løyser dette release-please Kategori B fullt ut?

Ja, og reinare enn "spegle versjon"-forslaget i
`release-please-endringsdato-dekning-evaluering.md`. Kvar av dei tre
submodels vert då ein ordinær, sjølvstendig `<domain>/<modell>`-katalog —
nøyaktig same mønster som dei 38 andre modellane, og nøyaktig same mønster
som Kategori A/C i den evalueringa alt tilrår. Dei kan då:
- Registrerast som ordinære, uavhengige pakkar i `release-please-config.json`
  (ingen `extra-files`-spegling naudsynt)
- Få reell uavhengig SemVer (i tråd med brukaren sitt generelle prinsipp
  "alle skal versjonerast uavhengig", jf. svar på spørsmål 2 i
  release-please-evalueringa — noko "spegle versjon"-alternativet eksplisitt
  **ikkje** oppnådde)
- Handterast av `find`/`extra-files`-oppdaginga utan spesialtilfelle i det
  heile — heile Kategori B forsvinn som eigen kategori, det vert éin
  einsarta løysing for alle 12 (9 + 3) manglande/feilhandterte pakkar

### 3. Kva skjer med kostnadsbiletet frå den arkiverte evalueringa?

Den arkiverte evalueringa (§2 "Der ho kostar noko") listar konkret
spesialkode knytt til at fleire skjema deler katalog:
`delmodell-spesialtilpassing.md`, `delmodell-dokumentasjon.md`,
`nye-host-python-kall-batching.md`, `reduser-podman-kall-docs-publish.md`,
`stille-feil-batching-regresjon.md`, samt `har_del`-feltet i
`generate-informasjonsmodell.py` og logikken i
`mkdocs/lib/sections/delmodellar.sh`. Alt dette er spesialkode som finst
**berre fordi** nokre modellar deler fysisk katalog med ein annan. Vert alle
tre submodels flytta ut, finst det ikkje lenger nokon "delmodell"-tilstand i
repoet i det heile — denne spesialkoden vert daud og kan fjernast. Dette er
ei direkte DRY-forbetring (CLAUDE.md § DRY): mindre spesialkode å halde ved
like, ikkje meir.

**Motstykke:** fjerning av spesialkoden er sjølv eit ikkje-trivielt
endringsarbeid (fleire filer i `mkdocs/lib/`, `src/assets/scripts/`), og bør
verifiserast grundig (m.a. `make docs-publish` lokalt) før han vert fjerna —
kan gjerast som eit eige oppfølgingssteg etter sjølve flyttinga, ikkje
naudsynt i same endring.

### 4. Påverkar dette konklusjon #3 i den arkiverte evalueringa (treng vi eit tredje grupperingsnivå)?

Nei — brukarens alternativ **held seg eksplisitt innanfor** dei to
eksisterande nivåa (domene/modell). Det er ikkje eit tredje nivå, det er
fråvær av eit unntak frå det andre nivået. Konklusjon #3 i den arkiverte
evalueringa ("nei, ikkje treng eit tredje nivå") vert difor ikkje utfordra —
tvert imot gjer dette alternativet spørsmålet endå meir irrelevant, sidan det
fjernar den einaste eksisterande grunnen til at nokon kunne ønskje seg eit
tredje nivå i utgangspunktet.

### 5. Kva misser vi ved å fjerne fysisk samlokalisering?

- **Menneskeleg lesbar gruppering** ("desse tre høyrer saman som éin
  spesifikasjon") — i dag implisitt via delt mappe. Etter flytting må
  relasjonen formidlast på andre måtar: `imports:`-lista er alt maskinlesbar
  og vert vist i mkdocs-portalen (jf. `specs/done/importhierarki-imports-seksjon.md`
  — "Imports"-seksjonen i genererte `index.md`-sider). `description.md` for
  kvar ny modellkatalog kan i tillegg eksplisitt nemne
  spesifikasjons-familien (t.d. "ModelDCAT-AP-NO består av tre delar:
  modelldcat-ap-no, modelldcat-katalog, modelldcat-modell"). Dette er
  ikkje verre enn korleis andre relaterte-men-sjølvstendige modellar i
  repoet i dag vert kryssreferert (t.d. `dcat-ap-no` som vert importert av
  dusinvis av domenemodellar utan å dele katalog med nokon av dei).
- **Delt versjonshistorikk** i éin `CHANGELOG.md` — submodels ville få eigen,
  fresh `CHANGELOG.md` (same som alle andre `make new-modell`-scaffoldingar).
  Historisk samanheng (kva endring i dqv-ap-no som trigga ei endring i
  dqv-core) forsvinn frå éin samla logg, men var uansett aldri eksplisitt
  kopla i den delte loggen i dag (begge skjema sine endringar vart berre
  interleava under same fil).

Ingen av desse er blokkerande — dei er avvegingar som allereie gjeld for
alle andre relaterte-men-sjølvstendige modellpar i repoet.

### 6. Migreringskostnad (per submodell — × 3: dqv-core, modelldcat-katalog, modelldcat-modell)

| Steg | Detalj |
|---|---|
| Opprett ny søskenmappe | `src/linkml/ap-no/<submodell>/` |
| Flytt skjemafil | filnamn er alt korrekt (`<submodell>-schema.yaml`), berre flytting |
| Flytt metadata-manifest | `metadata/<submodell>-manifest.yaml` finst alt separat for alle tre (stadfesta) — reint flytt, ingen ny fil |
| Ny `build.yaml` | Finst ikkje frå før for submodels (dei red på foreldrepakken sin) — må opprettast med full `generators:`-blokk (kopier frå foreldre-build.yaml) og eiga `validation_policy` |
| Nye `CHANGELOG.md`/`description.md`/`examples/` | Fresh, same som ved `make new-modell` |
| Oppdater 2 import-linjer per submodell | Sjå §1 — trivielt, verifisert konkret over |
| Fjern `submodels:`-felt | `dqv-ap-no/build.yaml`, `modelldcat-ap-no/build.yaml` |
| Legg til 3 nye pakkar | `release-please-config.json` + `-manifest.json`, startversjon = noverande `version:` i kvart skjema (dqv-core 1.0.0, modelldcat-katalog 1.0.0, modelldcat-modell 1.14.0) |
| Regenerer `valid-scopes.txt` | `make update-valid-scopes` (automatisk — allereie dynamisk generert) |
| Oppdater CONVENTIONS.md § "Éin modell per katalog" | `submodels:`-unntaket har då 0 aktive brukstilfelle — avklar om formuleringa skal fjernast, eller behaldast som dokumentert mekanisme for eit *framtidig* faktisk sirkulær-import-tilfelle |
| (Oppfølging, kan gjerast separat) | Fjern daud delmodell-spesialkode i `mkdocs/lib/`, `generate-informasjonsmodell.py` (`har_del`) |

Avgrensa og velkjent omfang — samanliknbart med å opprette 3 heilt nye
modellar via `make new-modell`, pluss fire trivielle import-sti-oppdateringar
og fjerning av eit build.yaml-felt.

## Tilråding

**Vedta alternativet.** Det er strengt betre enn både status quo og
"spegle versjon"-forslaget i `release-please-endringsdato-dekning-evaluering.md`:
løyser release-please-versjoneringsproblemet fullstendig (ikkje berre
dato-symptomet), gjev reell uavhengig versjonering i tråd med brukaren sitt
uttalte prinsipp, fjernar ein heil kategori dokumentert spesialkode
(DRY-gevinst), reintroduserer ikkje sirkulær-import-risiko, og utfordrar ikkje
konklusjonen om at eit tredje grupperingsnivå er unødvendig.

Dette **erstattar** Kategori B-tilrådinga ("alternativ (a) — spegl versjon
frå hovudpakken") i `release-please-endringsdato-dekning-evaluering.md` med
ei reinare løysing: gjer submodels til ordinære pakkar, akkurat som Kategori
A og C.

## Handlingsliste

- [x] Stadfest med brukar at migreringa (§6) skal gjennomførast for alle tre submodels — brukar bad eksplisitt om utføring
- [x] Opprett dei tre nye modellkatalogane (`dqv-core`, `modelldcat-katalog`, `modelldcat-modell`) med `build.yaml` (kopi av generators-blokk + `validation_policy: gold`, som før), `description.md`, `CHANGELOG.md` — ingen `examples/` oppretta (submodels manglar `tree_root`, hadde ingen frå før)
- [x] Flytt skjemafiler + metadata-manifest, oppdater dei 4 import-linjene (`dcat-ap-no`, `skos-ap-no` → `../dqv-core/...`; `modelldcat-ap-no` → `../modelldcat-katalog/...`; `modelldcat-katalog` → `../modelldcat-modell/...`)
- [x] Fjern `submodels:`-felt frå `dqv-ap-no/build.yaml` og `modelldcat-ap-no/build.yaml`; oppdater `description.md` i begge til å beskrive den nye strukturen
- [x] Legg dei tre nye pakkane til `release-please-config.json` + `-manifest.json` (startversjon = noverande `version:`: dqv-core 1.0.0, modelldcat-katalog 1.0.0, modelldcat-modell 1.14.0)
- [x] `make lint`/`make roundtrip` på alle tre nye kataloger + dei fire endra importørane — alle grøne (kun pre-eksisterande `canonical_prefixes`-åtvaringar, ingen nye)
- [x] Fann og retta éin hardkoda sti utover det spec opphavleg lista: `make/30-instances.mk` (`validate-informasjonsmodell-instance`) hadde `/work/src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml` hardkoda — oppdatert til ny sti
- [x] Regenerert `metadata/*-manifest.yaml` for alle 5 involverte skjema via `make gen-informasjonsmodell-instance` — `har_del`-referansane i dei to foreldre-manifesta er no korrekt tomme, `finnes_i_format`-URL-ane i dei tre nye peikar på rett stad
- [x] `make update-valid-scopes` — 37 scope uendra, dqv-core/modelldcat-katalog/modelldcat-modell framleis til stades
- [x] Oppdater CONVENTIONS.md § "Éin modell per katalog": fjerna unntaket, `submodels:` dokumentert som framleis tilgjengeleg mekanisme utan aktive brukstilfelle
- [x] Oppdater `mkdocs/docs/kom-i-gang/build-config.md` §`submodels`, `mkdocs/docs/automasjon/readme-tabellgenerering.md` og kommentaren i `generate-readme-tables.sh` — alle viste til dei no-flytta filene som eksempel
- [x] `make docs-publish` lokalt — fullførte med exit code 0. Alle tre nye modellar bygde eigne portalsider (`mkdocs/docs/ap-no/{dqv-core,modelldcat-katalog,modelldcat-modell}/`), og README.md sin auto-genererte skjematabell listar no alle tre som sjølvstendige rader (dei vart tidlegare filtrert bort av `generate-readme-tables.sh` sitt filnamn=katalognamn-krav — no oppfylt)
- [ ] Oppfølgingssteg (eiga spec): fjern daud delmodell-spesialkode i `mkdocs/lib/sections/delmodellar.sh`, `generate-informasjonsmodell.py` (`har_del`), `mkdocs/lib/generate_index.sh`, `mkdocs/lib/scripts/collect-schema-metadata.py`, `src/assets/scripts/scaffolding/remove-modell.sh` — ikkje gjort i denne runda, koden er dormant (ingen `submodels:`-førekomstar att) men ikkje fjerna
- [x] Oppdater `release-please-endringsdato-dekning-evaluering.md`: fjerna "spegle versjon"-alternativet, refererer hit i staden

## Utført

Utført 2026-08-17. Alle tre submodels (`dqv-core`, `modelldcat-katalog`,
`modelldcat-modell`) er no ordinære, sjølvstendige `<domain>/<modell>`-
katalogar under `src/linkml/ap-no/`, med eigen `build.yaml`,
`description.md`, `CHANGELOG.md` og eiga release-please-pakke (startversjon
= tidlegare `version:`-felt). `dqv-ap-no` og `modelldcat-ap-no` har ikkje
lenger `submodels:`-felt. Fire import-linjer (`dcat-ap-no`, `skos-ap-no`,
`modelldcat-ap-no`, `modelldcat-katalog`) er oppdaterte til dei nye stiane.

Verifisert: `make lint`/`make roundtrip` grøne på alle involverte skjema,
`make update-valid-scopes` uendra tal (37), `make gen-informasjonsmodell-instance`
regenererte alle fem påverka manifestfiler korrekt, og full `make docs-publish`
fullførte med exit code 0 — dei tre nye modellane fekk eigne portalsider, og
README.md sin auto-genererte skjematabell listar dei no som sjølvstendige
rader (tidlegare filtrerte bort).

**Biverknad oppdaga og retta:** ein hardkoda sti i
`make/30-instances.mk` (`validate-informasjonsmodell-instance`) peikte på den
gamle plasseringa av `modelldcat-katalog-schema.yaml` — retta til ny sti.
Dette var ikkje lista i den opphavlege migreringsplanen (§6).

**Bevisst utelate frå denne runda:** fjerning av den no daude
delmodell-spesialkoden i `mkdocs/lib/sections/delmodellar.sh`,
`generate-informasjonsmodell.py` (`har_del`-felt), `mkdocs/lib/generate_index.sh`,
`mkdocs/lib/scripts/collect-schema-metadata.py` og
`src/assets/scripts/scaffolding/remove-modell.sh`. Koden er verifisert
dormant (ingen `submodels:`-førekomstar att i noko `build.yaml`), men sjølve
fjerninga er eit eige, avgrensa oppfølgingsarbeid (jf. DRY-prinsippet i
CLAUDE.md — bør gjerast som eiga endring, ikkje bundla inn her).

**Ikkje gjort i denne runda (utanfor denne specen sitt omfang):** Kategori A
(9 manglande modellar) og Kategori C (referanse-splitten) frå
`release-please-endringsdato-dekning-evaluering.md` — den specen står framleis
i `specs/backlog/` med desse to attverande.
