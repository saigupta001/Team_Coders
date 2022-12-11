from sqlalchemy import func, and_, or_, not_
from db_models.nhl_models import *
import traceback
import gevent.monkey
gevent.monkey.patch_all(thread=False, select=False)
import requests
import grequests
import datetime
import json
from creators.person import *
from creators.game import *
from creators.team_stats import *
from creators.team_stats import *
from creators.skater_stats import *
from creators.goalie_stats import *
from creators.team import *

def convert_string_to_time(time_sec):
    arr = time_sec.split(":")
    h = 0
    m = int(arr[0])
    s = int(arr[1])
    while m > 59:
        h += 1
        m -= 60
    return datetime.time(h, m, s)

def convert_height_string_to_int(height):
    H_feet = height.split("'")[0]
    H_inch = height.split("'")[1].split("\"")[0]
    return int(H_feet) * 12 + int(H_inch)

def remove_gamePk(session, gamePk):
    curr_game = session.query(Game).filter(Game.gamePk == gamePk).first()

    all_goalie_stats = session.query(GoalieStats).filter(GoalieStats.gamePk == curr_game.gamePk)
    for stats in all_goalie_stats:
        session.delete(stats)

    all_skater_stats = session.query(SkaterStats).filter(SkaterStats.gamePk == curr_game.gamePk)
    for stats in all_skater_stats:
        session.delete(stats)

    all_team_stats = session.query(TeamStats).filter(TeamStats.gamePk == curr_game.gamePk)
    for stats in all_team_stats:
        session.delete(stats)

    session.delete(curr_game)
    session.commit()

def add_person_nickname(nickname, name, nhl_session):
    name = name.replace("\"", "")

    ids = []

    if name.isnumeric():
        ids = nhl_session.query(Person).filter(Person.id == int(name)).all()
    else:
        ids = nhl_session.query(Person).filter(func.lower(
            Person.fullName).contains(func.lower(name))).all()

    if len(ids) > 1:
        print("More than one id for:")
        print(name)
        return
        print(nhl_session.query(Person).filter(
            func.lower(Person.fullName).contains(func.lower(name))))
        raise "More than one id..."

    if len(ids) == 0:
        print("Cant find a player with that name for:")
        print(name)
        return
        print(nhl_session.query(Person).filter(
            func.lower(Person.fullName).contains(func.lower(name))))
        raise "Cant find a player with that name..."

    if not nhl_session.query(PersonNicknames).filter(and_(PersonNicknames.id == ids[0].id, func.lower(PersonNicknames.nickname) == func.lower(nickname))).first():
        new_nickname = PersonNicknames()

        new_nickname.id = ids[0].id
        new_nickname.nickname = nickname

        nhl_session.add(new_nickname)

def add_team_nickname(nickname, name, nhl_session):
    name = name.replace("\"", "")
    ids = nhl_session.query(Team).filter(func.lower(
        Team.name).contains(func.lower(name))).all()

    if len(ids) > 1:
        print("More than one id for:")
        print(name)
        return
        raise "More than one id..."

    if len(ids) == 0:
        print("Cant find a team with that name for:")
        print(name)
        print(nhl_session.query(Team).filter(func.lower(Team.name).contains(func.lower(name))))
        return
        raise "Cant find a team with that name..."

    if not nhl_session.query(TeamNicknames).filter(and_(TeamNicknames.id == ids[0].id, func.lower(TeamNicknames.nickname) == func.lower(nickname))).first():
        new_nickname = TeamNicknames()

        new_nickname.id = ids[0].id
        new_nickname.nickname = nickname

        nhl_session.add(new_nickname)

def add_game_to_db(session, game):
    try:
        new_game = create_game(game)
        session.add(new_game)
    except Exception as e:
        print(e)
        traceback.print_exc()

