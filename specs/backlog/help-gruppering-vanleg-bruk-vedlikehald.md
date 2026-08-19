# Plan: betre gruppering enn «Vanleg bruk»/«Vedlikehald» i `make help`

## Bakgrunn

Brukaren synest gruppeoverskriftene **«Vanleg bruk»** og **«Vedlikehald»**
i `make help` (kjelde: `categories`-lista i
`src/assets/scripts/makefile/help.sh`) er lite treffande, og ønskjer anten
å erstatte dei med betre namn, eller flytte kommandoane i dei inn i
eksisterande overskrifter (`Generering`, `Validering`,
`Dokumentasjonsportal`, `Container images`, `MCP-serverar`,
`Modell-analyse`).

`categories` er ei ordna liste av `(overskrift|grep-mønster)`-par —
kvart target vert plassert under **fyrste** overskrift der grep-mønsteret
matchar, sjølv om eit anna, meir presist mønster lenger nede i lista også
ville matcha. Dette har alt skapt éin reell feilplassering (sjå under).

## Noverande situasjon

**«Vanleg bruk»** — mønster `(test|roundtrip|clean|help)`:

| Target | Kommentar |
|---|---|
| `make help` | Sjølvreferanse — viser denne oversikta |
| `make test` | Køyr alle testar |
| `make roundtrip` | Roundtrip-test (YAML→TTL→YAML) |
| `make roundtrip-json-schema` | JSON Schema-roundtrip-test |
| `make clean` | Slett `generated/` |
| `make mcp-linkml-valider-modell-test` | Policy-testar for validator-MCP-en — **feilplassert** |
| `make mcp-linkml-modell-utkast-test` | Unit-testar for modell-utkast-MCP-en — **feilplassert** |

Dei to siste hamnar her berre fordi `test`-mønsteret i «Vanleg bruk» står
**før** `mcp-`-mønsteret i «MCP-serverar» i lista — sjølve targetnamnet
startar med `mcp-` og høyrer openbert heime saman med
`mcp-linkml-valider-modell-run`/`-smoke` og
`mcp-linkml-modell-utkast-run`/`-smoke`, som alt ligg i «MCP-serverar».

**«Vedlikehald»** — mønster `(update-|new-|remove-|check-)`:

| Target | Kommentar |
|---|---|
| `make update-modellkatalog` | Oppdaterer modellkatalog frå `schema.annotations.*` — genererer eit derivert artefakt, same familie som `gen-modellkatalog-instance` (alt i «Generering») |
| `make new-modell` | Scaffolding: opprett ny domenemodell |
| `make remove-modell` | Scaffolding: fjern ein domenemodell |
| `make new-modellkatalog` | Scaffolding: opprett ny organisasjonskatalog |
| `make new-begrepssamling` | Scaffolding: opprett ny begrepssamling |
| `make new-begrepskatalog` | Scaffolding: opprett ny (legacy) begrepskatalog |
| `make update-valid-scopes` | Regenererer `.github/valid-scopes.txt` — køyrer automatisk etter `new-modell`/`new-modellkatalog`/`new-begrepssamling`, høyrer difor tematisk saman med scaffolding-targeta over |
| `make check-prereqs` | Miljø-/verktøysjekk — heilt urelatert til dei sju andre («opprett»/«oppdater» vs. «diagnostiser») |

«Vedlikehald» er difor i praksis **to ulike ting** stua saman: scaffolding
(opprett/fjern modellstruktur) og eitt reint diagnostikk-target
(`check-prereqs`) som ikkje høyrer heime i nokon av dei andre gruppene.

## Forslag

### Forslag A — Redistribuer alt til eksisterande overskrifter (ingen nye)

- `mcp-linkml-valider-modell-test`, `mcp-linkml-modell-utkast-test` →
  **MCP-serverar** (rettar feilplasseringa)
- `update-modellkatalog`, `update-valid-scopes` → **Generering** (begge
  regenererer eit derivert artefakt frå skjema-metadata)
- `new-modell`, `remove-modell`, `new-modellkatalog`,
  `new-begrepssamling`, `new-begrepskatalog` → **Generering** (dei
  *opprettar* skjemastruktur, som tematisk er nær generering) — **eller**
  behald som eigen gruppe, sjå Forslag B
- `check-prereqs` → vert då eit enkeltståande target utan naturleg
  heim blant dei attverande gruppene; må anten bli verande i ei (mindre)
  «Vanleg bruk»-gruppe saman med `test`/`roundtrip*`/`clean`/`help`, eller
  få ei eiga eittlinjegruppe («Diagnostikk»)
