#!/usr/bin/python3
"""
A script that deletes all State objects
with a name containing the letter a from the database
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
    char = 'a'

    queryState = (
        session.query(State)
        .filter(State.name.like(f'%{char}%'))
        .delete()
    )

    session.commit()
    session.close()
