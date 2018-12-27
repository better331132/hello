#!/bin/bash

if [ $# -le 1 ]
then
    echo "파일명을 2개 입력하세요"
    echo "usage)~/s5_3.sh <file-name1> <file-name2>"
else
DATE=`date +%Y-%m-%d -d '1 day ago'`
    cat $1 >> ${DATE}.log
    cat $2 >> ${DATE}.log
fi
cat ${DATE}.log
