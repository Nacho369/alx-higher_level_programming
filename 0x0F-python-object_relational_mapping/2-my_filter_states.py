#!/usr/bin/python3
"""
A script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    state_name_arg = argv[4]

    conn = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306
    )

    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (f'{state_name_arg}',))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
