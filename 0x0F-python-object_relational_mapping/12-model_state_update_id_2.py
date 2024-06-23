#!/usr/bin/python3
"""
A script that prints the first State
object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, desc, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    conn_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State()
    newState.name = "Louisiana"

    queryState = (
        session.query(State).filter_by(id=2).all()
    )

    for state in queryState:
        state.name = "New Mexico"

    session.add(state)
    session.commit()

    session.close()
