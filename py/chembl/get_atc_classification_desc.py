import time
import pymysql
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def main():

  dh = Datahelper()
  try:
    chembl = pymysql.connect(host=os.environ["CHHOST"], user=os.environ["CHUSER"],  passwd=os.environ["CHPWD"],
             port=int(os.environ["CHPORT"]), db=os.environ["CHDB"])
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()


  count = 0
  for line in sys.stdin:
    data = line.strip().split(',')
    atc_code = data[3]
    rdata = data[:4]
    query = "select level3_description from atc_classification where level3 = '%s' limit 1" % (atc_code)
    count = 0
  
    with chembl.cursor() as cursor:
      cursor.execute(query)
      for row in cursor:
        count += 1
        descr = dh.get_normalised_phrase(row[0].lower())
        rdata.append(descr)
        rdata.append(data[4])
        print ','.join(rdata)

  chembl.close()
  return count

# execution flow starts here
#
start_time = time.time()

rcount = main()
#print "END:", time.time() - start_time, "seconds", rcount
