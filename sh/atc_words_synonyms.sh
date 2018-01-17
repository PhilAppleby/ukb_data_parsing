#!/bin/sh
source ${PROJROOT}/env/common
#
#   CHEMBL synonyms have been attached to both ATC classification data
#   and UKB coding data 
#   This is the main match process - the result file contains code matches
# 
#
cat ${UDATADIR}/medication_coding_synonyms.csv | \
	python ${PYDIR}/dt_match.py --clsfile=${CDATADIR}/atc_who_desc_synonyms.csv > \
	${DATADIR}/results/atc_res.csv
