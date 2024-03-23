#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create the engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" and the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes
    session.commit()
