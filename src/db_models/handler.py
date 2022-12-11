import sys
import glob
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import true
from db_models.nhl_models import *
from nhl_handler import *
from tqdm import tqdm
from datetime import date, datetime, timedelta
import json
import csv
import argparse

engine_nhl = create_engine('sqlite:///../db/nhl.db', echo=False)
Base_nhl.metadata.create_all(bind=engine_nhl)
Session_nhl = sessionmaker(bind=engine_nhl)

def check_year_below(value):
    ivalue = int(value)
    if ivalue < 2010:
        raise argparse.ArgumentTypeError("%s year is below 2010 no stats available for that period" % value)
    return ivalue

def check_year_above(value):
    ivalue = int(value)
    if ivalue > date.today().year:
        raise argparse.ArgumentTypeError("%s year is above %d no stats available for that period" % (value,date.today().year))
    return ivalue

def update_nhl_db(begin=None,end=None):
    global Session_nhl
    nhl_session = Session_nhl()
    fill_teams_and_persons(nhl_session)

    if begin is None and not end is None:
        return False

    if end is not None:
        if begin is None:
            begin = 2010
            
        for season in tqdm(range(begin, end)):
            fill_all_games_from_season(nhl_session, str(season) + str(season+1))
    
    if begin is not None and end is None:
        fill_all_games_from_season(end)

    nhl_session.commit()
    nhl_session.close()
    return true

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create or update nhl statistics database')
    parser.add_argument('-f','--from', help='start season', required=False, type=check_year_below)
    parser.add_argument('-t','--to', help='end season', required=False, type=check_year_above)
    args = vars(parser.parse_args())

    update_nhl_db(args['from'],args['to'])
