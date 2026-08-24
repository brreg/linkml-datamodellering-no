# CLAUDE.md

## Referansedokument

Desse dokumenta er autoritative kjelder — ikkje dupliser innhald herifrå i CLAUDE.md:

- **[SCOPE.md](SCOPE.md)** — kva repoet er, kva det ikkje er, kva som høyrer heime her, funksjonalitet
- **[PRINCIPLES.md](PRINCIPLES.md)** — dei 6 grunnleggjande designprinsippa (pull vs push, containerisering, import-hierarki, lenking, slots vs attributes, skriftspråk)
- **[CONVENTIONS.md](CONVENTIONS.md)** — navnekonvensjonar, manifestformat, commit-meldingar
- **[GOVERNANCE.md](GOVERNANCE.md)** — roller, eigarskap, RFC-prosess, versjonspolitikk

## Arbeidsflyt

**Ved kvar brukarinstruksjon:**

1. **Les tilbake instruksjonen** — skriv i 1-2 setningar kva du har forstått at brukaren vil ha gjort
2. **Avklar antakelser** — dersom du må gjere val eller antakelser for å utføre instruksjonen, spør brukaren om desse før du startar arbeidet
3. **Skriv spesifikasjon** — opprett ei ny spec i `specs/backlog/<kortnavn>.md` med bakgrunn, nummererte steg og handlingsliste. **Unntak:** dersom du allereie jobbar med å realisere tiltak i ein eksisterande spec i `specs/backlog/`, treng du ikkje opprette ny spec
4. **Utfør arbeidet** — følg spesifikasjonen og oppdater han etter kvart steg
5. **Avslutning** — når alle tiltak er utførte: (a) generer kompakt commit-melding, (b) legg til `## Utført`-seksjon i specen, (c) flytt specen til `specs/done/`

**Når treng du ikkje ny spec?**
- Du utfører allereie tiltak frå ein eksisterande spec i `specs/backlog/`
- Brukaren ber eksplisitt om å **ikkje** lage spec (t.d. "fiks raskt utan spec")
- Det er ein triviell endring (t.d. "rett stavefeil i linje 42")

