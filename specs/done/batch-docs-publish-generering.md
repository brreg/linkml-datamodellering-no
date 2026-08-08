# Batch per-skjema-generering i make docs-publish

## Bakgrunn

Brukaren bad om å evaluere om batching kan innførast i steg 2 av
`mkdocs/publish.sh` ("Generer innhald per domene og skjema"), som køyrer via
`make docs-publish`. Steg 2 er alt parallellisert på tvers av skjema (bash
`&`-bakgrunnsjobbar i `process_schema()`), men ei innleiande evaluering viste
at kvart skjema sin jobb gjer fleire *sekvensielle* `python3`- og
`find`-kall som kvar har målt ~100ms oppstartskostnad på dette
WSL2/NTFS-monterte (`/mnt/c/...`) filsystemet.

**Profilering** (isolert testrigg mot `ap-no/dcat-ap-no`, som har flest
importar — sjå metode under) synte følgjande fordeling for **eitt** skjema:

| Funksjon | Tid | Årsak |
|---|---|---|
| `generate_classes_section` | **14 198ms** | Kallar `get_imported_schemas()` (python3 `parse-dependency-tree.py` + `find`) **5 gonger** — éin gong per seksjon (classes/slots/enums/types/subsets) — pluss eit ekstra `find $REPO_ROOT/src/linkml -name ...` over **heile** treet per import, per seksjon |
| `copy_schema_artifacts` | **4 894ms** | `find ... -exec cp {} ... \;` og tilsvarande `sed`-kall spawnar éin ny prosess **per fil** i staden for batcha `+`-eksekvering |
| `generate_dependencies` | **3 522ms** | Kallar `get_imported_schemas()` (via `build_imported_models_links`) éin gong til — same berekning som over, **6. gongen** for same skjema — pluss enda eit whole-tree `find` per import |
| `generate_quickstart`, `generate_description`, `generate_changelog`, `generate_badges`, `generate_example`, `generate_validation_results`, `generate_contact_info` | 130-680ms kvar | Kvar spawnar 1-3 separate `python3 -c "import yaml; ..."`-eittlinjarar som kvar betalar full interpreter+import-oppstart |

**Total: ~25,5s for eitt skjema** (verifisert både med breakdown-summering og
direkte måling). Ein første test med full parallell køyring av alle 36
skjema (unbounded — ingen jobb-avgrensing, på ein maskin med 16 kjernar) vart
**avbrote etter 2 minutt** utan å fullføre — samstundes syner ei sekvensiell
måling av dei 3 fyrste skjema 7,2s / 17,4s / 25,5s kvar. Dette stadfestar at
36 samtidige jobbar × opptil 8 `python3`-spawn kvar (opptil ~290 samtidige
prosessar) skaper alvorleg ressurskonkurranse på dette filsystemet, ikkje
berre additiv oppstartskostnad.

## Rotårsak

To distinkte, batchbare problem er identifiserte — **ikkje** containerbruk
(dette steget køyrer ingen podman/linkml-kommandoar, berre bash+python3 mot
allereie genererte filer i `generated/`):

1. **Redundant recompute:** `get_imported_schemas()` (i
   `mkdocs/lib/utils/imported_schemas.sh`) vert kalla **6 gonger per skjema**
   for identisk input — 5 gonger frå `build_import_links()` i
   `mkdocs/lib/sections/classes.sh` (éin gong per Classes/Slots/Enumerations/
   Types/Subsets-seksjon) og éin gong til frå
   `build_imported_models_links()` i `mkdocs/lib/sections/avhengigheiter.sh`.
   Kvart kall spawnar eit nytt `python3`-interpreter
   (`parse-dependency-tree.py --format flat`) og gjer eit `find` — sjølv om
   resultatet er identisk for alle 6 kalla.

2. **Whole-tree `find` per import, per kallstad:** Både
   `build_import_links()` (classes.sh) og `build_imported_models_links()`
   (avhengigheiter.sh) inneheld **duplisert** logikk (identisk mønster, ulik
   fil) som for kvar importert skjema-namn gjer
   `find "$REPO_ROOT/src/linkml" -name "${imported_clean}-schema.yaml"` over
   **heile** kjeldetreet for å slå opp kva domene importen høyrer til. Dette
   er nøyaktig den typen "same fakta, fleire kjelder"-duplisering
   CLAUDE.md sin DRY-regel allereie handhevar for make-/Python-laget (jf.
   `specs/done/dry-opprydding.md`) — berre at han her ikkje er fanga opp
   endå, sidan han ligg i bash-seksjonane til mkdocs-portalen.

