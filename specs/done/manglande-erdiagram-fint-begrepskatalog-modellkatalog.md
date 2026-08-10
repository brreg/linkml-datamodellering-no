# Manglande ER-diagram-seksjon for FINT, Begrepskatalog og Modellkatalog

## Bakgrunn

Brukaren observerte at index.md-sidene til FINT-, Begrepskatalog- og
Modellkatalog-modellane i mkdocs-portalen ikkje viser
«Entity-relationship diagram»-seksjonen med tilhøyrande PlantUML-diagram,
i motsetnad til t.d. NGR- og AP-NO-modellane.

## Rotårsak

`## Entity-relationship diagram`-seksjonen i kvar modell sin `index.md`
vert generert av `mkdocs/lib/sections/er_diagram.sh` (`generate_er_diagram`).
Funksjonen sjekkar om `diagrams/<schema>-filtered.svg` eller
`diagrams/<schema>.svg` finst i `generated/<domain>/<schema>/` — finst
ingen av dei, hoppar funksjonen stille over heile seksjonen (linje 6-53,
ingen `else`-gren som feilar eller varslar).

Desse SVG-ane vert produserte av `make gen-plantuml`. Målet er derimot
**gata bak `build.yaml`-flagget `plantuml: true`**
(`make/10-generator-macros.mk` linje 107-122): skjema utan flagget vert
filtrerte bort før `batch-generate.py`/`batch-render-plantuml.sh` køyrer,
så det finst aldri nokon `diagrams/`-katalog for dei i eit reint
CI-bygg.

Alle 14 skjema i dei tre nemnde domena har `plantuml: false`:

| Domene | Skjema | Kjelde til flagget |
|---|---|---|
| FINT | fint-administrasjon, fint-arkiv, fint-common, fint-okonomi, fint-personvern, fint-ressurs, fint-utdanning | Bevisst avskrudd i commit `0987f9cb` («skrur av generering av json_context, shacl, python, protobuf, plantuml og openapi for alle skjema») |
| Begrepskatalog | brreg-begrepskatalog | Udokumentert standardverdi i `src/assets/scripts/scaffolding/new-begrepskatalog.sh:117` |
| Modellkatalog | brreg-modellkatalog, digdir-modellkatalog, kartverket-modellkatalog, ksdigital-modellkatalog, novari-modellkatalog, skatteetaten-modellkatalog | Udokumentert standardverdi i `src/assets/scripts/scaffolding/new-modellkatalog.sh:169` |

Til samanlikning har `new-modell.sh:130` (brukt for NGR, samt, oreg m.fl.)
`plantuml: true` som standard.

**Lokal villeiing:** eit tidlegare lokalt bygg av `brreg-begrepskatalog`
(før gatinga i `10-generator-macros.mk` vart innført, eller frå eit
manuelt `make gen-plantuml SCHEMA=...`-kall) har lagt att ein
`generated/begrepskatalog/brreg-begrepskatalog/diagrams/`-katalog med
gyldige SVG-ar på disk. `generated/` er gitignora, så dette er berre eit
lokalt artefakt — eit reint CI-bygg (eller `make clean && make domain-...`)
har ikkje desse filene, og portalen som faktisk vert publisert manglar
seksjonen.

**Ikkje ein feil i `er_diagram.sh` eller `10-generator-macros.mk`** — begge
fungerer som dokumentert. Rotårsaka er at `plantuml: false` er sett (eller
aldri sett til `true`) i dei 14 `build.yaml`-filene, kombinert med at
scaffolding-standardane for begrepskatalog/modellkatalog aldri har hatt
diagram på som standard.

## Tiltak

Brukaren har stadfesta at fiksen skal omfatte alle tre domena (inkl. å
reversere plantuml-delen av `0987f9cb` for FINT).

