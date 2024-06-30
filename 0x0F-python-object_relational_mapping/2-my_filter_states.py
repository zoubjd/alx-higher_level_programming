#!/usr/bin/python3
"""  displays all values where name matches the argument """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    mysql_usr = argv[1]
    mysql_pwd = argv[2]
    mysql_db = argv[3]
    word = argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_usr,
                           passwd=mysql_pwd,
                           db=mysql_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (word,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
