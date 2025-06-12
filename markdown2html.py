#!/usr/bin/python3
import sys
import os

# Check if exactly 2 arguments are given (script name doesn't count)
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# If everything is fine, exit successfully
sys.exit(0)
