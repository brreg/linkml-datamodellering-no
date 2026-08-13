# new-modell: silver-annotasjonar (auto-utleidd) + kontaktpunkt-slot

## Bakgrunn

Brukar ønskjer at `make new-modell` genererer:

1. Ein ny global slot:
   ```yaml
   kontaktpunkt:
     description: Kontaktinformasjon for ressursen.
     slot_uri: dcat:contactPoint
     range: uriorcurie
   ```
2. Ein `annotations:`-blokk rett før `prefixes:`, på forma:
   ```yaml
   annotations:
     utgiver: https://data.norge.no/organizations/<orgnr>
     endringsdato: "<dato>"
     utgivelsesdato: "<dato>"
     status: http://purl.org/adms/status/<status>
   ```

Brukaren sitt opphavlege eksempel brukte konkrete verdiar henta frå eit
eksisterande skjema (`991825827`, `2026-08-02`, `2023-01-01`, `Completed`).
Tre avklaringsspørsmål vart stilte og svara styrer designet under:

| Spørsmål | Svar |
|---|---|
| Skal `utgiver` hardkodast likt for alle domene? | **Nei** — auto-detekter frå `CODEOWNERS.md` sitt `path_patterns → org_uri`-oppslag, same mekanisme som allereie finst for begrepssamlingar (`collect-concepts.py`) |
| Skal `endringsdato`/`utgivelsesdato` vere faste datoar? | **Nei** — begge skal setjast til dagens dato ved genereringstidspunktet |
| Skal `status` vere `Completed`? | **Nei** — `http://purl.org/adms/status/UnderDevelopment` («Under utarbeidelse»), sidan eit ferskt utkast per definisjon ikkje er ferdigstilt |

Grunngjeving for CODEOWNERS-avvisinga: `path_patterns` i `CODEOWNERS.md`
mappar `src/linkml/oreg/**` til BRREG (`974760673`), **ikkje** Digdir
(`991825827`, som brukaren sitt eksempel brukte) — org-nummeret varierer
reelt per domene (stadfesta med grep: `991825827` for `ap-no/**`,
`974760673` for `oreg/**`/`fair/**`/BRREG-modellkatalog, `985870714` for
`fint/**`, `971040238`/`974761076` for ulike NGR-underdomene). Å hardkode
éin verdi ville vore feil for alle domene utanom `ap-no`.

## Nøkkelfunn — mekanismen finst alt, delvis

`src/mcp-linkml-modell-utkast/profiles/silver.yaml` definerer allereie
**nøyaktig** den forma brukaren spurte om:

```yaml
schema_annotations:
  utgiver: "https://data.norge.no/organizations/TODO"
  endringsdato: "TODO"
  utgivelsesdato: "TODO"
  status: "http://purl.org/adms/status/UnderDevelopment"
```

— og `converter.py` set denne inn i skjemaet **allereie i rett posisjon**
(mellom `license` og `prefixes`, sjå `converter.py:291-294`,
`schema["annotations"] = dict(profile_annotations)`, kalla etter
`schema["license"] = ...` og før `schema["prefixes"] = prefixes`).
`status: UnderDevelopment` er alt standardverdien i denne profilen —
stadfesta òg empirisk i `common-ap-no-schema.yaml` sjølv, som brukar same
statusverdi.

**Det som manglar er berre:**
1. `new-modell.sh` ber i dag ikkje om `profile: silver` i sitt
   `generate_linkml`-kall — `server.py` fell difor tilbake på
   `bronze` (`arguments.get("profile", "bronze")`), som ikkje har
   `schema_annotations` i det heile.
2. Silver-profilen sine TODO-placeholder-verdiar (`utgiver`, `endringsdato`,
   `utgivelsesdato`) må **post-prosesserast** til dei faktiske,
   dynamisk utleidde verdiane (org-oppslag + dagens dato) — same mønster
   som `common-ap-no`-import/lisens/PascalCase-transformasjonen som alt
   skjer i `new-modell.sh` sitt python-steg.

## DRY-vurdering — CODEOWNERS-oppslag

