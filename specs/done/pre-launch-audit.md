# Pre-launch Audit — Forberede repoet for eksterne brukarar

\*\*Status:\*\* Utført  
**Dato:** 2026-06-29  
**Kontekst:** Før repoet vert opna for eksterne brukarar må kritiske område handterast — særleg knytt til dokumentasjon, sikkerheit, datahandtering og brukarforventningar.

---

## Bakgrunn

Dette repoet presenterer seg som ein **Proof of Concept**, men opererer med verkelegheitsdata (begrepskatalog, modellkatalog) merka `publish_external: true`. Før eksterne organisasjonar vert inviterte inn må vi sikre:

1. **Forventningstydeleggjering** — PoC-status må vere eksplisitt kommunisert i heile repoet
2. **Datahandtering** — skil mellom PoC-modellar og skarpe produksjonsdata må vere tydeleg
3. **Sikkerheit og personvern** — ingen sensitive data, klare sikkerheitsprosedyrar
4. **Onboarding-kvalitet** — dokumentasjon og prosessar må vere komplette nok til at eksterne kan bidra
5. **Ansvar og eigarskap** — klare roller og prosedyrar når fleire organisasjonar deler same repo

---

## Kritiske funn

### 1. PoC-status er ikkje synleg overalt

**Problem:**  
- README.md har éin linje: "**NB dette er ein Proof of Concept**" heilt øvst
- Resten av dokumentasjonen (mkdocs-portalen, CONTRIBUTING.md, GOVERNANCE.md) presenterer repoet som eit produksjonsklart system utan forbehold
- Onboarding-rettleiingane (`ny-domenemodell.md`, `ny-org.md`, `publisering-begrep.md`) nemnest ingen avgrensingar eller kjent-bugs-seksjonar

**Konsekvens:**  
Nye brukarar forstår ikkje at dette er ein PoC. Dei vil forvente stabilitet, dokumentasjon og funksjonalitet på produksjonsnivå — og oppleve overraskingar når ting manglar eller er ustabilt.

**Tiltak:**

- [x] **T1.1** — Legg til PoC-disclaimer heilt øvst i `mkdocs/docs/index.md` med synleg visuell markering (quote block / admonition). Eksempel:

  ```markdown
  !!! warning "Proof of Concept"
  
      Dette repoet er ein **Proof of Concept** for LinkML-basert datamodellering i norsk offentleg sektor.
      
      **Kva det betyr:**
      
      - Modellar og verktøy er under utvikling og kan endre seg
      - Dokumentasjonen kan vere ufullstendig eller utdatert
      - Nokre funksjonar er berre delvis implementerte
      - Det finst kjende avgrensingar og bugs (sjå [kjende avgrensingar](../specs/bugs/))
      - Ingen garantert stabilitet eller support-SLA
      
      **For eksterne organisasjonar:** Før de tek i bruk repoet i produksjon — les [GOVERNANCE.md](../GOVERNANCE.md) 
      for forventningar til stabilitet og ansvar.
  ```
- [x] **T1.2** — Legg til PoC-status-seksjon i `GOVERNANCE.md` under "Bakgrunn" som seier kva stabilitet eksterne brukarar kan forvente
- [x] **T1.3** — Legg til PoC-disclaimer i `CONTRIBUTING.md` under "Kom i gang"
- [x] **T1.4** — Kvar rettleiing (`ny-domenemodell.md`, `ny-org.md`, `publisering-begrep.md`) skal ha ein "Avgrensingar"-seksjon nedst som refererer til `specs/bugs/` og kjende gap. Eksempel:

  ```markdown
  ---
  
  ## Kjende avgrensingar
  
  Denne rettleiinga dekkjer grunnleggjande arbeidsflyt for domenemodellering i LinkML. 
  Følgjande avgrensingar gjeld i PoC-fasen:
  
  ### Validering
  
  - **BUG-1**: `rdflib_loader` rekonstruerer ikkje `LangString`-verdiar korrekt frå TTL ved roundtrip-testing 
    ([specs/bugs/langstring-rdflib-roundtrip.md](../../specs/bugs/langstring-rdflib-roundtrip.md))
  - MCP-validator kjører berre bronze/silver/gold-policy — ingen automatisk validering mot eksterne API-ar enno
  
  ### Generatorar
  
  - PlantUML-diagram vert ikkje genererte for skjema med meir enn 50 klasser (ytelse)
  - JSON Schema-generatoren støttar ikkje `union_of` med meir enn to typar
  
  ### Publisering
  
  - Publisering til Felles Begrepskatalog er delvis implementert — sjå [publisering-begrep.md](publisering-begrep.md) 
    for faktisk status
  - Modellkatalogar med `publish_external: true` vert ikkje automatisk registrerte i data.norge.no enno
  
  **Fullstendig oversikt:** Sjå [specs/bugs/README.md](../../specs/bugs/README.md) for komplett liste 
  over kjende bugs og workarounds.
  
  **Rapporter nye problem:** Opne eit [GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) 
  med merkelappen `bug`.
  ```
