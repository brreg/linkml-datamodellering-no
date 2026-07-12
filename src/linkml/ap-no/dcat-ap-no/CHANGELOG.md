# Changelog

## [2.10.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.9.0...dcat-ap-no-v2.10.0) (2026-07-12)


### Features

* **ap-no:** implementer kontrollerte vokabular frå ModelDCAT-AP-NO kap. 9 ([669dcb2](https://github.com/brreg/linkml-datamodellering-no/commit/669dcb288227f908ff0b60f925a6367035e8bdcd))
* **ap-no:** legg til EU Access Rights, ADMS Publisher Type og DCT Frequency som enumerasjonar ([2fbc2d7](https://github.com/brreg/linkml-datamodellering-no/commit/2fbc2d7ff6ce1856c5ca426635882d46e2dd5d06))
* **ap-no:** legg til maskinlesbare annotations for kontrollerte vokabular ([baa7cee](https://github.com/brreg/linkml-datamodellering-no/commit/baa7ceee52b14ac15535c8052f0d011b43d3e626))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([9653abf](https://github.com/brreg/linkml-datamodellering-no/commit/9653abf7a46a7714b216e3d0f6e3ebb97efeabc9))
* **begrepskatalog:** begrep per fil, automatisk aggregering, nye verktøy og oppdatert dokumentasjon ([e2d7d95](https://github.com/brreg/linkml-datamodellering-no/commit/e2d7d9522971ad423c0f313d44a19780d23e4603))
* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* **dcat-ap-no:** legg til EU-vokabular-enumerasjonar og rett multiplisitetsavvik ([6f596ae](https://github.com/brreg/linkml-datamodellering-no/commit/6f596aefdcb85b4ba53dce4f1e4df3db7e6443cf))
* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([524a1d8](https://github.com/brreg/linkml-datamodellering-no/commit/524a1d845017d1c3da64ca6e1ddf19cbd0b5f8b2))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([1d493cd](https://github.com/brreg/linkml-datamodellering-no/commit/1d493cdafb5c3991b3270b901503b7df70717f6c))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([122c704](https://github.com/brreg/linkml-datamodellering-no/commit/122c7047e78c3a54952d9c91910d62f53da682a3))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([97fd24d](https://github.com/brreg/linkml-datamodellering-no/commit/97fd24de6b851e1807aa43d814ef77d58ac74b2d))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no,modellkatalog:** løys slot-merge-konflikt (duplikatslots) i modelldcat-ap-no-importkjeda ([3a9aaad](https://github.com/brreg/linkml-datamodellering-no/commit/3a9aaad45b688343a688d4a7130519800acfba65))
* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([ce4964b](https://github.com/brreg/linkml-datamodellering-no/commit/ce4964bc4d121438606489a41dae63ac1bea672b))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **dcat-ap-no:** tilrådde verdiar og subset-justeringar per retningslinjer for offentlege data ([ca2e1fd](https://github.com/brreg/linkml-datamodellering-no/commit/ca2e1fde619e89ef4034c156a86a885b7c8b557d))
* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([3041491](https://github.com/brreg/linkml-datamodellering-no/commit/3041491bda423efcd164c2ff82c02da0605f48bd))
* **los:** rett alle Los-URI-avvik og legg til rettleiing (LO1–LO5) ([05df4cc](https://github.com/brreg/linkml-datamodellering-no/commit/05df4ccd0f7b1565bd34b5fe039e238d3427bb63))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([abd967b](https://github.com/brreg/linkml-datamodellering-no/commit/abd967be7c48043154a9c06c14d98c59e7154f36))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

## [2.9.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.8.0...dcat-ap-no-v2.9.0) (2026-07-10)


### Features

* **ap-no:** implementer kontrollerte vokabular frå ModelDCAT-AP-NO kap. 9 ([669dcb2](https://github.com/brreg/linkml-datamodellering-no/commit/669dcb288227f908ff0b60f925a6367035e8bdcd))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([9653abf](https://github.com/brreg/linkml-datamodellering-no/commit/9653abf7a46a7714b216e3d0f6e3ebb97efeabc9))
* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* **dcat-ap-no:** legg til EU-vokabular-enumerasjonar og rett multiplisitetsavvik ([6f596ae](https://github.com/brreg/linkml-datamodellering-no/commit/6f596aefdcb85b4ba53dce4f1e4df3db7e6443cf))
* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([524a1d8](https://github.com/brreg/linkml-datamodellering-no/commit/524a1d845017d1c3da64ca6e1ddf19cbd0b5f8b2))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([1d493cd](https://github.com/brreg/linkml-datamodellering-no/commit/1d493cdafb5c3991b3270b901503b7df70717f6c))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([122c704](https://github.com/brreg/linkml-datamodellering-no/commit/122c7047e78c3a54952d9c91910d62f53da682a3))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([97fd24d](https://github.com/brreg/linkml-datamodellering-no/commit/97fd24de6b851e1807aa43d814ef77d58ac74b2d))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no,modellkatalog:** løys slot-merge-konflikt (duplikatslots) i modelldcat-ap-no-importkjeda ([3a9aaad](https://github.com/brreg/linkml-datamodellering-no/commit/3a9aaad45b688343a688d4a7130519800acfba65))
* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([ce4964b](https://github.com/brreg/linkml-datamodellering-no/commit/ce4964bc4d121438606489a41dae63ac1bea672b))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **dcat-ap-no:** tilrådde verdiar og subset-justeringar per retningslinjer for offentlege data ([ca2e1fd](https://github.com/brreg/linkml-datamodellering-no/commit/ca2e1fde619e89ef4034c156a86a885b7c8b557d))
* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([3041491](https://github.com/brreg/linkml-datamodellering-no/commit/3041491bda423efcd164c2ff82c02da0605f48bd))
* **los:** rett alle Los-URI-avvik og legg til rettleiing (LO1–LO5) ([05df4cc](https://github.com/brreg/linkml-datamodellering-no/commit/05df4ccd0f7b1565bd34b5fe039e238d3427bb63))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([abd967b](https://github.com/brreg/linkml-datamodellering-no/commit/abd967be7c48043154a9c06c14d98c59e7154f36))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

## [2.8.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.7.0...dcat-ap-no-v2.8.0) (2026-07-09)


### Features

* **ap-no:** implementer kontrollerte vokabular frå ModelDCAT-AP-NO kap. 9 ([d49a703](https://github.com/brreg/linkml-datamodellering-no/commit/d49a703659763dfb340d20a263654fc50b904897))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* **dcat-ap-no:** legg til EU-vokabular-enumerasjonar og rett multiplisitetsavvik ([f84493e](https://github.com/brreg/linkml-datamodellering-no/commit/f84493e44a565dd8452737893a7ef40f242ded34))
* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([463007f](https://github.com/brreg/linkml-datamodellering-no/commit/463007fcebf08eed74de2059278733fdd92c3fc3))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,modellkatalog:** løys slot-merge-konflikt (duplikatslots) i modelldcat-ap-no-importkjeda ([81d4aa8](https://github.com/brreg/linkml-datamodellering-no/commit/81d4aa8af16ffe2920eb3dfec67cee8747ea9a97))
* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* **dcat-ap-no:** tilrådde verdiar og subset-justeringar per retningslinjer for offentlege data ([2a0ad00](https://github.com/brreg/linkml-datamodellering-no/commit/2a0ad00d690b416083ca48cdcc7f63f387d26b05))
* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([1ad5d1c](https://github.com/brreg/linkml-datamodellering-no/commit/1ad5d1c59e9e593d03d2d7e1967acba24de64033))
* **los:** rett alle Los-URI-avvik og legg til rettleiing (LO1–LO5) ([7673852](https://github.com/brreg/linkml-datamodellering-no/commit/7673852bf911b8b8d0935aae6a471e9d1e79c485))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))

## [2.7.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.6.0...dcat-ap-no-v2.7.0) (2026-07-09)


### Features

* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))

## [2.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.5.0...dcat-ap-no-v2.6.0) (2026-07-09)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))

## [2.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.4.0...dcat-ap-no-v2.5.0) (2026-07-06)


### Features

* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))

## [2.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.3.0...dcat-ap-no-v2.4.0) (2026-07-05)


### Features

* **ap-no:** implementer kontrollerte vokabular frå ModelDCAT-AP-NO kap. 9 ([d49a703](https://github.com/brreg/linkml-datamodellering-no/commit/d49a703659763dfb340d20a263654fc50b904897))
* **dcat-ap-no:** legg til EU-vokabular-enumerasjonar og rett multiplisitetsavvik ([f84493e](https://github.com/brreg/linkml-datamodellering-no/commit/f84493e44a565dd8452737893a7ef40f242ded34))

## [2.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.2.2...dcat-ap-no-v2.3.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [2.2.2](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.2.1...dcat-ap-no-v2.2.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [2.2.1](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.2.0...dcat-ap-no-v2.2.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [2.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.1.2...dcat-ap-no-v2.2.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [2.1.2](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.1.1...dcat-ap-no-v2.1.2) (2026-07-01)


### Bug Fixes

* **ap-no,modellkatalog:** løys slot-merge-konflikt (duplikatslots) i modelldcat-ap-no-importkjeda ([81d4aa8](https://github.com/brreg/linkml-datamodellering-no/commit/81d4aa8af16ffe2920eb3dfec67cee8747ea9a97))

## [2.1.1](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.1.0...dcat-ap-no-v2.1.1) (2026-06-20)


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **dcat-ap-no:** tilrådde verdiar og subset-justeringar per retningslinjer for offentlege data ([2a0ad00](https://github.com/brreg/linkml-datamodellering-no/commit/2a0ad00d690b416083ca48cdcc7f63f387d26b05))

## [2.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/dcat-ap-no-v2.0.0...dcat-ap-no-v2.1.0) (2026-06-19)


### Features

* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([463007f](https://github.com/brreg/linkml-datamodellering-no/commit/463007fcebf08eed74de2059278733fdd92c3fc3))


### Bug Fixes

* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([1ad5d1c](https://github.com/brreg/linkml-datamodellering-no/commit/1ad5d1c59e9e593d03d2d7e1967acba24de64033))
* **los:** rett alle Los-URI-avvik og legg til rettleiing (LO1-LO5) ([7673852](https://github.com/brreg/linkml-datamodellering-no/commit/7673852bf911b8b8d0935aae6a471e9d1e79c485))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
