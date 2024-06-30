#!/usr/bin/python3
"""the first mysqlpython module"""
import sys
import MySQLdb

mysql_usr = sys.argv[1]
mysql_pwd = sys.argv[2]
mysql_db = sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_usr, passwd=mysql_pwd, db=mysql_db)
cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)
