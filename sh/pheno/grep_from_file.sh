#!/bin/sh
source ${PROJROOT}/env/common

while read term
do
    grep $term $2
done < $1
