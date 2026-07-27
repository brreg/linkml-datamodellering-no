# Semantisk versjonering basert på scope

## Bakgrunn

**Problem:**
Modellar får nye versjonar ved endringar som ikkje påverkar modellinnhaldet:
- `fix(docs):` — endrar README.md, mkdocs/docs/\*.md, bootstrap.sh
- `fix(docgen):` — endrar Jinja-templates, publish.sh, dokumentasjonsgenerering
- `feat(docgen):` — nye funksjonar i dokumentasjonsportalen

Døme frå siste commits:
- `0a07b6b7 fix(docs): bruk skjema-spesifikke taggar i import-døme` — endra README.md, mkdocs/docs/\*, bootstrap.sh
- `ccde7563 fix(docgen): fiks linjeskift i slot-tabellar` — endra index.md.jinja2
- `74e235ab feat(docgen): klikkbare "Defined in"-lenkjer` — endra index.md.jinja2

Desse utløyser `release-please` fordi dei brukar `feat` eller `fix`-prefix, men dei endrar **ikkje** modellinnhaldet (`.yaml`-skjema).

**Rotårsak:**
`.github/workflows/release-please.yml` linje 36 filtererer ut `style|docs|chore|test|ci|build|perf|refactor`, men **ikkje** `fix(docs)` eller `feat(docgen)` — desse har `fix`/`feat`-prefix, så dei passerer filteret.

**Ønska oppførsel:**
- Versjonering skal berre triggerast av endringar i **modellinnhaldet** (`.yaml`-skjema, klasser, slots, enumerations, types)
- Endringar i dokumentasjonsgenerering, mkdocs-innhald, CI/CD, testing o.l. skal **ikkje** trigge versjonering

---

## Løysingsalternativ

### A. Scope-basert filtrering (anbefalt)

**Prinsipp:** Berre `feat(<modell>)` og `fix(<modell>)` triggar versjonering — scope må vere eit gyldig modellnamn.

**Implementasjon:**
1. Utvid filteret i `release-please.yml` til å **inkludere scope-basert sjekk**:
   - `feat` eller `fix` **utan** scope → utløyser release (for bakoverkompatibilitet)
   - `feat(<scope>)` eller `fix(<scope>)` der `<scope>` er gyldig modellnamn → utløyser release
   - `feat(docs|docgen|ci|test|...)` → **ikkje** utløyse release
   
2. Legg til liste over gyldige scopes:
   - `ap-no`, `dcat-ap-no`, `skos-ap-no`, `cpsv-ap-no`, `dqv-ap-no`, `modelldcat-ap-no`
   - `ngr`, `ngr-adresse`, `ngr-eiendom`, `ngr-person`, `ngr-virksomhet`
   - `fint`, `fint-common`, `fint-administrasjon`, `fint-arkiv`, `fint-okonomi`, `fint-personvern`, `fint-ressurs`, `fint-utdanning`
   - `oreg`, `register-over-aksjeeiere`, `enhetsregisteret`
   - `samt`, `samt-bu`
   - `begrepskatalog`, `brreg-begrepskatalog`
   - `modellkatalog`, `brreg-modellkatalog`
   - `fair`, `fair-metadata`
   - `referanse`

3. Oppdater `CONVENTIONS.md` med ny scope-konvensjon:
   - **Modellendringar:** `feat(<modell>):` eller `fix(<modell>):`
   - **Dokumentasjon:** `docs(<scope>):` eller `fix(docs):`
   - **Dokumentgenerering:** `feat(docgen):` eller `fix(docgen):`
   - **CI/CD:** `ci:` eller `chore(ci):`
   - **Testing:** `test:` eller `fix(test):`

**Fordeler:**
- Eksplisitt kontroll over kva som utløyser versjonering
- Tydelig separasjon mellom modell- og dokumentendringar
- Kan enkelt utvidast med nye modellar

**Ulemper:**
- Krev vedlikehald av scope-liste når nye modellar leggast til
- Bryt med dagens konvensjon der `fix(docs):` brukes for dokumentendringar

