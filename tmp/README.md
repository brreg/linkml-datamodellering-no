# ./tmp

Her har vi artefakter som ikkje er kildekode i prosjektet, men som kan benyttes i make kommandoer.
F.eks `make json2linkml-generate SCHEMA=/tmp/person.json`.

Dersom en generert LinkML modell i ./tmp katalogen skal jobbes med og bli en offieisll modell, må den flyttes til ./src/linkml/..