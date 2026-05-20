# Forbetringar for nye utviklarar

Målet er å senke terskelen for å kome i gang med LinkML-modellering og artefaktgenerering i dette repoet. Tiltaka er sorterte i prioritert rekkefølgje for implementasjon.

---

## Tiltak 1 — "Kjem i gang"-narrativ i README

### Problem

README inneheld kommandoar men ikkje ein sekvensiell forteljing. Ein ny utviklar veit ikkje kva rekkefølgje ting skjer i, kvifor kvart steg er nødvendig, eller kva resultatet skal sjå ut som.

### Endring

Legg til ein dedikert seksjon **"Første schema på 10 minuttar"** i README som går gjennom:

```
1. Sjekk føresetnader (Podman, WSL2, make)
2. Bygg images éin gong: make linkml-build-docker
3. Lag nytt schema: make new-model NAME=mitt-schema DOMAIN=ngr
4. Rediger src/linkml/ngr/mitt-schema/mitt-schema-schema.yaml
5. Valider: make mcp-validate SCHEMA=... POLICY=bronze
6. Generer artefaktar: make ngr
7. Sjå resultatet: make docs-serve
```

Kvar seksjon har ei kort forklaring på *kvifor* (ikkje berre *kva*). Refererer til COMMANDS.md for fullstendig kommandoreferanse.

### Implementasjon

Oppdater `README.md` med ny seksjon. Flytt eksisterande kommandotabell til etter narrativet.

---

## Tiltak 2 — Annotert referanseskjema

### Problem

Nye utviklarar les eksisterande skjema for å forstå mønsteret, men produksjonsskjema er ikkje skrivne for å vere pedagogiske. Det er uklart *kvifor* `identifier: true`, `inlined_as_list: true`, `class_uri`, `slot_uri` osv. er der.

### Endring

Lag `src/linkml/referanse/referanse-schema.yaml` — eit minimalt, fullstendig schema med inline-kommentarar som forklarer kvar avgjerd:

```yaml
id: https://example.org/referanse
name: referanse-schema
description: Referanseskjema for nye utviklarar — viser alle hovudmønster i bruk

# Importer alltid frå eit AP-NO-profil eller common-ap-no, ikkje frå linkml:types direkte
imports:
  - linkml:types
  - ../../ap-no/common-ap-no/common-ap-no-schema

prefixes:
  linkml: https://w3id.org/linkml/
  ex: https://example.org/

default_prefix: ex
default_range: string

# Containerklassen samlar alle toppnivåobjekt og er inngangspunktet for serialisering
classes:
  Container:
    tree_root: true           # denne klassen er rota ved validering og serialisering
    attributes:
      ting:
        range: Ting
        multivalued: true
        inlined: true
        inlined_as_list: true  # serialiser som liste, ikkje objekt med URI-nøklar

  Ting:
    class_uri: ex:Ting        # eksplisitt RDF-klasse-URI — påkravd av bronze-policy
    slots:
      - id
      - namn

# Alle eigenskapar er globale slots — ikkje attributes inne i klassen
slots:
  id:
    identifier: true          # gjer instansar refererbare via URI i staden for inlining
    range: uriorcurie
    slot_uri: ex:id

  namn:
    slot_uri: ex:namn         # eksplisitt RDF-eigenskaps-URI — påkravd av bronze-policy
    range: string
    required: true

subsets:
  Obligatorisk: {}
  Anbefalt: {}
  Valgfri: {}
```

Legg til tilhøyrande `examples/referanse/referanse-eksempel.yaml`.

Referanseskjemaet skal:
- Vere gyldig mot bronze-policy
- Generere alle artefakttypar utan feil
- Ikkje vere ein del av produksjonsdomenet (ikkje dukke opp i portalen)

### Implementasjon

Ny katalog `src/linkml/referanse/` med schema og eksempel. Legg til referanse til fila i `ny-domenemodell.md`.

---

## Tiltak 3 — Visuell artefaktoversikt i dokumentasjonsportalen

### Problem

Det finst 10 generatorar som produserer ulike artefaktar. Ein ny utviklar forstår ikkje kva `gen-shacl` gir dei eller kvifor dei bryr seg om `gen-owl`. Artefaktane er lista i COMMANDS.md men utan kontekst om brukstilfelle.

