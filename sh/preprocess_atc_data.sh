#!/bin/sh
source ${PROJROOT}/env/common
#
# Preprocess the ATC classification data to cut the relevant columns
# Executed twice to capture both molregno and description
# Then to trim the ATC code to the required length (level3)
#
gawk -F '\t' '{print $2 "," $3}' ${CDATADIR}/atc_classification_molregno.tsv | \
	grep -v None > ${CDATADIR}/atc_who_desc_fullcode.csv
gawk -F '\t' '{print $2 "," $1}' ${CDATADIR}/atc_classification_molregno.tsv >> \
	${CDATADIR}/atc_who_desc_fullcode.csv
cat ${CDATADIR}/atc_who_desc_fullcode.csv | \
	python ${PYDIR}/atc_parse.py --codelen=4 > ${CDATADIR}/atc_who_desc.csv