- **Fordel:** ingen nye overskrifter å halde ved like
- **Ulempe:** «Generering» vert svært lang (alt har 22 target frå før),
  og scaffolding (lag ny modell) er konseptuelt ganske ulikt
  artefakt-generering frå eit *eksisterande* skjema

### Forslag B — Éi ny overskrift for scaffolding, resten redistribuert

- Ny overskrift **«Opprett og fjern modellar»** (mønster
  `(new-|remove-modell)`) for `new-modell`, `remove-modell`,
  `new-modellkatalog`, `new-begrepssamling`, `new-begrepskatalog`
- `update-valid-scopes` → same nye gruppe (køyrer alltid som sisteskritt
  i scaffolding-targeta, høyrer tematisk saman)
- `update-modellkatalog` → **Generering**
- `mcp-*-test` → **MCP-serverar** (som i Forslag A)
- `check-prereqs` → behald i ei sterkt redusert **«Vanleg bruk»**
  saman med `help`/`test`/`roundtrip`/`roundtrip-json-schema`/`clean` —
  gruppa vert då reindyrka «kommandoar du køyrer ofte, uavhengig av
  domene/skjema», som er ein presis nok skildring til å halde namnet
  **«Vanleg bruk»**
- **Fordel:** kvar gruppe får ein tydeleg, smal definisjon; løyser
  feilplasseringa av `mcp-*-test`; «Vanleg bruk» vert presist i staden
  for eit samlesekk-namn
- **Ulempe:** éin ny overskrift (kategori-lista i `help.sh` veks frå 8
  til 9 rader — minimal vedlikehaldskostnad, same mønster som
  eksisterande kategoriar)

### Forslag C — Behald to grupper, berre nye namn (minimal endring)

- «Vanleg bruk» → **«Testing og opprydding»** (skildrar
  `test`/`roundtrip*`/`clean` presist; `help` og `check-prereqs` flyttar
  ut, sjå under)
- «Vedlikehald» → **«Opprett og fjern modellar»** (skildrar
  `new-*`/`remove-modell` presist; `update-modellkatalog`,
  `update-valid-scopes`, `check-prereqs` flyttar ut, sjå under)
- `help` → ingen eiga gruppe treng nemne han; kan liggje øvst utanfor
  kategori-lista (spesialtilfelle i `help.sh`), eller bli verande fyrst
  i «Testing og opprydding» sidan han uansett må stå ein stad
- `check-prereqs` → **Container images**-gruppa (miljøsjekken avdekker
  mellom anna podman-tilstand, nær i tema) — **eller** ny minimal
  «Diagnostikk»-gruppe åleine med dette eine targetet
- `update-modellkatalog`, `update-valid-scopes` → **Generering**
- `mcp-*-test` → **MCP-serverar**
- **Fordel:** minst mogleg strukturell endring (framleis 8 grupper, berre
  2 nye namn), likevel presise namn
- **Ulempe:** `check-prereqs` sin heim (Container images) er eit svakt
  tematisk grep — han sjekkar meir enn berre podman (Git, GNU Make,
  diskplass, WSL2)

## Anbefaling

**Forslag B.** Scaffolding er ein tydeleg nok eigen arbeidsflyt
(«eg vil lage/fjerne noko») til å fortene eiga overskrift, i staden for
anten å drukne i «Generering» (Forslag A) eller tvinge `check-prereqs`
inn i ei tematisk feil gruppe (Forslag C). Den attverande, sterkt
innsnevra «Vanleg bruk»-gruppa (`help`/`test`/`roundtrip*`/`clean`/
`check-prereqs`) er òg det einaste forslaget der namnet «Vanleg bruk»
faktisk held stikk — dei er kommandoar du køyrer jamleg, uavhengig av
kva skjema/domene du jobbar med, i motsetnad til `new-*`/`remove-modell`
som berre er aktuelle i det augeblikket du lagar/fjernar noko.

## Handlingsliste

1. [ ] Brukaren vel forslag A, B eller C (eller ein variant)
2. [ ] Oppdater `categories`-lista i `src/assets/scripts/makefile/help.sh`
   etter valt forslag
3. [ ] Verifiser med `make help` at alle target framleis vert viste,
   ingen fell ut eller dupliserer seg mellom grupper
4. [ ] `COMMANDS.md` (linje 62, 118, § «Vedlikehald» linje 247) og
   `mkdocs/docs/kom-i-gang/kommandoar.md` (§ «Vedlikehald» linje 135)
   har eigne, sjølvstendige seksjonar med namnet «Vedlikehald» —
   stadfesta ved grep. Uklart enno om desse skal spegle nye
   `help.sh`-gruppenamn 1:1, eller er sjølvstendige dokumentstrukturar
   som berre tilfeldigvis deler namn — avklar med brukaren før
   `COMMANDS.md`/mkdocs vert endra
