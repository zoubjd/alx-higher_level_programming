#!/usr/bin/python3
"""   changes the name of a State object from the database """

from sys import argv
from sqlalchemy import create_engine, where
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State


if __name__ == "__main__":
    password = argv[1]
    username = argv[2]
    database = argv[3]
    state = "New Mexico"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name=state))

    state = session.query(State).update({"name": "New Mexico"}).where(State.id == 2)
    print('{}'.format(state.id))

    session.commit()
