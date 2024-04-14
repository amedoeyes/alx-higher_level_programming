#!/usr/bin/python3

"""python file that improves model_state.py"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True,
    )
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
