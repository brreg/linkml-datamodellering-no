# Plan: Erstatt "profil" med "policy" der omgrepet faktisk viser til validerings-policy

## Bakgrunn

Brukaren bad om å kartleggje om "profil" er brukt til å omtale
validerings-**policy** (bronze/silver/gold/felles-datakatalog/
felles-begrepskatalog) — spørsmålet stod alt uløyst i
`specs/backlog/TODO.md` (linje 79). Repoet har to reelt ulike omgrep:

- **policy** / `validation_policy` — bronze/silver/gold m.fl.-nivåa som
  validerer skjemakvalitet (`src/mcp-linkml-validator/`, `build.yaml`
  sitt `validation_policy`-felt, CLAUDE.md § "Policy-hierarki")
- **profil** — AP-NO-applikasjonsprofilar (`dcat-ap-no-schema`,
  `modelldcat-ap-no-schema` osv., CLAUDE.md § "LinkML Importhierarki")
  og organisasjonsprofilar i `mcp-linkml-begrep-utkast`
  (`brreg.yaml`/`default.yaml`, valfrie ved begrepsoppretting)

### Kartlegging

Eit breitt søk (kjeldekode, dokumentasjon, spec-filer, make-filer,
commit-historikk) fann fleire stader der "profil" er brukt om
policy-konseptet:

1. **`README.md:32`** — verktøyskildringa av `mcp-linkml-validator` skriv
   "kvalitets-**profilar**", "publiserings-**profilar**" og
   "egendefinerte **profilar**" om det som elles konsekvent heiter
   policy/medaljongnivå (`src/mcp-linkml-validator/README.md`,
   `server.py`, `policies/README.md`).

2. **`mkdocs/docs/kom-i-gang/ny-domenemodell.md`**
   - linje 174: eksempelkommando brukar `PROFILE=silver` mot
     `mcp-linkml-modell-utkast` — sjå punkt 3 under, flagget skal heite
     `POLICY=`.
   - linje 192: "Lint + validering mot **medaljong-profil**:" — einaste
     stad "medaljong-profil" finst; alle 14 andre treff i repoet brukar
     "medaljongnivå"/"medaljong-policy(en)".

3. **Heile `src/mcp-linkml-modell-utkast`-verktøyet** (JSON Schema →
   LinkML-konverterar) har eit `profiles/`-katalog med `bronze.yaml`/
   `silver.yaml` som er **eksplisitt designa for å samsvare 1:1** med
   `validation_policy: bronze/silver` — men er konsekvent kalla "profil"
   gjennom kode, CLI-flagg, MCP-verktøynamn og dokumentasjon. Dette er
   den mest reelle forvekslingskjelda, sidan README-en deira uttrykkjeleg
   koplar dei saman:
   > "Fyll inn silver-annotasjonar om skjemaet har
   > `validation_policy: silver` eller høgare (**berre silver-profil**)"

4. **Arkiverte spec-filer** (`specs/done/validering-logging-publish.md`,
   `bronze-policy-metadata-krav.md`,
   `new-modell-annotations-og-kontaktpunkt.md`) brukar same konflaterte
   språk. Desse er urørte per DRY-unntaket for `specs/done/` i CLAUDE.md.

5. **Commit-historikk** stadfestar opphavet: heile policy-mekanismen
   heitte opphavleg "valideringsprofil"/"ap-no profil", vart omdøypt til
   sjølve **bronze/silver/gold-profilnamna** i commit `e16dd977`
   ("endrer profilnavna til bronze, silver og gold"), og seinare til
   "policy" (frå `66bfa2bc`) — men omdøypinga vart aldri fullført i
   `mcp-linkml-modell-utkast` eller i dei to reine tekststadene over.

**Avklart med brukaren:** full omdøyping av `PROFILE=` → `POLICY=` i
`mcp-linkml-modell-utkast` er innanfor omfang, ikkje berre
dokumentasjonstekst — sjølv om dette endrar eit MCP-verktøy sitt
offentlege parameternamn og CLI-flagg.