- [x] **T1.5** — Alle modellkatalogar (`brreg-modellkatalog.yaml`, `digdir-modellkatalog.yaml`, osv.) skal ha `status: http://purl.org/adms/status/UnderDevelopment` til PoC-status er oppheva

**Prioritet:** HØGST — må gjerast før invitasjon av eksterne

---

### 2. Verkeleg produksjonsdata ligg i PoC-repoet

**Problem:**  
Følgjande datafiler er merka `publish_external: true`:

- `src/linkml/ngr/ngr-virksomhet/manifest.yaml` — merka for publisering til Felles Datakatalog
- `src/linkml/oreg/register-over-aksjeeiere/manifest.yaml` — merka for publisering
- `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml` (179 kB produksjonsdata)
- `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`

Samtidig står det i `publisering-begrep.md`:

> "Denne rettleiinga viser korleis begrepsdefinisjonar i `src/linkml/begrepskatalog/<katalog>/data/` vert konvertert til SKOS/Turtle og automatisk publisert til [Felles Begrepskatalog](https://data.norge.no/concepts) via eit høstingsendepunkt på GitHub Pages."

**Konsekvens:**  
- Det er **ikkje klart** om denne publiseringa faktisk skjer, eller om det berre er PoC-dokumentasjon
- Dersom det faktisk publiserer til Felles Begrepskatalog / Felles Datakatalog — korleis handterer vi kvalitet, ansvar og tilbaketrekking?
- Dersom det **ikkje** publiserer enno — kvifor ligg det verkelegheitsdata (`brreg-modellkatalog.yaml` m.fl.) i repoet?

**Tiltak:**

