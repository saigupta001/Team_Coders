from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class Game(Base_nhl):
    __tablename__ = "game"

    gamePk = Column('gamePk', Integer, primary_key=True)
    gameType = Column('gameType', String(2))
    season = Column('season', String(8))
    gameDate = Column('gameDate', DateTime)

    abstractGameState = Column('abstractGameState', String(20))
    codedGameState = Column('codedGameState', Integer)
    detailedState = Column('detailedState', String(20))
    statusCode = Column('statusCode', Integer)
    startTimeTBD = Column('startTimeTBD', Boolean)

    homeTeamId = Column('homeTeamId', Integer, ForeignKey('team.id'))
    awayTeamId = Column('awayTeamId', Integer, ForeignKey('team.id'))

    added = Column('added', DateTime, default=datetime.datetime.utcnow)
    updated = Column('updated', DateTime)
