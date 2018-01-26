# 
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser
from datahelper import Datahelper

def main():
  count = 0
  last_molno = ""
  related_synonyms = []
  dh = Datahelper()

  for line in sys.stdin:
    data = line.strip().split('\t')
    print "%s\t%s" % (data[1], data[0])

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

