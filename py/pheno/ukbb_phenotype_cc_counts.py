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

  hdr = sys.stdin.readline().strip().split('\t')

  for i, elem in enumerate(hdr):
    print i+1, elem

  #for line in sys.stdin:
  #  pass

  return count

# execution flow starts here
#
start_time = time.time()
#parser = OptionParser()
#
#parser.add_option("-p", "--pfile", dest="pfile",
#  help="phenotype code file", metavar="FILE")

#(#options, args) = parser.parse_args()

count = main()
#print "END:", time.time() - start_time, "seconds", count

