#!/usr/bin/env python3
"""
Parse dependency tree from importhierarki.md and build hierarchical tree for a schema.

Usage:
    python3 parse-dependency-tree.py <schema_name> <imports_list>

Arguments:
    schema_name: Name of the schema (e.g., "samt-bu", "dcat-ap-no")
    imports_list: Space-separated list of imports (e.g., "linkml:types ap-no/dcat-ap-no/dcat-ap-no")

Output:
    ASCII tree showing transitive dependencies from left to right
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Set, Optional


def parse_hierarchy_blocks(md_content: str) -> Dict[str, Dict[str, List[str]]]:
    """
    Parse all ASCII tree blocks from importhierarki.md.

    Returns:
        Dict mapping domain name to {schema_name: [child_schemas]}
    """
    hierarchies = {}
    current_domain = None
    in_code_block = False
    current_tree_lines = []

    for line in md_content.split('\n'):
        # Detect domain headers
        if line.startswith('## ') and '-hierarki' in line.lower():
            current_domain = line.replace('## ', '').replace('-hierarki', '').strip().lower()
            hierarchies[current_domain] = {}
            in_code_block = False
            current_tree_lines = []
        elif line.startswith('## '):
            # Non-hierarchy section
            if current_tree_lines and current_domain:
                hierarchies[current_domain] = parse_tree_lines(current_tree_lines)
            current_domain = None
            in_code_block = False
            current_tree_lines = []
        # Detect code blocks
        elif line.strip() == '```' and current_domain:
            if in_code_block:
                # End of code block
                hierarchies[current_domain] = parse_tree_lines(current_tree_lines)
                current_tree_lines = []
            in_code_block = not in_code_block
        elif in_code_block and current_domain:
            current_tree_lines.append(line)

    # Handle last block
    if current_tree_lines and current_domain:
        hierarchies[current_domain] = parse_tree_lines(current_tree_lines)

    return hierarchies


def parse_tree_lines(lines: List[str]) -> Dict[str, List[str]]:
    """
    Parse ASCII tree lines into {parent: [children]} mapping.

    Example input:
        linkml:types
            └── common-ap-no
                └── dcat-ap-no

    Returns:
        {
            'linkml:types': ['common-ap-no'],
            'common-ap-no': ['dcat-ap-no']
        }
    """
    tree = {}
    stack = []  # (indent_level, schema_name)

    for line in lines:
        if not line.strip():
            continue

        # Calculate indent level (count leading spaces/tree chars)
        indent = len(line) - len(line.lstrip())

        # Extract schema name (remove tree characters)
        schema = re.sub(r'^[\s│└├─]+', '', line).strip()
        if not schema:
            continue

        # Remove comments (anything after ←)
        schema = schema.split('←')[0].strip()

        # Find parent at lower indent level
        while stack and stack[-1][0] >= indent:
            stack.pop()

        if stack:
            parent = stack[-1][1]
            if parent not in tree:
                tree[parent] = []
            if schema not in tree[parent]:
                tree[parent].append(schema)

        stack.append((indent, schema))

    return tree


def normalize_schema_name(name: str) -> str:
    """
    Normalize schema name from imports.

    Examples:
        "ap-no/dcat-ap-no/dcat-ap-no-schema" -> "dcat-ap-no-schema"
        "linkml:types" -> "linkml:types"
        "../fint-common/fint-common-schema" -> "fint-common-schema"
    """
    # Remove path components
    name = name.split('/')[-1]
    # Keep -schema suffix
    return name


def build_subtree(
    schema: str,
    tree: Dict[str, List[str]],
    visited: Set[str],
    direct_imports: Set[str],
    indent: int = 0
) -> List[str]:
    """
    Build ASCII subtree for a schema and its dependencies.

    Args:
        schema: Root schema name
        tree: Full hierarchy tree
        visited: Set of already visited schemas (to avoid cycles)
        direct_imports: Set of direct imports from the schema
        indent: Current indentation level

    Returns:
        List of formatted tree lines
    """
    if schema in visited:
        return []

    visited.add(schema)
    lines = []

    # Add comment for direct/transitiv import
    comment = ""
    if schema in direct_imports:
        comment = "  # direkte import"
    elif indent > 0:
        comment = "  # transitiv import"

    # Add current schema
    if indent == 0:
        lines.append(schema + comment)
    else:
        prefix = '    ' * (indent - 1) + '└── '
        lines.append(prefix + schema + comment)

    # Add children
    children = tree.get(schema, [])
    for i, child in enumerate(children):
        is_last = (i == len(children) - 1)
        child_lines = build_subtree(child, tree, visited, direct_imports, indent + 1)

        # Adjust prefix for non-last children
        if not is_last and child_lines:
            child_lines[0] = child_lines[0].replace('└── ', '├── ')
            # Add vertical bars for continuation
            for j in range(1, len(child_lines)):
                child_lines[j] = '│   ' + child_lines[j][4:]

        lines.extend(child_lines)

    return lines


def find_relevant_imports(
    imports: List[str],
    hierarchies: Dict[str, Dict[str, List[str]]]
) -> Dict[str, List[str]]:
    """
    Find which hierarchies are relevant for the given imports.

    Returns:
        Dict mapping normalized schema names to their hierarchies
    """
    normalized_imports = [normalize_schema_name(imp) for imp in imports]

    # Build flat schema -> hierarchy mapping
    schema_to_hierarchy = {}
    for domain, tree in hierarchies.items():
        for schema in tree.keys():
            schema_to_hierarchy[schema] = tree
        for children in tree.values():
            for child in children:
                schema_to_hierarchy[child] = tree

    # Find relevant trees
    relevant = {}
    for imp in normalized_imports:
        if imp in schema_to_hierarchy:
            relevant[imp] = schema_to_hierarchy[imp]

    return relevant


def filter_tree_to_targets(
    tree: Dict[str, List[str]],
    targets: Set[str]
) -> Dict[str, List[str]]:
    """
    Filter tree to only include paths that lead to target schemas.
    Includes all intermediate nodes in the path.

    Args:
        tree: Full hierarchy tree
        targets: Set of target schema names we want to reach

    Returns:
        Filtered tree containing only relevant paths
    """
    def collect_ancestors(schema: str, visited: Set[str]) -> Set[str]:
        """Collect all ancestors (parents) of a schema."""
        ancestors = set()
        if schema in visited:
            return ancestors

        visited.add(schema)

        # Find parents in tree
        for parent, children in tree.items():
            if schema in children:
                ancestors.add(parent)
                ancestors.update(collect_ancestors(parent, visited))

        return ancestors

    def has_target_descendant(schema: str, visited: Set[str]) -> bool:
        """Check if schema or any descendant is in targets."""
        if schema in targets:
            return True
        if schema in visited:
            return False

        visited.add(schema)
        children = tree.get(schema, [])
        return any(has_target_descendant(child, visited) for child in children)

    # Collect all schemas that are either:
    # 1. Target schemas
    # 2. Ancestors of target schemas
    # 3. On the path between root and target schemas
    relevant_schemas = set(targets)

    # Add all ancestors of targets
    for target in targets:
        relevant_schemas.update(collect_ancestors(target, set()))

    # Build filtered tree - include all nodes that lead to or are targets
    filtered = {}
    for parent, children in tree.items():
        if parent in relevant_schemas:
            relevant_children = [
                child for child in children
                if child in relevant_schemas or has_target_descendant(child, set())
            ]
            if relevant_children:
                filtered[parent] = relevant_children

    return filtered


def build_dependency_tree(schema_name: str, imports: List[str], direct_imports: Set[str]) -> str:
    """
    Build complete dependency tree for a schema.

    Args:
        schema_name: Name of the schema
        imports: List of imported schemas
        direct_imports: Set of direct imports (normalized schema names)

    Returns:
        ASCII tree as string
    """
    # Read importhierarki.md
    repo_root = Path(__file__).resolve().parents[3]
    hierarchy_file = repo_root / 'mkdocs' / 'docs' / 'importhierarki.md'

    if not hierarchy_file.exists():
        # Fallback to flat list
        return '\n'.join(imports)

    with open(hierarchy_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Parse all hierarchies
    hierarchies = parse_hierarchy_blocks(md_content)

    if not hierarchies:
        # Fallback to flat list
        return '\n'.join(imports)

    # Normalize imports to match hierarchy names
    normalized_imports = [normalize_schema_name(imp) for imp in imports]
    target_schemas = set(normalized_imports)

    # Find relevant hierarchies for this schema's imports
    relevant_trees = find_relevant_imports(imports, hierarchies)

    if not relevant_trees:
        # Fallback to flat list
        return '\n'.join(imports)

    # Merge all relevant trees
    merged_tree = {}
    for tree in relevant_trees.values():
        for parent, children in tree.items():
            if parent not in merged_tree:
                merged_tree[parent] = []
            for child in children:
                if child not in merged_tree[parent]:
                    merged_tree[parent].append(child)

    # Filter tree to only show paths leading to target schemas
    filtered_tree = filter_tree_to_targets(merged_tree, target_schemas)

    if not filtered_tree:
        # Fallback to flat list
        return '\n'.join(imports)

    # Find root (schema with no parent in filtered tree)
    all_schemas = set(filtered_tree.keys())
    for children in filtered_tree.values():
        all_schemas.update(children)

    children_set = set()
    for children in filtered_tree.values():
        children_set.update(children)

    roots = all_schemas - children_set

    # Build tree from each root
    all_lines = []
    visited = set()

    for root in sorted(roots):
        root_lines = build_subtree(root, filtered_tree, visited, direct_imports)
        all_lines.extend(root_lines)

    return '\n'.join(all_lines) if all_lines else '\n'.join(imports)


def main():
    if len(sys.argv) < 3:
        print("Usage: parse-dependency-tree.py <schema_name> <imports_list> [direct_imports]", file=sys.stderr)
        sys.exit(1)

    schema_name = sys.argv[1]
    imports = sys.argv[2].split()

    # Parse direct imports (normalized schema names)
    direct_imports = set()
    if len(sys.argv) > 3 and sys.argv[3]:
        direct_imports = set(sys.argv[3].split())

    tree = build_dependency_tree(schema_name, imports, direct_imports)
    print(tree)


if __name__ == '__main__':
    main()
