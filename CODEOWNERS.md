```yaml
organizations:
  - alias: brreg
    name: Brønnøysundregistra
    org_uri: https://data.norge.no/organizations/974760673
    catalog_slug: brreg-modellkatalog
    catalog_title: "Brønnøysundregistra – Modellkatalog"
    contact_uri: https://brreg.no/kontakt/modellforvaltning
    github_team: "@AudunVindenesEggeBR"
    path_patterns:
      - src/linkml/ngr/ngr-virksomhet/**
      - src/linkml/oreg/enhetsregisteret-bvrinn/**
      - src/linkml/oreg/register-over-aksjeeiere/**

  - alias: digdir
    name: Digitaliseringsdirektoratet
    org_uri: https://data.norge.no/organizations/991825827
    catalog_slug: digdir-modellkatalog
    catalog_title: "Digitaliseringsdirektoratet – Modellkatalog"
    contact_uri: https://www.digdir.no/om-oss/kontakt-oss/887
    github_team: "@AudunVindenesEggeBR"
    path_patterns:
      - src/linkml/ap-no/**

  - alias: novari
    name: Novari IKS
    # Verifiser orgnr mot Brønnøysundregistrene: søk på "Novari IKS"
    org_uri: https://data.norge.no/organizations/985870714
    catalog_slug: novari-modellkatalog
    catalog_title: "Novari IKS – Modellkatalog (FINT)"
    contact_uri: https://novari.no/kontakt
    github_team: "@AudunVindenesEggeBR"
    path_patterns:
      - src/linkml/fint/**

  - alias: ksdigital
    name: KS Digital
    # KS Digital er ein del av KS (Kommunesektorens organisasjon). Orgnr for KS.
    org_uri: https://data.norge.no/organizations/971032146
    catalog_slug: ksdigital-modellkatalog
    catalog_title: "KS Digital – Modellkatalog"
    contact_uri: https://www.ks.no/fagomrader/digitalisering/
    github_team: "@AudunVindenesEggeBR"
    path_patterns:
      - src/linkml/samt/**

  - alias: skatteetaten
    name: Skatteetaten
    org_uri: https://data.norge.no/organizations/974761076
    catalog_slug: skatteetaten-modellkatalog
    catalog_title: "Skatteetaten – Modellkatalog"
    contact_uri: https://www.skatteetaten.no/kontakt/
    github_team: "@AudunVindenesEggeBR"
    path_patterns:
      - src/linkml/ngr/ngr-person/**

  - alias: kartverket
    name: Kartverket
    org_uri: https://data.norge.no/organizations/971040238
    catalog_slug: kartverket-modellkatalog
    catalog_title: "Kartverket – Modellkatalog"
    contact_uri: https://www.kartverket.no/om-kartverket/kontakt-oss/
    github_team: "@AudunVindenesEggeBR"
    path_patterns:
      - src/linkml/ngr/ngr-adresse/**
      - src/linkml/ngr/ngr-eiendom/**
```

# Modelleigarskapar (CODEOWNERS)

Dette dokumentet er det autoritative registeret over kva organisasjon som eig kva
domenemodell i dette repoet. Det tener to føremål:

1. **Maskinleseleg eigarskapsregister** — YAML-frontmatter vert lese av
   `src/assets/scripts/update-modellkatalog.py` for å opprette og oppdatere per-org
   modellkatalogar.
2. **Dokumentasjon** — forklarer eigarskapsmodellen og er utgangspunkt for `.github/CODEOWNERS`.

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

## Korleis eigarskap fungerer

Eigarskapet til ein domenemodell er definert av `annotations.utgiver`-feltet i skjemafila
(`*-schema.yaml`). Dette feltet inneheld ein URI på forma
`https://data.norge.no/organizations/<orgnr>` og peiker på eigarorganisasjonen.

`CODEOWNERS.md` treng **ikkje** liste individuelle modellar — berre
organisasjonsnivå-metadata (katalognamn, kontaktpunkt, GitHub-team) som ikkje kan
leias ut frå skjemaet åleine.

```
annotations.utgiver  ────→  org_uri i CODEOWNERS.md  ────→  modellkatalog
(i *-schema.yaml)          (maskinleseleg)                   (datafil per org)
```

## Felles infrastruktur (utan eigar-org)

Desse mappane er felles infrastruktur og er ikkje knytte til ein enkelt org:

| Mappe | Innhald |
|---|---|
| `src/linkml/ap-no/` | AP-NO-profilar (dcat-ap-no, dqv-ap-no, skos-ap-no, …) |
| `src/linkml/fair/` | FAIR-metadata-profil |
| `src/linkml/referanse/` | Referanseskjema (dokumentasjon) |
| `src/assets/` | Skript, CI-hjelparar, validatorpolicyer |

Endringar i felles infrastruktur krev godkjenning frå repo-administrator (sjå `GOVERNANCE.md`).

## Registrerte organisasjonar

| Alias | Organisasjon | Org-URI | Katalog | Modellar |
|---|---|---|---|---|
| `brreg` | Brønnøysundregistra | `https://data.norge.no/organizations/974760673` | `brreg-modellkatalog` | `ngr-virksomhet`, `oreg/enhetsregisteret-bvrinn`, `oreg/register-over-aksjeeiere` |
| `digdir` | Digitaliseringsdirektoratet | `https://data.norge.no/organizations/991825827` | `digdir-modellkatalog` | `ap-no/**` |
| `novari` | Novari IKS | `https://data.norge.no/organizations/985870714`¹ | `novari-modellkatalog` | `fint/**` |
| `ksdigital` | KS Digital | `https://data.norge.no/organizations/971032146` | `ksdigital-modellkatalog` | `samt/**` |
| `skatteetaten` | Skatteetaten | `https://data.norge.no/organizations/974761076` | `skatteetaten-modellkatalog` | `ngr-person` |
| `kartverket` | Kartverket | `https://data.norge.no/organizations/971040238` | `kartverket-modellkatalog` | `ngr-adresse`, `ngr-eiendom` |

> ¹ Verifiser orgnr for Novari IKS mot [Brønnøysundregistrene](https://www.brreg.no/) ved onboarding.

## Legg til ny organisasjon

Sjå [Ny organisasjon](mkdocs/docs/ny-org.md) for steg-for-steg-rettleiing.

Kort oppsummert:
1. Legg til org i YAML-frontmatter over (PR til `main`)
2. Køyr `make new-org-catalog ORG=<alias>` for å opprette katalogstruktur
3. Legg til `annotations.utgiver` i skjemaa med org sin URI
4. Køyr `make update-modellkatalog` for å synkronisere katalogen
