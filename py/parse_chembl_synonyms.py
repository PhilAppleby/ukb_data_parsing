# 
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser

def main():
  count = 0
  last_molno = ""
  related_synonyms = []

  for line in sys.stdin:
    data = line.strip().split('\t')
#    print data
    if data[0] != last_molno and last_molno != "":
      print '|'.join(related_synonyms)
      related_synonyms = []
    last_molno = data[0]
    text = data[1].lower()
    stype = data[2]
    syn = stype + ":" + text
    if syn not in related_synonyms:
      related_synonyms.append(syn)

  print '|'.join(related_synonyms)
# execution flow starts here
#
start_time = time.time()
#parser = OptionParser()
#
#parser.add_option("-c", "--cfile", dest="cfile",
#  help="medications code file", metavar="FILE")

#(options, args) = parser.parse_args()

count = main()
#print "END:", time.time() - start_time, "seconds", count
