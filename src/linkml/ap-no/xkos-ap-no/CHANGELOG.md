# Changelog

## [1.1.0](https://github.com/brreg/linkml-datamodellering-no/compare/xkos-ap-no-v1.0.0...xkos-ap-no-v1.1.0) (2026-08-17)


### Features

* **asyncapi:** reduser image-storleik frå 4.43 GB til 296 MB ([0b61fa2](https://github.com/brreg/linkml-datamodellering-no/commit/0b61fa2c813b89f1fef0357e5fe119f75b6c1ccb))
* **generatorar:** legg til gen-graphql for GraphQL SDL-generering ([cb0a7bd](https://github.com/brreg/linkml-datamodellering-no/commit/cb0a7bd4c220dbee889df488bed0eaeb25960ce4))
* **make:** batch linkml-validate for validate-examples per domene ([a38f603](https://github.com/brreg/linkml-datamodellering-no/commit/a38f6030b61a6bf6c1230303112d148d2788281d))
* **metadata:** dynamisk README-generering frå skjema-metadata ([53def55](https://github.com/brreg/linkml-datamodellering-no/commit/53def559d46e92c604ff429b46be90381f907eaf))


### Bug Fixes

* **ap-no,fint,fair,begrepskatalog:** sett status til UnderDevelopment i alle skjema ([2c6215e](https://github.com/brreg/linkml-datamodellering-no/commit/2c6215eac75b1e247f5f10ec355fe9b504c382af))
* **make:** korriger trap-syntaks i parallelle generator-makroar ([2d18827](https://github.com/brreg/linkml-datamodellering-no/commit/2d18827aa0568bdd04b1fc54242b3ca739ffe25b))
* **make:** rett stdin-konsumering i validate-bronze (BUG-10) ([91795ac](https://github.com/brreg/linkml-datamodellering-no/commit/91795ace2400341ba3ef052e4bb84cefe6e38215))
* **make:** valider ap-no-eksempelfiler via fixture, rett stdin-konsumerings-bug ([27c3979](https://github.com/brreg/linkml-datamodellering-no/commit/27c3979820230b8161e31aaf645917733745a5d6))


### Performance Improvements

* **mcp-linkml-validator:** parallelliser validate-examples, regenerer valideringsloggar ([fc67279](https://github.com/brreg/linkml-datamodellering-no/commit/fc672798d9b85870590a1bf7ea33fbca4181bf51))