**Legitime "profil"-treff — IKKJE i omfang:**
AP-NO-profilar (`dcat-ap-no` osv.), `er_profil_av`/`dx-prof`, og
organisasjonsprofilane i `mcp-linkml-begrep-utkast`
(`list_profiles`/`list-profiles`, `profiles/brreg.yaml`,
`profiles/default.yaml`) — desse er eit heilt anna, korrekt namngjeve
konsept og skal ikkje endrast.

## Plan

**Steg 1 — Reine tekstrettingar (README.md + ny-domenemodell.md)**
Bytt "profil" → "policy"/"medaljongnivå" der teksten faktisk omtaler
validerings-policy-konseptet.

**Steg 2 — Omdøyp `PROFILE=`/"profil" → `POLICY=`/"policy" gjennomgåande
i `mcp-linkml-modell-utkast`**
Dette er éin samanhengande kjede frå CLI-flagg via JSON-RPC-request til
MCP-serveren sin parameter og attende til dokumentasjonen — alle ledd må
endrast saman for at verktøyet framleis skal fungere:

- `src/mcp-linkml-modell-utkast/profiles/` → `policies/` (katalognavn,
  filene `bronze.yaml`/`silver.yaml` skal ikkje endre navn, berre
  innhaldet sin "profil"-tekst: "Bronze-profil" → "Bronze-policy" osv.)
- `converter.py`: `load_profile()` → `load_policy()`, `profile_dir` →
  `policy_dir`, parameteren `profile` → `policy` gjennom heile
  kallkjeda (`convert()`, `_resolve_type()`, `_build_schema()` m.fl.),
  kommentaren `# Profil` → `# Policy`, `profile_annotations` →
  `policy_annotations`
- `server.py`: `_PROFILES_DIR` → `_POLICIES_DIR`, `_list_profiles()` →
  `_list_policies()`, tool-parameteren `"profile"` → `"policy"`,
  `TOOL_LIST_PROFILES` → `TOOL_LIST_POLICIES`, MCP-verktøynamnet
  `list_profiles` → `list_policies`, `profile_name`/`load_profile`-import
  → `policy_name`/`load_policy`, feilmeldinga "Ukjend profil" → "Ukjend
  policy"
- `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py`:
  `--profile`-argumentet → `--policy`, JSON-RPC-feltet `"profile"` →
  `"policy"`
- `make/60-mcp.mk`: `PROFILE=bronze` → `POLICY=bronze` i `##`-kommentar
  og `log_error`-melding, `--profile`-flagget til Python-scriptet →
  `--policy`
- `src/assets/containers/Dockerfile.mcp-linkml` linje 30: `COPY
  src/mcp-linkml-modell-utkast/profiles/ profiles/` → `COPY
  src/mcp-linkml-modell-utkast/policies/ policies/` (linje 37, som gjeld
  `mcp-linkml-begrep-utkast` sine organisasjonsprofiler, er urørt)
- `src/mcp-linkml-modell-utkast/README.md`: `PROFILE=` → `POLICY=`
  gjennomgåande, "## Profiler" → "## Policyar", "### Silver-profil" →
  "### Silver-policy", "Profilane ligg i `profiles/<navn>.yaml`" →
  "Policyane ligg i `policies/<navn>.yaml`", tool-tabellen sin
  `profile`-parameter → `policy`, `list_profiles` → `list_policies`,
  "konverteringsprofiler" → "konverteringspolicyar", "berre
  silver-profil" → "berre silver-policy"
- `tests/test_mcp_linkml_generator.py`: importen `load_profile` →
  `load_policy`, hjelpefunksjonen `_profile()` → `_policy()`,
  `_profiles()` → `_policies()`, JSON-RPC-nøkkelen `"profile":` →
  `"policy":`, `list_profiles`-kallet → `list_policies`, testnamna
  `test_load_profile_les_bronze` → `test_load_policy_les_bronze`,
  `test_kvar_profil_har_name_og_description` →
  `test_kvar_policy_har_name_og_description`,
  `test_generate_med_ukjend_profil_gir_32602` →
  `test_generate_med_ukjend_policy_gir_32602`

