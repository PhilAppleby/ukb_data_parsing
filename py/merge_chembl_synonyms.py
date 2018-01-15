# 
# Attempt to match CHEMBL synonyms with coding data
# - Load a synonym dictionary
# - Processing up to this point:
#   dump_mysql_table.py --tablename=molecule_synonyms > ${CDATADIR}/molecule_synonyms.tsv
#   (this outputs a file with no header, currently)   
#   sort -n ${CDATADIR}/molecule_synonyms.tsv > ${CDATADIR}/molecule_synonyms_sorted.tsv
#   
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

def load_synonyms(fh):
  """
  Load whole synonyms only into a python dictionary
  which will then be used as a look-up for input data
  """
  synonyms = {}

  for line in fh:
    data = line.strip().split('\t')
    syns1 = data[1].split('|')
    syns = [x.strip() for x in syns1]
    if data[0] not in synonyms: 
      synonyms[data[0]] = []
    for syn in syns:
      synonyms[data[0]].append(syn)

  return synonyms

def main(options):
  count = 0
  mcount = 0
  umcount = 0
  dh = Datahelper()

  try:
    fh = open(options.synfile, "r")
    synonyms = load_synonyms(fh)
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

  for line in sys.stdin:
    count += 1
    data = line.strip().split(',')
    phrase = data[1].lower()
    matched = False
    for key in dh.get_merge_key_list(phrase):
      if key in synonyms:
        print "%s,%s,%s" % (data[0], phrase, '|'.join(synonyms[key]))
        matched = True
        mcount += 1
        break
    if matched == False:
      print "%s,%s" % (data[0], phrase)

  #for syn in synonyms:
  #  print "%s -> %s" % (syn, str(synonyms[syn]))
  #  count += 1
  return count, mcount

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-s", "--synfile", dest="synfile",
  help="molecule synonyms", metavar="FILE")

(options, args) = parser.parse_args()

count, mcount = main(options)
#print "END:", time.time() - start_time, "seconds", count, mcount

