# Changelog

## [1.11.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.10.0...dqv-ap-no-v1.11.0) (2026-07-10)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([9009b1e](https://github.com/brreg/linkml-datamodellering-no/commit/9009b1e63660f55fce18c1a9bf4dda0757a27d5e))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([9653abf](https://github.com/brreg/linkml-datamodellering-no/commit/9653abf7a46a7714b216e3d0f6e3ebb97efeabc9))
* **ci:** legg til XSD-generering via avrotize-pipeline ([22b585b](https://github.com/brreg/linkml-datamodellering-no/commit/22b585b91e357a8280ad2c9c914407e8a0b1057a))
* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([524a1d8](https://github.com/brreg/linkml-datamodellering-no/commit/524a1d845017d1c3da64ca6e1ddf19cbd0b5f8b2))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([a4cccbd](https://github.com/brreg/linkml-datamodellering-no/commit/a4cccbdfb8e327d0a9bb1874b34ec21bd9c374d0))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([7be7ef8](https://github.com/brreg/linkml-datamodellering-no/commit/7be7ef8ad6e4cda9fb2a08bbc336e1c782d5d794))
* **mkdocs:** dokumenter delmodell-hierarki og fjern dublett-schema-sider ([0ab89a3](https://github.com/brreg/linkml-datamodellering-no/commit/0ab89a34a232a5d7a1479b1698dcd6c4a9758d3e))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([1d493cd](https://github.com/brreg/linkml-datamodellering-no/commit/1d493cdafb5c3991b3270b901503b7df70717f6c))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([20d8bf8](https://github.com/brreg/linkml-datamodellering-no/commit/20d8bf8c0e3d5ed31c608ece6bf5d64d7802b9af))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([122c704](https://github.com/brreg/linkml-datamodellering-no/commit/122c7047e78c3a54952d9c91910d62f53da682a3))
* **modelldcat:** inline-instansar og full LinkML-validering ([7ad1432](https://github.com/brreg/linkml-datamodellering-no/commit/7ad1432331c03f4825cefdd2531cb35a47b2adfb))
* **modelldcat:** MVP generering av Informasjonsmodell-instansar ([076e812](https://github.com/brreg/linkml-datamodellering-no/commit/076e812a0957b2488ccf000613434b772291bfd3))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([97fd24d](https://github.com/brreg/linkml-datamodellering-no/commit/97fd24de6b851e1807aa43d814ef77d58ac74b2d))
* **validate-capture:** parallelliser validering av alle skjema ([7d9a0a2](https://github.com/brreg/linkml-datamodellering-no/commit/7d9a0a28797a918d887b6ff22303ac6d56204655))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([f0607bc](https://github.com/brreg/linkml-datamodellering-no/commit/f0607bc510640fa8c85b989b995e0162385eb06e))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([ce4964b](https://github.com/brreg/linkml-datamodellering-no/commit/ce4964bc4d121438606489a41dae63ac1bea672b))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([e7029d7](https://github.com/brreg/linkml-datamodellering-no/commit/e7029d735d66bc9a0ae4b1918dd7c431b6a0c7ef))
* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([3041491](https://github.com/brreg/linkml-datamodellering-no/commit/3041491bda423efcd164c2ff82c02da0605f48bd))
* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([cc5f104](https://github.com/brreg/linkml-datamodellering-no/commit/cc5f104abc70530c6dbd2a2b97cdb76a1e25bcec))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([abd967b](https://github.com/brreg/linkml-datamodellering-no/commit/abd967be7c48043154a9c06c14d98c59e7154f36))
* **release:** synk schema-versjon med release-nummer automatisk ([1d20298](https://github.com/brreg/linkml-datamodellering-no/commit/1d20298b932da0e876795152aab61baf99611daf))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([93a25e7](https://github.com/brreg/linkml-datamodellering-no/commit/93a25e79c2eacdfa5d7548d176370200efc79279))

## [1.10.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.9.0...dqv-ap-no-v1.10.0) (2026-07-10)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([463007f](https://github.com/brreg/linkml-datamodellering-no/commit/463007fcebf08eed74de2059278733fdd92c3fc3))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** dokumenter delmodell-hierarki og fjern dublett-schema-sider ([5c86549](https://github.com/brreg/linkml-datamodellering-no/commit/5c865492633796b95007b9d1c81e223e183e4a58))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modelldcat:** inline-instansar og full LinkML-validering ([70dc840](https://github.com/brreg/linkml-datamodellering-no/commit/70dc840bb89b86abf57bdf86b93d0cf2cf62c1a7))
* **modelldcat:** MVP generering av Informasjonsmodell-instansar ([f9bd633](https://github.com/brreg/linkml-datamodellering-no/commit/f9bd63356440e1cee93b0c3c81fd9a43ad88ab2d))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([1ad5d1c](https://github.com/brreg/linkml-datamodellering-no/commit/1ad5d1c59e9e593d03d2d7e1967acba24de64033))
* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([49a093a](https://github.com/brreg/linkml-datamodellering-no/commit/49a093a19d2799ecdf606e0379dc19bc8b154126))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))

## [1.9.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.8.0...dqv-ap-no-v1.9.0) (2026-07-09)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([463007f](https://github.com/brreg/linkml-datamodellering-no/commit/463007fcebf08eed74de2059278733fdd92c3fc3))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** dokumenter delmodell-hierarki og fjern dublett-schema-sider ([5c86549](https://github.com/brreg/linkml-datamodellering-no/commit/5c865492633796b95007b9d1c81e223e183e4a58))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modelldcat:** inline-instansar og full LinkML-validering ([70dc840](https://github.com/brreg/linkml-datamodellering-no/commit/70dc840bb89b86abf57bdf86b93d0cf2cf62c1a7))
* **modelldcat:** MVP generering av Informasjonsmodell-instansar ([f9bd633](https://github.com/brreg/linkml-datamodellering-no/commit/f9bd63356440e1cee93b0c3c81fd9a43ad88ab2d))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([1ad5d1c](https://github.com/brreg/linkml-datamodellering-no/commit/1ad5d1c59e9e593d03d2d7e1967acba24de64033))
* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([49a093a](https://github.com/brreg/linkml-datamodellering-no/commit/49a093a19d2799ecdf606e0379dc19bc8b154126))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))

## [1.8.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.7.0...dqv-ap-no-v1.8.0) (2026-07-09)


### Features

* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))

## [1.7.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.6.0...dqv-ap-no-v1.7.0) (2026-07-09)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse og description.md for alle modellar ([97dacce](https://github.com/brreg/linkml-datamodellering-no/commit/97dacce159f02236196c9daa686e375e503f15ef))
* **modelldcat:** inline-instansar og full LinkML-validering ([70dc840](https://github.com/brreg/linkml-datamodellering-no/commit/70dc840bb89b86abf57bdf86b93d0cf2cf62c1a7))
* **modelldcat:** MVP generering av Informasjonsmodell-instansar ([f9bd633](https://github.com/brreg/linkml-datamodellering-no/commit/f9bd63356440e1cee93b0c3c81fd9a43ad88ab2d))

## [1.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.5.0...dqv-ap-no-v1.6.0) (2026-07-07)


### Features

* **mkdocs:** dokumenter delmodell-hierarki og fjern dublett-schema-sider ([5c86549](https://github.com/brreg/linkml-datamodellering-no/commit/5c865492633796b95007b9d1c81e223e183e4a58))

## [1.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.4.0...dqv-ap-no-v1.5.0) (2026-07-06)


### Features

* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))

## [1.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.3.2...dqv-ap-no-v1.4.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [1.3.2](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.3.1...dqv-ap-no-v1.3.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [1.3.1](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.3.0...dqv-ap-no-v1.3.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [1.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.2.0...dqv-ap-no-v1.3.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [1.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.1.2...dqv-ap-no-v1.2.0) (2026-07-01)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))

## [1.1.2](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.1.1...dqv-ap-no-v1.1.2) (2026-06-20)


### Bug Fixes

* løys valideringsfeil i samt-bu og rotårsak i dqv-ap-no (BUG-6) ([49a093a](https://github.com/brreg/linkml-datamodellering-no/commit/49a093a19d2799ecdf606e0379dc19bc8b154126))

## [1.1.1](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.1.0...dqv-ap-no-v1.1.1) (2026-06-20)


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/dqv-ap-no-v1.0.0...dqv-ap-no-v1.1.0) (2026-06-19)


### Features

* **dcat-ap-no:** legg til frekvens og manglande valfrie slots på Datasett og Distribusjon ([463007f](https://github.com/brreg/linkml-datamodellering-no/commit/463007fcebf08eed74de2059278733fdd92c3fc3))


### Bug Fixes

* **dqv-ap-no:** løys strukturelle avvik mot DQV-AP-NO-spesifikasjonen ([1ad5d1c](https://github.com/brreg/linkml-datamodellering-no/commit/1ad5d1c59e9e593d03d2d7e1967acba24de64033))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
