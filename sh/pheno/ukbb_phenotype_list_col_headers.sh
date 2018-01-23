#!/bin/sh
source ${PROJROOT}/env/common
#
cat ${UKBPDIR}/all_pheno/UKB9888.BIN.20171206.txt | python ${PYDIR}/all_pheno/ukbb_phenotype_list_col_headers.py 
