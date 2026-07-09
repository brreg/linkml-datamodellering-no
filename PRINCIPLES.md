# Designprinsipp

**Formål:** Dokumenterer dei grunnleggjande designprinsippa som styrer modelleringa i dette repoet.

---

## 1. Slots, ikkje attributes (for domeneklassar)

Alle domeneklasseeigeskapar vert modellerte som globale slots. Klassespesifikke
innskrenkingar ligg i `slot_usage`. Containerklassen (`tree_root: true`) er unntaket:
der vert klassereferansar modellerte som inline `attributes`.

**Grunngiving:** Globale slots er gjenbrukbare og kan ha `slot_uri` som mapar til RDF.

---

## 2. Lenking framfor inlining

Klasser som kan opptre sjølvstendig får `identifier: true`. Referansar til andre klasser
vert modelert med URI-referanse, ikkje inlining.

**Grunngiving:** Instansar kan lenkast og delast mellom datasett utan å kopierast.

---

## 3. Modularitet via import-hierarki

Skjema importerer frå eit klart hierarki — aldri på tvers eller nedover.

**Fullstendig hierarki-oversikt:** Sjå [mkdocs/docs/importhierarki.md](mkdocs/docs/importhierarki.md) for komplett dokumentasjon av:
- AP-NO-hierarki (common-ap-no → dcat-ap-no / dqv-ap-no / skos-ap-no / xkos-ap-no / cpsv-ap-no / modelldcat-ap-no)
- FINT-hierarki (fint-common → fint-administrasjon / fint-arkiv / fint-okonomi / osv.)
- FAIR-metadata (standalone, kan kombinerast med AP-NO, FINT og oreg)
- Konkrete import-eksempel i YAML
- Reglar per hierarki
- Versjonslåsing-rettleiing for domenemodell-import

**Grunngiving:** Hindrar sirkulær import, gjer avhengigheitane tydelege og støttar gjenbruk.

---

## 4. Skriftspråk er domenebasert

| Domene | Språk |
|---|---|
| Modellering (klassenamn, slotnamn, skildringar i `.yaml`) | Norsk bokmål |
| Dokumentasjon (README, mkdocs-sider, spesifikasjonar i `specs/`) | Nynorsk |

**Grunngiving:** Bokmål i modellering følgjer terminologien i norske offentlege standardar
(DCAT-AP-NO, SKOS-AP-NO m.fl.) som er skrivne på bokmål.

---

## 5. Ingen lokale avhengigheiter

All verktøybruk skjer i containere (Podman, WSL2). Det skal ikkje installerast
Python-pakkar, Node-avhengigheiter eller anna verktøy direkte på vertsmaskina.

**Grunngiving:** Reproduserbarheit og portabilitet. Kvar brukar køyrer same miljø.

---

## 6. Pull, ikkje push

Repoet *genererer* artefaktar og publiserer dei til GitHub Pages og GitHub Releases.
Andre system hentar artefaktane derifrå sjølve — repoet pusher aldri til eksterne kjelder
(schema-registry, API-katalog, datakatalog o.l.).

**Grunngiving:** Push-integrasjon krev spesialtilpassingar per målsystem, knyt repoet til
ekstern tilgjengelegheit og autentisering, og gjer det vanskeleg å vedlikehalde.

---

## Sjå også

- [SCOPE.md](SCOPE.md) — kva repoet er, kva det ikkje er, og kva som høyrer heime her
- [CONVENTIONS.md](CONVENTIONS.md) — namnekonvensjonar og manifestformat
- [CLAUDE.md](CLAUDE.md) — detaljerte arbeidsflytinstruksjonar for AI-assistentar
