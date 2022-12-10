from db_models.base import Base_nhl
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Time, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class TeamStats(Base_nhl):
    __tablename__ = "teamStats"

    gamePk = Column('gamePk', Integer, ForeignKey('game.gamePk'), primary_key=True)
    teamId = Column('teamId', Integer, ForeignKey('team.id'), primary_key=True)
    isHome = Column('isHome', Integer)

    goals = Column('goals', Integer)
    pim = Column('pim', Integer)
    shots = Column('shots', Integer)
    powerPlayPercentage = Column('powerPlayPercentage', Float)
    powerPlayGoals = Column('powerPlayGoals', Float)
    powerPlayOpportunities = Column('powerPlayOpportunities', Float)
    faceOffWinPercentage = Column('faceOffWinPercentage', Float)
    blocked = Column('blocked', Integer)
    takeaways = Column('takeaways', Integer)
    giveaways = Column('giveaways', Integer)
    hits = Column('hits', Integer)

    goalsAgainst = Column('goalsAgainst', Integer)
    pimAgainst = Column('pimAgainst', Integer)
    shotsAgainst = Column('shotsAgainst', Integer)
    powerPlayPercentageAgainst = Column('powerPlayPercentageAgainst', Float)
    powerPlayGoalsAgainst = Column('powerPlayGoalsAgainst', Float)
    powerPlayOpportunitiesAgainst = Column('powerPlayOpportunitiesAgainst', Float)
    faceOffWinPercentageAgainst = Column('faceOffWinPercentageAgainst', Float)
    blockedAgainst = Column('blockedAgainst', Integer)
    takeawaysAgainst = Column('takeawaysAgainst', Integer)
    giveawaysAgainst = Column('giveawaysAgainst', Integer)
    hitsAgainst = Column('hitsAgainst', Integer)


    wins = Column('wins', Integer)
    losses = Column('losses', Integer)
    ot = Column('ot', Integer)
    leagueRecordType = Column('leagueRecordType', String(50))
    score = Column('score', Integer)

    added = Column('added', DateTime, default=datetime.datetime.utcnow)
    updated = Column('updated', DateTime)
