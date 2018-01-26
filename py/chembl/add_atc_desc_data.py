import time
import pymysql
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def main():

  dh = Datahelper()
  try:
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()


  count = 0
  for line in sys.stdin:
    data = line.strip().split(',')
    atc_code = data[0]
    query = "select level1_description, level2_description, level3_description from atc_classification where level3 = '%s' limit 1" % (atc_code)
    count = 0
  
    with chembl.cursor() as cursor:
      cursor.execute(query)
      for row in cursor:
        count += 1
        descr = row[0].lower() + ": " + dh.get_normalised_phrase(row[1].lower() + " " + row[2].lower())
        data.append(descr)
        print ','.join(data)

  chembl.close()
  return count

# execution flow starts here
#
start_time = time.time()

rcount = main()
#print "END:", time.time() - start_time, "seconds", rcount
