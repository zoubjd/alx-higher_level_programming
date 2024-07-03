#!/usr/bin/python3
""" creates the State “California” with the City “San Francisco”  """
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session

if __name__ == "__main__":
    password = argv[1]
    username = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="California"))
    session.add(City(name="San Francisco"))

    session.commit()
