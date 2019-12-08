#!/usr/bin/env bash

echo "Entrer une note comprise entre 0 et 20"

read value

re='^[0-9]+$'
if ! [[ $value =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi

if ! [[ $value -ge 0 && $value -le 20 ]] ; then
    echo "not valid number" >&2; exit 1
fi

if [ "$value" -le 5 ]; then
    echo "passable"
elif [ "$value" -le 10 ]; then
    echo "insuffisant"
elif [ "$value" -le 15 ]; then
    echo "bien"
elif [ "$value" -le 20 ]; then
    echo "excellent"
else
   echo "Unknown parameter"
fi