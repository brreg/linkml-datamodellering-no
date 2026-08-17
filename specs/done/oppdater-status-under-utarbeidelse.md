# Oppdater status til UnderDevelopment i alle skjema

## Bakgrunn

`annotations.status` (ADMS Status, jf. Digdir-regel 9/10/11 og
`CLAUDE.md` § «Silver-annotasjonar») skal setjast til
`http://purl.org/adms/status/UnderDevelopment` («Under utarbeidelse») i
alle skjema. Kartlegging av noverande tilstand
(`grep -A5 '^annotations:' <fil> | grep status:` over alle 36 skjema med
`annotations:`-blokk):

**Har allereie `UnderDevelopment` (24 skjema) — ingen endring:**
`common-ap-no`, `brreg-modellkatalog`, `digdir-modellkatalog`,
`kartverket-modellkatalog`, `ksdigital-modellkatalog`,
`novari-modellkatalog`, `skatteetaten-modellkatalog`, `ngr-adresse`,
`ngr-eiendom`, `ngr-person`, `ngr-virksomhet`,
`enhetsregisteret-bvrinn`, `lunchregisteret`,
`register-over-aksjeeiere`, `referansemodell`, `samt-bu`.

**Har `Completed` i dag (12 skjema) — skal endrast til `UnderDevelopment`:**
`dcat-ap-no`, `cpsv-ap-no`, `dqv-ap-no`, `dqv-core`, `modelldcat-ap-no`,
`modelldcat-modell`, `skos-ap-no`, `xkos-ap-no`,
`fint-administrasjon`, `fint-arkiv`, `fint-common`, `fint-okonomi`,
`fint-personvern`, `fint-ressurs`, `fint-utdanning`, `fair-metadata`,
`brreg-begrepskatalog`.

(Brukaren har stadfesta at desse skal endrast sjølv om dei implementerer
stabile eksterne standardar (DCAT-AP-NO, FINT, fair-metadata) — status
gjeld modelleringsarbeidet i dette repoet, ikkje standarden sjølv.)

**Manglar `status:` heilt (1 skjema) — legg til:**
`modelldcat-katalog-schema.yaml` har ei `annotations:`-blokk (med
`utgiver`) men ingen `status`-nøkkel.

**Haldt utanfor (referanse-/eksempelskjema, ikkje reelle modellar):**
`referansemodell-bronze`, `referansemodell-silver`,
`referansemodell-gold` — desse illustrerer bronze/silver/gold-policynivå
og har berre `annotations:`-blokker nesta i enkeltslots, ikkje ein
toppnivå `status`-annotasjon. Brukaren har stadfesta at desse skal stå
urørte.

## Steg

1. For kvart av dei 12 skjema med `status: Completed`: endre verdien til
   `http://purl.org/adms/status/UnderDevelopment`.
2. Legg til `status: http://purl.org/adms/status/UnderDevelopment` i
   `annotations:`-blokka i `modelldcat-katalog-schema.yaml`.
3. Køyr `make lint SCHEMA=<skjema>` for kvart endra skjema for å stadfeste
   at endringa ikkje bryt validering.
4. Oppdater denne specen med `## Utført`-seksjon og flytt til
   `specs/done/`.

## Handlingsliste

- [x] `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
- [x] `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`
- [x] `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`
- [x] `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml`
- [x] `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`
- [x] `src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml`
- [x] `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`
- [x] `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`
- [x] `src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml`
- [x] `src/linkml/fint/fint-arkiv/fint-arkiv-schema.yaml`
- [x] `src/linkml/fint/fint-common/fint-common-schema.yaml`
- [x] `src/linkml/fint/fint-okonomi/fint-okonomi-schema.yaml`
- [x] `src/linkml/fint/fint-personvern/fint-personvern-schema.yaml`
- [x] `src/linkml/fint/fint-ressurs/fint-ressurs-schema.yaml`
- [x] `src/linkml/fint/fint-utdanning/fint-utdanning-schema.yaml`
- [x] `src/linkml/fair/fair-metadata/fair-metadata-schema.yaml`
- [x] `src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml`
- [x] `src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml` (la til ny `status`-nøkkel)
- [x] `make lint` for kvart endra skjema
- [x] Flytt spec til `specs/done/` med `## Utført`-seksjon

## Utført

Alle 18 skjema oppdatert: `status` sett til
`http://purl.org/adms/status/UnderDevelopment` i dei 17 skjema som hadde
`Completed`, og lagt til som ny nøkkel i `modelldcat-katalog-schema.yaml`
(hadde ingen `status` frå før). `git diff` stadfesta at kvar endring er
isolert til éi linje (`status:`-verdien), ingen andre felt rørt.

`make lint` køyrt på alle 18 skjema. Ingen nye feil introdusert av
endringa — dei eksisterande åtvaringane (`canonical_prefixes` for
`dct`/`adms`/`odrl`/`cv`/`time`/`skosno`/`uneskos`/`cpsvno`, og
`recommended`-åtvaringar for slots utan `description` i FINT- og
begrepskatalog-skjema) er alle forhandsverande og urelaterte til
status-annotasjonen, verifisert direkte i diff-utdraget over.
`referansemodell-bronze/-silver/-gold` er halde utanfor som avtalt.
