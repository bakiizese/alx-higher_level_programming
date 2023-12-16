#!/usr/bin/python3
'''searcch that conatain 'a'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    '''search that conatain 'a'''

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stat = State(name="Louisiana")
    session.add(stat)
    session.commit()
    print(stat.id)
