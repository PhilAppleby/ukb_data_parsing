#!/bin/sh
source ${PROJROOT}/env/common

cat ${UKBPDIR}/ukb_20003_reported_medication_n.csv | python ${PYDIR}/pheno/assign_codes_to_participant_data.py --codefile=${DATADIR}/results/atc_matched_2.csv
