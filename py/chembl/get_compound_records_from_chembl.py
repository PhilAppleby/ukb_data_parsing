import os
import pymysql

chembl = pymysql.connect(host=os.environ["CHHOST"], user=os.environ["CHUSER"],  passwd=os.environ["CHPWD"],
     port=int(os.environ["CHPORT"]), db=os.environ["CHDB"])

with chembl.cursor() as cursor:
  sql = "show fields from chembldb23.compound_records"
  cursor.execute(sql)
  colhdrs=[]
  for row in cursor:
    colhdrs.append(row[0])

  print '\t'.join(colhdrs)

with chembl.cursor() as cursor:
  sql = "select * from chembldb23.compound_records cr"
  cursor.execute(sql)
  for row in cursor:
  	print '\t'.join([str(elem) for elem in row])

chembl.close()

