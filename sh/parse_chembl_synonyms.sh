#!/bin/sh
source ${PROJROOT}/env/common
# Parse synonyms extracted from the chembl molecule_synonyms table 
#
# Output a file where each synonym is represented vs its other synonyms
#
cat ${CDATADIR}/molecule_synonyms_sorted.tsv | python ${PYDIR}/parse_chembl_synonyms.py > ${CDATADIR}/synonym_list.txt
