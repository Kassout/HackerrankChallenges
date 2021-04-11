#!/bin/bash
# This script will generate folders and files for a new hackerrank challenge
# Usage: ./new_test.sh

echo Hello! Want to work on a new challenge? Please give it a name:

read -r challengename

mkdir challenges/"$challengename"

echo -e "Please choose your language:\n1) Python\n2) C#\nAnswer:"

read -r languagechoice

echo $varname $languagechoice | python core/challenge_generator.py