#-*- coding: utf-8 -*-
# function: import Excel data to the MySQL database
import xlrd
import MySQLdb
# Open the workbook and define the worksheet
book = xlrd.open_workbook("E:\competition_data\data_format1\\test_format1.csv")
sheet = book.sheet_by_name("test_format1")
# create a connection with MySQL
database = MySQLdb.connect(host="localhost", user = "root", passwd = "1234", db = "RUNOOB")
# get the cursor object to iterate through the data line by line
cursor = database.cursor()
# create insert SQL sentence
query = """INSERT INTO orders (user_id, merchant_id, prob) VALUES (%s, %s, %s)"""
# create a for circulation to iterate read the lines data in the  csv file and skip the title since the second line
for r in range(1, sheet.nrows):
    user_id     = sheet.cell(r,1).value
    merchant_id = sheet.cell(r,2).value
    prob         = sheet.cell(r,3).value
    values = (user_id , merchant_id, prob)
    # execute the sql sentence
    cursor.execute(query, values)
    info = cursor.fetchall()
    print info
# close cursor
cursor.close()
# commit
database.commit()
# close the DB connection
database.close()
# print results
print ""
print "Done! "
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print "我刚导入了 " %2B columns %2B " 列 and " %2B rows %2B " 行数据到MySQL!"