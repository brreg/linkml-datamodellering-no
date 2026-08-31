# brreg-felles-typer

![Utgiver](https://img.shields.io/badge/utgiver-Brønnøysundregistra-blue)
![Lisens](https://img.shields.io/badge/NLOD-2.0-blue)
![Status](https://img.shields.io/badge/status-Under_utvikling-orange)
![Versjon](https://img.shields.io/badge/versjon-0.1.0-blue)
![Validering](https://img.shields.io/badge/bronze-%E2%9C%93_godkjent-green)
![Endringsdato](https://img.shields.io/badge/endringsdato-2026--08--31-blue)


## Om denne modellen

> Denne sida dokumenterer LinkML-modellen brreg-felles-typer, inkludert klasser, eigenskapar, datatypar, valideringsresultat og genererte artefakter. Informasjonen er generert automatisk frå skjemaet og tilhøyrande byggeproses.

<!--
Felles primitivtypar utleia frå Brønnøysundregistrene (BR) sin interne
Løsningstypekatalog_v1. Meint for import frå oreg-domenet sine
enhetsregisteret-*-modellar og andre BR-registermodellar som treng dei
same, gjenbrukbare typane (Organisasjonsnummer, Fødselsnummer, UUID,
Tekst50 m.fl.) — sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md
for bakgrunn og metode.
-->


---

## Kom i gang

> Her finn du døme på korleis du importerer, validerer og brukar modellen i eigne prosjekt.

### Importer i egne LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/brreg-felles-typer-v0.1.0/src/linkml/felles/brreg-felles-typer/brreg-felles-typer-schema
```

### Valider skjemaet mot bronze-policy

```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/felles/brreg-felles-typer/brreg-felles-typer-schema.yaml
```

### Valider datafil mot LinkML-skjemaet

```bash
make validate-instance SCHEMA=src/linkml/felles/brreg-felles-typer/brreg-felles-typer-schema.yaml INSTANCE=mine-data.yaml
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
import no.norge.data.felles.brregfellestyper.Container;

ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
Container container = mapper.readValue(new File("mine-data.yaml"), Container.class);
```


### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from brreg_felles_typer_model import Container

container = yaml_loader.load('mine-data.yaml', target_class=Container)
```


---

## Modellmetadata {#metadata}

> Modellmetadata viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | brreg-felles-typer |
| Title | BRREG felles typer |
| Description | Gjenbrukbare primitivtypar utleia frå Brønnøysundregistrene (BR) sin interne Løsningstypekatalog_v1 (MagicDraw/XMI). Skjemaet er den felles kjelda for typar som elles vart lokalt (og inkonsistent) redefinert i kvart av dei sju enhetsregisteret-*-skjemaa, jf. specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md. Berre denne kjeldekatalogen ("Løsningsmodell"-laget hos BR) er brukt her — BRReferansemodell_v3 sitt eige, arva typelag i Strukturtypekatalog_v1 er eit separat, ikkje-importert lag (sjå nemnde spec, Funn 3). |
| Schema URI | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Versjon | 0.1.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgiver | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-08-31 |
| Utgivelsesdato | 2026-08-31 |
| Imports | `linkml:types` |


---

## Avhengigheiter (1) {#avhengigheiter}

> Denne modellen importerer og gjenbruker komponentar frå andre skjema. 
> Importerte klasser og eigenskapar kan vere synlege i diagram, valideringsrapportar og andre analysar sjølv om dei ikkje blir lista som lokale element i denne modellen.

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types  # direkte import
```

*Sjå [Importhierarki](../../arkitektur/importhierarki.md) for oversikt over heile repoet sitt importhierarki.*

*Importerte modeller: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml)*



## Datamodell

> Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette skjemaet.

Kjelde-datamodell i LinkML-format: [`brreg-felles-typer-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/felles/brreg-felles-typer/brreg-felles-typer-schema.yaml)

---

### Classes (0) {#classes}

> Classes viser klasser som er definerte lokalt i brreg-felles-typer modellen. 
> Klasser frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klasser og kan inngå i valideringsresultat og diagram.  
> Klasser grupperes i Obligatorisk, Anbefalt, Valgfri og Andre (uklassifisert).

---

### Slots (0) {#slots}

> Slots viser **eigenskapar** som er definert i eller brukt av lokale klasser i modellen.  
> Eigenskapar grupperes i "Verdiar" som inneheld data, og "Refransar" som refererer til andre klasser.  
> *Defined in* kolonna angir kildeskjemaet for eigenskapen.


---

### Enumerations (0) {#enumerations}

> Enumerations viser kontrollerte **verdiområder** som er definert i eller brukt lokalt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiområdet.


*Ingen enumerations definert lokalt eller brukt i denne modellen.*



---

### Types (53) {#types}

> Types viser primitive **verdiformat** som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar som er definert i eller brukt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiformatet.

| Type | URI | Description | Defined in |
| --- | --- | --- | --- |
| Aktivitetskode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for ein aktivitetstype i BR sine register. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| AktoerId | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | BR sin interne identifikator for ein aktør (person eller verksemd). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| AnyURI | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | Ein absolutt eller relativ URI (xsd:anyURI). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Base64Binary | [xsd:base64Binary](https://www.w3.org/TR/xmlschema11-2/#base64Binary) | Binærdata base64-koda (xsd:base64Binary). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Beloep | [xsd:decimal](https://www.w3.org/TR/xmlschema11-2/#decimal) | Eit pengebeløp. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Binaerobjekt | [xsd:base64Binary](https://www.w3.org/TR/xmlschema11-2/#base64Binary) | Eit vedlagt binærobjekt (t.d. eit dokument), base64-koda. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| BRAdresseId | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | BR sin interne identifikator for ei adresse. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| BRPersonId | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | BR sin interne identifikator for ein person. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| BrregGYear | [xsd:gYear](https://www.w3.org/TR/xmlschema11-2/#gYear) | Eit årstal (xsd:gYear). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| BrregNonNegativeInteger | [xsd:nonNegativeInteger](https://www.w3.org/TR/xmlschema11-2/#nonNegativeInteger) | Eit heiltal større enn eller lik null (xsd:nonNegativeInteger). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Bruksenhetsnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Bruksenhetsnummer (bustadnummer) i ei vegadresse, t.d. "H0101". | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| DateTime | [xsd:dateTime](https://www.w3.org/TR/xmlschema11-2/#dateTime) | Dato og klokkeslett (xsd:dateTime). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Epostadresse | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Ei e-postadresse. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Foedselsnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk fødselsnummer eller D-nummer (11 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Fylkesnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Nummerkode for fylke, jf. SSB sin fylkesinndeling. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| GYearMonth | [xsd:gYearMonth](https://www.w3.org/TR/xmlschema11-2/#gYearMonth) | Månad og år (xsd:gYearMonth). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| HexBinary | [xsd:hexBinary](https://www.w3.org/TR/xmlschema11-2/#hexBinary) | Binærdata heksadesimalt koda (xsd:hexBinary). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Husbokstav | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Husbokstav i ei vegadresse. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Husnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Husnummer i ei vegadresse. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| InstitusjonellSektorkode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | SSB sin institusjonelle sektorkode for ei verksemd. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Int | [xsd:integer](https://www.w3.org/TR/xmlschema11-2/#integer) | Eit heiltal, opphavleg xsd:int i kjelda. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Kommunenummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk kommunenummer (4 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Kontonummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk bankkontonummer (11 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Landkode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for land. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| LandkodeIsoAlpha3 | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | ISO 3166-1 alpha-3-landkode (t.d. NOR). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Long | [xsd:long](https://www.w3.org/TR/xmlschema11-2/#long) | Eit 64-bits heiltal (xsd:long). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| MappeId | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | BR sin interne identifikator for ei saksmappe. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Naeringskode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode frå SSB sin standard for næringsgruppering (SN2007). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| NasjonaltNummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Telefonnummer utan landkode/prefiks. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| NegativeInteger | [xsd:negativeInteger](https://www.w3.org/TR/xmlschema11-2/#negativeInteger) | Eit heiltal mindre enn null (xsd:negativeInteger). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| NonPositiveInteger | [xsd:nonPositiveInteger](https://www.w3.org/TR/xmlschema11-2/#nonPositiveInteger) | Eit heiltal mindre enn eller lik null (xsd:nonPositiveInteger). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Organisasjonsform | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for organisasjonsform, jf. Einingsregisteret sitt kodeverk. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Organisasjonsnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Organisasjonsnummer for ei norsk verksemd (9 sifer), jf. Einingsregisteret. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| PersonstatusType | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for status på ein person i BR sine register. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| PositiveInteger | [xsd:positiveInteger](https://www.w3.org/TR/xmlschema11-2/#positiveInteger) | Eit heiltal større enn null (xsd:positiveInteger). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Postboksnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Nummeret på ein postboks. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Postnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk postnummer (4 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| PrefiksMedNasjonalKode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Internasjonalt telefonprefiks (landkode), t.d. "+47". | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Saksstatus | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for status på ei sak hos BR. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Short | [xsd:short](https://www.w3.org/TR/xmlschema11-2/#short) | Eit 16-bits heiltal (xsd:short). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Spraakkode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for skriftspråk/målform. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Tekst100 | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Fritekst avgrensa til 100 teikn. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Tekst1000 | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Fritekst avgrensa til 1000 teikn. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Tekst175 | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Fritekst avgrensa til 175 teikn. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Tekst255 | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Fritekst avgrensa til 255 teikn. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Tekst50 | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Fritekst avgrensa til 50 teikn. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Token | [xsd:token](https://www.w3.org/TR/xmlschema11-2/#token) | Ein normalisert tekststreng utan linjeskift/dobbelt mellomrom (xsd:token). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| URI | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | Ein Uniform Resource Identifier. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| URL | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | Ein Uniform Resource Locator (nettadresse). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| UUID | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Ein universelt unik identifikator (UUID/GUID). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Valutakode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | ISO 4217-valutakode. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Virksomhetsnavn | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Namnet på ei verksemd, slik det er registrert i Einingsregisteret. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Virksomhetsstatus | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for status på ei verksemd (t.d. aktiv, konkurs, oppløyst). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |

*Importerte typer: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml)*

---

### Subsets (0) {#subsets}

> Subsets viser **klassifiseringar** av klasser og slots som blir brukt i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.  
> *Defined in* kolonna angir kildeskjemaet for klassifiseringa.

*Ingen subsets definert lokalt eller brukt i denne modellen.*

---

## Genererte artefakter (2) {#generated-artifacts}

> Denne seksjonen listar maskinlesbare artefakt som er genererte frå skjemaet. Artefakta blir brukte til validering, integrasjon, dokumentasjon og kodegenerering.

| Artefakt | Fil |
|----------|-----|
| Modellmanifest ihht Modelldcat-ap-no | [brreg-felles-typer-manifest.yaml](brreg-felles-typer-manifest.yaml) |
| ER-diagram (Mermaid) | [brreg-felles-typer-erdiagram.md](brreg-felles-typer-erdiagram.md) |

*Full byggekonfigurasjon: [build.yaml](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/felles/brreg-felles-typer/build.yaml)*

---


## Valideringsresultat

> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.

*Siste validering: 2026-08-31T15:13:11.836328+00:00 — v0.1.0 — [policy: bronze](../../arkitektur/valideringsregler.md#bronze)*

| Status | Feil | Åtvaringar |
|---|---|---|
| ✅ Godkjent | 0 | 0 |

---

## Modellanalyse

> Modellanalysen samanliknar dette skjemaet sine lokalt definerte klasse- og slotnavn mot andre skjema i same domene, og flaggar par med høg navnelikskap som eit mogleg duplikat- eller konsolideringssignal.

*Modellanalyse ikkje tilgjengeleg — krev at generate-workflowen har køyrt.*

---

## Kontakt

> Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar.

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

