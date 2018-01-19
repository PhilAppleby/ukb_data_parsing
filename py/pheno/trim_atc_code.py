#
# 
#
import time
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def main(options):
  count = 0
  dh = Datahelper()

  for line in sys.stdin:
    count += 1
    data = line.strip().split(',')
    data[2] = dh.format_atc_code(data[2], int(options.codelen))
    print ','.join(data)

  return count 

# execution flow starts here
#
start_time = time.time()

parser = OptionParser()
parser.add_option("-l", "--codelen", dest="codelen",
  help="ATC code length", metavar="INT")
(options, args) = parser.parse_args()


count = main(options)
#print "END:", time.time() - start_time, "seconds", count

