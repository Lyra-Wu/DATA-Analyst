#print "hello,world"
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
# open the connection of DB
db = MySQLdb.connect("localhost", "root", "1234", "RUNOOB", charset='utf8' )
# get the operate cursor by means of cursor() method
cursor = db.cursor()
# execute the SQL sentence by the method of execute()
cursor.execute("SELECT VERSION()")
# get a piece of data by the method of fetchone()
data = cursor.fetchone()
print "Database version : %s " % data
# close the DB connection
db.close()


