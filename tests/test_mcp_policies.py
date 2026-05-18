#!/usr/bin/env python3
"""Automatiske testar for MCP-validator-policyer (bronze, silver, gold).

Køyr frå repo-rot:
  make mcp-test-policies

Krev linkml og linkml-runtime (tilgjengeleg i containeren):
  python3 tests/test_mcp_policies.py -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "mcp-linkml-validator"))
from server import validate_schema


# ── Hjelpefunksjonar ─────────────────────────────────────────────────────────

def has_error(result: dict, code: str) -> bool:
    return any(i["code"] == code and i["severity"] == "error" for i in result["issues"])


def has_warning(result: dict, code: str) -> bool:
    return any(i["code"] == code and i["severity"] == "warning" for i in result["issues"])


def issues_for(result: dict, code: str, target: str) -> list:
    return [i for i in result["issues"] if i["code"] == code and i["target"] == target]


# ── Testskjema ───────────────────────────────────────────────────────────────

_BRONZE_PASS = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    exact_mappings:
      - https://data.norge.no/concepts/1
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""

_SILVER_PASS = """\
id: https://example.org/catalog
name: SilverKatalog
description: Testmodell for sølv-policy
prefixes:
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  dqv: http://www.w3.org/ns/dqv#
  ex: https://example.org/
default_prefix: ex
classes:
  Container:
    tree_root: true
    attributes:
      kataloger:
        range: Katalog
        multivalued: true
      datasett:
        range: Datasett
        multivalued: true
      kvalitetsmaal:
        range: Kvalitetsmaal
        multivalued: true
      kvalitetsmalinger:
        range: Kvalitetsmaaling
        multivalued: true
  Katalog:
    description: Ein DCAT-katalog
    exact_mappings:
      - https://data.norge.no/concepts/katalog
    slots:
      - id
      - beskrivelse
      - kontaktpunkt
      - tittel
      - utgiver
  Datasett:
    description: Eit DCAT-datasett
    exact_mappings:
      - https://data.norge.no/concepts/datasett
    slots:
      - id
      - beskrivelse
      - kontaktpunkt
      - tema
      - tittel
      - utgiver
  Kvalitetsmaal:
    description: Eit kvalitetsmål
    exact_mappings:
      - https://data.norge.no/concepts/kvalitetsmaal
    slots:
      - id
  Kvalitetsmaaling:
    description: Ei kvalitetsmåling
    exact_mappings:
      - https://data.norge.no/concepts/kvalitetsmaaling
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
  beskrivelse:
    description: Beskriving
    slot_uri: dct:description
    range: string
  kontaktpunkt:
    description: Kontaktpunkt
    slot_uri: dcat:contactPoint
    range: string
  tittel:
    description: Tittel
    slot_uri: dct:title
    range: string
  utgiver:
    description: Utgjevar
    slot_uri: dct:publisher
    range: string
  tema:
    description: Tema
    slot_uri: dcat:theme
    range: string
"""

_GOLD_PASS = """\
id: https://example.org/catalog
name: GoldKatalog
title: Gull-testkatalog
description: Testmodell for gull-policy
version: "1.0"
prefixes:
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  dqv: http://www.w3.org/ns/dqv#
  foaf: http://xmlns.com/foaf/0.1/
  ex: https://example.org/
