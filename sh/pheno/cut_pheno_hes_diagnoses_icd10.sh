#!/bin/sh
source /home/pda11181/devel/ukb_data_parsing/env/common
#
python ${PYDIR}/cut_main_csv_file.py --csvfile=${UKBDATADIR}/ukb9888.csv --colprefs=41202,41204 > \
  ${LOCDATADIR}/ukb_pheno_hes_diagnoses_icd10_data.csv
