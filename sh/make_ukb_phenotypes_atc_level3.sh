#!/bin/sh
source ${PROJROOT}/env/common
# step 1 attach  ATC phenotype identifiers (where possible) to ukb med data
# attach codes or 'NA'
echo 'step 1'
cat ${UKBPDIR}/ukb_20003_reported_medication_n.csv | python ${PYDIR}/assign_codes_to_participant_data.py --codefile=${DATADIR}/results/atc_matched_2.csv > ${UKBPDIR}/ukb_20003_with_atc_codes.csv

grep -w NA ${UKBPDIR}/ukb_20003_with_atc_codes.csv > ${UKBPDIR}/ukb_20003_with_atc_codes_unmatched.csv

grep -wv NA ${UKBPDIR}/ukb_20003_with_atc_codes.csv | sed '1,1d' > ${UKBPDIR}/ukb_20003_with_atc_codes_matched.csv

#------------------------------------------------------------------------------------------------
# For level 3
# step 2 sort to eliminate duplicates - at this stage we have level3 codes, one row per
# participant per code
echo 'step 2'
sort -u ${UKBPDIR}/ukb_20003_with_atc_codes_matched.csv > ${UKBPDIR}/ukb_20003_with_atc_codes_matched_sorted.csv

# step 3 get the list of possible phenotypes
echo 'step 3'
cut -f 3 -d ',' ${UKBPDIR}/ukb_20003_with_atc_codes_matched_sorted.csv | sort -u > ${UKBPDIR}/ukb_possible_med_phenotypes_level3.csv

# step 4 generate phenotype annotations
echo 'step 4'
cat ${UKBPDIR}/ukb_possible_med_phenotypes_level3.csv | python ${PYDIR}/atc_generate_medication_annotations.py --level=3 > ${UKBPDIR}/Anno_medications_BIN_atc_level3.csv

# step 5 generate phenotypes
echo 'step 5'
cat ${UKBPDIR}/ukb_20003_with_atc_codes_matched_sorted.csv | python ${PYDIR}/generate_medication_phenotypes.py --pfile=${UKBPDIR}/Anno_medications_BIN_atc_level3.csv > ${UKBPDIR}/med_phenotypes_level3.tsv
#------------------------------------------------------------------------------------------------
echo 'END'
