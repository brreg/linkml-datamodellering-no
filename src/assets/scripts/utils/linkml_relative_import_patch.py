#!/usr/bin/env python3
"""Monkeypatch for ein kjend feil i linkml/linkml_runtime sin relative-import-oppløysing.

To UAVHENGIGE stader i linkml/linkml_runtime løyser relative importar
(`../foo`) i eit importert skjema ved å bruke `pathlib.Path`/
`os.path.normpath` på skjemanamnet — verktøy laga for filsystem-stiar. Når
skjemanamnet er ein full URL (t.d. eit versjonslåst
`raw.githubusercontent.com`-import, sjå
mkdocs/docs/arkitektur/importhierarki.md § "Import på tvers av
domenemodellar"), kollapsar `pathlib.Path` doble skråstrekar som ikkje står
heilt fremst i strengen: `Path("https://host/a/b").parent` vert til
`"https:/host/a"` (éin skråstrek). Det etterfølgjande CURIE-oppslaget tolkar
då resultatet som ein CURIE og feilar med `Unknown CURIE prefix: https`.

Feilen slår berre inn når det *importerte* skjemaet sjølv har relative
importar (`../`) — reine skjema som berre importerer `linkml:types` er
upåverka. Sjå fullstendig analyse i
specs/backlog/mcp-validator-feilvising-og-relativ-import-bug.md og
bugs/relativ-import-via-versjonslast-url.md.

Denne patchen overstyrer berre resolusjonssteget for URL-baserte skjemanamn
(bruker `urllib.parse.urljoin`, som korrekt forstår URL-schema/netloc) — all
anna åtferd (lokale filsystem-stiar, CURIE-importar som `linkml:types`) er
uendra kopi av upstream-koden.

Dei to stadene:

1. `linkml_runtime.utils.schemaview.SchemaView.imports_closure()` — brukt av
   generatorar som byggjer på `SchemaView` direkte
   (owlgen/shaclgen/jsonschemagen/docgen/linkmlgen, samt
   mcp-linkml-validator).
2. `linkml.utils.mergeutils.resolve_merged_imports()` — brukt av den eldre
   `SchemaLoader`-baserte generator-familien
   (pythongen/protogen/rdfgen/graphqlgen/plantumlgen/jsonldcontextgen, jf.
   `uses_schemaloader = True` på desse generatorklassane). Same buggy
   mønster (`Path(imported_from).parent / imp`), men i eit heilt anna modul
   — ikkje dekt av fiksen i (1), oppdaga då `make domain-oreg` framleis
   feila for pythongen/protogen/rdfgen/graphqlgen/plantumlgen/
   jsonldcontextgen etter at (1) var patcha i `batch-generate.py`.

MERK: bind seg til den interne implementasjonen i
linkml==1.11.1 / linkml_runtime>=1.11.1,<2.0.0 (pinna i
src/assets/containers/Dockerfile.linkml / Dockerfile.mcp-linkml). Må
verifiserast på nytt ved oppgradering — sjå `_EXPECTED_SOURCE_MARKER_*` under.
"""

import sys
from functools import lru_cache
from urllib.parse import urljoin

# Ein bit av den originale, buggy koden i SchemaView.imports_closure() —
# dersom denne ikkje lenger finst i den installerte linkml_runtime-
# versjonen betyr det at upstream har endra funksjonen, og patchen må
# kontrollerast på nytt før han vert brukt.
_EXPECTED_SOURCE_MARKER_SCHEMAVIEW = "todo.append(os.path.normpath(str(Path(sn).parent / i)))"

# Tilsvarande for linkml.utils.mergeutils.resolve_merged_imports().
_EXPECTED_SOURCE_MARKER_MERGEUTILS = "resolved_imp = os.path.normpath(str(Path(imported_from).parent / Path(imp)))"

_patched = False


