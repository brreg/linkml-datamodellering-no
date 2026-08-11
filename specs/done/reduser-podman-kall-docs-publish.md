# Reduser talet på podman-kall i make docs-publish

## Bakgrunn

Brukaren bad om ei vurdering av om `make docs-publish` kan
ytelsesoptimaliserast ytterlegare, utover det `specs/done/batch-docs-publish-generering.md`
(2026-08-10) allereie oppnådde (batching av `find`/`python3`-kall gav
36 skjema frå "fullførte ikkje på 120s" til 37,7s isolert, og ein reell
40-skjema-produksjonskøyring på 98,9s for sjølve Steg 2).

Undersøkinga fann at denne gevinsten sidan er **spist opp igjen av ei
seinare, ikkje-relatert endring**: `specs/done/nye-host-python-kall-batching.md`
(2026-08-09, altså same dag/rett før batching-spec-en over) containeriserte
alle `python3 -c`/heredoc-kall i `mkdocs/publish.sh`/`mkdocs/lib/` — frå eit
bart host-`python3`-kall (~80-100ms oppstart) til eit fullt
`podman run --rm ...`-kall mot `localhost/python-pytest:latest`
(`run_python_container()` i `mkdocs/lib/utils/python_container.sh`). Dette
var eit medvite, brukar-godkjent val for å halde CLAUDE.md sitt prinsipp
("Ingen avhengigheiter skal installeres lokalt... Alt skal kjøres som
containere med podman") — men spec-en si eiga "Utført"-notis dokumenterte
alt den gongen at total `make docs-publish`-tid auka til **~5m27s**, utan å
bryte ned kvifor eller vurdere om containerkalla sjølv kunne batchast ned
til færre kall (same prinsipp som `batch-docs-publish-generering.md` alt
hadde etablert for `find`/bart `python3`).

## Profilering (direkte målt, 2026-08-11)

**Kostnad per `podman run`-kall** (isolert, `localhost/python-pytest:latest`
alt pulla lokalt — ingen nettverkstrafikk):

| Kall | Tid |
|---|---|
| `podman run ... python3 -c "print('hi')"` (1) | 3,10s |
| Same (2) | 2,98s |
| Same (3) | 2,77s |
| `podman run ... true` (ingen python i det heile) | 2,61s |
| Bart host-`python3 -c "print('hi')"` (til samanlikning) | **0,08s** |

Konklusjon: **~2,6-3,1s per `podman run`-kall er nesten heilt
container-oppstartskostnad** (namespace/cgroup/overlayfs-oppsett) — ikkje
Python-interpreter-oppstart, som isolert er 80ms. Dette er ein **~30-35×**
kostnad samanlikna med det opphavlege, bare host-kallet
`batch-docs-publish-generering.md` profilerte (~100ms).

**Steg 1.5 sin sekvensielle løkke** (`mkdocs/publish.sh` linje 174-196, les
`submodels`-feltet frå kvart `build.yaml` via `run_python_container`) —
reprodusert direkte mot ekte repo-data, **ingen endring i
`mkdocs/docs/`**:

```
Processed 41 manifest files in 122s
```

Dette er **eitt** kall per `build.yaml`, køyrt **heilt sekvensielt** (ingen
`&`/`wait`, i motsetnad til Steg 2) — og skjer **før** Steg 2 sin
parallelle skjema-generering i det heile teke startar. 122 sekund er difor
rein, ubunden ventetid på kvar einaste `make docs-publish`-køyring.

## Rotårsak

To distinkte problem, begge introdusert av containeriserings-fiksen
(`228385b6`, jf. Bakgrunn), ikkje av batching-arbeidet:

1. **Steg 1.5-løkka batchar ikkje `podman run`-kalla sine**, sjølv om
   akkurat denne løkka er staden der `SCHEMA_NAME_TO_DOMAIN_SERIALIZED`/
   `SCHEMA_NAME_TO_PATH_SERIALIZED` alt vert bygd med **éin** pre-berekning
   for heile repoet (jf. `batch-docs-publish-generering.md` sitt steg 2).
   `submodels`-feltet kunne lesast med same mønster — éin container-prosess
   som les alle 41 `build.yaml`-filer, i staden for 41 separate prosessar.

2. **Steg 2 sin per-skjema-jobb gjer 4-5 separate `podman run`-kall**
   (talet varierer med om skjemaet har `annotations.utgiver`), sjølv om
   `load_manifest_cache()` (`metadata_parsers.sh`) alt demonstrerer at
   fleire YAML-felt kan hentast i **éin** prosess:

   | Kallstad | Kall | Gjeld |
   |---|---|---|
   | `metadata_parsers.sh: load_manifest_cache()` | 1 | Alle 36 skjema |
   | `kom_i_gang.sh: generate_quickstart()` | 2 (versjon + auto-deteksjon) | Alle 36 skjema |
   | `kontakt.sh: generate_contact_info()` | 1 | Alle 36 skjema |
   | `badges.sh: generate_badges()` (utgjevar-oppslag) | 1 | 26 av 36 skjema (har `annotations.utgiver`) |
   | `delmodellar.sh` (parent-title / sub-title / sub-desc) | 1-3 | Berre dei ~2 skjema som har `submodels` sett |

   Med 36 skjema × ~4,7 kall i snitt ≈ **~170 `podman run`-kall** i Steg 2
   åleine. Desse køyrer parallelt **på tvers av** skjema (36 bakgrunnsjobbar,
   som før), men **sekvensielt innanfor kvart skjema** — og fordi kvart
   kall har ~2,7s eigen container-oppstartskostnad, skaper 36 samstundes
   jobbar som kvar startar 4-5 containerar i rekkefølgje den same typen
   ressurskonkurranse (overlayfs/cgroup-manager) som `batch-docs-publish-generering.md`
   alt dokumenterte for bare prosessar — berre med tyngre einingar. Dette
   samsvarar med at total `make docs-publish`-tid (5m27s, jf. Bakgrunn) er
   monaleg meir enn 122s (Steg 1.5) + eit naivt "36 parallelle jobbar × 5
   kall × 2,7s = ~13,5s kritisk sti"-anslag for Steg 2 skulle tilseie.

**Presedens finst alt i repoet for løysinga:** akkurat same mønster
(pre-berekna, serialisert oppslag bygd éin gong i Steg 1.5, konsumert utan
vidare prosess-spawning i Steg 2) er alt implementert for
`SCHEMA_NAME_TO_DOMAIN_SERIALIZED`/`IMPORTED_SCHEMAS_CACHE`. Denne spec-en
foreslår å bruke same mønster for dei resterande `podman run`-kalla, **ikkje**
å fjerne containeriseringa (som ville bryte det etablerte prinsippet og
reversere ein medvite brukar-godkjent fiks).

## Mindre funn (sekundært, ikkje podman-relatert)

7 filer gjer framleis eit eige `find "$REPO_ROOT/src/linkml/$domain" -name
"${schema}-schema.yaml"` for **skjemaet sin eigen fil** (ikkje importerte
skjema), sjølv om `lookup_schema_path()` (`imported_schemas.sh`, bygd i
`batch-docs-publish-generering.md`) alt løyser akkurat dette oppslaget frå
det pre-berekna `SCHEMA_NAME_TO_PATH_SERIALIZED`-registeret:

- `copy_artifacts.sh`, `eksempeldatafil.sh`, `avhengigheiter.sh`,
  `kom_i_gang.sh`, `versjonslog.sh`, `om_denne_modellen.sh`,
  `imported_schemas.sh` (`get_imported_schemas()` sjølv, for gjeldande
  skjema)

Kvart kall er eit avgrensa (per-domene, ikkje heile-treet) `find`, så
kostnaden er lita (millisekund, ikkje sekund) samanlikna med
podman-funna over — men det er same type duplisert oppslag
`batch-docs-publish-generering.md` sin DRY-grunngjeving alt gjeld for,
berre ikkje fullt gjennomført til alle kallstader den gongen. Verdt å rydde
opp i same runde sidan fila/mønsteret uansett vert rørt.

## Mål

- Steg 1.5 sin `submodels`-oppslag: **1** container-kall for alle 41
  `build.yaml`-filer (i staden for 41).
- Steg 2 sin per-skjema-metadata (versjon, `build.yaml`-felt, CODEOWNERS-
  oppslag, quickstart-auto-deteksjon): **1** container-kall for **alle**
  36 skjema, pre-berekna i Steg 1.5 (same stad/mønster som
  `SCHEMA_NAME_TO_DOMAIN_SERIALIZED`), **0** container-kall attverande i
  Steg 2 sine parallelle jobbar.
- Netto: frå **~211 `podman run`-kall** (41 + ~170) til **2** for heile
  `make docs-publish`.
- Alle 6 `find`-duplikatane i "Mindre funn" bytt til `lookup_schema_path()`.
- Ingen endring i generert `mkdocs/docs/`-innhald (byte-for-byte identisk,
  same verifiseringsmetode som `batch-docs-publish-generering.md`).

## Steg

1. **Design éitt samla Python-script**
   (`mkdocs/lib/scripts/collect-schema-metadata.py`, stdlib +
   `PyYAML` — køyrer i `python-pytest`-kontaineren via
   `run_python_container`) som for **alle** skjema i repoet i éin prosess:
   - Les kvart `build.yaml`: `validation_policy`, `external_spec_url`,
     `external_spec_label`, `submodels`
   - Les kvart `*-schema.yaml`: `version`, `title`/`name`, `description`
     (fyrste setning), container-klasse + auto-deteksjon av
     eksempel-klasse/-variabel (same logikk som heredocen i
     `kom_i_gang.sh` i dag)
   - Les `CODEOWNERS.md` éin gong, matchar kvart skjema sin `schema_path`/
     `catalog_slug` mot `path_patterns`/`org_uri` (same logikk som
     `badges.sh`/`kontakt.sh` sine heredocar i dag)
   - Skriv éin samla JSON/TSV-blob til stdout, éin rad per skjemanamn

2. **Kall scriptet éin gong i Steg 1.5** (`mkdocs/publish.sh`, same stad
   som `SCHEMA_NAME_TO_DOMAIN_SERIALIZED` vert bygd), lagra resultatet i
   ein ny serialisert env-variabel (t.d. `SCHEMA_METADATA_SERIALIZED`) og
   eksporter til subshells, same mønster som dei eksisterande registera.

3. **Erstatt alle 5 kallstadene i Steg 2** (`metadata_parsers.sh`,
   `kom_i_gang.sh`, `badges.sh`, `kontakt.sh`, `delmodellar.sh`) med
   oppslag mot `SCHEMA_METADATA_SERIALIZED` (ny hjelpefunksjon,
   t.d. `lookup_schema_metadata()` i `imported_schemas.sh` eller ei ny
   delt fil) i staden for eigne `run_python_container`-kall. Behald same
   fallback-/ÅTVARING-semantikk som i dag for manglande felt.

4. **Erstatt Steg 1.5-løkka sitt `submodels`-oppslag** med oppslag mot
   same `SCHEMA_METADATA_SERIALIZED`-register — fjernar den sekvensielle
   41-kalls-løkka heilt.

5. **Rett dei 6 `find`-duplikatane** i "Mindre funn" til å bruke
   `lookup_schema_path()`.

6. **Verifiser byte-for-byte identisk output** — same metode som
   `batch-docs-publish-generering.md`: isolert rigg + full
   `make docs-publish`-køyring, samanlikna mot **eksisterande**
   `mkdocs/docs/`-innhald før endringa (hugs: `mkdocs/docs/` er gitignora,
   så bruk direkte fil-samanlikning, ikkje `git diff`).

7. **Mål total `make docs-publish`-tid før/etter**, dokumenter i
   "Utført". Dersom Steg 2 framleis syner reell ressurskonkurranse etter
   at podman-kall-talet er kutta til 2 totalt (usannsynleg, men vurder
   dersom målt tid framleis er uventa høg), vurder om dei 36 parallelle
   `process_schema`-jobbane treng jobb-avgrensing — men **berre** som
   oppfølging, ikkje no, sidan hovudfunnet er talet på containerstartar,
   ikkje sjølve parallelliteten.

## Akseptansekriterium

- [x] `mkdocs/lib/scripts/collect-schema-metadata.py` finst, testa isolert
      mot fire representative skjema (med/utan `annotations.utgiver`,
      med/utan `submodels`, med/utan manifest, delmodell-skjema med avvikande
      quickstart-policy) — verifisert mot faktiske funksjonar i
      `metadata_parsers.sh`/`kom_i_gang.sh` før dei vart endra
- [x] Talet på `podman run`-kall i `make docs-publish` er redusert frå
      ~211 til **1** (betre enn måltalet på 2 — org-oppslag og
      submodels-oppslag vart konsoliderte inn i det same kallet, verifisert
      med `grep -c run_python_container` over heile `mkdocs/`)
- [x] Alle 7 (ikkje 6, jf. korrigering i "Mindre funn") `find
      "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml"`
      -duplikata for gjeldande skjema er bytt til `lookup_schema_path()`
- [x] Full `make docs-publish`-køyring: identisk generert innhald i
      `mkdocs/docs/` for alle 9 domene/40 skjema-einingar (byte-for-byte,
      `diff -rq` mot ein fersk "før"-basislinje frå uendra kode via
      `git stash` — 0 avvik av 6261 filer utanom det kjende
      tidsstempel-unntaket)
- [x] Total køyretid målt før og etter, dokumentert med konkret
      sekund-/prosentforbetring: 6m31,9s → 2m29,2s (**-62 %**). Målet
      "under 1 minutt" frå den opphavlege, kontensjonsfrie estimeringa vart
      **ikkje** nådd — sjå "Utført" for kvifor (FS-kontensjon i Steg 2,
      ikkje podman, er attverande flaskehals)
- [x] `bash -n` på alle 13 endra/nye `.sh`-filer, `python3 -m py_compile`
      på det nye scriptet — alle bestod

## Relaterte filer

- `mkdocs/publish.sh` — Steg 1.5 (nytt samla metadata-oppslag, fjern
  `submodels`-løkka)
- `mkdocs/lib/scripts/collect-schema-metadata.py` — nytt script
- `mkdocs/lib/utils/python_container.sh` — `run_python_container()`,
  uendra, men talet på kallstader som brukar han går kraftig ned
- `mkdocs/lib/utils/metadata_parsers.sh` — `load_manifest_cache()` les frå
  nytt register i staden for eige `podman run`
- `mkdocs/lib/sections/kom_i_gang.sh`, `badges.sh`, `kontakt.sh`,
  `delmodellar.sh` — same endring
- `mkdocs/lib/copy_artifacts.sh`, `sections/eksempeldatafil.sh`,
  `sections/versjonslog.sh`, `sections/om_denne_modellen.sh`,
  `sections/avhengigheiter.sh`, `utils/imported_schemas.sh` —
  `find` → `lookup_schema_path()`
- `specs/done/batch-docs-publish-generering.md` — presedens for
  pre-berekna/serialiserte oppslag i Steg 1.5
- `specs/done/nye-host-python-kall-batching.md` — spec-en som introduserte
  regresjonen (medvite, for å halde containeriserings-prinsippet — denne
  spec-en reverserer **ikkje** det valet, berre talet på kall)

## Utført

Alle 7 steg gjennomførte. Full `bash -n`/`py_compile`-sjekk av alle 13
endra/nye filer bestod utan feil.

**Design-avvik frå opphavleg plan (steg 1):** i staden for at
`collect-schema-metadata.py` sjølv walkar `src/linkml/` for å finne
domain/schema-para, bygg publish.sh sin **Steg 1.4** (ny — flytta ut av det
som før var Steg 2) `ALL_DOMAINS`/`DOMAIN_SCHEMA_LIST` frå `generated/`
**før** Steg 1.5, og Steg 1.5 sender domain/schema/schema_file/manifest som
strukturert stdin-input til scriptet. Dette unngår at scriptet må
gjenskape Steg 2 sin dedup-logikk (`*-schema`-katalogar) sjølv, og held
domain/schema-enumereringa på **éin** stad i kodebasen.

**Ein pre-eksisterande inkonsistens vart medvite bevart, ikkje fiksa:** for
delmodell-skjema (t.d. `dqv-core`, som deler `build.yaml` med
foreldreskjemaet sitt katalog) las `kom_i_gang.sh` sin quickstart-seksjon
validation_policy frå schema-fila **sin eigen katalog** sitt `build.yaml`
(→ "gold" for dqv-core, arva frå dqv-ap-no), medan
`metadata_parsers.sh`/badges brukte den **konstruerte**
`src/linkml/<domain>/<schema>/build.yaml`-stien (→ "bronze", sidan
`ap-no/dqv-core/build.yaml` ikkje finst). Dette gav alt før denne
refaktoreringa eit motstridande badge/quickstart-par på dqv-core sin
publiserte side. Halde ved like byte-for-byte via eit eige
`quickstart_policy`-felt i scriptet sin output, i staden for å konsolidere
det inn i det generelle `policy`-feltet (som ville endra generert output).

**Verifisert korrektheit** (ikkje berre isolert, men mot heile
produksjonspipelinen):
1. `git stash` av alle endringar, `make docs-publish` køyrt med **uendra**
   kode for å etablere ein fersk "før"-basislinje (40 skjema-einingar i
   dagens `generated/`), snapshot av heile `mkdocs/docs/` (6261 filer)
2. Endringane gjenoppretta, `make docs-publish` køyrt på nytt med den nye
   koden
3. `diff -rq` mellom dei to `mkdocs/docs/`-snapshotta: **0 avvik** av 6261
   filer, bortsett frå den forventa `_Portalen vart sist bygd: ...`
   -tidsstempellinja i topp-`index.md` (same, kjende unntak som
   `batch-docs-publish-generering.md` dokumenterte)
4. Stikkprøve på `ap-no/dqv-core/index.md` stadfesta at
   badge/quickstart-inkonsistensen (over) er identisk bevart
5. `grep -c run_python_container` over heile `mkdocs/`: **éin** kallstad
   att (Steg 1.5 sitt samla kall) — ned frå dei opphavleg dokumenterte
   ~211

**Målt tid** (same maskin, rett etter kvarandre, ingen andre endringar):

| Køyring | Steg 1 | Steg 1.4+1.5 (gap) | Steg 2 | Totalt (`make docs-publish`) |
|---|---|---|---|---|
| Før (uendra kode, 40 skjema-einingar) | 14,8s | ~184s | 192,7s | **6m31,9s** |
| Etter (denne spec-en) | 14,2s | ~24,9s | 110,1s | **2m29,2s** |
| Endring | ≈0 | **-159s (-86 %)** | **-83s (-43 %)** | **-242s (-62 %)** |

Steg 1.4+1.5-gevinsten (~184s → ~25s) stadfestar hovudfunnet direkte: den
sekvensielle 41-kalls `podman run`-løkka var hovudkostnaden der, no éin
container-prosess. Steg 2-gevinsten (43 %, ikkje dei ~99 % ein naiv
"eliminert 170 podman-kall"-rekning skulle tilseie) skuldast at Steg 2 sin
resterande køyretid i hovudsak er **filsystem-I/O på det WSL2/NTFS-monterte
repoet** (40 parallelle jobbar som kvar gjer `find`/`cp`/`mkdir` — stadfesta
av at `sys`-tid frå `time`-målinga oversteig `real`-tid i begge køyringar),
ikkje podman-oppstart — eit funn verdt å notere for framtidige
ytelsesrundar på dette pipeline-laget, men utanfor scope for denne
spec-en (som eksplisitt målretta podman-kall-talet, ikkje FS-kontensjon).

**Ikkje gjort:** jobb-avgrensing for Steg 2 (spec-en sitt steg 7,
betinga oppfølging) — ikkje vurdert naudsynt, sidan den attverande Steg
2-kostnaden er FS-bunden (jf. over), ikkje podman-kontensjon, og
jobb-avgrensing ville ikkje adressert rotårsaka.
