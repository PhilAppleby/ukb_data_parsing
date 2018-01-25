#!/bin/sh
#
source ${PROJROOT}/env/common
#
# G56 Mononeuropathies of upper limb
# G57 Mononeuropathies of lower limb
# G58 Other mononeuropathies
# G59 Mononeuropathy in diseases classified elsewhere
#
egrep "G56|G57|G58|G59" ${UKBPDIR}/ukb_pheno_hes_diagnoses_icd10_data_n.csv > \
  ${PDATADIR}/neuropathy/participant_codes_list.csv
#
cut -f 1 -d',' ${PDATADIR}/neuropathy/participant_codes_list.csv | \
  sort -u > \
  ${PDATADIR}/neuropathy/participant_list.csv
# Get the list of participants having taken medications from the med_list.txt in 
# the neuropathy directory
${SHDIR}/pheno/match_icd10_list_vs_medications.sh neuropathy
