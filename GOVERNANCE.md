# Styringsmodell (GOVERNANCE)

Dette dokumentet beskriv avgjerdsmyndigheit og ansvar for `linkml-datamodellering-no`.
For korleis ein bidrar teknisk, sjå [CONTRIBUTING.md](CONTRIBUTING.md).

---

## PoC-status og stabilitetsnivå

Dette repoet er ein **Proof of Concept** for LinkML-basert datamodellering i norsk offentleg sektor.

### Kva eksterne organisasjonar kan forvente

**Stabilitet:**
- Modellar og verktøy er under aktiv utvikling og kan endre seg utan varsel
- Breaking changes kan skje mellom versjonar, også minor-versjonar i PoC-fasen
- AP-NO-profilar følgjer semantisk versjonering, men kan ha større endringar enn i eit produksjonssystem

**Dokumentasjon:**
- Dokumentasjonen kan vere ufullstendig eller utdatert
- Kjende avgrensingar er dokumenterte i `specs/bugs/`, men lista kan vere ufullstendig
- Rettleiingar dekkjer hovudbruken, men edge cases er ikkje alltid dokumenterte

**Support:**
- Ingen garantert responstid på GitHub Issues
- Ingen SLA for feilretting eller feature-forespurnader
- Repo-administrator prioriterer eigne behov og kritiske feil først

**Publisering:**
- Artefaktar publiserte til GitHub Pages kan endre format eller struktur
- `publish_external: true` betyr tilrettelegging for høsting, ikkje garantert publisering til Felles Begrepskatalog/Datakatalog
- Høsting frå eksterne katalogar må koordinerast manuelt med Digitaliseringsdirektoratet

**Anbefaling:** Test repoet grundig i eige miljø før de brukar det til produksjonsdata. Vurder å forke repoet dersom de treng full kontroll over endringar.

---

## Publiseringspolicy for eksterne katalogar

Denne policyen gjeld for datafiler og modellar merka med `publish_external: true` i `manifest.yaml`.

### Kva publiserast

Repoet publiserer **artefaktar til GitHub Pages** som høstingsendepunkt:

- **Begrepskatalogar:** SKOS/Turtle-filer (`.ttl`) genererte frå `src/linkml/begrepskatalog/*/data/`
- **Modellkatalogar:** ModelDCAT-AP-NO-metadata (`.ttl`) genererte frå `src/linkml/modellkatalog/*/data/`

Repoet **pusher ikkje** direkte til Felles Begrepskatalog eller Felles Datakatalog. Høsting må konfigurerast eksternt av kvar organisasjon.

### Krav i PoC-fasen

**Før `publish_external: true` kan setjast:**

1. Datafila må validere med `felles-begrepskatalog`- eller `felles-datakatalog`-policy (null feil)
2. Alle TODO-verdiar må vere fylt inn
3. Skjemaet må ha `status: http://purl.org/adms/status/UnderDevelopment` eller høgare
4. Organisasjonen må ha koordinert med Digitaliseringsdirektoratet om høstingsoppsett

**I PoC-fasen:**

- Data publisert med `publish_external: true` er å rekne som **testdata**
- Ingen garanti for stabilitet i URI-struktur eller metadata-format
- Organisasjonen er sjølv ansvarleg for kvalitet og korrektheit i publiserte data
- Tilbaketrekking av feil-publiserte data må handterast manuelt (sjå nedanfor)

### Tilbaketrekking av publiserte data

Dersom data med `publish_external: true` må trekkjast tilbake:

1. **Stopp vidare publisering:** Endre `publish_external: true` → `publish_external: false` i `manifest.yaml`
2. **Fjern frå GitHub Pages:** CI sluttar å publisere fila ved neste kjøring
3. **Varsle Digitaliseringsdirektoratet:** Send e-post til dataopen@digdir.no med URI-ar som skal fjernast frå Felles Begrepskatalog/Datakatalog
4. **Dokumentér i commit-melding:** Forklar kvifor data vart trekt tilbake

### Ansvar

- **Katalogeigarleiing:** Ansvarleg for kvalitet og korrektheit i eige org sine publiserte data
- **Repo-administrator:** Ansvarleg for at publish-mekanismen fungerer teknisk, ikkje for innhaldet
- **Digitaliseringsdirektoratet:** Ansvarleg for høsting og publisering på data.norge.no — repoet har ikkje kontroll over når/om høsting skjer

