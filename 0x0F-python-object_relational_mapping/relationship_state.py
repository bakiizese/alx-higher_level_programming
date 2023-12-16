#!/usr/bin/python3
'''alchemy python'''


from sqlalchemy import Integer, MetaData, String, Column
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City
from sqlalchemy.orm import relationship



class State(Base):
    '''class to db'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
