#!/bin/sh
source ${PROJROOT}/env/common
#
# override
DATADIR=/home/pda11181/data/

cat ${DATADIR}/icd10/ukb_pheno_hes_diagnoses_icd10_data.csv | python ${PYDIR}/normalise_pheno_data.py > ${DATADIR}/icd10/hes_normalised.csv
