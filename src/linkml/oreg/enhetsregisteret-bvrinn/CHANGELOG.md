# Changelog

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/enhetsregisteret-bvrinn-v1.0.0...enhetsregisteret-bvrinn-v1.1.0) (2026-08-17)


### Features

* **asyncapi:** reduser image-storleik frå 4.43 GB til 296 MB ([0b61fa2](https://github.com/brreg/linkml-datamodellering-no/commit/0b61fa2c813b89f1fef0357e5fe119f75b6c1ccb))
* **generatorar:** legg til gen-graphql for GraphQL SDL-generering ([cb0a7bd](https://github.com/brreg/linkml-datamodellering-no/commit/cb0a7bd4c220dbee889df488bed0eaeb25960ce4))
* **make:** batch linkml-validate for validate-examples per domene ([a38f603](https://github.com/brreg/linkml-datamodellering-no/commit/a38f6030b61a6bf6c1230303112d148d2788281d))
* **metadata:** dynamisk README-generering frå skjema-metadata ([53def55](https://github.com/brreg/linkml-datamodellering-no/commit/53def559d46e92c604ff429b46be90381f907eaf))


### Bug Fixes

* **ci:** ekskluder begrepssamling-katalogar og legg til validation_policy i modellkatalog ([fe7dce0](https://github.com/brreg/linkml-datamodellering-no/commit/fe7dce05a14fcf7736372248e1d551188415624f))
* **lenkjesjekk:** rett resterande brotne lenkjer og ekskluder stadfesta upubliserte vokabular ([6cb82bf](https://github.com/brreg/linkml-datamodellering-no/commit/6cb82bfa54ceafaeaab625aae5dcfbaa8241eb2d))
* **oreg,mcp-validator:** rett generate-workflow-feil for blomsterregisteret ([1bd6f61](https://github.com/brreg/linkml-datamodellering-no/commit/1bd6f6183d0586fc13e21ccb81f9affce4e54992))
* **oreg:** rett Adressenummer.nummer sin range til Husnummer ([918f6ff](https://github.com/brreg/linkml-datamodellering-no/commit/918f6ff7bf4559d1fca5458650f048e5b6f9f501))


### Performance Improvements

* **mcp-linkml-validator:** parallelliser validate-examples, regenerer valideringsloggar ([fc67279](https://github.com/brreg/linkml-datamodellering-no/commit/fc672798d9b85870590a1bf7ea33fbca4181bf51))
