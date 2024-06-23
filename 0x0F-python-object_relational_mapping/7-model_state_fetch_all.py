#!/usr/bin/python3
"""
A script that lists all State objects
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    conn_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query_data = session.query(State).order_by(State.id)

    for state in query_data:
        print(f'{state.id}: {state.name}')

    session.close
