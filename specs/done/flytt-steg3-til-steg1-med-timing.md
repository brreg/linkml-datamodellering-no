# Flytt Steg 3 til slutten av Steg 1 i docs-publish, med per-kall timing

## Bakgrunn

Brukaren bad om å (1) flytte dei to operasjonane i "Steg 3" i
`mkdocs/publish.sh` — kopier `README.md` → `docs/index.md` (+ footer med
byggetidspunkt), og generer `arkitektur/valideringsregler.md` — til
slutten av Steg 1, og (2) innføre timing og logging av timing for kvar av
desse kalla individuelt (ikkje berre eit samla steg-nivå-tal, som i dag).

**Kontekst:** `publish.sh` har i dag **to** steg begge kalla "Steg 3"
(linje ~431 og ~449 — éin for readme-kopieringa, éin for
valideringsregel-genereringa), målt saman som éin kombinert
`elapsed3_ms`. Ingen av dei to operasjonane avheng av Steg 2 sitt
parallelle skjema-arbeid: dei les statiske filer (`$REPO_ROOT/README.md`,
`src/mcp-linkml-validator/policies/README.md`) og skriv til
`$DOCS/index.md`/`$DOCS/arkitektur/valideringsregler.md` — `arkitektur/`
er eksplisitt kvitelista i Steg 1 sin oppryddingsloop og vert difor aldri
sletta. `BUILD_TIMESTAMP` (nødvendig for footer-en) vert alt berekna rett
etter Steg 1 i dag, og brukast **berre** av footer-skrivinga (verifisert
med `grep -n BUILD_TIMESTAMP`). Å flytte desse to operasjonane tidlegare
fjernar unødig sekvensiell venting etter det tunge Steg 2-arbeidet — sjølv
om begge operasjonane i dag er svært raske (<50ms samla per eksisterande
`elapsed3_ms`-logg), er gevinsten her primært ryddigare rekkjefølgje og
betre profileringsgrunnlag for framtidige ytelsesrundar (jf.
`specs/done/reduser-podman-kall-docs-publish.md`), ikkje eit stort
tidsspark.

Repoet har alt ein etablert, delt tidtakings-/loggingsfunksjon for nett
dette føremålet: **`timed_run "<label>" <kommando...>`**, definert i
`make/00-settings.mk` sin `LOG_FUNCTIONS` (linje 73-86) og alt tilgjengeleg
inne i `publish.sh` via det eksisterande `eval "$LOG_FUNCTIONS"`-kallet
(linje 8). `timed_run` målar elapsed med `fmt_elapsed_ms`, loggar
kommandonamn+tid ved suksess (`log_info`) og feil+kommandolinje+tid ved
feil (`log_error`) — nøyaktig det "timing og logging av timing"-ønsket
ber om, utan å måtte finne opp noko nytt. `publish.sh` sine eksisterande
steg-tidtakingar (`t1`/`elapsed1_ms` osv.) er derimot handrulla (ikkje via
`timed_run`), så dei følgjer **ikkje** same konvensjon som resten av
make-laget alt brukar for tidtaking/logging (jf. `COMMANDS.md` §
«Ingen stille feil»).

## Mål

- Dei to operasjonane som i dag utgjer "Steg 3" flyttar til slutten av
  Steg 1 (rett etter opprydding, før Steg 1.4).
- Kvar operasjon vert individuelt tidtatt og logga via det eksisterande
  `timed_run`-hjelpemiddelet, ikkje berre eit samla steg-tal.
- Steg-nummereringa vert rydda opp som eit biprodukt: dei to stega som i
  dag begge heiter "Steg 3" forsvinn; attverande rekkjefølgje vert
  Steg 1 (utvida), Steg 1.4, Steg 1.5, Steg 2, Steg 3 (var Steg 4 —
  mkdocs.yml-generering).
- Ingen endring i generert `mkdocs/docs/`-innhald (identisk output, berre
  annan rekkjefølgje/logging internt i scriptet).

## Antakelser (spør brukar dersom desse er feil før implementering)