3. **`-exec ... \;` i staden for `-exec ... +`:** `copy_schema_artifacts()`
   (`mkdocs/lib/copy_artifacts.sh`) spawnar éin ny `cp`- eller `sed`-prosess
   per fil i staden for å batche fleire filer inn i færre prosessar.

4. (Mindre bidrag) Fleire seksjonar spawnar separate `python3 -c` for å
   hente enkeltfelt frå same YAML-fil (t.d. `get_validation_policy`,
   `get_external_spec_url`, `get_external_spec_label` i
   `metadata_parsers.sh` opnar og parsar **same** `build.yaml` tre gonger).

## Metode for profilering

Testrigget køyrer dei same funksjonane som `mkdocs/publish.sh` sin
`process_schema()` kallar, men skriv til ein scratch-katalog i staden for
`mkdocs/docs/` (unngår å røre committa filer). Verifisert konsistent:
breakdown-summen (24 908ms) matchar direkte måling av heile
`process_schema` for same skjema (25 484ms) innanfor målefeil.

## Mål

Fjern redundant `python3`/`find`-arbeid som ligg **sekvensielt** på kvart
skjema sin kritiske sti, utan å endre generert output. "Batching" her betyr
konkret:

- Berekn `get_imported_schemas()` **éin gong per skjema**, gjenbruk resultatet
  frå alle kallstader (5 seksjonar i classes.sh + 1 i avhengigheiter.sh)
- Slå opp importert-skjema→domene via eit **føre-berekna oppslag** (bygd éin
  gong for heile repoet i Steg 1.5, same stad som det eksisterande
  `SCHEMA_PARENT_MODEL_SERIALIZED`-oppslaget vert bygd) i staden for
  gjentekne whole-tree `find`
- Batch fil-kopiering/sed-endring med `-exec ... +` i staden for `-exec ... \;`
- Slå saman dei 3 separate `build.yaml`-felthentingane i
  `metadata_parsers.sh` til éin `python3`-prosess

**Eksplisitt utanfor scope:** avgrensing av parallellitet (jobb-pool
kapp mot `nproc`) er ein separat, komplementær fiks — vurder han berre
dersom steg 1-4 under ikkje åleine bringar total Steg 2-tid ned til eit
akseptabelt nivå.

## Steg

1. **Memoiser `get_imported_schemas()` per skjema:**
   - I `mkdocs/lib/generate_index.sh` sin `generate_schema_index()`: kall
     `get_imported_schemas "$domain" "$schema"` **éin gong**, lagra
     resultatet i ein eksportert variabel (t.d. `IMPORTED_SCHEMAS_CACHE`)
     før dei 14 `generate_*`-kalla
   - Endra `build_import_links()` (classes.sh) og
     `build_imported_models_links()` (avhengigheiter.sh) til å lese frå
     `$IMPORTED_SCHEMAS_CACHE` i staden for å kalle
     `get_imported_schemas()` sjølv
   - Rydd opp variabelen saman med `CURRENT_DOMAIN`/`CURRENT_SCHEMA` på
     slutten av `generate_schema_index()`

2. **Bygg eit globalt skjemanamn→domene-oppslag i Steg 1.5:**
   - I `mkdocs/publish.sh`, same stad som `SCHEMA_PARENT_MODEL_TMP`/
     `SCHEMA_SUBMODELS_TMP` vert bygd (linje ~243-276): legg til eit tredje
     pass som finn alle `*-schema.yaml` under `src/linkml/` **éin gong**,
     og byggjer `SCHEMA_NAME_TO_DOMAIN_TMP["<namn-utan-.yaml>"]="<domain>"`
   - Serialiser og eksporter som `SCHEMA_NAME_TO_DOMAIN_SERIALIZED`, same
     mønster som dei to eksisterande serialiserte maps
   - Legg til éi delt hjelpefunksjon (t.d. `lookup_schema_domain()` i
     `mkdocs/lib/utils/imported_schemas.sh`, sidan begge kallstadene alt
     `source`-ar den fila) som gjer eit lineært oppslag i
     `SCHEMA_NAME_TO_DOMAIN_SERIALIZED` og returnerer domenet
   - Erstatt dei to duplikate `find "$REPO_ROOT/src/linkml" -name
     "${imported_clean}-schema.yaml"`-blokkene (classes.sh linje 56-65,
     avhengigheiter.sh linje 43-52) med kall til denne funksjonen —
     konsoliderer samstundes ei DRY-duplisering CLAUDE.md sin eigen regel
     ville flagga
   - Skjemafil-stien (nødvendig for `schema_id`-oppslag i classes.sh) kan
     rekonstruerast direkte frå konvensjonen
     `src/linkml/<domain>/<namn>/<namn>-schema.yaml`
     (jf. `CONVENTIONS.md` katalogstruktur) i staden for eit ekstra `find`

