# 
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser

def load_synonyms(fh):
  synonyms = {}

  for line in fh:
    keyval = line.strip().split(',')
    syns1 = keyval[1].split('|')
    syns = [x.strip() for x in syns1]
    synonyms[keyval[0]] = syns

  return synonyms

def main(options):
  count = 0
  mcount = 0

  try:
    fh = open(options.synfile, "r")
    synonyms = load_synonyms(fh)
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
    if phrase in synonyms:
      if len(phrase) > 1:
        print "%s,%s,%s" % (data[0], phrase, '|'.join(synonyms[phrase]))
        #print "MATCH ALL %s,%s,%s" % (data[0], phrase, str(synonyms[phrase]))
        mcount += 1
        continue
    words = phrase.split()
    if len(words) > 1:
      bigram = ' '.join(words[0:2])
      if bigram in synonyms:
        print "%s,%s,%s" % (data[0], phrase, '|'.join(synonyms[bigram]))
        #print "MATCH TWO %s,%s,%s,%s" % (data[0], bigram, phrase, str(synonyms[bigram]))
        mcount += 1
        continue
    word_match = False
    for word in words:
      if word in synonyms:
        print "%s,%s,%s" % (data[0], phrase, '|'.join(synonyms[word]))
        #print "MATCH SGL %s,%s,%s,%s" % (data[0], word, phrase, str(synonyms[word]))
        mcount += 1
        word_match = True
        continue
    if word_match == False:
      print "%s,%s" % (data[0], phrase)
    #print "MISS %s,%s" % (data[0], phrase)


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

