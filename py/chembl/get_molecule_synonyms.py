import time
import pymysql
import os, sys
from optparse import OptionParser

def main():

  try:
    chembl = pymysql.connect(host=os.environ["CHHOST"], user=os.environ["CHUSER"],  passwd=os.environ["CHPWD"],
             port=int(os.environ["CHPORT"]), db=os.environ["CHDB"])
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()

  query = """select atc.who_name, atc.level5, matc.molregno, atc.level4_description, ms.synonyms, ms.syn_type 
  from atc_classification atc 
  LEFT JOIN molecule_atc_classification matc 
  ON atc.level5 = matc.level5 
  LEFT JOIN molecule_synonyms ms 
  ON matc.molregno = ms.molregno"""
  #query = "select atc.who_name, atc.level5, matc.molregno, atc.level4_description from atc_classification atc, molecule_atc_classification matc where atc.level5 = matc.level5"

  count = 0
  
  with chembl.cursor() as cursor:
    cursor.execute(query)
    for row in cursor:
      count += 1
      print '\t'.join([str(elem) for elem in row])

  chembl.close()

  return count


# execution flow starts here
#
start_time = time.time()

rcount = main()
#print "END:", time.time() - start_time, "seconds", rcount
