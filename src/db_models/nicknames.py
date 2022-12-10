from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class PersonNicknames(Base_nhl):
    __tablename__ = "personnicknames"

    innerId = Column('innerId', Integer, primary_key=True)
    id = Column('id', Integer, ForeignKey('person.id'))
    nickname = Column('nickname', String(50))


class TeamNicknames(Base_nhl):
    __tablename__ = "teamnicknames"

    innerId = Column('innerId', Integer, primary_key=True)
    id = Column('id', Integer, ForeignKey('team.id'))
    nickname = Column('nickname', String(50)) 
