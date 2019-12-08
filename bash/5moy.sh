#!/usr/bin/env bash

re='^[0-9]+$'
sum=0
count=0
while [ true ]
do
    echo "Entrer une note comprise en 0 et 20. q pour quitter."
    read value
    if [ $value = 'q' ] ; then
        break;
    fi
    if ! [[ $value =~ $re ]] ; then
    echo "error: Not a number" >&2; continue
    else
        if ! [[ $value -ge 0 && $value -le 20 ]] ; then
        echo "not valid number" >&2; continue
        else
            count=$(($count + 1))
            sum=$(($value + $sum))
        fi
    fi
done

echo "La moyenne est de : $(($sum / $count))"