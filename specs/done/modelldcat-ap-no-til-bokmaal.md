# Skriv om modelldcat-ap-no-schema.yaml til norsk bokmål

## Bakgrunn

`modelldcat-ap-no-schema.yaml` inneheld ei blanding av nynorske ord, engelske prefiks
og ukorrekte translittereringar. Alle klasse- og slotnamn skal følgje norsk bokmål
etter terminologien i den offisielle spesifikasjonen på
https://github.com/Informasjonsforvaltning/modelldcat-ap-no/tree/develop/docs.

Spesifikasjonen er brukt som fasit for korrekt namngjeving. Der spesifikasjonen oppgir
eit norsk namn som inneheld særnorske bokstavar, vert desse translitterererte etter
regelen i CLAUDE.md (`æ → ae`, `ø → oe`, `å → aa`).

---

## Klassenamn — endringar

| Noverande | Nytt | Årsak |
|---|---|---|
| `Aktor` | `Aktoer` | Feil translittering: `Aktør → Aktoer` (manglar `e`) |
| `Eigenskap` | `Egenskap` | Nynorsk → bokmål; spec: *Egenskap* |
| `RootObjekttype` | `Rotobjekttype` | Engelsk prefiks → bokmål; spec: *Rotobjekttype* |
| `EnkelType` | `Enkeltype` | Feil casing; spec: *Enkeltype* |
| `Sammensetning` | `Komposisjon` | Feil term; spec: *Komposisjon* (`modelldcatno:Composition`) |
| `AlleAv` | `Alle` | Feil term; spec: *Alle* (`modelldcatno:AllOf`) |
| `NoenAv` | `NoenAv` | Allereie korrekt translittering av *Noen av* |
| `Merknad` | `Note` | Feil term; spec: *Note* (`modelldcatno:Note`) |
| `Betingelsesregel` | `Begrensningsregel` | Feil term; spec: *Begrensningsregel* (`modelldcatno:ConstraintRule`) |
| `XEllerY` | `EntenEller` | Feil term; spec: *Enten eller* → `EntenEller` |

**Inga endring:** `KatalogisertRessurs`, `Kontaktopplysning`, `Standard`, `Lisensdokument`,
`Lokasjon`, `Tidsperiode`, `Dokument`, `Modellkatalog`, `Informasjonsmodell`,
`Modellelement`, `Objekttype`, `Datatype`, `Kodeliste`, `Modul`, `Attributt`,
`Assosiasjon`, `Rolle`, `Spesialisering`, `Realisering`, `Abstraksjon`, `Avhengighet`,
`Samling`, `Valg`, `Og`, `Eller`, `Ikke`, `Kodeelement`.

---

## Slotnamn — endringar

### Nynorsk → bokmål / feil term

| Noverande slot | Nytt slot | Årsak | Brukt i klasse(r) |
|---|---|---|---|
| `namn_aktor` | `navn_aktoer` | Nynorsk `namn` → bokmål `navn`; `Aktør → Aktoer` | `Aktoer` |
| `har_eigenskap` | `har_egenskap` | Nynorsk → bokmål; spec: *har egenskap* | `Modellelement` |
| `eigenskapsmerknad` | `egenskapsmerknad` | Nynorsk → bokmål (`eigenskap → egenskap`) | `Note` |
| `skapar` | `produsent` | Nynorsk `skapar` → spec: *produsent* (`dct:creator`) | `Informasjonsmodell` |
| `heimeside` | `hjemmeside` | Nynorsk → bokmål; spec: *hjemmeside* (`foaf:homepage`) | `Modellkatalog`, `Informasjonsmodell` |
| `er_erstatta_av` | `er_erstattet_av` | Nynorsk `erstatta` → bokmål `erstattet` | `Informasjonsmodell` |
| `betinger` | `begrenser` | Feil term; spec: *begrenser* (`modelldcatno:constrains`) | `Begrensningsregel` |
| `betingelsesuttrykk` | `begrensningsuttrykk` | Feil term; spec: *begrensningsuttrykk* (`modelldcatno:constraintExpression`) | `Begrensningsregel` |
| `status` | `modellstatus` | Feil term; spec: *modellstatus* (`adms:status`) | `Informasjonsmodell` |
| `versjonsmerknad` | `versjonsnote` | Feil term; spec: *versjonsnote* (`adms:versionNotes`) | `Informasjonsmodell` |
| `har_format` | `finnes_i_format` | Feil term; spec: *finnes i format* (`dct:hasFormat`) | `Informasjonsmodell` |
| `tidsperiode` (slot) | `gyldighetsperiode` | Feil term; spec: *gyldighetsperiode* (`dct:temporal`) | `Informasjonsmodell` |

### Translittereringsfeil (særnorske bokstavar)

