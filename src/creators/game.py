def create_game(game):
    new_game = Game()
    new_game.gamePk = game["gamePk"]
    new_game.gameType = game["gameType"] if "gameType" in game else None
    new_game.season = game["season"] if "season" in game else None
    new_game.gameDate = datetime.datetime.strptime(game["gameDate"], "%Y-%m-%dT%H:%M:%SZ") if "gameDate" in game else None
    new_game.abstractGameState = game["status"]["abstractGameState"] if "status" in game and "abstractGameState" in game["status"] else None
    new_game.codedGameState = game["status"]["codedGameState"] if "status" in game and "codedGameState" in game["status"] else None
    new_game.detailedState = game["status"]["detailedState"] if "status" in game and "detailedState" in game["status"] else None
    new_game.statusCode = game["status"]["statusCode"] if "status" in game and "statusCode" in game["status"] else None
    new_game.startTimeTBD = game["status"]["startTimeTBD"] if "status" in game and "startTimeTBD" in game["status"] else None
    new_game.homeTeamId = game["teams"]["home"]["team"]["id"]
    new_game.awayTeamId = game["teams"]["away"]["team"]["id"]

    return new_game 
