#
# Reduce words in a BNF code description to keyword versus
# formatted BNF code dictionaries
#
# Dictionaries:
# 
# Start with whole words extracted from the name field vs formatted BNF codes
# Could then: match partial words by sorting left / right truncations as keys.
#
# Classification system code file data fields:
# 1 the code
# 2 the description
# 3 synonyms added from CHEMBL (separated by '|')
# 
import time
import datetime
import re
import string
import os, sys
from optparse import OptionParser
from datahelper import Datahelper

def main(options):
  dcount = 0
  count = 0
  match_count = 0
  miss_count = 0

  # try to load the classification system codes file
  try:
    fh = open(options.clsfile, "r")
    dh = Datahelper()
    dcount = dh.load_cls_phrases(fh)
    #print "Dictionary size = %d" % (dcount)
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

  # stdin used to read in medications coding data
  #sd = dh.get_phrase_dictionary()
  #for key in sd:
  #  print key
  hdr = sys.stdin.readline()
  for line in sys.stdin:
    count += 1
    matched = False
    data = line.strip().split(',')
    all_phrases = [data[1]]
    if len(data) == 3:
      all_phrases += data[2].split('|')

    match_string = ""
    code, match_data = dh.match_all_phrases(all_phrases)
    if code != None:
      print "%s,%s,%s,%s" % (data[0], data[1], str(match_data), code)
      match_count += 1
    else:      
      print "%s,%s,%s,%s" % (data[0], data[1], str(match_data), "NA")
      miss_count += 1

  return count, match_count, miss_count 


# execution flow starts here
#
parser = OptionParser()
parser.add_option("-b", "--clsfile", dest="clsfile",
  help="file contains input classification system codes and descriptions", metavar="FILE")

start_time = time.time()
(options, args) = parser.parse_args()

count, match_count, miss_count = main(options)
#print "END:", time.time() - start_time, "seconds", count, match_count, miss_count

