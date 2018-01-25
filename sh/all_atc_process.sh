e!/bin/sh
source ${PROJROOT}/env/common
#
# All steps to run through data preparation, ATC and UKBB data synonym merging,
# UKB medication data matching and preparation and generation of phenotypes
#
# case 2:
# All ATC codes and descriptions:
# UKBB side - has synonyms
# ATC side - has synonyms
#
#
echo "Step 1 - Get ATC classification data from the CHEMBL Db"
time ${SHDIR}/chembl/get_chembl_atc_classification_data.sh
echo "Step 2 - Preprocess ATC classification data"
time ${SHDIR}/preprocess_atc_data.sh
echo "Step 3 - Get and reorganise CHEMBL molecule synonyms"
time ${SHDIR}/get_molecule_synonyms.sh
echo "Step 4 - Merge CHEMBL molecule synonyms and ATC classification data"
time ${SHDIR}/merge_chembl_synonyms_atc.sh
echo "Step 5 - Merge CHEMBL molecule synonyms and UKB self-reported medication data"
time ${SHDIR}/merge_chembl_synonyms_ukbb.sh
echo "Step 6 - The main matching step - attempt to assign ATC level3 codes to UKBB data"
time ${SHDIR}/atc_words_synonyms.sh
echo "Step 7 - Post process match / mismatch data to format for manual intervention and phenotype generation"
time ${SHDIR}/atc_post_process_match_data.sh
echo "Step 8 - Extract phenotype information from the UKBB main phenotype file - \
  information only run in the US"
#time ${SHDIR}/pheno/medication_pheno_extract.sh
echo "Step 9 - Transpose extracted phenotype data"
time ${SHDIR}/pheno/medication_pheno_transpose.sh
echo "Step 10 - Prepare ATC data for phenotype generation"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_prep.sh
echo "Step 11a - Generate level2 phenotypes"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_level2.sh
echo "Step 11b - Generate level3 phenotypes"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_level3.sh
