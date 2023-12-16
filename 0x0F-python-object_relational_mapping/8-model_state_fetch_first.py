#!/usr/bin/python3
'''fitchone'''

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    '''fitch one'''

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stats = session.query(State).order_by(State.id).first()
    if stats is None:
        print('Nothing')
    else:
        print("{}: {}".format(stats.id, stats.name))
