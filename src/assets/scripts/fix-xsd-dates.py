#!/usr/bin/env python3
"""Post-process .xsd: replace xs:integer/xs:long with xs:date/xs:dateTime
for xs:element names that have format: date or date-time in the JSON Schema.

Usage: fix-xsd-dates.py <schema.xsd> <schema.json>

Background: avrotize a2x ignores Avro logical types (logicalType: date/timestamp-millis)
and always emits xs:integer or xs:long. This script corrects the output using the
original JSON Schema as a reference for which fields are actually date-typed.
"""

import json
import re
import sys


XSD_TYPE = {
    "date":      ("xs:integer", "xs:date"),
    "date-time": ("xs:integer", "xs:dateTime"),  # j2a maps both date and date-time to Avro int
}


def collect_formats(jsonschema_path):
    with open(jsonschema_path) as f:
        schema = json.load(f)
    formats = {}
    for defn in schema.get("$defs", {}).values():
        for name, prop in defn.get("properties", {}).items():
            fmt = prop.get("format")
            if fmt in XSD_TYPE:
                formats[name] = fmt
    return formats


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <schema.xsd> <schema.json>", file=sys.stderr)
        sys.exit(1)

    xsd_path, json_path = sys.argv[1], sys.argv[2]
    formats = collect_formats(json_path)

    with open(xsd_path) as f:
        content = f.read()

    total = 0
    for name, fmt in formats.items():
        wrong, right = XSD_TYPE[fmt]
        pattern = rf'(<xs:element name="{re.escape(name)}" type="){re.escape(wrong)}"'
        content, n = re.subn(pattern, rf'\g<1>{right}"', content)
        total += n

    with open(xsd_path, "w") as f:
        f.write(content)

    print(f"fix-xsd-dates: {total} datofelt fiksa ({', '.join(formats)})", file=sys.stderr)
