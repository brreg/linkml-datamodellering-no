# Per-host throttling for purl.org i lenkjesjekk (lychee)

## Bakgrunn

Jobben `lenkjesjekk` i `.github/workflows/lenkje-og-mermaid-sjekk.yml`
(køyring [31931289364](https://github.com/brreg/linkml-datamodellering-no/actions/runs/31931289364/job/95126557164),
2026-08-16) fekk `conclusion: success` (steget `Sjekk lenkjer i dokumentasjon`
avsluttar sjølve `podman run ... lychee ...`-kallet med `|| true`, sjå
line 303 i workflow-fila), men lychee logga to hint i steget:

> Hint: Encountered rate limit responses. You might be able to work around
> this by adding `[hosts."purl.org"]` to the TOML config to adjust the
> `concurrency` and `request_interval` values.
>
> Hint: Followed 483 redirects. You might want to consider replacing
> redirecting URLs with the resolved URLs. Use verbose mode (`-v`/`-vv`) to
> see redirection details.

Den opplasta rapport-artefakten (`lenkjesjekk-report.md`, 8811 linjer,
3836 rapporterte broten lenkjer totalt) stadfestar begge hint:

- **20 av 20** `[429]`-funn i rapporten er mot `purl.org` (t.d.
  `http://purl.org/adms/publishertype/Company`,
  `http://purl.org/dc/terms/requires`) — ingen andre vertar har 429-funn.
  Dette samsvarar heilt med lychee sitt eige forslag om å leggje til ei
  `[hosts."purl.org"]`-innskrenking.
- Rapporten skil ikkje ut kva for redirects som gjeld `purl.org` (lychee sin
  markdown-rapport viser berre feil, ikkje vellykka redirects — `-v`/`-vv`
  trengst for detaljar, sjå Steg 3), men alle `purl.org`-referansar i
  LinkML-skjema (`grep -rn "purl\.org" src/linkml/*/*/*.yaml`) brukar
  konsekvent `http://` — dette er dei kanoniske RDF/DCT/ADMS-vokabular-URI-ane
  (t.d. `dct: http://purl.org/dc/terms/`, jf. CLAUDE.md §
  Standardprefix). `http://purl.org/...` gjev normalt eit HTTP→HTTPS-
  redirect ved oppslag, noko som mest sannsynleg forklarer ein stor del av
  dei 483 redirectane.

**Merk (utanfor omfanget til denne spec-en):** Rapporten inneheld òg ~40
`purl.org`-funn med status `404` som kjem av **malforma lenkjer** i genererte
sider — t.d. `http://purl.org/adms/publishertype/PrivateIndividual(s)>` (ein
stray `(s)`-suffiks) og `http://purl.org/adms/status/(Completed>` (ein stray
opningsparentes). Dette er ein separat feil i lenkjegenereringa (truleg i
gen-doc-malen eller kjeldeskildringane som inneheld parentesar som vert tolka
som del av URI-en), ikkje eit rate limiting- eller redirect-problem. Bør
handterast som ein eigen spec/bug dersom det skal rettast.

## Evaluering av hinta

1. **`[hosts."purl.org"]` (rate limit) — tilrå å implementere.** Lychee
   støttar per-host-innskrenking av `concurrency` og `request_interval` via
   TOML (stadfesta mot `lychee.example.toml` i
   github.com/lycheeverse/lychee), t.d.:
   ```toml
   [hosts."purl.org"]
   concurrency = 2
   request_interval = "1s"
   ```
   Dette er presis den mekanismen lychee sjølv peikar til, og er meir
   presist enn å redusere global `--concurrency`/`max_concurrency` (som ville
   seinka heile jobben for vertar som ikkje har noko rate limiting-problem).
   Same rotårsak-mønster som `mermaid-click-href-sjekk`
   (`specs/done/mermaid-click-href-429-retry.md`), men ulik løysingsmekanisme
   sidan lychee er eit ferdig CLI-verktøy styrt av config — ikkje eigen
   Python-kode med retry-logikk.
2. **"483 redirects" — ikkje aktuelt å handtere ved å byte ut URL-ane.**
   `purl.org`-URI-ane som opptrer i skjemaa er kanoniske RDF-vokabular-
   namnerom (`dct:`, `adms:` osv.) som **skal** vere `http://` per
   CLAUDE.md § Standardprefix og W3C/DCAT-AP-NO-konvensjon — å byte dei til
   den redirect-oppløyste `https://`-forma ville endre namnerom-identiteten
   til RDF-data (eit brot på Linked Data-prinsippet om stabile URI-ar), ikkje
   berre ei kosmetisk lenkjeretting. Redirects er alt godkjende av
   `accept = ["300..=399"]` i eksisterande config, så dei tel ikkje som
   broten lenkjer — hintet er reint informativt/ytelsesretta. Den auka
   førespurnadsvolumet redirectane gjev mot `purl.org`, vert i staden
   absorbert av same per-host-innskrenking som i punkt 1.

## Steg

1. Legg til ein `[hosts."purl.org"]`-seksjon nedst i `.github/lychee.toml`
   med `concurrency = 2` og `request_interval = "1s"` (juster verdiane
   dersom 429-funn framleis dukkar opp ved neste køyring — sjå Steg 3).
2. Legg til ein kort kommentar over seksjonen som viser til denne spec-en og
   forklarer kvifor `purl.org` treng eiga innskrenking (jf. hint frå
   køyring 31931289364).
3. Verifiser lokalt: køyr same `podman run ... lychee ... --config
   .github/lychee.toml ...`-kommando som i workflow-steget «Sjekk lenkjer i
   dokumentasjon» (line 298–303) mot ein bygd `mkdocs/site`/repo-tre, og
   stadfest at `[429]`-funn mot `purl.org` ikkje lenger dukkar opp i
   `lenkjesjekk-report.md`. Merk: full `make docs-publish && make docs-build`
   må køyrast først for at alle genererte `.md`-filer skal finnast, jf.
   workflow-steget «Publiser og bygg dokumentasjonsportal».
4. Stadfest at talet på broten lenkjer i rapporten går ned tilsvarande dei
   20 tidlegare 429-funna (dei resterande ~40 malforma `purl.org`-404-funna
   og andre ekte 404/401/400/403-funn er utanfor omfanget til denne
   spec-en, sjå "Merk" i Bakgrunn).

## Handlingsliste

- [x] Legg til `[hosts."purl.org"]` med `concurrency`/`request_interval` i
      `.github/lychee.toml`
- [x] Kommenter kvifor (vis til denne spec-en)
- [x] Lokal verifisering: 429-funn mot `purl.org` borte frå
      `lenkjesjekk-report.md`
- [x] Stadfest at broten-tal i rapporten går ned med talet på tidlegare
      429-funn (20)

## Utført

La til `[hosts."purl.org"]` (`concurrency = 2`, `request_interval = "1s"`)
nedst i `.github/lychee.toml`, med kommentar som viser til denne spec-en.
TOML-syntaksen stadfesta gyldig med `lychee --dump`.

Lokal verifisering: `make docs-publish` (frå eksisterande `generated/`) +
same `podman run ... lychee --config .github/lychee.toml ...`-kommando som
i CI-steget, køyrt mot heile repoet:

- Hint om rate limit er borte frå lychee sin output (berre redirect-hintet
  står att, som venta — sjå evaluering over).
- **0 av 3812** rapporterte funn er `[429]`, mot 20/3836 i CI-køyringa
  (2026-08-16, run 31931289364) — alle mot `purl.org`.
- `purl.org` har framleis 44 `[404]`-funn frå den kjende, urelaterte
  malforma-lenkje-feilen (parentesar i genererte URI-ar) — uendra og
  stadfesta utanfor omfanget til denne spec-en.
- Total broten-tal gjekk frå 3836 → 3812 (differansen samsvarar med dei
  fjerna 429-funna; mindre avvik i andre statuskodar mellom køyringane
  (t.d. eit par nye `503`) skuldast normal nettverksvariasjon mellom
  separate køyringar, ikkje denne endringa).
