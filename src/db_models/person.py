from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class Person(Base_nhl):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    fullName = Column('fullName', String(50))
    firstName = Column('firstName', String(50))
    lastName = Column('lastName', String(50))
    positionCode = Column('positionCode', Integer)
    weight = Column('weight',Integer)
    height = Column('height',Integer)
    shootsCatches = Column('shootsCatches',String(2))
    added = Column('added', DateTime, default=datetime.datetime.utcnow)
    updated = Column('updated', DateTime)