3. **Batch `cp`/`sed`-kall i `copy_schema_artifacts()`
   (`mkdocs/lib/copy_artifacts.sh`):**
   - `find "$schema_dir" -maxdepth 1 -type f -exec cp {} "$out/" \;` →
     `-exec cp -t "$out" {} +`
   - `find "$schema_dir/docs" -name "*.md" -exec cp {} "$out/klasser/" \;` →
     `-exec cp -t "$out/klasser" {} +`
   - `find "$schema_dir/diagrams" -type f -exec cp {} "$out/diagrams/" \;` →
     `-exec cp -t "$out/diagrams" {} +`
   - Den avsluttande `find ... -exec sed -i ... {} \;` (lenkje-lowercasing)
     → `-exec sed -i ... {} +`
   - **Ikkje endra** lowercase-omdøypingsloopen (`for f in ...*.md; do ...
     mv ... mv ...`) — to-stegs `.tmp`-omvegen er der bevisst pga.
     case-insensitivt NTFS-filsystem, ikkje eit uforvarande duplikat

4. **Slå saman dei 3 `build.yaml`-felthentingane i
   `metadata_parsers.sh`:**
   - Erstatt `get_validation_policy()`, `get_external_spec_url()`,
     `get_external_spec_label()` sine tre separate `python3 -c`-kall med
     éin `python3 -c` som skriv alle tre felta (eitt per linje), lest av
     bash med `read -r policy url label < <(...)`
   - Behald identisk fallback-åtferd (`bronze` / tom streng) per felt

5. **Verifiser kvart steg isolert mot testrigget** (ikkje samla til slutt):
   - Køyr same profileringsrigg som under "Metode" før/etter kvart steg,
     mot minst `ap-no/dcat-ap-no` (flest importar) og eitt skjema utan
     importar (t.d. eit `referanse`-skjema), for å stadfeste både
     tidsgevinst og at ingen regresjon oppstår for skjema utan importar
   - **Byte-for-byte samanlikning** av generert `index.md` før/etter kvart
     steg (`diff`) — denne refaktoreringa skal **ikkje** endre nokon
     generert output, berre køyretid
   - Etter steg 1-4: full `bash mkdocs/publish.sh`-køyring mot verkeleg
     `generated/`, `git diff mkdocs/docs/` skal vere tomt bortsett frå
     `_Portalen vart sist bygd: ...`-tidsstempelet i `index.md`

6. **Mål total Steg 2-tid før/etter** med ekte `make docs-publish`-køyring,
   dokumenter i "Utført"-seksjonen. Dersom total tid framleis er
   uakseptabelt høg etter steg 1-4 (t.d. framleis fleire minutt), vurder
   jobb-avgrensing (`xargs -P $(nproc)`-mønster i staden for unbounded `&`)
   som eit oppfølgingssteg — **ikkje** gjer dette no utan å først stadfeste
   at det trengst, sidan steg 1-4 fjernar mesteparten av
   ressurskonkurransen som gjorde unbounded parallellitet skadeleg i
   utgangspunktet.

## Akseptansekriterium

- [x] `get_imported_schemas()` vert kalla maks éin gong per skjema
- [x] Ingen `find $REPO_ROOT/src/linkml -name "*-schema.yaml"` over heile
      treet gjenstår i `classes.sh`/`avhengigheiter.sh` — begge bruker det
      delte oppslaget