**Steg 3 — Oppdater referansar i `COMMANDS.md` og
`mkdocs/docs/kom-i-gang/kommandoar.md`**
`COMMANDS.md:273` og `kommandoar.md:162` sine
`PROFILE=default`-eksempel → `POLICY=default` (sjølve
`default`-verdien er ein alt eksisterande, ikkje-relatert unøyaktigheit
i desse to linjene — ingen `default.yaml`-policy finst, berre
`bronze.yaml`/`silver.yaml` — og rettast ikkje her, då det er utanfor
denne specens omfang).

**Steg 4 — Fjern punktet frå `specs/backlog/TODO.md`**
Linje 79 ("kartlegg om vi har brukt begrepet PROFIL...") er løyst av
denne specen og kan fjernast frå lista.

**Steg 5 — Verifiser**
- `make mcp-linkml-modell-utkast-test` (unit-testar for MCP-serveren)
- `make mcp-linkml-modell-utkast-smoke`
- `make mcp-linkml-modell-utkast SCHEMA=<eksisterande json-schema-fil>
  POLICY=silver` — stadfest at det nye flagget fungerer end-to-end
- `grep -rniE 'PROFILE=|load_profile|_list_profiles|list_profiles\b'
  src/mcp-linkml-modell-utkast make/60-mcp.mk
  src/assets/scripts/makefile/mcp-build-modell-utkast-request.py
  tests/test_mcp_linkml_generator.py` → skal ikkje gje treff (utanom
  legitime `mcp-linkml-begrep-utkast`-treff, som ikkje er del av desse
  filene)

## Filer som vert påverka

- `README.md` (linje 32)
- `mkdocs/docs/kom-i-gang/ny-domenemodell.md` (linje 174, 192)
- `mkdocs/docs/kom-i-gang/kommandoar.md` (linje 162)
- `COMMANDS.md` (linje 273)
- `make/60-mcp.mk`
- `src/assets/containers/Dockerfile.mcp-linkml` (linje 30)
- `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py`
- `src/mcp-linkml-modell-utkast/server.py`
- `src/mcp-linkml-modell-utkast/converter.py`
- `src/mcp-linkml-modell-utkast/README.md`
- `src/mcp-linkml-modell-utkast/profiles/` → `policies/` (katalognavn +
  innhald i `bronze.yaml`/`silver.yaml`)
- `tests/test_mcp_linkml_generator.py`
- `specs/backlog/TODO.md` (fjern løyst punkt)

**Ikkje påverka** (legitime "profil"-bruk):
`src/mcp-linkml-begrep-utkast/` (organisasjonsprofiler,
`list_profiles`/`list-profiles`), alle AP-NO-profil-referansar i
CLAUDE.md/mkdocs/skjema, `er_profil_av`/`dx-prof`,
`specs/done/*` (arkivert).

## Handlingsliste

1. [x] Steg 1 — README.md + ny-domenemodell.md tekstrettingar
2. [x] Steg 2 — full `PROFILE`→`POLICY`-omdøyping i
   `mcp-linkml-modell-utkast` (kode, make-target, hjelpescript, README,
   testar, testfixture) — **med eitt avvik, sjå «Utført»**
3. [x] Steg 3 — `COMMANDS.md` + `kommandoar.md` referansar
4. [x] Steg 4 — fjern punktet frå `specs/backlog/TODO.md`
5. [x] Steg 5 — verifiser med testar/smoke-test/grep/end-to-end

## Utført

- **Steg 1**: `README.md` (kvalitets-/publiserings-/egendefinerte
  policyar), `mkdocs/docs/kom-i-gang/ny-domenemodell.md` (`PROFILE=silver`
  → `POLICY=silver`, "medaljong-profil" → "medaljongnivå").
