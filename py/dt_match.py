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
  count = 0
  match_count = 0
  miss_count = 0

  # try to load the classification system codes file
  try:
    fh = open(options.clsfile, "r")
    dh = Datahelper()
    cls_words = dh.load_cls_words(fh)
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
  hdr = sys.stdin.readline()
  for line in sys.stdin:
    count += 1
    data = line.strip().split('|')
    desc_words = dh.get_normalised_sentence(data[1].lower()).split()
    ngram = ""
    code = None
    if len(desc_words) > 2:
      ngram = ' '.join(desc_words[0:3])
      if ngram in cls_words:
        code = dh.get_most_common(cls_words[ngram])
    if len(desc_words) > 1 and code == None:
      ngram = ' '.join(desc_words[0:2])
      if ngram in cls_words:
        code = dh.get_most_common(cls_words[ngram])
    if code == None:
      for ngram in desc_words:
        if (dh.isExcludedWord(ngram) != True) and dh.isMeasure(ngram) != True and dh.isSingleLetter(ngram) != True:
          if ngram in cls_words:
            code = dh.get_most_common(cls_words[ngram])
            break
    if code != None:
      #print "%s,%s,%s,%s,%s" % (data[0], data[1], ngram, code, str(cls_lookup[code]))
      print "%s,%s,%s,%s" % (data[0], data[1], ngram, code)
      match_count += 1
    else:
      print "%s,%s,%s,%s" % (data[0], data[1], ngram, "NA")
      miss_count += 1

  #for word in cls_words:
  #  cls_dict_count += 1
  #  print "%s -> %s" % (word, str(cls_words[word]))
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

