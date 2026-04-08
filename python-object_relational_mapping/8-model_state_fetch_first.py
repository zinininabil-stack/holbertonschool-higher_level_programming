#!/usr/bin/python3
"""Script that prints the first State object."""

import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    session = sessionmaker(bind=engine)()

    states = session.query(State).order_by(State.id).first()

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")
