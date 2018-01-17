#!/bin/sh
source ${PROJROOT}/env/common
# 
# Merge (attach) chembl synonyms with atc classification data - both originally 
# extracted from the CHEMBL database
# 
#
cat ${CDATADIR}/atc_who_desc.csv | \
  python ${PYDIR}/merge_chembl_synonyms.py --synfile=${CDATADIR}/syn_dict_all.txt > \
  ${CDATADIR}/atc_who_desc_synonyms.csv 
