# Horisontal linje etter description.md

## Bakgrunn

`index.md` for kvar modell har i dag ein horisontal linje (`---`) rett etter badges og før description.md-innhald. Brukaren ønskjer å:

1. Fjerne den horisontale linja som kjem rett etter badges
2. Legge til ein horisontal linje etter description.md-bolken (altså etter `generate_description()`)

Dette forbetrar den visuelle flyten — description.md vert meir integrert med header/badges-seksjonen, mens det kjem ein tydeleg skiljelinje før quickstart/eksempel-seksjonane.

## Tiltak

1. ✅ Fjern `echo "---"` frå slutten av `mkdocs/lib/sections/badges.sh`
2. ✅ Legg til `echo "---"` og `echo ""` i slutten av `mkdocs/lib/sections/description.sh`
3. ✅ Fjern "Hoppar over"-melding for dublett-skjema i `mkdocs/publish.sh` (linje 304)
4. ✅ Fjern `echo "---"` frå starten av `mkdocs/lib/sections/external_reference.sh` (linje 19)
5. Test at endringane fungerer ved å køyre `make docs-publish` og inspisere genererte `index.md`-filer

## Filer som må endrast

- `mkdocs/lib/sections/badges.sh` — fjern `---` på linje 60
- `mkdocs/lib/sections/description.sh` — legg til `---` etter `description_file` vert skrive ut
- `mkdocs/publish.sh` — fjern "Hoppar over"-melding for dublett-skjema (linje 304)
- `mkdocs/lib/sections/external_reference.sh` — fjern `---` på linje 19
