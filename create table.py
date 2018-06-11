#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
# open the connection of DB
db = MySQLdb.connect("localhost", "root", "1234", "RUNOOB", charset='utf8' )
# get the operate cursor by means of cursor() method
cursor = db.cursor()
# use the execute() method to delete the table if it is already exist
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# create the SQL sentence of table
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
sql1 = "use RUNOOB"
sql2 = "show tables"
sql3 = "desc EMPLOYEE"
cursor.execute(sql)
# sql4 = sql1 + sql2 + sql3
cursor.execute(sql1)
cursor.execute(sql2)
table =cursor.fetchall()
cursor.execute(sql3)
sheet = cursor.fetchall()
print table
print sheet
# close the DB connection
db.close()