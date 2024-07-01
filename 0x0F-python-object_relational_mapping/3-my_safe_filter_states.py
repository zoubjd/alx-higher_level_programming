#!/usr/bin/python3
"""  a safe script that displays all values in the states """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <username> <password> \
                <database> <state_name>")
        exit(1)
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
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'\
                    ORDER BY id ASC".format(word))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
