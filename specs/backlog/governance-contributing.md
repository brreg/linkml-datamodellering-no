# Spesifikasjon: GOVERNANCE.md og oppdatert CONTRIBUTING.md

## Bakgrunn

Når repoet opnar for fleire eigarorganisasjonar (sjå `multi-org-eigarskap.md`) trengst
tydelegare rammer for:

- Kven som har myndigheit til kva (repo-administrator vs. org-eigar vs. bidragsytar)
- Korleis avgjerder om delt infrastruktur (AP-NO-profilar, tooling, CI) vert tekne
- Korleis ein ny org kjem inn og kva som krevst av dei
- Kva som gjeld for individuelle bidragsytarar (pull requests, kodegjennomgang, osv.)

### Treng vi GOVERNANCE.md?

**Ja.** Utan ein styringsmodell vil det vere uklart:
- Kven som kan godkjenne breaking changes i `common-ap-no` (som alle domenemodeller arvar)
- Kven som avgjer om ein ny org kan ta i bruk repoet
- Kva konsensus krevst for endringar i CI-pipeline eller validatorpolicyer

`CONTRIBUTING.md` handlar om _korleis_ ein bidrar teknisk. `GOVERNANCE.md` handlar om
_avgjerdsmyndigheit_ og _ansvar_ — desse er separate og begge nødvendige.

### Treng vi oppdatert CONTRIBUTING.md?

**Ja.** Gjeldande `CONTRIBUTING.md` er skriven for intern bruk i éin org. Den manglar:
- Seksjon for eksterne bidragsytarar (andre org-ar)
- Omtale av CODEOWNERS og eigarskapsprosess
- PR-godkjenningskrav (kor mange reviews, kven kan merge)
- Lenkjer til GOVERNANCE.md og ny-org.md

---

## Tiltak

### Tiltak 1 — `GOVERNANCE.md` (ny fil, repo-rota)

#### Innhald

**1. Repoeigarskap og rollar**

| Rolle | Ansvar | Kven |
|---|---|---|
| **Repo-administrator** | Godkjenner onboarding av nye org-ar, maintainer av felles infrastruktur (AP-NO, tooling, CI), kan merge til `main` | GitHub-team hos repo-host |
| **Katalogeigarleiing** | Eig og godkjenner endringar i eigen org sine domenemodeller og modellkatalog | Utpeikt person per org, registrert i `CODEOWNERS.md` |
| **Bidragsytar** | Sender PR-ar, skriv modellar, rapporterer feil | Alle med write-tilgang |

**2. Delt infrastruktur vs. domenemodeller**

- **Felles infrastruktur** (AP-NO-profilar, `common-ap-no`, CI/CD, Makefile, validator-policies,
  `src/assets/`): endringer krev review og godkjenning frå **repo-administrator**.
  Breaking changes krev RFC-prosess (sjå punkt 4).
  
- **Domenemodeller** (alt under `src/linkml/<domain>/` som ikkje er AP-NO): endringar
  krev review frå **katalogeigar for den aktuelle org-en** (via GitHub CODEOWNERS).
  Repo-administrator kan override ved behov.

- **Modellkatalogar** (`src/linkml/modellkatalog/`): kvar org eig og godkjenner sin
  eigen katalog. Endringar i `brreg-modellkatalog` krev brreg-godkjenning osv.

**3. Onboarding av ny organisasjon**

Krav for å bli registrert org i repoet:
1. Sender PR med tillegg i `CODEOWNERS.md` og katalogscaffold (`make new-org-catalog`)
2. PR vert godkjent av repo-administrator
3. Repo-administrator gir GitHub-teamet til org-en write-tilgang til repoet
4. Org-en utnemner minst eitt kontaktpunkt (namn + e-post i CODEOWNERS.md)

Det er ingen formelle krav til organisasjonstype — både offentlege verksemder,
forskningsmiljø og leverandørar kan delta. Alle modellar som vert publiserte med
`publish_external: true` må ha gyldig `dct:publisher`-URI frå `data.norge.no`.

**4. RFC-prosess for breaking changes**

