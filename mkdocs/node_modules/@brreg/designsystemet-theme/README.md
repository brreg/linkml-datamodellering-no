Theme for the Brønnøysund Register Centre for use with [@digdir/designsystemet](https://github.com/digdir/designsystemet)

[![Latest release](https://img.shields.io/npm/v/%40brreg%2Fdesignsystemet-theme)](https://www.npmjs.com/package/@brreg/designsystemet-theme)

## Gettings started:

### 1 Set up designsystemet
See https://github.com/digdir/designsystemet?tab=readme-ov-file#-get-started

### 2. Install theme


````
npm install @brreg/designsystemet-theme
````

### 3. Import theme-css
````ts
import '@brreg/designsystemet-theme/css/brreg.css'
````

## Contributing

### Updating CSS
CSS-files are automatically generated whenever changes to token-files are pushed to `main`-branch.

To update manually, run ```npm run build``` in your local repository.


### Publishing a new version
To release a new version of the package, just update the version-number in [package.json](package.json).
