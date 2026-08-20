# Rettleiing: ny modelleigar

!!! note "Beskrivelse"

    Denne rettleiinga forklarer korleis ein ny organisasjon tek i bruk repoet for å
    publisere eigne informasjonsmodellar saman med Brønnøysundregistra og andre verksemder.

## Føresetnader

Same som for [ny domenemodell](ny-domenemodell.md):

```bash
make check-prereqs
make linkml-build-docker && make python-build-docker && make mcp-val-build
```

## Steg 1 — Registrer organisasjonen i CODEOWNERS.md

Legg til organisasjonen i YAML-frontmatter i `CODEOWNERS.md` (repo-rota).

```yaml
organizations:
  # ... eksisterande organisasjonar ...
  - alias: <alias>                          # kort nøkkel, t.d. digdir, ssb, kartverket
    name: <Organisasjonsnavn>
    org_uri: https://data.norge.no/organizations/<9-sifra orgnr>
    catalog_slug: <alias>-modellkatalog     # mappenavn, t.d. digdir-modellkatalog
    catalog_title: "<Org> - Modellkatalog"
    contact_uri: https://<org-domene>/kontakt/modellforvaltning
    github_team: "@<github-org>/<team>"
    path_patterns:
      - src/linkml/<domain>/**              # mappane org-en eig
```

Send **pull request** mot `main` med denne endringa. Repo-administratoren godkjenner
PR-en og gir GitHub-teamet write-tilgang til repoet (sjå `GOVERNANCE.md`).

## Steg 2 — Scaffold modellkatalog

Etter godkjent PR, opprett katalogstrukturen:

```bash
make new-modellkatalog ORG=<alias>
```

Dette oppretter:
```
src/linkml/modellkatalog/<alias>-modellkatalog/
├── <alias>-modellkatalog-schema.yaml    ← LinkML-skjema for katalogen
├── build.yaml                         ← publish_external: true
├── examples/
│   └── <alias>-modellkatalog-eksempel.yaml
└── data/
    └── <alias>-modellkatalog/
        ├── <alias>-modellkatalog.yaml    ← katalogdatafil (med TODO-verdiar)
        └── build.yaml
```

Fyll inn `TODO`-verdiane i datafila manuelt:
- `tittel` og `beskrivelse` på katalogen
- `har_del`-lista (vert automatisk synkronisert seinare av `gen-modellkatalog-instance`, sjå Steg 4)
- Navn på kontaktpunkt i `aktoerer`-lista

## Steg 3 — Opprett domenemodellar

```bash
make new-modell DOMAIN=<domene> NAME=<modell>
```

Opne den genererte skjemafila og set `annotations.utgiver` til org-en sin URI:

```yaml
annotations:
  utgiver: https://data.norge.no/organizations/<orgnr>
  endringsdato: "YYYY-MM-DD"
  utgivelsesdato: "YYYY-MM-DD"
  status: http://purl.org/adms/status/UnderDevelopment
  oppdateringsfrekvens: http://publications.europa.eu/resource/authority/frequency/IRREG
```

Sjå [Ny domenemodell](ny-domenemodell.md) for full rettleiing om korleis ein modellerer.

## Steg 4 — Synkroniser modellkatalog

!!! warning "Endra frå `update-modellkatalog` til `gen-modellkatalog-instance`"

    `make update-modellkatalog` (patcha berre utvalde felt i eksisterande
    katalogoppføringar, og skreiv `TODO`-stubs for uregistrerte skjema) er
    fjerna. `make gen-modellkatalog-instance` **regenererer heile
    katalogfila frå botnen** ut frå kvart skjema sin genererte
    Informasjonsmodell-instans — han skriv ikkje lenger `TODO`-stubs for
    felt som `tema`/`lisens`/`kontaktpunkt` som manglar kjelde. Sjå
    [spesifikasjonen for grunngjevinga](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/done/make-target-namn-vs-funksjon.md).
    Verifiser at manuelt utfylte felt i eksisterande katalogoppføringar
    framleis er korrekte etter fyrste køyring med den nye kommandoen.

Etter at skjema har korrekt `annotations.utgiver`, generer
Informasjonsmodell-instansen (dersom han ikkje alt finst, t.d. via
`make domain-<domene>`) og synkroniser deretter katalogdatafila:

```bash
make gen-informasjonsmodell-instance SCHEMA=<sti-til-skjema>
make gen-modellkatalog-instance
```

Kommandoen finn alle genererte Informasjonsmodell-instansar
(`metadata/modelldcat.yaml`) med `utgiver` matchande org-URI, og bygger
katalogdatafila for organisasjonen på nytt frå desse.

