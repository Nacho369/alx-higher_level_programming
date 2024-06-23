#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    State.cities = relationship(
        "City", order_by=City.id,
        back_populates="state")

    connection = (
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    engine = create_engine(connection, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session.query(State, City)
             .filter(City.state_id == State.id)
             .all())

    for row in query:
        print(f"{row[0].name}: ({row[1].id}) {row[1].name}")