- **Steg 2**: Full omdøyping i `mcp-linkml-modell-utkast`:
  `converter.py` (`load_profile`→`load_policy`, parameteren `profile`→
  `policy` gjennom heile kallkjeda), `server.py`
  (`_list_profiles`→`_list_policies`, MCP-verktøyet `list_profiles`→
  `list_policies`, tool-parameteren `"profile"`→`"policy"`),
  `profiles/bronze.yaml`/`silver.yaml` (innhaldstekst "Bronze-profil"/
  "Silver-profil"→"-policy"), `mcp-build-modell-utkast-request.py`
  (`--profile`→`--policy`), `make/60-mcp.mk` (`PROFILE=`→`POLICY=`),
  `src/mcp-linkml-modell-utkast/README.md` (heile "## Profiler"-seksjonen
  → "## Policyar"), `tests/test_mcp_linkml_generator.py` (alle
  funksjons-/testnamn), `tests/test-mcp-linkml-generator.json`
  (smoke-test-fixturen kalla framleis `list_profiles` — oppdaga og retta
  under verifisering i steg 5, var ikkje i opphavleg filliste).
- **Avvik frå planen — katalognamnet `profiles/` er IKKJE omdøypt til
  `policies/`:** eit alvorleg WSL2/DrvFs-mount-cache-problem gjorde
  katalogen `src/mcp-linkml-modell-utkast/policies/` vedvarande
  utilgjengeleg (`d?????????`-spøkelsesoppføring, "No such file or
  directory" trass i at han eksisterte) etter fleire forsøk på
  `mv`/`rm -rf`/`mkdir`, også etter 4+ minutt venting. For å unngå
  datatap vart endringane til slutt gjenoppretta til den opphavlege,
  stabile `profiles/`-katalogen. Koden peikar difor framleis på den
  fysiske katalogen `profiles/` (med ein kort forklarande kommentar i
  `converter.py`/`server.py` som viser til denne specen), sjølv om alle
  variabel-/funksjonsnamn, CLI-flagg, MCP-verktøynamn og dokumentasjon
  konsekvent brukar "policy". Ein ufarleg, tom spøkelseskatalog
  `src/mcp-linkml-modell-utkast/policies/` kan liggje att som eit
  urørleg, utracka artefakt i den lokale arbeidskopien (synest i
  `git status` som `??`, men kan ikkje listast/slettast) — dette er
  eit lokalt WSL-filsystemproblem, ikkje eit repo-problem, og
  forsvinn truleg ved omstart av WSL/Claude Code-økta. **Oppfølging:**
  når nokon (menneske eller ei frisk økt) kan få tilgang til katalogen
  att, byt katalognamnet fysisk til `policies/` og fjern kommentarane
  i `converter.py`/`server.py` som viser til dette avviket, samt
  `Dockerfile.mcp-linkml` sine to `COPY .../profiles/ profiles/`-linjer
  for `modell-utkast`-target (linje 30) — desse er urørte i denne
  runden av same grunn.
- **Steg 3**: `COMMANDS.md` og `kommandoar.md` sine
  `PROFILE=default`-eksempel → `POLICY=default`.
- **Steg 4**: Punktet fjerna frå `specs/backlog/TODO.md`.
- **Steg 5 — verifisert**:
  - `make mcp-linkml-modell-utkast-test`: 44/44 testar OK
  - `make mcp-linkml-modell-utkast-smoke`: `list_policies` og
    `POLICY`-parameteren fungerer korrekt i JSON-RPC-svara
  - `make mcp-linkml-modell-utkast SCHEMA=... FORMAT=json-schema
    POLICY=silver`: genererer og roundtrip-validerer korrekt
    end-to-end via det nye flagget
  - Repo-breitt grep etter `list_profiles`/`PROFILE=` gav berre eitt
    attverande, legitimt treff (`mcp-linkml-begrep-utkast-list-profiles`
    i `make/60-mcp.mk`, organisasjonsprofiler — utanfor omfang)