`src/assets/scripts/makefile/collect-concepts.py` har alt
`load_codeowners(repo_root)` og `find_owner_org(path, orgs)`
(fnmatch-basert path-matching mot `path_patterns`) — brukt for
begrepssamlingar. Å implementere same logikk ein tredje gong direkte i
`new-modell.sh` sitt python-steg ville krysse DRY-terskelen i `CLAUDE.md`
(«tre eller fleire identiske tilfelle» krev konsolidering).

**Løysing:** ekstraher `load_codeowners()`/`find_owner_org()` til
`src/assets/scripts/utils/codeowners.py` (ny, delt modul — same katalog
som `utils.error_handler`/`utils.yaml_io` som alt vert importerte andre
stader). `collect-concepts.py` refaktorerast til å importere derifrå i
staden for eiga lokal kopi. `new-modell.sh` sitt python-steg importerer
same modul via `sys.path.insert(0, '$REPO_ROOT/src/assets/scripts')`
(same mønster som dei python-baserte make-scripta alt brukar, tilpassa
sidan `python3 -c` ikkje har `__file__` å utleie repo-rota frå — `$REPO_ROOT`
er alt tilgjengeleg som bash-variabel i scriptet).

`generate-modellkatalog.py` sin eigen, annleis-forma `load_codeowners()`
(nøkla på `org_uri`, ingen path-matching — anna bruksområde) er **ikkje**
omfatta av denne konsolideringa, sidan signaturen/formålet skil seg frå
dei to andre.

## Steg

1. **Opprett `src/assets/scripts/utils/codeowners.py`** — flytt
   `load_codeowners(repo_root: Path) -> List[Dict]` og
   `find_owner_org(path: Path, orgs: List[Dict]) -> Optional[Dict]` frå
   `collect-concepts.py` hit, uendra signatur/åtferd.

2. **Refaktorer `collect-concepts.py`** til å importere frå
   `utils.codeowners` i staden for eigne lokale kopiar av dei to
   funksjonane. Verifiser med
   `make new-begrepssamling`-relatert testflyt / eksisterande testar for
   begrepssamling-aggregering at åtferda er uendra.

3. **Legg til `kontaktpunkt`-slot i `converter.py`** — i
   `slots_out`-bygginga (rundt linje 444-451, same stad som `id`), bak eit
   nytt profil-flagg `add_kontaktpunkt_slot` (`gen.get("add_kontaktpunkt_slot", True)`,
   same mønster som `add_id_slot`):
   ```python
   if add_kontaktpunkt:
       slots_out["kontaktpunkt"] = {
           "description": "Kontaktinformasjon for ressursen.",
           "slot_uri":    "dcat:contactPoint",
           "range":       "uriorcurie",
       }
   ```
   Sloten vert **ikkje** lagt til i stub-klassen sin `slots:`-liste (jf.
   avklaringssvar) — berre definert globalt, klar til bruk. Legg til
   `add_kontaktpunkt_slot: true` i `profiles/bronze.yaml` sin
   `generation:`-seksjon for dokumentasjon/kontrollerbarheit, same stad
   som `add_id_slot`.

4. **`new-modell.sh` — be om silver-profil** — legg til
   `'profile': 'silver'` i `generate_linkml`-kallet sine `arguments`
   (rundt linje 44-48, saman med `inputFormat`/`schemaId`/`schemaName`/
   `schemaTitle`).

5. **`new-modell.sh` — post-prosesser annotasjonane** — utvid det
   eksisterande python-transformasjonssteget (der PascalCase-namngjeving,
   `common-ap-no`-import og lisens alt vert sett) til òg å:
   - Importere `utils.codeowners` (sjå steg 1-2) via
     `sys.path.insert(0, '$REPO_ROOT/src/assets/scripts')`.
   - Matche `src/linkml/$DOMAIN/$NAME` mot `path_patterns` i
     `CODEOWNERS.md` via `find_owner_org()`.
   - Ved treff: sett `schema['annotations']['utgiver']` til det matcha
     `org_uri`-et direkte (allereie på forma
     `https://data.norge.no/organizations/<orgnr>`).
   - Ved **ikkje**-treff: behald `TODO`-placeholderen frå silver-profilen
     og skriv ei åtvaring til stderr (jf. «Ingen stille feil»-prinsippet i
     `CLAUDE.md`, same mønster som `get_aggregation_metadata()` sin
     `[WARNING] Kan ikkje finne eigar-org...`).
   - Sett `schema['annotations']['endringsdato']` og
     `schema['annotations']['utgivelsesdato']` til
     `datetime.date.today().isoformat()`.
   - `status` vert **ikkje** endra — silver-profilen sin standardverdi
     (`UnderDevelopment`) er alt rett.

