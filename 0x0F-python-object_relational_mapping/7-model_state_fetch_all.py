#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa"""

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
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
