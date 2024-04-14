#!/usr/bin/python3

"""script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")
