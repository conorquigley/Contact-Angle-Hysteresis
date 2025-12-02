#!/usr/bin/env python3
import os
import re

# Path to the boundary file
boundary_file = "constant/polyMesh/boundary"

if not os.path.exists(boundary_file):
    print(f"Boundary file not found: {boundary_file}")
    exit(1)

with open(boundary_file, "r") as f:
    content = f.read()

# Function to replace the type line in the axis block and add inGroups
def replace_axis_block(match):
    block = match.group(0)
    # Match the indentation of the type line
    def repl_type_line(m):
        indent = m.group(1)
        return f"{indent}type            empty;\n{indent}inGroups        1(empty);"
    # Replace only the type patch line
    block = re.sub(r"(^\s*)type\s+patch\s*;", repl_type_line, block, flags=re.MULTILINE)
    return block

# Regex to match the entire axis block
pattern = re.compile(r"(    axis\s*\{[^}]*?\})", re.DOTALL)

new_content, n_replacements = re.subn(pattern, replace_axis_block, content)

if n_replacements > 0:
    with open(boundary_file, "w") as f:
        f.write(new_content)
    print(f"Updated '{boundary_file}' successfully.")
else:
    print(f"No matching 'axis' block found in '{boundary_file}'.")
