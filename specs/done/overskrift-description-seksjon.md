# Overskrift for description.md-seksjon i index.md

**Bakgrunn:** Brukaren merka at description.md-innhaldet i index.md per skjema manglar overskrift. Dette ser inkonsistent ut — alle andre seksjonar i index.md har overskrifter (Kom i gang, Eksempeldatafil, Modellmetadata osv.), men description.md-teksten kjem direkte etter badges/external_reference utan tydeleg seksjonsskil.

**Mål:** Legg til ei fornuftig seksjon-overskrift over description.md-innhaldet for å gjere strukturen tydeleg og konsistent.

**Avklart overskrift:** `## Om denne modellen`

**Planlagde steg:**
1. ~~Avklar med brukaren kva overskrift som skal brukast~~ ✓ Avklart: "Om denne modellen"
2. Oppdater `mkdocs/lib/sections/description.sh` til å generere `## Om denne modellen` over innhaldet
3. Regenerer dokumentasjonsportal (`make docs-publish`) for å verifisere at overskrifta vises i alle skjema med `description.md`
4. Verifiser visuelt i ein nettlesar at overskrifta vises korrekt (t.d. samt-bu, register-over-aksjeeiere)

**Handlingsliste:**
- [x] Avklar overskrift med brukaren
- [x] Oppdater `description.sh`
- [x] Regenerer portal
- [x] Verifiser visuelt (samt-bu, register-over-aksjeeiere, dcat-ap-no)

## Utført

Implementerte overskrifta "Om denne modellen" i `mkdocs/lib/sections/description.sh` og regenererte dokumentasjonsportalen. Verifiserte visuelt i samt-bu, register-over-aksjeeiere og dcat-ap-no at overskrifta vises korrekt. Alle skjema med `description.md` har no tydeleg seksjon-overskrift.
