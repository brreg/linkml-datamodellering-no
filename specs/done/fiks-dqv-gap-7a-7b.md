# Fiks gap 7a og 7b: DQV-kvalitetsmålingar for begrepskatalog og modellkatalog

## Bakgrunn

Frå `specs/done/fiks-dqv-measurements-data-policy-nokkel.md`:

- **7a:** `brreg-begrepskatalog.yaml` manglar `samlingar:`-container, så
  `gen-dqv-measurements` har ingen stad å ankre kvalitetsmålinga.
- **7b:** 5 av 6 modellkatalog-skjema manglar `kvalitetsmaalingar`-attributtet
  på `ModellkatalogContainer` (berre `brreg-modellkatalog-schema.yaml` har det).

## Utvida rotårsak (funne under undersøking)

Git-historikk viser at `brreg-begrepskatalog.yaml` **hadde** ein reell
`samlingar:`-blokk (id `https://begrep.brreg.no/samlingar/registerbegrep-2025`,
identisk med `examples/brreg-begrepskatalog-eksempel.yaml`) fram til commit
`9009b1e6`. Etter det starta `collect-concepts.py` (commit `e2d7d952`) å
regenerere fila med `data = {"begrep": all_begrep}` — ei **full overskriving**
som stille fjerna `samlingar:` og `kvalitetsmaalingar:`.

`generate-modellkatalog.py` har **same mønster**: `generate_modellkatalog_for_org()`
byggjer heile `modellkataloger`/`informasjonsmodeller`-strukturen på nytt kvar
gong og skriv over fila fullstendig. Dette ville ha visket ut
`brreg-modellkatalog.yaml` sine nyleg reparerte DQV-målingar (frå
`fiks-dqv-measurements-data-policy-nokkel.md`) neste gong
`make gen-modellkatalog-instance` køyrer (CI køyrer dette før generatorfasen).

Å berre leggje til data/skjema-attributt utan å fikse denne overskrivings-
åtferda ville løyst 7a/7b kosmetisk, men brote dei att ved neste CI-køyring.

## Steg

1. **`collect-concepts.py`:** før skriving, last eksisterande datafil (om ho
   finst) og bevar alle toppnivånøklar unntatt `begrep` (`samlingar`,
   `kvalitetsmaalingar`, m.fl.) uendra.
2. **`generate-modellkatalog.py`:** før skriving, last eksisterande datafil
   (om ho finst) og bevar `kvalitetsmaalingar`-blokka og
   `har_kvalitetsmaaling`-referansen på `modellkataloger[0]`.
3. **Legg til `kvalitetsmaalingar`-attributtet** på `ModellkatalogContainer` i
   `digdir-`, `kartverket-`, `ksdigital-`, `novari-` og
   `skatteetaten-modellkatalog-schema.yaml` (kopier attributt-definisjonen
   frå `brreg-modellkatalog-schema.yaml`).
4. **Gjenopprett `samlingar:`-blokka** i `brreg-begrepskatalog.yaml` med dei
   same, verifiserte historiske verdiane (frå git-historikk/eksempelfila) —
   ikkje nye, oppfunne verdiar.
5. Køyr `make gen-begrepskatalog-instance` og `make gen-modellkatalog-instance`
   på nytt for å stadfeste at dei bevarer eksisterande DQV-data (regresjonstest
   for steg 1-2).
6. Køyr `make gen-dqv-measurements` for å populere friske målingar for alle 7
   datafiler (begrepskatalog + 6 modellkatalogar).
7. Valider alle påverka datafiler med `make validate-instance`.
8. Oppdater `mkdocs/docs/arkitektur/standardetterleving.md`: fjern/marker
   gap 7a og 7b som løyste, rad "Beskrivelse av kvalitet på datasett" tilbake
   til ✅ dersom alt er verifisert grønt.

## Utført

1. **`collect-concepts.py`** (`generate_begrepskatalog()`): les no eksisterande
   datafil før skriving og bevarer alle toppnivånøklar unntatt `begrep`.
   Verifisert: køyrde `make gen-begrepskatalog-instance` på nytt etter
   steg 4 — `samlingar:`-blokka overlevde uendra.
2. **`generate-modellkatalog.py`** (`main()`): les no eksisterande datafil
   før skriving og bevarer `kvalitetsmaalingar` (toppnivå) og
   `modellkataloger[0].har_kvalitetsmaaling`.
   **Viktig funn under verifisering:** full køyring av
   `make gen-modellkatalog-instance` avdekte at dei 6 modellkatalog-
   datafilene er **sterkt utdaterte** i forhold til kva generatoren i dag
   ville produsert frå `metadata/*-manifest.yaml` (andre URI-mønster, fleire
   informasjonsmodellar, endra skildringar/`tema`-felt m.m.) — ei drift som
   er heilt uavhengig av DQV-fiksen. Denne regenereringa vart **reversert**
   (`git checkout --`) for å halde denne specen avgrensa til DQV-omfanget;
   den brei drifta er ikkje del av denne fiksen og bør handterast i ein eigen,
   dedikert spec dersom han skal rettast opp.
3. **Skjema-fiks (7b):** `kvalitetsmaalingar`-attributtet lagt til
   `ModellkatalogContainer` i `digdir-`, `kartverket-`, `ksdigital-`,
   `novari-` og `skatteetaten-modellkatalog-schema.yaml`, identisk med
   `brreg-modellkatalog-schema.yaml`. Verifisert med `make validate-instance`
   og `make lint` (same pre-eksisterande "manglar description"-åtvaringar
   som brreg-modellkatalog, ingen nye feil).
4. **Datagjenoppretting (7a):** `samlingar:`-blokka i
   `brreg-begrepskatalog.yaml` er gjenoppretta med dei same verifiserte
   historiske verdiane (id, tittel nb+nn, kontaktpunkt, utgjevar, beskriving,
   medlem-liste) — henta frå git-historikk (commit `9009b1e6`, før
   `collect-concepts.py` viska ut blokka i `e2d7d952`) og
   `examples/brreg-begrepskatalog-eksempel.yaml` (som alt hadde nb+nn-versjonen).
   Ikkje oppfunne nytt innhald.
5. **`make gen-dqv-measurements`** køyrd på nytt etter alle fiksane: alle 7
   datafiler (begrepskatalog + 6 modellkatalogar) fekk friske
   kvalitetsmålingar. Alle 7 validerte med `make validate-instance` — «No
   issues found».
6. **`mkdocs/docs/arkitektur/standardetterleving.md`:** rad "Beskrivelse av
   kvalitet på datasett" tilbake til ✅. Gap 7 markert lukka (samla med
   `fiks-dqv-measurements-data-policy-nokkel.md`). Nytt, lågt prioritert
   gap 8 lagt til: faktoriser `ModellkatalogContainer` til delt basisskjema
   (DRY) — reint vedlikehaldspoeng, ikkje eit standardetterlevingsgap.

**Ikkje del av denne specen:** den brei datadrifta i dei 6 modellkatalog-
datafilene (punkt 2 over) og faktorisering av `ModellkatalogContainer` (gap 8).
