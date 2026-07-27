# Auto-generert valid-scopes for release-please

## Bakgrunn

**Problem:**
`.github/workflows/release-please.yml` inneheld ei manuelt vedlikehalden liste over gyldige modell-scopes (33 verdiar):
```bash
VALID_SCOPES="common-ap-no|cpsv-ap-no|dcat-ap-no|..."
```

Kvar gong `make new-model`, `make new-modellkatalog` eller `make new-begrepssamling` køyrer, må lista oppdaterast manuelt — dette er feilutsett og lét til å bli gløymt.

**Ønska løysing:**
Ei **auto-generert** fil som:
1. Vert oppdatert automatisk av `make new-model` / `make new-modellkatalog` / `make new-begrepssamling`
2. Kan regenererast på demand med `make update-valid-scopes`
3. Vert lest av `.github/workflows/release-please.yml` (i staden for hardkoda liste)
4. Følgjer same mønster som Makefile sitt `SCHEMAS := $(shell find ...)` — dynamisk oppdaging

---

## Løysingsforslag

### A. Auto-generert `.github/valid-scopes.txt` (anbefalt)

**Prinsipp:** Éin fil med éi scope per linje, generert frå `find src/linkml -name "*-schema.yaml"`.

**Implementasjon:**

1. **Ny fil:** `.github/valid-scopes.txt`
   ```
   common-ap-no
   cpsv-ap-no
   dcat-ap-no
   ...
   ```

2. **Nytt Makefile-target:** `update-valid-scopes`
   ```makefile
   # Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
   update-valid-scopes:
       @echo "Genererer .github/valid-scopes.txt..."
       @find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
         | sed 's|.*/||; s|-schema\.yaml$$||' \
         | sort \
         > .github/valid-scopes.txt
       @echo "Generert $(shell wc -l < .github/valid-scopes.txt) scopes"
   ```

3. **Integrer i `new-model.sh`, `new-modellkatalog.sh`, `new-begrepssamling.sh`:**
   ```bash
   # På slutten av kvar script:
   echo "Oppdaterer .github/valid-scopes.txt..."
   make --no-print-directory update-valid-scopes
   ```

4. **Oppdater `.github/workflows/release-please.yml`:**
   ```yaml
   - name: Sjekk om siste commit skal trigge release-please
     id: check_commit_type
     if: github.event_name == 'push'
     run: |
       # Les gyldige scopes frå fil (pipe-separert)
       VALID_SCOPES=$(cat .github/valid-scopes.txt | tr '\n' '|' | sed 's/|$//')
       
       COMMIT_MSG=$(cat <<'EOF'
       ${{ github.event.head_commit.message }}
       EOF
       )
       FIRST_LINE=$(echo "$COMMIT_MSG" | head -n 1)
       
       # 1. Hopp over ikkje-releasande typar
       if echo "$FIRST_LINE" | grep -qE '^(style|docs|chore|test|ci|build|perf|refactor)(\(.*\))?:'; then
         echo "skip=true" >> $GITHUB_OUTPUT
         exit 0
       fi
       
       # 2. Tillat feat/fix utan scope
       if echo "$FIRST_LINE" | grep -qE '^(feat|fix):'; then
         echo "skip=false" >> $GITHUB_OUTPUT
         exit 0
       fi
       
       # 3. Tillat feat/fix med gyldig scope
       if echo "$FIRST_LINE" | grep -qE "^(feat|fix)\(($VALID_SCOPES)\):"; then
         echo "skip=false" >> $GITHUB_OUTPUT
         exit 0
       fi
       
       # 4. Elles: hopp over
       echo "skip=true" >> $GITHUB_OUTPUT
   ```

**Fordeler:**
- Éin kjelde til sanning — fila vert auto-generert frå faktisk filstruktur
- Kan regenererast når som helst med `make update-valid-scopes`
- Vert automatisk oppdatert av `make new-model` osv.
- Enkelt å sjekke i kodegjennomgang (git diff viser nye scopes)
- Kan gjenbrukast av andre workflows/scripts

**Ulemper:**
- Ein ekstra fil i `.github/`
- Krev `checkout` i workflow-steg før fil kan lesast

---

### B. Dynamisk generering i workflow (utan fil)

**Prinsipp:** GitHub Actions-workflow køyrer `find` direkte, utan mellomlagring.

**Implementasjon:**
```yaml
- name: Checkout for scope-sjekk
  if: github.event_name == 'push'
  uses: actions/checkout@v7

- name: Sjekk om siste commit skal trigge release-please
  id: check_commit_type
  if: github.event_name == 'push'
  run: |
    # Generer VALID_SCOPES dynamisk
    VALID_SCOPES=$(find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
      | sed 's|.*/||; s|-schema\.yaml$||' \
      | tr '\n' '|' \
      | sed 's/|$//')
    
    # ... resten som før
```

