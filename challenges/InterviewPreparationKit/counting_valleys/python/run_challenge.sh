#!/bin/bash
cd "$(dirname "$0")"
# This script will generate folders and files for a new hackerrank challenge
# Usage: ./run_challenge.sh

# Execution
echo "Start of script..."

if [ ! -d "output" ];
then
  mkdir "output"
fi

FILES="data/output/*"
for file in $FILES; do
  NEW_FILE=output/"${file##*/}"
  if [ ! -d "$NEW_FILE" ];
  then
    echo > "$NEW_FILE"
  fi

  export "OUTPUT_PATH=$NEW_FILE"
  FILE_CONTENT=$(<"${file//output/input}")
  echo "$FILE_CONTENT" | python counting_valleys.py
done

python tests/test_counting_valleys.py

echo "End of script."