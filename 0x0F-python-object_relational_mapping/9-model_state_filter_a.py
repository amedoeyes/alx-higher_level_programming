#!/usr/bin/python3

"""
script that lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        print(f"{state.id}: {state.name}")
