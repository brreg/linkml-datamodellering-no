# Changelog

## [1.8.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.7.0...modelldcat-ap-no-v1.8.0) (2026-07-09)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **ci:** legg til XSD-generering via avrotize-pipeline ([4b7478a](https://github.com/brreg/linkml-datamodellering-no/commit/4b7478a340c100db4e4d7fb5f3178bf3f0e8b4af))
* legg til flag for publisering av kvar enkelt modell i manifest.yaml som er omdøpt fra generate.yaml. Flytter data og examples katalogane inn under src/linkml/domene slik at alle relaterte filer ligg i samme struktur. ([0e1e4fb](https://github.com/brreg/linkml-datamodellering-no/commit/0e1e4fbeff55711958f0b29c74af2944302d9896))
* legg til OpenAPI 3.1 og AsyncAPI 3.0-generering ([887fe84](https://github.com/brreg/linkml-datamodellering-no/commit/887fe84fa94e08bc3616cad9aa30887740c93253))
* **mkdocs:** dokumenter delmodell-hierarki og fjern dublett-schema-sider ([5c86549](https://github.com/brreg/linkml-datamodellering-no/commit/5c865492633796b95007b9d1c81e223e183e4a58))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))
* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))
* **modellkatalog:** rull ut per-org-modellkatalogar og fyll metadata (MD2-MD4, MD6) ([7ee7b0e](https://github.com/brreg/linkml-datamodellering-no/commit/7ee7b0e0e71af5b62cadacf611e7c3b71b908f5c))
* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))
* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))
* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))


### Bug Fixes

