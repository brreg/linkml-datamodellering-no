# Bug: `SchemaView` kollapsar `https://` til `https:/` når han løyser relative importar i eit versjonslåst URL-importert skjema

**ID:** BUG-15
**Status:** `workaround`
**Komponent:** `linkml-runtime` (`linkml_runtime/utils/schemaview.py::SchemaView.imports_closure`)
**Oppdaga:** 2026-08-13

## Symptom

`make mcp-linkml-valider-modell SCHEMA=<skjema med versjonslåst URL-import>`
feila med ein kryptisk `KeyError: 'result'` (sjå òg feilvisings-fiksen i
`src/mcp-linkml-validator/flatten-and-validate.bash`, som no i staden viser
den reelle feilen). Den reelle feilen frå MCP-serveren var:

```
Uventa feil: Unknown CURIE prefix: https
```

Trigga av eit skjema (t.d. `src/linkml/oreg/blomsterregisteret/blomsterregisteret-schema.yaml`)
som importerer `dcat-ap-no-schema` via ein versjonslåst
`raw.githubusercontent.com`-URL, slik
[mkdocs/docs/arkitektur/importhierarki.md](../mkdocs/docs/arkitektur/importhierarki.md#import-på-tvers-av-domenemodellar)
anbefaler for import mellom domenemodellar.

## Rot-årsak

`SchemaView.imports_closure()` løyser relative importar (`../foo`) i eit
*allereie importert* skjema slik:

```python
if "/" in sn and ":" not in i:
    todo.append(os.path.normpath(str(Path(sn).parent / i)))
```

`sn` er her namnet/nøkkelen på skjemaet som nett vart lasta. Når `sn` er ein
full URL (t.d. `https://raw.githubusercontent.com/.../dcat-ap-no/dcat-ap-no-schema`)
og det importerte skjemaet sjølv har ein relativ import (t.d.
`dcat-ap-no-schema.yaml` sin `../dqv-ap-no/dqv-core-schema`), brukar koden
`pathlib.Path`/`os.path.normpath` — verktøy laga for filsystem-stiar.
`pathlib.Path` kollapsar doble skråstrekar som ikkje står heilt fremst i
strengen, så `Path("https://host/a/b").parent` vert til `"https:/host/a"` —
**éin skråstrek, ikkje to**. Det etterfølgjande CURIE-oppslaget
(`Namespaces.uri_for`) ser ingen `"://"`, tolkar strengen som ein CURIE, og
feilar med `Unknown CURIE prefix: https` fordi `https` ikkje er ein
registrert prefiks.

Feilen slår berre inn når det **importerte** skjemaet sjølv har relative
importar utover `linkml:types` — reine "løv"-skjema (t.d. `ngr-adresse-schema`,
som berre importerer `linkml:types`) er upåverka, som forklarar kvifor
eksempelet i importhierarki.md (`ngr-adresse-schema` via pinna URL) fungerer
i dag. Alle AP-NO-profilar (som `dcat-ap-no-schema`) har derimot fleire nivå
relative importar internt, så **enhver** versjonslåst URL-import av eit
skjema som transitivt importerer ein AP-NO-profil ville treffe same bug.

Stadfesta ved å køyre `linkml_runtime` direkte inne i
`mcp-linkml-validator`-kontaineren mot eit minimalt reproduksjonsskjema —
sjå full traceback og analyse i
`specs/backlog/mcp-validator-feilvising-og-relativ-import-bug.md`.

## Workaround

Monkeypatch av berre den buggy grenen i `imports_closure()` (bruk
`urllib.parse.urljoin` når skjemanamnet inneheld `"://"`, elles uendra
åtferd) — sjå `src/assets/scripts/utils/linkml_relative_import_patch.py`.
Patchen er kalla frå dei fem stadene `SchemaView` vert bygd (direkte eller
transitivt via `linkml.generators.*`) i repoet:

- `src/mcp-linkml-validator/server.py`
- `src/assets/scripts/makefile/batch-linkml-validate.py`
- `src/assets/scripts/makefile/gen-modelldcat-elements.py`
- `src/assets/scripts/makefile/validate-modelldcat.py`
- `src/assets/scripts/makefile/batch-generate.py` (drivar for
  `gen-linkml-merge`/`gen-shacl`/`gen-jsonschema`/`gen-owl`/`gen-docs` m.fl.
  — patchen vart gløymd her i første runde, oppdaga då `make domain-oreg`
  feila i CI for eit skjema med versjonslåst URL-import)

Patchen sjekkar sjølv om kjeldekoden til `imports_closure()` framleis
inneheld den forventa buggy linja før han patchar — dersom `linkml_runtime`
vert oppgradert og metoden er endra, hoppar patchen over seg sjølv og skriv
ei tydeleg åtvaring til stderr i staden for å risikere å bryte noko stille.
Må difor kontrollerast på nytt (og potensielt oppdaterast) ved kvar
`linkml_runtime`-versjonsoppgradering i
`src/assets/containers/Dockerfile.mcp-linkml` (pinna `>=1.11.1,<2.0.0`).

## Løysing

Ingen upstream-fiks venta enno. Feilen bør meldast til
[linkml/linkml-runtime](https://github.com/linkml/linkml-runtime) (`SchemaView.imports_closure`
brukar filsystem-semantikk på URL-baserte skjemanamn i staden for
`urllib.parse.urljoin`) — når/dersom upstream fiksar dette kan
`linkml_relative_import_patch.py` fjernast og kallestadene ryddast opp.
