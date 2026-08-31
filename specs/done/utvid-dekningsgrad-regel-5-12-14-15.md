# Utvid dekningsgrad: Digdir-regel 5, 12, 14 og 15

## Bakgrunn

`src/mcp-linkml-validator/policies/README.md` § «Digdir-reglar og FAIR-prinsipp —
dekningsgrad» markerer i dag fire reglar som *«Ikkje evaluert»*:

| # | Regel | Noverande tekst i «Dekt av» |
|---|---|---|
| 5 | Visualisering | ER-diagram vert generert av `make erdiagram`, men ikkje validert |
| 12 | Sammenhenger mellom modeller | Dokumenterast manuelt via `er_profil_av`, `erstatter` o.l. i modellkatalogen |
| 14 | Gjenbruk | Best practice, ikkje maskinelt sjekkbart |
| 15 | Standardiserte datatyper | LinkML arvar XSD-typar via `linkml:types` |

Brukaren har bede om konkrete forslag til korleis desse kan evaluerast — anten som
policy-sjekkar i `mcp-linkml-validator` (bronse/sølv/gull) eller som ein
**modellanalyse-jobb** (jf. det eksisterande, ikkje-CI-blokkerande mønsteret i
`make/91-modell-analyse.mk` + `.github/workflows/modell-analyse.yml`, som allereie
dekkjer liknande-navn-analyse, ubrukte lokale definisjonar og IRI-dereferering).

Denne specen er ei **rein forslags-/kartleggingsoppgåve** — ingen kode er endra.
Handlingslista under er forslag til framtidig implementasjon, ikkje utført arbeid.

## Avklaringar (stadfesta av brukaren)

1. **14a — `must_import`-verdi:** `dqv-ap-no-schema` (ikkje `dqv-core-schema`).
2. **Alvorsgrad på gull:** alle tre nye åtvaringar (5, 14a, 15) skal — i tråd med det
   generelle mønsteret elles i `gold.yaml` — oppgraderast til `error` på gullnivå.
3. **Rapport-granularitet for 12/14b:** modellanalyse-jobbane skal berre rapportere
   **avvik**, ikkje ei full liste over alle skjema (same stil som
   `find-similar-names.py`).

## Relevant eksisterande infrastruktur (funn)

Kartlegginga avdekte fire mekanismar som gjer forslaga under billegare å implementere
enn dei kunne sett ut som ved fyrste augekast:

1. **`_check_schema_imports` (server.py:430)** — eksisterande, generisk sjekk-type
   (`check: schema_imports`) brukt i dag av `felles-begrepskatalog.yaml` og
   `felles-datakatalog.yaml`. Tek `must_import` (strengmatch mot skjemaets eigne
   `imports:`-linjer) og valfri `characteristic_class` (fallback: sjekkar om
   `SchemaView.get_class(...)` finn klassen — dette fangar **transitive** importar,
   sidan `SchemaView` løyser heile importgrafen uavhengig av om treffet står i
   skjemaets eiga `imports:`-liste). Gjenbrukbar direkte for regel 14.
