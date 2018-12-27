#!/bin/bash


for i in {2..19}
do
    for j in {1..19}
    do
        echo "$i X $j = $(( $i*$j ))"
    done
done