### Endring

Legg til ein tabell i `mkdocs/docs/ny-domenemodell.md` (eller eigen side `artefaktar.md`):

| Artefakt | Fil | Brukstilfelle |
|----------|-----|---------------|
| SHACL shapes | `shapes.ttl` | Validering av RDF-data mot skjema i triple stores |
| JSON-LD kontekst | `context.jsonld` | Mapping frå JSON til RDF — brukast saman med API-ar |
| JSON Schema | `schema.json` | Validering av JSON-data i applikasjonar |
| OWL ontologi | `ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy |
| RDF/Turtle skjema | `schema.ttl` | Fullstendig RDF-representasjon av skjemaet |
| Python-klasser | `model.py` | Direkte bruk i Python-applikasjonar via LinkML |
| ER-diagram | `erdiagram.md` | Visuell oversikt over klasser og relasjonar |
| Eksempeldata | `eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon |

Legg til kva domenar som genererer kva (t.d. fint og samt hoppar over `schema.ttl`).

### Implementasjon

Oppdater `mkdocs/docs/ny-domenemodell.md` med artefakttabellen. Alternativt eigen side `mkdocs/docs/artefaktar.md` med lenke frå ny-domenemodell.

---

## Tiltak 4 — `make check-prereqs`

### Problem

Podman, WSL2 og GNU make er føresetnader som ikkje gir hyggelege feilmeldingar om dei manglar eller er feil konfigurerte. Den vanlegaste årsaka til at nye utviklarar gir opp dei første 30 minuttane er kryptiske feilmeldingar frå manglande oppsett.

### Endring

Nytt Makefile-mål `make check-prereqs` som sjekkar:

```
✓ GNU make tilgjengeleg
✓ Podman tilgjengeleg (podman --version)
✓ Podman rootless fungerer (podman run --rm hello-world)
✓ User namespace-mapping er konfigurert (/etc/subuid og /etc/subgid)
✓ WSL2-miljø (berre åtvaring, ikkje blokkering)
✓ Tilstrekkeleg diskplass (> 5 GB ledig)
```

Gir tydelege feilmeldingar med lenke til rettleiing ved problem:

```
✗ Podman rootless fungerer ikkje.
  Prøv: podman system migrate
  Sjå: https://docs.podman.io/en/latest/markdown/podman-system-migrate.1.html
```

Legg til `make check-prereqs` som første steg i README-narrativet.

### Implementasjon

Nytt bash-skript `src/assets/scripts/check-prereqs.bash` kalla frå Makefile-mål `check-prereqs`.

---

## Tiltak 5 — Pre-commit hook for bronze-validering

### Problem

Ein utviklar oppdagar at skjemaet bryt bronze-policy etter eit push til CI — fleire minutt seinare. Feedback-loopen er for lang og gjer at feil akkumulerer over fleire commit.

### Endring

`make new-model` skriv automatisk ein `.git/hooks/pre-commit`-fil i det nye skjemaets katalog som køyrer bronze-validering før kvar commit:

```bash
#!/usr/bin/env bash
# Auto-generert av make new-model
SCHEMA=$(git diff --cached --name-only | grep -E 'src/linkml/.+/.+-schema\.yaml' | head -1)
[ -z "$SCHEMA" ] && exit 0
echo "→ Validerer $SCHEMA mot bronze-policy..."
make mcp-validate SCHEMA="$SCHEMA" POLICY=bronze --no-print-directory
```

Alternativt: ein repo-global pre-commit hook som validerer alle staged schema-filer.

Dokumenter korleis ein installerer hooken i README og `ny-domenemodell.md`.

### Implementasjon

Legg til hook-mal i `src/assets/hooks/pre-commit` og skriv installasjonsinstruksjonar. Oppdater `make new-model` til å tilby å installere hooken.

---

## Samandrag

| # | Tiltak | Innsats | Effekt |
|---|--------|---------|--------|
| 1 | Getting started-narrativ i README | Lav | Høg |
| 2 | Annotert referanseskjema | Medium | Høg |
| 3 | Visuell artefaktoversikt | Lav | Medium |
| 4 | `make check-prereqs` | Medium | Medium |
| 5 | Pre-commit hook | Medium | Medium |
