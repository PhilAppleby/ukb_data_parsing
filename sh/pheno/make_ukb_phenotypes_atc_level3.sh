#!/bin/sh
source ${PROJROOT}/env/common
# For level 3
# step 1 sort to eliminate duplicates - at this stage we have level3 codes, one row per
# participant per assigned ATC code
echo 'step 1'
cat ${UKBPDIR}/ukb_20003_with_atc_codes_matched.csv | \
  python ${PYDIR}/pheno/trim_atc_code.py --codelen=4 | \
  sort -u  > ${UKBPDIR}/ukb_20003_with_atc_codes_matched_sorted_level3.csv

# step 2 get the list of possible phenotypes
echo 'step 2'
cut -f 3 -d ',' ${UKBPDIR}/ukb_20003_with_atc_codes_matched_sorted_level3.csv | \
  sort -u > ${UKBPDIR}/ukb_possible_med_phenotypes_level3.csv

# step 3 generate phenotype annotations
echo 'step 3'
cat ${UKBPDIR}/ukb_possible_med_phenotypes_level3.csv | \
  python ${PYDIR}/chembl/generate_atc_medication_annotations.py --level=3 > \
  ${UKBPDIR}/Anno_medications_BIN_atc_level3.csv

# step 4 generate phenotypes
echo 'step 4'
cat ${UKBPDIR}/ukb_20003_with_atc_codes_matched_sorted_level3.csv | \
  python ${PYDIR}/pheno/generate_medication_phenotypes.py \
  --pfile=${UKBPDIR}/Anno_medications_BIN_atc_level3.csv > \
  ${UKBPDIR}/med_phenotypes_level3.tsv
#------------------------------------------------------------------------------------------------
echo 'END'
