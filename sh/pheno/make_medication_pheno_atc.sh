#!/bin/sh
source ${PROJROOT}/env/common
# 
# Run steps 10, 11a, 11b
# Phenotype generation following matching
#
echo "Step 10 - Prepare ATC data for phenotype generation"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_prep.sh
echo "Step 11a - Generate level2 phenotypes"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_level2.sh
echo "Step 11b - Generate level3 phenotypes"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_level3.sh

