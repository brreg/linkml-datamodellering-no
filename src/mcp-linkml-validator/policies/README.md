# Policyer for mcp-linkml-validator

Sjekkane i bronze-, silver- og gold-policyane realiserer
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(Digitaliseringsdirektoratet, v1.0, juni 2022). Tabellen under viser kva reglar som er dekte
av kva policy, og kva som ikkje er automatisk evaluert.

---

## Digdir-reglar og dekningsgrad

| # | Namn | Kort skildring | Dekt av |
|---|---|---|---|
| 1 | **Forståelighet** | Namn og skildringar er forståelege for målgruppa | Bronze: `title` (error), `description` (warning) |
| 2 | **Meningsfullhet** | Namn speglar innhald og formål | Bronze: `title` (error) |
| 3 | **Navne- og skrivekonvensjoner** | PascalCase for klassar, snake_case/camelCase for eigenskapar | Bronze: `class_names_pascal_case`, `slot_names_snake_case` (warning) |
| 4 | **Identifiserbarhet** | Persistente URI-ar for modell, element og eigenskapar | Bronze: `id`, `default_prefix` (HTTPS-URI) (error); `class_uri`, `slot_uri`, identifikator-slot (warning) |
| 5 | **Visualisering** | Modell tilgjengeleg med god visuell representasjon | *Ikkje evaluert* — ER-diagram vert generert av `make erdiagram`, men ikkje validert |
| 6 | **Modularitet** | Handterleg mengde modellelement per modul | Bronze: `class_count_limit` — warning om skjemaet har fleire enn 50 klasser |
| 7 | **Tilgjengeliggjøring** | Modell fritt tilgjengeleg på nett med open lisens | Bronze: `license` (warning) |
| 8 | **Maskinprosserbarhet** | Modell tilgjengeleg i opne, maskinlesbare format | Bronze: `class_uri`, `slot_uri` (indirekte, via regel 4-sjekken) |
| 9 | **Datering** | Modell er datert med publiserings-, endrings- og gyldigheitsdato | Bronze: `version` (warning); Silver: `annotations.endringsdato` (warning) |
| 10 | **Ansvar** | Eigarskap og innhaldsansvar for modellen er tydeleg | Silver: `annotations.utgiver` (warning) |
| 11 | **Modellstatus** | Modellen har ein eksplisitt status (under utarbeiding, ferdig, forelda …) | Silver: `annotations.status` (warning) |
| 12 | **Sammenhenger mellom modeller** | Samanhengar med andre modellar er skildra | *Ikkje evaluert* — dokumenterast manuelt via `er_profil_av`, `erstatter` o.l. i modellkatalogen |
| 13 | **Begreper** | Modellelement og -eigenskapar er knytte til omgrep | Bronze: `annotations.begrepsidentifikator` på alle klasser (warning) |
| 14 | **Gjenbruk** | Eksisterande modellelement vert gjenbrukt framfor nydefinisjoner | *Ikkje evaluert* — best practice, ikkje maskinelt sjekkbart |
| 15 | **Standardiserte datatyper** | Primitive datatypar er standardiserte (XSD, RDFS) | *Ikkje evaluert* — LinkML arvar XSD-typar via `linkml:types` |

> **Merk:** Regel 5, 6, 12, 14 og 15 let seg ikkje automatisk validere berre frå skjemastruktur.
> Dei vert handterte gjennom verktøy (ER-diagram), konvensjonar (CLAUDE.md) og manuell
> gjennomgang.

---

## To typar validering

Policyfilene her er brukte til to ulike føremål:

**Skjemakvalitet (bronze / silver / gold)**  
Sjekkar at eit LinkML-skjema (`.yaml`-fila i `src/linkml/`) held eit visst
kvalitetsnivå: metadata, namngjeving, URI-ar, begrepsreferansar osv.  
Køyrast med `make mcp-validate SCHEMA=... POLICY=bronze`.

**Publiseringskonformitet (felles-datakatalog / felles-begrepskatalog)**  
Sjekkar at eit skjema er i samsvar med krava til ei bestemt ekstern katalog.
Brukt for skjema der `publish_external: true` i manifest.

---

## Nivå for skjemakvalitet

| Nivå | Krav | Digdir-reglar (Bør tilfredsstille) |
|---|---|---|
| `bronze` | Grunnleggande metadata og modelleringskvalitet (dette repoets baseline) | 1, 2, 3, 4, 6, 7, 8, 13 |
| `silver` | Bronze + AP-NO-konformitet og livssyklusmetadata | 1–4, 7–11, 13 |
| `gold` | Silver + FAIR F1–R1.3: full semantisk interoperabilitet | 1–4, 7–11, 13 + FAIR |

