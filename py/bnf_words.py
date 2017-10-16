#
# Reduce words in a BNF code description to keyword versus
# formatted BNF code dictionaries
#
# Data fields:
# 1 = bnf_code_formatted
# 2 = bnf_desc
# 3 = aprroved name
#
# Dictionaries:
# 
# Starting with whole words extracted from the 2 text fields vs a list of possible keywords
# Could then: try to match partial words by sorting left / right truncations as keys.
# BNF code file data fields:
#
# TODO: Open the BNF file via file open and load as part of an initial step
#       Then: Read the medications_coding file via stdin - this will allow
#       lookups per word, per record - start with full words and see what matches.
#
# field#  What it is
# 0       Full BNF code (individual drug level).
# 1       formatted BNF code for this item - may or may not go to ch.section.subsection level
# 2       BNF description
# 3       Approved Name
# 4       ch
# 5       ch.section
# 6       ch.section.subsection (not always present)
import time
import datetime
import re
import string
import os, sys
from optparse import OptionParser

# Could use Dictionaries to express relationships? 
# (could convert to RDF triples later)
#  mapsToC = {}
#  mapsToCs = {}
#  mapsToCode = {}
#  isSubStringOf = {}

# words that are too general to try and match
general_words = {
    }

def load_bnf_words(fh):
  # words that are too common to try and match
  # these include adjectives such as colours,
  # 'the', 'a', 'it', common nouns
  common_words = {
      'cream':1,
      'product':1,
      'gel':1,
      'liquid':1,
      'oil':1,
      'ml':1,
      'spray':1,
      'powder':1,
      'co':1,
      'bio':1,
      'over':1,
      'the':1,
      'c':1,
      'vitamin':1,
      'orange':1,
      'green':1,
  }
  bnf_whole_words = {}
  bnf_part_words = {}

  hdr = sys.stdin.readline()
  for line in fh:
    data = line.strip().split(',')
    desc_words = get_normalised_sentence(data[2].lower()).split()
    for word in desc_words:
      if word not in bnf_whole_words:
        bnf_whole_words[word] = []
      if data[1] not in bnf_whole_words[word]:
        bnf_whole_words[word].append(data[1])
  return bnf_whole_words

def get_normalised_sentence(sentence):
  return re.sub(r'[\W_]', ' ', sentence)

def main(options):

  count = 0
  bnf_dict_count = 0
  # try to load the bnf codes file
  try:
    fh = open(options.bnffile, "r")
    bnf_words = load_bnf_words(fh)
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

  # stdin used to read in medications coding data
  hdr = sys.stdin.readline()
  for line in sys.stdin:
    count += 1
    data = line.strip().split('|')
    desc_words = get_normalised_sentence(data[1].lower()).split()
    for word in desc_words:
      if word in bnf_words:
        if len(bnf_words[word]) <= 2:
          print "MATCH %s:%s -> %s" % (data[0], word, str(bnf_words[word]))
        else:
          #print "COMMON %s:%s -> %s" % (data[0], word, str(bnf_words[word]))
          print "COMMON,%s,%s,%d" % (data[0], word, len(bnf_words[word]))
      else:
        print "MISS %s:%s" % (data[0], word)

  for word in bnf_words:
    bnf_dict_count += 1
    print "%s -> %s" % (word, str(bnf_words[word]))
  return count, bnf_dict_count 


# execution flow starts here
#
parser = OptionParser()
parser.add_option("-b", "--bnffile", dest="bnffile",
  help="file contains input BNF code as and descriptions", metavar="FILE")

start_time = time.time()
(options, args) = parser.parse_args()

count, bnf_dict_count = main(options)
print "END:", time.time() - start_time, "seconds", count, bnf_dict_count