- [x] **T2.1** — Skriv ein eksplisitt policy i `GOVERNANCE.md` for kva som kan publiserast til eksterne katalogar i PoC-fasen
- [x] **T2.3** — Dersom publisering ikkje skjer — erstatt verkelege data med syntetiske eksempeldata og dokumentér dette eksplisitt (Vi beheld verkelege data, men la til disclaimer i T2.4)
- [x] **T2.4** — Dersom publisering skjer — legg til disclaimer i katalogfilene (t.d. i `beskrivelse`-feltet) at dette er PoC-data med avgrensa kvalitet
- [x] **T2.5** — Legg til README-seksjon "Kva publiserast til eksterne system" med klart svar på kva som faktisk vert pusha ut av repoet
- [x] **T2.6** — Endre formuleringa i `publisering-begrep.md` frå "automatisk publisert til Felles Begrepskatalog" til "tilrettelagt for automatisk høsting til Felles Begrepskatalog". Eksempel på ny formulering:

  ```markdown
  # Publiser til Felles Begrepskatalog
  
  Denne rettleiinga viser korleis begrepsdefinisjonar i `src/linkml/begrepskatalog/<katalog>/data/` vert
  konvertert til SKOS/Turtle og **tilrettelagt for automatisk høsting** til
  [Felles Begrepskatalog](https://data.norge.no/concepts).
  
  Repoet publiserer SKOS/Turtle-filer til GitHub Pages som eit høstingsendepunkt. Felles Begrepskatalog
  kan konfigurere seg til å høste frå dette endepunktet, men **repoet pusher ikkje** direkte til
  data.norge.no — det følgjer "pull, ikkje push"-prinsippet.
  
  ## Slik fungerer det
  
  1. **Lokal redigering:** Du redigerer begrep i `data/<katalog>/<katalog>.yaml`
  2. **Generering:** `make convert-data` konverterer YAML til SKOS/Turtle
  3. **Publisering til GitHub Pages:** CI publiserer `.ttl`-filen til `https://brreg.github.io/linkml-datamodellering-no/...`
  4. **Høsting (ekstern prosess):** Felles Begrepskatalog kan konfigurere seg til å høste frå GitHub Pages-adressa
  
  **Status i PoC-fasen:** Steg 1-3 er implementerte. Steg 4 (faktisk høsting til Felles Begrepskatalog) 
  må manuelt settes opp i Felles Begrepskatalog for kvar organisasjon som skal publisere sine begrepskataloger.
  ```

- [x] **T2.7** — Endre formuleringa i `mkdocs/docs/publisering-modell.md` (dersom denne fila eksisterer) frå "publisert til Felles Datakatalog" til "tilrettelagt for automatisk høsting til Felles Datakatalog". Eksempel på ny formulering:

  ```markdown
  # Publiser til Felles Datakatalog
  
  Denne rettleiinga viser korleis informasjonsmodellar frå dette repoet vert skildra i 
  ModelDCAT-AP-NO-format og **tilrettelagt for automatisk høsting** til 
  [Felles Datakatalog](https://data.norge.no) via GitHub Pages.
  
  Repoet genererer ModelDCAT-AP-NO-metadata og publiserer dette til GitHub Pages som eit høstingsendepunkt. 
  Felles Datakatalog kan konfigurere seg til å høste frå dette endepunktet, men **repoet pusher ikkje** 
  direkte til data.norge.no — det følgjer "pull, ikkje push"-prinsippet.
  
  ## Slik fungerer det
  
  1. **Modellering:** Du lagar eller oppdaterer LinkML-skjema i `src/linkml/<domain>/<modell>/`
  2. **Generering:** `make <domain>` genererer ModelDCAT-AP-NO-metadata frå skjema-annotasjonar
  3. **Publisering til GitHub Pages:** CI publiserer metadata til `https://brreg.github.io/linkml-datamodellering-no/...`
  4. **Høsting (ekstern prosess):** Felles Datakatalog kan konfigurere seg til å høste frå GitHub Pages-adressa
  
  **Status i PoC-fasen:** Steg 1-3 er implementerte. Steg 4 (faktisk høsting til Felles Datakatalog) 
  må koordinerast med Digitaliseringsdirektoratet for kvar organisasjon som skal publisere sine 
  informasjonsmodellar.
  ```

**Prioritet:** HØGST — må avklarast før invitasjon

---

### 3. Mange TODO-verdiar i produksjonsdata

**Problem:**  
```
src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml:
  endringsdato: "TODO"
  utgivelsesdato: "TODO"

src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml:
  - 'TODO: beskriv klassen' (fleire gonger)
```

**Konsekvens:**  
Dersom desse datafilene faktisk publiserast til eksterne katalogar vert det publisert ufullstendige metadata. Dette bryt med Digdir sine krav til metadata (sjå `specs/done/` for bronze/silver/gold-policy).

**Tiltak:**

- [-] **T3.1** — ~~Fyll inn alle TODO-verdiar i `brreg-modellkatalog.yaml` før publisering~~ — **Ikkje utført:** TODO-verdiar skal fyllast inn av dataeigaren, ikkje som del av pre-launch audit
- [x] **T3.2** — Deaktiver `publish_external` i `brreg-begrepskatalog/manifest.yaml` til TODO-verdiar i `brreg-begrepskatalog-schema.yaml` er fylt inn (endre `publish_external: true` → `publish_external: false`)
- [-] **T3.3** — ~~Legg til pre-commit hook eller CI-sjekk som blokkerer commit dersom `publish_external: true` OG fila inneheld "TODO"~~ — **Ikkje utført:** Utsett til etter første eksterne organisasjon er inne; T3.2 løyser det akutte problemet

**Prioritet:** HØGST — må fikserast før reell publisering

---

### 4. `.gitignore` ekskluderer `./specs` (!)

**Problem:**  
`.gitignore` inneheld:

```
./specs
```

Dette betyr at ingenting under `./specs/` skal versjonskontrollerast, men `specs/` er fylt med dokumentasjon (`specs/done/`, `specs/backlog/`, `specs/bugs/`) som er sjekka inn i git.

**Konsekvens:**  
- Dette er inkonsistent. Anten er det ein feil, eller så er `.gitignore`-regelen ikkje aktiv (relativt vs. absolutt sti?)
- Dersom reglane vert aktive ved ein git-oppdatering kan heile `specs/`-katalogen forsvinne frå versjonskontroll

**Tiltak:**

- [x] **T4.1** — Fjern `./specs` frå `.gitignore` — `specs/` er normativ dokumentasjon og skal versjonskontrollerast

**Prioritet:** MEDIUM

---

### 5. Alle GitHub Teams peikar til same person

**Problem:**  
I `CODEOWNERS.md`:

```yaml
organizations:
  - alias: brreg
    github_team: "@AudunVindenesEggeBR"
  - alias: digdir
    github_team: "@AudunVindenesEggeBR"
  - alias: novari
    github_team: "@AudunVindenesEggeBR"
  # osv. — alle seks org peikar til same brukar
```

**Konsekvens:**  
- Dette er ein midlertidig PoC-konfigurasjon der éin person rollespelar alle organisasjonar
- Når eksterne organisasjonar vert inviterte inn må dei ha eigne GitHub-team
- `.github/CODEOWNERS`-fila vil ikkje fungere som forvendt så lenge alle peikar til same brukar

**Tiltak:**

- [x] **T5.1** — Legg til PoC-forklaring i `CODEOWNERS.md` som seier at denne konfigurasjonen er midlertidig. Eksempel:

  ```markdown
  ---
  
  ## PoC-status: midlertidig eigarskapskonfigurasjon
  
  **NB:** I PoC-fasen peikar alle `github_team`-felt til same brukar (`@AudunVindenesEggeBR`). 
  Dette er ein midlertidig konfigurasjon for testing og utvikling.
  
  **Før eksterne organisasjonar vert inviterte inn:**
  
  - Kvar organisasjon må opprette eige GitHub-team (eller utpeike minst éin GitHub-brukar med write-tilgang)
  - `github_team`-feltet i YAML-frontmatter må oppdaterast til å peike på organisasjonen sitt team
  - `.github/CODEOWNERS`-fila vert automatisk generert frå denne konfigurasjonen
  
  **Sjå òg:** [GOVERNANCE.md](GOVERNANCE.md) for fullstendig oversikt over roller og ansvar.
  
  ---
  ```
- [x] **T5.2** — Før eksterne organisasjonar vert inviterte: krev at dei opprettar eige GitHub-team og legg det til i `CODEOWNERS.md`. Eksempel på onboarding-prosess som må dokumenterast i `GOVERNANCE.md` eller `CONTRIBUTING.md`:

  ```markdown
  ## Onboarding-sjekkliste for nye organisasjonar
  
  Før ein ny organisasjon får tilgang til repoet må følgjande vere på plass:
  
  ### 1. GitHub-team eller kontaktperson
  
  Organisasjonen må anten:
  - **Alternativ A:** Opprette eit GitHub-team (t.d. `@organisasjon/linkml-forvaltning`) med minst éin medlem
  - **Alternativ B:** Utpeike minst éin GitHub-brukar med write-tilgang til repoet
  
  ### 2. Oppdater CODEOWNERS.md
  
  Legg til organisasjonen i YAML-frontmatter:
  
  ```yaml
  organizations:
    - alias: eksempelorg
      name: Eksempelorganisasjonen
      org_uri: https://data.norge.no/organizations/<orgnr>
      catalog_slug: eksempelorg-modellkatalog
      catalog_title: "Eksempelorganisasjonen - Modellkatalog"
      contact_uri: https://eksempelorg.no/kontakt
      github_team: "@eksempelorg/linkml-forvaltning"  # eller "@enkeltbrukar"
      path_patterns:
        - src/linkml/eksempelorg/**
  ```
  
  ### 3. Verifiser tilgang
  
  - Repo-administrator gir GitHub-teamet (eller brukaren) write-tilgang til repoet
  - Test at teamet kan opprette ein PR og få automatisk review-forespørsel
  ```
- [x] **T5.3** — Dokumentér i `GOVERNANCE.md` at kvar org må ha minst éin GitHub-brukar med write-tilgang til repoet. Eksempel på seksjon som skal leggjast til:

  ```markdown
  ## Tekniske krav for organisasjonar
  
  Kvar registrert organisasjon i `CODEOWNERS.md` må oppfylle følgjande tekniske krav:
  
  ### GitHub-tilgang
  
  **Minimumskrav:** Minst éin GitHub-brukar med **write-tilgang** til repoet.
  
  **Anbefalt:** Opprett eit GitHub-team (t.d. `@organisasjon/linkml-forvaltning`) med fleire medlemmar 
  for å sikre redundans ved ferie, sjukdom eller personalskifte.
  
  ### CODEOWNERS-konfigurasjon
  
  `github_team`-feltet i `CODEOWNERS.md` må peike på anten:
  - Eit GitHub-team: `"@organisasjon/teamnamn"`
  - Ein enkelt GitHub-brukar: `"@brukarnamn"`
  
  Repo-administrator gir tilgang til repoet etter at organisasjonen er godkjent (sjå onboarding-prosess).
  
  ### Ansvar
  
  Organisasjonen er ansvarleg for:
  - Å halde GitHub-teamet oppdatert med aktive medlemmar
  - Å varsle repo-administrator dersom kontaktinformasjon endrar seg
  - Å godkjenne PR-ar som endrar deira eigne domenemodeller (via `.github/CODEOWNERS`)
  ```

**Prioritet:** HØGST — må løysast før eksterne organisasjonar får tilgang

---

### 6. Publiseringsworkflow er uklar

**Problem:**  
`README.md` seier:

> "**Pull, ikkje push.** Dette repoet genererer og publiserer artefaktar til GitHub Pages og GitHub Releases. Andre system hentar artefaktane derifrå sjølve — repoet pusher aldri artefaktar til eksterne kjelder."

Dette stemmer med "pull, ikkje push"-prinsippet, men tidlegare formuleringar i `publisering-begrep.md` og `publisering-modell.md` sa "automatisk publisert til Felles Begrepskatalog/Datakatalog" — noko som kunne tolkast som at repoet pushar direkte til data.norge.no.

**Konsekvens:**  
Misforståing om ansvarsfordeling — det var ikkje klart at repoet berre tilrettelegg for høsting (via GitHub Pages) og ikkje sjølv pushar data til eksterne katalogar.

**Tiltak:**

- [x] **T6.1** — Skriv ein eigen spesifikasjonsfil `specs/backlog/publiseringsflyt-oversikt.md` som dokumenterer kva som faktisk skjer:
  - Kvar genererte filer endar (`generated/`, GitHub Pages, GitHub Releases)
  - At repoet **ikkje** har credentials for å pushe til data.norge.no — det berre tilrettelegg for høsting
  - At Felles Begrepskatalog/Datakatalog må konfigurere høsting på si side (ekstern prosess)
- [x] **T6.2** — *Omfattast no av T2.6 og T2.7* — `publisering-begrep.md` og `publisering-modell.md` skal oppdaterast til å seie "tilrettelagt for automatisk høsting" i staden for "automatisk publisert til"
- [x] **T6.3** — Legg til arkitekturdiagram i `mkdocs/docs/arkitektur-oversikt.md` (eller ny fil) som viser datautveksling mellom repo og eksterne system. Diagrammet skal vise:
  - Repoet → GitHub Pages (push)
  - GitHub Pages → Felles Begrepskatalog/Datakatalog (pull/høsting)
  - At høstinga skjer eksternt, ikkje frå repoet

**Prioritet:** HØGST — må vere tydeleg før eksterne organisasjonar vert inviterte

---

### 7. Sikkerheit og rapportering

**Problem:**  
`SECURITY.md` er veldig kort og inneheld berre:

```
Send e-post til **ave@brreg.no** med:
- Beskriving av sårbarheita
- Steg for å reprodusere problemet
```

Det manglar:

- Tidsfrist for svar
- Kven som har ansvar for sikkerheitsvurdering
- Kva som skjer dersom det er ei kritisk sårbarheit
- Om eksterne organisasjonar har eige ansvar for sikkerheit i sine domenemodeller

**Tiltak:**

- [x] **T7.1** — Utvid `SECURITY.md` med:
  - Svar innan 5 arbeidsdagar (OK — allereie der, men bør forklarast meir)
  - Kva som tel som sikkerheitssårbarheit (infrastruktur vs. domenemodell)
  - At kvar org er ansvarleg for sikkerheit i sine eigne domenemodeller
- [x] **T7.2** — Legg til seksjon i `GOVERNANCE.md` om sikkerheitsansvar ved fleire organisasjonar
- [x] **T7.3** — Legg til seksjon i `CONTRIBUTING.md` som minner bidragsytarar om å ikkje legge inn personopplysningar eller sensitive data i modellar

**Prioritet:** HØGST

---

### 8. Ingen brukarstatistikk eller monitorering

**Problem:**  
Det finst ingen dokumentasjon på:

- Om GitHub Pages-nettstaden har monitorering (besøksstatistikk, feilloggar)
- Om publisering til Felles Begrepskatalog loggast eller validérast
- Om det finst mekanisme for å trekke tilbake feil-publiserte data

**Tiltak:**

- [x] **T8.1** — Skriv `mkdocs/docs/monitorering.md` som dokumenterer korleis publisering monitorérast via GitHub Actions-loggar. Fila skal innehalde:


  **Innhald i monitorering.md:**
  
  1. **GitHub Actions-loggar** (primær monitorering i PoC-fase):
     - Korleis finne loggar: `https://github.com/brreg/linkml-datamodellering-no/actions/workflows/generate.yml`
     - Kva loggar viser: validering, generering, publisering til GitHub Pages
     - Kor lenge loggar vert lagra: 90 dagar
     - Korleis filtere etter branch, status, dato
     - Lenke til konkrete eksempel på vellukka og feila køyringar
  
  2. **Verifisere publisering**:
     - Sjekk at artefaktar er på GitHub Pages: `https://brreg.github.io/linkml-datamodellering-no/`
     - Korleis verifisere at TTL-filer er oppdaterte (sjekk Last-Modified header)
     - Korleis sjekke at høstingsendepunkt er tilgjengelege eksternt
  
  3. **Framtidige monitoreringsalternativ** (valfritt):
     - GoatCounter for besøksstatistikk (GDPR-compliant, gratis, anbefalt)
     - UptimeRobot for uptime-monitorering (gratis tier)
     - RSS-feed for releases (`/releases.atom`)
  
  4. **Avgrensingar**:
     - Repoet kan ikkje monitorere om Felles Begrepskatalog/Datakatalog faktisk høstar
     - Ingen statistikk frå data.norge.no (eksternt system)
- [x] **T8.2** — Legg til rutine for tilbaketrekking av feil-publiserte data i `GOVERNANCE.md` (Utført i T2.1 — sjå "Publiseringspolicy for eksterne katalogar" → "Tilbaketrekking av publiserte data")
- [ ] **T8.3** — Vurder å legge til CI-steg som validerer at `publish_external: true`-filer oppfyller minimum bronze-policy

**Prioritet:** MEDIUM

---

### 9. Dokumentasjon manglar viktige avgrensingar

**Problem:**  
Ingen av rettleiingane (`ny-domenemodell.md`, `ny-org.md`, osv.) nemnest:

- Kva som er støtta vs. ikkje støtta i PoC-fasen
- Kjente avgrensingar i LinkML-generatorane
- Kva som skjer dersom ein bug vert funnen i ein modell som allereie er publisert
- Om det finst SLA eller forventningar til support

**Tiltak:**

- [x] **T9.1** — Legg til "Kjende avgrensingar"-seksjon i `mkdocs/docs/index.md` som refererer til `specs/bugs/README.md`
- [x] **T9.2** — Legg til "Support og feilsøking"-seksjon i `CONTRIBUTING.md` som forklarer:
  - Dette er ein PoC — det finst ingen SLA
  - Feil rapporterast via GitHub Issues
  - Kvar org er ansvarleg for feilsøking av sine eigne modellar
- [x] **T9.3** — Utvid `specs/bugs/README.md` til å vere ein komplett oversikt over kjente avgrensingar som kan delast med eksterne

**Prioritet:** HØGST

---

### 10. Manglande dokumentasjon av rollekonfliktar

**Problem:**  
`GOVERNANCE.md` seier:

> "Repo-administrator kan override ved behov."

Men det finst ingen dokumentasjon på:

- Kva som skjer dersom repo-administrator og katalogeigarleiinga er usamde om ei endring
- Kva som skjer dersom to organisasjonar er avhengige av same AP-NO-profil og ønskjer motstridige endringar

**Tiltak:**

- [x] **T10.1** — Legg til seksjon "Konfliktløysing ved delte avhengigheiter" i `GOVERNANCE.md`
- [x] **T10.2** — Legg til eksempel på RFC-prosess for breaking changes i `GOVERNANCE.md` (med konkret døme)
- [x] **T10.3** — Dokumentér i `GOVERNANCE.md` kva som skjer dersom ein organisasjon trekkjer seg ut av repoet (eigarskapsovergang)

**Prioritet:** MEDIUM

---

### 11. CI/CD-workflows kan ikkje tilpasse seg fleire organisasjonar

**Problem:**  
Alle workflows (`generate.yml`, `release-please.yml`, osv.) føresett at det finst éin eigar (`${{ github.repository_owner }}`). Det er ikkje klart om workflows vil fungere korrekt når fleire organisasjonar samhandlar i same repo.

**Tiltak:**

- [ ] **T11.1** — Dokumentér i `GOVERNANCE.md` at alle organisasjonar må godta at CI køyrer under repo-eigar sin GitHub-konto
- [ ] **T11.2** — Vurder om det trengst per-org-image-bygging eller om alle kan dele same container-images
- [ ] **T11.3** — Test at release-please fungerer korrekt når fleire organisasjonar endrar ulike modellar i same PR

**Prioritet:** LÅGT — kan handterast etter første eksterne organisasjon er inne

---

## Prioritert handlingsliste

### Må gjerast FØR invitasjon av eksterne organisasjonar

1. **T1.1-T1.5** — Synleggjere PoC-status i all dokumentasjon
2. **T2.1-T2.5** — Avklare og dokumentere publiseringsflyt til eksterne katalogar
3. **T3.1-T3.3** — Fjerne eller fylle inn alle TODO-verdiar i produksjonsdata
4. **T5.1-T5.3** — Legg til prosess for GitHub-team per organisasjon
5. **T6.1-T6.3** — Dokumentere faktisk publiseringsflyt (ikkje berre teori)
6. **T7.1-T7.3** — Utvide sikkerheitsdokumentasjon
7. **T9.1-T9.3** — Legg til kjente avgrensingar og support-forventningar

### Kan gjerast etter første eksterne organisasjon er inne

8. **T4.1-T4.2** — Fikse `.gitignore`-regel for `./specs`
9. **T8.1-T8.3** — Legg til monitorering og tilbaketrekkingsrutiner
10. **T10.1-T10.3** — Utvide konfliktløysingsmekanismar
11. **T11.1-T11.3** — Teste og dokumentere CI/CD-flyt med fleire organisasjonar

---

## Oppsummering

Dette repoet har eit solid teknisk fundament og god struktur, men det er **ikkje klart for eksterne brukarar enno**. Hovudproblemet er:

- **Forventningsgap** — PoC-status er ikkje synleg nok
- **Dataansvar** — det er ikkje klart om produksjonsdata faktisk publiserast, og i så fall korleis kvalitet og ansvar handterast
- **Dokumentasjonsavgrensingar** — manglande "Kjente avgrensingar"-seksjonar
- **Sikkerheit og ansvar** — manglande prosedyrar for fleire organisasjonar

**Anbefaling:**  
Utfør alle "Må gjerast FØR"-tiltaka (T1-T7, T9) før eksterne organisasjonar får tilgang. Dette vil ta ~2-4 arbeidsdagar dersom utført sekvensielt. Mange av tiltaka kan gjerast parallelt.

**Forslag til neste steg:**  
1. Verifiser om GitHub Pages faktisk publiserer til data.norge.no (T2.2, T6.2)
2. Fjern eller fyll inn alle TODO-verdiar i produksjonsdata (T3.1-T3.2)
3. Legg til PoC-disclaimer i `mkdocs/docs/index.md` (T1.1)
4. Utvid `SECURITY.md` og `GOVERNANCE.md` (T7.1-T7.2)
5. Legg til "Kjende avgrensingar"-seksjon i alle hovudrettleiingar (T9.1-T9.2)
