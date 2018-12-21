#!/bin/bash

if [ $# -gt 0 ]
then
cat $1
else
    echo "파일명을 입력하세요."
fi


