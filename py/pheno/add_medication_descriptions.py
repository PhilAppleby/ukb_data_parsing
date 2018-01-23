# 
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser

def load_descriptions(dfile):
  dlookup = {}
  for line in dfile:
    data = line.strip().split("|")
    dlookup[data[0]] = data[1]
  return dlookup

def main(options):
  counts = {}
  pcounts = {}
  plookup = {}
  count = 0
  try:
    fh = open(options.cfile, "r")
    dlookup = load_descriptions(fh)
  except:
    print "Failed to open medications code file %s" % (options.cfile)
    sys.exit()

  hdr = sys.stdin.readline().strip().split(",")
  hdr.append("narrative")
  print ",".join(hdr)

  for line in sys.stdin:
    data = line.strip().split(",")
    if data[1] in dlookup:
      data.append(dlookup[data[1]])
    else:
      data.append("NA")
    print ",".join(data)

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-c", "--cfile", dest="cfile",
  help="medications code file", metavar="FILE")

(options, args) = parser.parse_args()

count = main(options)
#print "END:", time.time() - start_time, "seconds", count

