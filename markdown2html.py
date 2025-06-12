#!/usr/bin/env python3
"""
markdown2html.py - Converts a Markdown file to HTML.

Usage:
    ./markdown2html.py input.md output.html

Checks:
    - Prints usage if arguments are missing.
    - Prints error if input file does not exist.
    - Exits silently with 0 if conversion succeeds.
"""

import sys
import os

# Check for the correct number of arguments
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.isfile(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    exit(1)

# Read the Markdown content and write to the output file
with open(input_file, 'r') as md_file:
    content = md_file.read()

# Just copy content to HTML file for now
with open(output_file, 'w') as html_file:
    html_file.write(content)

exit(0)
