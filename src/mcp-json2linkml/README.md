# ./src/mcp-json2linkml

Dette er en mcp server for å generere utkast til ny LinkML-schema basert på json-schema. LinkML-schema vil bli lagret til samme katalog som json-schemaet.

## eksempel på bruk

`make json2linkml-generate SCHEMA=./tmp/person.json`

## tilpassinger av generert LinkML skjema

### sette inn riktig URI til begrep i begrepskatalogen

Først må du finne riktig begrep i begrepskatalogen: Gå til https://data.norge.no/concepts og søk etter begrepet du skal modellere.

Dersom du ikkje finn riktig begrep må du sørge for at det blir oppretta. Sjekk ut denne sida for tips om begrepsarbeid: https://confluence.brreg.no/spaces/ENREG/pages/271934467/Arbeidsomr%C3%A5de+begrep

Når du har funne riktig begrep skal du **ikkje bruke URLen til begrepet**, men gå inn på sida som beskriver begrepet og **kopier URIen som ligg under overskrifta Identifikator**.

Du kan teste om URIen returnerer contenttype ld+json slik:

```
curl -v -H "Accept: application/ld+json" \
  "https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/6f790959-a3e0-4b3b-b56b-0715e7180322"
```

Når du har verifisert av URIen fungerer skal du legge den inn i LinkML skjemaet som ein **annotasjons/begrepsidentifikator** på den aktuelle klassen.

```
classes:
  Person:
    description: Ein person.
    class_uri: ex:Person
    annotations:
      begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/6f790959-a3e0-4b3b-b56b-0715e7180322
```
