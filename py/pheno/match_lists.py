# 
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser

def load_keys(fh):
  keys = {}

  for line in fh:
    line = line.strip()
    keys[line] = 1

  return keys

def main(options):
  count = 0
  last_molno = ""
  related_synonyms = []

  # try to load keys file
  try:
    fh = open(options.keysfile, "r")
    keys = load_keys(fh)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    print "I/O error:", sys.exc_info()
    exit()
  except TypeError as e:
    print "Missing arguments ", e
    exit()
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()

  col = 0
  if options.col != None:
    col = int(options.col)

  for line in sys.stdin:
    data = line.strip().split(',')
    if data[col] in keys:
      print line.strip()
# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-u", "--keysfile", dest="keysfile",
  help="keys for matching in main file", metavar="FILE")

parser.add_option("-c", "--col", dest="col",
  help="col in target file", metavar="INT")

(options, args) = parser.parse_args()

count = main(options)
#print "END:", time.time() - start_time, "seconds", count

