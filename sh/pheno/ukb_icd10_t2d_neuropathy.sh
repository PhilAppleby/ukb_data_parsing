#!/bin/sh
#
source ${PROJROOT}/env/common
#
# E11 Non-insulin-dependent diabetes mellitus
#
echo "Get t2d diagnosed participants from the ICD10 (HES) extract\
 and make a list of unique ptcpt ids" 
egrep "E11" ${UKBPDIR}/ukb_pheno_hes_diagnoses_icd10_data_n.csv > \
  ${PDATADIR}/t2d/participant_codes_list.csv
#
cut -f 1 -d',' ${PDATADIR}/t2d/participant_codes_list.csv | \
  sort -u > \
  ${PDATADIR}/t2d/participant_list.csv
# -----------------------------------------------------------------
echo "Get a list of ALL participants taking NP drugs" 
# -----------------------------------------------------------------
cut -f 1 -d ',' ${MDATADIR}/t2d/med_list.txt > \
  ${MDATADIR}/t2d/med_list_codes.txt

# grep_from_file.sh is a simple 
#!/bin/sh
# source ${PROJROOT}/env/common
#
# while read term
# do
#       grep $term $2
# done < $1
${SHDIR}/pheno/grep_from_file.sh ${MDATADIR}/t2d/med_list_codes.txt \
  ${UKBPDIR}/ukb_20003_reported_medication_n.csv > \
  ${MDATADIR}/t2d/all_medication_data.csv

cut -f 1 -d ',' ${MDATADIR}/t2d/all_medication_data.csv | \
  sort -u > \
  ${MDATADIR}/t2d/all_participants_taking_np_drugs.txt

# -----------------------------------------------------------------
echo "Set operations via 'comm' - t2d ptcpts taking np drugs and\
 all ptcpts taking np drugs" 
# -----------------------------------------------------------------
comm -12 ${MDATADIR}/t2d/participant_list.csv \
  ${MDATADIR}/t2d/all_participants_taking_np_drugs.txt > \
  ${MDATADIR}/t2d/cases.txt
comm -23 ${MDATADIR}/t2d/participant_list.csv \
  ${MDATADIR}/t2d/all_participants_taking_np_drugs.txt > \
  ${MDATADIR}/t2d/candidate_controls.txt
# -----------------------------------------------------------------
echo "Get a list of ALL participants taking the 'other' NP drugs" 
# -----------------------------------------------------------------
cut -f 1 -d ',' ${MDATADIR}/t2d_excluded/med_list.txt > \
  ${MDATADIR}/t2d_excluded/med_list_codes.txt

# grep_from_file.sh is a simple 
#!/bin/sh
# source ${PROJROOT}/env/common
#
# while read term
# do
#       grep $term $2
# done < $1
${SHDIR}/pheno/grep_from_file.sh ${MDATADIR}/t2d_excluded/med_list_codes.txt \
  ${UKBPDIR}/ukb_20003_reported_medication_n.csv > \
  ${MDATADIR}/t2d_excluded/all_medication_data.csv

cut -f 1 -d ',' ${MDATADIR}/t2d_excluded/all_medication_data.csv | \
  sort -u > \
  ${MDATADIR}/t2d_excluded/all_participants_taking_np_excl_drugs.txt
# -----------------------------------------------------------------
echo "Set operation via 'comm' - eliminate candidate controls taking\
 excluded drugs"
# -----------------------------------------------------------------
comm -23 ${MDATADIR}/t2d/candidate_controls.txt \
  ${MDATADIR}/t2d_excluded/all_participants_taking_np_excl_drugs.txt > \
  ${MDATADIR}/t2d/controls.txt
# -----------------------------------------------------------------
echo "Build a Binary phenotype file (cases=1, controls=0)"
# -----------------------------------------------------------------
echo -e "FID\tIID\tT2D_with_neuropathy" > ${MDATADIR}/t2d/phenotypes.tsv
perl -pe 's/(\d+)/$1\t$1\t0/g' ${MDATADIR}/t2d/controls.txt >> ${MDATADIR}/t2d/phenotypes.tsv
perl -pe 's/(\d+)/$1\t$1\t1/g' ${MDATADIR}/t2d/cases.txt >> ${MDATADIR}/t2d/phenotypes.tsv








