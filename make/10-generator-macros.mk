# ==============================================================================
# make/10-generator-macros.mk
#
# Generiske generator-makroar for å byggje LinkML-artefakter.
#
# Dei reint linkml-baserte generatorane (merge, jsonld-context, shacl,
# python, json-schema, owl, rdf, proto) batchar no N skjema inn i ÉIN
# podman-kontainar via src/assets/scripts/makefile/batch-generate.py —
# import av linkml/linkml_runtime (~5,4 s) vert då betalt éin gong per
# generator-kall i staden for éin gong per skjema. Filtrering mot
# build.yaml-flagg, ekstra-flagg-override (shacl_flags/owl_flags) og
# timing/logging er implementert i batch-generate.py sjølv (REGISTRY-et
# der er einaste kjelde for kva build.yaml-flagg/suffiks kvar generator
# brukar — spesifiser det IKKJE på nytt her). Sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 1).
#
# gen-doc, gen-erdiagram og gen-plantuml er delt i fleire batcha fasar
# (linkml-generering via batch-generate.py, python-etterhandsaming via
# batch-generate-instances.py, SVG-rendering via batch-render-plantuml.sh)
# — sjå Tiltak 2/3/4 i spec-fila for grunngjeving og enkeltsteg.
#
# gen-xsd køyrer framleis udelt via run-parallel-gen.sh (éin kontainar per
# skjema × 3 verktøy) — berre 1 skjema i heile repoet har xsd: true, så det
# finst ingenting å vinne på å batche (jf. «Ikkje eit tiltak: gen-xsd» i
# spec-fila). `asyncapi validate` (i gen-asyncapi) er av same grunn framleis
# udelt, sjølv om resten av gen-asyncapi/gen-openapi er batcha.
# ==============================================================================

# ---------------------------------------------------------------------------
# Generisk batch-generator-makro — dekkar generatorar utan spesiell
# etterhandsaming (jsonld-context, python, json-schema, proto), brukt av
# både frittståande gen-*-target (make/11-generator-targets.mk) og
# domain_target (make/20-domain-targets.mk)
# ---------------------------------------------------------------------------
# $1=schemas  $2=batch-generate.py generator-namn (jf. REGISTRY der)
define run_gen_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator $(2) -- $(1)
endef

# ---------------------------------------------------------------------------
# LinkML merge-imports (gen-linkml) — reint fail-fast valideringssteg
# (output diskarda), berre eit steg i domain_target-pipelinen, ingen
# frittståande gen-linkml-target finst
# ---------------------------------------------------------------------------
define run_gen_linkml_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator merge -- $(1)
endef

# ---------------------------------------------------------------------------
# SHACL-generering — gata mot build.yaml (shacl: true), per-schema
# shacl_flags-override lesen direkte frå build.yaml
# ---------------------------------------------------------------------------
define run_gen_shacl_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator shacl -- $(1)
endef

# ---------------------------------------------------------------------------
# OWL-generering — gata mot build.yaml (owl: true), per-schema owl_flags-
# override lesen direkte frå build.yaml (elles standardflagga i REGISTRY)
# ---------------------------------------------------------------------------
define run_gen_owl_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator owl -- $(1)
endef

# ---------------------------------------------------------------------------
# RDF-generering — gata mot build.yaml (rdf: true)
# ---------------------------------------------------------------------------
define run_gen_rdf_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator rdf -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-doc (genererer dokumentasjon til katalog i staden for stdout) —
# gata mot build.yaml (docs: true). Heilt batcha (sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md, Tiltak 3+4):
# Fase A batchar `gen-docgen-examples.py` (reint Python), Fase B batchar
# sjølve `gen-doc`-CLI-et (DocGenerator, Click-drive-invokering same
# mønster som dei linkml-baserte generatorane i Tiltak 1 — skriv sjølv til
# katalog via -d, ikkje stdout, jf. GeneratorSpec sin extra_argv_fn/post_fn
# i batch-generate.py). Ingen run-parallel-gen.sh-fase att.
# ---------------------------------------------------------------------------
define run_gen_doc_parallel
@$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator docgen-examples -- $(1)
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator doc -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-erdiagram — gata mot build.yaml (erdiagram: true). Tre fasar (sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md, Tiltak 4):
# Fase A batchar rå-genereringa (linkml, batch-generate.py). Fase A.5 er
# awk-steget (Container-stripping) — køyrer framleis per skjema direkte på
# host (ikkje kontainerisert i dag, difor ingen kontainar-kostnad å
# batche). Fase B batchar python-filteret (batch-generate-instances.py).
# ---------------------------------------------------------------------------
define run_gen_erdiagram_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator erdiagram -- $(1)
@for s in $(1); do \
	domain=$$(echo "$$s" | cut -d/ -f3); \
	name=$$(basename "$$s" -schema.yaml | sed 's/-schema$$//'); \
	raw="$(GEN_DIR)/$$domain/$$name/$$name-erdiagram-raw.md"; \
	[ -f "$$raw" ] || continue; \
	awk -f src/assets/scripts/makefile/filter_container.awk "$$raw" > "$(GEN_DIR)/$$domain/$$name/$$name-erdiagram-unfiltered.md"; \
