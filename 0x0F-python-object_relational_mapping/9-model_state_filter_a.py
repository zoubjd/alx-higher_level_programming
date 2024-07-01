#!/usr/bin/python3
"""   lists all State objects that contain the letter a """

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

    for state in session.query(State).filter(State.name.like('%a%')):
        print('{}: {}'.format(state.id, state.name))
    session.close()