6. **Regenerer og verifiser** — køyr `make new-modell NAME=<test> DOMAIN=oreg`
   (domene med kjend CODEOWNERS-treff, BRREG) og stadfest:
   - `annotations:`-blokka ligg rett før `prefixes:`, med
     `utgiver: https://data.norge.no/organizations/974760673` (BRREG, ikkje
     Digdir), dagens dato på begge datofelt, og
     `status: http://purl.org/adms/status/UnderDevelopment`.
   - `kontaktpunkt`-sloten finst i `slots:`, **ikkje** i stub-klassen sin
     `slots:`-liste.
   - `make mcp-linkml-valider-modell SCHEMA=... POLICY=silver` (no som
     silver-profilen faktisk er brukt) gir `"valid": true`.
   - Test òg med eit domene **utan** CODEOWNERS-treff (t.d. ein oppdikta
     `DOMAIN=nyttdomene`) og stadfest at TODO-placeholderen + åtvaringa
     dukkar opp korrekt.

7. **Oppdater dokumentasjon** — `mkdocs/docs/kom-i-gang/ny-domenemodell.md`
   sitt dokumenterte skjema-eksempel (kring linje 50-97) må utvidast med
   `annotations:`-blokka og `kontaktpunkt`-sloten, og TODO-tabellen må
   nemne det nye auto-utleidde `utgiver`-feltet (inkl. TODO-fallback ved
   manglande CODEOWNERS-treff).

8. **Rydd opp testartefaktar** — fjern alle midlertidige testmodellar frå
   steg 6, `make update-valid-scopes`.

## Handlingsliste

- [x] 1: Opprett `src/assets/scripts/utils/codeowners.py` (ekstrahert frå `collect-concepts.py`)
- [x] 2: Refaktorer `collect-concepts.py` til å importere frå `utils.codeowners`
- [x] 3: `converter.py` — nytt `add_kontaktpunkt_slot`-flagg + `kontaktpunkt`-slot i `slots_out`; `bronze.yaml` oppdatert
- [x] 4: `new-modell.sh` — be om `profile: silver` i `generate_linkml`-kallet
- [x] 5: `new-modell.sh` — post-prosesser `annotations.utgiver` (CODEOWNERS-oppslag) og `endringsdato`/`utgivelsesdato` (dagens dato)
- [x] 6: Regenerer testmodellar (med og utan CODEOWNERS-treff) + verifiser silver-validering
- [x] 7: Oppdater `mkdocs/docs/kom-i-gang/ny-domenemodell.md`
- [x] 8: Rydd opp testartefaktar, `make update-valid-scopes`
- [x] 9: Flytt spec til `specs/done/` med `## Utført`-seksjon

## Utført

**1-2: Delt CODEOWNERS-modul.** Oppretta
`src/assets/scripts/utils/codeowners.py` med `load_codeowners(repo_root)`
og `find_owner_org(path, orgs)`, uendra åtferd frå originalen i
`collect-concepts.py`. `collect-concepts.py` importerer no derifrå
(`from utils.codeowners import load_codeowners, find_owner_org`) i staden
for eigne lokale kopiar — `import re`/`import fnmatch` fjerna som
overflødige. Verifisert funksjonelt med
`make gen-begrepskatalog-instance`: identisk output som før
(`git status` viste ingen diff i den genererte
`brreg-begrepskatalog.yaml`), og korrekt org-deteksjon i logg-utskrifta.

**3: `kontaktpunkt`-slot.** Nytt profil-flagg `add_kontaktpunkt_slot`
(`gen.get(..., True)`, same mønster som `add_id_slot`) i `converter.py`,
lagt til i `slots_out`-bygginga rett etter `id`. **Ikkje** lagt til i
stub-klassen sin `slots:`-liste, per avklaringssvar. `bronze.yaml` sin
`generation:`-seksjon dokumenterer det nye flagget.

