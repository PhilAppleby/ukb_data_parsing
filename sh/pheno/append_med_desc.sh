#!/bin/sh
source ${PROJROOT}/env/common
MDTDIR=/home/pda11181/devel/data/medication/
#
cat ${MDTDIR}/neuropathy/initial_matches.csv | python ${PYDIR}/append_med_desc.py --col=1 --descfile=${UDATADIR}/medication_coding.csv
