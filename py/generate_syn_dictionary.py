# 
# 
import time
import datetime
import re
import os, sys
import random
import json

def main():
  count = 0
  synonyms = {}
  #codes = {}

  for line in sys.stdin:
    data = line.strip().split(',')
    type_syns = data[0].split('|')
    syns = [x.split(':')[1].strip() for x in type_syns]
    for syn in syns:
      if syn not in synonyms:
        synonyms[syn] = [] 
        #codes[syn] = []
      #if data[1] not in codes[syn]:
      #  codes[syn].append(data[1])
      for altsyn in syns:
        if altsyn not in synonyms[syn]:
          synonyms[syn].append(altsyn)
        

  for syn in synonyms:
    #print "%s\t%s\t%s" % (syn, '|'.join(synonyms[syn]), '|'.join(codes[syn]))
    print "%s\t%s" % (syn, '|'.join(synonyms[syn]))
    count += 1
  return count

# execution flow starts here
#
start_time = time.time()
count = main()
#print "END:", time.time() - start_time, "seconds", count

