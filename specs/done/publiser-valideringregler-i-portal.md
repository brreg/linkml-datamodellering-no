# Spesifikasjon: Publiser valideringsreglane i portalen

## Bakgrunn

`src/mcp-linkml-validator/README.md` er den fullstendige, brukarretta dokumentasjonen
av validatoren — alle medaljongnivå (bronze/silver/gold), publiseringspolicyer
(felles-begrepskatalog, felles-datakatalog), policyarv og MCP-verktøy.

Dokumentet er per i dag berre synleg for dei som les kjeldefilene i repoet.
Det bør publiserast i portalen under «Rettleiingar» slik at det er søkbart og lenkjebart
saman med dei andre rettleiingane (`ny-domenemodell.md`, `publisering-begrep.md` o.l.).

`policies/README.md` er ei meir teknisk referansefil retta mot dei som vedlikeheld
policyane — ho er ikkje aktuell for portalen.

## Kva som må gjerast

### Tiltak 1 — Synk README.md med faktisk bronze-konfigurasjon

`src/mcp-linkml-validator/README.md` speglar ikkje dei siste endringane i
`bronze.yaml` (tiltak 1-7 i `bronze-policy-metadata-krav.md`).

Desse avvika må rettast i README.md **før** kopiering:

| Felt | README.md viser | Faktisk (bronze.yaml) |
|---|---|---|
| `schema.title` | `warning` | `error` |
| `schema.default_prefix` | ikkje nemnt | `error` (to sjekkar: tilstades + HTTPS-URI) |
| Klassenamn PascalCase | ikkje nemnt | `warning` (`class_names_pascal_case`) |
| Slotnamn snake_case | ikkje nemnt | `warning` (`slot_names_snake_case`, FINT unnteke) |
| `schema.license` | ikkje nemnt | `warning` |

Silver manglar òg dei tre nye annotasjons-sjekkane (`annotations.utgiver`,
`annotations.endringsdato`, `annotations.status`) frå tiltak 11.

### Tiltak 2 — Kopier og tilpass for portalen

Kopier `src/mcp-linkml-validator/README.md` til `mkdocs/docs/valideringregler.md`.

Tilpassingar i kopien:
- Endre relativ lenkje `[policies/felles-begrepskatalog.yaml](policies/felles-begrepskatalog.yaml)` til
  ei passande absolutt GitHub-URL eller fjern lenkja
- Vurder om avsnittet «MCP-verktøy» er relevant for portallesarar — eventuelt
  flytt til slutten som «Teknisk referanse»

`src/mcp-linkml-validator/README.md` skal framleis eksistere uendra (kjeldedokument
for repoet og for Docker-container-konteksten) — `valideringregler.md` er ei kopi.

### Tiltak 3 — Legg til i nav-menyen

I `mkdocs/publish.sh`, i `nav:` → `- Rettleiingar:`-blokka:

```bash
      - Valideringsreglar: valideringregler.md
```

Legg til **etter** `Ny domenemodell` og **før** `Publiser til Felles Begrepskatalog`,
sidan sida handlar om validering generelt (ikkje domenespesifikt):

```yaml
  - Rettleiingar:
      - Ny domenemodell: ny-domenemodell.md
      - Ny begrepskatalog: ny-begrepsmodell.md
      - Modellmanifest: manifest-config.md
      - Valideringsreglar: valideringregler.md        # ← ny
      - Publiser til Felles Begrepskatalog: publisering-begrep.md
      - Publiser til Felles Datakatalog: publisering-modell.md
      - Bruk frå eksternt repo: ekstern-bruk.md
```

Per CLAUDE.md: «Sannkjelda for nav-menyen er `mkdocs/publish.sh`, ikkje `mkdocs.yml`.»

### Tiltak 4 — Legg til lenkje frå `ny-domenemodell.md`

I `mkdocs/docs/ny-domenemodell.md`, i steg 3 (valider undervegs), legg til ei lenkje:

```markdown
Sjå [Valideringsreglar](valideringregler.md) for fullstendig oversikt over
kva som vert sjekka på kvart nivå.
```

## Avhengigheiter

- Tiltak 2 og 3 avheng av tiltak 1 (oppdatert bronze-innhald i README.md)
- Tiltak 4 kan gjerast uavhengig

## Prioritet

Medium — portalsida er nyttig men blokkerer ingenting. Høgaste verdi: brukaren av
`ny-domenemodell.md`-sida kan klikke seg inn og sjå kva bronze faktisk krev utan
å lesa YAML-filer.

## Utført

Utført 2026-06-10.

- **Tiltak 1**: `src/mcp-linkml-validator/README.md` synkronisert med faktisk `bronze.yaml`:
  `schema.title` oppgradert til `error`, `schema.default_prefix` (to sjekkar) lagt til som `error`,
  `schema.license`, `class_names_pascal_case` og `slot_names_snake_case` lagt til som `warning`.
  Silver-seksjonen omstrukturert med livssyklusmetadata-blokk (`annotations.utgiver`,
  `annotations.endringsdato`, `annotations.status`) som `warning` før DCAT-AP-NO-krava.

- **Tiltak 2**: `mkdocs/docs/valideringregler.md` oppretta som tilpassa kopi av README.md.
  Relativ lenkje til `policies/felles-begrepskatalog.yaml` endra til absolutt GitHub-URL.
  «MCP-verktøy»-seksjonen flytta til slutten som «Teknisk referanse — MCP-verktøy».
  Interne lenkjer til `publisering-begrep.md` og `publisering-modell.md` er relative
  (fungerer i mkdocs-kontekst).

- **Tiltak 3**: `mkdocs/publish.sh` — `- Valideringsreglar: valideringregler.md` lagt til
  etter `Modellmanifest: manifest-config.md` i `- Rettleiingar:`-blokka.

- **Tiltak 4**: `mkdocs/docs/ny-domenemodell.md` — lenkjesetning til `valideringregler.md`
  erstatta den tidlegare lenkja til `policies/README.md` på GitHub i steg 3 (valider undervegs).
