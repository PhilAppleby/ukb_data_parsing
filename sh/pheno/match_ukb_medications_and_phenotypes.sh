#!/bin/sh
source ${PROJROOT}/env/common
# All steps to run through med data extraction for a group of medicines
#
# must supply arg1 (name for condition)
if [[ $# -ne 1 ]] ; then
  echo 'Must supply condition name'
  exit 1
fi
cat ${MDATADIR}/${1}/participant_list.csv | python ${PYDIR}/match_lists.py --col=1 --keysfile=${MDATADIR}/${1}/all_participants_taking_listed_drugs.txt > ${MDATADIR}/${1}/participants_taking_drugs_from_list.csv