1. **"Slutten av steg 1"** tyder rett etter oppryddingsloopen (dagens
   `elapsed1_ms`-logglinje), **før** Steg 1.4 (domene-/skjema-
   enumerering) — ikkje etter Steg 1.4/1.5. Rekkjefølgja mellom desse tre
   blokkene (dei flytta Steg 3-kalla, Steg 1.4, Steg 1.5) har ingen
   funksjonell konsekvens sidan ingen av dei avheng av kvarandre; vald
   plassering er den mest bokstavlege lesinga av instruksjonen.
2. **"Alle kalla"** tyder dei kalla som **i dag** utgjer Steg 3
   (README-kopi+footer, valideringsregel-generering) — ikkje ei generell
   ombygging av heile `publish.sh` sine eksisterande steg-tidtakingar
   (Steg 1/2/3) til `timed_run`. Den breiare migreringa nemnast som
   mogleg oppfølging (sjå "Utanfor scope"), ikkje del av denne spec-en.
3. Dei to interne `log_info`-linjene i `generate_validation_docs()`
   ("→ Genererer valideringsregler.md..." / "✓ Genererte $output") vert
   fjerna, sidan dei ville dublisert `timed_run` sin eigen før/etter-logg
   for same kall. Output-stien kan behaldast som ein `log_debug`-linje om
   ønskt for feilsøking.

## Steg

1. I `mkdocs/publish.sh`: flytt kodeblokka for "Steg 3: Generer index.md
   frå README.md" og "Steg 3: Generer valideringsregler.md"
   (noverande linje ~430-455) til rett etter Steg 1 sin
   `elapsed1_ms`-logglinje, før `# Generer byggetidspunkt`-kommentaren/
   Steg 1.4-blokka.
2. Fjern dei to `log_step`-kalla og dei to separate `t3`/`elapsed3_ms`
   -blokkene — desse vert erstatta av `timed_run` sin eigen logging per
   operasjon (eit samla steg-banner gjev ikkje meirverdi når kvar
   operasjon uansett loggar eiga tid).
3. Erstatt README→index.md-kopieringa+footer med ein liten funksjon
   (`write_index_from_readme()`), sidan `timed_run` krev ein
   kommando/funksjon, ikkje eit vilkårleg shell-uttrykk med heredoc:
   ```bash
   write_index_from_readme() {
       cp "$REPO_ROOT/README.md" "$DOCS/index.md"
       cat >> "$DOCS/index.md" <<EOF

   ---

   _Portalen vart sist bygd: ${BUILD_TIMESTAMP}_
   EOF
   }
   ```
   Kall via `timed_run "Generer index.md frå README.md" write_index_from_readme`.
4. Kall `generate_validation_docs` via
   `timed_run "Generer valideringsregler.md" generate_validation_docs` i
   staden for eit bart funksjonskall. Fjern dei to interne
   `log_info`-linjene i funksjonen (jf. antaking 3).
5. Flytt `BUILD_TIMESTAMP`-berekninga (`# Generer byggetidspunkt
   (ISO 8601 UTC)`) til rett før `write_index_from_readme`-kallet — same
   avhengigheit som i dag (må finnast før footer-en vert skriven), berre
   flytta saman med resten av blokka.
