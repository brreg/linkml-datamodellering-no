# Samla tabell for silver-policy i policies/README.md

## Bakgrunn

`bronze`- og `gold`-overskriftene i `src/mcp-linkml-validator/policies/README.md`
har kvar éin samla tabell med kolonnene `Sjekk | Alvor | Digdir-regel | FAIR`
(gold har i tillegg `Skildring`) som listar alle reglane policynivået evaluerer.

`silver`-overskrifta manglar tilsvarande samla tabell. I staden er reglane
spreidde over fire strukturelt ulike tabellar:

1. **Livssyklusmetadata** (3 rader) — same kolonneformat som bronze/gold
2. **Klasse-slot-krav** — gruppert *per klasse* (éin rad = éin klasse med
   fleire påkravde slots i éi celle), ikkje éin rad per konkret sjekk
3. **Containerklasse-krav** (2 rader) — same kolonneformat som bronze/gold
4. **Instansvalidering (silver)** (2 rader) — heilt anna kolonneformat
   (`Sjekk | Alvor | Kode | Skildring`, ingen Digdir-regel/FAIR), og krev
   instansdata (`INSTANCE=`) i motsetnad til dei andre sjekkane

**Mål:** Slå alle fire saman til éin tabell rett under `### silver`-overskrifta,
med same kolonneformat som gold: `Sjekk | Alvor | Digdir-regel | FAIR | Skildring`.

## Avklarte val (frå brukardialog)

- **Omfang:** Alle fire eksisterande tabellar (inkl. instansvalidering) slåast
  saman til éi tabell — silver skal ikkje ha nokon eigen sub-tabell att.
- **Klasse-slot-krav:** Flatast ut til éin rad per klasse+slot-kombinasjon
  (t.d. «Katalog har `dct:title`»), ikkje éin rad per klasse.
- **Digdir-regel/FAIR for flata klasse-slot-rader:** Kjeldedataet gir i dag
  berre eitt kombinert regelsett *per klasse* (t.d. Katalog: reglar 1, 2, 10 —
  FAIR F2, R1.2), ikkje presist per slot. For å unngå å dikte opp ny
  finkorna mapping utan grunnlag, arvar kvar utflata slot-rad **same
  Digdir-regel/FAIR-verdiar som klassa dei høyrer til** hadde i den opphavlege
  tabellen. Dette bør handsamast som ei forenkling — flagg det gjerne til
  brukaren for gjennomsyn dersom meir presis per-slot-mapping er ønskt seinare.
- **Instansvalideringsrader:** Manglar i dag Digdir-regel/FAIR heilt. Dei
  koplast til regel **8 — Maskinprosserbarheit** / FAIR **I1**, same mapping
  som den tilsvarande skjema-sjekken «Slots med kontrollerte vokabular har
  korrekte annotations» i bronze-tabellen (same underliggande krav — kontrollert
  vokabular — berre evaluert på instansnivå i staden for skjemanivå). Radene
  merkast eksplisitt med at dei krev `INSTANCE=`, sidan dette skil dei frå
  resten av tabellen (som berre treng sjølve skjemaet).
- **Kode-kolonnen** frå den gamle instansvalideringstabellen droppast som eigen
  kolonne (gold-formatet har ikkje Kode-kolonne) — kodenamnet vert i staden
  nemnt i Skildring-teksten (t.d. «Kode: `instance_slot_invalid_vocabulary_pattern`»).

## Relevante filer

- `src/mcp-linkml-validator/policies/README.md` — einaste fila som skal endrast

## Steg

### 1. Erstatt dei fire eksisterande silver-tabellane med éi samla tabell

Erstatt heile innhaldet frå `### silver` (linje 96) til rett før `---` /
`### gold` (linje 145-146) i `src/mcp-linkml-validator/policies/README.md`
med:

