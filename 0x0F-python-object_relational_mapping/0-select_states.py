#!/usr/bin/python3
"""
A Python script that list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])

    cursor = con.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    db = cursor.fetchall()

    for rows in db:
        print(rows)

    cursor.close()
    con.close()
