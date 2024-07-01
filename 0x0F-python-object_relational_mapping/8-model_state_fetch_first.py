#!/usr/bin/python3
"""  list the first states from the database """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State


if __name__ == "__main__":
    password = argv[1]
    username = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).filter_by(id=1):
        print('{}: {}'.format(state.id, state.name))
