# Opprydding av "Attverande gap"-tabellen i standardetterleving.md

## Bakgrunn

`mkdocs/docs/arkitektur/standardetterleving.md` sin "Attverande gap"-tabell
inneheld fleire rader som alt er merkte med gjennomstreking og status
**"Lukka"** (gap 3, 7, 9, 10) — desse er attverande i tabellen berre som
historisk spor, sjølv om dei ikkje lenger representerer opent arbeid. Brukaren
har bede om å fjerne alle lukka gap frå tabellen, og deretter reevaluere dei
attverande gapa (1, 2, 4, 5, 6, 8, 11) mot faktisk repo-tilstand for å sjå om
status har endra seg sidan tabellen sist vart oppdatert.

## Steg

1. Undersøk kvart attverande gap (1, 2, 4, 5, 6, 8, 11) mot faktisk kode-/spec-tilstand:
   - Gap 1 (URI-peikarar) — status på `specs/backlog/avvik-peikarar-til-offentlege-ressursar.md`
   - Gap 2 (TBX-eksport) — finst det TBX-eksport i dag?
   - Gap 4 (Person/Enhet kryssreferanse i description.md) — finst dokumentasjon alt?
   - Gap 5 (begrepsidentifikator-annotasjon) — noverande talet skjema med/utan, jf. `specs/backlog/begrepsidentifikator-gap-liste-fase2.md` og `plan-konsekvent-begrepsidentifikator.md`
   - Gap 6 (owl:sameAs-kryssreferanse) — finst dokumentasjon alt?
   - Gap 8 (ModellkatalogContainer DRY) — er dette gjort?
   - Gap 11 (6 oreg-skjema manglar manifest) — finst manifest-filene no?
2. Fjern gap 3, 7, 9, 10 (alle "Lukka") frå tabellen.
3. Renummerer attverande gap fortløpande (1-7).
4. Oppdater status/prioritet/vurdering for kvart attverande gap dersom
   undersøkinga i steg 1 viser endring.
5. Oppdater forklaringsavsnittet under tabellen (linje ~86-101) slik at det
   berre viser til attverande gap, ikkje dei fjerna.
6. Verifiser at alle lenkjer i tabellen framleis er gyldige (relative vs.
   absolutte iht. `.claude/rules/mkdocs-portal.md`).

## Handlingsliste

- [x] Undersøk gap 1, 2, 4, 5, 6, 8, 11
- [x] Fjern lukka gap (3, 7, 9, 10) frå tabellen
- [x] Renummerer attverande gap
- [x] Oppdater status der endra
- [x] Oppdater forklaringsavsnitt under tabellen
- [x] Verifiser lenkjer

## Utført

Undersøkte alle 7 attverande gap mot faktisk repo-tilstand:

- **Gap 1, 2, 3 (Person/Enhet), 5 (owl:sameAs), 6 (DRY):** uendra — ingen ny
  aktivitet funnen.
- **Gap 4 (begrepsidentifikator, tidlegare #5):** status endra — nytt
  MCP-søkjeverktøy `sok_begrepskatalog` bygd, Fase 2-batchsøk køyrt (121
  kandidattreff av 326 søkbare klassar), dokumentert i
  `specs/backlog/plan-konsekvent-begrepsidentifikator.md` og
  `specs/backlog/begrepsidentifikator-gap-liste-fase2.md`. Går frå
  "13/43 skjema" til fasebeskriving med presis klassetal.
- **Gap 7 (oreg-manifest, tidlegare #11):** status endra — alle 6
  manifestfilene som manglar er no CI-generert, men `brreg-modellkatalog.yaml`
  er ikkje regenerert, så dei manglar enno i `informasjonsmodeller`-lista.
  Prioritet senka frå Middels til Låg (berre regenerering står att, ikkje
  kodeendring).

Fjerna gap 3, 7, 9, 10 (alle merkte "Lukka") frå tabellen, renummererte
attverande gap 1-7, oppdaterte kryssreferansar til gap-nummer i
Pilar 3-tabellen (linje 54-55), og skreiv om forklaringsavsnittet under
tabellen til å reflektere ny tilstand.
