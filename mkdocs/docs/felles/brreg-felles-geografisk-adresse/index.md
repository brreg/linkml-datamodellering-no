# brreg-felles-geografisk-adresse

![Utgiver](https://img.shields.io/badge/utgiver-Brønnøysundregistra-blue)
![Lisens](https://img.shields.io/badge/NLOD-2.0-blue)
![Status](https://img.shields.io/badge/status-Under_utvikling-orange)
![Versjon](https://img.shields.io/badge/versjon-0.1.0-blue)
![Validering](https://img.shields.io/badge/silver-ukjent-lightgrey)
![Endringsdato](https://img.shields.io/badge/endringsdato-2026--09--01-blue)


## Om denne modellen

> Denne sida dokumenterer LinkML-modellen brreg-felles-geografisk-adresse, inkludert klasser, eigenskapar, datatypar, valideringsresultat og genererte artefakter. Informasjonen er generert automatisk frå skjemaet og tilhøyrande byggeproses.

<!--
Felles geografiske adresseklassar utleia frå Brønnøysundregistrene (BR)
sin interne BRReferansemodell_v3. Meint for import frå oreg-domenet sine
enhetsregisteret-*-modellar og andre BR-registermodellar som treng same
adressestruktur — sjå
specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for
bakgrunn og metode.
-->


---

## Kom i gang

> Her finn du døme på korleis du importerer, validerer og brukar modellen i eigne prosjekt.

### Importer i egne LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/brreg-felles-geografisk-adresse-v0.1.0/src/linkml/felles/brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-schema
```

### Valider skjemaet mot silver-policy

```bash
make mcp-linkml-valider-modell SCHEMA=src/linkml/felles/brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-schema.yaml
```

### Valider datafil mot LinkML-skjemaet

```bash
make validate-instance SCHEMA=src/linkml/felles/brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-schema.yaml INSTANCE=mine-data.yaml
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
import no.norge.data.felles.brregfellesgeografiskadresse.GeografiskAdresse;

ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
GeografiskAdresse geografisk_adresse = mapper.readValue(new File("mine-data.yaml"), GeografiskAdresse.class);
```


### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from brreg_felles_geografisk_adresse_model import GeografiskAdresse

geografisk_adresse = yaml_loader.load('mine-data.yaml', target_class=GeografiskAdresse)
```


---

## Modellmetadata {#metadata}

> Modellmetadata viser sentrale metadata for modellen, inkludert versjon, status, lisens, identifikatorar og avhengigheiter. Verdiane er henta direkte frå skjemaet.

| Felt | Verdi |
| --- | --- |
| Name | brreg-felles-geografisk-adresse |
| Title | BRREG felles geografisk adresse |
| Description | Gjenbrukbare geografiske adresseklassar utleia frå Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3 (MagicDraw/XMI), pakken "Adresse" (GeografiskAdresse-hierarkiet), pluss dei adresse-relaterte komplekstypane frå Strukturtypekatalog_v1 (Poststed, Kommune, Fylke, Matrikkelnummer, Adressenummer) som adressehierarkiet er avhengig av. Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på. |
| Schema URI | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| Versjon | 0.1.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](https://data.norge.no/nlod/no/2.0) |
| Utgiver | [https://data.norge.no/organizations/974760673](https://data.norge.no/organizations/974760673) |
| Status | [http://purl.org/adms/status/UnderDevelopment](http://purl.org/adms/status/UnderDevelopment) |
| Endringsdato | 2026-09-01 |
| Utgivelsesdato | 2026-09-01 |
| Imports | `linkml:types`<br>`../brreg-felles-typer/brreg-felles-typer-schema` |


---

## Avhengigheiter (2) {#avhengigheiter}

> Denne modellen importerer og gjenbruker komponentar frå andre skjema. 
> Importerte klasser og eigenskapar kan vere synlege i diagram, valideringsrapportar og andre analysar sjølv om dei ikkje blir lista som lokale element i denne modellen.

Dette skjemaet importerer følgjande skjema (direkte og transitivt):

```
linkml:types  # direkte import
└── brreg-felles-typer-schema  # direkte import
```

*Sjå [Importhierarki](../../arkitektur/importhierarki.md) for oversikt over heile repoet sitt importhierarki.*

*Importerte modeller: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [brreg-felles-typer](../brreg-felles-typer/#datamodell)*


---

## Entity-relationship diagram

> ER-diagrammet viser struktur og relasjonar mellom dei lokale klassane i modellen. Importerte klasser er som standard filtrerte bort for å gjere diagrammet enklare å lese.

[![ER-diagram](diagrams/brreg-felles-geografisk-adresse-filtered.svg)](diagrams/brreg-felles-geografisk-adresse-filtered.svg)

*Diagrammet viser kun lokale klasser. Klikk for å zoome. [Vis fullstendig diagram med importerte klasser](diagrams/brreg-felles-geografisk-adresse.svg).*

---

## Datamodell

> Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette skjemaet.

Kjelde-datamodell i LinkML-format: [`brreg-felles-geografisk-adresse-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/felles/brreg-felles-geografisk-adresse/brreg-felles-geografisk-adresse-schema.yaml)

---

### Classes (11) {#classes}

> Classes viser klasser som er definerte lokalt i brreg-felles-geografisk-adresse modellen. 
> Klasser frå importerte modellar er ikkje inkluderte i teljinga, men kan vere refererte frå lokale klasser og kan inngå i valideringsresultat og diagram.  
> Klasser grupperes i Obligatorisk, Anbefalt, Valgfri og Andre (uklassifisert).

#### Andre (11)

| Class | Description |
| --- | --- |
| [Adressenummer](klasser/adressenummer.md) | Adressenummeret (husnummer og eventuell husbokstav) i ei vegadresse. |
| [Fylke](klasser/fylke.md) | Eit norsk fylke. |
| [GeografiskAdresse](klasser/geografiskadresse.md) | Ei geografisk adresse. Abstrakt basisklasse for dei konkrete adressetypane under. |
| [InternasjonalAdresse](klasser/internasjonaladresse.md) | Ei adresse i eit anna land enn Noreg, i fri form. |
| [Kommune](klasser/kommune.md) | Ein norsk kommune. |
| [Matrikkeladresse](klasser/matrikkeladresse.md) | Ei matrikkeladresse (knytt til eit matrikkelnummer). |
| [Matrikkelnummer](klasser/matrikkelnummer.md) | Eit matrikkelnummer (gårds-, bruks-, feste- og seksjonsnummer). |
| [Postboksadresse](klasser/postboksadresse.md) | Ei postboksadresse. |
| [Poststed](klasser/poststed.md) | Eit poststed knytt til eit postnummer. |
| [Stedsadresse](klasser/stedsadresse.md) | Ei stadfesta adresse utan vegadresse (t.d. i utmark). |
| [Vegadresse](klasser/vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |


---

### Slots (43) {#slots}

> Slots viser **eigenskapar** som er definert i eller brukt av lokale klasser i modellen.  
> Eigenskapar grupperes i "Verdiar" som inneheld data, og "Refransar" som refererer til andre klasser.  
> *Defined in* kolonna angir kildeskjemaet for eigenskapen.
#### Verdiar (38)

| Slot | Description | Defined in |
| --- | --- | --- |
| [adresseidentifikator](klasser/adresseidentifikator.md) | Ein ekstern identifikator for adressa (t.d. frå eit utanlandsk adresseregister). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [adressenavn](klasser/adressenavn.md) | Namnet på vegen/gata/staden. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [adressenummer_tekst](klasser/adressenummer_tekst.md) | Adressenummer som fritekst (for utanlandske adresser med anna format enn norsk husnummer/husbokstav). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [adressetilleggsnavn](klasser/adressetilleggsnavn.md) | Tilleggsnamn til adressa (t.d. stadnamn i tillegg til vegadresse). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [anleggsnavn](klasser/anleggsnavn.md) | Namnet på anlegget/institusjonen postboksen høyrer til. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [boenhet](klasser/boenhet.md) | Bueining/leilegheitsnummer. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [bokstav](klasser/bokstav.md) | Husbokstaven, dersom adressa har ein. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [br_adresse_id](klasser/br_adresse_id.md) | BR sin interne identifikator for adressa. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [bruksenhetsnummer](klasser/bruksenhetsnummer.md) | Bruksenhetsnummer (bustadnummer) i adressa, t.d. "H0101". | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [bruksnummer](klasser/bruksnummer.md) | Bruksnummer i matrikkelen. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [by_eller_stedsnavn](klasser/by_eller_stedsnavn.md) | By- eller stadnamn. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [bygning](klasser/bygning.md) | Bygningsnamn eller -nummer. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [co_navn](klasser/co_navn.md) | C/O-namn (omsorgsperson/-verksemd) knytt til adressa. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [distrikt_eller_bydel](klasser/distrikt_eller_bydel.md) | Distrikt eller bydel. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [etasjenummer](klasser/etasjenummer.md) | Etasjenummer. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [festenummer](klasser/festenummer.md) | Festenummer i matrikkelen (for festetomter). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [fri_adressetekst](klasser/fri_adressetekst.md) | Heile adressa som fritekst, når ho ikkje kan strukturerast i felta over. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [fylkesnavn](klasser/fylkesnavn.md) | Namnet på fylket. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [fylkesnummer](klasser/fylkesnummer.md) | Fylkesnummeret. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [gaardsnummer](klasser/gaardsnummer.md) | Gårdsnummer i matrikkelen. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [id](klasser/id.md) | URI-identifikator for ressursen. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [kommunenavn](klasser/kommunenavn.md) | Namnet på kommunen. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [kommunenummer](klasser/kommunenummer.md) | Kommunenummeret. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [kort_adressenavn](klasser/kort_adressenavn.md) | Forkorta versjon av adressenamnet. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [landkode](klasser/landkode.md) | Landet adressa ligg i. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [matrikkeladresse_id](klasser/matrikkeladresse_id.md) | BR sin interne identifikator for matrikkeladressa. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [navn](klasser/navn.md) | Namnet på ressursen. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [nummer](klasser/nummer.md) | Husnummeret. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [postboks](klasser/postboks.md) | Postboksnummer (utanlandsk format). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [postboksnummer](klasser/postboksnummer.md) | Nummeret på postboksen. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [postkode](klasser/postkode.md) | Utanlandsk postkode (ikkje norsk postnummer). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [postnummer](klasser/postnummer.md) | Postnummeret. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [region](klasser/region.md) | Region, delstat eller provins. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [seksjonsnummer](klasser/seksjonsnummer.md) | Seksjonsnummer i matrikkelen (for seksjonerte eigedomar). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [stedsnavn](klasser/stedsnavn.md) | Namnet på staden (for adresser utan vegadresse). | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [type](klasser/type.md) | Diskriminator for kva slag adresse dette er. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [undernummer](klasser/undernummer.md) | Undernummer for seksjonert eigedom. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [vegadresse_id](klasser/vegadresse_id.md) | BR sin interne identifikator for vegadressa. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |

#### Referansar (5)

| Slot | Description | Defined in |
| --- | --- | --- |
| [adressenummer](klasser/adressenummer.md) | Husnummer og eventuell husbokstav i vegadressa. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [fylke](klasser/fylke.md) | Fylket adressa ligg i. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [kommune](klasser/kommune.md) | Kommunen adressa ligg i. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [matrikkelnummer](klasser/matrikkelnummer.md) | Matrikkelnummeret adressa er knytt til. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |
| [poststed](klasser/poststed.md) | Poststedet adressa høyrer til. | [https://data.norge.no/felles/brreg-felles-geografisk-adresse](https://data.norge.no/felles/brreg-felles-geografisk-adresse) |



---

### Enumerations (0) {#enumerations}

> Enumerations viser kontrollerte **verdiområder** som er definert i eller brukt lokalt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiområdet.


*Ingen enumerations definert lokalt eller brukt i denne modellen.*



---

### Types (11) {#types}

> Types viser primitive **verdiformat** som datoar, URI-ar, språkstrengar og andre grunnleggjande datatypar som er definert i eller brukt i modellen.  
> *Defined in* kolonna angir kildeskjemaet for verdiformatet.

| Type | URI | Description | Defined in |
| --- | --- | --- | --- |
| Bruksenhetsnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Bruksenhetsnummer (bustadnummer) i ei vegadresse, t.d. "H0101". | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Fylkesnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Nummerkode for fylke, jf. SSB sin fylkesinndeling. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Husbokstav | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Husbokstav i ei vegadresse. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Husnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Husnummer i ei vegadresse. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| integer | [xsd:integer](https://www.w3.org/TR/xmlschema11-2/#integer) | An integer | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| Kommunenummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk kommunenummer (4 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Landkode | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Kode for land. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Postboksnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Nummeret på ein postboks. | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| Postnummer | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | Norsk postnummer (4 sifer). | [https://data.norge.no/felles/brreg-felles-typer](https://data.norge.no/felles/brreg-felles-typer) |
| string | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | A character string | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| uriorcurie | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |

*Importerte typer: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [brreg-felles-typer](../brreg-felles-typer/#types)*

---

### Subsets (0) {#subsets}

> Subsets viser **klassifiseringar** av klasser og slots som blir brukt i modellen. For AP-NO-modellar vil dette typisk vere Obligatorisk, Anbefalt og Valgfri.  
> *Defined in* kolonna angir kildeskjemaet for klassifiseringa.

*Ingen subsets definert lokalt eller brukt i denne modellen.*

---

## Genererte artefakter (12) {#generated-artifacts}

> Denne seksjonen listar maskinlesbare artefakt som er genererte frå skjemaet. Artefakta blir brukte til validering, integrasjon, dokumentasjon og kodegenerering.

| Artefakt | Fil |
|----------|-----|
| Modellmanifest ihht Modelldcat-ap-no | [brreg-felles-geografisk-adresse-manifest.yaml](brreg-felles-geografisk-adresse-manifest.yaml) |
| SHACL shapes | [brreg-felles-geografisk-adresse-shapes.ttl](brreg-felles-geografisk-adresse-shapes.ttl) |
| JSON-LD kontekst | [brreg-felles-geografisk-adresse-context.jsonld](brreg-felles-geografisk-adresse-context.jsonld) |
| JSON Schema | [brreg-felles-geografisk-adresse-schema.json](brreg-felles-geografisk-adresse-schema.json) |
| OpenAPI 3.1 | [brreg-felles-geografisk-adresse-openapi.yaml](brreg-felles-geografisk-adresse-openapi.yaml) |
| OWL ontologi | [brreg-felles-geografisk-adresse-ontology.ttl](brreg-felles-geografisk-adresse-ontology.ttl) |
| RDF/Turtle skjema | [brreg-felles-geografisk-adresse-schema.ttl](brreg-felles-geografisk-adresse-schema.ttl) |
| Python-klasser | [brreg-felles-geografisk-adresse-model.py](brreg-felles-geografisk-adresse-model.py) |
| Protobuf-skjema | [brreg-felles-geografisk-adresse-schema.proto](brreg-felles-geografisk-adresse-schema.proto) |
| GraphQL-skjema | [brreg-felles-geografisk-adresse-schema.graphql](brreg-felles-geografisk-adresse-schema.graphql) |
| ER-diagram (Mermaid) | [brreg-felles-geografisk-adresse-erdiagram.md](brreg-felles-geografisk-adresse-erdiagram.md) |
| PlantUML-diagram | [brreg-felles-geografisk-adresse-filtered.svg](diagrams/brreg-felles-geografisk-adresse-filtered.svg) · [brreg-felles-geografisk-adresse-filtered.puml](diagrams/brreg-felles-geografisk-adresse-filtered.puml) · [brreg-felles-geografisk-adresse.puml](diagrams/brreg-felles-geografisk-adresse.puml) (full) |

*Full byggekonfigurasjon: [build.yaml](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/felles/brreg-felles-geografisk-adresse/build.yaml)*

---

## Valideringsresultat

> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.

*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*

---

## Modellanalyse

> Modellanalysen samanliknar dette skjemaet sine lokalt definerte klasse- og slotnavn mot andre skjema i same domene, og flaggar par med høg navnelikskap som eit mogleg duplikat- eller konsolideringssignal.

*Modellanalyse ikkje tilgjengeleg — krev at generate-workflowen har køyrt.*

---

## Kontakt

> Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar.

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)

