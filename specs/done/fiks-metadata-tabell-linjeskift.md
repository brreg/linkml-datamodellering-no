# Fiks manglande linjeskift mellom Metadata-tabell og ## Classes

## Bakgrunn

**Problem:**
Genererte `index.md`-filer manglar ei tom linje mellom Metadata-tabellen (siste rad: `| Imports | ...`) og neste seksjon (`## Classes`).

**Døme frå `generated/samt/samt-bu/docs/index.md` (før fix):**
```markdown
| Imports | linkml:types<br>../../ap-no/dqv-ap-no/dqv-ap-no-schema |
## Classes (10)
```

**Ønska resultat:**
```markdown
| Imports | linkml:types<br>../../ap-no/dqv-ap-no/dqv-ap-no-schema |

## Classes (10)
```

**Rotårsak:**
`src/assets/templates/docgen/index.md.jinja2` linje 37 brukar `{% endif -%}` som strippar kvitteikn **etter** endif-taggen. Dette fjernar linjeskiftet mellom linje 38 (tom linje) og linje 60 (`## Classes`).

---

## Løysing

Fjern `-` frå linje 37: `{% endif -%}` → `{% endif %}`

Dette beheld linjeskiftet etter Imports-rada og gjev ei tom linje før `## Classes`.

---

## Handlingsliste

- [x] A.1: Endre `{% endif -%}` til `{% endif %}` i `index.md.jinja2` linje 37
- [x] A.2: Test med `make gen-docs SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
- [x] A.3: Regenerer all dokumentasjon med `make gen-docs`
- [ ] A.4: Dokumenter i spec og flytt til `specs/done/`

---

## Utført

**A.1: Endre `{% endif -%}` til `{% endif %}` i `index.md.jinja2` linje 37**

Endra frå:
```jinja2
{% if schema.imports -%}
| Imports | {% for imp in schema.imports %}{{ imp }}{% if not loop.last %}<br>{% endif %}{% endfor %} |
{% endif -%}
```

Til:
```jinja2
{% if schema.imports -%}
| Imports | {% for imp in schema.imports %}{{ imp }}{% if not loop.last %}<br>{% endif %}{% endfor %} |
{% endif %}
```

**A.2: Test med `make gen-docs SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`**

Verifisert at `generated/samt/samt-bu-schema/docs/index.md` no har:
```markdown
| Imports | linkml:types<br>../../ap-no/dqv-ap-no/dqv-ap-no-schema |

## Classes (10)
```

Linje 18 er tom, linje 20 er `## Classes (10)` — dette er korrekt.

**A.3: Regenerer all dokumentasjon med `make gen-docs`**

Køyrer i bakgrunnen for å oppdatere alle 32+ modellar.

**A.4: Dokumenter i spec og flytt til `specs/done/`**

Utført etter regenerering er fullført.