Ein endring i delt infrastruktur er "breaking" viss den krev endringar i eksisterande
domenemodeller hjå registrerte org-ar. Prosess:
1. Opne eit GitHub Issue merka `RFC` og `breaking-change`
2. Diskusjonsperiode på **14 dagar** (alle org-ar varsla via Issue-kommentar)
3. Konsensus mellom repo-administrator og berørte katalogeigarleiingar
4. Repo-administrator kan override ved tryggleik- eller standard-conformance-grunnar

**5. Versjonspolitikk for AP-NO-profilar**

- Minor endringar (nye valgfrie slottar, ny warnings i policy): utan RFC
- Breaking endringar (fjerne slot, endre `required`, endre `class_uri`): krev RFC
- Versjonsnummer i schema-`version`-felt følgjer semantisk versjonering

**6. Konflikthandtering**

Ueinigheitar om endringar i felles infrastruktur:
1. Forsøk direkte dialog mellom partane i GitHub Issue
2. Repo-administrator megler om nødvendig
3. Repo-administrator har siste ord

---

### Tiltak 2 — `CONTRIBUTING.md` (oppdatering)

Behald dagens tekniske innhald, legg til/endre:

**Ny seksjon: Kven kan bidra**

```markdown
## Kven kan bidra

Alle med write-tilgang til repoet kan bidra. Det er to typar bidragsytarar:

- **Registrerte organisasjonar** — verksemder registrert i `CODEOWNERS.md` med
  eigen modellkatalog. Sjå [GOVERNANCE.md](GOVERNANCE.md) for korleis ein org
  vert registrert.
- **Individuelle bidragsytarar** — personar frå ein registrert org som bidreg
  med modellar, feilretting eller verktøyutvikling. Får tilgang gjennom sin org.

Eksterne bidragsytarar utan write-tilgang kan sende PR frå ein fork.
```

**Ny seksjon: Eigarskap og kodegjennomgang**

```markdown
## Eigarskap og kodegjennomgang

Kvar domenemodell har ein eigar-org (sjå `CODEOWNERS.md`). GitHub requestar automatisk
review frå rett team basert på `.github/CODEOWNERS`.

For din PR å bli merge-klar:
- Endringar i eigen org sine modeller: godkjenning frå éin person i same org-team
- Endringar i felles infrastruktur: godkjenning frå repo-administrator

Sjå [GOVERNANCE.md](GOVERNANCE.md) for fullstendig forklaring av roller og myndigheit.
```

**Oppdater seksjon "Ny domenemodell":**

```markdown
## Ny domenemodell

Sjå [Ny domenemodell](mkdocs/docs/ny-domenemodell.md) for steg-for-steg-rettleiing.

Om du representerer ein ny organisasjon som ikkje er registrert i `CODEOWNERS.md` enno,
sjå [Ny organisasjon](mkdocs/docs/ny-org.md) først.
```

**Oppdater seksjon "Pull request":**

Legg til krav om `make mcp-validate POLICY=bronze` og at skjema passerer lint
**før** PR vert sendt. Legg til at CI køyrer desse sjekkane automatisk.

---

## Avhengigheiter

- Tiltak 1 (`GOVERNANCE.md`) og tiltak 2 (`CONTRIBUTING.md`) er uavhengige av kvarandre
- Begge avheng konseptuelt av `multi-org-eigarskap.md` tiltak 1 (at `CODEOWNERS.md` finst)
- `ny-org.md` (tiltak 4 i `multi-org-eigarskap.md`) bør eksistere før `CONTRIBUTING.md`
  refererer til ho

## Prioritet

Medium-høg. `GOVERNANCE.md` er viktig for å setje forventningar før første eksterne org
kjem inn — det er lettare å etablere styringsmodellen tidleg enn å innføre den etterpå.
`CONTRIBUTING.md`-oppdatering er nyttig men ikkje blokkerende.

Anbefalt timing: etter tiltak 1 i `multi-org-eigarskap.md` (CODEOWNERS.md er oppretta)
og `ny-org.md`-rettleiinga er skriven.
