#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        """
    )
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