```markdown
### silver

Arvar bronse. Legg til livssyklusmetadata og krav frå DCAT-AP-NO og DQV-AP-NO
for domenemodeller i norsk offentleg sektor, samt instanssjekkar for
kontrollerte vokabular.

| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.annotations.utgiver` er URI på forma `https://data.norge.no/organizations/<orgnr>` | warning | 10 — Ansvar | R1.2 | Identifiserer kven som har ansvar for modellen |
| `schema.annotations.endringsdato` er ISO 8601-dato | warning | 9 — Datering | R1.3 | Datering av siste endring |
| `schema.annotations.status` er ADMS Status-URI | warning | 11 — Modellstatus | R1.3 | Eksplisitt livssyklusstatus (`UnderDevelopment`/`Completed`/`Deprecated`/`Withdrawn`) |
| `Katalog` har `dct:title` | error | 1, 2, 10 | F2, R1.2 | Tittel på katalogen |
| `Katalog` har `dct:description` | error | 1, 2, 10 | F2, R1.2 | Skildring av katalogen |
| `Katalog` har `dcat:contactPoint` | error | 1, 2, 10 | F2, R1.2 | Kontaktpunkt for katalogen |
| `Katalog` har `dct:publisher` | error | 1, 2, 10 | F2, R1.2 | Utgjevar av katalogen |
| `Katalogpost` har `dct:modified` | error | 9 | R1.3 | Endringsdato for katalogposten |
| `Katalogpost` har `foaf:primaryTopic` | error | 9 | R1.3 | Kopling til hovudressursen katalogposten skildrar |
| `Datasett` har `dct:title` | error | 1, 2, 10 | F2, R1.2 | Tittel på datasettet |
| `Datasett` har `dct:description` | error | 1, 2, 10 | F2, R1.2 | Skildring av datasettet |
| `Datasett` har `dcat:contactPoint` | error | 1, 2, 10 | F2, R1.2 | Kontaktpunkt for datasettet |
| `Datasett` har `dcat:theme` | error | 1, 2, 10 | F2, R1.2 | Tema/kategori for datasettet (Los) |
| `Datasett` har `dct:publisher` | error | 1, 2, 10 | F2, R1.2 | Utgjevar av datasettet |
| `Distribusjon` har `dcat:accessURL` | error | — | A1 | Tilgangsadresse til distribusjonen |
| `Datatjeneste` har `dcat:endpointURL` | error | 1, 2, 10 | F2, A1, R1.2 | Endepunkt-URL for tenesta |
| `Datatjeneste` har `dcat:contactPoint` | error | 1, 2, 10 | F2, A1, R1.2 | Kontaktpunkt for tenesta |
| `Datatjeneste` har `dct:title` | error | 1, 2, 10 | F2, A1, R1.2 | Tittel på tenesta |
| `Datatjeneste` har `dct:publisher` | error | 1, 2, 10 | F2, A1, R1.2 | Utgjevar av tenesta |
| `Aktør` har `foaf:name` | error | 1 | F2 | Namn på aktøren |
| Containerklassen (`tree_root`) har attributt med range `Katalog`, `Datasett`, `Kvalitetsmaal`, `Kvalitetsmaaling` | error | — | — | Sikrar at hovudklassene i DCAT-AP-NO/DQV-AP-NO er kopla til containeren |
| Containerklassen har attributt med range `Distribusjon`, `Datatjeneste`, `Kvalitetsdimensjon`, `Kvalitetsmerknad` | warning | — | — | Sikrar at støtteklassene er kopla til containeren |
| Instansverdiar for slots med `vokabular_pattern` matchar regex-mønsteret **(krev `INSTANCE=`)** | error/warning/info | 8 — Maskinprosserbarheit | I1 | Kode: `instance_slot_invalid_vocabulary_pattern`. Alvor avheng av `vokabular_krav`: **error** for `skal`, **warning** for `bør`, **info** for `kan` |
| Instansverdiar er frå korrekt vokabular-domene (`gyldige_verdier`) **(krev `INSTANCE=`)** | error/warning | 8 — Maskinprosserbarheit | I1 | Kode: `instance_slot_invalid_vocabulary_domain`. Sjekkar at URI-ar startar med `gyldige_verdier`-domenet |

