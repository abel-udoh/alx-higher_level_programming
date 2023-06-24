#!/usr/bin/python3
""" a script that changes the name of a State
    object from the database hbtn_0e_6_usa.
    it changes the name of the State where id = 2 to New Mexico
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    new_session = Session()

    newState = session.query(State).get(2)
    newState.name = "New Mexico"
    new_session.add(newState)
    new_session.commit()
    new_session.close()
