#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
   takes in 3 arguments: mysql-username, mysql-password, database-name
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    new_session = Session()

    newState = State(name='Louisiana')
    new_session.add(newState)
    new_session.commit()

    state = new_session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