---

## Roller

| Rolle | Ansvar | Kven |
|---|---|---|
| **Repo-administrator** | Godkjenner onboarding av nye org-ar, vedlikeheld felles infrastruktur (FAIR, referanse, tooling, CI), kan merge til `main` | GitHub-team hos repo-host |
| **Katalogeigarleiing** | Eig og godkjenner endringar i eigen org sine domenemodeller og modellkatalog | Utpeikt person per org, registrert i `CODEOWNERS.md` |
| **Bidragsytar** | Sender PR-ar, skriv modellar, rapporterer feil | Alle med write-tilgang |

---

## Delt infrastruktur vs. domenemodeller

**Felles infrastruktur** (`src/linkml/ap-no/`, `src/linkml/fair/`, `src/linkml/referanse/`,
`src/assets/`, CI/CD, Makefile, validator-policies):
Endringar krev review og godkjenning frå **repo-administrator**.
Breaking changes krev RFC-prosess (sjå nedanfor).

**Unntak — release-PR:** PR-en som `release-please` opprettar automatisk
(versjonsbump, changelog, dato-annotasjonar) er unnateke krav om
review/godkjenning og auto-merges når statussjekken `validate` er grønn.
Innholdet er avgrensa til det `release-please` genererer frå conventional
commits — ikkje fritt redigerbart. Sjå `specs/done/auto-merge-release-pr.md`
for korleis dette er sett opp (bypass-rolle i branch-ruleset + PAT i
`release-please.yml`).

**Domenemodeller** (alt under `src/linkml/<domain>/` som ikkje er AP-NO):
Endringar krev review frå **katalogeigarleiinga for den aktuelle org-en** (via GitHub CODEOWNERS).
Repo-administrator kan override ved behov.

**Modellkatalogar** (`src/linkml/modellkatalog/`):
Kvar org eig og godkjenner sin eigen katalog.

---

## Onboarding av ny organisasjon

### Onboarding-sjekkliste

Før ein ny organisasjon får tilgang til repoet må følgjande vere på plass:

#### 1. GitHub-team eller kontaktperson

Organisasjonen må anten:
- **Alternativ A:** Opprette eit GitHub-team (t.d. `@organisasjon/linkml-forvaltning`) med minst éin medlem
- **Alternativ B:** Utpeike minst éin GitHub-brukar med write-tilgang til repoet

#### 2. Oppdater CODEOWNERS.md

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

#### 3. Verifiser tilgang

- Repo-administrator gir GitHub-teamet (eller brukaren) write-tilgang til repoet
- Test at teamet kan opprette ein PR og få automatisk review-forespørsel

### Krav

Det er ingen formelle krav til organisasjonstype — både offentlege verksemder,
forskningsmiljø og leverandørar kan delta. Alle modellar som vert publiserte med
`publish_external: true` må ha gyldig `dct:publisher`-URI frå `data.norge.no`.

Sjå [Ny organisasjon](mkdocs/docs/ny-org.md) for steg-for-steg-rettleiing.

---

## Utmelding og eigarskapsovergang

### Når ein organisasjon ønskjer å trekkje seg ut

Dersom ein registrert organisasjon ønskjer å trekkje seg ut av repoet:

#### Steg 1: Varsel repo-administrator

Send e-post til repo-administrator (ave@brreg.no) med:
- Grunngjeving (valfritt)
- Kva som skal skje med eksisterande modellar og data
- Tidsramme for uttrekkinga

#### Steg 2: Vel eigarskapsmodell

**Alternativ A: Behalde modellar i repoet (anbefalt)**

Modellane vert overførte til repo-administrator eller ein annan registrert organisasjon:

1. Oppdater `annotations.utgiver` i alle skjema til ny eigar sin org-URI
2. Oppdater `CODEOWNERS.md` — flytt modellar til ny eigar sin `path_patterns`
3. Flytt modellar frå `src/linkml/<gamal-org>/` til `src/linkml/<ny-org>/`
4. Oppdater modellkatalogar (`make update-modellkatalog`)
5. Deaktiver `publish_external` i datafiler (eller overfør til ny eigar)

