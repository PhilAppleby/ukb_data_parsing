import time
import pymysql
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def main(options):

  level = int(options.level)

  dh = Datahelper()
  try:
		chembl = pymysql.connect(host="stvus105.corpnet2.com", 
        user="chemblq", 
        passwd="starlite", 
        port=3306, 
        db="chembldb23")
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()

  print "pheno,PHENOTYPE,Category,type"

  count = 0
  for line in sys.stdin:
    data = line.strip().split(',')
    atc_code = data[0]
    query = "select level%d_description from atc_classification where level%d = '%s' limit 1" % (level, level, atc_code)
    count = 0
  
    with chembl.cursor() as cursor:
      cursor.execute(query)
      for row in cursor:
        count += 1
        pheno_string = dh.get_normalised_phrase(row[0])
        pheno_string = dh.make_pheno_string(pheno_string)
        data.append(data[0] + "_" + pheno_string)
        data.append(pheno_string)
        data.append("BINARY")
        print ','.join(data)

  chembl.close()
  return count

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
parser.add_option("-l", "--level", dest="level",
  help="ATC level", metavar="INT")
(options, args) = parser.parse_args()

rcount = main(options)
#print "END:", time.time() - start_time, "seconds", rcount