6. Renummerer attverande steg-tekstar: "Steg 2" står som før, "Steg 4:
   Generer mkdocs.yml" vert til "Steg 3: Generer mkdocs.yml". Behald
   `t4`/`elapsed4_ms`-variabelnamna uendra (minimal diff, jf. "Utanfor
   scope" — berre `log_step`-**teksten** endrar nummer).
7. Verifiser at logg-utskrifta no viser dei to nye `timed_run`-linjene
   (med individuell tid) rett etter "✓ Steg 1 ferdig", før Steg 1.4/1.5
   sitt arbeid startar.
8. Køyr `make docs-publish` og samanlikn generert `mkdocs/docs/`-innhald
   byte-for-byte mot ein fersk baseline (same metode som
   `specs/done/reduser-podman-kall-docs-publish.md`: `git stash` for
   uendra kode → køyr → snapshot → gjenopprett endringar → køyr på nytt →
   `diff -rq`) — forventa **0 avvik** utanom det kjende
   tidsstempel-unntaket i topp-`index.md`.
9. `bash -n mkdocs/publish.sh` etter endringa.

## Utanfor scope

- Migrering av dei attverande handrulla steg-tidtakingane (Steg 1/2/3
  sine `t*`/`elapsed*_ms`-blokker) til `timed_run`/`fmt_elapsed_ms` for
  full intern konsistens — verdt å vurdere som eiga, seinare spec, men
  ikkje del av denne førespurnaden (jf. antaking 2).
- Individuell `timed_run`-tidtaking av dei to `sed`-kalla **inni**
  `generate_validation_docs()` — desse er sub-millisekund-operasjonar på
  éi lita fil; å tidtake heile funksjonen som eitt kall gjev tilstrekkeleg
  presisjon utan å fragmentere loggen unødig.

## Akseptansekriterium

- [x] Dei to Steg 3-operasjonane køyrer no rett etter Steg 1 sin
      opprydding, før Steg 1.4
- [x] Kvar operasjon er individuelt tidtatt og logga via `timed_run`
      (synleg i `make docs-publish`-output som to separate
      `→ <label> (Xs)`-linjer)
- [x] Ingen duplisert logging (dei interne `log_info`-linjene i
      `generate_validation_docs()` er fjerna, erstatta med éi
      `log_debug`-linje)
- [x] "Steg 4" er omdøypt til "Steg 3" i `log_step`-teksten **og** i den
      avsluttande "✓ Steg 3 ferdig"-linja (`t4`/`elapsed4_ms`
      -variabelnamna er uendra, som planlagt)
- [x] `bash -n mkdocs/publish.sh` utan feil
- [x] Full `make docs-publish`-køyring: identisk generert
      `mkdocs/docs/`-innhald mot fersk baseline (byte-for-byte, jf. metode
      i `specs/done/reduser-podman-kall-docs-publish.md`), einaste avvik
      det kjende tidsstempelet

## Utført

Alle 9 steg gjennomførte nøyaktig som planlagt, ingen avvik frå
antakelsane i "Antakelser".

**Verifisert korrektheit** (same metode som
`specs/done/reduser-podman-kall-docs-publish.md`):
1. `git stash` av endringa, `make docs-publish` køyrt med committa
   (uendra) kode for ein fersk "før"-basislinje, snapshot av
   `mkdocs/docs/` (6261 filer)
2. Endringa gjenoppretta, `make docs-publish` køyrt på nytt
3. `diff -rq` mellom dei to snapshotta: **0 avvik** av 6261 filer, bortsett
   frå det kjende `_Portalen vart sist bygd: ...`-tidsstempelet i topp-
   `index.md`

**Ny logg-rekkjefølgje** (stadfesta direkte i byggeloggen):
```
✓ Steg 1 ferdig (14.0s)
→ Generer index.md frå README.md (0.05s)
→ Generer valideringsregler.md (0.02s)
***
Steg 2: Generer innhald per domene og skjema (parallelt)
...
***
Steg 3: Generer mkdocs.yml
✓ Steg 3 ferdig (0.0s)
```
Dei to operasjonane er no individuelt synlege med eigne tider (0,05s og
0,02s) rett etter Steg 1, i staden for eit felles, no forsvunne
"Steg 3"-par etter Steg 2.

**Tid:** ingen merkbar endring i total køyretid (2m29,4s → 2m26,4s, godt
innanfor normal måling-til-måling-variasjon på dette systemet) — venta,
sidan dei to flytta operasjonane til saman brukar <0,1s. Gevinsten er
rekkjefølgje/synlegheit, ikkje fart, slik "Bakgrunn" alt sa.

**Ikkje gjort:** dei to punkta under "Utanfor scope" (migrering av
Steg 1/2/3 sine attverande handrulla tidtakingar til `timed_run`,
finkorna tidtaking av `sed`-kalla inni `generate_validation_docs()`) —
ikkje del av førespurnaden, ikkje vurdert naudsynt no.

## Relaterte filer

- `mkdocs/publish.sh` — flytting, `timed_run`-innpakking,
  steg-omnummerering
- `make/00-settings.mk` — `LOG_FUNCTIONS`, definerer
  `timed_run`/`fmt_elapsed_ms` (uendra, berre gjenbrukt)
- `specs/done/reduser-podman-kall-docs-publish.md` — presedens for
  verifiseringsmetode (git stash + byte-for-byte diff) og for
  `podman run`/tidtakings-relatert kontekst i same script
