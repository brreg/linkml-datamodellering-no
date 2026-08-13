# Bør new-modell sin genererte license: peike på EULicence.NLOD_2_0 i staden for data.norge.no?

## Avvist

**Avvist 2026-08-13.** `schema.license` og `EULicence`/`Lisensdokument.id`
er to **ulike felt med ulikt formål og ulik dokumentert konvensjon** — dei
treng ikkje bruke same URI-form, og eit skifte til EU-forma for
`schema.license` ville bryte den **eksisterande, dominerande, dokumenterte**
konvensjonen i heile resten av repoet.

Empirisk sjekk avgjer saka: **28 av 29** eksisterande skjema i repoet
brukar allereie `https://data.norge.no/nlod/no/2.0` for `license:` — det
er òg det som alt stod dokumentert i `CLAUDE.md`/`CONVENTIONS.md` frå før.
`schema.license` vert dessutan aldri validert eller kryssjekka mot
`EULicence`-enumen, så ei eventuell «konsistens» mellom felta ville berre
vore kosmetisk, ikkje funksjonell. Sjå fullstendig grunngjeving under.

## Spørsmål

Etter at `specs/backlog/eulicence-nlod-norsk-lenke.md` konkluderte med at
`EULicence.NLOD_2_0` sitt `meaning:`-felt **skal** halde fram å peike til
EU Publications Office-forma
(`http://publications.europa.eu/resource/authority/licence/NLOD_2_0`), var
neste spørsmål: bør `schema.license` (feltet `new-modell.sh` genererer i
sjølve LinkML-skjemaet, endra i
`specs/done/new-modell-genererer-gyldig-eksempel.md` til
`https://data.norge.no/nlod/no/2.0`) i staden peike til **den same
EU-Publications-Office-URI-en** som `EULicence.NLOD_2_0.meaning`, for
konsistens?

## Vurdering — dei to felta er ikkje same konsept

| Felt | Kva det skildrar | Kven/kva brukar verdien |
|---|---|---|
| `schema.license` | Lisensen **LinkML-skjemaet/modell-definisjonen sjølv** er utgitt under (metadata om *artefakten*) | Menneske som les/gjenbrukar skjemaet; ingen RDF-serialisering av data-instansar |
| `Distribusjon.lisens` → `Lisensdokument.id` (via `EULicence`) | Lisensen **eit konkret datasett/distribusjon** er utgitt under (DCAT-AP-NO-metadata om *data*) | RDF/DCAT-verktøy som konsumerer publiserte datakatalogar; **skal** hentast frå EU-vokabularet (jf. `vokabular_krav: skal` i `common-ap-no-schema.yaml`) |

`schema.license` er eit **generisk LinkML-metafelt** (definert i
LinkML sin eigen metamodell, ikkje av `common-ap-no`) — det har **ingen**
`range`, `enum_referanse` eller `vokabular_krav`-avgrensing i det heile.
Kravet om å bruke EU-Publications-Office-vokabularet gjeld eksplisitt og
utelukkande `Lisensdokument.id` (jf. `lisens`-sloten sin dokumentasjon i
`common-ap-no-schema.yaml:513-524`, sjå
`specs/backlog/eulicence-nlod-norsk-lenke.md`).

## Empirisk stadfesting — kva brukar resten av repoet faktisk?

```bash
grep -h "^license:" src/linkml/*/*/[a-z]*-schema.yaml | sort | uniq -c | sort -rn
```

```
28 license: https://data.norge.no/nlod/no/2.0
 1 license: https://creativecommons.org/licenses/by/4.0/
```

**28 av 29 faktiske, eksisterande skjema i repoet** brukar allereie
`https://data.norge.no/nlod/no/2.0` for `license:`. Den eine avvikande
oppføringa (`src/linkml/oreg/veteranbilregisteret/veteranbilregisteret-schema.yaml`)
er nettopp modellen som utløyste heile denne spec-serien — generert **før**
`new-modell.sh` vart fiksa til å bruke NLOD 2.0 som standard, og er sjølv
eit argument for `data.norge.no`-forma, ikkje mot. **Ingen** skjema i
repoet brukar EU-Publications-Office-forma i `license:`-feltet.

`https://data.norge.no/nlod/no/2.0` er òg det eksplisitt dokumenterte
standardvalet i `CLAUDE.md` og `CONVENTIONS.md` (§ Schema-metadata,
`license`-rada), **uavhengig av** og **frå før** dette spec-arbeidet — det
er den etablerte konvensjonen i repoet, ikkje noko nytt vi innfører no.

## Konsekvens av å byte til EU-forma likevel

Å endre `new-modell.sh` sin standard til
`http://publications.europa.eu/resource/authority/licence/NLOD_2_0` ville:

1. Gjere **nye** modellar sitt `license:`-felt inkonsistent med **alle 28**
   eksisterande modellar, utan tilsvarande endring av dei — eit
   nytt, usemantisk skilje mellom «gamle» og «nye» skjema.
2. Krevje anten (a) å òg retroaktivt oppdatere alle 28 eksisterande skjema
   (stort, urelatert scope-hopp — ikkje bedt om), eller (b) leve med
   varig inkonsistens.
3. Ikkje gje nokon reell semantisk gevinst: `schema.license` vert aldri
   validert eller kryssjekka mot `EULicence`-enumen (dei er heilt
   frikopla felt), så «konsistens» her er berre kosmetisk, ikkje
   funksjonell.

`new-modell.sh` og `converter.py` sin `schema.license`-standard
(`https://data.norge.no/nlod/no/2.0`, sett i
`specs/done/new-modell-genererer-gyldig-eksempel.md`) står difor ved lag
som han er — ingen kodeendring. Denne spec-en dokumenterer vurderinga for
framtidig referanse, slik at spørsmålet ikkje treng takast opp på nytt
utan ny informasjon.