Gyldige verdiar for `annotations.status`: `http://purl.org/adms/status/UnderDevelopment`, `Completed`, `Deprecated`, `Withdrawn`.

Annotasjonsnøklane svarar til `Informasjonsmodell`-slots i `modelldcat-ap-no-schema.yaml`
(Digdir regel 10 og 8 — Maskinprosserbarheit via ModellDCAT-AP-NO).
`make update-modellkatalog` genererer `Informasjonsmodell`-instansar for modellkatalogen frå desse annotasjonane.

**Døme (instanssjekk):** Dersom `spraak`-slot har `vokabular_krav: skal` og
`vokabular_pattern: "^http://publications\\.europa\\.eu/resource/authority/language/[A-Z]{3}$"`,
så vil verdien `"http://example.com/NOB"` gje **error** (feil domene) og
`"http://publications.europa.eu/resource/authority/language/NORSK"` gje **error**
(feil pattern — skal vere 3-bokstavskode).

---
```

Behald `---`-skiljelinja og `### gold`-overskrifta uendra rett etter.

### 2. Verifiser at ingenting anna i README.md refererer til dei gamle silver-under-overskriftene

Søk etter `Livssyklusmetadata`, `Klasse-slot-krav`, `Containerklasse-krav`,
`Instansvalidering (silver)` andre stader i repoet (t.d. `mkdocs/`-lenkjer
eller andre spec-filer) som peikar på desse som ankertekst/overskrift, og
oppdater eventuelle treff.

### 3. Visuell kontroll

Les gjennom den nye tabellen og stadfest at:
- Alle 24 rader frå dei fire opphavlege tabellane er representerte
- Ingen sjekk gjekk tapt i samanslåinga
- Fotnotane (ADMS-status, annotasjonsnøklar, instanseksempel) er framleis
  til stades rett under tabellen

## Handlingsliste

- [x] Erstatt dei fire silver-tabellane med éi samla tabell (steg 1)
- [x] Søk etter og oppdater eventuelle andre referansar til dei gamle
      underoverskriftene (steg 2)
- [x] Visuell kontroll av at alle 24 rader er korrekt representerte (steg 3)

## Utført

Alle tre steg gjennomførte utan avvik frå planen:

1. Dei fire silver-tabellane erstatta med éi samla tabell (24 rader) i
   `src/mcp-linkml-validator/policies/README.md`, same kolonneformat som gold.
2. Søk etter `Livssyklusmetadata`, `Klasse-slot-krav`, `Containerklasse-krav`,
   `Instansvalidering (silver)` fann ingen levande referansar utanom
   `mkdocs/docs/valideringregler_old.md` — ei orfødd, ikkje-lenka fil (ingen
   treff på filnamnet nokon stad i repoet, ikkje del av `publish.sh`-generering).
   Latt urørt, sidan oppgåva berre gjaldt `policies/README.md`.
3. Visuell kontroll stadfesta at alle 24 rader og alle fotnotar
   (ADMS-status-verdiar, annotasjonsnøkkel-forklaring, instanseksempel) er
   til stades i den nye tabellen.

## Utkast til commit-melding

```
docs(mcp-linkml-validator): slå saman silver-tabellane til éi i policies/README.md
  - src/mcp-linkml-validator/policies/README.md: erstatt fire ulikt formaterte
    silver-tabellar (livssyklus, klasse-slot, container, instans) med éi samla
    tabell i gold-stil format (Sjekk/Alvor/Digdir-regel/FAIR/Skildring)
  - specs/backlog/silver-policy-samla-tabell.md: flytta til specs/done/
```
