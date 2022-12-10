from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class SkaterStats(Base_nhl):
    __tablename__ = "skaterStats"

    playerId = Column('playerId', Integer, ForeignKey('person.id'), primary_key=True)
    gamePk = Column('gamePk', Integer, ForeignKey('game.gamePk'), primary_key=True)
    position = Column('position', Integer)
    team = Column('team', Integer)

    timeOnIce = Column('timeOnIce', Time)
    assists = Column('assists', Integer)
    goals = Column('goals', Integer)
    shots = Column('shots', Integer)
    hits = Column('hits', Integer)
    powerPlayGoals = Column('powerPlayGoals', Integer)
    powerPlayAssists = Column('powerPlayAssists', Integer)
    penaltyMinutes = Column('penaltyMinutes', Integer)
    faceOffWins = Column('faceOffWins', Integer)
    faceoffTaken = Column('faceoffTaken', Integer)
    takeaways = Column('takeaways', Integer)
    giveaways = Column('giveaways', Integer)
    shortHandedGoals = Column('shortHandedGoals', Integer)
    shortHandedAssists = Column('shortHandedAssists', Integer)
    blocked = Column('blocked', Integer)
    plusMinus = Column('plusMinus', Integer)
    evenTimeOnIce = Column('evenTimeOnIce', Time)
    powerPlayTimeOnIce = Column('powerPlayTimeOnIce', Time)
    shortHandedTimeOnIce = Column('shortHandedTimeOnIce', Time)

    added = Column('added', DateTime, default=datetime.datetime.utcnow)
    updated = Column('updated', DateTime)
