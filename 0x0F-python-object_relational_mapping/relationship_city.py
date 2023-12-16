#!/usr/bin/python3
'''alchemy python'''


from sqlalchemy import Integer, MetaData, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''class to db'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
