#
# Reduce words in a BNF code description to keyword versus
# formatted BNF code dictionaries
#
# Data fields:
# 0 = Full bnf_code
# 1 = bnf_code_formatted
# 2 = bnf_desc
# 3 = approved name
#
# Dictionaries:
# 
import time
import datetime
# import re
import os, sys
from optparse import OptionParser

def load_dictionaries(fh):
  bnf_words = {}
  return bnf_words()

def main(options):

  codes = []
  count = 0
  hdr = sys.stdin.readline()

  for line in sys.stdin:
    data = line.strip().split(',')
    print data

  return count 

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
parser.add_option("-b", "--bnffile", dest="bnffile",
  help="file contains input BNF code as and descriptions", metavar="FILE")
(options, args) = parser.parse_args()

count = main(options)
print "END:", time.time() - start_time, "seconds", count