## Førende prinsipper
- Ingen avhengigheter skal installeres lokalt. Alt skal kjøres som containere med podman i WSL2.
- **Bruk Makefile-targets:** Køyr **alltid** LinkML-verktøy via `make`-kommandoane dokumenterte i `COMMANDS.md` (t.d. `make gen-doc`, `make gen-plantuml`, `make lint`). **Aldri** køyr podman/linkml-kommandoar direkte — Makefile sikrar korrekte flagg, container-image, volum-mount og versjonskonsekvens. Manuell køyring kan gi feil artefakter (t.d. manglande `--no-hierarchical-class-view` i gen-doc). Einaste unntak er når du feilsøkjer eller utviklar nye Makefile-targets.
- **Aldri commit eller push:** LLM skal **aldri** kjøre `git commit`, `git push`, `git add`, `git stash` eller andre git-kommandoar som endrar versjonskontroll-tilstand. LLM skal heller **aldri** foreslå at brukaren skal committe, pushe eller organisere commits. Brukaren kontrollerer all versjonskontroll sjølv. Generer utkast til commit-meldingar (sjå under) for å dokumentere kva som er endra, men lat brukaren utføre alle git-kommandoar sjølv.
- **Pull, ikkje push:** Dette repoet genererer artefakter som andre system kan hente (pull) — via GitHub Pages, GitHub Releases eller `raw.githubusercontent.com`. Repoet skal **aldri** sjølv pushe artefakter til eksterne kjelder (schema-registry, API-katalogar, datakatalogar o.l.), fordi slik integrering krev spesialtilpassingar per målsystem og gjer repoet avhengig av ekstern tilgjengelegheit og autentisering. Dersom nokon ber om å implementere push-funksjonalitet mot ein ekstern kjelde, avslå og forklar prinsippet.
- **Følg arbeidsflyten:** Sjå seksjonen "Arbeidsflyt" ovanfor for korleis instruksjonar skal handterast (les tilbake → avklar → skriv spec → utfør → avslutt).
- **Commit-melding etter kvar endring:** Etter *kvar* arbeidsøkt der filer er endra — uavhengig av om det er ei spesifikasjon, ein bugfix, ein konfigurasjonsjustering eller anna — skal det alltid genererast eit utkast til commit-melding i conventional commits-format (sjå `specs/done/conventional-commits-modellversjonering.md` for typar, scope-konvensjon og døme). Generer meldinga til slutt i svaret, utan å spørje om løyve.
- **DRY — ikkje gjenta deg sjølv:** Kvar regel, klasse, slot og kommando skal ha éi kjelde. I LinkML-skjema: definer klasser/slots éin stad og importer. I CLAUDE.md: ikkje gjenta forklåringar som finst i `mkdocs/docs/` — legg til kryssreferanse i staden. Terskel: tre eller fleire identiske tilfelle. To like tilfelle krev ingen abstraksjon. `specs/done/` er unntatt — arkiverte spesifikasjonar skal stå urørte og treng ikkje konsoliderast. Omskriv aldri eksisterande kode eller konfigurasjon med DRY som einaste grunngjeving utan å spørje brukaren om løyve først. Regelen er handheva systematisk for make-/Python-/CI-laget (hardkoda lister erstatta med dynamisk oppslag, dupliserte funksjonar konsoliderte til delte modular) — sjå `specs/done/dry-opprydding.md` for metode og eksempel.
- **Nye verktøyavhengigheiter:** Legg du til eit verktøy i `Dockerfile*`, `requirements*.txt` eller `.github/workflows/*.yml` som endar opp bundla i eit publisert containerbilete eller i den publiserte mkdocs-portalen, sjekk om lisensen krev attribution og oppdater attributions-tabellen i `mkdocs/docs/om.md`. Sjå `CONTRIBUTING.md` (seksjonen «Nye verktøyavhengigheiter») og `specs/done/verktoy-lisensoversikt.md` for metode.
- **Ingen stille feil:** Nye script og funksjonar skal **aldri** kunne feile utan at feilen vert logga synleg, minimum ved `LOGLVL=ERROR` (default-nivå). I `make/*.mk`: aldri `> /dev/null 2>&1` (eller tilsvarande) rundt ein kommando som kan feile — bruk `run_logged "<label>" <kommando>` frå `LOG_FUNCTIONS` (sjå `COMMANDS.md` § «Ingen stille feil»). I Python-script under `src/assets/scripts/` og `mkdocs/lib/scripts/`: bruk `error_handler.log_error()` for uventa unntak, og spesifiser alltid unntakstype — ein bar `except:`/`except Exception:` utan eksplisitt logging er ikkje tillate. Ein bevisst, mjuk fallback (t.d. "brukar default-verdi") skal framleis skrive éi linje til stderr om kvifor — mjuke åtvaringar er greitt, stille feil er det ikkje. Sjå `specs/done/ingen-stille-feil.md` for grunngjeving og eksempel.
- **Actionlint etter CI-endring:** Etter *kvar* endring i `.github/workflows/*.yml` skal `actionlint` køyrast mot den endra fila før arbeidet vert rekna som ferdig. GitHub Actions evaluerer `${{ }}`-uttrykk overalt i eit `run:`-steg — også inni kommentarar — så eit bokstaveleg tomt `${{ }}` eller anna ugyldig uttrykk får heile workflowen til å feile ved parse-tid, utan at éin einaste jobb køyrer (synest som ei 0-sekunds "workflow file issue"-feiling i Actions-historikken). Køyr via podman, aldri lokal installasjon: `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/<fil>.yml`. Berre feil av typen `[expression]` (og andre reelle syntaks-/schemafeil) blokkerer — `[shellcheck]`-funn er stilråd og treng ikkje rettast som del av same endring.
- **Kompakt commit-format:** Commit-meldingar skal vere **så kompakte som mogleg** og følgje conventional commits-formalismen. Meldinga skal skrivast i **presens** og kun innehalde **kva som er endra** (ikkje kvifor eller bakgrunn — det finst i specen/koden). Format: éi hovudlinje (`<type>(<scope>): <skildring>`) og éin kort bullet per endra fil/komponent. Unngå lange forklarande avsnitt; bruk stikkord. **Inkluder ALDRI `Co-Authored-By:`-linje i utkast til commit-meldingar** — brukaren legg det til manuelt ved commit dersom det er ønskt. Døme:
  ```
  fix(mcp-modell-utkast): prioriter multivalued og primitive typar i slot-konfliktar
    - converter.py: prioriter multivalued over single-value, primitive over klasse-ref
    - tests/test_make.sh: normaliser property-navn (bindestrek → underscore)
    - specs/done/json-schema-roundtrip-test.md: alle tre testar passerer
  ```

