#!/usr/bin/python3
"""
A python file that contains the class definition of a
City and an instance Base = declarative_base()
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''
        Creates table for cities
    '''
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
    name = Column(String(128), nullable=False)
