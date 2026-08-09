# Dokumenter batching i COMMANDS.md

## Bakgrunn

Brukaren bad om å oppdatere kommandooversikta (`COMMANDS.md`) med kva
kommandoar som nyttar batching, og ei skildring av korleis batchinga
fungerer for kvar kommando.

Repoet har over fleire tidlegare økter (`specs/done/effektiviser-generate-
workflow-koyretid.md`, `specs/done/effektiviser-mcp-linkml-validator-
koyretid.md`, `specs/done/batch-validate-lint-test-per-skjema.md`) bygd ut
eit gjennomgåande batching-mønster: i staden for éin `podman run` per
skjema (som betaler ~5-8 s import-/oppstartskostnad for `linkml`/
`linkml_runtime` kvar gong), samlar batch-scripta N skjema inn i **éin**
kontainarprosess. Dette er dokumentert spreidd i kommentarar i `make/*.mk`
og i dei tre spesifikasjonane over, men **ikkje samla på éin stad** i
`COMMANDS.md` — brukarar av kommandoane har i dag ingen enkel måte å sjå
kva kommandoar som er batcha, kva som framleis er per-skjema, og korleis
batchinga faktisk fungerer per kommando.

**Merk skiljet mot "Parallellisering"** (alt dokumentert i COMMANDS.md §
"Generering av artefakter"): parallellisering (`PARALLEL=N`) styrer kor
mange **skjema som køyrer samstundes** (fleire prosessar/bakgrunnsjobbar).
Batching er noko anna — det styrer kor mange **kontainarar** som startast
i det heile, ved å behandle N skjema i éin delt prosess. Dei to teknikkane
er komplementære (t.d. batcha `gen-plantuml` sin SVG-rendering-fase køyrer
i éin kontainar for alle skjema, medan `validate-examples` framleis er
per-skjema men parallellisert via bakgrunnsjobbar).

## Kartlegging (frå kodelesing, ikkje spekulasjon)

Gjennomgått: `make/10-generator-macros.mk`, `make/11-generator-targets.mk`,
`make/20-domain-targets.mk`, `make/30-instances.mk`,
`make/40-validation.mk`, `Makefile`.

**Batcha kommandoar:**

| Kommando | Mekanisme |
|---|---|
| `make validate` | `run_gen_linkml_parallel` → `batch-generate.py --generator merge`, éin kontainar for alle skjema |
| `make lint` | `batch-lint.py` — delt `Linter`/`TerminalFormatter`-sesjon, éin kontainar |
| `make gen-jsonld-context`, `gen-python`, `gen-jsonschema`, `gen-proto` | `run_gen_parallel` → `batch-generate.py --generator <namn>`, éin kontainar |
| `make gen-shacl`, `gen-owl`, `gen-rdf` | Same REGISTRY-mønster, eigne makroar (`run_gen_shacl_parallel` m.fl.) |
| `make gen-docs` | To batcha fasar: Fase A (`batch-generate-instances.py --generator docgen-examples`, Python-kontainar) + Fase B (`batch-generate.py --generator doc`, linkml-kontainar) |
| `make gen-erdiagram` | Tre fasar: Fase A batcha (linkml), Fase A.5 **ikkje** batcha/kontainerisert (awk på host, per skjema), Fase B batcha (Python-filter) |
| `make gen-plantuml` | Tre fasar: Fase A batcha (linkml), Fase B batcha (Python-filter), Fase C batcha SVG-rendering for **alle** skjema i éin PlantUML-kontainar |
| `make gen-openapi` | Fullt batcha (generering + validering saman) |
| `make gen-asyncapi` | Fase A batcha (generering), Fase B **ikkje** batcha (`asyncapi validate`, Node-image — kun 1 skjema i repoet har `asyncapi: true`, ikkje verdt å batche) |
| `make validate-bronze DOMAIN=<d>` | `batch-flatten-and-validate.py --policy bronze`, éin kontainar for alle skjema i domenet |
| `make validate-data DOMAIN=<d>` | Same script, `--jobs-tsv` for heterogene (skjema, policy, datafil)-triplar |
| `make gen-informasjonsmodell-instance` (som steg i `domain-*`) | `batch-generate-instances.py --generator informasjonsmodell`, reint Python, éin kontainar |
| `tests/test_make.sh` (`make test`, `make roundtrip`) | Fase A/Fase B-mønster — alle 17 teststeg batchar no generering/validering på tvers av heile skjemalista **før** per-skjema-assert (Kategori A-D, sjå `specs/done/batch-validate-lint-test-per-skjema.md`) |

