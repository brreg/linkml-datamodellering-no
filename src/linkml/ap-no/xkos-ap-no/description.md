XKOS-AP-NO er den norske applikasjonsprofilen av [XKOS](http://rdf-vocabulary.ddialliance.org/xkos) (eXtended Knowledge Organization System), tilpassa norsk offentleg sektor og modellert i LinkML.

Profilen definerer korleis klassifikasjonar, klassifikasjonsnivå og kategoriar skal beskrivas med metadata — etter krava i [XKOS-AP-NO-spesifikasjonen](https://data.norge.no/specification/xkos-ap-no) frå Digitaliseringsdirektoratet.

**Typisk brukar:** Offentlege verksemder som skal publisere klassifikasjonar (t.d. kodeverk, nomenklaturer) til [Felles datakatalog](https://data.norge.no), og utviklare som implementerer XKOS-AP-NO-kompatible system.

**Nøkkelklasser:** `Klassifikasjon`, `Klassifikasjonsnivaa`, `Kategori`, `KorrespondanseTabell`, `Versjon`.

**Relasjon til andre modellar i dette repoet:**
- `common-ap-no` er basislaget — felles typar og prefiks vert importerte derifrå
- `dcat-ap-no` vert importert for `Katalog`-klassen
- `skos-ap-no` er ein relatert profil for omgrep (begrep), ikkje klassifikasjonar
