#!/usr/bin/python3
"""   adds the State object “Louisiana” to the database """

from sys import argv
from sqlalchemy import create_engine, insert
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State


if __name__ == "__main__":
    password = argv[1]
    username = argv[2]
    database = argv[3]
    state = "“Louisiana”"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name=state))

    for state in session.query(State).filter(State.name == state).first():
        print('{}'.format(state.id))

    session.commit()
