#!/bin/sh
source ${PROJROOT}/env/common
# Parse synonyms extracted from the chembl molecule_synonyms table 
#
# Output a file where each synonym is represented vs its other synonyms
#
cat ${CDATADIR}/synonym_list.txt | python ${PYDIR}/generate_syn_dictionary.py > ${CDATADIR}/syn_dict_all.txt
