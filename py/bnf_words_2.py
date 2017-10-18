#
# Reduce words in a BNF code description to keyword versus
# formatted BNF code dictionaries
#
# Dictionaries:
# 
# Start with whole words extracted from the name field vs formatted BNF codes
# Could then: match partial words by sorting left / right truncations as keys.
#
# BNF code file data fields:
#
# field#  What it is
# 0       BNF code unformatted
# 1       BNF Name
# 
import time
import datetime
import re
import string
import os, sys
from optparse import OptionParser
# Could use Dictionaries to express relationships? 
# (could convert to RDF triples later)
#  mapsToCodes = {}
#  isSubStringOf = {}

def format_bnf_code(code):
  code = code.strip()
  ch = code[0:2]
  s = code[2:4]
  ss = '00'
  if len(code) >=6:
    ss = code[4:6]
  if ss != '00':
    return "%d.%d.%d" % (int(ch),int(s),int(ss))
  return "%d.%d" % (int(ch),int(s))

def isMeasure(word):
  """
  Check is the word is a measure - digits followed by measurement abbreviations 
  or full words
  """
  if (re.match('\d+(m*g|m*l|micrograms)$', word)) != None:
    return True
  return False

def isDigits(word):
  """
  Check is the word consists of digits only
  """
  if (re.match('^\d+', word)) != None:
    return True
  return False

def load_bnf_words(fh):
  bnf_whole_words = {}
  bnf_part_words = {}

  hdr = fh.readline()
  for line in fh:
    data = line.strip().split(',')
    fcode = format_bnf_code(data[0])
    desc_words = get_normalised_sentence(data[1].lower().strip()).split()
    for word in desc_words:
      if word not in bnf_whole_words:
        bnf_whole_words[word] = []
      if fcode not in bnf_whole_words[word]:
        bnf_whole_words[word].append(fcode)
  return bnf_whole_words

def get_normalised_sentence(sentence):
  return re.sub(r'[\W_]', ' ', sentence)

def main(options):
  # excluded words that are too common or too general
  # to try and match these include adjectives such as colours,
  # 'the', 'a', 'it', common nouns, drug delivery nouns (eg suspension,
  # tab, tablet)
  excluded_words = {
      'over': 1,
      'the': 1,
      'counter': 1,
      'a': 1,
      'it': 1,
      'to': 1,
      'other': 1,
      'fruit': 1,
      'gel': 1,
      'cream': 1,
      'solution': 1,
      'suspension': 1,
      'liquid': 1,
      'tablet': 1,
      'tablets': 1,
      'pastille': 1,
      'granules': 1,
      'mixture': 1,
      'ointment': 1,
      'capsule': 1,
      'suppository': 1,
      'pellet': 1,
      'elixir': 1,
      'drops': 1,
      'inhaler': 1,
      'sachet': 1,
      'bath': 1,
      'powder': 1,
      'solvent': 1,
      'green': 1,
      'orange': 1,
      'mint': 1,
      'x': 1,
      'r': 1,
      'vitamin': 1,
      'e': 1,
      'f': 1,
      'product': 1,
      'unknown': 1,
      'free': 1,
      'leg': 1,
      'm': 1,

  }

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
      if isMeasure(word) == True:
        print "EXCL (MEASURE) %s:%s" % (data[0], word)
        continue
      if isDigits(word) == True:
        print "EXCL (DIGITS) %s:%s" % (data[0], word)
        continue
      if word in excluded_words:
        print "EXCL (WORD) %s:%s" % (data[0], word)
        continue
      if word in bnf_words:
        if len(bnf_words[word]) <= 2:
          print "MATCH %s:%s -> %s" % (data[0], word, str(bnf_words[word]))
        else:
#          #print "COMMON %s:%s -> %s" % (data[0], word, str(bnf_words[word]))
          print "COMMON,%s,%s,%d" % (data[0], word, len(bnf_words[word]))
      else:
        print "MISS %s:%s" % (data[0], word)

  #for word in bnf_words:
  #  bnf_dict_count += 1
  #  print "%s -> %s" % (word, str(bnf_words[word]))
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

