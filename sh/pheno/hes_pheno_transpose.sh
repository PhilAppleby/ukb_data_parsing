#!/bin/sh
source ${PROJROOT}/env/common
#
# Wrap the pheno/transpose_pheno_data.sh script, supplying parameters
# for hes icd10 data
#
echo "Transpose icd10 (HES)  phenotype data, eliminating empty cells"
time ${SHDIR}/pheno/transpose_pheno_data.sh hes_diagnoses_icd10_data pheno
