#!/usr/bin/python3
"""
Script that converts a Markdown file to HTML.
Usage: ./markdown2html.py input.md output.html
"""

import sys
import os

# Check if the number of arguments is correct
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Success
sys.exit(0)
