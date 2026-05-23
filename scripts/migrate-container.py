#!/usr/bin/env python3
"""
migrate-container.py — Migrerer containerklasse frå globale slots til inline attributes.

Endringa per skjemafil:
  1. Containerklassen sin `slots:`-blokk vert erstatta av `attributes:` med inline definisjonar.
  2. Globale slotdefinisjonar som BERRE er brukt av containerklassen vert sletta.
  3. Identifier-slots (identifier: true) vert fjerna frå containerklassen (ikkje gjort om til attributes).

Bruk:
    python3 scripts/migrate-container.py <schema-fil>
"""

import sys
import yaml
from pathlib import Path


# ---------------------------------------------------------------------------
# Schema-analyse (PyYAML)
# ---------------------------------------------------------------------------

def load_schema(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_container_class(schema):
    """Return (name, class_dict) for the class with tree_root: true, or (None, None)."""
    for name, cls in (schema.get("classes") or {}).items():
        if cls and cls.get("tree_root"):
            return name, cls
    return None, None


def get_slot_info(schema, slot_name):
    return (schema.get("slots") or {}).get(slot_name) or {}


def is_used_outside_container(schema, slot_name, container_name):
    """True if the slot is referenced by any class other than the container."""
    for cls_name, cls in (schema.get("classes") or {}).items():
        if cls_name == container_name:
            continue
        if cls and slot_name in (cls.get("slots") or []):
            return True
    return False


# ---------------------------------------------------------------------------
# Teksttransformasjon
# ---------------------------------------------------------------------------

def line_indent(ln):
    """Return the indentation depth of a line, or None for blank lines."""
    stripped = ln.lstrip()
    return len(ln) - len(stripped) if stripped else None


def migrate_content(content, container_name, regular_slots, slots_to_delete):
    """
    Utfør tekstleg migrasjon av YAML-innhaldet.

    regular_slots: {slot_name: {range, multivalued, inlined, inlined_as_list}}
    slots_to_delete: set av slotnaman som skal slettast frå global slots-seksjon
    """
    lines = content.split("\n")
    result = []
    i = 0

    # Forventa innrykk (2-space-stil, konsistent i heile repoet)
    CLASS_INDENT = 2      # "  ClassName:"
    SLOTS_KEY_INDENT = 4  # "    slots:"
    ITEM_INDENT = 6       # "      - slotname"
    ATTR_NAME_INDENT = 6  # "      slotname:"
    ATTR_PROP_INDENT = 8  # "        range: ..."
    GLOBAL_SLOT_INDENT = 2  # "  slotname:" i slots-seksjonen

    in_classes_section = False
    in_container_class = False
    slots_block_handled = False
    in_slots_section = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        indent = line_indent(line)

        # ── Seksjonsdeteksjon på toppnivå ───────────────────────────────
        if stripped == "classes:" and indent == 0:
            in_classes_section = True
            in_slots_section = False
            in_container_class = False
            result.append(line)
            i += 1
            continue

        if stripped == "slots:" and indent == 0:
            in_classes_section = False
            in_container_class = False
            in_slots_section = True
            result.append(line)
            i += 1
            continue

        if indent == 0 and stripped and not stripped.startswith("#"):
            # Anna toppnivånøkkel (enums:, subsets:, prefixes: …)
            in_classes_section = False
            in_container_class = False
            in_slots_section = False

        # ── Oppdager start av containerklassen ──────────────────────────
        if in_classes_section and not in_container_class:
            expected = f"{container_name}:"
            if (indent == CLASS_INDENT
                    and (stripped == expected or stripped.startswith(expected + " "))):
                in_container_class = True
                slots_block_handled = False
                result.append(line)
                i += 1
                continue

        # ── Inne i containerklassen: leitar etter `slots:` ──────────────
        if in_container_class and not slots_block_handled:
            # Forlét vi klassen?
            if indent is not None and indent <= CLASS_INDENT and stripped and not stripped.startswith("#"):
                in_container_class = False
                # fall through → handsam linja normalt nedanfor

            if in_container_class:
                # Er dette `slots:`-nøkkelen for containerklassen?
                if indent == SLOTS_KEY_INDENT and stripped == "slots:":
                    # Samlar opp slots-lista (med kommentarar mellom)
                    attrs_to_write = []  # list av ('slot'|'comment'|'other', verdi)
                    j = i + 1
                    while j < len(lines):
                        item_line = lines[j]
                        item_stripped = item_line.strip()
                        item_indent = line_indent(item_line)

                        # Kommentarar høyrer alltid til slots-lista, uansett innrykk
                        if item_stripped.startswith("#"):
                            attrs_to_write.append(("comment", item_line))
                            j += 1
                            continue

                        if item_indent is None:
                            break  # blank linje = slutt på lista
                        if item_indent < ITEM_INDENT:
                            break  # tilbake til klassenivå

                        if item_stripped.startswith("- "):
                            slot_name = item_stripped[2:].strip()
                            attrs_to_write.append(("slot", slot_name))

                        j += 1

                    # Skriv `attributes:`-blokka
                    name_pfx = " " * ATTR_NAME_INDENT
                    prop_pfx = " " * ATTR_PROP_INDENT
                    result.append(f"{' ' * SLOTS_KEY_INDENT}attributes:")

                    for atype, aval in attrs_to_write:
                        if atype == "comment":
                            result.append(aval)
                        elif atype == "slot" and aval in regular_slots:
                            info = regular_slots[aval]
                            result.append(f"{name_pfx}{aval}:")
                            for key in ["range", "multivalued", "inlined", "inlined_as_list"]:
                                if key in info:
                                    v = info[key]
                                    if isinstance(v, bool):
                                        v = "true" if v else "false"
                                    result.append(f"{prop_pfx}{key}: {v}")
                        # identifier-slots og ukjende typar vert stille fjerna

                    slots_block_handled = True
                    i = j
                    continue
                else:
                    result.append(line)
                    i += 1
                    continue

        # ── Global slots-seksjon: slett containerslots ───────────────────
        if in_slots_section:
            if (indent == GLOBAL_SLOT_INDENT
                    and ":" in stripped
                    and not stripped.startswith("#")):
                slot_candidate = stripped.split(":")[0].strip()
                if slot_candidate in slots_to_delete:
                    # Hopp over denne slotdefinisjonen og alle eigenskapane
                    i += 1
                    while i < len(lines):
                        sl = lines[i]
                        sl_indent = line_indent(sl)
                        if sl_indent is None:
                            i += 1  # tom linje inne i definisjonen
                            continue
                        if sl_indent <= GLOBAL_SLOT_INDENT:
                            break
                        i += 1
                    continue

        result.append(line)
        i += 1

    return "\n".join(result)


# ---------------------------------------------------------------------------
# Hovudprogram
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        print(f"Bruk: {sys.argv[0]} <schema-fil>", file=sys.stderr)
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"FEIL: Finna ikkje fila: {file_path}", file=sys.stderr)
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    schema = load_schema(file_path)

    container_name, container_cls = find_container_class(schema)
    if not container_cls:
        print("INFO: Ingen containerklasse (tree_root: true) funnen — hoppar over")
        sys.exit(0)

    if container_cls.get("attributes") and not container_cls.get("slots"):
        print(f"INFO: '{container_name}' brukar allereie attributes — ingenting å gjere")
        sys.exit(0)

    container_slot_list = list(container_cls.get("slots") or [])
    if not container_slot_list:
        print(f"INFO: '{container_name}' har ingen slots — ingenting å gjere")
        sys.exit(0)

    print(f"Skjema:    {file_path}")
    print(f"Container: {container_name} ({len(container_slot_list)} slots)")

    # Klassifiser kvar slot i containerklassen
    identifier_slots = []
    regular_slots = {}

    for slot_name in container_slot_list:
        info = get_slot_info(schema, slot_name)
        if info.get("identifier"):
            identifier_slots.append(slot_name)
        else:
            regular_slots[slot_name] = {
                k: info[k]
                for k in ["range", "multivalued", "inlined", "inlined_as_list"]
                if k in info
            }

    if identifier_slots:
        print(f"  Fjernar identifier-slots frå container: {identifier_slots}")

    # Finn kva globale slots som berre er brukt av containerklassen
    slots_to_delete = set()
    for slot_name in container_slot_list:
        if not is_used_outside_container(schema, slot_name, container_name):
            slots_to_delete.add(slot_name)

    kept_global = set(container_slot_list) - slots_to_delete
    if kept_global:
        print(f"  Beheld som globale slots (brukt av andre klassar): {sorted(kept_global)}")

    # Utfør migrasjonen
    new_content = migrate_content(content, container_name, regular_slots, slots_to_delete)

    # Bevar trailing newline frå originalen
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"

    # Sjekk at resultatet er gyldig YAML
    try:
        yaml.safe_load(new_content)
    except yaml.YAMLError as e:
        print(f"FEIL: Generert YAML er ugyldig: {e}", file=sys.stderr)
        print("Ingenting vart skrive.", file=sys.stderr)
        sys.exit(1)

    file_path.write_text(new_content, encoding="utf-8")
    print(f"Ferdig. Skreiv {file_path}")


if __name__ == "__main__":
    main()
