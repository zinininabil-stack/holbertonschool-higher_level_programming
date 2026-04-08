#!/usr/bin/python3
"""Script that lists states matching a given name from hbtn_0e_0_usa."""

from sys import argv

import MySQLdb


def main():
    """Connect to MySQL and list states matching user input by id."""
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    ) as connexion:
        with connexion.cursor() as cur:
            request = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
            cur.execute(request, (argv[4],))
            for row in cur.fetchall():
                print(row)


if __name__ == "__main__":
    main()
