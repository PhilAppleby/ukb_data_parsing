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

def load_cs_codes(fh):
  code_lookup = {}

  for line in fh:
    data = line.strip().split(',')
    code_lookup[data[0]] = data[4]

  return code_lookup

def main(options):
  count = 0
  match_count = 0
  miss_count = 0
  dh = Datahelper()

  try:
    fh = open(options.codefile, "r")
    code_lookup = load_cs_codes(fh)
    #print len(synonyms)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    exit()
  except TypeError as e:
    print "Missing arguments ", e
    exit()
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()

  hdr = sys.stdin.readline().strip()
  print "%s,%s" % (hdr, "cs_code")

  for line in sys.stdin:
    count += 1
    data = line.strip().split(',')
    if data[1] in code_lookup:
      data.append(code_lookup[data[1]])
      match_count += 1
    else:
      data.append("NA")
      miss_count += 1
    print ",".join(data)

  return count, match_count, miss_count

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-c", "--codefile", dest="codefile",
  help="UKBB vs CS code file", metavar="FILE")

(options, args) = parser.parse_args()

count, ycount, ncount = main(options)
#print "END:", time.time() - start_time, "seconds", count, ycount, ncount
