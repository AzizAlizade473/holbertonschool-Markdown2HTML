#!/usr/bin/env python3
import sys
import os

# Check number of arguments
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    exit(1)

# If all good, just exit 0 (no output required)
exit(0)
