#!/usr/bin/python3
""" lists all cities from the database """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    mysql_usr = argv[1]
    mysql_pwd = argv[2]
    mysql_db = argv[3]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_usr,
                           passwd=mysql_pwd,
                           db=mysql_db)
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
