#!/usr/bin/python3
"""   deletes all State objects with a name containing the letter a """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    password = argv[1]
    username = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    for City in session.query(City).order_by(City.id):
        for State in session.query(State).filter(State.id == city.state_id):
            print('{}: ({}) {}'.format(State.name, City.id, City.name))

    session.commit()
