#!/bin/sh
source ${PROJROOT}/env/common
# Post process the ATC results files
#
# differentiate between unmatched and matched data
egrep -w "NA" ${DATADIR}/results/atc_res_${1}.csv > ${DATADIR}/results/atc_res_${1}_NA.csv
egrep -vw "NA" ${DATADIR}/results/atc_res_${1}.csv > ${DATADIR}/results/atc_res_${1}_NONA.csv
# add UKBB counts to matches and unmatches
cat ${DATADIR}/results/atc_res_${1}_NA.csv | python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > ${DATADIR}/results/atc_missing_${1}.csv
cat ${DATADIR}/results/atc_res_${1}_NONA.csv | python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > ${DATADIR}/results/atc_matched_${1}.csv
# one_word matches are the most risky
grep ":1," ${DATADIR}/results/atc_matched_${1}.csv > ${DATADIR}/results/atc_one_word_match_full_${1}.csv
cut -f 1,2,3,5,6 -d ',' ${DATADIR}/results/atc_one_word_match_full_${1}.csv > ${DATADIR}/results/one_word_match_list_${1}.csv

# all matches
cut -f 1,2,8 -d ',' ${DATADIR}/results/atc_matched_${1}.csv > ${DATADIR}/results/atc_matched_list_${1}.csv
sort ${DATADIR}/results/atc_matched_list_${1}.csv > ${DATADIR}/results/atc_matched_list_${1}_sorted.csv
# looking at missing data
cut -f 1,2,8 -d ',' ${DATADIR}/results/atc_missing_${1}.csv > ${DATADIR}/results/atc_unmatched_list_${1}.csv
sort ${DATADIR}/results/atc_unmatched_list_${1}.csv > ${DATADIR}/results/atc_unmatched_list_${1}_sorted.csv
# unique matched UKBB ids
cut -f 1,2 -d ',' ${DATADIR}/results/atc_matched_${1}.csv | sort -u > ${DATADIR}/results/atc_matched_unique_${1}.csv
cut -f 1,2 -d ',' ${DATADIR}/results/atc_matched_${1}.csv | sort | uniq -c | sort -nr > ${DATADIR}/results/atc_match_counts_${1}.csv