2. **`mermaid-render`-jobben i `.github/workflows/lenkje-og-mermaid-sjekk.yml`**
   (linje 163-268) — trekk alt ut kvar ```mermaid-blokk frå genererte `.md`-sider
   (inkludert ER-diagram) og rendrar dei med `mermaid-cli` nattleg. Dette **dekkjer
   allereie** «er det genererte ER-diagrammet syntaktisk gyldig?» for skjema med
   publisert dokumentasjon — regel 5 er difor ikkje heilt uevaluert i dag, berre
   `erdiagram: true`-flagget i `build.yaml` manglar ein eigen sjekk.
3. **`build_dependency_graph` i `mkdocs/publish.sh`** (linje 174-199, jf.
   `specs/done/avhengighetstre-index.md`) — les `imports:` per skjema og byggjer
   direkte + transitivt avhengigheitstre, brukt i dag til `index.md`. Same logikk
   er det naturlege utgangspunktet for regel 12 og regel 14b sin importgraf-analyse.
4. **`make/91-modell-analyse.mk` + `summarise-modell-analyse.py`** — det etablerte
   mønsteret for informative, aldri-CI-blokkerande rapportar (job summary + artefakt,
   vekentleg cron, konsolidert i `analyse-sammendrag`). Nye jobbar skal følgje dette
   mønsteret, ikkje leggjast til som feilande policy-sjekkar.

## Forslag per regel

### Regel 5 — Visualisering

**To delar, begge i validatoren (bronse-nivå):**

1. Ny sjekk `schema_har_erdiagram_aktivert`: gitt `schema_path` (tilgjengeleg i
   `validate_schema()`, jf. `make mcp-linkml-valider-modell` som alltid kallar med
   `schemaPath`), les sysken-fila `build.yaml` i same katalog og verifiser
   `generators.erdiagram: true`. Severity **warning** på bronse (matchar mønsteret
   til andre build.yaml-gata generator-sjekkar, t.d. `class_count_limit`).
   - **Teknisk merknad:** dagens sjekk-funksjonar tek signaturen
     `(sv, schema, config, issues)` — ingen har tilgang til `schema_path`. Legg til
     som eit eige steg i `validate_schema()` (ikkje via den generiske
     `_run_checks`-løkka), sidan denne sjekken krev filsystemtilgang utover sjølve
     skjemaobjektet. Hopp over sjekken heilt (ikkje varsel) når validatoren er kalla
     med berre `schemaText` (ingen `schema_path` → ingen `build.yaml` å lese).
2. **Ingen ny kode for sjølve diagram-gyldigheita** — `mermaid-render`-jobben (funn 2
   over) dekkjer alt dette nattleg for alle skjema med publisert dokumentasjon.
   Oppdater berre teksten i README slik at dekninga vert synleg (sjå «Oppdatering av
   README.md» under).
3. **Gull:** legg til same sjekk i `gold.yaml` med `severity: error` (jf. mønsteret
   der gull oppgraderer arva åtvaringar — sjå «Avklaringar» punkt 2).

### Regel 12 — Sammenhenger mellom modellar

**Forslag: ny modellanalyse-jobb**, ikkje ein validator-policy-sjekk — sidan dette er
ei kryss-skjema/kryss-katalog-samanlikning, ikkje eit enkeltskjema-krav.

`er_profil_av`, `erstatter`, `er_erstattet_av`, `har_del`, `er_i_samsvar_med` er
alt definerte som slots på `Informasjonsmodell`-klassen i
`modelldcat-katalog-schema.yaml`, og populerte per organisasjon i
modellkatalog-datafiler (t.d. `src/linkml/modellkatalog/digdir-modellkatalog/data/...`)
generert via `make gen-informasjonsmodell-instance` / `make gen-modellkatalog-instance`.

**Nytt script** `src/assets/scripts/makefile/check-model-relationships.py`:

1. Bygg importgrafen for alle domeneskjema (gjenbruk logikken frå
   `build_dependency_graph` i `mkdocs/publish.sh`, eller porter ho til Python —
   vurder om dette bikkar DRY-terskelen på 3 samtidige implementasjonar; per no
   finst logikken berre éin stad, så ei rein Python-standalone-utgåve er også
   akseptabelt).
2. Les aggregerte `Informasjonsmodell`-instansar frå modellkatalogane og hent ut
   `er_profil_av`/`har_del`/`er_i_samsvar_med`/`erstatter`/`er_erstattet_av`
   per modell.
3. Rapporter **berre avvik** (informativt, aldri feil — jf. «Avklaringar» punkt 3;
   skjema som alt følgjer mønsteret skal ikkje takast med, same stil som
   `find-similar-names.py`):
   - Skjema som importerer eit anna domeneskjema strukturelt (t.d. `dcat-ap-no`),
     men der tilhøyrande `Informasjonsmodell`-instans **ikkje** har nokon
     `har_del`/`er_i_samsvar_med`/`er_profil_av`-verdi som peikar mot det
     importerte skjemaet — eit dokumentasjonsgap mellom kode og katalog.
   - `erstatter`/`er_erstattet_av`-par som ikkje er gjensidige (A seier `erstatter:
     B`, men B manglar tilsvarande `er_erstattet_av: A`).
4. Nytt make-target `analyse-modell-sammenhenger` i `make/91-modell-analyse.mk`,
   ny jobb i `.github/workflows/modell-analyse.yml` (same mønster som dei fem
   eksisterande: job summary + artefakt, vekentleg cron, `continue-on-error`).
   Legg til i `CHECKS`-lista i `summarise-modell-analyse.py`.

### Regel 14 — Gjenbruk

To heilt ulike sjekk-mekanismar, éin per konkret eksempel brukaren nemnde:

**14a — `dqv-ap-no`/`dqv-core` for sølv/gull (validator-sjekk, låg kostnad):**

Legg til i `silver.yaml` (arva av `gold`):

```yaml
schema_importerer_dqv_ap_no:
  severity: warning
  description: >
    Skjemaet bør importere dqv-ap-no-schema (direkte eller transitivt) for å
    gjenbruke kvalitetsvokabularet (Kvalitetsmaal, Kvalitetsmaaling,
    Kvalitetsdimensjon, Kvalitetsmerknad) i staden for å definere eigne
    tilsvarande klassar/slots. Digdir-regel 14: Gjenbruk.
  check: schema_imports
  must_import: dqv-ap-no-schema
  characteristic_class: Kvalitetsmaal
  digdir_rule: 14
  fair_principle: I3
