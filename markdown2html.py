#!/usr/bin/env python3
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

# Read the Markdown content and write to the output file (basic copy here)
with open(input_file, 'r') as md_file:
    content = md_file.read()

# For now, just output raw content (no conversion specified in the prompt)
with open(output_file, 'w') as html_file:
    html_file.write(content)

# Exit successfully
exit(0)

