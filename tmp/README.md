# ./tmp

Her har vi artefakter som ikkje er kjeldekode i prosjektet, men som kan nyttast i make-kommandoar.
T.d. `make json2linkml-generate SCHEMA=/tmp/person.json`.

Dersom ein generert LinkML-modell i ./tmp-katalogen skal arbeidast vidare med og bli ein offisiell modell, må han flytjast til ./src/linkml/..