#!/bin/sh
source ${PROJROOT}/env/common
# Only runnable against the single read-only copy of the UKB Phenotype data
#
# must supply arg1, arg2 only (descriptive name and column prefix)
if [[ $# -ne 2 ]] ; then
    echo 'must supply arg1, arg2 only (descriptive name and column prefix)'
    exit 1
fi
python ${PYDIR}/pheno/cut_main_csv_file.py --csvfile=${UKBDATADIR}/ukb9888.csv --colprefs=${2} > ${UKBPDIR}/ukb_${2}_${1}.csv
