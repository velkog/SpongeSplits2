#!/bin/bash
FILE=$1
[ -z $1 ] && FILE="autosplit/app.py"
[ ! -f $FILE ] && FILE="autosplit/$FILE.py"
[ ! -f $FILE ] && >&2 echo "Error: File '$FILE' does not exist" || .win-venv/Scripts/python.exe $FILE