**4-5: Silver-profil + dynamisk `annotations`.** `new-modell.sh` sitt
`generate_linkml`-kall ber no om `'profile': 'silver'`. Det eksisterande
python-transformasjonssteget er utvida til å importere
`utils.codeowners` (via `sys.path.insert(0, '$REPO_ROOT/src/assets/scripts')`
— `python3 -c` manglar `__file__`, difor bash-interpolert `$REPO_ROOT` i
staden for `Path(__file__).resolve().parents[...]`-mønsteret andre script
brukar), matchar `src/linkml/$DOMAIN/$NAME` mot `path_patterns`, og set
`annotations.utgiver` til det matcha `org_uri`-et (eller behelder
TODO-placeholderen frå silver-profilen + skriv ei åtvaring til stderr ved
ikkje-treff). `endringsdato`/`utgivelsesdato` vert sett til
`datetime.date.today().isoformat()`. `status` er urørt
(`UnderDevelopment` er alt rett frå silver-profilen).

**Ekstra funn undervegs — «Neste steg» § 4 justert attende til bronze.**
Testa `POLICY=silver` mot ein ferskt scaffolda modell: silver-policy krev
strukturelle DCAT-AP-NO/DQV-AP-NO-klassar i containeren (`Katalog`,
`Datasett`, `Kvalitetsmaal`, `Kvalitetsmaaling` — 4 feil,
`container_missing_required_class`), heilt urelatert til
annotasjons-arbeidet i denne spec-en. `build.yaml` sin
`validation_policy: silver` var alt sett slik **før** denne spec-en (ikkje
noko eg endra), men gjorde at eit ferskt scaffolda utkast aldri kunne
passere silver-validering ut av boksen, sjølv med korrekte annotasjonar —
dette er eit pre-eksisterande gap, ikkje noko denne spec-en løyser.
`new-modell.sh` sitt «Neste steg» § 4 vart difor endra fram og attende
(kortvarig sett til `POLICY=silver`, retta attende til `POLICY=bronze`,
som er det som faktisk passerer reint for eit ferskt utkast). Verdt ei
eiga oppfølging seinare dersom silver-valideringsflyten for ferske utkast
skal bli reelt oppnåeleg.

**6: Verifisering.** To testmodellar:
- `oreg/annotasjonstest` (kjend CODEOWNERS-treff): genererte
  `annotations.utgiver: https://data.norge.no/organizations/974760673`
  (BRREG, korrekt for `oreg/**` — ikkje Digdir-verdien `991825827`
  brukaren opphavleg oppgav som eksempel), dagens dato på begge datofelt,
  `status: UnderDevelopment`. `kontaktpunkt` i `slots:`, ikkje i
  stub-klassen. `make mcp-linkml-valider-modell POLICY=bronze` →
  `"valid": true, errorCount: 0, warningCount: 0`.
- `nyttdomeneutankodeeigar/domenetest` (ukjend domene): korrekt
  `ÅTVARING: fann ingen eigar-organisasjon...`-melding til stderr, og
  `annotations.utgiver: https://data.norge.no/organizations/TODO`
  (uendra TODO-placeholder). Datofelt/status sett som normalt. Bronze
  passerte reint.

Begge testmodellane sletta att, `make update-valid-scopes` køyrd.

**7: Dokumentasjon.** `mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt
`tilskudd-schema.yaml`-eksempel oppdatert med `annotations:`-blokka (rett
før `prefixes:`) og ein `slots: kontaktpunkt`-seksjon, med forklarande
prosa om at `kontaktpunkt` ikkje er auto-kopla til stub-klassen. TODO-
tabellen har tre nye rader for `annotations.utgiver`/`endringsdato`+`utgivelsesdato`/`status`.

**8: Opprydding.** Testmodellane frå steg 6 sletta,
`make update-valid-scopes` køyrd (37 scopes).

**9: Flytting.** Denne fila vert flytta til `specs/done/` som siste steg.
