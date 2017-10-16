#!/bin/sh
export DATADIR=${PROJROOT}/data/ukb/pheno
export PYDIR=${PROJROOT}/devel/HIC.Genomics/ukb/py

python ${PYDIR}/cut_main_csv_file.py --csvfile=${DATADIR}/ukb7002.csv --colprefs=137,20027,20003 > ${DATADIR}/medications_data.csv
