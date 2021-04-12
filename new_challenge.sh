#!/bin/bash
# This script will generate folders and files for a new hackerrank challenge
# Usage: ./new_challenge.sh

# Execution
echo "Start of script..."
echo "Hello! Want to work on a new challenge? Please give it a name:"

read -r challengename

mkdir -p challenges/"$challengename"

list="1 2"
languagechoice="0"
while [[ $languagechoice != @(1|2) ]]
do
  echo -e "Please choose your language:\n1) Python\n2) C#\nAnswer:"
  read -r languagechoice
done

echo $challengename $languagechoice | python core/challenge_generator.py
echo "End of script..."

