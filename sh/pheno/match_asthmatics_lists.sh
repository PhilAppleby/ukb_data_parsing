#!/bin/sh
source ${PROJROOT}/env/common
MDTDIR=/home/pda11181/devel/data/ukb_medication/
#
cat ${MDTDIR}/asthmatics_list.csv | python ${PYDIR}/match_lists.py --col=1 --keysfile=${MDTDIR}/asthmatics_taking_listed_drugs.txt 
#cat ${UDATADIR}/medication_coding.csv | python ${PYDIR}/compare_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv 
