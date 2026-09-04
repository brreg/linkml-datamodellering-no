# Logg ikkje-trivielle avgjerder i spec

## Bakgrunn

Brukaren ønskjer at alle ikkje-trivielle avgjerder (reasoning) LLM-en tek
undervegs i arbeidet skal loggast. Vurdert som eiga Claude Code-rule eller
-skill, men begge mekanismane er *betinga* utløyst (rule: filsti, skill:
eksplisitt kall/oppgåve-treff) — logging av avgjerder skal derimot gjelde
**ubetinga**, uavhengig av kva filer som vert rørt. Høyrer difor heime som
ein standing-instruks i CLAUDE.md sin eksisterande arbeidsflyt, ikkje som
noko som må "trigge".

Presisert av brukar: berre **ikkje-trivielle** val (ikkje kvar mikro-steg),
logga **per spec** — altså i den same `specs/backlog/<kortnavn>.md`-fila
arbeidsflyten alt krev, ikkje ein separat sentral logg.

## Steg

1. Utvid CLAUDE.md § "Arbeidsflyt", steg 3 ("Skriv spesifikasjon"): ei ny
   spec skal òg innehalde ei tom `## Avgjerder`-seksjon frå starten av.
2. Utvid CLAUDE.md § "Arbeidsflyt", steg 4 ("Utfør arbeidet"): ikkje-trivielle
   val skal loggast i `## Avgjerder`-seksjonen etter kvart som dei vert
   tekne — kort kva som vart valt og kvifor.
3. Ikkje endre `specs/done/` retroaktivt — 539 arkiverte specs er urørte
   per DRY-unntaket i CLAUDE.md sin innleiing (arkiverte specs skal ikkje
   konsoliderast/omskrivast).

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | Legg til `## Avgjerder`-krav i spec-skriving | `CLAUDE.md` (Arbeidsflyt, steg 3) | |
| 2 | Legg til logg-plikt under utføring | `CLAUDE.md` (Arbeidsflyt, steg 4) | |

## Avgjerder

- **Rule/skill vurdert og forkasta til fordel for CLAUDE.md-tillegg.**
  Grunngjeving: logging skal gjelde ubetinga (kvar spec, uavhengig av
  filsti), medan rules (filsti-scopa) og skills (eksplisitt kall) begge er
  betinga mekanismar — ingen av dei passar for eit krav som skal gjelde
  heile tida.
- **Loggen ligg i sjølve spec-fila (`## Avgjerder`), ikkje ein separat
  sentral fil.** Grunngjeving: brukar presiserte eksplisitt "logg per
  spec" — held avgjerda kontekstnær der ho vart teken, og følgjer same
  livssyklus som resten av specen (backlog → done).
- **Berre ikkje-trivielle val loggast, ikkje kvar mikro-steg.**
  Grunngjeving: brukar presiserte eksplisitt "berre ikkje-trivielle val" —
  unngår støy frå trivielle, sjølvforklarande handlingar.
- **`specs/done/` vert ikkje retroaktivt oppdatert med Avgjerder-seksjonar.**
  Grunngjeving: DRY-unntaket i CLAUDE.md sin innleiing fastset at arkiverte
  specs skal stå urørte; å leggje til seksjonar i 539 filer i etterkant
  ville òg vore eit uforholdsmessig stort, ikkje-etterspurt tiltak.

## Utført

- `CLAUDE.md` § "Arbeidsflyt": steg 3 utvida med krav om tom
  `## Avgjerder`-seksjon i nye specs; steg 4 utvida med logg-plikt for
  ikkje-trivielle val.
