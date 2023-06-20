#!/usr/bin/python3
"""
a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    output = session.query(State).filter(State.name.like(
        '%s' % (sys.argv[4], ))).first()

    if output is None:
        print("Not found")
    else:
        print(output.id)
    session.close()
