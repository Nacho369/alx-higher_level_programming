#!/usr/bin/python3
"""
A script that lists all cities from the database
hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = conn.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
