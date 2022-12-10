from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class GoalieStats(Base_nhl):
    __tablename__ = "goalieStats"

    playerId = Column('playerId', Integer, ForeignKey('person.id'), primary_key=True)
    gamePk = Column('gamePk', Integer, ForeignKey('game.gamePk'), primary_key=True)
    position = Column('position', Integer)
    team = Column('team', Integer)

    timeOnIce = Column('timeOnIce', Time)
    assists = Column('assists', Integer)
    goals = Column('goals', Integer)
    pim = Column('pim', Integer)
    shots = Column('shots', Integer)
    saves = Column('saves', Integer)
    powerPlaySaves = Column('powerPlaySaves', Integer)
    shortHandedSaves = Column('shortHandedSaves', Integer)
    evenSaves = Column('evenSaves', Integer)
    shortHandedShotsAgainst = Column('shortHandedShotsAgainst', Integer)
    evenShotsAgainst = Column('evenShotsAgainst', Integer)
    powerPlayShotsAgainst = Column('powerPlayShotsAgainst', Integer)
    decision = Column('decision', String(1))
    savePercentage = Column('savePercentage', Float)
    powerPlaySavePercentage = Column('powerPlaySavePercentage', Float)
    evenStrengthSavePercentage = Column('evenStrengthSavePercentage', Float)

    added = Column('added', DateTime, default=datetime.datetime.utcnow)
    updated = Column('updated', DateTime) 
