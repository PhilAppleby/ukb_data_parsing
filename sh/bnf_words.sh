#!/bin/sh
export DATADIR=${PROJROOT}/ukb/data
export PYDIR=${PROJROOT}/ukb/py

cat ${DATADIR}/medication_coding.tsv | python ${PYDIR}/bnf_words.py --bnffile=${DATADIR}/bnf_data_formatted.csv
