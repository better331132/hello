#!/bin/bash

if [ $# -eq 0 ]
then
    echo "파일명을 입력하세요"
    exit 0
fi
DATE=`date +%Y-%m-%d`
mv $1 ${DATE}.txt
