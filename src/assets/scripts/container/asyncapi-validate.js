#!/usr/bin/env node
const fs = require('fs');
const { Parser } = require('@asyncapi/parser');
const yaml = require('js-yaml');

async function validate(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    yaml.load(content);

    const parser = new Parser();
    const { diagnostics } = await parser.parse(content);

    if (diagnostics.length > 0) {
      let hasErrors = false;
      console.log('Validation diagnostics:');
      diagnostics.forEach(d => {
        const severity = d.severity === 0 ? 'ERROR' : d.severity === 1 ? 'WARN' : 'INFO';
        console.log(`  ${severity}: ${d.message}`);
        if (d.severity === 0) hasErrors = true;
      });

      if (hasErrors) {
        console.error(`\nFile ${filePath} has validation errors.`);
        process.exit(1);
      } else {
        console.log(`\nFile ${filePath} is valid but has warnings.`);
        process.exit(0);
      }
    }

    console.log(`File ${filePath} is valid!`);
    process.exit(0);
  } catch (error) {
    console.error('Validation failed:', error.message);
    if (error.stack) console.error(error.stack);
    process.exit(1);
  }
}

// Support both "asyncapi-validate <file>" and "asyncapi-validate validate <file>" syntax
let filePath = process.argv[2];
if (filePath === 'validate' && process.argv[3]) {
  // Backward compatibility: called as "asyncapi-validate validate <file>"
  filePath = process.argv[3];
} else if (!filePath) {
  console.error('Usage: asyncapi-validate [validate] <file>');
  process.exit(1);
}

validate(filePath);
