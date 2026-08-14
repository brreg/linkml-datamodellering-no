# Synkroniser version/endringsdato i schema-filer etter multi-PR-bugen

## Bakgrunn

Jf. samtalen som avdekte dette: «Oppdater schema-versjonar i release-PR»-
steget i `release-please.yml` hadde ein bug (løyst i
`specs/done/fiks-release-please-multi-pr-bug.md`) som gjorde at det berre
prosesserte éin av dei 22 release-PR-ane (#61–#82) som vart merga
2026-08-14. Fiksen var ukommitert då PR-ane faktisk merga, så 20 av 21
andre pakkar (unnateke `cpsv-ap-no`, som var den eine PR-en den gamle,
buggy koden prosesserte) fekk aldri `version:`/`annotations.endringsdato`
i sjølve schema-fila synkronisert med den nye manifest-versjonen, sjølv om
korrekte git-tags/GitHub Releases vart oppretta av release-please sjølv
(styrt direkte av manifestet, uavhengig av vårt custom sync-steg).

`src/linkml/referanse` er eit strukturelt særtilfelle — komponenten sitt
manifest-path peikar til ein katalog utan eiga topplevel `*-schema.yaml`
(dei fire faktiske skjemafilene ligg eitt nivå djupare, i
`referansemodell/`, `referansemodell-bronze/` osv.). Det opphavlege
sync-steget sitt `find "$pkg_path" -maxdepth 1` ville **aldri** ha funne
nokon av dei, uavhengig av multi-PR-buggen — dette er eit separat,
uløyst spørsmål om kva for éin av dei fire skjemafilene (om nokon) som
eigentleg skal representere «referanse»-komponenten sin versjon, og er
difor **halde utanfor** denne fiksen.

## Steg

1. For kvar av dei 20 pakkane med stadfesta avvik (alle unnateke
   `cpsv-ap-no`, som alt var korrekt, og `referanse`, som er halde
   utanfor): oppdater `version:`-feltet i toppnivå-`*-schema.yaml` til å
   matche `.github/release-please-manifest.json`
2. Oppdater `annotations.endringsdato` til dagens dato (2026-08-14),
   same åtferd som det opphavlege sync-steget (`yq eval -i
   ".annotations.endringsdato = \"$TODAY\""`)
3. La `annotations.utgivelsesdato` stå urørt (det opphavlege steget
   set han berre dersom han manglar/er ugyldig — alle 20 hadde alt ein
   gyldig dato)
4. Avgrens redigeringa til header-delen av kvar fil (før `prefixes:`)
   for å ikkje røre djupare, per-slot `endringsdato`/`utgivelsesdato`-
   annotasjonar som finst lenger nede i fleire av skjemaa (t.d.
   `dcat-ap-no-schema.yaml` har fleire slike på slot-nivå)
5. Verifiser at alle 20 filene framleis er gyldig YAML

## Handlingsliste

- [x] Steg 1: version-felt oppdatert i alle 20
- [x] Steg 2: endringsdato oppdatert til 2026-08-14 i alle 20
- [x] Steg 3: utgivelsesdato uendra (stadfesta gyldig i alle 20 frå før)
- [x] Steg 4: redigering avgrensa til header — stadfesta med diff på dcat-ap-no (einaste fila med djupare, nøkkellike annotasjonar)
- [x] Steg 5: YAML-validitet verifisert for alle 20

## Utført

Alle fem steg utført og verifisert. 20 filer endra:
`dcat-ap-no` (2.13.0→2.14.0), `dqv-ap-no` (1.15.0→1.16.0),
`modelldcat-ap-no` (1.10.0→1.15.0), `skos-ap-no` (2.16.0→2.17.0),
`fint-arkiv` (4.5.0→4.6.0), `fint-personvern` (4.5.0→4.6.0),
`fint-common` (4.4.0→4.5.0), `fair-metadata` (1.6.0→1.7.0),
`brreg-begrepskatalog` (1.6.1→1.7.0), `fint-administrasjon` (4.5.1→4.6.0),
`fint-okonomi` (4.5.0→4.6.0), `fint-ressurs` (4.5.0→4.6.0),
`fint-utdanning` (4.5.0→4.6.0), `ngr-adresse` (1.6.0→1.7.0),
`brreg-modellkatalog` (1.5.1→1.6.0), `ngr-eiendom` (1.6.0→1.7.0),
`ngr-virksomhet` (1.6.0→1.7.0), `ngr-person` (1.6.0→1.7.0),
`register-over-aksjeeiere` (1.7.0→1.8.0), `samt-bu` (1.9.0→1.10.0).

`referanse` er medvite halde utanfor (strukturelt særtilfelle, sjå
Bakgrunn) — bør handterast i ein eigen, separat spec.

Brukaren utfører commiten sjølv.