| Noverande slot | Nytt slot | Rett translittering |
|---|---|---|
| `tilhorer_modul` | `tilhoerer_modul` | `tilhører → tilhoerer` (`ø → oe`) |
| `har_leverandor` | `har_leverandoer` | `leverandør → leverandoer` (`ø → oe`) |
| `nokkelord` | `noekkelord` | `nøkkelord → noekkelord` (`ø → oe`) |
| `monster` | `moenster` | `mønster → moenster` (`ø → oe`) |

### Feil term (spec-avvik)

| Noverande slot | Nytt slot | Årsak | Brukt i klasse(r) |
|---|---|---|---|
| `relasjonsegenskapetikett` | `relasjonsegenskapsnavn` | Spec: *relasjonsegenskapsnavn* | `Egenskap` |
| `min_multiplisitet` | `nedre_multiplisitet` | Spec: *nedre multiplisitet* | `Egenskap` |
| `maks_multiplisitet` | `oevre_multiplisitet` | Spec: *øvre multiplisitet → oevre_multiplisitet* | `Egenskap` |
| `danner_symmetri_med` | `utgjor_symmetrisk_relasjon_med` | Spec: *utgjør symmetrisk relasjon med* | `Egenskap` |
| `typedefinisjon_referanse` | `typedefinisjon` | Spec: *typedefinisjon* | `Enkeltype` |
| `fraksjonssifre` | `antall_desimaler` | Spec: *antall desimaler* | `Enkeltype` |
| `maks_eksklusiv` | `maksimum_ikke_inklusivt` | Spec: *maksimum ikke-inklusivt* | `Enkeltype` |
| `maks_inklusiv` | `maksimum_inklusivt` | Spec: *maksimum inklusivt* | `Enkeltype` |
| `min_eksklusiv` | `minimum_ikke_inklusivt` | Spec: *minimum ikke-inklusivt* | `Enkeltype` |
| `min_inklusiv` | `minimum_inklusivt` | Spec: *minimum inklusivt* | `Enkeltype` |
| `min_lengde` | `minimum_lengde` | Spec: *minimum lengde* | `Enkeltype` |
| `totalt_sifre` | `totalt_antall_siffer` | Spec: *totalt antall siffer* | `Enkeltype` |
| `i_skjema` | `i_kodeliste` | Spec: *i kodeliste* (`skos:inScheme`) | `Kodeelement` |
| `notasjon` | `kode` | Spec: *kode* (`skos:notation`) | `Kodeelement` |
| `anbefalt_term` | `anbefalt_kodetekst` | Spec: *anbefalt kodetekst* (`skos:prefLabel`) | `Kodeelement` |
| `topp_begrep_av` | `toppelement_til` | Spec: *toppelement til* (`skos:topConceptOf`) | `Kodeelement` |
| `eksempel_kode` | `eksempel` | Spec: *eksempel* (`skos:example`) | `Kodeelement` |
| `eksklusjonsnotat` | `eksklusjonsmerknad` | Spec: *eksklusjonsmerknad* (`xkos:exclusionNote`) | `Kodeelement` |
| `forrige` | `forrige_kodeelement` | Spec: *forrige kodeelement* (`xkos:previous`) | `Kodeelement` |
| `skjult_term` | `fraradet_kodetekst` | Spec: *frarådet kodetekst → fraradet_kodetekst* | `Kodeelement` |
| `inklusjonsnotat` | `inklusjonsmerknad` | Spec: *inklusjonsmerknad* (`xkos:inclusionNote`) | `Kodeelement` |
| `notat` | `merknad` | Spec: *merknad* (`skos:note`) | `Kodeelement` |
| `neste` | `neste_kodeelement` | Spec: *neste kodeelement* (`xkos:next`) | `Kodeelement` |
| `omfangsnotat` | `omfangsmerknad` | Spec: *omfangsmerknad* (`skos:scopeNote`) | `Kodeelement` |
| `alternativ_term` | `tillatt_kodetekst` | Spec: *tillatt kodetekst* (`skos:altLabel`) | `Kodeelement` |

**Inga endring:** `utgiver`, `kontaktpunkt`, `lisens`, `tema`, `temaer`, `begrep`,
`har_del`, `modell`, `er_del_av`, `er_profil_av`, `erstatter`,
`informasjonsmodellidentifikator`, `inneholder_modellelement`, `har_eigenskap` (vert
`har_egenskap`), `navigerbar`, `sekvensnummer`, `har_type`, `har_datatype`,
`har_enkel_type`, `har_verdi_fra`, `inneholder_objekttype`, `refererer_til`,
`har_objekttype`, `har_generelt_begrep`, `inneholder`, `er_abstraksjon_av`,
`avhengig_av`, `har_noe`, `lengde`, `maks_lengde`, `annoterer`, `startdato`,
`sluttdato`, `dekningsomraade`, `endringsdato`, `utgivelsesdato`, `er_i_samsvar_med`,
`er_profil_av`, `spraak`, `har_versjonsnummer`, `har_referanse`, `identifikator_literal`,
`tilhorer_modul` (vert `tilhoerer_modul`).

