#!/usr/bin/python3
"""
A script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
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
    search = argv[4]

    query_data = (
        session.query(State).filter_by(name=search).first()
    )

    if query_data:
        print(f"{query_data.id}")
    else:
        print("Not found")

    session.close()
