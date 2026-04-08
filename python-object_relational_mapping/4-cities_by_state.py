#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa."""
from sys import argv
import MySQLdb


def main():
    """Connect to MySQL and list all cities with their state, sorted by id."""
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    ) as connexion:
        with connexion.cursor() as cur:
            select = "SELECT cities.id, cities.name, states.name FROM cities "
            join = "INNER JOIN states ON states.id = cities.state_id "
            order = "ORDER BY cities.id ASC"
            cur.execute(select + join + order)
            for row in cur.fetchall():
                print(row)


if __name__ == "__main__":
    main()
