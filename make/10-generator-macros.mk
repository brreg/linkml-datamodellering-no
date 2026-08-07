# ==============================================================================
# make/10-generator-macros.mk
#
# Generiske generator-makroar for å byggje LinkML-artefaktar.
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
# Dei resterande makroane (gen-doc, gen-erdiagram, gen-plantuml, gen-xsd,
# gen-openapi, gen-asyncapi) har etterhandsaming/eksterne verktøy som ikkje
# er reine linkml-Python-API-kall, og nyttar framleis den delte
# xargs-orkestreringa i run-parallel-gen.sh (filtrering mot build.yaml-
# flagg, parallellisering, timing, logging) — sjå spec Tiltak 2/3 for
# vidare batching av desse.
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
# gata mot build.yaml (docs: true)
# ---------------------------------------------------------------------------
define run_gen_doc_parallel
@GEN_CMD='mkdir -p "$$outdir/docgen-examples" "$$outdir/docs" && \
run_logged "gen-docgen-examples $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-docgen-examples.py \
	"$$s" \
	"src/linkml/$$domain/$$name/examples/$$name-eksempel.yaml" \
	"$$outdir/docgen-examples" && \
run_logged "gen-doc $$domain/$$name" $(LINKML_RUN) gen-doc \
	--template-directory src/assets/templates/docgen \
	--no-mergeimports \
	--no-render-imports \
	--no-hierarchical-class-view \
	--diagram-type mermaid_class_diagram \
	--example-directory "$$outdir/docgen-examples" \
	-d "$$outdir/docs" "$$s" && \
sed -i "/Container/d" "$$outdir/docs/index.md"' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator "gen-docgen-examples + gen-doc" --flag docs -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-erdiagram (pipar gjennom awk for å stripa Container-klassar) —
# gata mot build.yaml (erdiagram: true)
# ---------------------------------------------------------------------------
define run_gen_erdiagram_parallel
@GEN_CMD='mkdir -p "$$outdir" && \
$(LINKML_RUN) gen-erdiagram --no-mergeimports "$$s" \
	| awk -f src/assets/scripts/makefile/filter_container.awk \
	> "$$outdir/$$name-erdiagram-unfiltered.md" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py \
	"$$s" \
	"$$outdir/$$name-erdiagram-unfiltered.md" \
	> "$$outdir/$$name-erdiagram.md"' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-erdiagram --flag erdiagram -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-plantuml (genererer PlantUML-diagram med filtrering) — hoppar over
# skjema utan `plantuml: true` i build.yaml, sidan images.json sitt
# required_if_generator_flag: "plantuml" føreset at biletet faktisk ikkje
# vert bruka for slike skjema
# ---------------------------------------------------------------------------
define run_gen_plantuml_parallel
@GEN_CMD='mkdir -p "$$outdir/diagrams" && \
$(LINKML_RUN) gen-plantuml "$$s" > "$$outdir/diagrams/$$name-raw.puml" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py \
	"$$s" "$$outdir/diagrams/$$name-raw.puml" filtered \
	> "$$outdir/diagrams/$$name-filtered.puml" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py \
	"$$s" "$$outdir/diagrams/$$name-raw.puml" full \
	> "$$outdir/diagrams/$$name.puml" && \
podman run --rm -v "$(CURDIR)/$$outdir/diagrams:/data" $(PLANTUML_IMAGE) -tsvg /data/$$name.puml > /dev/null && \
podman run --rm -v "$(CURDIR)/$$outdir/diagrams:/data" $(PLANTUML_IMAGE) -tsvg /data/$$name-filtered.puml > /dev/null' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-plantuml --flag plantuml -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-xsd (JSON Schema → Avro → XSD via avrotize) — gata mot build.yaml
# (xsd: true), krev at gen-jsonschema alt har køyrt (--check-suffix
# schema.json). Namnerom hentast frå skjemaet sin `id:`-topplevel-nøkkel med
# sed (unngår awk/nøsta-anførselsteikn-problem inni GEN_CMD, som alt er
# enkelt-quota — sjå specs/done/forenkle-make-laget.md).
# ---------------------------------------------------------------------------
define run_gen_xsd_parallel
@GEN_CMD='namespace=$$(sed -n "s/^id: *//p" "$$s" | head -1) && \
run_logged "gen-xsd/j2a $$domain/$$name" $(AVROTIZE_RUN) j2a /work/$$input --out /work/$$outdir/$$name.avsc && \
run_logged "gen-xsd/a2x $$domain/$$name" $(AVROTIZE_RUN) a2x /work/$$outdir/$$name.avsc --namespace "$$namespace" --out /work/$$out && \
run_logged "gen-xsd/fix-xsd-dates $$domain/$$name" podman run --rm --entrypoint python3 -v "$(CURDIR):/work" $(AVROTIZE_IMAGE) /work/src/assets/scripts/makefile/fix-xsd-dates.py /work/$$out /work/$$input && \
rm -f "$$outdir/$$name.avsc"' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-xsd --flag xsd --check-suffix schema.json --out-suffix schema.xsd -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-asyncapi (JSON Schema → AsyncAPI YAML → validate) — gata mot
# build.yaml (asyncapi: true), krev gen-jsonschema (--check-suffix schema.json)
# ---------------------------------------------------------------------------
define run_gen_asyncapi_parallel
@GEN_CMD='run_logged "gen-asyncapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "asyncapi-validate $$domain/$$name" $(ASYNCAPI_RUN) validate /work/$$out' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-asyncapi --flag asyncapi --check-suffix schema.json --out-suffix asyncapi.yaml -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-openapi (JSON Schema → OpenAPI YAML → validate) — gata mot
# build.yaml (openapi: true), krev gen-jsonschema (--check-suffix schema.json)
# ---------------------------------------------------------------------------
define run_gen_openapi_parallel
@GEN_CMD='run_logged "gen-openapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "openapi-spec-validator $$domain/$$name" $(PYTHON_RUN) openapi-spec-validator /work/$$out' \
	bash src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-openapi --flag openapi --check-suffix schema.json --out-suffix openapi.yaml -- $(1)
endef