default_prefix: ex
classes:
  Container:
    tree_root: true
    attributes:
      kataloger:
        range: Katalog
        multivalued: true
      datasett:
        range: Datasett
        multivalued: true
      kvalitetsmaal:
        range: Kvalitetsmaal
        multivalued: true
      kvalitetsmalinger:
        range: Kvalitetsmaaling
        multivalued: true
  Katalog:
    class_uri: dcat:Catalog
    description: Ein DCAT-katalog
    exact_mappings:
      - https://data.norge.no/concepts/katalog
    slots:
      - id
      - beskrivelse
      - kontaktpunkt
      - tittel
      - utgiver
      - lisens
      - opphavar
  Datasett:
    class_uri: dcat:Dataset
    description: Eit DCAT-datasett
    exact_mappings:
      - https://data.norge.no/concepts/datasett
    slots:
      - id
      - beskrivelse
      - kontaktpunkt
      - tema
      - tittel
      - utgiver
  Kvalitetsmaal:
    class_uri: dqv:Metric
    description: Eit kvalitetsmål
    exact_mappings:
      - https://data.norge.no/concepts/kvalitetsmaal
    slots:
      - id
  Kvalitetsmaaling:
    class_uri: dqv:QualityMeasurement
    description: Ei kvalitetsmåling
    exact_mappings:
      - https://data.norge.no/concepts/kvalitetsmaaling
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    slot_uri: dct:identifier
    range: uriorcurie
  beskrivelse:
    description: Beskriving
    slot_uri: dct:description
    range: string
  kontaktpunkt:
    description: Kontaktpunkt
    slot_uri: dcat:contactPoint
    range: string
  tittel:
    description: Tittel
    slot_uri: dct:title
    range: string
  utgiver:
    description: Utgjevar
    slot_uri: dct:publisher
    range: string
  tema:
    description: Tema
    slot_uri: dcat:theme
    range: string
  lisens:
    description: Lisens
    slot_uri: dct:license
    range: uriorcurie
  opphavar:
    description: Opphavar
    slot_uri: dct:creator
    range: string
"""


# ── Bronze ───────────────────────────────────────────────────────────────────

class TestBronze(unittest.TestCase):

    def test_gyldig_skjema_har_ingen_feil(self):
        r = validate_schema(_BRONZE_PASS, "bronze")
        self.assertEqual(r["errorCount"], 0)

    def test_klasse_utan_description_gir_advarsel(self):
        # id og name er alltid auto-populert av linkml-runtime frå filnamnet;
        # klasse-description er derimot ikkje auto-populert og er testbar.
        schema = """\
id: https://example.org/schema
name: TestSchema
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "bronze"), "missing_recommended_metadata"))

    def test_schema_utan_description_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
prefixes:
  ex: https://example.org/
