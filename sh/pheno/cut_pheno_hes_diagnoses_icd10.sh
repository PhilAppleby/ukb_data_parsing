#!/bin/sh
source ${PROJROOT}/env/common
#
python ${PYDIR}/pheno/cut_main_csv_file.py --csvfile=${UKBDATADIR}/ukb9888.csv --colprefs=41202,41204 > \
  ${UKBPDIR}/ukb_pheno_hes_diagnoses_icd10_data.csv
