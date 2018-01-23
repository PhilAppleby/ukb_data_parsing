#!/bin/sh
source ${PROJROOT}/env/common
# The Match steps:
# ATC and UKBB data synonym merging,
#
# All ATC codes and descriptions:
# UKBB side - has synonyms
# ATC side - has synonyms
#
#
echo "Step 4 - Merge CHEMBL molecule synonyms and ATC classification data"
time ${SHDIR}/merge_chembl_synonyms_atc.sh
echo "Step 5 - Merge CHEMBL molecule synonyms and UKB self-reported medication data"
time ${SHDIR}/merge_chembl_synonyms_ukbb.sh
echo "Step 6 - The main matching step - attempt to assign ATC level3 codes to UKBB data"
time ${SHDIR}/atc_words_synonyms.sh
echo "Step 7 - Post process match / mismatch data to format for manual intervention and phenotype generation"
time ${SHDIR}/atc_post_process_match_data.sh

# Main output files at the end of each step:

# 4) ${CDATADIR}/atc_who_desc_synonyms.csv

# 5) ${UDATADIR}/medication_coding_synonyms.csv

# 6) ${DATADIR}/results/atc_res.csv

# 7) ${DATADIR}/results/atc_matched.csv and ${DATADIR}/results/atc_missing.csv (which is then used to assign manual matches) 
