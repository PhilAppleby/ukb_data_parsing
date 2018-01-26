# 
# 
import time
import datetime
import os, sys

def main():
  length_counts = {}
  full_match_count = 0
  rcount = 0

  for line in sys.stdin:
    data = line.strip().split(',')
    rcount += 1
    if data[1] == data[2]:
      full_match_count += 1
      continue
    words = data[2].split()
    lgth = len(words)
    length_counts[lgth] = length_counts.get(lgth, 0) + 1

  print full_match_count

  for count in length_counts:
    print count, length_counts[count]
  print rcount
# execution flow starts here
#
start_time = time.time()
#

count = main()
#print "END:", time.time() - start_time, "seconds", count

