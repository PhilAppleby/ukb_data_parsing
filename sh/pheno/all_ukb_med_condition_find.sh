#!/bin/sh
source ${PROJROOT}/env/common
# All steps to run through med data extraction for a group of medicines
#
# must supply arg1 (name for condition)
if [[ $# -ne 1 ]] ; then
  echo 'Must supply drug group / disease area name'
  exit 1
fi
cut -f 1 -d ',' ${MDATADIR}/${1}/med_list.txt > ${MDATADIR}/${1}/med_list_codes.txt

${SHDIR}/pheno/grep_from_file.sh ${MDATADIR}/${1}/med_list_codes.txt \
  ${UKBPDIR}/ukb_20003_reported_medication_n.csv > \
  ${MDATADIR}/${1}/all_medication_data.csv

cut -f 1 -d ',' ${MDATADIR}/${1}/all_medication_data.csv | \
  sort -u > \
  ${MDATADIR}/${1}/all_participants_taking_listed_drugs.txt
