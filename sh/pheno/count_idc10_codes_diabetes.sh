#!/bin/sh
source ${PROJROOT}/env/common
#
# In directory ${UKBPDIR}
#
# count instances of codes beginning E11 (Non-Insulin dependent Diabetes = T2D
grep E11  ukb_pheno_hes_diagnoses_icd10_data_n.csv | cut -f 2 -d ',' | sort | uniq -c
# Results
#     98 E110
#    181 E111
#    340 E112
#   1631 E113
#    661 E114
#    491 E115
#    132 E116
#      8 E117
#     80 E118
#  24267 E119

# Total
grep E11 ukb_pheno_hes_diagnoses_icd10_data_n.csv | sort -nu | wc -l
# Total: 24146



# count instances of codes beginning E10
grep E10  ukb_pheno_hes_diagnoses_icd10_data_n.csv | cut -f 2 -d ',' | sort | uniq -c
# Results
#     50 E100
#    358 E101
#    128 E102
#    751 E103
#    233 E104
#    173 E105
#     55 E106
#     17 E107
#     54 E108
#   3611 E109
grep E10 ukb_pheno_hes_diagnoses_icd10_data_n.csv | sort -nu | wc -l
# Total: 3644


