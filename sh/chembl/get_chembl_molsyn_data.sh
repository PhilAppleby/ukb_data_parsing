#!/bin/sh
source ${PROJROOT}/env/common
# Get synonyms from the CHEMBL 
# atc_classification, molecule_atc_classification and molecule_synonyms tables 
#
python ${PYDIR}/chembl/get_molecule_synonyms.py > ${CDATADIR}/molecule_synonyms_with_atc_data.tsv 