* **ap-no,modellkatalog:** løys slot-merge-konflikt (duplikatslots) i modelldcat-ap-no-importkjeda ([81d4aa8](https://github.com/brreg/linkml-datamodellering-no/commit/81d4aa8af16ffe2920eb3dfec67cee8747ea9a97))
* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))
* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))
* **modelldcat-ap-no:** legg til manglande dcat-ap-no-import i modelldcat-modell ([2fdf786](https://github.com/brreg/linkml-datamodellering-no/commit/2fdf78621a51c02620793b93323b9af89b78f4bf))
* normaliser version-felt til tre-delt semver for release-please-kompatibilitet ([5af2108](https://github.com/brreg/linkml-datamodellering-no/commit/5af2108f3b7749fee1537950c4abf9eebf9a4eaa))
* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))
* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([6e4d623](https://github.com/brreg/linkml-datamodellering-no/commit/6e4d623d1a5f91b472748d45942e8a4fb05ad53b))
* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))

## [1.7.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.6.0...modelldcat-ap-no-v1.7.0) (2026-07-09)


### Features

* **modellmanifest:** autogenerer &lt;modell&gt;-manifest.yaml i make domain-* ([321b8a8](https://github.com/brreg/linkml-datamodellering-no/commit/321b8a8ea36b37531bc9512f5c90407a92389b8f))

## [1.6.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.5.0...modelldcat-ap-no-v1.6.0) (2026-07-09)


### Features

* **ap-no:** publiser common-ap-no i nav-meny og omdøp katalog ([35da103](https://github.com/brreg/linkml-datamodellering-no/commit/35da103f75e856685bf01e255b732241792964fa))
* **mkdocs:** konfigurerbar lenke-tekst for offisiell referanse ([a41c35a](https://github.com/brreg/linkml-datamodellering-no/commit/a41c35a660445f0180b3cdc17175386b1bd730a9))

## [1.5.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.4.0...modelldcat-ap-no-v1.5.0) (2026-07-07)


### Features

* **mkdocs:** dokumenter delmodell-hierarki og fjern dublett-schema-sider ([5c86549](https://github.com/brreg/linkml-datamodellering-no/commit/5c865492633796b95007b9d1c81e223e183e4a58))

## [1.4.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.3.0...modelldcat-ap-no-v1.4.0) (2026-07-06)


### Features

* **mkdocs:** konfigurerbare seksjons-kjelder i index.md ([94c2efb](https://github.com/brreg/linkml-datamodellering-no/commit/94c2efb8c90571a03efa5108a869e5204544bcbf))

## [1.3.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.2.2...modelldcat-ap-no-v1.3.0) (2026-07-04)


### Features

* **validate-capture:** parallelliser validering av alle skjema ([6267587](https://github.com/brreg/linkml-datamodellering-no/commit/6267587223de8b03fe459c0d6458c492aa5dd279))

## [1.2.2](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.2.1...modelldcat-ap-no-v1.2.2) (2026-07-04)


### Bug Fixes

* **release:** synk schema-versjon med release-nummer automatisk ([6dbb358](https://github.com/brreg/linkml-datamodellering-no/commit/6dbb358b6929bfbd73ef9c5fde8f1a0c24cb56e2))

## [1.2.1](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.2.0...modelldcat-ap-no-v1.2.1) (2026-07-04)


### Bug Fixes

* **ap-no:** fjern tvetydig type for lisens og hardkod generator-flagg ([c6514ca](https://github.com/brreg/linkml-datamodellering-no/commit/c6514ca76cfaa3c85753a3515b9481f726997a8f))

## [1.2.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.1.0...modelldcat-ap-no-v1.2.0) (2026-07-03)


### Features

* **validering:** komplett valideringssystem med auto-detect og visuell rapportering ([20caed0](https://github.com/brreg/linkml-datamodellering-no/commit/20caed0d1764e27864f377fcaea212506f3a6fab))

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.0.2...modelldcat-ap-no-v1.1.0) (2026-07-01)


### Features

* **ap-no,begrepskatalog,modellkatalog:** legg til DQV-kvalitetsmålingar (kvantifiserbar kvalitet) ([6fb9bad](https://github.com/brreg/linkml-datamodellering-no/commit/6fb9badce3ca37ea38fb2a6a882cad466ba8eae8))
* **modellkatalog:** rull ut per-org-modellkatalogar og fyll metadata (MD2-MD4, MD6) ([7ee7b0e](https://github.com/brreg/linkml-datamodellering-no/commit/7ee7b0e0e71af5b62cadacf611e7c3b71b908f5c))


### Bug Fixes

* **ap-no,modellkatalog:** løys slot-merge-konflikt (duplikatslots) i modelldcat-ap-no-importkjeda ([81d4aa8](https://github.com/brreg/linkml-datamodellering-no/commit/81d4aa8af16ffe2920eb3dfec67cee8747ea9a97))
* **modelldcat-ap-no:** legg til manglande dcat-ap-no-import i modelldcat-modell ([2fdf786](https://github.com/brreg/linkml-datamodellering-no/commit/2fdf78621a51c02620793b93323b9af89b78f4bf))
* **samt-bu:** rett stale slotnamn på Kvalitetsdimensjon-instans i eksempel ([6e4d623](https://github.com/brreg/linkml-datamodellering-no/commit/6e4d623d1a5f91b472748d45942e8a4fb05ad53b))

## [1.0.2](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.0.1...modelldcat-ap-no-v1.0.2) (2026-06-20)


### Bug Fixes

* **ap-no,specs:** rett avvik mot Prinsipper for informasjonsmodellar ([f93510f](https://github.com/brreg/linkml-datamodellering-no/commit/f93510f32fd44ff09cd0567d6b744bc3e661eea5))

## [1.0.1](https://github.com/brreg/linkml-datamodellering-no/compare/modelldcat-ap-no-v1.0.0...modelldcat-ap-no-v1.0.1) (2026-06-19)


### Bug Fixes

* **schemas,mcp-validator:** etterlevingsopprett mot Digdir felles modelleringsreglar (regel 6-11, 15) ([72aaaf2](https://github.com/brreg/linkml-datamodellering-no/commit/72aaaf2990834bf37a84cd514798141559e1ffef))
