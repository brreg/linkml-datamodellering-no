# Domene-index.md — meir relevant innhald per domene

## Bakgrunn

`index.md` for kvart domene i NAV-menyen (t.d. [FINT - Fylkeskommunale integrasjonar](../../mkdocs/docs/fint/index.md)) vert i dag generert av `mkdocs/publish.sh` (linje 388-421) som berre ei tittellinje (`domain_label()`) etterfølgt av ein tabell med skjema og tilgjengelege artefaktar. Domenet sjølv — kva det dekkjer, kven det er meint for, kva standardar det byggjer på — vert aldri skildra. Brukaren av portalen må klikke seg inn i kvart einskild skjema for å forstå kva domenet inneheld.

Repoet har allereie eit etablert mønster for akkurat dette problemet på **skjema-nivå**: eit valfritt `src/linkml/<domain>/<schema>/description.md` vert rendra inn i "Om denne modellen"-seksjonen av skjemaet sin `index.md` (`mkdocs/lib/sections/om_denne_modellen.sh`, dokumentert i `mkdocs/docs/index-md-struktur.md`). Denne specen innfører same mønster ein katalognivå opp: eit valfritt `src/linkml/<domain>/description.md` som vert rendra inn i domenet sin `index.md`, før tabellen.

**Avklart med brukar (2026-08-05):**
- Kjelde: ny fil `src/linkml/<domain>/description.md` per domene (same mønster som skjema-nivå), ikkje hardkoda tekst i `publish.sh`.
- Omfang: skriv innhald for alle 9 domene no (`ap-no`, `begrepskatalog`, `fair`, `fint`, `modellkatalog`, `ngr`, `oreg`, `referanse`, `samt`), ikkje berre mekanismen.
- Innhaldselement: typisk brukar/bruksområde, relaterte standardar/spesifikasjonar, kort oversikt over modellane i domenet (supplerer tabellen, som berre listar artefakt-typar).
- Språk: nynorsk (dokumentasjonsdomenet, jf. CLAUDE.md § Skriftspråk) — same som eksisterande skjema-nivå `description.md`-filer.

## Steg

1. **Ny funksjon `generate_domain_description()`** i ny fil `mkdocs/lib/sections/domain_description.sh`, etter mønster frå `om_denne_modellen.sh`: les `src/linkml/<domain>/description.md` dersom fila finst, `cat` innhaldet, returner tomt (ingen seksjon) dersom fila manglar. Ingen ingress-boilerplate (domene-sida treng ikkje "denne sida dokumenterer..."-teksten som skjema-nivå har, sidan tittelen + tabell alt gjer det tydeleg).

2. **Kople inn i `publish.sh`**: `source` den nye fila saman med dei andre `lib/sections/*.sh`-filene, og kall `generate_domain_description "$domain"` rett etter tittellinja (`echo "# $(domain_label "$domain")"` + tom linje) og før tabelloverskrifta, i løkka på linje 388-421.

3. **Opprett 9 `description.md`-filer** (éin per domenekatalog i `src/linkml/`), nynorsk, 2-4 avsnitt kvar: kva domenet dekkjer, kva modellar det inneheld (kort, supplerer tabellen), relaterte standardar, "Typisk brukar". Utkast (basert på eksisterande skjema-nivå `description.md`-filer og `SCOPE.md`):

   - **`ap-no/description.md`** — dei 7 AP-NO-profilane (common, dcat, dqv, skos, xkos, cpsv, modelldcat), berre for import, ingen `tree_root`, lenkje til Digdir sine spesifikasjonar.
   - **`begrepskatalog/description.md`** — SKOS-AP-NO-baserte omgrepskatalogar med produksjonsdata under `data/`, publisert til Felles begrepskatalog.
   - **`fair/description.md`** — `fair-metadata`, FAIR-tilleggseigenskapar for AP-NO-profilane, berre for import.
   - **`fint/description.md`** — `fint-common` + 6 fagmodellar (administrasjon, arkiv, økonomi, personvern, ressurs, utdanning), `camelCase`-namngjeving arva frå FINT API-spec.
   - **`modellkatalog/description.md`** — ModelDCAT-AP-NO-baserte modellkatalogar per verksemd (BRREG, Digdir, Kartverket, KS Digital, Novari, Skatteetaten), publisert til Felles modellkatalog.
   - **`ngr/description.md`** — 4 domenemodellar for Nasjonale grunndata (adresse, eiendom, person, virksomhet), `_ref`-suffiks-konvensjon.
   - **`oreg/description.md`** — 2 proof-of-concept-registermodellar (Enhetsregisteret BVRINN, Aksjeeigarregisteret).
   - **`referanse/description.md`** — undervisningsskjema (`referansemodell` + medaljong-variantar bronze/silver/gold), ikkje for produksjon.
   - **`samt/description.md`** — `samt-bu`, tverrgåande kommunal samhandling (barn og unge).

4. **Oppdater `mkdocs/docs/index-md-struktur.md`** med ei kort ny seksjon om domene-nivå `index.md` (skil frå skjema-nivå-seksjonen som allereie finst der), inkl. kjeldehierarki-linje for `src/linkml/<domain>/description.md`.

5. **Regenerer og verifiser**: køyr `make docs-publish` (eller tilsvarande dokumentert i `COMMANDS.md`), sjekk at alle 9 domene-`index.md` no har skildringstekst før tabellen, og at domene utan feil i description.md-filene framleis byggjer reint (`actionlint` er ikkje relevant her sidan ingen `.github/workflows/*.yml` vert endra).

## Handlingsliste

- [x] Opprett `mkdocs/lib/sections/domain_description.sh` med `generate_domain_description()`
- [x] Kople inn ny seksjon i `publish.sh` sin domene-`index.md`-løkke (linje ~388-421)
- [x] Skriv `src/linkml/ap-no/description.md`
- [x] Skriv `src/linkml/begrepskatalog/description.md`
- [x] Skriv `src/linkml/fair/description.md`
- [x] Skriv `src/linkml/fint/description.md`
- [x] Skriv `src/linkml/modellkatalog/description.md`
- [x] Skriv `src/linkml/ngr/description.md`
- [x] Skriv `src/linkml/oreg/description.md`
- [x] Skriv `src/linkml/referanse/description.md`
- [x] Skriv `src/linkml/samt/description.md`
- [x] Oppdater `mkdocs/docs/index-md-struktur.md` med domene-nivå-seksjon
- [x] Køyr `make docs-publish` og verifiser alle 9 domene-`index.md`

## Utført

Alle steg gjennomførte som planlagt, med to små justeringar frå det opphavlege utkastet:

- Seksjonsfila fekk namnet `domene_beskrivelse.sh` (nynorsk, i tråd med den faktiske namnekonvensjonen i `lib/sections/` — dei andre filene der heiter t.d. `avhengigheiter.sh`, `kontakt.sh`, ikkje dei engelske namna referert i den eldre delen av `index-md-struktur.md`).
- `generate_domain_description()` treng ikkje eige `source`-kall i `publish.sh`: `generate_index.sh` sourcar alt i `lib/sections/*.sh` via glob-løkke, så funksjonen vart tilgjengeleg automatisk.

`make docs-publish` køyrde reint (171s, 9 domene, 0 feil). Verifisert manuelt at alle 9 domene-`index.md` no har skildringsteksten rett under tittelen og før modell-tabellen (t.d. `mkdocs/docs/samt/index.md`).