**Fordeler:**
- Ingen ekstra fil å vedlikehalde
- Alltid oppdatert (generert frå faktisk tilstand)

**Ulemper:**
- Krev `checkout` før filter-steget (litt tregare)
- Logikken ligg i workflow i staden for Makefile (mindre DRY)
- Vanskelegare å teste lokalt

---

## Anbefalt løysing

**A. Auto-generert `.github/valid-scopes.txt`** — fordi:
1. Éin kjelde til sanning, gjenbrukbar
2. Kan regenererast og testast lokalt (`make update-valid-scopes`)
3. Synleg i git diff når nye modellar leggast til
4. Konsistent med Makefile-mønsteret: automatisk oppdaging, ingen hardkoda lister

---

## Handlingsliste

- [x] A.1: Opprett `make update-valid-scopes` i Makefile
- [x] A.2: Generer initial `.github/valid-scopes.txt`
- [x] A.3: Integrer `make update-valid-scopes` i `new-model.sh`
- [x] A.4: Integrer `make update-valid-scopes` i `new-modellkatalog.sh`
- [x] A.5: Integrer `make update-valid-scopes` i `new-begrepssamling.sh`
- [x] A.6: Oppdater `.github/workflows/release-please.yml` til å lese `.github/valid-scopes.txt`
- [x] A.7: Fjern hardkoda `VALID_SCOPES` frå `release-please.yml`
- [ ] A.8: Test workflow med `fix(docs):` og `feat(ny-modell):` commits
- [x] A.9: Dokumenter i `CONVENTIONS.md` (korleis lista vert oppdatert)
- [x] A.10: Dokumenter i spec og flytt til `specs/done/`

---

## Utført

**A.1: Opprett `make update-valid-scopes` i Makefile**

Lagt til nytt target i Makefile (etter `new-begrepskatalog`):
```makefile
update-valid-scopes:
	@echo "Genererer .github/valid-scopes.txt..."
	@find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt
	@echo "Generert $$(wc -l < .github/valid-scopes.txt) scopes"
```

**A.2: Generer initial `.github/valid-scopes.txt`**

Køyrde `make update-valid-scopes` — genererte 32 scopes (éi linje per modell).

**A.3: Integrer `make update-valid-scopes` i `new-model.sh`**

Lagt til før "Neste steg:"-seksjonen:
```bash
# Oppdater .github/valid-scopes.txt
echo ""
echo "Oppdaterer .github/valid-scopes.txt..."
cd "$REPO_ROOT"
make --no-print-directory update-valid-scopes
```

**A.4: Integrer `make update-valid-scopes` i `new-modellkatalog.sh`**

Lagt til før "Neste steg:"-seksjonen (same mønster som A.3).

**A.5: Integrer `make update-valid-scopes` i `new-begrepssamling.sh`**

Lagt til før "Neste steg:"-seksjonen (same mønster som A.3).

**A.6: Oppdater `.github/workflows/release-please.yml` til å lese `.github/valid-scopes.txt`**

Lagt til nytt steg "Checkout for scope-sjekk" før "Sjekk om siste commit...":
```yaml
- name: Checkout for scope-sjekk
  if: github.event_name == 'push'
  uses: actions/checkout@v7
```

Oppdatert "Sjekk om siste commit..."-steg til å lese frå fil:
```bash
VALID_SCOPES=$(cat .github/valid-scopes.txt | tr '\n' '|' | sed 's/|$//')
```

**A.7: Fjern hardkoda `VALID_SCOPES` frå `release-please.yml`**

Erstatta hardkoda liste med dynamisk lesing frå fil (sjå A.6).

**A.8: Test workflow med `fix(docs):` og `feat(ny-modell):` commits**

Ikkje utført enno — krev faktisk push til main for å teste i GitHub Actions.

**A.9: Dokumenter i `CONVENTIONS.md` (korleis lista vert oppdatert)**

Oppdatert seksjonen "Gyldige modellnamn (scope)" med:
- Forklaring av auto-generering
- Korleis regenerere manuelt (`make update-valid-scopes`)
- Kva som oppdaterer lista automatisk (`make new-model` m.fl.)
- Referanse til `.github/valid-scopes.txt`

**A.10: Dokumenter i spec og flytt til `specs/done/`**

Utført no — flyttar etter denne oppdateringa.

---

## Implementasjonsdetaljar

### `make update-valid-scopes`

```makefile
# Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
# Køyrer automatisk ved `make new-model`, `make new-modellkatalog`, `make new-begrepssamling`
update-valid-scopes:
	@echo "Genererer .github/valid-scopes.txt..."
	@find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt
	@echo "Generert $(shell wc -l < .github/valid-scopes.txt) scopes"
```

