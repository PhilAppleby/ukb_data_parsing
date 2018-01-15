# 
# Third step in the chembl synonym generation pipeline:
# python ${PYDIR}/dump_mysql_table_data.py --tablename=molecule_synonyms | sort -n | python ${PYDIR}/parse_chembl_synonyms.py | python ${PYDIR}/generate_syn_dictionary.py > ${CDATADIR}/syn_dict_all.txt
# 
import time
import datetime
import re
import os, sys
import random
import json

def main():
  """
  For each synonym set of size n (record) in the input: generate n records in
  which each synonym is the key.

  But special cases need handling:
  Achieved by building an internal dictionary which allows for synonyms apprearing in more
  than 1 input record (In CHEMBL terms allows for > 1 molregno having the same synonym in its
  synonym set)
  """
  count = 0
  synonyms = {}
  #codes = {}

  for line in sys.stdin:
    data = line.strip().split(',')
    type_syns = data[0].split('|')
    syns = [x.split(':')[1].strip() for x in type_syns]
    for syn in syns:
      if syn not in synonyms:
        synonyms[syn] = [] 
        #codes[syn] = []
      #if data[1] not in codes[syn]:
      #  codes[syn].append(data[1])
      for altsyn in syns:
        if altsyn not in synonyms[syn]:
          synonyms[syn].append(altsyn)
        

  for syn in sorted(synonyms):
    #print "%s\t%s\t%s" % (syn, '|'.join(synonyms[syn]), '|'.join(codes[syn]))
    print "%s\t%s" % (syn, '|'.join(set(synonyms[syn])))
    count += 1
  return count

# execution flow starts here
#
start_time = time.time()
count = main()
#print "END:", time.time() - start_time, "seconds", count

