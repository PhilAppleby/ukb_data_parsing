# 
# 
import time
import datetime
import os, sys

def main():
  length_counts = {}
  full_match_count = 0
  rcount = 0

  hdr = sys.stdin.readline()

  for line in sys.stdin:
    data = line.strip().split(',')
    lgth = len(data)
    length_counts[lgth] = length_counts.get(lgth, 0) + 1
    if lgth == 2:
      print line.strip()
    rcount += 1

  #for count in length_counts:
  #  print count, length_counts[count]
  #print rcount
# execution flow starts here
#
start_time = time.time()
#

count = main()
#print "END:", time.time() - start_time, "seconds", count

