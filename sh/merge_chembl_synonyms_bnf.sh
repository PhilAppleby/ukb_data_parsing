#!/bin/sh
source ${PROJROOT}/env/common
# Merge bulk BNF data (ownership uncertain, possibly HIC) with 
# synonyms from the CHEMBL database
#
cat ${BDATADIR}/bnf_combined.csv | \
  python ${PYDIR}/merge_chembl_synonyms.py --synfile=${CDATADIR}/syn_dict_all.txt > \
  ${BDATADIR}/bnf_combined_synonyms_all.csv 
