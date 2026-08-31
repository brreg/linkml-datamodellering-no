# brreg-felles-adresse

## Om denne modellen

> Denne sida dokumenterer LinkML-modellen brreg-felles-adresse, inkludert klasser, eigenskapar, datatypar, valideringsresultat og genererte artefakter. Informasjonen er generert automatisk frå skjemaet og tilhøyrande byggeproses.

<!--
Felles adresseklassar (geografisk og digital adresse) utleia frå
Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3. Meint for
import frå oreg-domenet sine enhetsregisteret-*-modellar og andre
BR-registermodellar som treng same adressestruktur — sjå
specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for
bakgrunn og metode.
-->


---

## Kom i gang

> Her finn du døme på korleis du importerer, validerer og brukar modellen i eigne prosjekt.

### Importer i egne LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/brreg-felles-adresse-v0.1.0/src/linkml/felles/brreg-felles-adresse/brreg-felles-adresse-schema
```

### Valider skjemaet mot silver-policy

```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/felles/brreg-felles-adresse/brreg-felles-adresse-schema.yaml
```

### Valider datafil mot LinkML-skjemaet

```bash
make validate-instance SCHEMA=src/linkml/felles/brreg-felles-adresse/brreg-felles-adresse-schema.yaml INSTANCE=mine-data.yaml
```

### Java-bruk

```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.34</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-yaml</artifactId>
    <version>2.17.2</version>
</dependency>
```

```java
import java.io.File;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import no.norge.data.felles.brregfellesadresse.GeografiskAdresse;

ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
GeografiskAdresse geografisk_adresse = mapper.readValue(new File("mine-data.yaml"), GeografiskAdresse.class);
```


### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from brreg_felles_adresse_model import GeografiskAdresse

geografisk_adresse = yaml_loader.load('mine-data.yaml', target_class=GeografiskAdresse)
```


---

## Avhengigheiter (2) {#avhengigheiter}

> Denne modellen importerer og gjenbruker komponentar frå andre skjema. 
> Importerte klasser og eigenskapar kan vere synlege i diagram, valideringsrapportar og andre analysar sjølv om dei ikkje blir lista som lokale element i denne modellen.

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types
brreg-felles-typer/brreg-felles-typer-schema
```

*Sjå [Importhierarki](../../arkitektur/importhierarki.md) for oversikt over heile repoet sitt importhierarki.*

*Importerte modeller: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [brreg-felles-typer](../brreg-felles-typer/#datamodell)*



## Datamodell

> Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette skjemaet.

Kjelde-datamodell i LinkML-format: [`brreg-felles-adresse-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/felles/brreg-felles-adresse/brreg-felles-adresse-schema.yaml)


---


## Valideringsresultat

> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.

*Siste validering: 2026-08-31T15:17:02.829597+00:00 — v0.1.0 — [policy: silver](../../arkitektur/valideringsregler.md#silver)*

| Status | Feil | Åtvaringar |
|---|---|---|
| ❌ Ikkje godkjent | 1 | 21 |

### Feil (1)

1. **`no_container_class`** — `schema`
   `Ingen tree_root-klasse funnen — kan ikkje sjekke container-klasse-krav`


### Åtvaringar (21)

1. **`all_slots_have_slot_uri`** — `slot:id`
   `Slot 'id' manglar slot_uri — formell RDF-semantikk er ikkje definert`

2. **`all_classes_have_concept_ref`** — `class:GeografiskAdresse`
   `Klasse 'GeografiskAdresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

3. **`all_classes_have_concept_ref`** — `class:Postboksadresse`
   `Klasse 'Postboksadresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

4. **`all_classes_have_concept_ref`** — `class:Stedsadresse`
   `Klasse 'Stedsadresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

5. **`all_classes_have_concept_ref`** — `class:Vegadresse`
   `Klasse 'Vegadresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

6. **`all_classes_have_concept_ref`** — `class:Matrikkeladresse`
   `Klasse 'Matrikkeladresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

7. **`all_classes_have_concept_ref`** — `class:InternasjonalAdresse`
   `Klasse 'InternasjonalAdresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

8. **`all_classes_have_concept_ref`** — `class:DigitalAdresse`
   `Klasse 'DigitalAdresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

9. **`all_classes_have_concept_ref`** — `class:IPAdresse`
   `Klasse 'IPAdresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

10. **`all_classes_have_concept_ref`** — `class:EPostadresse`
   `Klasse 'EPostadresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

11. **`all_classes_have_concept_ref`** — `class:Nettadresse`
   `Klasse 'Nettadresse' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

12. **`all_classes_have_concept_ref`** — `class:Meldingsboks`
   `Klasse 'Meldingsboks' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

13. **`all_classes_have_concept_ref`** — `class:Mobiltelefonnummer`
   `Klasse 'Mobiltelefonnummer' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

14. **`all_classes_have_concept_ref`** — `class:Telefonnummer`
   `Klasse 'Telefonnummer' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

15. **`all_classes_have_concept_ref`** — `class:Poststed`
   `Klasse 'Poststed' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

16. **`all_classes_have_concept_ref`** — `class:Kommune`
   `Klasse 'Kommune' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

17. **`all_classes_have_concept_ref`** — `class:Fylke`
   `Klasse 'Fylke' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

18. **`all_classes_have_concept_ref`** — `class:Matrikkelnummer`
   `Klasse 'Matrikkelnummer' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

19. **`all_classes_have_concept_ref`** — `class:Adressenummer`
   `Klasse 'Adressenummer' manglar annotations.begrepsidentifikator som peikar på begrep i https://concept-catalog.fellesdatakatalog.digdir.no/collections`

20. **`schema_has_annotation_oppdateringsfrekvens`** — `schema`
   `schema.annotations.oppdateringsfrekvens manglar`

21. **`missing_required_import`** — `schema`
   `Skjemaet importerer ikkje 'dqv-ap-no-schema'`


---

## Modellanalyse

> Modellanalysen samanliknar dette skjemaet sine lokalt definerte klasse- og slotnavn mot andre skjema i same domene, og flaggar par med høg navnelikskap som eit mogleg duplikat- eller konsolideringssignal.

*Modellanalyse ikkje tilgjengeleg — krev at generate-workflowen har køyrt.*

---

## Kontakt

> Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar.

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