**Alternativ B: Slette modellar frå repoet**

Berre dersom modellane er test-data eller ikkje i bruk:

1. Deaktiver `publish_external: false` i alle datafiler
2. Slett katalogane: `src/linkml/<org>/`, `src/linkml/modellkatalog/<org>-modellkatalog/`
3. Fjern org frå `CODEOWNERS.md`
4. Oppdater `.github/CODEOWNERS` (dersom automatisk generert)
5. Push endringane og vent på at GitHub Pages oppdaterar seg

**NB:** Sletting av publiserte modellar kan øydelegge eksterne avhengigheiter. Vurder å behalde modellane i ein deprecert tilstand i staden.

#### Steg 3: Trekk tilbake publiserte data (dersom relevant)

Dersom organisasjonen har publisert data til Felles Begrepskatalog/Datakatalog:

1. Deaktiver `publish_external: false` i datafiler
2. Varsle Digitaliseringsdirektoratet (dataopen@digdir.no) om at høsting skal stoppast
3. Be Digitaliseringsdirektoratet om å fjerne dataene frå data.norge.no

#### Steg 4: Fjern GitHub-tilgang

Repo-administrator fjernar GitHub-teamet (eller brukaren) sin write-tilgang til repoet.

### Når repo-administrator trekkjer seg ut

Dersom repo-administrator (Brønnøysundregistra) ønskjer å trekkje seg ut:

1. **Finn ny repo-administrator:** Ein annan registrert organisasjon må ta over administrasjonen
2. **Overfør repo:** GitHub-repoet må transfererast til ny eigar (krev GitHub-admin-tilgang)
3. **Oppdater dokumentasjon:** Alle referansar til Brønnøysundregistra i `GOVERNANCE.md`, `SECURITY.md`, osv. må oppdaterast
4. **Oppdater CI/CD:** Container-images, GitHub Actions, osv. må oppdaterast til ny eigar sin org

**Alternativ:** Dersom ingen vil ta over administrasjonen, kan repoet arkiverast (read-only) eller slettast.

---

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

---

## RFC-prosess for breaking changes

Ein endring i delt infrastruktur er «breaking» viss den krev endringar i eksisterande
domenemodeller hjå registrerte org-ar. Prosess:

1. Opne eit GitHub Issue merka `RFC` og `breaking-change`
2. Diskusjonsperiode på **14 dagar** (alle org-ar varsla via Issue-kommentar)
3. Konsensus mellom repo-administrator og berørte katalogeigarleiingar
4. Repo-administrator kan override ved tryggleik- eller standard-conformance-grunnar

### Eksempel: RFC for å gjere dct:publisher obligatorisk

**Scenario:** Digitaliseringsdirektoratet oppdaterer DCAT-AP-NO-standarden til å kreve `dct:publisher` på alle datasett. Repoet må følgje standarden.

