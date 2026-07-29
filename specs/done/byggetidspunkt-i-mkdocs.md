# Vis byggetidspunkt i mkdocs-portalen

## Bakgrunn

Brukarar av dokumentasjonsportalen skal kunne sjå når portalen sist vart bygd, for å vurdere om innhaldet er oppdatert. Byggetidspunktet skal visast i footer på hovudsida (`index.md`).

## Mål

- Vis byggetidspunkt i footer på `mkdocs/docs/index.md`
- Tidspunkt hentast frå faktisk køyretid for `publish.sh`
- Format: ISO 8601 dato og tid (t.d. `2026-07-29 14:32 UTC`)
- Statisk verdi skrive inn i fil under bygging

## Avklaringar

- **Plassering:** Footer på hovud-`index.md` (ikkje global footer for alle sider)
- **Format:** Dato og tid i ISO 8601-format med UTC-tidssone
- **Datakjelde:** Faktisk køyretidspunkt for `publish.sh`
- **Statisk vs dynamisk:** Statisk verdi injisert under bygging

## Gjennomføring

### Steg 1: Generer tidsstempel i publish.sh

Legg til tidsstempel-generering i `mkdocs/publish.sh` etter Steg 1 (rens katalogar):

```bash
# Generer byggetidspunkt (ISO 8601 UTC)
BUILD_TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")
echo "Byggetidspunkt: $BUILD_TIMESTAMP"
```

### Steg 2: Injiser tidsstempel i hovud-index.md

Når `mkdocs/docs/index.md` vert generert frå `README.md` (Steg 3 i publish.sh), legg til footer med byggetidspunkt:

```bash
# Legg til footer med byggetidspunkt
cat >> mkdocs/docs/index.md <<EOF

---

_Portalen vart sist bygd: ${BUILD_TIMESTAMP}_
EOF
```

Alternativt, dersom hovud-index.md allereie har ein footer, oppdater eksisterande seksjon.

### Steg 3: Verifiser output

Køyr `make docs-publish` og sjekk at `mkdocs/docs/index.md` inneheld footer:

```markdown
---

_Portalen vart sist bygd: 2026-07-29 14:32 UTC_
```

### Steg 4: Oppdater publish.sh-dokumentasjon

Sjekk om `publish.sh` har intern dokumentasjon eller kommentarar som må oppdaterast for å forklare tidsstempel-injeksjonen.

## Handlingsliste

- [x] Legg til `BUILD_TIMESTAMP`-generering i `publish.sh` (etter Steg 1)
- [x] Injiser tidsstempel i `mkdocs/docs/index.md` (i Steg 3, etter README-transformering)
- [x] Verifiser at `make docs-publish` genererer korrekt footer
- [x] Oppdater publish.sh-dokumentasjon dersom nødvendig

## Utført

Alle steg i planen er gjennomført:

1. **Tidsstempel-generering:** Lagt til `BUILD_TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")` etter Steg 1 i `mkdocs/publish.sh` (linje 238)
2. **Footer-injeksjon:** Lagt til heredoc som injiserer footer i `mkdocs/docs/index.md` i Steg 3 (linje 403-409)
3. **Verifisering:** Køyrde `make docs-publish` og bekrefta at footer vart korrekt generert: `_Portalen vart sist bygd: 2026-07-29 12:33 UTC_`

Publish.sh-dokumentasjon (kommentarar i scriptet) vart ikkje oppdatert sidan endringane er sjølvdokumenterande via variabelnamnet `BUILD_TIMESTAMP` og konteksten der dei er plasserte.

## Potensielle tilleggsfunksjonar (utanfor scope for denne planen)

- Vis byggetidspunkt i global footer (alle sider)
- Vis byggetidspunkt per skjema-side (basert på siste endring av `<modell>-schema.yaml`)
- Legg til lenke til GitHub commit som utløyste bygginga (dersom tilgjengeleg i CI-kontekst)