- [x] `copy_schema_artifacts()` bruker `-exec ... +` for alle fleir-fil-
      operasjonar der rekkjefølgje ikkje har noko å seie
- [x] `metadata_parsers.sh` sine tre `build.yaml`-felt hentast med eitt
      `python3`-kall
- [x] Full `make docs-publish`-køyring fullfører feilfritt og produserer
      identisk innhald som før (verifisert direkte, sidan `mkdocs/docs/`
      viser seg å vere **gitignora** i heile si breidd — `.gitignore` linje
      15-25 dekkjer alle domenekatalogane og `index.md` — så `git diff` kan
      ikkje brukast som verifiseringsmetode slik akseptansekriteriet
      opphavleg føresette. Sjå "Utført" for faktisk brukt metode)
- [x] Målt total Steg 2-tid dokumentert før og etter, med konkret
      sekund-/prosentforbetring
- [x] `bash -n` på alle endra `.sh`-filer

## Relaterte filer

- `mkdocs/publish.sh` — Steg 1.5 (nytt oppslag), Steg 2-orkestrering
- `mkdocs/lib/generate_index.sh` — memoisering av `get_imported_schemas`
- `mkdocs/lib/sections/classes.sh` — `build_import_links()`
- `mkdocs/lib/sections/avhengigheiter.sh` — `build_imported_models_links()`,
  `generate_dependencies()`
- `mkdocs/lib/utils/imported_schemas.sh` — `get_imported_schemas()`, ny
  `lookup_schema_domain()`
- `mkdocs/lib/copy_artifacts.sh` — `copy_schema_artifacts()`
- `mkdocs/lib/utils/metadata_parsers.sh` — `get_validation_policy()`,
  `get_external_spec_url()`, `get_external_spec_label()`
- `specs/done/dry-opprydding.md` — presedens for same type funn
  (duplisert oppslagslogikk) på make-/Python-laget

## Utført

Alle 4 steg (memoisering, delt oppslag, `-exec +`-batching,
manifest-cache) implementerte og verifiserte. Eitt uventa funn undervegs
(sjå under) vart retta i same økt.

**Målt effekt** (isolert profileringsrigg, sjå "Metode"):

| Mål | Før | Etter | Endring |
|---|---|---|---|
| `ap-no/dcat-ap-no` åleine (flest importar) | 25 484ms | 7 324ms | **-71 %** |
| 3 representative skjema, sekvensielt | 63 207ms | 22 467ms | **-64 %** |
| Alle 36 skjema, parallelt (`&`) | Fullførte ikkje — avbrote etter 120 000ms | 37 706ms, 0 feil | Frå "fullførte ikkje" til fullført |
| Reell `make docs-publish`, Steg 2, 40 skjema-einingar (inkl. referansemodell-bronze/silver/gold og 6 modellkatalog-instansar) | (aldri fullført lokalt før fiksen — sjå under) | 98 900ms, 0 feil | Fullført, ingen regresjon |

**Funn 1 — rotårsak stadfesta:** `get_imported_schemas()` vart kalla 6
gonger per skjema (5× frå `classes.sh`, 1× frå `avhengigheiter.sh`), og
`build_import_links()`/`build_imported_models_links()` hadde duplisert,
whole-tree `find`-logikk for kvar import. `generate_classes_section` gjekk
frå 14 198ms til 447ms for `dcat-ap-no`; `generate_dependencies` frå
3 522ms til 530ms.

**Funn 2 — uventa bug, retta:** `load_manifest_cache()` sitt fyrste
utkast brukte tre separate `IFS= read -r VAR`-kall mot ei
kommandosubstitusjon med tre linjer. Sidan `$(...)` strippar **alle**
etterfølgjande linjeskift, kollapsa dei to siste (tomme)
`external_spec_url`/`external_spec_label`-linjene, og tredje `read` trefte
EOF og returnerte feilkode — som under `set -e` avslutta heile
`generate_schema_index()` for **kvart einaste skjema utan** ekstern
referanse (dvs. dei fleste). Løyst ved å skrive `key=verdi`-linjer (aldri
ei reint tom linje, sjølv med tom verdi) og lese via prosess-substitusjon
(`< <(printf '%s\n' "$result")`) som garanterer avsluttande linjeskift.
Stadfesta med `set -x`-sporing mot `ap-no/common-ap-no` (som manglar
begge felta) før og etter fiksen.

