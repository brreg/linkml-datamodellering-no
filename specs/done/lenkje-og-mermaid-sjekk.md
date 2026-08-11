# CI-workflow: mermaid-rendering og lenkjesjekk

## Bakgrunn

Repoet har 15 mermaid-diagram spreidd over `mkdocs/docs/`, `specs/` og
`src/linkml/fair/fair-metadata/fair-metadata.md`. Mermaid-blokker kan feile
å rendre sjølv om syntaksen ser gyldig ut (jf. minnenotat
`feedback_mermaid_classdef_quirk` — ein ny `classDef` broke rendering
stille i `arkitektur-oversikt.md`). Det finst ingen automatisk sjekk som
fangar dette i dag.

Repoet inneheld òg mange hundre eksterne lenkjer i `.md`-dokumentasjon
(README, `mkdocs/docs/`, `specs/`). Desse vert aldri verifiserte —
lenkjer kan rotne (404, DNS-feil, flytta ressursar) utan at nokon merkar det.

Eit rått søk fann ~12 000 URL-tilfelle i `.md`/`.yaml`/`.yml` samla, men
dei fleste er plasshaldarar (`example.org`, `eksempel.no`, `<org-domene>`,
`{domene}`) eller RDF-namespace-URI-ar (`dct:`, `dcat:` osv.) som ikkje er
meint å dereferast. Denne workflowen avgrensar seg difor til reelle
dokumentasjonslenkjer i `.md`-filer.

## Avklarte val (frå brukar)

1. **Omfang:** Berre lenkjer i `.md`-filer (dokumentasjon), ikkje URI-ar i
   LinkML-skjema (`class_uri`/`slot_uri`) eller W3C/EU-namespace-URI-ar.
2. **Trigger:** `workflow_dispatch` (manuell) + `schedule` (vekentleg).
3. **Feiloppførsel:** Workflowen skal **aldri feile CI** — han skal logge
   funn til jobb-summary og last opp som artefakt, med HTTP-returkode for
   kvar lenkje som ikkje svarar 2xx/3xx.

## Steg

1. Opprett `.github/workflows/lenkje-og-mermaid-sjekk.yml` med to
   parallelle jobbar: `mermaid-render` og `lenkjesjekk`.
2. **`mermaid-render`-jobb:**
   - Finn alle ```` ```mermaid ```` … ```` ``` ```` -blokker i `*.md`-filer
     repo-vidt (ekskl. `.git/`), med kjeldefil og blokk-indeks bevart.
   - Trekk inn `docker.io/minlag/mermaid-cli:latest` via `podman pull` og
     rendra kvar blokk til SVG via `podman run … mmdc -i … -o …`.
   - Logg feil med `::warning file=<fil>::` + siste linjer av mmdc-stderr.
   - Skriv ein Markdown-tabell (fil, blokk-nr, status) til
     `$GITHUB_STEP_SUMMARY` og last opp som artefakt
     `mermaid-render-report`.
3. **`lenkjesjekk`-jobb:**
   - Legg til `.github/lychee.toml` med `exclude`-mønster for kjende
     plasshaldar-domene (`example.*`, `eksempel.no`/`eksempelorg.no`,
     `*.example.org`, `<...>`-mønster, `localhost`,
     `host.containers.internal`) og `timeout`/`max_retries`-innstillingar.
   - Trekk inn `docker.io/lycheeverse/lychee:latest` via `podman pull` og
     køyr han mot alle `**/*.md` med `--format markdown`.
   - Skriv rapporten (kjelde, lenkje, HTTP-status) til
     `$GITHUB_STEP_SUMMARY` og last opp som artefakt
     `lenkjesjekk-report`. Undertrykk ikkje-null exit-kode frå lychee slik
     at jobben aldri feilar CI.
4. Køyr `actionlint` mot den nye workflow-fila (påkravd av CLAUDE.md etter
   kvar CI-endring):
   `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/lenkje-og-mermaid-sjekk.yml`
5. Oppdater `mkdocs/docs/automasjon/monitorering.md` (eller tilsvarande
   automasjons-oversiktsside) med ein kort omtale av den nye workflowen,
   dersom den sida dokumenterer eksisterande scheduled/CI-sjekker.

## Handlingsliste

- [x] `.github/workflows/lenkje-og-mermaid-sjekk.yml` oppretta med
      `mermaid-render`- og `lenkjesjekk`-jobbar, `workflow_dispatch` +
      vekentleg `schedule`
- [x] `.github/lychee.toml` oppretta med ekskluderingsmønster for
      plasshaldar-domene
- [x] `actionlint` køyrt mot ny workflow-fil, ingen `[expression]`-feil
- [ ] Dokumentasjon oppdatert dersom relevant — **ikkje utført**, sjå
      "Utført"-seksjonen under for grunngjeving

## Utført

- `mermaid-render`-jobben trekkjer ut ```` ```mermaid ```` -blokker frå
  alle `git ls-files -- '*.md'`-sporte filer (bash-regex, ikkje
  per-linje `grep`-fork — testa lokalt: 48 diagram funne på 680 sporte
  `.md`-filer). `git ls-files` valt framfor `find` fordi han automatisk
  avgrensar til versjonskontrollerte filer og hoppar over
  `.gitignore`-a byggoutput (`generated/`, `mkdocs/docs/<domene>/…`)
  utan eksplisitt filtrering.
- Kvar blokk vert rendra med `docker.io/minlag/mermaid-cli:latest` via
  podman. **Funn under implementering:** biletet køyrer som uid 1001,
  men i podman rootless vert monterte filer eigd av "root" i
  containerens brukarnamnerom — treng `--user 0:0` for skrivetilgang
  til output-SVG. Verifisert både for vellukka rendering og for eit
  bevisst broten diagram (feilmelding fanga korrekt i logg).
- `lenkjesjekk`-jobben køyrer `docker.io/lycheeverse/lychee:latest` mot
  `**/*.md` med `.github/lychee.toml`. **Funn under implementering:**
  `exclude_mail` er ikkje eit gyldig felt i lychee sin config-schema
  (lychee ekskluderer `mailto:` som standard) — fjerna frå config.
  Ekskluderingsmønstra for plasshaldar-domene (`example.org`,
  `eksempel.no`, `<org-domene>` osv.) er verifiserte mot ein
  syntetisk testfil.
- Testkøyring av `lenkjesjekk` mot `README.md` avdekte at fleire
  relative lenkjer (`[REFERANSE](referanse/)` m.fl.) peikar til
  katalogar som ikkje finst på repo-rot (dei reelle katalogane ligg
  under `src/linkml/<domene>/`). Dette er truleg reelt etterslep frå
  ein tidlegare katalogstruktur, men er **ikkje retta** her — omfanget
  var å byggje sjekkeverktøyet, ikkje å rette opp alle funna. Neste
  planlagde/manuelle køyring av workflowen vil rapportere dette i
  jobb-summary; brukaren kan opprette eiga sak/spec for oppretting.
- Ingen endring gjort i `mkdocs/docs/automasjon/monitorering.md` —
  sida dokumenterer eksisterande overvaking av *publiserte* artefakt
  (lenkje-helse på GitHub Pages-portalen), ikkje kjeldekontroll-CI.
  Vurdert som utanfor omfanget av denne spesifikke spec-en; kan
  leggjast til i eiga endring om ønska.