**RFC Issue (#123):**

```markdown
# RFC: Gjer dct:publisher obligatorisk i dcat-ap-no

## Bakgrunn
DCAT-AP-NO v3.0 krev no `dct:publisher` på alle datasett. Vi må oppdatere 
`dcat-ap-no-schema.yaml` for å vere i samsvar med standarden.

## Foreslått endring
```yaml
slot_usage:
  utgiver:
    required: true  # nytt
```

## Konsekvens
- **Berørte org-ar:** Alle som importerer dcat-ap-no (Kartverket, Skatteetaten, osv.)
- **Breaking:** Ja — eksisterande modellar utan `dct:publisher` vil feile validering
- **Migreringsarbeid:** Kvar org må legge til `dct:publisher` i sine Datasett-klassar

## Tidslinje
- **Diskusjonsfrist:** 14 dagar (til 2026-07-15)
- **Staging branch:** `dcat-ap-no-v3` (opprettas 2026-07-16)
- **Migreringsperiode:** 3 månader (til 2026-10-15)
- **Merge til main:** 2026-10-15

## Alternativ
1. **Gjere det obligatorisk no** (følgje standarden)
2. **Halde det valfritt** (avvike frå standarden — ikkje anbefalt)
3. **Gjere det anbefalt** (kompromiss, men ikkje i samsvar med standard)

@kartverket @skatteetaten @novari — de har 14 dagar til å svare.
```

**Diskusjon (dag 1-14):**
- Kartverket: "Vi må sjekke om alle våre datasett har utgiver. Kan vi få 4 månader?"
- Repo-admin: "OK, forlenger migreringsperiode til 4 månader"
- Skatteetaten: "Ingen problem, vi har allereie utgiver på alt"

**Resultat:**
- ✅ Konsensus oppnådd
- 🗓️ Staging branch `dcat-ap-no-v3` opprettas 2026-07-16
- 📅 Migreringsperiode: 4 månader
- 🔀 Merge til `main` når alle org-ar er klare

---

## Versjonspolitikk for AP-NO-profilar

- **Minor endringar** (nye valfrie slottar, nye warnings i policy): utan RFC
- **Breaking endringar** (fjerne slot, endre `required`, endre `class_uri`): krev RFC

Versjonsnummer i schema-`version`-felt følgjer semantisk versjonering.

---

## Konflikthandtering

Ueinigheitar om endringar i felles infrastruktur:

1. Forsøk direkte dialog mellom partane i GitHub Issue
2. Repo-administrator megler om nødvendig
3. Repo-administrator har siste ord

---

## Sikkerheitsansvar

### Ansvarsfordeling

| Komponent | Ansvarleg for sikkerheit | Rapportering |
|---|---|---|
| Felles infrastruktur (CI/CD, containerar, AP-NO-profilar) | Repo-administrator | E-post til ave@brreg.no |
| Domenemodeller (schema, datafiler) | Katalogeigarleiing per org | GitHub Issue (`bug` eller `data-quality`) |
| Personopplysningar i datafiler | Katalogeigarleiing per org | GitHub Issue + omgåande fjerning |
| Publiserte artefaktar på GitHub Pages | Repo-administrator (infrastruktur), Katalogeigarleiing (innhald) | Avhengig av type problem |

### Katalogeigarleiing sitt ansvar

Kvar organisasjon er ansvarleg for:

- **Datakvalitet:** Sikre at domenemodeller og datafiler ikkje inneheld feil eller manglande metadata
- **Personvern:** Ikkje legge inn personopplysningar (namn, e-post, fødselsnummer, osv.) i modellar eller datafiler
- **Konfidensialitet:** Ikkje legge inn konfidensielle forretningsdata i offentlege modellar
- **Rask respons:** Fjerne sensitive data omgåande dersom dei vert oppdaga

### Repo-administrator sitt ansvar

Repo-administrator er ansvarleg for:

- **Infrastruktur-sikkerheit:** Sikre at CI/CD-pipelines, containerar og GitHub Actions-workflows ikkje har sårbarheiter
- **Secrets-handtering:** Sikre at GitHub Secrets ikkje vert lekka i loggar eller artefaktar
- **Sårbarheitsrespons:** Svare på sikkerheitsrapportar innan 5 arbeidsdagar (1 dag for kritiske)
- **Koordinering:** Koordinere fiks og ansvarleg offentleggjering ved sårbarheiter i felles infrastruktur

### Prosedyre ved oppdaga personopplysningar

Dersom personopplysningar vert oppdaga i ein domenemodell eller datafil:

1. **Oppdagar** (kven som helst) opnar GitHub Issue med merkelappen `data-quality` og `urgent`
2. **Katalogeigarleiing** for den aktuelle org-en vert varsla automatisk (via CODEOWNERS)
3. **Katalogeigarleiing** må:
   - Fjerne dei sensitive dataa frå fila
   - Pushe ein fix til `main` innan 24 timar
   - Vurdere om git-historikk må renskast (kontakt repo-administrator)
4. **Repo-administrator** hjelper med force-push eller history-rewrite om nødvendig

Sjå [SECURITY.md](SECURITY.md) for fullstendig sikkerheitspolicy.

---

## Konfliktløysing ved delte avhengigheiter

Når fleire organisasjonar brukar same repo kan det oppstå konfliktar om endringar i delte komponentar (AP-NO-profilar, FAIR-metadata, felles verktøy).

### Scenario 1: To org-ar ønskjer motstridige endringar i same AP-NO-profil

**Døme:** Organisasjon A ønskjer å gjere `dct:title` obligatorisk (`required: true`) i `dcat-ap-no`, medan organisasjon B ønskjer at det skal vere valfritt.

**Prosess:**

1. **RFC-prosess startar:** Den som foreslår endringa opnar eit GitHub Issue merka `RFC` og `breaking-change`
2. **Diskusjonsperiode (14 dagar):** Alle registrerte org-ar vert varsla via kommentar på Issue
3. **Forhandling:** Organisasjonane diskuterer i Issue-kommentarar eller i direkte dialog
4. **Mogleg løysing:**
   - **Kompromiss:** Gjer feltet anbefalt (`in_subset: Anbefalt`) i staden for obligatorisk
   - **Forking:** Organisasjon A opprettar eigen profil (`org-a-dcat-ap-no`) som arvar frå `dcat-ap-no` og legg til `required: true` i `slot_usage`
   - **Konsensus:** Éin part trekkjer forslaget sitt
5. **Repo-administrator avgjer:** Dersom ingen konsensus etter 14 dagar, har repo-administrator siste ord

**Prinsipp:** Prioriter kompromiss som gjer alle fornøgde. Breaking changes i delte komponentar krev sterk grunngjeving (t.d. standard-conformance, sikkerheit).

### Scenario 2: Repo-administrator og katalogeigarleiing er usamde

**Døme:** Katalogeigarleiing ønskjer å publisere ein modell med `publish_external: true`, men repo-administrator meiner datakvaliteten er for låg.

**Prosess:**

1. **Dialog:** Repo-administrator forklarar kvifor datakvaliteten er for låg (t.d. mange TODO-verdiar, manglar obligatoriske felt)
2. **Forbetringsplan:** Katalogeigarleiing får ei liste over kva som må rettast før publisering
3. **Re-evaluering:** Etter at rettingane er gjort, vurderast publisering på nytt
4. **Override-kriterium:** Repo-administrator kan berre blokkere publisering dersom:
   - Datafila ikkje validerer med `felles-begrepskatalog`- eller `felles-datakatalog`-policy (teknisk krav)
   - Publisering bryt med "pull, ikkje push"-prinsippet eller publiseringspolicy (sjå [Publiseringspolicy](#publiseringspolicy-for-eksterne-katalogar))
   - Publisering utgjer ein sikkerheitsrisiko (t.d. lekking av credentials, personopplysningar)

**Prinsipp:** Repo-administrator kan ikkje blokkere publisering av gyldig data berre pga. subjektive kvalitetsoppfatningar. Tekniske krav (validering, policy) er objektive og ikkje opp til forhandling.

### Scenario 3: Breaking change i AP-NO-profil påverkar fleire org-ar

**Døme:** `dcat-ap-no` må oppdaterast til ein ny versjon av DCAT-AP-EU-standarden. Oppgraderinga krev endringar i alle domenemodeller som importerer `dcat-ap-no`.

**Prosess:**

1. **RFC opnast:** Repo-administrator (eller kven som helst) opnar RFC med analyse av konsekvensane
2. **Koordineringsperiode (14 dagar):** Alle berørte org-ar diskuterer migreringsplan
3. **Staging-branch:** Breaking change vert gjort på ein eigen branch (t.d. `dcat-ap-no-v3`)
4. **Parallell migreringsperiode:** Kvar org migrerer sine modellar til ny branch i eige tempo (inntil 3 månader)
5. **Merge til main:** Når alle org-ar er klare, vert staging-branch merga til `main`

**Prinsipp:** Breaking changes i delte komponentar krev koordinering og tilstrekkeleg migreringstid. Ingen org skal tvingjast til å migrere raskare enn dei har kapasitet til.

### Eskalering

Dersom ein konflikt ikkje kan løysast gjennom dialog eller RFC-prosess:

1. **Megling:** Repo-administrator fungerer som megler mellom partane
2. **Votering:** Dersom repoet har fleire enn 5 registrerte org-ar, kan det gjennomførast ein avstemming (éin stemme per org)
3. **Siste ord:** Repo-administrator har siste ord, men bør alltid prioritere konsensus

**NB:** I PoC-fasen er det berre éin aktiv organisasjon (Brønnøysundregistra), så desse prosedyrane er førebuande for framtidig bruk.
