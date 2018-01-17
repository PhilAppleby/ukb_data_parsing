#!/bin/sh
source ${PROJROOT}/env/common
# Post process the ATC results files
#
# differentiate between unmatched and matched data
egrep -w "NA" ${DATADIR}/results/atc_res.csv > \
	${DATADIR}/results/atc_res_NA.csv
egrep -vw "NA" ${DATADIR}/results/atc_res.csv > \
	${DATADIR}/results/atc_res_NONA.csv
# add UKBB counts to matches and unmatches
cat ${DATADIR}/results/atc_res_NA.csv | \
	python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > \
	${DATADIR}/results/atc_missing.csv
cat ${DATADIR}/results/atc_res_NONA.csv | \
	python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > \
	${DATADIR}/results/atc_matched.csv
# one_word matches are the most risky
grep ":1," ${DATADIR}/results/atc_matched.csv > \
	${DATADIR}/results/atc_one_word_match_full.csv
cut -f 1,2,3,5,6 -d ',' ${DATADIR}/results/atc_one_word_match_full.csv > \
	${DATADIR}/results/one_word_match_list.csv

# Following steps extract data for manual examination / intervention
# all matches
cut -f 1,2,8 -d ',' ${DATADIR}/results/atc_matched.csv > \
	${DATADIR}/results/atc_matched_list.csv
sort ${DATADIR}/results/atc_matched_list.csv > \
	${DATADIR}/results/atc_matched_list_sorted.csv
# looking at missing data
cut -f 1,2,8 -d ',' ${DATADIR}/results/atc_missing.csv > \
	${DATADIR}/results/atc_unmatched_list.csv
sort ${DATADIR}/results/atc_unmatched_list.csv > \
	${DATADIR}/results/atc_unmatched_list_sorted.csv
# unique matched UKBB ids
cut -f 1,2 -d ',' ${DATADIR}/results/atc_matched.csv | \
	sort -u > ${DATADIR}/results/atc_matched_unique.csv
cut -f 1,2 -d ',' ${DATADIR}/results/atc_matched.csv | \
	sort | \
	uniq -c | \
	sort -nr > ${DATADIR}/results/atc_match_counts.csv