Kvart nivå arvar krava frå nivåa under (`silver` arvar `bronze` osv., via `extends:`).

---

## Bronze-sjekkliste

| Sjekk | Alvor | Digdir-regel |
|---|---|---|
| `schema.id` til stades | error | 4 — Identifiserbarhet |
| `schema.name` til stades | error | 1 — Forståelighet |
| `schema.title` til stades | error | 1 — Forståelighet, 2 — Meningsfullhet |
| `schema.default_prefix` til stades | error | 4 — Identifiserbarhet |
| `schema.default_prefix` er absolutt HTTPS-URI med avsluttande `/` | error | 4 — Identifiserbarhet |
| `schema.id` er HTTP(S)-URI | error | 4 — Identifiserbarhet |
| `schema.description` til stades | warning | 1 — Forståelighet |
| `schema.version` til stades | warning | 9 — Datering |
| `schema.license` til stades | warning | 7 — Tilgjengeliggjøring |
| Skjema har ikkje fleire enn 50 klasser (unntatt `tree_root`) | warning | 6 — Modularitet |
| Alle klassenamn startar med stor bokstav (PascalCase) | warning | 3 — Navne- og skrivekonvensjoner |
| Alle slotnamn er snake_case | warning | 3 — Navne- og skrivekonvensjoner |
| Alle klasser (unntatt `tree_root`) har `class_uri` | warning | 4 — Identifiserbarhet, 8 — Maskinprosserbarhet |
| Alle globale slots har `slot_uri` | warning | 4 — Identifiserbarhet, 8 — Maskinprosserbarhet |
| Alle klasser (unntatt `tree_root`) har identifikator-slot | warning | 4 — Identifiserbarhet |
| Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` | warning | 13 — Begreper |

> FINT-skjema er unntekne frå snake_case-sjekken — dei arvar camelCase frå FINT API-spesifikasjonen.

---

## Silver-sjekkliste (i tillegg til bronze)

| Sjekk | Alvor | Digdir-regel |
|---|---|---|
| DCAT-AP-NO: obligatoriske klasser og slots (`Katalog`, `Datasett`, m.fl.) | error | — |
| DQV-AP-NO: obligatoriske klasser og slots (`Kvalitetsmaal`, `Kvalitetsmaaling`) | error | — |
| `schema.annotations.utgiver` til stades — URI på forma `https://data.norge.no/organizations/<orgnr>` | warning | 10 — Ansvar |
| `schema.annotations.endringsdato` til stades — ISO 8601-dato | warning | 9 — Datering |
| `schema.annotations.status` til stades — ADMS Status-URI | warning | 11 — Modellstatus |


Annotasjonsnøklane svarar til `Informasjonsmodell`-slots i `modelldcat-ap-no-schema.yaml`
(Digdir regel 10 og 8 — Maskinprosserbarhet via ModellDCAT-AP-NO).  
`make update-modellkatalog` genererer `Informasjonsmodell`-instansar for modellkatalogen frå desse annotasjonane.

**Gyldige verdiar for `annotations.status`:**

| Status | URI |
|---|---|
| Under utarbeidelse | `http://purl.org/adms/status/UnderDevelopment` |
| Ferdigstilt | `http://purl.org/adms/status/Completed` |
| Foreldet | `http://purl.org/adms/status/Deprecated` |
| Trukket tilbake | `http://purl.org/adms/status/Withdrawn` |

---

## Skiljet mellom skjema- og datavalidering

| Kva | Verktøy | Policy |
|---|---|---|
| Skjemakvalitet | `make mcp-validate POLICY=bronze/silver/gold` | Policyfilene her |
| Datakvalitet (instansar) | `make validate-instance` | — |
| Publiseringskonformitet | `make mcp-validate POLICY=felles-datakatalog` | `felles-datakatalog.yaml` |

`felles-begrepskatalog.yaml` har i tillegg eit eige `instance_checks:`-felt for
sjekkar som krev faktiske instansdata (gitt via `INSTANCE=` til
`make mcp-validate`), t.d. `utgjevar_er_kjend_org` (kjende utgivar-URI-ar) og
`begrep_har_definisjon_pa_nb_og_nn` (tospråkskravet — sjå
`specs/done/avvik-skos-ap-no.md`, SK5 Forslag A).
