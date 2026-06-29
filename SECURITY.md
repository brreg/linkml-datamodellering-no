# Sikkerheit

## Rapporter ein sårbarheit

Bruk **ikkje** public GitHub Issues for å rapportere sikkerheitssårbarheiter.

Send e-post til **ave@brreg.no** med:
- Beskriving av sårbarheita
- Steg for å reprodusere problemet
- Mogleg verknad
- Påverka komponentar (infrastruktur, CI/CD, domenemodell, osv.)

**Vi svarer innan 5 arbeidsdagar** med:
- Stadfesting på motteken rapport
- Innleiande vurdering av alvorlighetsgrad
- Forventa tidsramme for undersøking og eventuell fiks

Vi koordinerer ansvarleg offentleggjering saman med deg.

---

## Kva tel som sikkerheitssårbarheit

### Infrastruktur og CI/CD

**Sikkerheitssårbarheiter som bør rapporterast:**

- Kjeldekodeinjeksjon i CI-pipelines (t.d. uvalidert input i GitHub Actions)
- Lekking av credentials eller secrets i loggar eller artefaktar
- Utilsikta eksponering av intern infrastruktur
- Sårbarheiter i containerar (Dockerfile, dependencies)
- Ukontrollert ekstern input i `Makefile`, shell-skript eller Python-skript

**Ansvarleg:** Repo-administrator

### Domenemodeller og data

**IKKJE sikkerheitssårbarheiter, men datakvalitetsproblem:**

- Feil i ein domenemodell (t.d. feil `class_uri`, ugyldig YAML)
- Personopplysningar eller sensitive data i modellar/datafiler
- Feil metadata i begrepskatalogar eller modellkatalogar

**Ansvarleg:** Katalogeigarleiing for den aktuelle organisasjonen

**Korleis rapportere:** Opne ein public GitHub Issue med merkelappen `bug` eller `data-quality`

---

## Ansvarsfordeling

| Type problem | Ansvarleg | Rapporteringsmåte |
|---|---|---|
| Infrastruktur-sårbarheit (CI/CD, containerar, secrets) | Repo-administrator | **E-post til ave@brreg.no** |
| Sårbarheit i felles verktøy (mcp-linkml-validator, mcp-linkml-modell-utkast) | Repo-administrator | **E-post til ave@brreg.no** |
| Feil i domenemodell (feil URI, ugyldig YAML) | Katalogeigarleiing | GitHub Issue (`bug`) |
| Personopplysningar i datafiler | Katalogeigarleiing | GitHub Issue (`data-quality`) + fjern data omgåande |
| Sårbarheit i AP-NO-profilar (felles infrastruktur) | Repo-administrator | **E-post til ave@brreg.no** |

---

## Personopplysningar og sensitive data

**Kvar organisasjon er ansvarleg for:**

- Å ikkje legge inn personopplysningar (namn, e-post, fødselsnummer, osv.) i domenemodeller eller datafiler
- Å ikkje legge inn konfidensielle forretningsdata i offentlege modellar
- Å fjerne sensitive data omgåande dersom dei vert oppdaga

**Dersom du oppdagar personopplysningar i ein domenemodell:**

1. Opne ein GitHub Issue med merkelappen `data-quality` og `urgent`
2. Tagg katalogeigarleiinga for den aktuelle organisasjonen (sjå `CODEOWNERS.md`)
3. **Ikkje inkluder dei sensitive dataa i issue-beskrivinga** — skriv berre kvar dei ligg (filsti og linjenummer)

**Katalogeigarleiinga må:**

1. Fjerne dei sensitive dataa frå fila
2. Pushe ein fix til `main` omgåande
3. Kontakte repo-administrator for å vurdere om git-historikk må renskast (force-push)

---

## Kritiske sårbarheiter

Dersom ein sårbarheit er **kritisk** (t.d. lekking av credentials, RCE i CI/CD):

1. Send e-post til **ave@brreg.no** med `[CRITICAL]` i subject-linja
2. Vi svarer innan **1 arbeidsdagdag**
3. Offentleggjering vert utsett til ein fix er tilgjengeleg

Dersom du ikkje får svar innan 2 arbeidsdagar, kontakt [GitHub Security Advisory](https://github.com/brreg/linkml-datamodellering-no/security/advisories).