def hook_factory(*factory_args, **factory_kwargs):
    def add_game_stats_to_db(res, *args, **kwargs):
        try:
            info = factory_kwargs["info"]
            session = info["session"]
            res = res.json()

            for home_or_away in ("home", "away"):
                rev_home_away = "home" if home_or_away == "away" else "away"
                team_info = res["teams"][home_or_away]
                rev_team_info = res["teams"][rev_home_away]
                new_team_stats = create_team_stats(rev_team_info,info,team_info,home_or_away)
                session.add(new_team_stats)

                for player_id in team_info["players"]:
                    player_info = team_info["players"][player_id]

                    if player_info["position"]["code"] == "G":
                        if "goalieStats" in player_info["stats"]:
                            res_goalie_stats = player_info["stats"]["goalieStats"]
                            new_goalie_stats = create_goalie_stats(player_info,info,team_info,res_goalie_stats)
                            session.add(new_goalie_stats)
                    else:
                        if "skaterStats" in player_info["stats"]:
                            res_skater_stats = player_info["stats"]["skaterStats"]
                            new_skater_stats = create_skater_stats(player_info,info,res_skater_stats,team_info)
                            session.add(new_skater_stats)
        except Exception as e:
            print(e)
            print(info["gamePk"])
            traceback.print_exc()

    return add_game_stats_to_db

def fill_all_games_from_season(session, season):
    res = requests.get('https://statsapi.web.nhl.com/api/v1/schedule?season={}'.format(season))
    res = res.json()

    base = "https://statsapi.web.nhl.com/api/v1/game/"
    urls = []

    games_that_dont_have_to_be_updated = {}
    games = session.query(Game).filter(Game.statusCode == 7)
    
    for game in games:
        games_that_dont_have_to_be_updated[game.gamePk] = game

    if "dates" in res:
        for date in res["dates"]:
            for game in date["games"]:
                if (game["gameType"] == "R" or game["gameType"] == "P") and (game["gamePk"] not in games_that_dont_have_to_be_updated.keys()):
                    if session.query(Game).filter(Game.gamePk == game["gamePk"]).first():
                        remove_gamePk(session, game["gamePk"])

                    add_game_to_db(session, game)
                    game_pk = game["gamePk"]
                    urls.append((base + str(game_pk) + "/boxscore", {   "session": session, 
                                                                        "gamePk": str(game_pk), 
                                                                        "stats" : {
                                                                            game["teams"]["home"]["team"]["id"]: {
                                                                                "wins": game["teams"]["home"]["leagueRecord"]["wins"],
                                                                                "losses": game["teams"]["home"]["leagueRecord"]["losses"],
                                                                                "ot": game["teams"]["home"]["leagueRecord"]["ot"] if "ot" in game["teams"]["home"]["leagueRecord"] else "",
                                                                                "type": game["teams"]["home"]["leagueRecord"]["type"],
                                                                                "score": game["teams"]["home"]["score"]
                                                                            },
                                                                            game["teams"]["away"]["team"]["id"]: {
                                                                                "wins": game["teams"]["away"]["leagueRecord"]["wins"],
                                                                                "losses": game["teams"]["away"]["leagueRecord"]["losses"],
                                                                                "ot": game["teams"]["away"]["leagueRecord"]["ot"] if "ot" in game["teams"]["away"]["leagueRecord"] else "",
                                                                                "type": game["teams"]["away"]["leagueRecord"]["type"],
                                                                                "score": game["teams"]["away"]["score"]
                                                                            }
                                                                        }}))

    rs = (grequests.get(u[0], hooks={'response': [hook_factory(info=u[1])]}) for u in urls)
    responses = grequests.map(rs)

def fill_teams_and_persons(session):
    res = requests.get('https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster')
    res = res.json()

    all_players_in_db = [player.id for player in session.query(Person).all()]

    for team in res["teams"]:
        if not session.query(Team).filter(Team.id == team["id"]).first():
            new_team = create_team(team)
            session.add(new_team)

        if "roster" in team:
            for player in team["roster"]["roster"]:
                details = requests.get('https://statsapi.web.nhl.com'+player["person"]["link"])
                details = details.json()
                if session.query(Person).filter(Person.id == player["person"]["id"]).first():
                    session.query(Person).filter(Person.id == player["person"]["id"]).update({
                        "fullName": player["person"]["fullName"],
                        "positionCode": player["position"]["code"],
                        "weight": details["people"][0]["weight"],
                        "shootsCatches": details["people"][0]["shootsCatches"],
                        "height": convert_height_string_to_int(details["people"][0]["height"]),
                        "updated":datetime.datetime.utcnow()})
                else:
                    new_person = create_person(player,details)
                    session.add(new_person)
