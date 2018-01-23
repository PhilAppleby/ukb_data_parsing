#!/bin/sh
source ${PROJROOT}/env/common
# All steps to run through med data extraction for a group of medicines
#
# must supply arg1 (name for condition)
if [[ $# -ne 1 ]] ; then
  echo 'Must supply condition name'
  exit 1
fi
echo $1
echo ${MDATADIR}/${1}/participant_list.txt
cat ${MDATADIR}/medication_data_normalised.csv | python ${PYDIR}/match_lists.py --col=0 --keysfile=${MDATADIR}/${1}/participant_list.csv > ${MDATADIR}/${1}/initial_matches.csv
