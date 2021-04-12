#!/bin/bash
cd "$(dirname "$0")"
# This script will generate folders and files for a new hackerrank challenge
# Usage: ./new_challenge.sh

# Execution
echo "Start of script..."

python core/challenge_generator.py

echo "End of script."