---

## Utanfor scope for denne spesifikasjonen

Følgjande slot-namnendringar er lista i tabellen over, men er utelate frå implementasjonen
fordi slotsa er definerte i `common-ap-no-schema.yaml` og brukte av fleire AP-NO-skjema
(dcat-ap-no, cpsv-ap-no, skos-ap-no, xkos-ap-no m.fl.). Namneendring krev ein eigen
breiare cleanup-oppgåve:

| Slot | Ønskt nytt namn | Årsak |
|---|---|---|
| `nokkelord` | `noekkelord` | Translitteringsfeil (`nøkkelord → noekkelord`) |
| `status` | `modellstatus` | Spec-term for `adms:status` i modellkontekst |
| `heimeside` | `hjemmeside` | Nynorsk → bokmål |
| `versjonsmerknad` | `versjonsnote` | Feil spec-term |

---

## Påverknad på nedstrøms skjema

`modelldcat-ap-no` vert per i dag ikkje importert av andre skjema i repoet. Endringsrisikoen
er avgrensa til:

- `src/linkml/modellkatalog/brreg-modellkatalog/` — brukar klassar og slots direkte
- `examples/`-filer under `src/linkml/modellkatalog/` — must oppdaterast med nye slotnamn

Sjekk også at `generated/`-katalogen vert regenerert etter endringa.

---

## Validering etter kvart tiltak

```bash
make lint SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml
make lint SCHEMA=src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml
make validate-instance SCHEMA=src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml \
  INSTANCE=src/linkml/modellkatalog/brreg-modellkatalog/examples/brreg-modellkatalog-eksempel.yaml
```

---

## Prioritert tiltaksliste

| # | Gruppe | Tiltak | Omfang |
|---|---|---|---|
| 1 | Klassenamn | Gi alle 10 klasser nytt namn (sjå tabellen over) | Høg — påverkar `is_a:` og `range:` i heile fila |
| 2 | Slot: nynorsk → bokmål | `namn_aktor`, `har_eigenskap`, `eigenskapsmerknad`, `skapar`, `heimeside`, `er_erstatta_av`, `betinger`, `betingelsesuttrykk`, `status`, `versjonsmerknad`, `har_format`, `tidsperiode`(slot) | Høg |
| 3 | Slot: translittereringsfeil | `tilhorer_modul`, `har_leverandor`, `nokkelord`, `monster` | Medium |
| 4 | Slot: feil spec-term (Egenskap/Enkeltype) | `relasjonsegenskapetikett`, `min_multiplisitet`, `maks_multiplisitet`, `danner_symmetri_med`, `typedefinisjon_referanse`, `fraksjonssifre`, `maks_eksklusiv`, `maks_inklusiv`, `min_eksklusiv`, `min_inklusiv`, `min_lengde`, `totalt_sifre` | Medium |
| 5 | Slot: feil spec-term (Kodeelement) | Alle 14 Kodeelement-slots i tabellen over | Medium |
| 6 | Oppdater `brreg-modellkatalog-schema.yaml` | Juster `range:` og `slots:`-lister etter klasse- og slotrename | Høg — blokkerer validering |
| 7 | Oppdater eksempelfiler | Erstatt gamle slotnamn i alle `.yaml`-eksempel under `modellkatalog/` | Medium |

---

## Utført

Utført 2026-06-10. Alle tiltak i prioritert tiltaksliste er gjennomførte med følgjande avvik:

**Implementert:**
- 9 klassenamn omdøypt i `modelldcat-ap-no-schema.yaml` (sjå klasserenamn-tabell)
- 37 slotnamn omdøypt i `modelldcat-ap-no-schema.yaml` (sjå slotrenamet-tabell)
- `anbefalt_kodetekst`-slotdefinisjonen fantest ikkje i originalen — lagt til ny top-level definisjon med `slot_uri: skos:prefLabel`
- `brreg-modellkatalog-schema.yaml` oppdatert: `range: Egenskap`, `range: Aktoer`, og alle nynorske container-attributtnamn (`eigenskapar → egenskaper`, `objekttypar → objekttyper`, `modellkatalogar → modellkataloger`, `informasjonsmodellar → informasjonsmodeller`, `aktorer → aktoerer`)
- `brreg-modellkatalog-eksempel.yaml` og `brreg-modellkatalog.yaml` oppdatert med `modellkataloger:`, `informasjonsmodeller:`, `aktoerer:`, `navn_aktoer:`
- Instansvalidering passerte utan feil

**Ikkje implementert (sjå «Utanfor scope»-seksjonen):**
- `nokkelord`, `status`, `heimeside`, `versjonsmerknad` — definerte i `common-ap-no-schema.yaml`, brukte av fleire skjema, utsett til eigen cleanup-oppgåve