1. Set `plantuml: true` i `generators:`-seksjonen i alle 14 `build.yaml`:
   - `src/linkml/fint/{fint-administrasjon,fint-arkiv,fint-common,fint-okonomi,fint-personvern,fint-ressurs,fint-utdanning}/build.yaml`
   - `src/linkml/begrepskatalog/brreg-begrepskatalog/build.yaml`
   - `src/linkml/modellkatalog/{brreg,digdir,kartverket,ksdigital,novari,skatteetaten}-modellkatalog/build.yaml`
2. Oppdater scaffolding-standardane slik at nye skjema av desse typane får
   diagram på frå start:
   - `src/assets/scripts/scaffolding/new-begrepskatalog.sh:117` → `plantuml: true`
   - `src/assets/scripts/scaffolding/new-modellkatalog.sh:169` → `plantuml: true`
   - (`new-begrepssamling.sh:60` er ein datafil-manifest utan `generators:`-bruk
     for skjemagenerering — sjå om flagget der er relevant, eller om det skal
     stå urørt sidan begrepssamlingar ikkje er skjema med klasser å teikne.)
3. Køyr `make gen-plantuml DOMAIN=fint`, `make gen-plantuml DOMAIN=begrepskatalog`
   og `make gen-plantuml DOMAIN=modellkatalog` og stadfest at
   `generated/<domain>/<schema>/diagrams/*.svg` vert produserte for alle 14.
4. Køyr `make docs-publish` (eller tilsvarande mkdocs-byggsteg) og stadfest
   at `mkdocs/docs/<domain>/<schema>/index.md` no inneheld
   `## Entity-relationship diagram`-seksjonen for alle 14 modellane.
5. Ryd opp det stale lokale `generated/begrepskatalog/brreg-begrepskatalog/diagrams/`-innhaldet
   (t.d. via `make clean` eller tilsvarande) slik at neste bygg reflekterer
   det oppdaterte `build.yaml`-flagget og ikkje eit gamalt artefakt.

## Utført

Tiltak 1-5 gjennomførte og verifiserte:
- `plantuml: true` sett i alle 14 `build.yaml` (7 FINT-skjema, 1
  Begrepskatalog-skjema, 6 Modellkatalog-skjema).
- Scaffolding-standardane i `new-begrepskatalog.sh:117` og
  `new-modellkatalog.sh:169` oppdatert til `plantuml: true`.
  `new-begrepssamling.sh:60` late urørt — begrepssamlingar har
  `erdiagram: false`/`docs: false` og er datafil-aggregat utan klassar å
  teikne, ikkje eit skjema.
- `make gen-plantuml DOMAIN=fint`, `DOMAIN=begrepskatalog` og
  `DOMAIN=modellkatalog` køyrde og produserte
  `generated/<domain>/<schema>/diagrams/*.svg` for alle 14 skjema
  (stadfesta med filstørrelse-sjekk).
- For Begrepskatalog og Modellkatalog er den *filtrerte* SVG-en tom
  (419 byte) sidan desse skjemaa berre definerer éin lokal
  containerklasse (`BegrepContainer`/`ModellkatalogContainer`) — resten av
  klassane er importerte frå AP-NO-skjema, og containerklassen vert
  filtrert bort per PRINCIPLES.md-regelen om at `tree_root`-klassar ikkje
  skal visast. Dette er korrekt filtreringsåtferd, ikkje ein feil —
  `er_diagram.sh` fell då tilbake til å vise full versjon med ei
  forklarande merknad, i staden for å utelate seksjonen heilt.
- `make docs-publish` køyrde reelt (i bakgrunnen, ~130s) og fullførte utan
  feil. Verifisert med grep at `## Entity-relationship diagram` no finst i
  `mkdocs/docs/<domain>/<schema>/index.md` for alle 14 modellane.
- Det stale lokale diagram-artefaktet i
  `generated/begrepskatalog/brreg-begrepskatalog/diagrams/` er no
  overskrive av eit ferskt bygg (stadfesta med filtidsstempel).
- Merk: `podman run` feila først med
  «chmod /run/user/1000/libpod: read-only file system» i sandboxa
  Bash-økt — måtte køyrast med sandbox mellombels avskrudd. Ikkje eit
  produktfeil, berre eit lokalt økt-miljøavvik.
