#!/usr/bin/env python3
"""
markdown2html.py - Converts a Markdown file to HTML.

Usage:
    ./markdown2html.py input.md output.html

Supports:
    - Checks for correct number of arguments
    - Checks if input file exists
    - Converts Markdown headings (# to ######) into <h1> to <h6>
"""

import sys
import os
import re

# Check argument count
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.isfile(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    exit(1)

# Read input Markdown file and convert
converted_lines = []

with open(input_file, 'r') as md_file:
    for line in md_file:
        stripped = line.strip()
        # Match headings from # to ######
        match = re.match(r'^(#{1,6}) (.+)', stripped)
        if match:
            hashes = match.group(1)
            text = match.group(2)
            level = len(hashes)
            converted_lines.append(f"<h{level}>{text}</h{level}>\n")
        else:
            # Optionally handle non-heading lines here
            pass

# Write output HTML file
with open(output_file, 'w') as html_file:
    html_file.writelines(converted_lines)

exit(0)