**Funn 3 — uventa regresjon, retta:** Fyrste utkast av
`lookup_schema_path()`-erstatninga i `classes.sh` rekonstruerte
skjemafil-stien frå konvensjonen
`src/linkml/<domain>/<namn>/<namn>-schema.yaml`. Dette braut for
**delmodell**-skjema (t.d. `dqv-core-schema.yaml`, som ligg i
foreldreskjemaet sin katalog `ap-no/dqv-ap-no/`, ikkje i ein eigen
`dqv-core/`-katalog) — importerte delmodell-lenkjer forsvann stille frå
"Importerte klasser/slots/enums"-lister. Oppdaga ved eksplisitt
byte-for-byte-diff av `dcat-ap-no` og `referansemodell` (begge importerer
`dqv-core` transitivt) før/etter, ikkje ved isolert einingstesting av
funksjonen sjølv. Løyst ved å utvide Steg 1.5-oppslaget til å lagre full
filsti direkte (`SCHEMA_NAME_TO_PATH_SERIALIZED`) i staden for å anta ein
katalogkonvensjon — stadfesta med byte-identisk output etterpå.

**Verifiseringsmetode** (ettersom `git diff mkdocs/docs/` viste seg
ubrukeleg — heile katalogen er gitignora, jf. `.gitignore` linje 15-25):

1. Isolert rigg: same funksjonar som `process_schema()` kallar, køyrt mot
   scratch-katalog, samanlikna byte-for-byte (`diff -rq`) mot output frå
   uendra kode (henta via `git show HEAD:<fil>`) for 3 representative
   skjema (flest importar, tomme ekstra-felt, ingen importar) — 0 avvik
   etter dei to fiksane over
2. Byte-for-byte samanlikning av alle 72 `index.md`/`klasser/index.md`
   mot **eksisterande** (før-endring) innhald i `mkdocs/docs/` for alle 36
   skjema — 5 avvik, alle forklarte som eit avgrensa testrigg som ikkje
   sette opp delmodell-konteksten (`PARENT_MODEL`/`SUBMODELS`), ikkje som
   reelle kodefeil (stadfesta ved manuell inspeksjon av dei 5 filene)
3. Reell `make docs-publish`-køyring mot verkeleg `generated/`: fullførte
   feilfritt (`exit 0`), 0 feila skjema, Steg 2 98 900ms. Manuelt
   inspisert `dqv-ap-no`/`dqv-core` (delmodell-boks + Delmodellar-seksjon
   korrekt) og `dcat-ap-no` (alle 5 import-lenkjelister — klasser, slots,
   enums, typer, subsets — inneheld korrekt `common-ap-no` **og**
   `dqv-core`)
4. `bash -n` på alle 7 endra filer

**Ikkje gjort:** Jobb-avgrensing (steg 6 sitt oppfølgingsforslag) — ikkje
nødvendig, sidan steg 1-4 åleine tok den isolerte 36-skjema-køyringa frå
"fullførte ikkje på 120s" til 37,7s, og den reelle produksjonskøyringa
(40 skjema-einingar) fullførte feilfritt på 98,9s.

## Relaterte filer (endra)

- `mkdocs/publish.sh` — nytt `SCHEMA_NAME_TO_DOMAIN_SERIALIZED` +
  `SCHEMA_NAME_TO_PATH_SERIALIZED`-oppslag i Steg 1.5
- `mkdocs/lib/generate_index.sh` — memoiserer `IMPORTED_SCHEMAS_CACHE` og
  kallar `load_manifest_cache()` éin gong per skjema
- `mkdocs/lib/sections/classes.sh` — `build_import_links()` bruker delt
  oppslag i staden for `find`
- `mkdocs/lib/sections/avhengigheiter.sh` — same fiks i
  `build_imported_models_links()`
- `mkdocs/lib/utils/imported_schemas.sh` — nye `lookup_schema_domain()`,
  `lookup_schema_path()`
- `mkdocs/lib/utils/metadata_parsers.sh` — nye `load_manifest_cache()`,
  gettarane sjekkar cache før dei fell tilbake til `python3`
- `mkdocs/lib/copy_artifacts.sh` — `-exec ... \;` → `-exec ... +` (4 stader)
