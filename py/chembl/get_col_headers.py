import pymysql
from optparse import OptionParser


def main(options):

  try:
    chembl = pymysql.connect(host=os.environ["CHHOST"], user=os.environ["CHUSER"],  passwd=os.environ["CHPWD"],
             port=int(os.environ["CHPORT"]), db=os.environ["CHDB"])
  except:
    print "Unexpected error:", sys.exc_info()
    exit()

  query = "show fields from %s" % (options.tablename)

  with chembl.cursor() as cursor:
    cursor.execute(query)
    colhdrs=[]
    for row in cursor:
      colhdrs.append(row[0])
    print '\t'.join(colhdrs)
  chembl.close()

# execution flow starts here
#
parser = OptionParser()
parser.add_option("-t", "--tablename", dest="tablename",
      help="Table name", metavar="STR")
(options, args) = parser.parse_args()
main(options)

