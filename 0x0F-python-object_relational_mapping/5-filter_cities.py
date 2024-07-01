#!/usr/bin/python3
""" lists all cities from the database with a given state """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    mysql_usr = argv[1]
    mysql_pwd = argv[2]
    mysql_db = argv[3]
    state = argv[4]
    cities = []

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_usr,
                           passwd=mysql_pwd,
                           db=mysql_db)
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name\
                    FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE BINARY states.name = '{}'\
                    ORDER BY cities.id ASC".format(state))
    rows = cursor.fetchall()
    for row in rows:
        for city in row:
            cities.append(city)
    print(", ".join(cities))
    cursor.close()
    conn.close()