done
@$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator erdiagram-filter -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-plantuml (genererer PlantUML-diagram med filtrering) — hoppar over
# skjema utan `plantuml: true` i build.yaml, sidan images.json sitt
# required_if_generator_flag: "plantuml" føreset at biletet faktisk ikkje
# vert bruka for slike skjema.
#
# Tre fasar (sjå specs/backlog/effektiviser-generate-workflow-koyretid.md,
# Tiltak 2+4): Fase A batchar rå-.puml-generering (linkml,
# batch-generate.py). Fase B batchar python-filteret, 2 modus per skjema
# (batch-generate-instances.py). Fase C batchar SVG-renderinga for ALLE
# skjema sine .puml-filer til ÉITT podman-kall (PlantUML sitt CLI tek
# fleire filer om gongen).
# ---------------------------------------------------------------------------
define run_gen_plantuml_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator plantuml -- $(1)
@$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator plantuml-filter -- $(1)
@PLANTUML_IMAGE=$(PLANTUML_IMAGE) bash src/assets/scripts/makefile/batch-render-plantuml.sh $(1)
endef

# ---------------------------------------------------------------------------
# gen-xsd (JSON Schema → Avro → XSD via avrotize) — gata mot build.yaml
# (xsd: true), krev at gen-jsonschema alt har køyrt (--check-suffix
# schema.json). Namnerom hentast frå skjemaet sin `id:`-topplevel-nøkkel med
# sed (unngår awk/nøsta-anførselsteikn-problem inni GEN_CMD, som alt er
# enkelt-quota — sjå specs/done/forenkle-make-laget.md).
# ---------------------------------------------------------------------------
define run_gen_xsd_parallel
@podman run --rm \
	-v "$(CURDIR):/work" -w /work \
	-e GEN_DIR=/work/$(GEN_DIR) \
	--entrypoint sh \
	$(AVROTIZE_IMAGE) \
	/work/src/assets/scripts/makefile/batch-gen-xsd.sh $(1)
endef

# ---------------------------------------------------------------------------
# gen-asyncapi (JSON Schema → AsyncAPI YAML → validate) — gata mot
# build.yaml (asyncapi: true), krev gen-jsonschema.
#
# To fasar (sjå specs/backlog/effektiviser-generate-workflow-koyretid.md,
# Tiltak 3): Fase A batchar sjølve genereringa (`gen-asyncapi.py`, reint
# Python) for ALLE skjema til ÉIN kontainar. Fase B (`asyncapi validate`)
# køyrer i eit heilt anna image (Node.js, ASYNCAPI_IMAGE) og er difor IKKJE
# batcha — berre 1 skjema i heile repoet har asyncapi: true i dag, så det
# finst ingenting å vinne på å batche denne delen no (jf. "Ikkje eit
# tiltak: gen-xsd" i same spec for identisk grunngjeving).
# ---------------------------------------------------------------------------
define run_gen_asyncapi_parallel
@$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator asyncapi -- $(1)
@GEN_CMD='run_logged "asyncapi-validate $$domain/$$name" $(ASYNCAPI_RUN) validate /work/$$input' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator asyncapi-validate --flag asyncapi --check-suffix asyncapi.yaml -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-openapi (JSON Schema → OpenAPI YAML → validate) — gata mot
# build.yaml (openapi: true), krev gen-jsonschema. Generering OG validering
# (`openapi-spec-validator`) køyrer begge i python-pytest-biletet, og er
# difor batcha saman for ALLE skjema til ÉIN kontainar (sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md, Tiltak 3) —
# ingen resterande per-skjema-fase her, i motsetnad til gen-asyncapi.
# ---------------------------------------------------------------------------
define run_gen_openapi_parallel
@$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator openapi -- $(1)
endef
