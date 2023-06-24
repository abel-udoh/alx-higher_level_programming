#!/usr/bin/python3
"""
    a script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa.
    it takes arguments: mysql-username, mysql-password, database-name
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

    for state in new_session.query(State).filter(
            State.name.ilike('%a%')).order_by(State.id):
        new_session.delete(state)
    new_session.commit()
