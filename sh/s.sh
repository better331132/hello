#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Input the filename, please.."
    echo "usage) ./s4.sh <file>"
    exit 0
fi

cat $1
