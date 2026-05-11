 ---                                                                                                                                                                                                 
  Plan: Testar for alle make-targets
                                                                                                                                                                                                      
  Prinsipp                                                  
                                                                                                                                                                                                      
  - Testar køyrer mot eit dedikert minimal-fixture-skjema — ikkje dei ekte skjemaa (for treige, for mykje støy)                                                                                       
  - Strukturert som eit bash-testskript (tests/test_make.sh) — konsistent med eksisterande tests/test_schemas.sh
  - Kvar test er ein funksjon: køyrer kommando, sjekkar output, rapporterer pass/fail med farge                                                                                                       
  - Cleanup via trap — ryddar opp genererte testfiler sjølv om testar feiler                                                                                                                          
                                                                                                                                                                                                      
  ---                                                                                                                                                                                                 
  Steg 1 — Fixture-skjema                                   
                                                                                                                                                                                                      
  src/linkml/test/test-schema/test-schema-schema.yaml — minimalt, sjølvstendig (berre linkml:types), 2–3 klasser med class_uri/slot_uri, ein Container med tree_root: true.
                                                                                                                                                                                                      
  examples/test/test-schema-eksempel.yaml — tilsvarande instansdata, brukt av convert-rdf-testen.                                                                                                     
                                                                                                                                                                                                      
  Fixture-skjemaet vert automatisk inkludert i SCHEMAS-variabelen i Makefile via find.                                                                                                                
                                                            
  ---                                                                                                                                                                                                 
  Steg 2 — Testar per target                                
                                                                                                                                                                                                      
  Alle generator-testar overridar SCHEMAS-variabelen på kommandolinja for å avgrense til fixture-skjemaet.
                                                                                                                                                                                                      
  ┌────────────────┬───────────────────────────────────────┬────────────────────────────┬───────────────────────────────────────────────┐                                                             
  │      Test      │               Kommando                │         Output-fil         │                  Syntaxsjekk                  │                                                             
  ├────────────────┼───────────────────────────────────────┼────────────────────────────┼───────────────────────────────────────────────┤                                                             
  │ validate       │ make validate SCHEMAS=<fixture>        │ —                          │ exit 0                                        │
  ├────────────────┼────────────────────────────────────────┼────────────────────────────┼───────────────────────────────────────────────┤
  │ gen-jsonld     │ make gen-jsonld SCHEMAS=<fixture>      │ test-schema-context.jsonld            │ python3 -m json.tool + @context-nøkkel finst  │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ gen-shacl      │ make gen-shacl SCHEMAS=<fixture>       │ test-schema-shapes.ttl                │ rdflib.Graph().parse() + > 0 tripler          │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ gen-python     │ make gen-python SCHEMAS=<fixture>      │ test-schema-model.py                  │ python3 -m py_compile                         │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ gen-jsonschema │ make gen-jsonschema SCHEMAS=<fixture>  │ test-schema-schema.json               │ python3 -m json.tool + $defs/properties finst │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ gen-owl        │ make gen-owl SCHEMAS=<fixture>         │ test-schema-ontology.ttl              │ rdflib.Graph().parse() + > 0 tripler          │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ gen-rdf        │ make gen-rdf SCHEMAS=<fixture>         │ test-schema-schema.ttl                │ rdflib.Graph().parse() + > 0 tripler          │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ gen-erdiagram  │ make gen-erdiagram SCHEMAS=<fixture>   │ test-schema-erdiagram.md              │ inneheld ```mermaid + erDiagram               │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ docs           │ make docs SCHEMAS=<fixture>            │ docs/*.md                             │ inneheld #-overskrift, ikkje tom              │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ convert-rdf    │ make convert-rdf (berre test-eksempel) │ test-schema-eksempel.ttl              │ rdflib.Graph().parse() + > 0 tripler          │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ publish        │ make publish (etter generator-testar)  │ mkdocs/docs/test/test-schema/index.md │ finst + inneheld #-overskrift                 │
  ├────────────────┼────────────────────────────────────────┼───────────────────────────────────────┼───────────────────────────────────────────────┤                                                 
  │ clean          │ make clean                             │ generated/                            │ katalog er sletta                             │
  └────────────────┴────────────────────────────────────────┴───────────────────────────────────────┴───────────────────────────────────────────────┘                                                 
                                                            
  ---
  Steg 3 — Utelate
                  
  ┌─────────────────────────────────┬──────────────────────────────────────────────────┐
  │             Target              │                      Grunn                       │                                                                                                              
  ├─────────────────────────────────┼──────────────────────────────────────────────────┤
  │ docs-serve                      │ Interaktiv, kan ikkje automatiserast             │                                                                                                              
  ├─────────────────────────────────┼──────────────────────────────────────────────────┤
  │ docs-build / docs-build-fast    │ Deployment-test, ikkje unit-test                 │                                                                                                              
  ├─────────────────────────────────┼──────────────────────────────────────────────────┤                                                                                                              
  │ mcp-*                           │ Dekka av eksisterande tests/test_mcp_server.py   │                                                                                                              
  ├─────────────────────────────────┼──────────────────────────────────────────────────┤                                                                                                              
  │ make <domene> (fint, ngr, osv.) │ For treige; dekka indirekte av generator-testane │
  └─────────────────────────────────┴──────────────────────────────────────────────────┘                                                                                                              
                                                            
  ---                                                                                                                                                                                                 
  Steg 4 — Dependency: rdflib                               
                             
  Alle Turtle-sjekkar treng rdflib. Vi bygger eigen linkml-container som har rdflib installert, slik at alle RDF-sjekkar køyrer i containeren utan lokale dependencies.
                                                                                                                                                                                                      
  ---
  Steg 5 — Integrasjon                                                                                                                                                                                
                                                                                                                                                                                                      
  Legg til kall til tests/test_make.sh i make test-target saman med eksisterande tests/test_schemas.sh.
         