default_prefix: ex
"""
        self.assertTrue(has_warning(validate_schema(schema, "bronze"), "missing_recommended_metadata"))

    def test_klasse_utan_identifikator_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
"""
        self.assertTrue(has_warning(validate_schema(schema, "bronze"), "all_classes_have_identifier"))

    def test_klasse_med_arva_identifikator_passerer(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Base:
    description: Baseklasse
    slots:
      - id
  Ting:
    description: Ei ting
    is_a: Base
    exact_mappings:
      - https://data.norge.no/concepts/1
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        r = validate_schema(schema, "bronze")
        self.assertFalse(issues_for(r, "all_classes_have_identifier", "class:Ting"))

    def test_klasse_utan_omgrepstilvisning_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "bronze"), "all_classes_have_concept_ref"))

    def test_see_also_til_begrepskatalog_godtatt(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    see_also:
      - https://data.norge.no/concepts/2
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        r = validate_schema(schema, "bronze")
        self.assertFalse(issues_for(r, "all_classes_have_concept_ref", "class:Ting"))

    def test_tree_root_klasse_er_unntatt_frå_sjekkar(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Container:
    tree_root: true
    attributes:
      ting:
        range: Ting
  Ting:
    description: Ei ting
    exact_mappings:
      - https://data.norge.no/concepts/1
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        r = validate_schema(schema, "bronze")
        self.assertFalse(issues_for(r, "all_classes_have_identifier", "class:Container"))
        self.assertFalse(issues_for(r, "all_classes_have_concept_ref", "class:Container"))


# ── Silver ───────────────────────────────────────────────────────────────────

class TestSilver(unittest.TestCase):

    def test_gyldig_skjema_har_ingen_feil(self):
        r = validate_schema(_SILVER_PASS, "silver")
        self.assertEqual(r["errorCount"], 0)

    def test_arvar_bronze_omgrepstilvisning_sjekk(self):
        # Verifiserer at silver arvar bronze-sjekken for omgrepstilvisning
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "silver"), "all_classes_have_concept_ref"))

    def test_katalog_utan_beskrivelse_gir_feil(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
classes:
  Katalog:
    description: Ein katalog
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        self.assertTrue(has_error(validate_schema(schema, "silver"), "class_missing_required_slot"))

    def test_datasett_utan_tema_gir_feil(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  dcat: http://www.w3.org/ns/dcat#
  ex: https://example.org/
default_prefix: ex
classes:
  Datasett:
    description: Eit datasett
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        self.assertTrue(has_error(validate_schema(schema, "silver"), "class_missing_required_slot"))

    def test_klasse_ikkje_i_skjema_utløyser_ikkje_sjekk(self):
        # Katalogpost er ikkje definert — ingen sjekkar for den klassen
        r = validate_schema(_SILVER_PASS, "silver")
        self.assertFalse(any(i["target"] == "class:Katalogpost" for i in r["issues"]))

    def test_container_utan_katalog_gir_feil(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Container:
    tree_root: true
    attributes:
      ting:
        range: Ting
  Ting:
    description: Ei ting
"""
        self.assertTrue(has_error(validate_schema(schema, "silver"), "container_missing_required_class"))

    def test_container_utan_distribusjon_gir_advarsel(self):
        # Container har alle obligatoriske klasser, men manglar Distribusjon (anbefalt)
        r = validate_schema(_SILVER_PASS, "silver")
        self.assertTrue(has_warning(r, "container_missing_recommended_class"))

    def test_ingen_containerklasse_gir_feil_berre_ein_gong(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
"""
        r = validate_schema(schema, "silver")
        no_container = [i for i in r["issues"] if i["code"] == "no_container_class"]
        self.assertEqual(len(no_container), 1)  # deduplisert — berre éin feil


# ── Gold ─────────────────────────────────────────────────────────────────────

class TestGold(unittest.TestCase):

    def test_gyldig_skjema_har_ingen_feil(self):
        r = validate_schema(_GOLD_PASS, "gold")
        self.assertEqual(r["errorCount"], 0)

    def test_arvar_silver_katalog_manglar_slot_gir_feil(self):
        # Gold arvar silver — AP-NO-sjekk for Katalog skal framleis gjelda
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
version: "1.0"
prefixes:
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  ex: https://example.org/
default_prefix: ex
classes:
  Katalog:
    class_uri: dcat:Catalog
    description: Ein katalog
    exact_mappings:
      - https://data.norge.no/concepts/katalog
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    slot_uri: dct:identifier
    range: uriorcurie
"""
        self.assertTrue(has_error(validate_schema(schema, "gold"), "class_missing_required_slot"))

    def test_fair_f1_schema_id_ikkje_http_gir_feil(self):
        schema = """\
id: urn:example:schema
name: TestSchema
description: Testmodell
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
"""
        self.assertTrue(has_error(validate_schema(schema, "gold"), "fair_f1"))

    def test_fair_f2_schema_utan_title_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
description: Testmodell
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_f2"))

    def test_fair_f3_klasse_utan_class_uri_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
version: "1.0"
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    exact_mappings:
      - https://data.norge.no/concepts/1
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    slot_uri: dct:identifier
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_f3"))

    def test_fair_f4_schema_utan_version_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_f4"))

    def test_fair_i1_slot_utan_slot_uri_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
version: "1.0"
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    exact_mappings:
      - https://data.norge.no/concepts/1
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_i1"))

    def test_fair_i2_utan_standard_prefiks_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
version: "1.0"
prefixes:
  ex: https://example.org/
default_prefix: ex
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_i2"))

    def test_fair_r11_utan_lisensslot_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
version: "1.0"
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    exact_mappings:
      - https://data.norge.no/concepts/1
    slots:
      - id
slots:
  id:
    description: Identifikator
    identifier: true
    slot_uri: dct:identifier
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_r11"))

    def test_fair_r12_utan_provenienssslot_gir_advarsel(self):
        schema = """\
id: https://example.org/schema
name: TestSchema
title: Testtittel
description: Testmodell
version: "1.0"
prefixes:
  dct: http://purl.org/dc/terms/
  ex: https://example.org/
default_prefix: ex
classes:
  Ting:
    description: Ei ting
    exact_mappings:
      - https://data.norge.no/concepts/1
    slots:
      - id
      - lisens
slots:
  id:
    description: Identifikator
    identifier: true
    slot_uri: dct:identifier
    range: uriorcurie
  lisens:
    description: Lisens
    slot_uri: dct:license
    range: uriorcurie
"""
        self.assertTrue(has_warning(validate_schema(schema, "gold"), "fair_r12"))


if __name__ == "__main__":
    unittest.main()