**Ikkje batcha (medvite, eller endå ikkje gjort):**

| Kommando | Kvifor ikkje batcha |
|---|---|
| `make gen-xsd` | Berre 1 skjema i repoet har `xsd: true` — inga gevinst |
| `make convert-rdf`, `make convert-data` | Framleis éin `linkml-convert`-podman-kall per fil, sekvensielt. `tests/test_make.sh` sin eigen `batch-convert.py` batchar tilsvarande operasjon internt i testsuiten, men denne batchinga er **ikkje** kopla til dei faktiske `make convert-rdf`/`convert-data`-måla |
| `make validate-examples DOMAIN=<d>` | Framleis éin `linkml validate`-podman-kall per skjema — parallellisert via bakgrunnsjobbar, men **ikkje** batcha til éin kontainar |
| `make mcp-linkml-valider-modell` | Tek berre eitt skjema om gongen (ingen `SCHEMAS`-liste) — den underliggande `batch-flatten-and-validate.py` støttar batching, men targetet eksponerer det ikkje |
| `make gen-dqv-measurements`, `gen-modellkatalog-instance`, `gen-begrepskatalog-instance` | Køyrer alt som eitt samla script over all data — ikkje eit per-skjema-mønster å batche i utgangspunktet |

## Steg

1. Legg til ein ny seksjon «## Batching» i `COMMANDS.md`, plassert etter
   «## Logging» og før «## Wrapper-target» (same nivå som dei andre
   tverrgåande arkitektur-seksjonane).
2. Forklar kort kva batching er og korleis det skil seg frå
   parallellisering (jf. «Merk skiljet» over).
3. Legg til ei tabell over batcha kommandoar med kort skildring av
   mekanismen per kommando/fase (basert på kartlegginga over).
4. Legg til ei tabell over ikkje-batcha kommandoar med grunngjeving, slik
   at fråveret av batching er eksplisitt dokumentert og ikkje ser ut som
   ei forgløymt inkonsistens.
5. Kryssrefererer til dei tre kjelde-spesifikasjonane i `specs/done/` for
   djupare detaljar/målingar, i tråd med DRY-prinsippet i CLAUDE.md
   (ikkje dupliser dei fulle målingane/grunngjevingane — berre
   oppsummer og lenk).
6. Oppdater specen med `## Utført` og flytt til `specs/done/`.

## Akseptansekriterium

- `COMMANDS.md` har ein tydeleg «Batching»-seksjon som listar kvar batcha
  kommando og korleis batchinga fungerer for han.
- Ikkje-batcha kommandoar med relevant historikk (spesielt dei som kunne
  forvekslast med å vere batcha, t.d. `convert-rdf`) er eksplisitt nemnde.
- Ingen påstandar i den nye seksjonen som ikkje er verifiserte direkte mot
  koden i `make/*.mk`.

## Utført

Ny «## Batching»-seksjon lagt til i `COMMANDS.md`, plassert mellom
«## Logging» og «## Wrapper-target».

- **Innleiing:** forklarer skiljet mellom batching (kor mange kontainarar
  som startast) og parallellisering (kor mange skjema som køyrer
  samstundes), med lenkjer til dei tre kjelde-spesifikasjonane i
  `specs/done/` for djupare målingar/grunngjeving (DRY — ikkje dupliserte
  detaljane herifrå).
- **Tabell «Batcha kommandoar»:** 13 rader, éi per kommando/kommandogruppe
  som nyttar batching, med kort skildring av mekanismen (script/makro,
  tal fasar) — verifisert direkte mot `make/10-generator-macros.mk`,
  `make/11-generator-targets.mk`, `make/30-instances.mk`,
  `make/40-validation.mk` og `Makefile`.
