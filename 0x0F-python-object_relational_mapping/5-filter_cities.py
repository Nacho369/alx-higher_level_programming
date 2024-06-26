#!/usr/bin/python3
"""
A script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8"
        )

    cursor = conn.cursor()
    query = """SELECT cities.name
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    WHERE states.name = %s"""
    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()
    vals = []

    for row in rows:
        vals.append(row[0])

    print(*vals, sep=", ")

    cursor.close()
    conn.close()
