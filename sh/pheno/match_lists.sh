#!/bin/sh
source ${PROJROOT}/env/common
MDTDIR=/home/pda11181/devel/data/ukb_medication/
#
cat ${MDTDIR}/medication_data_asthma.txt | python ${PYDIR}/match_lists.py --keysfile=${MDTDIR}/asthmatics_list_iid_sorted.csv > ${MDTDIR}/res2.txt
#cat ${UDATADIR}/medication_coding.csv | python ${PYDIR}/compare_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv 
