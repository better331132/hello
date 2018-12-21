#!/bin/bahs

PRE_IFS=$IFS
IFS="
"
FileName="bin_file.txt"
touch $FileName

echo "-------------------------------------------------------------------------"
for i in `ls -al /bin`
do
    S=`echo $i | awk '{print $9}'`
    F=`echo $i | awk '{print $5}'`

    if [ "$S" == "." ] || [ "$S" == ".." ] || [ "$S" == "" ]; then
        continue
    fi
    echo "$S $F" >> $FileName

done

IFS=$PRE_IFS
