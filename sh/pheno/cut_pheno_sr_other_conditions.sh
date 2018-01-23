#!/bin/sh
source /home/pda11181/devel/ukb_data_parsing/env/common
# Match words in medication_coding.tsv (The UKBB site has tis as coding4.tsv - download link
# was http://biobank.ctsu.ox.ac.uk/showcase/coding.cgi?id=4 as at 20171019
#
#python ${PYDIR}/cut_main_csv_file.py --csvfile=${UKBDATADIR}/ukb9888.csv --colprefs=20002 > /home/pda11181/devel/data/ukb_other_condition_data.csv
python ${PYDIR}/cut_main_csv_file.py --csvfile=${UKBDATADIR}/ukb9888.csv --colprefs=20002,87,135 > /home/pda11181/devel/data/ukb_other_condition_data.csv