## LinkML Importhierarki

Sjå [PRINCIPLES.md § 3](PRINCIPLES.md#3-modularitet-via-import-hierarki) og [mkdocs/docs/arkitektur/importhierarki.md](mkdocs/docs/arkitektur/importhierarki.md) for fullstendig importhierarki, konkrete YAML-eksempel, reglar og versjonslåsing-rettleiing.

**Hovudpunkt:**
- `common-ap-no-schema` importerer `linkml:types` — berre AP-NO-profilene importerer denne direkte
- Domenemodellar importerer AP-NO-profilene (t.d. `dcat-ap-no-schema`), ikkje `common-ap-no-schema`
- `fint-common-schema` er felles for alle FINT-modellar
- `fair-metadata-schema` kan kombinerast med både AP-NO, FINT og oreg-skjema

Importhierarkiet er repoets primære DRY-mekanisme for skjema: klasser og slots definerast éin stad og importerast nedover. MC8-MC11 (sjå `specs/done/avvik-modelldcat-ap-no.md`) er eit praktisk døme — duplikate klasser vart fjerna frå `modelldcat-katalog-schema.yaml` ved å importere `dcat-ap-no-schema` i staden.


## Valider arbeidet ditt

```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
make lint SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
make validate-instance SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml INSTANCE=src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml

# Rask roundtrip-verifisering (JSON og TTL) — ~30 sek i staden for ~3 min:
make roundtrip SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml

# MCP-validator dersom dette er angitt av bruker:
# POLICY vert auto-detektert frå build.yaml — overstyr ved behov med POLICY=<bronze|silver|gold>
make mcp-linkml-valider-modell SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml
```

## Policy-hierarki

Bronze/silver/gold validerer **skjemakvalitet** (modellens metadata og struktur),
ikkje instansdata. Instansdata vert validert med `make validate-instance`.

`felles-datakatalog` og `felles-begrepskatalog` er separate policyer for
skjema som publiserer til eksterne katalogar (`publish_external: true`).

Policy-hierarkiet realiserer både Digdir sine
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(regel 1-15) og [FAIR-prinsippa](https://www.go-fair.org/fair-principles/)
(Findable, Accessible, Interoperable, Reusable).

Sjå `src/mcp-linkml-validator/policies/README.md` for fullstendig sjekkliste,
Digdir-regel-mapping og FAIR-prinsipp per nivå.

## Kjente feil

Alle kjente feil med aktive workarounds er dokumenterte i `bugs/`.
Sjå `BUGS.md` for full oversikt.

**Konvensjon:** kvar skip-betingelse i `tests/test_make.sh` skal referere til
ei tilhøyrande fil i `bugs/` med BUG-ID i kommentaren og meldinga, t.d.:

```bash
# BUG-1: rdflib_loader rekonstruerer ikkje LangString-verdiar frå TTL
# Sjå bugs/langstring-rdflib-roundtrip.md
if [[ "$name" == "skjema-med-langstring" ]]; then
    echo "Hoppar over for $name (BUG-1: ...)"
    return 0
fi
```

Når ein ny bug vert oppdaga og workaround lagt inn, opprett ei ny fil i
`bugs/` og oppdater `BUGS.md`.

## Dokumentasjonsportal (mkdocs)

`mkdocs/mkdocs.yml` vert **automatisk regenerert** av `mkdocs/publish.sh` kvar gong `make docs-publish` køyrer — endringar gjort direkte i `mkdocs.yml` vert overskrivne ved neste publisering. **Sannkjelda for nav-menyen er `mkdocs/publish.sh`**, ikkje `mkdocs.yml`.

Detaljert rettleiing (steg-for-steg for `publish.sh`, PlantUML-diagramgenerering, Jinja2-template whitespace-reglar, heading-slug-fella for æ/ø/å, relative/absolutte lenkjereglar) lastar automatisk ved arbeid med `mkdocs/`- eller `src/assets/templates/docgen/`-filer, sjå `.claude/rules/mkdocs-portal.md`.

## Modelleringsprinsipper

### Skriftspråk

Repoet nyttar to skriftspråk med klart skilde domene:

| Domene | Språk | Gjeld |
|---|---|---|
| Modellering | **Norsk bokmål** | Klassenavn, slotnavn, skildringar og kommentarar i `.yaml`-skjema |
| Dokumentasjon | **Nynorsk** | README-filer, mkdocs-sider, spesifikasjonar i `specs/` |

Bokmål i modellering følgjer terminologien i norske offentlege standardar (DCAT-AP-NO, SKOS-AP-NO m.fl.) som er skrivne på bokmål. Unntaket er tekniske omgrep fastsette i ein spesifikasjon (t.d. `dcat:Dataset` → `Datasett`).

**Unntak for Modellmetadata-tabellen:** Modellmetadata-tabellen i genererte `index.md`-sider (name, title, description, versjon, lisens, utgiver, status, endringsdato, utgivelsesdato) skal vise verdiane **ordrette slik dei er skrivne i skjemaet** (som følgjer bokmål-konvensjonen) — ikkje omsetjast til nynorsk, sjølv om resten av dokumentasjonssida elles følgjer nynorsk. Skjemaet er sannkjelde for alle metadataverdiar; redigering eller omsetjing av desse verdiane i dokumentasjonen ville bryte sannkjelde-prinsippet.

**Unntak — enkeltord i bokmålsform:** Desse orda skal alltid skrivast i bokmålsforma, sjølv i elles nynorsk dokumentasjonstekst (README, mkdocs, `COMMANDS.md`, spec-filer i `specs/backlog/`):

| Nynorsk (unngå) | Bruk i staden |
|---|---|
| namn | navn |
| artefaktar | artefakter |
| hamnar | havner |

Desse er historiske, brukarstadfesta unntak — ikkje eit generelt skifte til bokmål. `specs/done/` er urørt (arkivert, jf. DRY-unntaket i innleiinga). Sjå `specs/done/erstatt-artefaktar-med-artefakter.md`, `specs/done/namn-navn-konsistens-make-help.md` og `specs/done/erstatt-hamnar-med-havner.md` for grunngjeving.

### Endringer i koderepoet
Forsøk alltid å utføre minimale endringer som kun løser den spesifikke oppgava.

LinkML-spesifikke modelleringsprinsipp (slots vs attributes, lenking fremfor inlining, klassenavn, containerklasse-reglar, Los-tema, ny profil) lastar automatisk ved arbeid med filer under `src/linkml/`, sjå `.claude/rules/linkml-schema.md`.

## Navngjeving

### Teiknsett

- **ASCII hyphen (U+002d, "-")** skal brukast i all kjeldekode, YAML-filer,
  shell-scripts og Markdown-dokumentasjon.
- **Unicode en-dash (U+2013, "–")** skal **ikkje** brukast — det kan
  forvekslast med ASCII hyphen og skape parsing-problem i YAML og andre format.
- **Em-dash (U+2014, "—")** kan brukast i løpande prosa der typografisk
  distinksjon er ønskt, men bør unngåast i teknisk dokumentasjon.

Katalogstruktur, manifestformat (`build.yaml`), fil-/mappenavn, schema-metadata, translitterering av norske bokstavar, slotnavnkonvensjonar, standardprefiks og silver-annotasjonar for LinkML-skjema lastar automatisk ved arbeid med filer under `src/linkml/`, sjå `.claude/rules/linkml-schema.md`.
