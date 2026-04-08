#!/usr/bin/python3
"""Script that lists all states starting with 'N'
    from the database hbtn_0e_0_usa."""

from sys import argv

import MySQLdb


def main():
    """Connect to MySQL and list all states whose name starts with 'N',
        sorted by id ascending."""
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    ) as connexion:
        with connexion.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            for row in cur.fetchall():
                if row[1][0] == "N":
                    print(row)


if __name__ == "__main__":
    main()