- **Tabell «Ikkje batcha»:** 6 rader som eksplisitt dokumenterer kommandoar
  som *kunne* sjå ut som batcha (t.d. `convert-rdf`, som har ein batcha
  test-intern parallell i `batch-convert.py` som ikkje er kopla til det
  faktiske make-målet) eller som medvite er utelatne (`gen-xsd`,
  asyncapi-valideringsfasen) — grunngjeving verifisert mot kommentarane i
  `make/10-generator-macros.mk` og direkte lesing av `Makefile`-oppskriftene
  for `convert-rdf`/`convert-data`/`validate-examples`.

**Verifisert:** alle påstandar i begge tabellane kryssjekka direkte mot
gjeldande kode (ikkje mot spec-tekst åleine) — `make/10-generator-macros.mk`
sine makro-definisjonar, `make/11-generator-targets.mk` sin
`make_gen_target`-generator, `make/30-instances.mk` sin
`run_gen_informasjonsmodell_instance_parallel`, `make/40-validation.mk` sine
`validate`/`lint`/`validate-bronze`/`validate-data`/`validate-examples`-mål,
og `Makefile` sine `convert-rdf`/`convert-data`/`test`/`roundtrip`-mål.
Ingen kodeendring gjort — reint dokumentasjonstillegg.

### Revidert (same dag, oppfølging)

Brukaren peika på at den fyrste versjonen braut DRY-prinsippet:
kvar kommando vart no dokumentert **to gonger** — éin gong i sin
eksisterande tabell (§ Validering / § Generering av artefakter /
§ Vedlikehald) og éin gong til i dei nye «Batcha kommandoar»/
«Ikkje batcha»-tabellane. Retta ved å:

- Fjerne dei to separate tabellane frå «## Batching»-seksjonen, behalde
  berre den konseptuelle innleiinga (kva batching er, skiljet mot
  parallellisering, lenkjer til kjelde-spesifikasjonane).
- Leggje til ei ny **«Batching»-kolonne** i dei tre eksisterande tabellane
  der kvar kommando alt var dokumentert («Validering», «Enkeltartefakter»
  under «Generering av artefakter», «Vedlikehald»), med same innhald
  (mekanisme eller grunngjeving) som før, berre flytta inn i kommandoen
  sin eigen rad i staden for ei duplisert rad i ein eigen tabell.
- Lagt til éi kort tilvisings-setning i «Per domene»-avsnittet (før
  domain-*-tabellen) som peikar til «Batching»-kolonna i
  «Enkeltartefakter»-tabellen, i staden for å duplisere dei same 13
  kommandoradene ein tredje gong for domain-*-varianten.

Kvar kommando er no dokumentert nøyaktig éin gong i `COMMANDS.md`.

### Retta feil (same dag, brukarspørsmål)

Brukaren spurde om `domain-*`-kommandoane har batching. Svar: `domain-*`
er sjølv **ikkje** ei batch-operasjon — han er ein fase-parallell
orkestrator (`run-domain-pipeline.sh`) som kallar kvart delsteg som eit
rekursivt `$(MAKE) <target> DOMAIN=<domain>`-kall til eit alt batcha
target. Under denne oppfølginga vart det oppdaga at «Per domene»-avsnittet
sitt steg 3 ("Eksempelkonvertering") **ikkje** brukar `convert-rdf`
(som COMMANDS.md alt korrekt dokumenterte som ikkje-batcha), men eit
eige, batcha target — `gen-linkml-convert` (`make/20-domain-targets.mk`,
`batch-generate-instances.py --generator convert --jobs-tsv`) — som ikkje
var dokumentert nokon stad i `COMMANDS.md`.

Retta:
- «Per domene»-avsnittet: presiserer no at `domain-*` sjølv ikkje batchar,
  berre delegerer til alt batcha steg, og at han ikkje batchar på tvers
  av domene.
- Steg 3 sin skildring viser no til `gen-linkml-convert` ved namn.
- Ny rad i «Enkeltartefakter»-tabellen for `gen-linkml-convert`, markert
  Batcha, med eksplisitt notat om at han **ikkje** er same implementasjon
  som `convert-rdf` (som framleis er korrekt dokumentert som ikkje-batcha).
- `convert-rdf`-rada oppdatert med tilsvarande kryssreferanse, for å hindre
  at dei to vert forveksla.

Status: ferdig.
