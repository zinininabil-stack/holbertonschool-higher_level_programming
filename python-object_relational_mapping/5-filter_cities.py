#!/usr/bin/python3
"""Script that lists all cities of a given state from hbtn_0e_4_usa."""

from sys import argv

import MySQLdb


def main():
    """Connect to MySQL and list all cities of a state given as argument."""
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    ) as connexion:
        with connexion.cursor() as cur:
            select = "SELECT cities.name FROM cities "
            join = "INNER JOIN states ON states.id = cities.state_id "
            where = "WHERE states.name = %s "
            order = "ORDER BY cities.id ASC"
            cur.execute(select + join + where + order, (argv[4],))
            print(", ".join(row[0] for row in cur.fetchall()))


if __name__ == "__main__":
    main()
