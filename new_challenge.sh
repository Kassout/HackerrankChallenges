#!/bin/bash
# This script will generate folders and files for a new hackerrank challenge
# Usage: ./new_challenge.sh

# Function
contains() {
    [[ $2 =~ (^|[[:space:]])$1($|[[:space:]]) ]] && return 1 || return 0
}


# Execution
echo "Start of script..."
echo "Hello! Want to work on a new challenge? Please give it a name:"

read -r challengename

mkdir challenges/"$challengename"

list="1 2"
languagechoice="0"
while (contains list languagechoice)
do
  echo -e "Please choose your language:\n1) Python\n2) C#\nAnswer:"
  read languagechoice
done

echo $varname $languagechoice | python core/challenge_generator.py
echo "End of script..."

