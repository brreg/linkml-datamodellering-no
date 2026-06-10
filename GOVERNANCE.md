# Styringsmodell (GOVERNANCE)

Dette dokumentet beskriv avgjerdsmyndigheit og ansvar for `linkml-datamodellering-no`.
For korleis ein bidrar teknisk, sjå [CONTRIBUTING.md](CONTRIBUTING.md).

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

**Domenemodeller** (alt under `src/linkml/<domain>/` som ikkje er AP-NO):
Endringar krev review frå **katalogeigarleiinga for den aktuelle org-en** (via GitHub CODEOWNERS).
Repo-administrator kan override ved behov.

**Modellkatalogar** (`src/linkml/modellkatalog/`):
Kvar org eig og godkjenner sin eigen katalog.

---

## Onboarding av ny organisasjon

Krav for å bli registrert org i repoet:

1. Send PR med tillegg i `CODEOWNERS.md` og katalogscaffold (`make new-org-catalog`)
2. PR vert godkjent av repo-administrator
3. Repo-administrator gir GitHub-teamet til org-en write-tilgang til repoet
4. Org-en utnemner minst eitt kontaktpunkt (namn + e-post i `CODEOWNERS.md`)

Det er ingen formelle krav til organisasjonstype — både offentlege verksemder,
forskningsmiljø og leverandørar kan delta. Alle modellar som vert publiserte med
`publish_external: true` må ha gyldig `dct:publisher`-URI frå `data.norge.no`.

Sjå [Ny organisasjon](mkdocs/docs/ny-org.md) for steg-for-steg-rettleiing.

---

## RFC-prosess for breaking changes

Ein endring i delt infrastruktur er «breaking» viss den krev endringar i eksisterande
domenemodeller hjå registrerte org-ar. Prosess:

1. Opne eit GitHub Issue merka `RFC` og `breaking-change`
2. Diskusjonsperiode på **14 dagar** (alle org-ar varsla via Issue-kommentar)
3. Konsensus mellom repo-administrator og berørte katalogeigarleiingar
4. Repo-administrator kan override ved tryggleik- eller standard-conformance-grunnar

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
