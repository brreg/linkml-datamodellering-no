# Kjeldehenvisning for felles-begrepskatalog og felles-datakatalog

## Bakgrunn

Brukaren ønskjer at kvar valideringsregel i `felles-begrepskatalog`- og
`felles-datakatalog`-tabellane i `src/mcp-linkml-validator/policies/README.md`
skal henvise til kjelda for regelen — dvs. kva stad i den offisielle
spesifikasjonen (SKOS-AP-NO-Begrep / ModelDCAT-AP-NO) som fastset
kravnivået. Brukaren sin uttalte føresetnad: obligatoriske eigenskapar i
spesifikasjonen skal gje `error`, anbefalte skal gje `warning` — "typisk
slik" i dag.

For å kunne skrive korrekte kjeldelenkjer (ikkje gjette URL-ar, jf.
retningslinja om aldri å generere/gjette URL-ar), vart dei to offisielle
spesifikasjonssidene henta og gjennomgått:

- ModelDCAT-AP-NO: <https://data.norge.no/specification/modelldcat-ap-no>
  (base-URL alt kjend frå `see_also:` i `modelldcat-ap-no-schema.yaml`)
- SKOS-AP-NO-Begrep: <https://data.norge.no/specification/skos-ap-no-begrep>
  (base-URL alt kjend frå `see_also:` i `skos-ap-no-schema.yaml`)
- ModelDCAT-AP-NO sitt eige namnerom-vedlegg:
  <https://data.norge.no/specification/modelldcat-ap-no#Navnerom>
  («Vedlegg A – Navnerom som er brukt i spesifikasjonen» — stadfesta å
  liste både `dct` og `dcat` med URI). Brukt som kjelde for
  `schema_brukar_dct_prefix`/`schema_brukar_dcat_prefix` i
  `felles-datakatalog`-tabellen.
- SKOS-AP-NO-Begrep sitt eige namnerom-vedlegg:
  <https://informasjonsforvaltning.github.io/skos-ap-no-begrep/#Navnerom-brukt-i-standarden>
  («Vedlegg A – Navnerom som er brukt i denne standard», Tabell 5 —
  stadfesta å liste `dct`, `dcat` og `skos` med URI). Brukt som kjelde for
  `schema_brukar_dct_prefix`/`schema_brukar_skos_prefix` i
  `felles-begrepskatalog`-tabellen.
