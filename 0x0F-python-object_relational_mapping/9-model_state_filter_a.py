#!/usr/bin/python3
"""
A script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, Column, Integer, String
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
    letter = 'a'
    query_data = (
        session.query(State)
        .filter(State.name.like(f'%{letter}%'))
        .order_by(State.id)
        .all()
    )

    for state in query_data:
        print(f'{state.id}: {state.name}')

    session.close()
