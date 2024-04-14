#!/usr/bin/python3

"""
script that creates the State “California” with the City “San Francisco” from
the database hbtn_0e_100_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
