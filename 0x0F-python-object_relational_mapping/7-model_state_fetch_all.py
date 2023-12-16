#!/usr/bin/python3
'''fetcha;;'''


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    '''fetchall'''

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    ste = session.query(State).order_by(State.id)

    for i in ste:
        print("{}: {}".format(i.id, i.name))
