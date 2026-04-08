#!/usr/bin/python3
"""Script that updates the name of the State with id 2 to New Mexico."""

from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )

    session = sessionmaker(bind=engine)()

    state = session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"

    session.add(state)
    session.commit()