- Ei DCAT-AP-NO-namnerom-side (<https://informasjonsforvaltning.github.io/dcat-ap-no/#URIer-i-bruk>)
  vart vurdert som eit tredje alternativ, men er ikkje brukt: dei to
  spesifikke spesifikasjonane sine eigne namnerom-vedlegg (over) er meir
  presise kjelder for prefikskrav som håndhevast innanfor akkurat den
  spesifikasjonen, sidan dei ikkje krev eit ekstra hopp til ein
  søsterspesifikasjon.

Begge sidene har **stabile per-eigenskap-anker** i HTML-en (t.d.
`id="Informasjonsmodell-tittel"`, `id="Begrep-anbefalt-term"`) og eit
eksplisitt felt **«Kravnivå / Requirement level: Obligatorisk/Anbefalt/
Valgfri»** for kvar eigenskap. Desse ankera og kravnivåa vart lest ut
systematisk og samanlikna mot `severity:`-verdien i
`felles-datakatalog.yaml` og `felles-begrepskatalog.yaml`.

## Funn: brukaren sin føresetnad stemmer nesten heilt — 2 avvik i ModelDCAT-AP-NO

**SKOS-AP-NO-Begrep (felles-begrepskatalog.yaml): 0 avvik.** Alle 29
sjekkane sin `severity` stemmer nøyaktig med spesifikasjonen sitt
Kravnivå-felt for tilhøyrande eigenskap.

**ModelDCAT-AP-NO (felles-datakatalog.yaml): 2 avvik:**

| Sjekk (kode) | Noverande `severity` | Kravnivå i spesifikasjonen | Bør vere |
|---|---|---|---|
| `informasjonsmodell_har_kontaktpunkt` | `warning` | **Obligatorisk** (3.15.1.1, multiplisitet 1..n) | `error` |
| `modellkatalog_har_identifikator` | `error` | **Anbefalt** (3.22.2.3) — spesifikasjonen presiserer eksplisitt i kap. 4.4 at `dct:identifier` medvite er sett som anbefalt (ikkje obligatorisk) sidan instansar av Modellkatalog/Informasjonsmodell m.fl. alt får ein «innebygd» identifikator (URI-en/subjektet i RDF-triplet) | `warning` |

Merk at `dct:hasPart` (`modellkatalog_har_del`) **er** obligatorisk (3.22.1.2)
og `modelldcatno:model` (`modellkatalog_har_modell`) **er** anbefalt
(3.22.2.5) i den formelle Kravnivå-tabellen, sjølv om ei forklarande
brødtekst-passasje i kap. 4.3.2 kan lesast som at `modell` er obligatorisk
("er det obligatorisk å inkludere minst én informasjonsmodell") — den
forklarande teksten er ikkje den normative Kravnivå-erklæringa, så
noverande `warning` er korrekt og skal **ikkje** endrast.

## Forslag

### 1. Ny «Kjelde»-kolonne i README.md

Legg til ein femte kolonne «Kjelde» i tabellane under
§ [`felles-begrepskatalog`](#felles-begrepskatalog) og
§ [`felles-datakatalog`](#felles-datakatalog) i
`src/mcp-linkml-validator/policies/README.md`, med direkte lenkje til
anker-seksjonen i spesifikasjonen. For sjekkar utan eit tilsvarande
normativt punkt i sjølve spesifikasjonsteksten (import-/prefiks-/
container-krav som er LinkML-tekniske føresetnader for å uttrykke
vokabularet, og instanssjekkar med repo-interne kjende-utgivar-lister),
merk kjelda som *«Repo-krav»* eller *«Repo-intern»* i staden for å lenkje
til eit ikkje-eksisterande normativt ankerpunkt.

### 2. Full kjeldetabell — `felles-datakatalog` (ModelDCAT-AP-NO)

Klar til å limast inn som ny kolonne, i rekkjefølgja radene alt står i
README-tabellen:

| Kode | Kjelde | Kravnivå |
|---|---|---|
| `schema_importerer_modelldcat_ap_no` | Repo-krav (LinkML-import, ikkje eit spesifikasjonspunkt) | — |
| `schema_brukar_dct_prefix` | [Vedlegg A — Navnerom (ModelDCAT-AP-NO)](https://data.norge.no/specification/modelldcat-ap-no#Navnerom) | — |
| `schema_brukar_dcat_prefix` | [Vedlegg A — Navnerom (ModelDCAT-AP-NO)](https://data.norge.no/specification/modelldcat-ap-no#Navnerom) | — |
| `container_har_modellkatalog` | [§ Modellkatalog](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog) (repo-konvensjon: `tree_root`) | — |
| `container_har_informasjonsmodell` | [§ Informasjonsmodell](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell) (repo-konvensjon) | — |
| `modellkatalog_har_tittel` | [§ 3.22.1.4 Modellkatalog – tittel](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-tittel) | Obligatorisk |
| `modellkatalog_har_beskrivelse` | [§ 3.22.1.1 Modellkatalog – beskrivelse](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-beskrivelse) | Obligatorisk |
| `modellkatalog_har_identifikator` | [§ 3.22.2.3 Modellkatalog – identifikator](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-identifikator) | **Anbefalt** ⚠️ |
| `modellkatalog_har_utgjevar` | [§ 3.22.1.5 Modellkatalog – utgiver](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-utgiver) | Obligatorisk |
| `modellkatalog_har_kontaktpunkt` | [§ 3.22.1.3 Modellkatalog – kontaktpunkt](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-kontaktpunkt) | Obligatorisk |
| `modellkatalog_har_del` | [§ 3.22.1.2 Modellkatalog – har del](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-har-del) | Obligatorisk |
| `modellkatalog_har_lisens` | [§ 3.22.2.4 Modellkatalog – lisens](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-lisens) | Anbefalt |
| `modellkatalog_har_modell` | [§ 3.22.2.5 Modellkatalog – modell](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-modell) | Anbefalt |
| `informasjonsmodell_har_tittel` | [§ 3.15.1.2 Informasjonsmodell – tittel](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-tittel) | Obligatorisk |
| `informasjonsmodell_har_utgjevar` | [§ 3.15.1.3 Informasjonsmodell – utgiver](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-utgiver) | Obligatorisk |
| `informasjonsmodell_har_beskrivelse` | [§ 3.15.2.2 Informasjonsmodell – beskrivelse](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-beskrivelse) | Anbefalt |
| `informasjonsmodell_har_identifikator` | [§ 3.15.2.3 Informasjonsmodell – identifikator](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-identifikator) | Anbefalt |
| `informasjonsmodell_har_modellidentifikator` | [§ 3.15.2.4 Informasjonsmodell – informasjonsmodellidentifikator](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-informasjonsmodellidentifikator) | Anbefalt |
| `informasjonsmodell_har_kontaktpunkt` | [§ 3.15.1.1 Informasjonsmodell – kontaktpunkt](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-kontaktpunkt) | **Obligatorisk** ⚠️ |
| `informasjonsmodell_har_lisens` | [§ 3.15.2.6 Informasjonsmodell – lisens](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-lisens) | Anbefalt |
| `informasjonsmodell_har_tema` | [§ 3.15.2.7 Informasjonsmodell – tema](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-tema) | Anbefalt |
| `informasjonsmodell_har_modellelement` | [§ 3.15.2.5 Informasjonsmodell – inneholder modellelement](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-inneholder-modellelement) | Anbefalt |
| `utgjevar_er_kjend_org` (instans) | Repo-intern (kjend-utgivar-liste, ikkje frå spesifikasjonen) | — |

### 3. Full kjeldetabell — `felles-begrepskatalog` (SKOS-AP-NO-Begrep)

| Kode | Kjelde | Kravnivå |
|---|---|---|
| `schema_importerer_skos_ap_no` | Repo-krav (LinkML-import, ikkje eit spesifikasjonspunkt) | — |
| `schema_brukar_skos_prefix` | [Vedlegg A — Navnerom brukt i standarden, Tabell 5 (SKOS-AP-NO-Begrep)](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/#Navnerom-brukt-i-standarden) | — |
| `schema_brukar_dct_prefix` | [Vedlegg A — Navnerom brukt i standarden, Tabell 5 (SKOS-AP-NO-Begrep)](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/#Navnerom-brukt-i-standarden) | — |
| `container_har_begrep` | [§ Begrep](https://data.norge.no/specification/skos-ap-no-begrep#Begrep) (repo-konvensjon: `tree_root`) | — |
| `container_har_samling` | [§ Begrepssamling](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling) (repo-konvensjon) | — |
| `begrep_har_anbefalt_term` | [§ 3.5.1.1 Begrep – anbefalt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-anbefalt-term) | Obligatorisk |
| `begrep_anbefalt_term_er_multivalued_langstring` | [§ 3.5.1.1 Begrep – anbefalt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-anbefalt-term) (Merknad 1: multiplisitet 2..n, bokmål+nynorsk) | Obligatorisk |
| `begrep_har_definisjon` | [§ Begrep – definisjon, direkte angivelse](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-definisjon-direkte-angivelse) / [via definisjonsobjekt](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-definisjon-via-definisjonsobjekt) | Obligatorisk |
| `begrep_har_identifikator` | [§ Begrep – identifikator](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-identifikator) | Obligatorisk |
| `begrep_har_utgjevar` | [§ Begrep – publisert av](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-publisert-av) | Obligatorisk |
| `begrep_har_kontaktpunkt` | [§ Begrep – kontaktpunkt](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-kontaktpunkt) | Obligatorisk |
| `begrep_har_fagomrade` | [§ 3.5.2.6 Begrep – fagområde](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-fagområde) | Anbefalt |
| `begrep_har_ansvarleg_verksemd` | [§ Begrep – ansvarlig virksomhet](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-ansvarlig-virksomhet) | Anbefalt |
| `begrep_har_gyldig_fra` | [§ Begrep – dato gyldig fra og med](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-gyldig-fra-og-med) | Anbefalt |
| `begrep_har_gyldig_til` | [§ Begrep – dato gyldig til og med](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-gyldig-til-og-med) | Anbefalt |
| `begrep_har_opprettingsdato` | [§ Begrep – dato opprettet](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-opprettet) | Anbefalt |
| `begrep_har_endringsdato` | [§ Begrep – dato sist oppdatert](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-sist-oppdatert) | Anbefalt |
| `begrep_har_merknad` | [§ Begrep – merknad](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-merknad) | Anbefalt |
| `begrep_har_tillate_term` | [§ Begrep – tillatt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-tillatt-term) | Anbefalt |
| `definisjon_har_tekst` | [§ Definisjon – tekst](https://data.norge.no/specification/skos-ap-no-begrep#Definisjon-tekst) | Obligatorisk |
| `definisjon_har_kjelde_relasjon` | [§ Definisjon – forhold til kilde](https://data.norge.no/specification/skos-ap-no-begrep#Definisjon-forhold-til-kilde) | Anbefalt |
| `assosiativ_relasjon_har_til_omgrep` | [§ Assosiativ begrepsrelasjon – har til begrep](https://data.norge.no/specification/skos-ap-no-begrep#Assosiativ-begrepsrelasjon-har-til-begrep) | Obligatorisk |
| `assosiativ_relasjon_har_relasjontype` | [§ Assosiativ begrepsrelasjon – relasjonsrolle](https://data.norge.no/specification/skos-ap-no-begrep#Assosiativ-begrepsrelasjon-relasjonsrolle) | Obligatorisk |
| `generisk_relasjon_har_overomgrep` | [§ Generisk begrepsrelasjon – har overbegrep](https://data.norge.no/specification/skos-ap-no-begrep#Generisk-begrepsrelasjon-har-overbegrep) | Obligatorisk |
| `generisk_relasjon_har_underomgrep` | [§ Generisk begrepsrelasjon – har underbegrep](https://data.norge.no/specification/skos-ap-no-begrep#Generisk-begrepsrelasjon-har-underbegrep) | Obligatorisk |
| `generisk_relasjon_har_inndelingskriterium` | [§ Generisk begrepsrelasjon – inndelingskriterium](https://data.norge.no/specification/skos-ap-no-begrep#Generisk-begrepsrelasjon-inndelingskriterium) | Anbefalt |
| `partitiv_relasjon_har_delomgrep` | [§ Partitiv begrepsrelasjon – har delbegrep](https://data.norge.no/specification/skos-ap-no-begrep#Partitiv-begrepsrelasjon-har-delbegrep) | Obligatorisk |
| `partitiv_relasjon_har_heilskapleg_omgrep` | [§ Partitiv begrepsrelasjon – har helhetsbegrep](https://data.norge.no/specification/skos-ap-no-begrep#Partitiv-begrepsrelasjon-har-helhetsbegrep) | Obligatorisk |
| `partitiv_relasjon_har_inndelingskriterium` | [§ Partitiv begrepsrelasjon – inndelingskriterium](https://data.norge.no/specification/skos-ap-no-begrep#Partitiv-begrepsrelasjon-inndelingskriterium) | Anbefalt |
| `samling_har_identifikator` | [§ Begrepssamling – identifikator](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling-identifikator) | Obligatorisk |
| `samling_har_tittel` | [§ Begrepssamling – navn](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling-navn) | Obligatorisk |
| `samling_har_utgjevar` | [§ Begrepssamling – publisert av](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling-publisert-av) | Obligatorisk |
| `samling_har_kontaktpunkt` | [§ Begrepssamling – kontaktpunkt](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling-kontaktpunkt) | Obligatorisk |
| `samling_har_medlem` | [§ Begrepssamling – inneholder begrep](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling-inneholder-begrep) | Obligatorisk |
| `samling_har_beskrivelse` | [§ Begrepssamling – beskrivelse](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling-beskrivelse) | Anbefalt |
| `begrep_har_definisjon_pa_nb_og_nn` (instans) | [§ 3.5.1.1 Begrep – anbefalt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-anbefalt-term) (Merknad 1+2: tospråkskravet) | Obligatorisk |
| `utgjevar_er_kjend_org` (instans) | Repo-intern (kjend-utgivar-liste, ikkje frå spesifikasjonen) | — |

## Avklaringar (stadfesta av brukaren)

1. **Ja** — dei to avvika i ModelDCAT-AP-NO skal rettast som del av denne
   specen: `informasjonsmodell_har_kontaktpunkt` → `severity: error`,
   `modellkatalog_har_identifikator` → `severity: warning`, i
   `felles-datakatalog.yaml`.
2. **Ja** — kjelda skal òg leggjast inn som eit maskinlesbart felt
   (`spec_url:`) i sjølve `checks:`-oppføringane i både
   `felles-datakatalog.yaml` og `felles-begrepskatalog.yaml`, ikkje berre
   som ein kolonne i README.md. **Avgrensing:** dette er berre eit nytt,
   passivt metadatafelt på kvar `checks:`-oppføring (same slag som dei
   allereie eksisterande `digdir_rule:`/`fair_principle:`-felta i andre
   policyfiler) — det vert **ikkje** lese av `_run_checks`/
   `_CHECK_HANDLERS` i `server.py`, og syner difor **ikkje** automatisk
   opp i MCP-verktøyresultata (`issues[].message`) med mindre det gjerast
   som eit eige, seinare steg. README.md sin «Kjelde»-kolonne er framleis
   handhalden separat (ingen auto-genereringsskript koplar `spec_url:` til
   README-tabellen i dag — stadfesta ved gjennomgang av
   `generate-readme-tables.sh`, som berre genererer rot-`README.md` sine
   domene-/skjema-tabellar, ikkje `policies/README.md`).
3. **Ja** — legg til ei kort fotnote under kvar av dei to tabellane som
   forklarar `Repo-krav`/`Repo-intern`-merkinga.

## Steg

1. Legg til «Kjelde»-kolonne i `felles-datakatalog`-tabellen i
   `src/mcp-linkml-validator/policies/README.md`, med verdiane frå
   tabellen i punkt 2 over.
2. Legg til «Kjelde»-kolonne i `felles-begrepskatalog`-tabellen, med
   verdiane frå tabellen i punkt 3 over.
3. Legg til ei kort fotnote under kvar tabell som forklarar
   `Repo-krav`/`Repo-intern`-merkinga.
4. Legg til `spec_url:`-felt på kvar `checks:`-oppføring i
   `felles-datakatalog.yaml` og `felles-begrepskatalog.yaml`, med same
   URL som i README-kjeldetabellane (punkt 2/3). Oppføringar merkte
   «Repo-krav»/«Repo-intern» i README får **ikkje** noko `spec_url:`-felt
   (ingen normativ kjelde å peike til).
5. Rett `informasjonsmodell_har_kontaktpunkt` til `severity: error` og
   `modellkatalog_har_identifikator` til `severity: warning` i
   `felles-datakatalog.yaml`. Oppdater `description`-tekstane til å seie
   høvesvis «Obligatorisk» og «Anbefalt» konsekvent med den nye
   alvorsgraden.
6. Køyr `make mcp-linkml-valider-modell-test` for å stadfeste at
   eksisterande testar framleis er grøne, og legg til nye testar for dei
   to endra sjekkane (positiv/negativ for begge, same mønster som
   eksisterande `TestGold`/`TestSilver`-testar).
7. Køyr `make mcp-linkml-valider-modell SCHEMA=<modellkatalogskjema> POLICY=felles-datakatalog`
   mot eksisterande modellkatalogskjema (t.d. `digdir-modellkatalog`,
   `brreg-modellkatalog`) for å stadfeste om nokon av dei no får eit nytt
   avvik (manglar `kontaktpunkt` på ein `Informasjonsmodell`-instans) —
   varsle brukaren dersom så er tilfelle, sidan det kan krevje ei
   oppfølgingsendring i modellkatalog-datafilene deira.

## Handlingsliste

- [x] Steg 1: Kjelde-kolonne i `felles-datakatalog`-tabellen
- [x] Steg 2: Kjelde-kolonne i `felles-begrepskatalog`-tabellen
- [x] Steg 3: Fotnote for Repo-krav/Repo-intern
- [x] Steg 4: `spec_url:`-felt i begge YAML-policyfilene
- [x] Steg 5: Rett dei to avvika i `felles-datakatalog.yaml`
- [x] Steg 6: Testverifisering
- [x] Steg 7: Regresjonssjekk mot reelle modellkatalogskjema

## Utført

**Dato:** 2026-08-31

Alle sju steg gjennomførte som planlagt.

- **`policies/README.md`:** ny «Kjelde»-kolonne lagt til i både
  `felles-begrepskatalog`- og `felles-datakatalog`-tabellen, med direkte
  lenkjer til spesifikasjonsankera identifiserte tidlegare i denne specen.
  Dei to feilretta radene (`modellkatalog_har_identifikator` → warning,
  `informasjonsmodell_har_kontaktpunkt` → error, flytta til
  obligatorisk-gruppa) er oppdaterte i tabellen, med ei forklarande linje
  under tabellen. Fotnotar (¹Repo-krav, ²Repo-konvensjon, ³Repo-intern)
  lagt til under begge tabellane.
- **`felles-datakatalog.yaml`:** `spec_url:` lagt til på alle 21 sjekkar
  med normativ kjelde (unnateke `schema_importerer_modelldcat_ap_no`, som
  er reint repo-krav). `modellkatalog_har_identifikator` endra til
  `severity: warning` og flytta til «anbefalte»-seksjonen;
  `informasjonsmodell_har_kontaktpunkt` endra til `severity: error` og
  flytta til «obligatoriske»-seksjonen. Begge sine `description:`-tekstar
  oppdaterte til å forklare kjelda til endringa.
- **`felles-begrepskatalog.yaml`:** `spec_url:` lagt til på alle 34
  sjekkar med normativ kjelde (`checks:` + éin `instance_checks:`-sjekk),
  unnateke `schema_importerer_skos_ap_no` og `utgjevar_er_kjend_org`
  (reine repo-krav/repo-interne). Ingen severity-endringar (0 avvik
  funne mot spesifikasjonen for denne policyen).
- **`tests/test_mcp_policies.py`:** ny `TestFellesDatakatalog`-klasse med
  4 nye testar (positiv/negativ for begge dei retta sjekkane), første
  gongen `felles-datakatalog`-policyen får eiga testdekning i denne
  fila. Alle 4 grøne.

**Verifisering:**

- `make mcp-linkml-valider-modell-test`: 43/44 testar grøne (44 totalt,
  opp frå 40 — dei 4 nye). Den attverande feilen
  (`TestGold.test_gyldig_skjema_har_ingen_feil`) er den same
  pre-eksisterande, urelaterte feilen dokumentert i
  `specs/done/utvid-dekningsgrad-regel-5-12-14-15.md` — ikkje påverka av
  denne specen, ikkje retta (utanfor scope).
- **Regresjonssjekk mot reelle modellkatalogskjema (steg 7):** køyrde
  `make mcp-linkml-valider-modell SCHEMA=... POLICY=felles-datakatalog
  INSTANCE=...` for `digdir-modellkatalog` og `brreg-modellkatalog`, både
  før (via `git stash`) og etter endringane. Identisk resultat i begge
  tilfelle (`errorCount: 0`, éi uendra åtvaring). Ingen ny feil frå
  `informasjonsmodell_har_kontaktpunkt`-endringa: sjekken
  (`merged_class_has_slot_with_uri`) er ein **skjemastrukturell** sjekk
  (finst det ein slot med denne URI-en definert på klassen), ikkje ein
  instans-fullstendigheitssjekk — og `modelldcat-ap-no-schema.yaml`
  definerer alt `kontaktpunkt`-slotten strukturelt for `Informasjonsmodell`,
  så alle seks org-katalogane (som transitivt importerer same skjema) er
  upåverka. Genererte `validation/<versjon>/felles-datakatalog.json`-filer
  frå denne verifiseringa er rydda vekk att (ikkje del av leveransen).