### Integrasjon i `new-model.sh`

Legg til på slutten (før `echo "Neste steg:"`):
```bash
# Oppdater .github/valid-scopes.txt
echo ""
echo "Oppdaterer .github/valid-scopes.txt..."
cd "$REPO_ROOT"
make --no-print-directory update-valid-scopes
```

### Integrasjon i `new-modellkatalog.sh`

Legg til på slutten (før `echo "Neste steg:"`):
```bash
# Oppdater .github/valid-scopes.txt
echo ""
echo "Oppdaterer .github/valid-scopes.txt..."
cd "$REPO_ROOT"
make --no-print-directory update-valid-scopes
```

### Integrasjon i `new-begrepssamling.sh`

Legg til på slutten (før `echo "Neste steg:"`):
```bash
# Oppdater .github/valid-scopes.txt
echo ""
echo "Oppdaterer .github/valid-scopes.txt..."
cd "$REPO_ROOT"
make --no-print-directory update-valid-scopes
```

### Oppdatering av `release-please.yml`

```yaml
- name: Checkout for scope-sjekk
  if: github.event_name == 'push'
  uses: actions/checkout@v7

- name: Sjekk om siste commit skal trigge release-please
  id: check_commit_type
  if: github.event_name == 'push'
  run: |
    # Les gyldige scopes frå auto-generert fil
    if [ ! -f .github/valid-scopes.txt ]; then
      echo "Feil: .github/valid-scopes.txt finst ikkje — køyr 'make update-valid-scopes'" >&2
      exit 1
    fi
    
    VALID_SCOPES=$(cat .github/valid-scopes.txt | tr '\n' '|' | sed 's/|$//')
    
    COMMIT_MSG=$(cat <<'EOF'
    ${{ github.event.head_commit.message }}
    EOF
    )
    FIRST_LINE=$(echo "$COMMIT_MSG" | head -n 1)
    
    # 1. Hopp over ikkje-releasande typar
    if echo "$FIRST_LINE" | grep -qE '^(style|docs|chore|test|ci|build|perf|refactor)(\(.*\))?:'; then
      echo "skip=true" >> $GITHUB_OUTPUT
      echo "Siste commit er ikkje ein release-utløysande type — hoppar over"
      exit 0
    fi
    
    # 2. Tillat feat/fix utan scope (bakoverkompatibilitet)
    if echo "$FIRST_LINE" | grep -qE '^(feat|fix):'; then
      echo "skip=false" >> $GITHUB_OUTPUT
      echo "Siste commit er feat/fix utan scope — held fram"
      exit 0
    fi
    
    # 3. Tillat feat/fix med gyldig modell-scope
    if echo "$FIRST_LINE" | grep -qE "^(feat|fix)\(($VALID_SCOPES)\):"; then
      echo "skip=false" >> $GITHUB_OUTPUT
      echo "Siste commit er feat/fix med gyldig modell-scope — held fram"
      exit 0
    fi
    
    # 4. Elles: hopp over (t.d. feat(docs), fix(docgen))
    echo "skip=true" >> $GITHUB_OUTPUT
    echo "Siste commit har ikkje gyldig modell-scope — hoppar over"
```

### Oppdatering av `CONVENTIONS.md`

Legg til under seksjonen "Commit-meldingar":

**Automatisk oppdatering av valid-scopes:**

Lista over gyldige modellnamn vert automatisk generert og lagra i `.github/valid-scopes.txt`.

- **Køyr `make update-valid-scopes`** for å regenerere lista manuelt
- **`make new-model`**, **`make new-modellkatalog`** og **`make new-begrepssamling`** oppdaterer lista automatisk
- Fila vert lest av `.github/workflows/release-please.yml` for å validere commit-scopes

---

## Testing

1. **Lokal generering:**
   ```bash
   make update-valid-scopes
   cat .github/valid-scopes.txt  # skal vise 33 linjer
   ```

2. **Test at new-model oppdaterer lista:**
   ```bash
   make new-model NAME=test-modell DOMAIN=test
   git diff .github/valid-scopes.txt  # skal vise 'test-modell' lagt til
   ```

3. **Test workflow:**
   - Commit med `docs(test):` → skal hoppe over release-please
   - Commit med `feat(test-modell):` → skal trigge release-please

---

## Alternativ: Inkluder i pre-commit hook

Dersom `.github/valid-scopes.txt` vert gløymt, kan ein pre-commit hook regenerere den:

```bash
# .git/hooks/pre-commit
#!/bin/bash
if git diff --cached --name-only | grep -qE 'src/linkml/.*/.*-schema\.yaml'; then
    make --no-print-directory update-valid-scopes
    git add .github/valid-scopes.txt
fi
```

Dette sikrar at lista alltid er synkronisert med `src/linkml/`-strukturen.