def _apply_schemaview_patch() -> None:
    import inspect

    from linkml_runtime.utils import schemaview as sv_mod

    original_source = inspect.getsource(sv_mod.SchemaView.imports_closure)
    if _EXPECTED_SOURCE_MARKER_SCHEMAVIEW not in original_source:
        print(
            "ÅTVARING: linkml_relative_import_patch hoppar over patching av "
            "SchemaView.imports_closure() — kjeldekoden har endra seg sidan "
            "patchen vart skriven. Versjonslåste (raw.githubusercontent.com) "
            "importar av skjema med fleire nivå relative importar kan feile "
            "med 'Unknown CURIE prefix'. Sjå "
            "src/assets/scripts/utils/linkml_relative_import_patch.py.",
            file=sys.stderr,
        )
        return

    @lru_cache(None)
    def patched_imports_closure(self, imports=True, traverse=None, inject_metadata=True):
        if self.schema_map is None:
            self.schema_map = {self.schema.name: self.schema}

        closure = sv_mod.deque()
        visited = set()
        todo = [self.schema.name]

        if traverse is not None:
            sv_mod.warnings.warn(
                "traverse behaves identically to imports and will be removed in a future version. "
                "Use imports instead.",
                DeprecationWarning,
            )

        if not imports or (not traverse and traverse is not None):
            return todo

        while len(todo) > 0:
            sn = todo.pop()
            if sn not in self.schema_map:
                self.schema_map[sn] = self.load_import(sn)

            if sn not in visited:
                for i in self.schema_map[sn].imports:
                    if i == sn:
                        continue

                    if "://" in sn and ":" not in i:
                        # URL-basert skjemanamn — bruk urljoin (forstår
                        # URL-schema/netloc korrekt) i staden for
                        # pathlib/os.path (som kollapsar "//").
                        todo.append(urljoin(sn, i))
                    elif "/" in sn and ":" not in i:
                        if sv_mod.WINDOWS:
                            todo.append(
                                sv_mod.PurePath(sv_mod.os.path.normpath(sv_mod.PurePath(sn).parent / i)).as_posix()
                            )
                        else:
                            todo.append(sv_mod.os.path.normpath(str(sv_mod.Path(sn).parent / i)))
                    else:
                        todo.append(i)

            closure.appendleft(sn)
            visited.add(sn)

        closure = list(dict.fromkeys(closure).keys())

        if inject_metadata:
            for s in self.schema_map.values():
                elements: list = []
                elements.extend(s.classes.values())
                elements.extend(s.enums.values())
                elements.extend(s.slots.values())
                elements.extend(s.subsets.values())
                elements.extend(s.types.values())

                for x in elements:
                    x.from_schema = s.id
                for c in s.classes.values():
                    for a in c.attributes.values():
                        a.from_schema = s.id
        return closure

    sv_mod.SchemaView.imports_closure = patched_imports_closure


def _apply_mergeutils_patch() -> None:
    import inspect
    import os
    from pathlib import Path

    from linkml.utils import mergeutils as mu_mod

    original_source = inspect.getsource(mu_mod.resolve_merged_imports)
    if _EXPECTED_SOURCE_MARKER_MERGEUTILS not in original_source:
        print(
            "ÅTVARING: linkml_relative_import_patch hoppar over patching av "
            "mergeutils.resolve_merged_imports() — kjeldekoden har endra seg "
            "sidan patchen vart skriven. Versjonslåste "
            "(raw.githubusercontent.com) importar av skjema med fleire nivå "
            "relative importar kan feile med 'Unknown CURIE prefix' for "
            "SchemaLoader-baserte generatorar (python/proto/rdf/graphql/"
            "plantuml/jsonld-context). Sjå "
            "src/assets/scripts/utils/linkml_relative_import_patch.py.",
            file=sys.stderr,
        )
        return

    def patched_resolve_merged_imports(target, mergee, imported_from=None) -> None:
        for imp in mergee.imports:
            if imp is None:
                continue

            if imp in target.imports:
                continue

            elif mu_mod.urlparse(imp).scheme:
                target.imports.append(imp)
                continue

            elif Path(imp).is_absolute():
                target.imports.append(imp)
                continue

            elif imp.startswith("."):
                if imported_from is None:
                    mu_mod.logger.warning(f"Cannot resolve relative import: {imp}")
                    target.imports.append(imp)
                elif "://" in imported_from:
                    # URL-basert skjemanamn — bruk urljoin (forstår
                    # URL-schema/netloc korrekt) i staden for
                    # pathlib/os.path (som kollapsar "//").
                    target.imports.append(urljoin(imported_from, imp))
                else:
                    resolved_imp = os.path.normpath(str(Path(imported_from).parent / Path(imp)))
                    target.imports.append(resolved_imp)

            else:
                target.imports.append(imp)

    mu_mod.resolve_merged_imports = patched_resolve_merged_imports


def apply() -> None:
    """Installer begge patchane. Trygt å kalle fleire gonger (idempotent)."""
    global _patched
    if _patched:
        return

    _apply_schemaview_patch()
    _apply_mergeutils_patch()
    _patched = True
