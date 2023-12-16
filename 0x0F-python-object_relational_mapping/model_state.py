#!/usr/bin/python3
'''alchemy python'''


from sqlalchemy import Integer, MetaData, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())


class State(Base):
    '''class to db'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