```

**Viktig teknisk presisering:** DQV-kjerneklassane (`Kvalitetsmaal`,
`Kvalitetsmaaling` m.fl.) er definerte i `dqv-core-schema.yaml`, importert
**transitivt** via `dcat-ap-no-schema` (`dcat-ap-no-schema.yaml:39`) — dei fleste
sølv-/gull-skjema vil difor **aldri** ha den bokstavelege strengen
`dqv-ap-no-schema` (eller `dqv-core-schema`) i si eiga `imports:`-liste, berre
`dcat-ap-no-schema`. Den direkte strengsjekken i `_check_schema_imports` vil difor
nesten alltid feile *åleine*. Det er `characteristic_class: Kvalitetsmaal`-fallbacken
som gjer den faktiske jobben her — `SchemaView.get_class("Kvalitetsmaal")` løyser
heile importgrafen og finn klassen sjølv om ho kjem inn via to importnivå. Dette er
same mønster som allereie fungerer for `felles-datakatalog.yaml`. Sjekken er difor
reell og korrekt, men **verdien av `must_import`-feltet er i praksis kosmetisk** for
dei fleste skjema. Stadfesta (sjå «Avklaringar» punkt 1): `must_import: dqv-ap-no-schema`
skal brukast, ikkje `dqv-core-schema`.

**Gull:** legg til same sjekk i `gold.yaml` med `severity: error` (sjå «Avklaringar»
punkt 2).

**14b — `common-ap-no-schema` for `ap-no/*`-domenet (modellanalyse-jobb):**

Dette er eit **arkitektonisk**, katalog-avgrensa krav (jf. PRINCIPLES.md § 3 og
CLAUDE.md: AP-NO-**profilane** — `dcat-ap-no`, `cpsv-ap-no`, `dqv-ap-no`,
`skos-ap-no` m.fl. — skal importere `common-ap-no-schema`; **domenemodellar**
skal importere ein AP-NO-profil, ikkje `common-ap-no-schema` direkte). Dette
gjeld altså éin bestemt katalog (`src/linkml/ap-no/*`), ikkje alle skjema som
vel ein gitt policy-nivå — difor passar det dårleg som ein generell
bronse/sølv/gull-sjekk, og betre som ein målretta modellanalyse-jobb:

Nytt script `src/assets/scripts/makefile/check-ap-no-reuse.py`:

1. For kvart skjema under `src/linkml/ap-no/*/*-schema.yaml` (unnateke
   `common-ap-no-schema` sjølv): verifiser at `common-ap-no-schema` finst i
   importgrafen (direkte eller transitivt — gjenbruk same importgraf-logikk som
   14a/regel 12).
2. **Bonus-sjekk (arkitekturdrift):** flagg skjema **utanfor** `ap-no/*` som
   importerer `common-ap-no-schema` **direkte** i staden for via ein AP-NO-profil
   — eit brot på pull/lenking-prinsippet dokumentert i PRINCIPLES.md § 3.
3. Rapporter **berre avvik** (jf. «Avklaringar» punkt 3) — skjema som alt
   importerer korrekt, skal ikkje takast med i rapporten.
4. Nytt make-target `analyse-ap-no-gjenbruk`, ny jobb i `modell-analyse.yml`,
   lagt til i `summarise-modell-analyse.py` sin `CHECKS`-liste — same mønster
   som 12.

### Regel 15 — Standardiserte datatyper

**Forslag: ny validator-sjekk (bronse-nivå).** Kartlegginga stadfesta at lokale
`types:`-blokker i repoet allereie konsekvent oppgjev `uri:` mot eit
standardnamnerom, t.d. i `common-ap-no-schema.yaml`:

```yaml
types:
  LangString:
    uri: rdf:langString
  NonNegativeInteger:
    uri: xsd:nonNegativeInteger
```

Dette er eit reelt, maskinsjekkbart mønster — men det er per no ein **konvensjon**,
ikkje ein handheva regel. Ny sjekk `local_types_have_standard_uri`:

- For kvar lokalt definert type under skjemaets eiga `types:`-blokk (**ikkje**
  arva/importerte typar frå `linkml:types` sjølv — dei er allereie garantert XSD-
  mappa av LinkML-modellen): krev at `uri:` er sett, og at verdien (etter
  prefiks-oppløysing via skjemaets `prefixes:`) startar med eitt av dei kjende
  standardnamneromma: `xsd:`/`http://www.w3.org/2001/XMLSchema#`,
  `rdf:`/`http://www.w3.org/1999/02/22-rdf-syntax-ns#`,
  `rdfs:`/`http://www.w3.org/2000/01/rdf-schema#`, `owl:`/`http://www.w3.org/2002/07/owl#`.
- Severity **warning** på bronse (dei fleste skjema definerer ingen lokale typar i
  det heile, så sjekken vil sjeldan slå ut — men gjev verdi når han gjer det).
- `digdir_rule: 15`, `fair_principle: I1`.
- **Gull:** legg til same sjekk i `gold.yaml` med `severity: error` (sjå
  «Avklaringar» punkt 2).

## Oppdatering av README.md

Etter implementasjon, oppdater `src/mcp-linkml-validator/policies/README.md`:

- Dekningsgrad-tabellen (rad 5, 12, 14, 15) — byt ut *«Ikkje evaluert»*-teksten med
  tilvising til dei nye sjekkane/jobbane (same format som andre rader,
  t.d. `Bronze: schema_har_erdiagram_aktivert (warning) — sjølve diagram-gyldigheita
  dekt av nattleg mermaid-render-jobb i lenkje-og-mermaid-sjekk.yml`).
- «Merk»-avsnittet rett under tabellen (linje 30-31) — presiser at regel 12 og 14b
  no er *delvis* dekt via informative modellanalyse-jobbar (aldri CI-blokkerande),
  medan 5, 14a og 15 er dekte via bronse/sølv-policysjekkar.
- Legg dei to nye sjekkane til i bronse-/sølv-tabellane (§ «Kvalitetspolicyer»).
- Legg dei to nye modellanalyse-jobbane til i `COMMANDS.md` § «Modell-analyse»
  (same stad som dei fem eksisterande `analyse-*`-targeta er dokumenterte).

## Steg

1. Implementer `schema_har_erdiagram_aktivert` i `bronze.yaml` (warning) + `gold.yaml`
   (error) og tilhøyrande sjekk-kode i `server.py` — regel 5.
2. Implementer `schema_importerer_dqv_ap_no` (`must_import: dqv-ap-no-schema`,
   `characteristic_class: Kvalitetsmaal`) i `silver.yaml` (warning) + `gold.yaml`
   (error) — reint YAML, ingen ny Python-kode (gjenbruk av eksisterande
   `schema_imports`-sjekktype) — regel 14a.
3. Implementer `local_types_have_standard_uri` i `bronze.yaml` (warning) +
   `gold.yaml` (error) og tilhøyrande sjekk-kode i `server.py` — regel 15.
4. Skriv `check-model-relationships.py` (berre-avvik-rapport), nytt make-target
   `analyse-modell-sammenhenger`, ny jobb i `modell-analyse.yml`, oppdater
   `summarise-modell-analyse.py` — regel 12.
5. Skriv `check-ap-no-reuse.py` (berre-avvik-rapport), nytt make-target
   `analyse-ap-no-gjenbruk`, ny jobb i `modell-analyse.yml`, oppdater
   `summarise-modell-analyse.py` — regel 14b.
6. Oppdater `policies/README.md` (dekningsgrad-tabell, «Merk»-avsnitt,
   bronse-/sølv-/gull-tabellane) og `COMMANDS.md` § «Modell-analyse».
7. `actionlint` mot `modell-analyse.yml` etter steg 4/5 (obligatorisk per CLAUDE.md).
8. Verifiser: `make mcp-linkml-valider-modell SCHEMA=... POLICY=bronze/silver/gold`
   mot minst eitt skjema med og eitt utan kvart av dei nye avvika (inkl. at gull
   faktisk gjev `error`, ikkje `warning`); lokal køyring av
   `make analyse-modell-sammenhenger` og `make analyse-ap-no-gjenbruk` som
   stadfestar at berre avvik vert lista.

## Handlingsliste

- [x] Steg 1: `schema_har_erdiagram_aktivert` (bronse+gull) (regel 5)
- [x] Steg 2: `schema_importerer_dqv_ap_no` (sølv+gull) (regel 14a)
- [x] Steg 3: `local_types_have_standard_uri` (bronse+gull) (regel 15)
- [x] Steg 4: `analyse-modell-sammenhenger` (regel 12)
- [x] Steg 5: `analyse-ap-no-gjenbruk` (regel 14b)
- [x] Steg 6: Oppdater `policies/README.md` + `COMMANDS.md`
- [x] Steg 7: `actionlint`
- [x] Steg 8: Lokal verifisering

## Utført

**Dato:** 2026-08-31

Alle åtte steg gjennomførte som planlagt.

- **server.py:** to nye sjekkfunksjonar (`_check_local_types_have_standard_uri`,
  `_check_build_yaml_generator_flag`) og éin ny spesialhandtert `check`-type
  (`build_yaml_generator_flag`) i `_run_checks`, sidan denne krev `schema_path`
  utover den uniforme `(sv, schema, config, issues)`-signaturen. `_run_checks`
  og kallet i `validate_schema()` oppdatert til å føre `schema_path` gjennom.
- **bronze.yaml / silver.yaml / gold.yaml:** dei tre nye sjekkane
  (`schema_har_erdiagram_aktivert`, `schema_importerer_dqv_ap_no`,
  `local_types_have_standard_uri`) lagt til med `warning` på bronse/sølv og
  `error`-duplikat på gull (jf. eksisterande mønster i gold.yaml).
- **tests/test_mcp_policies.py:** 12 nye einingstestar (positiv/negativ for
  alle tre sjekkane, på både bronse/sølv- og gull-nivå). Alle 12 er grøne.
- **check-ap-no-reuse.py / check-model-relationships.py:** nye,
  sjølvstendige script (rein `pyyaml`, ingen LinkML-runtime), verifiserte
  lokalt både direkte (`python3 ...`) og via `make analyse-ap-no-gjenbruk`/
  `make analyse-modell-sammenhenger`.
- **make/91-modell-analyse.mk, .github/workflows/modell-analyse.yml,
  summarise-modell-analyse.py:** to nye make-target, to nye jobbar (same
  mønster som dei eksisterande — job summary + artefakt, aldri CI-feilande),
  og sammendrag-scriptet utvida med ein ny `avvik`-parsartype (gjenbrukbar
  for begge dei nye rapportane sitt `**Totalt: N avvik funne av M sjekka.**`-
  format). `actionlint` køyrt mot `modell-analyse.yml` — ingen funn.
- **policies/README.md + COMMANDS.md:** dekningsgrad-tabellen (rad 5, 12, 14,
  15), «Merk»-avsnittet, nivå-tabellen (Digdir-reglar per nivå) og bronse-/
  sølv-/gull-sjekktabellane oppdaterte. Dei to nye `analyse-*`-måla
  dokumenterte i `COMMANDS.md` § «Modell-analyse».

**Verifisering:**

- `make mcp-linkml-valider-modell-test`: 39/40 testar grøne. Den eine
  feilen (`TestGold.test_gyldig_skjema_har_ingen_feil`, `errorCount 2 != 0`)
  er **stadfesta pre-eksisterande** (reprodusert identisk via `git stash` mot
  HEAD før denne specen) — `_GOLD_PASS`-testfixturen manglar
  `dct:accessRights`/`dcatap:applicableLegislation` på `Datasett`, urelatert
  til regel 5/12/14/15. Ikkje retta som del av denne specen (utanfor scope).
- **Regresjonssjekk mot reelle gull-skjema:** køyrde `make
  mcp-linkml-valider-modell` mot alle 11 skjema med `validation_policy: gold`
  i `build.yaml`, både før (via `git stash`) og etter endringane. Ingen av
  dei mangla `erdiagram: true`. To skjema (`ap-no/cpsv-ap-no`,
  `fair/fair-metadata`) fekk **éin ny `missing_required_import`-feil kvar**
  frå `schema_importerer_dqv_ap_no` (23→24 og 19→20 `errorCount`) — begge
  hadde alt 19-24 andre uløyste gull-feil før denne endringa, og
  `mcp-linkml-valider-modell` er ikkje kopla inn som ei CI-gate mot reelle
  skjema (kun brukt til å generere det informative
  `validation/<versjon>/<policy>.json`-loggutdraget vist i dokumentasjonen)
  — inga CI-brytande regresjon, men verdt å merke seg dersom nokon seinare
  vil bringe desse to skjema i samsvar med regel 14. Genererte
  `validation/*.json`-testfiler frå denne verifiseringa er rydda vekk att
  (ikkje del av leveransen).
- `make analyse-ap-no-gjenbruk` / `make analyse-modell-sammenhenger`: begge
  køyrer reint. Førstnemnde finn 0 avvik (arkitekturen følgjer alt mønsteret).
  Sistnemnde finn 21 avvik — venta, sidan ingen Informasjonsmodell-instansar
  i modellkatalogane per no populerer `har_del`/`er_i_samsvar_med`/
  `er_profil_av` i det heile (stadfestar at regel 12 var reelt uevaluert).
