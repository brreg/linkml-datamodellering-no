# Verifiser artefakttype-flagg i build.yaml og README.md

## Bakgrunn

Brukaren bad om å verifisere at `build.yaml`-manifest (kalla "manifest.yaml" i
førespurnaden — det finst ingen fil med det litterale namnet, det er
`build.yaml` som er manifestformatet, jf. CLAUDE.md § Namngjeving →
Manifestformat) har flagg for alle tilgjengelege artefakttypar, og at
`README.md` dokumenterer alle desse.

Kartlegging viste:

- **README.md** (linje 237-256): dokumenterer alle 15 kjende `generators:`-
  flagg (`jsonld_context`, `shacl`, `owl`, `rdf`, `example_rdf`, `python`,
  `json_schema`, `xsd`, `protobuf`, `graphql`, `asyncapi`, `openapi`,
  `erdiagram`, `plantuml`, `docs`) i artefakt-tabellen, med lenke til
  tilhøyrande `COMMANDS.md`-target. Ingen manglar.
- **build.yaml** (34 skjema-manifest med `generators:`-seksjon): 11 filer
  manglar eitt eller flere av dei nyare flagga (`xsd`, `asyncapi`, `openapi`)
  — sannsynlegvis fordi manifesta vart skrivne før desse generatorane fanst
  og aldri fekk ettermontert flagget. `batch-generate.py:176-181`
  (`read_build_yaml_flag`) tolkar eit fråverande flagg identisk med
  `false`, så oppførselen er uendra i dag — men det er implisitt, ikkje
  eksplisitt dokumentert i manifestet sjølv.

Brukaren valde: legg til dei manglande flagga som `false` (gjør dagens
implisitte oppførsel eksplisitt, ingen endring i kva som genererast).

## Filer som skal rettast

| Fil | Manglar |
|---|---|
| `src/linkml/ap-no/common-ap-no/build.yaml` | `xsd`, `openapi`, `asyncapi` |
| `src/linkml/oreg/begrepssamling-foretaksregisteret/build.yaml` | `xsd`, `openapi`, `asyncapi` |
| `src/linkml/referanse/referansemodell/build.yaml` | `xsd`, `openapi`, `asyncapi` |
| `src/linkml/referanse/referansemodell-bronze/build.yaml` | `xsd`, `openapi`, `asyncapi` |
| `src/linkml/referanse/referansemodell-gold/build.yaml` | `xsd`, `openapi`, `asyncapi` |
| `src/linkml/referanse/referansemodell-silver/build.yaml` | `xsd`, `openapi`, `asyncapi` |
| `src/linkml/modellkatalog/digdir-modellkatalog/build.yaml` | `xsd`, `asyncapi` |
| `src/linkml/modellkatalog/kartverket-modellkatalog/build.yaml` | `xsd`, `asyncapi` |
| `src/linkml/modellkatalog/ksdigital-modellkatalog/build.yaml` | `xsd`, `asyncapi` |
| `src/linkml/modellkatalog/novari-modellkatalog/build.yaml` | `xsd`, `asyncapi` |
| `src/linkml/modellkatalog/skatteetaten-modellkatalog/build.yaml` | `xsd`, `asyncapi` |

## Steg

1. Legg til manglande flagg (`xsd: false`, `openapi: false`, `asyncapi: false`
   der aktuelt) i alle 11 filer, plassert i samme relative rekkjefølgje som
   dei komplette manifesta (`xsd` → `openapi` → `asyncapi`, etter
   `example_rdf`/eksisterande `openapi`).
2. Verifiser med det same Python-oppslaget som avdekte avviket at alle 34
   skjema-manifest no har alle 15 flagg.
3. README.md krev ingen endring (allereie komplett) — dokumenter dette i
   spec utan filendring.
4. Generer commit-melding og flytt spec til `specs/done/`.

## Handlingsliste

- [x] Rett dei 11 build.yaml-filene
- [x] Verifiser fullstendigheit på nytt
- [x] Commit-melding
- [x] Flytt spec til specs/done/

## Utført

Alle 11 manifest fekk lagt til manglande flagg som `false`, i samme
rekkjefølgje (`xsd` → `openapi` → `asyncapi`) som dei allereie komplette
manifesta. Verifiseringsskriptet stadfestar at alle 34 skjema-manifest no
har alle 15 kjende `generators:`-flagg. README.md var allereie komplett —
ingen endring der.
