from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class Team(Base_nhl):
    __tablename__ = "team"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50))
    teamName = Column('teamName', String(50))

    added = Column('added', DateTime, default=datetime.datetime.utcnow)
    updated = Column('updated', DateTime)