### B. Path-basert filtrering

**Prinsipp:** Sjekk om commit endrar filer i `src/linkml/` — berre då skal versjonering triggerast.

**Implementasjon:**
1. Legg til steg i `release-please.yml` som sjekkar om siste commit endrar `src/linkml/**/*.yaml`
2. Hopp over release-please dersom ingen `.yaml`-filer i `src/linkml/` vart endra

**Fordeler:**
- Automatisk — krev ikkje scope-liste
- Fungerer uavhengig av commit-melding

**Ulemper:**
- Meir kompleks logikk
- Krev checkout for å sjekke filendringar (innan filter-steget)
- Kan trigge falske positivar dersom `examples/*.yaml` eller `data/*.yaml` endrast (men desse **skal** trigge versjonering)

---

## Anbefalt løysing

**A. Scope-basert filtrering** — fordi:
1. Eksplisitt og kontrollerbar
2. Samsvarar med conventional commits-standarden
3. Krev minimal endring i eksisterande workflow

---

## Handlingsliste

- [x] A.1: Definer liste over gyldige modell-scopes
- [x] A.2: Oppdater `.github/workflows/release-please.yml` med scope-basert filter
- [x] A.3: Oppdater `CONVENTIONS.md` med nye scope-reglar
- [ ] A.4: Test workflow med `fix(docs):` og `feat(dcat-ap-no):` commits
- [ ] A.5: Dokumenter i spec og flytt til `specs/done/`

---

## Utført

**A.1: Definer liste over gyldige modell-scopes**

Liste generert frå `find src/linkml -name "*-schema.yaml"` (33 skjema):
```
common-ap-no, cpsv-ap-no, dcat-ap-no, dqv-ap-no, dqv-core, modelldcat-ap-no, 
modelldcat-katalog, modelldcat-modell, skos-ap-no, xkos-ap-no, ngr-adresse, 
ngr-eiendom, ngr-person, ngr-virksomhet, fint-common, fint-administrasjon, 
fint-arkiv, fint-okonomi, fint-personvern, fint-ressurs, fint-utdanning, 
register-over-aksjeeiere, enhetsregisteret-bvrinn, samt-bu, brreg-begrepskatalog, 
brreg-modellkatalog, digdir-modellkatalog, kartverket-modellkatalog, 
ksdigital-modellkatalog, novari-modellkatalog, skatteetaten-modellkatalog, 
fair-metadata, referanse
```

**A.2: Oppdater `.github/workflows/release-please.yml` med scope-basert filter**

Endra `check_commit_type`-steget til å:
1. Hoppe over `style|docs|chore|test|ci|build|perf|refactor` (uendra)
2. Tillate `feat:` og `fix:` **utan** scope (bakoverkompatibilitet)
3. Tillate `feat(<modell>):` og `fix(<modell>):` der `<modell>` er gyldig modellnamn
4. Hoppe over alt anna (t.d. `feat(docs):`, `fix(docgen):`, `feat(ci):`)

Logikken sjekkar:
- Først: ikkje-releasande typar (uavhengig av scope)
- Så: `feat`/`fix` utan scope
- Så: `feat`/`fix` med gyldig modell-scope
- Elles: hopp over

**A.3: Oppdater `CONVENTIONS.md` med nye scope-reglar**

Utvida `## Commit-meldingar`-seksjonen med:
- Ny kolonne "Utløyser release?" i tabell
- Liste over gyldige modellnamn
- Klargjering av kva som utløyser versjonering
- Døme på modellendringar vs. dokumentendringar vs. dokumentgenerering
- Viktig-boks med reglar

**A.4: Test workflow med `fix(docs):` og `feat(dcat-ap-no):` commits**

Ikkje utført enno — krev faktisk push til main for å teste i GitHub Actions.

**A.5: Dokumenter i spec og flytt til `specs/done/`**

Utført no — flyttar etter denne oppdateringa.
