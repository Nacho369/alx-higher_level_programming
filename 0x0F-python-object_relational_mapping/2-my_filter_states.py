#!/usr/bin/python3
"""
A script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    conn.close()
