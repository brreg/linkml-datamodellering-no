# Legg til endringsdato- og utgiver-badge

## Bakgrunn

`mkdocs/lib/sections/badges.sh` genererer badge-rada øvst i kvar skjemaside
(Versjon, Status, Validering, Lisens). Vurdering av om `annotations.utgiver`
og `annotations.endringsdato` (silver-annotasjonar, jf. CLAUDE.md § Namngjeving
→ Silver-annotasjonar) burde få eigne badges konkluderte med:

- **Endringsdato**: legg til — kompakt dato er nyttig for rask "kor fersk er
  denne modellen"-scanning, same mønster som Versjon/Status/Lisens er allereie
  duplisert mellom badge-rad og Modellmetadata-tabellen.
- **Utgiver**: opphavleg vurdert som "ikkje legg til" fordi verdien er eit
  bart organisasjonsnummer utan namneoppslag (t.d. `991825827`). Revidert:
  organisasjonsnamnet finst allereie i `CODEOWNERS.md` (`name`-feltet per
  org, jf. § Korleis eigarskap fungerer). Utgiver-badgen skal difor slå opp
  namnet ved å matche `annotations.utgiver`-URI-en mot `org_uri`-elementet
  i `CODEOWNERS.md` sin YAML-frontmatter, og vise `name`-verdien i badgen.

Feltet finst berre på skjema med `validation_policy: silver` eller høgare
(26 av 36 genererte skjema per no) — begge badges må difor vere valfrie,
same mønster som `license`-parsinga i same fil.

## Steg

1. Parse `Endringsdato`-rada frå `gendoc_index` i `generate_badges()`
2. Legg til valfri badge-output (berre dersom verdien finst), plassert etter
   Lisens-badgen
3. Verifiser mot eit skjema med og eit utan `endringsdato`-annotasjon
4. Parse `Utgjevar`-rada frå `gendoc_index` for å hente ut org-URI-en
   (`https://data.norge.no/organizations/<orgnr>`)
5. Slå opp `name`-feltet i `CODEOWNERS.md` sin YAML-frontmatter ved å
   matche `org_uri` mot org-URI-en frå steg 4 (gjenbruk parsing-mønsteret
   frå `kontakt.sh`, men match på `org_uri`-likskap i staden for
   `path_patterns`/`catalog_slug`)
6. Legg til valfri Utgiver-badge (berre dersom både utgiver-URI og matchande
   `name` finst), plassert før Endringsdato-badgen
7. Verifiser mot eit skjema med kjend org (t.d. `digdir` → `991825827`) og
   eit utan `annotations.utgiver`

## Handlingsliste

- [x] Oppdater `mkdocs/lib/sections/badges.sh` — Endringsdato-badge
- [x] Verifiser med eksisterande genererte gendoc-indeksar — Endringsdato
- [x] Oppdater `mkdocs/lib/sections/badges.sh` — Utgiver-badge (CODEOWNERS-oppslag)
- [x] Verifiser Utgiver-badge mot kjend org og mot skjema utan utgiver

## Utført

- Lagt til valfri Endringsdato-badge etter Lisens-badgen, same mønster (kun
  vist når verdien finst)
- Verifisert med `dcat-ap-no` (har endringsdato) og `dqv-core` (manglar) —
  siste utelet badgen utan feil
- Oppdaga og fiksa undervegs: shields.io krev at bokstavelege bindestrekar i
  badge-meldinga vert escapa som `--`, elles vert badgen "404 badge not
  found" (verifisert direkte mot img.shields.io). Datoen `2026-08-02` vart
  difor koda til `2026--08--02` før bruk i badge-URL-en.
- Lagt til valfri Utgiver-badge (plassert før Endringsdato-badgen): parsar
  `annotations.utgiver`-URI-en frå gendoc-indeksen, slår opp `name`-feltet i
  `CODEOWNERS.md` sin YAML-frontmatter ved å matche `org_uri`, med mjuk
  fallback (`|| utgiver_navn=""`) dersom python-oppslaget feilar
- Encoding av org-namn til shields.io: mellomrom → `_`, bindestrekar → `--`
  (same escaping-behov som Endringsdato-badgen)
- Verifisert mot `dcat-ap-no` (`991825827` → "Digitaliseringsdirektoratet"),
  `fint-administrasjon` (`985870714` → "Novari IKS", verifisert korrekt
  rendering av mellomrom-encoding direkte mot img.shields.io), og `dqv-core`
  (ingen utgiver-annotasjon → badge utelaten utan feil)
