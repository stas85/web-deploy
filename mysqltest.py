#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
import mysql.connector
import pymongo

cgitb.enable()
form = cgi.FieldStorage()

id = form.getvalue("users")
#id= "stas"
print ("Content-type: text/html\n\n")
print ("<html><body>")


user = id

dbmysql = ["apico_" , "apico_v2_" , "commonapi_" ]
dbmongo = ["apico_" , "smssender_"]


def func_mysqldb():
    ddd = mysql.connector.connect(host='localhost',database='mysql',user='root',password='')
    cursor = ddd.cursor()
    cursor.execute("show databases;") # select the database
    dbsmysql = []
    for (asd,) in cursor:
        dbsmysql.append(asd)
    return (dbsmysql)


def func_find_db(temp, dbs, **options):
   if options.get("status") == "not":
     for indbs in dbs:
          if indbs == temp + user:
             return ("""<font color="green"> found: """ + indbs + """</font>""")
     return ("""<font color="red">""" + "not found: " + temp + user + """</font>""")

   if options.get("status") == "status":
      for indbs in dbs:
          if indbs == temp + user:
            return (0)
      else:
            return(1)

def func_status_db(dbs):
      dic = []
      for db in dbmysql: 
         dic.append(func_find_db(db, dbs, status = "status"))
      for stat in dic:
          if int(stat) == 1:
             return ("""<font color="red"> Failed   </font>""")
      return ("""<font color="green"> OK  </font>""")


def func_mongodb():
      client = pymongo.MongoClient("localhost", 27017)
      dbs_mongo = client.database_names()
      return (dbs_mongo)

dbsmongo =  (func_mongodb())
dbsmysql =  (func_mysqldb())

##################### HTML ###################
     
print ("<p> MysqlDB = ")
print (func_status_db(dbsmysql))
#dball = []
print ("[")
for db in dbmysql: 
    print (func_find_db(db, dbsmysql, status = "not"))
    print (": ")
print ("]")
print ("</p>")



print ("<p> MongoDB = ")
print (func_status_db(dbsmongo))
#dball = []
print ("[")
for db in dbmongo:
    print (func_find_db(db, dbsmongo, status = "not"))
    print (": ")
print ("]")
print ("</p>")







print ("</body></html>")