**Konvensjon:** Modellkatalogen skal liste **alle** skjema org-en forvaltar — også
modellar som ikkje er ferdige enno. Sett `annotations.status` til
`http://purl.org/adms/status/UnderDevelopment` for utkast. Modellkatalogen er den
maskinlesbare oversikta rettleiaren *Veileder for tilgjengeliggjøring av åpne data*
krev (jf. punkt 12 — «òg for data som ikkje er tilgjengelege enno»), så ufullstendige
modellar skal vere synlege i katalogen med korrekt status, ikkje utelatne til dei er
klare.

## Steg 5 — Valider

Valider kvar enkelt domenemodell:
```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=silver
```

Valider modellkatalogen mot publiseringspolicy:
```bash
make mcp-linkml-valider-modell \
  SCHEMA=src/linkml/modellkatalog/<alias>-modellkatalog/<alias>-modellkatalog-schema.yaml \
  POLICY=felles-datakatalog \
  INSTANCE=src/linkml/modellkatalog/<alias>-modellkatalog/data/<alias>-modellkatalog/<alias>-modellkatalog.yaml
```

Sjå [Valideringsreglar](../arkitektur/valideringsregler.md) for fullstendig oversikt.

## Steg 6 — Send pull request

Lag ein PR mot `main` med:
- Nye domenemodellar i `src/linkml/<domain>/`
- Oppdatert `CODEOWNERS.md` (om ikkje gjort i steg 1)
- Ny katalogstruktur i `src/linkml/modellkatalog/<alias>-modellkatalog/`

CI køyrer lint, instansvalidering og policy-sjekkar automatisk. Alle sjekkar må passere
før PR-en kan mergast.

---

## Tverretatleg samarbeid

### Importere ap-no profil

Alle AP-NO-profilar i `src/linkml/ap-no/` er felles infrastruktur og kan importerast
av alle domenemodellar uavhengig av eigar-org:

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
```

### Foreslå endringar i felles infrastruktur

Endringar i `src/linkml/ap-no/`, `src/assets/` eller `Makefile` krev godkjenning frå
repo-administrator (sjå `GOVERNANCE.md`). Send ein PR og skriv tydeleg i PR-beskrivselen
kvifor endringa er nødvendig og om ho er bakoverkompatibel.

Breaking changes (fjerne/endre eksisterande slottar eller klasser) krev ein RFC-prosess
med 14 dagars diskusjonsperiode — sjå `GOVERNANCE.md` for detaljar.

### Referere til ein annan org sin modell

Alle modellar i dette repoet er offentlige og kan gjenbrukes i andre modellar.

Bruk `schema_id`-URIen frå den andre org sin modell som `slot_uri` eller `class_uri`:

```yaml
imports:
  - linkml:types
  - ../../dcat-ap-no/dcat-ap-no-schema
  # Importer ikkje direkte frå ein annan org sin domenemodell —
  # bruk heller eit felles AP-NO-importlag
```

---

## Tilgang og kontakt

For å få write-tilgang til repoet, kontakt repo-administrator via GitHub Issues.
Sjå `GOVERNANCE.md` for formelle krav og prosess.

---

## Kjende avgrensingar

Denne rettleiinga dekkjer onboarding av nye organisasjonar i repoet. 
Følgjande avgrensingar gjeld i PoC-fasen:

### Organisasjonsstruktur

- Alle organisasjonar må ha éin felles modellkatalog — støtte for fleire katalogar per org er ikkje implementert
- GitHub-team-konfigurasjonen krev at alle medlemmar har write-tilgang til heile repoet (ikkje berre eigne modellar)

### Automatisering

- `make gen-modellkatalog-instance` regenererer katalogfila frå Informasjonsmodell-instansar, men fyller ikkje inn felt utan kjelde (t.d. `tema`/`lisens`) automatisk
- `.github/CODEOWNERS`-fila må oppdaterast manuelt basert på `CODEOWNERS.md` — ingen automatisk synkronisering enno

### Samhandling

- Dersom to org-ar treng motstridige endringar i same AP-NO-profil må dette løysast gjennom RFC-prosess (sjå GOVERNANCE.md)
- Konfliktløysingsmekanismar er ikkje fullt dokumenterte enno

**Fullstendig oversikt:** Sjå [BUGS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/BUGS.md) for komplett liste over kjende bugs og workarounds.

**Rapporter nye problem:** Opne eit [GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) med merkelappen `bug`.

## Relatert dokumentasjon

- [Ny domenemodell](ny-domenemodell.md) — opprette nytt skjema for den nye organisasjonen
- [Ny begrepskatalog](ny-begrepsmodell.md) — opprette ny begrepskatalog for den nye organisasjonen
- [GOVERNANCE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/GOVERNANCE.md) — roller, eigarskap og RFC-prosess
